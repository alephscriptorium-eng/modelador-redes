# Vendorizar el ecosistema FairCoop, borrar las marcas «muerto / 0 / no hay nada» y cerrar TK-C00

## Context

El agente anterior recibió `vendor/plan.md` (commit `162cc60`, "sin ejecutar": manifiesto `vendor.json` + `scripts/vendor.sh` + generalizar la reescritura de enlaces) y en vez de ejecutarlo dejó por todo el repo la tesis «Faircoin está muerto, no hay nada que vendorizar, Oasis lo cubre todo». El usuario ha clonado a mano los 12 repos en `vendor/` y **todos los SHA coinciden exactamente con los pines del plan** (verificado con `git rev-parse HEAD` en cada clon). Los ficheros que el plan quiere citar existen (`faircoin/src/poc.cpp`, `chainparams.cpp`, `fairchains/src/fairchains-tool.cpp`, `doc/on-proof-of-cooperation.md`, `doc/CVN-operators-guide.md`, `doc/fasito-*.md`).

Decisiones del usuario en esta sesión:
- Alcance: **main + draftv3 en `dev/res_publica`** (cierra TK-C00 citando `vendor/faircoin` fichero:línea). Las demás ramas quedan para más adelante.
- El hecho «`faircoin/faircoin`: último commit 2022-02-05» (el clon lo confirma) **se conserva como dato, sin adjetivo**. Se eliminan «muerto», «cero líneas auditadas», «no es un sustrato vivo», «no se vendoriza» y similares en `main`.
- Los drafts anteriores **no se reescriben** (regla del repo): la marca de `draftv0 #2` («La capa Faircoin está muerta») se corrige en el draftv3.

Estado del árbol: `main` limpio salvo `README.md` (sin §Oasis) y `THIRD_PARTY.md` (línea suelta `vendor/plan.md`, sin instrucciones de clonado) — ambos ficheros se reescriben enteros en la fase A, así que esos cambios quedan absorbidos.

Gotcha: `vendor/plan.md` está **trackeado a la fuerza dentro de un directorio ignorado** (`git ls-files vendor` lo lista). Se mueve a `docs/plan-vendor.md` (histórico, como `docs/plan-web.md`) para que `git ls-files | grep vendor` vuelva a estar vacío.

---

## Fase A · Infraestructura en `main`

### A1. `vendor.json` (raíz, nuevo) — única fuente de verdad

Lista `vendor` con 12 entradas `{id, repo, sha, fecha, licencia, por_defecto, proposito}`. Datos: tabla "Se vendoriza" de `vendor/plan.md` §Inventario (SHA ya verificados en disco). **Verificar la licencia leyendo el fichero de cada clon** al escribirla: `faircoin/COPYING`, `fairchains/COPYING`, `fasito/COPYING`, `faircoin2-cce/COPYING`, `electrumfair/LICENCE`, `electrumfairx/LICENCE`, `faircoin-exporter/LICENSE`, `faircoin-nrp/LICENSE`, `valuenetwork/LICENSE`, `oasis/LICENSE`; `faircoin-seeder` y `coopshares` **no tienen fichero de licencia** → `"sin licencia"` (solo lectura).

### A2. `scripts/vendor.sh` (nuevo, `chmod +x`)

Tal como lo especifica `vendor/plan.md` §2: bash + git + python3 (lee el JSON, sin jq); modos por defecto / `--check` / `--only id…` / `--all` / `--list`. Por entrada: si `vendor/<id>/.git` existe → `rev-parse HEAD` == sha (si no, «DERIVA», exit 1; **nunca toca un clon existente**); si no existe → `git init` + `remote add` + `fetch --depth 1 origin <sha>` + `checkout FETCH_HEAD`, con fallback a fetch completo. `set -euo pipefail`, rutas desde `$(dirname "$0")/..`. Como los 12 clones ya están, la primera ejecución real es `--check` y debe dar 12 OK.

### A3. Generalizar la reescritura de enlaces

