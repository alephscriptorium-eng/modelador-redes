# Plan: vendor del ecosistema FairCoop + `scripts/vendor.sh`

## Context

Hoy el único código de terceros en `vendor/` es Oasis (`epsylon/oasis` @ `9a657b7`), clonado a mano según `THIRD_PARTY.md`, con el SHA hardcodeado en `modelador_redes/paths.py` y una regex en `modelador_redes/modelos/enlaces.py` que solo reescribe `vendor/oasis/...`. `llms.md` prohíbe hoy "vendorizar Faircoin ni ningún código de terceros", y `res_publica/draftv2` deja TK-C00 ("clonar `faircoin/faircoin` en vendor para citar fichero:línea") sin resolver.

El usuario quiere (1) saber qué código del ecosistema FairCoop existe y es forkable, para citarlo `fichero:línea` desde los drafts (no para ejecutarlo), y (2) un script versionado en `main` que clone todo el vendor de forma reproducible. Decisiones tomadas: **script en shell** (`scripts/vendor.sh`) y **todo lo forkable por defecto**.

Todo este trabajo es infraestructura → **solo en `main`** (el árbol está ya en `main`, limpio, en `870b38c`).

## Inventario verificado (2026-09-09, API de GitHub/GitLab)

### Se vendoriza (todos GitHub; pin = HEAD de la rama por defecto hoy)

| id | Repo | SHA | Último commit | Lic. | Tamaño | Para qué |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `oasis` | epsylon/oasis | `9a657b776fcafc7c24bf3ad61825316385ecf513` | 2026-09-08 | AGPL-3.0 | 80 MB | ya vendorizado; objeto de todas las auditorías |
| `faircoin` | faircoin/faircoin | `8e9b8f54b04aed385fb99e69718c6c045817a4c7` | 2022-02-05 | MIT | 54 MB | Bitcoin 0.12 + PoC: `src/poc.cpp` (90 KB), `src/chainparams.cpp` (CVN/admin hardcodeados), `doc/on-proof-of-cooperation.md`, `doc/CVN-operators-guide.md`, `doc/fasito-*.md`. Carril C (Faircoin3), TK-C00, CL-5 |
| `fairchains` | FairChains/fairchains | `3e07f44c2497176a6c81ca98495da9987c3b2681` | 2018-09-21 | MIT | 51 MB | mismo árbol + `src/fairchains-tool*.cpp` (**crea una cadena PoC nueva desde JSON sin recompilar**) + Omnilayer. El más relevante para "génesis nuevo"; ojo: 4 años por detrás de faircoin master |
| `fasito` | faircoin/Fasito | `a62e97e942db3e18c4741c79a83b73a9e8d7afe7` | 2022-02-07 | GPL-3.0 | 0.5 MB | firmware del token de firma de los CVN (Teensy); contrapunto a `-cvn=file` |
| `electrumfair` | faircoin/electrumfair | `ce0cc7ac89df71d970d113493f524f206e84ed5d` | 2021-04-21 | MIT | 36 MB | cartera ligera (rama por defecto `3.3.4-fc`) |
| `electrumfairx` | faircoin/electrumfairx | `3a33675e117dd97ecba80d35ec10b9c98290ed50` | 2018-09-08 | MIT | 2.5 MB | servidor Electrum |
| `faircoin-seeder` | faircoin/faircoin-seeder | `f5851c00ec49f469d9482ef60d278362f3402f79` | 2017-07-18 | **sin licencia** | 0.2 MB | DNS seeder; necesario para una red nueva. Solo lectura |
| `faircoin2-cce` | faircoin/faircoin2-cce-4.0 | `872e2c7c2e1737200e9fced76a3bf75539a567a3` | 2017-10-19 | GPL-3.0 | 0.1 MB | explorador de bloques |
| `faircoin-exporter` | mmoya/faircoin_exporter | `db0b72011d4e3dd0527dbad1c1f1a4bf20344105` | 2017-07-24 | Apache-2.0 | 0.7 MB | métricas Prometheus de CVN |
| `valuenetwork` | FreedomCoop/valuenetwork | `900bfcdab024644b5e504515327761f27788322f` | 2021-02-07 | AGPL-3.0 | 27 MB | OCP: contabilidad REA, membresía por shares, multicurrency (BotC), pasarela faircoin. Arte previo para CL-3/CL-4 (reparto), CL-8 (multi-contexto = federación) |
| `faircoin-nrp` | django-rea/faircoin-nrp | `51d39379e0ccf6f78e1506bfd7bfaac155360b4b` | 2016-08-22 | GPL-3.0 | 0.03 MB | puente electrum-fair ↔ NRP: el mismo seam que el adaptador RPC de `Banking` |
| `coopshares` | bankofthecommons/coopshares | `002cb514d66a00730a0a4adc0b03a5cd5c223663` | 2018-07-26 | **sin licencia** | 1 MB | shares de Bank of the Commons. Solo lectura |

