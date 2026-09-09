> **Estado (2026-09-09):** guía operativa para el agente que administra el VPS `pub`. **Pendiente de ejecutar.** Versiones verificadas contra `files.radicle.dev` y el código fuente de heartwood / radicle-explorer en esta fecha: radicle **1.10.3**, radicle-httpd **0.28.0**, radicle-explorer commit `fb11e4d9`.

# Nodo Radicle en `pub` → `rad.escrivivir.co`

Eres el agente que opera el VPS `pub`. Tu tarea: levantar un **nodo Radicle** propio, en Docker, que semille los repos del Scriptorium y los exponga por web en `https://rad.escrivivir.co`. Esta guía es autocontenida: no necesitas nada más que el VPS y los datos de la tabla de §1. Ejecuta las secciones en orden; cada una termina con una comprobación. Si una comprobación falla, para y repórtalo; no improvises alrededor.

## 0. Qué vas a montar

| Pieza | Qué es | Dónde escucha | Quién la ve |
| :-- | :-- | :-- | :-- |
| `radicle-node` | El nodo P2P: replica repos con la red por gossip, firma con la identidad del nodo | `0.0.0.0:8776` (TCP plano) | Internet (otros nodos) |
| `radicle-httpd` | API JSON + git smart-HTTP sobre el storage del nodo | `127.0.0.1:8080` | Solo Caddy |
| Radicle Explorer | SPA estática (Svelte) que navega la API | ficheros en `/var/www/rad.escrivivir.co` | Caddy los sirve |
| Caddy (host, systemd, ya existe) | TLS + enrutado: `/api/*`, `/raw/*`, `*.git` → httpd; el resto → explorer | `:80`/`:443` | Internet |

El puerto **8776 no pasa por Caddy** (no es HTTP). El 8080 **nunca** se expone fuera del loopback.

Al terminar devolverás el NID del nodo, su dirección externa, la ruta de datos y el resultado de cada check de §11.

## 1. Entradas

| Placeholder | Qué es | Cómo lo obtienes |
| :-- | :-- | :-- |
| `<DATA>` | Punto de montaje del volumen de datos de 40 GB | §2 (`df -h`, `lsblk`) |
| `<IP>` | IP pública del VPS (y la IPv6 si tiene) | `curl -4 ifconfig.me`, `curl -6 ifconfig.me` |
| `<NID>` | Node ID del nodo (`z6Mk…`) | Se genera en §6; lo anotas tú |
| `<RID>` | ID Radicle de `modelador-redes` (`rad:z…`) | **Lo pasa el usuario. Puede no existir aún.** Todo lo demás se monta igual; §10 se hace cuando llegue |
| Passphrase | Cifra la clave del nodo | Se genera en el VPS en §6. No la pidas, no la reportes |

## 2. Diagnóstico previo (solo lectura)