- `modelador_redes/vendor.py` (nuevo): dataclass `Entrada` + `cargar_manifiesto(path=None) -> dict[str, Entrada]`. `paths.py` gana `VENDOR_JSON = PROJECT_ROOT / "vendor.json"`; `OASIS_*` se quedan (sin I/O en `paths.py`).
- `modelador_redes/modelos/enlaces.py`: `VENDOR_RE = r"\]\((?:base/teoria/)?vendor/([a-z0-9-]+)/?([^)#\s]*)(#L\d+(?:-L?\d+)?)?\)"` y `reescribir_vendor(md, repos=None)` (id → `blob/<sha>` fichero, `tree/<sha>` dir; id desconocido intacto). `reescribir_oasis` queda como wrapper (tests actuales intactos). `reescribir_para_web` / `reescribir_para_zip` usan `reescribir_vendor`. `reescribir_inline_code` ya es genérico.
- `modelador_redes/cli/check.py`: `validar_manifiesto()` (JSON parsea, ids únicos `^[a-z0-9-]+$`, sha 40 hex, repo https, `oasis` presente con sha == `OASIS_SHA`). No exige que `vendor/` exista.
- `modelador_redes/cli/build.py`: `_ctx` añade `vendor` (lista de entradas); `catalogo.json` conserva `oasis` y añade `vendor: [...]`.
- `modelador_redes/site/packs.py:53-54`: texto del README del zip genérico («Los enlaces a código de terceros apuntan a los commits fijados en `vendor.json` (Oasis @ …). Ningún código de terceros se incluye en este paquete.»).
- `site/templates/foss/tecnico.html`: §Oasis → §Vendor: párrafo + tabla desde `vendor` (id · repo `tree/<sha>` · fecha · licencia · propósito); fila de `enlaces.py` en la tabla de módulos: «rutas `vendor/<id>/…` → blob/tree al SHA fijado».

### A4. Borrar las marcas y documentar (todo en `main`)

- `THIRD_PARTY.md`: reescribir. Tabla "Se vendoriza" (12 filas, mismos datos que el manifiesto) + "Documentado, no vendorizado" (FairMarket/Odoo, BotC sobre Cyclos, OCE, Komun, `visbtc/fair-coin`, `jaromil/faircoin2`; **aviso FairCoinOfficial = otra moneda**, relevante para TK-80) + dependencias PyPI + comando `scripts/vendor.sh`. Quita «Solo documentado; no se vendoriza» y la línea suelta `vendor/plan.md`.
- `README.md`: §Vendor (dos líneas + `scripts/vendor.sh`), en el hueco donde estaba §Oasis.
- `llms.md`: L15 «Vive en `vendor/oasis`…» → «Todo el código de terceros citable está en `vendor.json` y se clona con `scripts/vendor.sh` (ver `THIRD_PARTY.md`)»; L152 «(80 MB, AGPL)» → «(~190 MB, licencias varias)»; **L156 «No vendorizar Faircoin ni ningún código de terceros» → «Solo se vendoriza lo que está en `vendor.json`, con `scripts/vendor.sh`; nunca se commitea»**; convención de cita `vendor/<id>/ruta#Lx-Ly` para cualquier id; estructura (+`vendor.json`, `scripts/vendor.sh`, `vendor.py`, `docs/plan-vendor.md`); checklist (+`scripts/vendor.sh --check`). L14 («No hay fork de Oasis, no hay cadena Faircoin3») se conserva: es alcance, no marca.
- `docs/informe-tutoria-plasticidad.md`: ficha «FairCoop: inventariado (12 repos) y *no* auditado» → «vendorizado (12 repos, `vendor.json`), pendiente de auditar»; L19 «del ecosistema FairCoop hay cero líneas auditadas» → «el ecosistema FairCoop está vendorizado y aún sin auditar; `faircoin/faircoin` no recibe commits desde 2022-02-05 (verificado en el clon)»; L294 «inventariado y muerto desde 2022» → «vendorizado y sin commits desde 2022-02-05». Sin más cambios.
- `git mv vendor/plan.md docs/plan-vendor.md` + nota de cabecera «ejecutado el 2026-09-10».
- `CHANGELOG.md` 0.3.0 + `pyproject.toml` version 0.3.0 + `__version__` (donde viva; `build.py` lo importa).