### Documentado, no vendorizado

- **FairMarket** = `sarantapichos/faircoop-market`: árbol Odoo 8 completo (119 MB, AGPL-3.0, 2015). Demasiado grande y nada específico; se cita la URL.
- **Bank of the Commons** corría sobre Cyclos (no forkable); `opencooperativeecosystem/agent|kit|rea-app` (frontend OCW, ValueFlows, sin licencia, 2018) — referencia.
- **Komun** (framagit/gitlab): sin código de FairCoin salvo `faircoin-monitor-bot`; `thokon00/faircoin-cvn-bot`.
- **`FairCoinOfficial/*` (2023-2026, activo)**: **otra moneda** con el nombre FAIR (Quark PoW/PoS, masternodes, premine 5 M, puente WFAIR en Base). No es la FairCoin cooperativa. Relevante para TK-80 (nombre/marca): "Faircoin3" colisiona con un proyecto vivo.
- Históricos: `visbtc/fair-coin` (FairCoin1, 2014), `jaromil/faircoin2` (staging 2016).
- Dominios FairCoop/BotC/FairMarket caídos; fair-coin.org "Cooling down" 2024-06-17 (ya en draftv2).

## Cambios

### 1. `vendor.json` (raíz, nuevo) — única fuente de verdad

```json
{
  "vendor": [
    {"id": "oasis", "repo": "https://github.com/epsylon/oasis", "sha": "9a657b77…", "fecha": "2026-09-08",
     "licencia": "AGPL-3.0", "por_defecto": true, "proposito": "Objeto de la auditoría (release 1.0.7)"},
    …
  ]
}
```

Campos: `id` (`^[a-z0-9-]+$`, carpeta `vendor/<id>`), `repo` (https, GitHub), `sha` (40 hex), `fecha`, `licencia` (`"sin licencia"` donde falte), `por_defecto` (true en los 12 de la tabla), `proposito`. Vive en la raíz porque `vendor/` entero está en `.gitignore`.

### 2. `scripts/vendor.sh` (nuevo, ejecutable)

Bash + `git` + `python3` (para leer el JSON; ya es requisito del proyecto). Sin jq.

```
scripts/vendor.sh                 # clona los por_defecto que falten; verifica los que existan
scripts/vendor.sh --check         # no escribe; exit 1 si falta alguno o HEAD ≠ sha
scripts/vendor.sh --only faircoin fairchains
scripts/vendor.sh --all           # también los por_defecto=false (hoy ninguno)
scripts/vendor.sh --list          # tabla id · sha · licencia · estado
```

Por entrada: si `vendor/<id>/.git` existe → `git rev-parse HEAD` == sha (si no, "DERIVA", exit 1; **nunca toca un clon existente**); si no existe → `git init -q` + `remote add origin` + `fetch --depth 1 origin <sha>` + `checkout -q FETCH_HEAD`; si el fetch por SHA falla (servidor sin allowReachableSHA1InWant) → fallback `fetch origin` completo + `checkout <sha>`. Resumen final por id. `set -euo pipefail`, ruta absoluta desde `$(dirname "$0")/..`.

### 3. Generalizar `modelador_redes/modelos/enlaces.py`

