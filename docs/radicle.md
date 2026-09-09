> **Estado (2026-09-09):** guía operativa. La migración está **pendiente**: ni el repo está inicializado en Radicle ni el nodo `rad.escrivivir.co` está desplegado. Este documento es el plan y el manual; nada de lo que describe está en marcha todavía.

# Radicle: migración desde GitHub

GitHub queda **deprecated** como remoto canónico de `modelador-redes`. Seguirá recibiendo `push` mientras dure la transición (y Pages sigue publicando desde ahí), pero el original pasará a vivir en [Radicle](https://radicle.xyz).

## Qué es

Git de verdad —los mismos objetos, los mismos commits— sin servidor central. Cada nodo replica los repos vía gossip P2P y el repositorio se identifica por un **RID** criptográfico (`rad:z3gqc…`) en lugar de una URL. Issues y *patches* (el equivalente a los PR) son objetos git firmados: viajan con el repo y funcionan offline.

Lo que eso implica para este proyecto:

| | GitHub | Radicle |
| :-- | :-- | :-- |
| Identidad | cuenta en un servicio | par de claves Ed25519 propio (`did:key:z6Mk…`) |
| Repo | URL de un servidor | RID replicado por N nodos |
| Disponibilidad | la del proveedor | la de cualquier nodo que lo semille |
| PR / issues | base de datos ajena | objetos git firmados en el propio repo |

## Qué necesitas

**1. El CLI** (`rad` + `radicle-node`, Rust, sin dependencias externas):

```bash
curl -sSf https://radicle.xyz/install | sh
```

Se instala en `~/.radicle/bin`; hay que añadirlo al `PATH` (`~/.zshrc` o `~/.bash_profile`).

**2. Una identidad.** No hay registro ni cuenta: se genera un par de claves con passphrase.

```bash
rad auth --alias euler
```

Claves en `~/.radicle/keys`. La passphrase se cachea en el `ssh-agent`; para automatizar, `RAD_PASSPHRASE`.

**3. Un nodo corriendo.** Sin nodo el repo existe en local pero nadie lo ve.

```bash
rad node start            # demonio
rad node start --foreground   # para verlo trabajar
rad node status
```

## Inicializar el repo

```bash
cd modelador-redes
rad init --name modelador-redes \
         --description "Catálogo de modelizaciones políticas sobre redes distribuidas" \
         --default-branch main \
         --public
```

Devuelve el RID, añade un remote llamado `rad` y anuncia el repo a los seeds públicos. **El RID resultante hay que anotarlo aquí y en el `README.md`** — es la única dirección del repo.

`rad` convive con `origin`: es un remote más, no lo sustituye.

## Flujo de trabajo

```bash
git push rad                       # empujar la rama actual
rad sync                           # replicar con la red
rad sync --announce                # forzar anuncio
rad clone rad:z3gqc…               # lo que hace otra persona con el RID

git push rad HEAD:refs/patches     # abrir un patch (≈ PR)
rad patch list
rad issue open --title "…"
rad inspect                        # RID, delegados, estado
```

La convención de ramas del repo no cambia: una `dev/<modelo>` por modelo que solo toca su carpeta, `main` integra. Los patches se abren contra `main` igual que los PR.

## Nodo propio: `rad.escrivivir.co` — **pendiente**

Un nodo Radicle propio en el VPS `pub` (dominio `rad.escrivivir.co`) que semille los repos del Scriptorium, de modo que no dependamos ni de GitHub ni de los seeds públicos de terceros. Corre en Docker: `radicle-node` (P2P, `8776/tcp`), `radicle-httpd` (API + git por HTTPS) y Radicle Explorer (navegación web), los dos últimos detrás del Caddy del host. Política de seeding `block`: solo replica lo que se autoriza con `rad seed`.

**Despliegue:** guía paso a paso para el agente del VPS en [`vps-rad-node.md`](vps-rad-node.md).

Lo que falta por hacer:

- [ ] Desplegar el nodo siguiendo `vps-rad-node.md` (§§2–9) y abrir `8776/tcp`.
- [ ] Anotar aquí lo que devuelva el agente (§12 de la guía): `NID`, seed address `<NID>@rad.escrivivir.co:8776`.
- [ ] `rad init` de este repo (arriba) y anotar el RID.
- [ ] Semillar desde el nodo: `rad seed <RID> --scope all` + alias `modelador-redes` en httpd (§10 de la guía).
- [ ] En el portátil, apuntar al nodo propio y anunciar:
  ```bash
  rad config push preferredSeeds '"<NID>@rad.escrivivir.co:8776"'       # los valores son JSON: las comillas dobles van dentro
  rad config set publicExplorer '"https://rad.escrivivir.co/nodes/$host/$rid$path"'
  rad node connect <NID>@rad.escrivivir.co:8776
  rad sync --announce
  ```
- [ ] Decidir qué pasa con Pages (hoy depende de `.github/workflows/pages.yml`, que es GitHub-only): mantener Pages como espejo o publicar `public/` desde el VPS. El explorer del nodo navega el repo, no sustituye a la web del proyecto.
- [ ] Actualizar `README.md`, `CITATION.cff` y `llms.md` con el RID y el seed.

Hasta que eso exista, `rad init` anuncia contra los bootstrap públicos del equipo de Radicle y el repo se puede explorar en `radicle.network`.

Registro (rellenar cuando el agente entregue):

```
NID:            —
Seed address:   —@rad.escrivivir.co:8776
RID:            —
```

## Mientras tanto

`origin` (GitHub) sigue siendo el remoto que publica la web. No se borra nada hasta que el nodo esté arriba, el RID anotado y `git clone https://rad.escrivivir.co/modelador-redes.git` funcione.