### A5. Tests

- `tests/test_vendor.py`: manifiesto real carga, 12 ids únicos, sha hex, `oasis` == `OASIS_SHA`; cada id del manifiesto aparece en `THIRD_PARTY.md`; `reescribir_vendor` con id `faircoin` (fichero, dir, ancla `-38`→`-L38`, fence intacto), id desconocido intacto, prefijo `base/teoria/` aceptado; `validar_manifiesto` sobre un JSON roto en `tmp_path`.
- Test del script sobre un repo git local en `tmp_path` (`subprocess`): `--check` exit 1 si falta; 0 tras clonar; 1 tras mover HEAD.
- `tests/test_enlaces.py` sin cambios (siguen verdes).

---

## Fase B · `draftv3` en `dev/res_publica`

Orden: **después de A** (los enlaces `vendor/faircoin/...` solo se reescriben con A3 y `modelador check` los cazaría como rotos).

`git checkout dev/res_publica` → crear `modelos/res_publica/drafts/draftv3.md` → `.venv/bin/modelador indice --modelo res_publica` → editar `revision/00-indice.md` (la línea «Draft vigente» la escribe el comando; añadir nota «draftv3: carril C citado sobre `vendor/faircoin`, TK-C00 cerrada» y cambiar «Tabla 1 de draftv1 en limpio (draftv3)» → «(draftv4)», porque ese sufijo queda usado). Solo se toca `modelos/res_publica/`.

Contenido de `draftv3.md` («Carril C sobre el código: Faircoin citado fichero:línea»):