- Nuevo `modelador_redes/vendor.py`: `cargar_manifiesto(path=None) -> dict[str, Entrada]` (dataclass `id, repo, sha, licencia, por_defecto, proposito, fecha`), `VENDOR_JSON` en `paths.py`.
- `VENDOR_RE = r"\]\((?:base/teoria/)?vendor/([a-z0-9-]+)/?([^)#\s]*)(#L\d+(?:-L?\d+)?)?\)"`; `reescribir_vendor(md, repos=None)` resuelve el id en el manifiesto → `blob/<sha>` (fichero) o `tree/<sha>` (dir); id desconocido → se deja intacto (`modelador check` lo cazará como enlace relativo roto).
- `reescribir_oasis(md, repo, sha)` se mantiene como wrapper (tests actuales intactos); `reescribir_para_web` / `reescribir_para_zip` usan `reescribir_vendor`.
- `paths.py` sigue sin I/O: `OASIS_SHA` se queda; test de consistencia manifiesto ↔ constante.

### 4. `modelador check`

Añadir `validar_manifiesto()`: JSON parsea, ids únicos y bien formados, sha 40 hex, repo https, `oasis` presente con `OASIS_SHA`. No exige que `vendor/` exista (build sigue sin depender del disco).

### 5. Web y docs (todo en `main`)

- `site/templates/foss/tecnico.html` §Oasis → §Vendor: párrafo + tabla generada desde el manifiesto (`contexto.py` añade `vendor`), con enlace `tree/<sha>` por fila.
- `THIRD_PARTY.md`: tabla "Se vendoriza" (desde el manifiesto) + "Documentado, no vendorizado" (lista de arriba, incluido el aviso FairCoinOfficial) + comando `scripts/vendor.sh`. Sustituye las instrucciones manuales de clonado.
- `README.md` §Oasis → §Vendor (dos líneas + comando).
- `llms.md`: regla "No vendorizar Faircoin…" → "Solo se vendoriza lo que está en `vendor.json`, con `scripts/vendor.sh`; nunca se commitea"; convención de cita `vendor/<id>/ruta#Lx-Ly` para cualquier id; estructura (+`vendor.json`, `scripts/`); checklist (+`scripts/vendor.sh --check`).
- `CHANGELOG.md` 0.3.0 + `pyproject.toml` version 0.3.0 (asumo release menor por ser feature de infraestructura).
- `docs/plan-web.md` no se toca (histórico).

### 6. Tests

- `tests/test_vendor.py`: manifiesto real carga, ids únicos, sha hex, `oasis` == `OASIS_SHA`; `reescribir_vendor` con id `faircoin` (fichero, dir, ancla `-38`→`-L38`, dentro de fence intacto), id desconocido intacto, prefijo `base/teoria/` aceptado.
- `tests/test_enlaces.py`: sin cambios (deben seguir verdes).
- Prueba del script sobre un repo git local en `tmp` (bash desde pytest con `subprocess`, `--check` devuelve 1 si falta, 0 tras clonar, 1 tras mover HEAD).

## Orden de ejecución

1. `vendor.json` + `scripts/vendor.sh` (+ `chmod +x`) → `scripts/vendor.sh --list`, `scripts/vendor.sh --check` (oasis OK, resto falta) → `scripts/vendor.sh` (clona ~11 repos, ≈170 MB) → `--check` OK.
2. `vendor.py`, `paths.py`, `enlaces.py`, `check.py`, `contexto.py`, `tecnico.html`, tests.
3. Docs: THIRD_PARTY, README, llms, CHANGELOG, pyproject.
4. `.venv/bin/pytest` · `.venv/bin/modelador build` · `.venv/bin/modelador check` · `git ls-files | grep vendor` vacío · `git add` (incluye `public/` y `data/` regenerados) · commit en `main` `feat(vendor): manifiesto vendor.json + scripts/vendor.sh; ecosistema FairCoop citable (0.3.0)`. No push salvo que se pida.

## Verificación

- `scripts/vendor.sh --check` exit 0 con los 12 ids; `git -C vendor/faircoin rev-parse HEAD` == pin.
- `pytest` verde; `modelador check` OK; `public/foss/tecnico.html` muestra la tabla de vendor; `grep -r "base/teoria/vendor" public` vacío.
- Un enlace de prueba `[poc.cpp](vendor/faircoin/src/poc.cpp#L10)` en un draft de `tests/conftest.py` sale como `https://github.com/faircoin/faircoin/blob/8e9b8f5…/src/poc.cpp#L10`.
- `git status` no muestra nada bajo `vendor/`.

## Fuera de alcance (para las ramas `dev/*`)

Los drafts que aprovechen esto (TK-C00 de res_publica, carril de tesoro de colectivizaciones) se escriben en su rama, no aquí.