```bash
docker --version && docker compose version          # necesitas compose v2 (`docker compose`, no `docker-compose`)
df -h && lsblk                                      # identifica <DATA>: el volumen de 40 GB
docker info 2>/dev/null | grep 'Docker Root Dir'    # debe estar en el volumen de sistema, no en <DATA>
systemctl status caddy --no-pager | head -5         # Caddy en el host, activo
grep -nE '^\s*import|escrivivir' /etc/caddy/Caddyfile   # cómo se añaden sitios: ¿`import sites/*`? ¿bloques en el propio Caddyfile?
ls /etc/caddy/                                      # directorio de sitios importados, si lo hay
id caddy                                            # usuario con el que corre Caddy (leerá el build del explorer)
ss -tlnp | grep -E ':8776|:8080' || echo "8776 y 8080 libres"
ufw status 2>/dev/null; nft list ruleset 2>/dev/null | head -40   # qué firewall hay
```

Anota: `<DATA>`, el mecanismo de sitios de Caddy (fichero importado por glob **o** bloque en el Caddyfile), el usuario de Caddy y el firewall. Si `docker compose` no existe o Caddy no corre en el host, para y repórtalo.

## 3. Layout

```
/opt/radicle/                        # volumen de sistema: solo definiciones (KB)
├── compose.yml
├── .env                             # DATA=… y RAD_PASSPHRASE=…   chmod 600
├── Dockerfile                       # imagen `radicle`: rad + radicle-node + git-remote-rad + radicle-httpd
└── explorer/
    ├── Dockerfile                   # build multi-stage de Radicle Explorer
    └── local.json                   # config del explorer apuntando a nuestro nodo
<DATA>/radicle/home/                 # RAD_HOME del nodo: keys/, storage/, node/, config.json  (esto es lo que crece)
/var/www/rad.escrivivir.co/          # build estático del explorer, lo lee Caddy
```

```bash
sudo mkdir -p /opt/radicle/explorer <DATA>/radicle/home /var/www/rad.escrivivir.co
sudo chown 1000:1000 <DATA>/radicle/home       # el contenedor corre como uid 1000
```

## 4. Imagen `radicle`

No hay imagen oficial. Se construye sobre Alpine con los binarios estáticos (musl) que publica Radicle, verificando el SHA-256. Un solo Dockerfile sirve para el nodo, el httpd y los comandos `rad`.

`/opt/radicle/Dockerfile`:

```dockerfile
FROM alpine:3.22

ARG RADICLE_VERSION=1.10.3
ARG HTTPD_VERSION=0.28.0
ARG TARGET=x86_64-unknown-linux-musl

# git >= 2.34 es requisito de Radicle; xz para los tarballs.
RUN apk add --no-cache git ca-certificates curl xz

RUN set -eu; cd /tmp; \
    R="radicle-${RADICLE_VERSION}-${TARGET}"; \
    H="radicle-httpd-${HTTPD_VERSION}-${TARGET}"; \
    curl -fsSLO "https://files.radicle.dev/releases/${RADICLE_VERSION}/${R}.tar.xz"; \
    curl -fsSLO "https://files.radicle.dev/releases/${RADICLE_VERSION}/${R}.tar.xz.sha256"; \
    curl -fsSLO "https://files.radicle.dev/releases/radicle-httpd/${HTTPD_VERSION}/${H}.tar.xz"; \
    curl -fsSLO "https://files.radicle.dev/releases/radicle-httpd/${HTTPD_VERSION}/${H}.tar.xz.sha256"; \
    sha256sum -c "${R}.tar.xz.sha256" "${H}.tar.xz.sha256"; \
    tar -xJf "${R}.tar.xz" --strip-components=2 -C /usr/local/bin "${R}/bin/"; \
    tar -xJf "${H}.tar.xz" --strip-components=2 -C /usr/local/bin "${H}/bin/"; \
    rm -f /tmp/*.tar.xz /tmp/*.sha256; \
    rad --version && radicle-node --version && radicle-httpd --version

RUN addgroup -g 1000 radicle && adduser -D -u 1000 -G radicle radicle
ENV RAD_HOME=/home/radicle/.radicle
USER radicle
WORKDIR /home/radicle
```

Si el VPS es ARM: `--build-arg TARGET=aarch64-unknown-linux-musl`. El sha256 esperado de `radicle-1.10.3-x86_64-unknown-linux-musl.tar.xz` es `3d78e3ffc17f9e6eca7fcd3acc439f2252060532eb457cf17f2747fed4cc6751`; si `sha256sum -c` falla, **no** sigas.

## 5. `compose.yml`

`/opt/radicle/compose.yml`:

```yaml
x-radicle: &radicle
  build: .
  image: scriptorium/radicle:1.10.3
  restart: unless-stopped
  init: true
  volumes:
    - ${DATA}/radicle/home:/home/radicle/.radicle

services:
  node:
    <<: *radicle
    container_name: radicle-node
    command: ["radicle-node", "--listen", "0.0.0.0:8776", "--force"]
    env_file: .env                # RAD_PASSPHRASE: el nodo descifra la clave al arrancar
    ports:
      - "8776:8776"
    stop_grace_period: 30s
    mem_limit: 2g

  httpd:
    <<: *radicle
    container_name: radicle-httpd
    # Cuando exista <RID>, añade: "--alias", "modelador-redes", "<RID>"
    command: ["radicle-httpd", "--listen", "0.0.0.0:8080"]
    ports:
      - "127.0.0.1:8080:8080"     # solo loopback: lo consume Caddy
    depends_on:
      - node
```

`--force` arranca aunque quede un control socket huérfano de un apagado sucio (es lo que hace el unit de systemd oficial). `httpd` no necesita la passphrase: lee el storage y habla con el nodo por el socket de control que comparten en el volumen.

## 6. Identidad y `config.json` (una sola vez)

```bash
cd /opt/radicle
umask 077
printf 'DATA=%s\nRAD_PASSPHRASE=%s\n' "<DATA>" "$(openssl rand -base64 32)" > .env
chmod 600 .env
docker compose build

# Crea el par de claves Ed25519 del nodo (identidad = NID). Passphrase por stdin, sin prompt.
docker compose run --rm -T node sh -c 'printf "%s" "$RAD_PASSPHRASE" | rad auth --alias rad.escrivivir.co --stdin'
docker compose run --rm node rad self
```

`rad self` imprime `Node ID` (`z6Mk…`): ese es `<NID>`. Anótalo. (Si `rad auth` avisa de que no puede registrar la clave en `ssh-agent`, es normal: no hay agente en el contenedor y no hace falta.)

`rad auth` deja un `config.json` mínimo. Sobrescríbelo con este (`<DATA>/radicle/home/config.json`, propietario 1000:1000):

```json
{
  "publicExplorer": "https://rad.escrivivir.co/nodes/$host/$rid$path",
  "preferredSeeds": [],
  "web": {
    "name": "rad.escrivivir.co",
    "description": "Nodo Radicle del Scriptorium",
    "pinned": { "repositories": [] }
  },
  "cli": { "hints": true },
  "node": {
    "alias": "rad.escrivivir.co",
    "listen": ["0.0.0.0:8776"],
    "externalAddresses": ["rad.escrivivir.co:8776"],
    "connect": [
      "z6Mkmqogy2qEM2ummccUthFEaaHvyYmYBYh3dbe9W4ebScxo@rosa.radicle.network:58776",
      "z6MkrLMMsiPWUcNPHcRajuMi9mDfYckSoJyPwwnknocNYPm7@iris.radicle.network:58776",
      "z6MksmpU5b1dS7oaqF2bHXhQi1DWy2hB7Mh9CuN7y1DN6QSz@seed.radicle.dev:58776"
    ],
    "peers": { "type": "dynamic" },
    "relay": "auto",
    "network": "main",
    "log": "INFO",
    "workers": 8,
    "seedingPolicy": { "default": "block" }
  }
}
```

Claves que importan:

- `externalAddresses`: lo que el nodo anuncia a la red. Tiene que resolver a `<IP>` (§9) y tener 8776 abierto (§7).
- `connect`: los tres nodos públicos del equipo de Radicle, para que el nuestro entre en la red. Ojo: ellos escuchan en **58776**, nosotros en 8776.
- `seedingPolicy.default = block`: **no replica nada que no se haya autorizado con `rad seed`**. Con 40 GB no queremos ser espejo del mundo. `web.pinned.repositories` y el `--alias` del httpd se rellenan en §10 con `<RID>`.

Comprobación:

```bash
docker compose run --rm node rad config        # imprime la config sin error
python3 -m json.tool <DATA>/radicle/home/config.json > /dev/null && echo JSON OK
```

## 7. Arranque y firewall

```bash
cd /opt/radicle && docker compose up -d
docker compose logs -f node        # espera a ver conexiones establecidas con rosa/iris/seed.radicle.dev; Ctrl-C
docker compose exec node rad node status
```

Abre **8776/tcp** entrante. Docker ya inserta la regla en iptables al publicar el puerto, pero el firewall del proveedor (panel del VPS / security group) y `ufw` pueden bloquearlo igualmente:

```bash
sudo ufw allow 8776/tcp comment radicle-node      # si hay ufw
```

Comprobación (desde **fuera** del VPS, p. ej. tu portátil): `nc -vz <IP> 8776` → `succeeded`.

## 8. Radicle Explorer

Es una SPA estática. Se compila una vez en Docker (Node 24) y el resultado se exporta al host para que lo sirva Caddy; no queda ningún contenedor corriendo. Sin releases etiquetadas: se fija el commit.

`/opt/radicle/explorer/local.json` — el explorer se configura para ser la portada de **nuestro** nodo:

```json
{
  "nodes": { "homepage": "node" },
  "preferredSeeds": [
    { "hostname": "rad.escrivivir.co", "port": 443, "scheme": "https" }
  ]
}
```

`/opt/radicle/explorer/Dockerfile`:

```dockerfile
FROM node:24-bookworm AS build
ARG EXPLORER_COMMIT=fb11e4d9c2c758468b9dca5c615f2392fb011c6e
WORKDIR /src
# Origen canónico: el propio seed de Radicle. Espejo: https://github.com/radicle-dev/radicle-explorer.git
RUN git clone https://seed.radicle.dev/z4V1sjrXqjvFdnCUbxPFqd5p4DtH5.git . \
 && git checkout --detach "${EXPLORER_COMMIT}"
COPY local.json config/local.json
RUN npm ci && npm run build

FROM scratch AS out
COPY --from=build /src/build /
```

```bash
cd /opt/radicle/explorer
docker build --target out -o /var/www/rad.escrivivir.co .
sudo chown -R <USUARIO_CADDY>:<USUARIO_CADDY> /var/www/rad.escrivivir.co     # el que dio `id caddy` en §2
ls /var/www/rad.escrivivir.co/index.html
```

Si el build falla (npm, red, versión de Node): **plan B** = servir solo la API. Omite el `handle` del explorer en §9 y navega el nodo desde `https://radicle.network/nodes/rad.escrivivir.co`. Repórtalo como pendiente.

## 9. DNS + Caddy

**DNS**, donde gestionen `escrivivir.co`: registro `A` `rad.escrivivir.co → <IP>` (y `AAAA` si el VPS tiene IPv6). Espera a que `dig +short rad.escrivivir.co` devuelva `<IP>` antes de tocar Caddy: si Caddy intenta emitir el certificado antes de que el DNS apunte aquí, ACME falla y aplica backoff.

**Caddy**: añade este bloque por el mecanismo que descubriste en §2 (fichero nuevo en el directorio importado, p. ej. `/etc/caddy/sites/rad.escrivivir.co.caddy`, o bloque al final del Caddyfile):

```caddyfile
rad.escrivivir.co {
    encode zstd gzip

    # API JSON, ficheros crudos y git smart-HTTP → radicle-httpd
    @httpd path /api/* /raw/* /*.git /*.git/*
    handle @httpd {
        reverse_proxy 127.0.0.1:8080
    }

    # Todo lo demás → Radicle Explorer (SPA)
    handle {
        root * /var/www/rad.escrivivir.co
        try_files {path} /index.html
        file_server
    }
}
```

```bash
sudo caddy validate --config /etc/caddy/Caddyfile && sudo systemctl reload caddy
```

El certificado lo emite Caddy solo (ACME) en la primera petición; puede tardar unos segundos.

## 10. Semillar `modelador-redes` (cuando el usuario te pase `<RID>`)

Con `seedingPolicy = block`, el nodo **rechaza** todo repo que no esté autorizado explícitamente:

```bash
cd /opt/radicle
docker compose exec node rad seed <RID> --scope all --no-fetch
```

(`--scope all` = replicar las ramas de todos los colaboradores, no solo de los delegados; `--no-fetch` porque aún no hay de quién traerlo: el portátil del usuario lo anunciará después.)

Luego:

1. En `config.json`, `web.pinned.repositories: ["<RID>"]`.
2. En `compose.yml`, `httpd.command`: `["radicle-httpd", "--listen", "0.0.0.0:8080", "--alias", "modelador-redes", "<RID>"]` → permite `git clone https://rad.escrivivir.co/modelador-redes.git` y URLs del explorer por nombre.
3. `docker compose up -d` (recrea `httpd`; `node` relee config al reiniciar: `docker compose restart node`).

El contenido llega cuando el portátil del usuario se conecta y anuncia (`rad node connect <NID>@rad.escrivivir.co:8776` + `rad sync --announce`, documentado en [`radicle.md`](radicle.md)). Verás el fetch en `docker compose logs -f node`.

## 11. Verificación

| Comando | Esperado |
| :-- | :-- |
| `docker compose exec node rad node status` | `running`; sesiones con rosa/iris/seed.radicle.dev |
| `curl -s https://rad.escrivivir.co/api/v1` | JSON con `"service":"radicle-httpd"` y `"nid":"<NID>"` |
| `curl -s https://rad.escrivivir.co/api/v1/node \| jq .config.externalAddresses` | `["rad.escrivivir.co:8776"]` |
| `curl -sI https://rad.escrivivir.co/ \| head -3` | `200`, `content-type: text/html` (el explorer, **no** el JSON de httpd) |
| Navegador: `https://rad.escrivivir.co/` | Vista del nodo `rad.escrivivir.co`, sin errores de API |
| Navegador: `https://radicle.network/nodes/rad.escrivivir.co` | Carga el nodo (prueba 443 + CORS) |
| Desde fuera: `nc -vz rad.escrivivir.co 8776` | `succeeded` |
| Tras §10: `curl -s https://rad.escrivivir.co/api/v1/repos \| jq '.[].rid'` | Incluye `<RID>` |
| Tras §10 y el announce del portátil: `git clone https://rad.escrivivir.co/modelador-redes.git /tmp/t && ls /tmp/t/README.md` | Clona |

## 12. Lo que devuelves

Un bloque así, listo para pegar en `docs/radicle.md` del repo:

```
NID:                <NID>
Seed address:       <NID>@rad.escrivivir.co:8776
Web / API:          https://rad.escrivivir.co  (httpd 0.28.0, explorer fb11e4d9)
Imagen:             scriptorium/radicle:1.10.3
RAD_HOME en host:   <DATA>/radicle/home
Caddy:              <ruta del fichero/bloque añadido>
Firewall:           8776/tcp abierto en <ufw|nft|panel>
Checks §11:         <uno por línea: OK / FALLA + salida>
Pendiente:          <p. ej. "§10: sin RID todavía", "explorer: plan B">
```

Sin la passphrase, sin el contenido de `.env`, sin las claves.

## 13. Operación

| Qué | Cómo |
| :-- | :-- |
| Logs | `docker compose logs -f node` · `docker compose exec node rad node logs` |
| Reiniciar | `docker compose restart node` (httpd sobrevive; tarda ~30 s en volver a conectar peers) |
| Actualizar Radicle | cambia `ARG RADICLE_VERSION` / `HTTPD_VERSION` en el Dockerfile y el tag `image:` → `docker compose build --pull && docker compose up -d` |
| Actualizar explorer | cambia `EXPLORER_COMMIT` → repite §8 |
| Disco | `du -sh <DATA>/radicle/home/storage` · `docker compose exec node rad node inventory` · quitar un repo: `rad unseed <RID>` |
| Añadir otro repo del Scriptorium | §10 con su RID |
| **Backup** | `<DATA>/radicle/home/keys/{radicle,radicle.pub}` + `/opt/radicle/.env`, cifrados y **fuera** del VPS. Perder la clave = perder el NID (hay que re-anunciar todo con una identidad nueva). El `storage/` no hace falta: se rehace desde la red |

**No hagas:** `seedingPolicy.default = allow` (llenaría los 40 GB con repos ajenos) · publicar 8080 fuera del loopback · borrar `keys/` · correr el nodo como root.