0. **Qué cambia respecto a draftv2** — tabla numerada (`| # | … |`, no la extrae el backlog): TK-C00 resuelta (`vendor/faircoin` @ `8e9b8f5`, más `fairchains`, `fasito`, `electrumfair`, `valuenetwork`, `faircoin-nrp`…); corrección de `draftv0 #2` y `draftv0 L258` («La capa Faircoin está muerta», «☠️»): el hecho es «sin commits desde 2022-02-05, código completo, MIT, citable»; OP-02 (TK-07…12) no queda inoperativa por «muerte» sino sustituida por la decisión de génesis nuevo de draftv2; la viñeta de hechos técnicos de `draftv2 L24` pasa a citas verificadas.
1. **Hechos verificados en código** (cada uno con `[fichero:Lx](vendor/faircoin/src/...#Lx-Ly)`; **releer cada línea al escribir**, los números de abajo son los localizados hoy):
   - PoC: `CheckProofOfCooperation` `poc.cpp#L944`, `CheckNextBlockCreator` `#L1209`, `CvnVerifyChainSignature` `#L525`, `CheckAdminSignature(…, fCoinSupply)` `#L698`, `UpdateChainParameters` `#L915`, `SetCoinSupplyStatus` `#L902`, `UpdateChainAdmins` `#L882`.
   - Génesis hardcodeado: `chainparams.cpp#L89-L96` (dynParams mainnet), `#L109-L110` (`vChainAdmins[0]` con pubkey literal; idem testnet `#L194-L195`, regtest `#L279-L280`); validación `#L351-L387`.
   - Clave del CVN: `init.cpp#L1118-L1131` (`-cvn=fasito|file`), `poc.cpp#L67`, `#L2030`, `#L2302`; firmware en `vendor/fasito/`.
   - RPC admin: `rpc/cvn.cpp` `getactivecvns #L59`, `getactiveadmins #L113`, `addcvn #L820`, `removecvn #L913`, `fasito #L1116`, `bancvn #L1185`, `setchainparameters #L1219`; `rpc/client.cpp#L100-L105` (`addcoinsupply`).
   - Génesis nuevo sin recompilar: `vendor/fairchains/src/fairchains-tool.cpp#L253-L254` (ids), `#L308-L313` (`CreateGenesisBlock` + `vCvns`/`vChainAdmins` desde JSON), `#L357`.
   - Doctrina del proyecto original: `doc/on-proof-of-cooperation.md` (§Who's next `#L19`, §Fasito `#L37`), `doc/CVN-operators-guide.md` §4.1 criterios socio-políticos `#L101`, §4.5 removal `#L128`.
2. **Carril C revisado** — tabla con el formato del carril G (`| ID | Tarea | Depende | Seam | T | P |`, para que `backlog.py` la extraiga): TK-C00 cerrada; nuevas TK-C01…C06 con seam fichero:línea: C01 `addcvn/removecvn/bancvn` ↔ TK-49 (admin = Presidencia, G06); C02 `setchainparameters` como ley (TK-84, `UpdateChainParameters`); C03 `addcoinsupply` ↔ TK-48 (emisión al tesoro por ley, `CheckAdminSignature(fCoinSupply)`); C04 génesis con `fairchains-tool` (JSON) frente a recompilar `chainparams.cpp`; C05 `-cvn=file` frente a Fasito (custodia, TK-82); C06 criterios de certificación de CVN (guide §4.1/§4.5) ↔ doble voto tribu+general de TK-49. Nota a TK-80: «Faircoin3» colisiona con `FairCoinOfficial/*` (otra moneda, activa) — ver `THIRD_PARTY.md`.
3. **Fuentes y certeza**: todo lo de Faircoin verificado en el clon pineado; fecha 2022-02-05 tomada del clon; nada afirmado sobre el estatus de FairCoop.

Después: commit en la rama → `git checkout main && git merge --no-ff dev/res_publica` → `modelador build` + `check` + `pytest` → `git add public data`.

---

## Ficheros críticos

Nuevos: `vendor.json`, `scripts/vendor.sh`, `modelador_redes/vendor.py`, `tests/test_vendor.py`, `modelos/res_publica/drafts/draftv3.md`, `docs/plan-vendor.md` (mv).
Modificados: `modelador_redes/{paths.py, modelos/enlaces.py, cli/check.py, cli/build.py, site/packs.py}`, `site/templates/foss/tecnico.html`, `THIRD_PARTY.md`, `README.md`, `llms.md`, `docs/informe-tutoria-plasticidad.md`, `CHANGELOG.md`, `pyproject.toml`, `modelos/res_publica/revision/00-indice.md`.

Reutilizar: `_fuera_de_fences` y `normalizar_ancla` (`enlaces.py`), `_ctx` (`build.py`), fixtures `modelos_dir`/`tmp_path` (`tests/conftest.py`), patrón de `validar_grafo` para `validar_manifiesto`.

Commits: uno por fase (`feat(vendor): …(0.3.0)`, `feat(res_publica): draftv3 …`, merge, `build: public/ …`), **cada uno solo con tu OK** (regla de `llms.md`). Sin push.

## Verificación

1. `scripts/vendor.sh --check` → 12 OK, exit 0; `scripts/vendor.sh --list` muestra la tabla.
2. `.venv/bin/pytest` verde (incluye `test_vendor.py` y el test del script).
3. `.venv/bin/modelador build && .venv/bin/modelador check` → OK; `public/foss/tecnico.html` muestra la tabla de vendor; `grep -r "base/teoria/vendor" public` vacío.
4. `grep -o 'https://github.com/faircoin/faircoin/blob/8e9b8f5[^"]*' public/modelos/res_publica/drafts/draftv3.html | head` → enlaces a fichero:línea; ninguno relativo `vendor/`.
5. `git ls-files | grep vendor` vacío; `git status` sin nada bajo `vendor/`.
6. `grep -rniE "muert|cero líneas|no se vendoriza|No vendorizar" README.md THIRD_PARTY.md llms.md docs/informe-tutoria-plasticidad.md site/templates` → sin resultados (salvo el «Muerte voluntaria» de la ficha de clase, que es otra cosa y está en `modelos/`).
7. `.venv/bin/modelador indice --modelo res_publica --check` OK; `git diff --stat main dev/res_publica` solo bajo `modelos/res_publica/`.
