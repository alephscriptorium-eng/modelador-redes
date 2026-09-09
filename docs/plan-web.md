> **Nota (2026-09-09):** plan histórico, superado. La estructura vigente es `modelos/<modelo>/{drafts,revision}` en este mismo repo, sin comando `sync`; ver `llms.md`.

# Plan: repo `modelador-redes` — aventura devops FOSS para `base/teoria`

## Contexto

`base/teoria/` (untracked en IAIA_2000) incuba un proyecto ajeno al tertuliano: la modelización de la **República Pura de Trevijano** sobre **Oasis/SSB** (SolarNET.HuB) y un **Faircoin3** reflotado. Tiene tres documentos maduros:

| Fichero | Qué es |
| :-- | :-- |
| `base/teoria/contexto.md` | Transcripción v1 (2025): prompt de activación + backlog OP-01…05 / TK-01…25 |
| `base/teoria/pura.md` | Rev. 2 (2026-09-09): auditoría de Oasis 1.0.7 contra 7 criterios trevijanistas, spec RP-1…RP-10, backlog v2 |
| `base/teoria/draftv1.md` | **Backlog v3 (el bueno, ya cerrado según el usuario)**: OP-01…10, TK-01…90, esqueleto andante, sprints 0…6, riesgos R1…R13, mapeos v1/v2→v3 |

`pura.md` enlaza código como rutas relativas a IAIA_2000 (`base/teoria/vendor/oasis/src/models/parliament_model.js#L17-L26`), que solo resuelven con el clon shallow de `epsylon/oasis` @ `9a657b7` (AGPL-3.0) en `base/teoria/vendor/oasis` (gitignorado por `.gitignore:1`).

**Objetivo:** un repo público `alephscriptorium-eng/modelador-redes` con el **mismo look&feel y arquitectura web** que `medidor-lawfare` (generador Python/Jinja2 propio, `public/` commiteado, Pages por Actions, tema gris bicolor, cadena de proveniencia Escrivivir › Scriptorium Skins › Animus Iocandi › producto › F.A.R.O.), que **explica e inicializa** la aventura devops FOSS (vendorizar Oasis, instalarlo, regtest Faircoin3) y publica auditoría + backlog como "cuaderno".

**Decisiones del usuario (AskUserQuestion):** carpeta de sync en `base/teoria/vendor/modelador-redes` · repo **público** · alcance **generador completo**; el backlog es `draftv1.md`.

### Referencia calcada: `medidor-lawfare`
- Clon local (1 commit detrás del remoto, solo cambia LICENSE): `/Users/morente/Desktop/SCRIPTORIUM_v0/SENSORES/MEDIDOR-LAWFER`. Se usa **solo de lectura** como fuente para copiar CSS/plantillas/estructura.
- Piezas a reutilizar tal cual (copiar): `site/assets/foss/style.css`, `site/assets/root/style.css`, `site/assets/foss/theme.js` (clave `ml-theme`; se **mantiene** a propósito: ambos sitios cuelgan de `alephscriptorium-eng.github.io`, mismo origen, y así comparten preferencia de tema), `site/templates/_partials/{provenance-footer,provenance-strip}.html`, `site/templates/root/index.html`, `site/templates/foss/base.html`, `.github/workflows/pages.yml` (verbatim), `.gitignore`, patrón de `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`, `llms.md`.
- Patrón de código a calcar: `medidor_lawfare/paths.py`, `site/brand.py` (`brand_context`, `provenance_context`), `cli/build.py` (`_jinja_env`, `_href_context`, `_copiar_assets`, `build_root`, `build_foss`), `cli/main.py` (argparse con subcomandos).
- LICENSE: copiar la **versión remota** (AIPLv1 composite = `GPL-3.0-or-later AND LicenseRef-Animus-Iocandi`), no la local (GPL plano). Cabeceras SPDX `GPL-3.0-or-later` en los `.py`.
- Wart a NO copiar: logos PNG de 4,6 MB duplicados 4 veces.

## Diseño

### Ubicación y sync (lo que pidió el usuario)
```
IAIA_2000/base/teoria/
├── contexto.md  pura.md  draftv1.md        ← fuente de verdad (siguen aquí)
└── vendor/                                  ← gitignorado
    ├── oasis/                               ← upstream @ 9a657b7 (ya existe)
    └── modelador-redes/                     ← NUEVO: clon del repo GitHub
```
`modelador sync` copia los tres `.md` a `docs/teoria/` del repo (`draftv1.md` → `backlog.md`), reescribe enlaces y escribe `docs/teoria/manifest.json` `{fuente, sha256, bytes, fecha, commit_oasis}`. Dirección **siempre base/teoria → repo** (snapshot); nunca al revés. Ruta origen por defecto `../..` relativa al repo, sobreescribible con `--src`.

**Reescritura de enlaces** (inventario real: 39 en pura.md, 1 inline-code en draftv1.md, 0 en contexto.md; formas `file`, `file#L5`, `file#L17-L26`, 3 directorios con `/` final; varios dentro de encabezados):
- Regex sobre el destino del enlace, fuera de fences (pura.md tiene 8): `\]\(base/teoria/vendor/oasis/?([^)#\s]*)(#L\d+(?:-L?\d+)?)?\)` → `blob/<sha40>/ruta#L..-L..` para ficheros, `tree/<sha40>/ruta` si acaba en `/` o vacío. SHA completo `9a657b776fcafc7c24bf3ad61825316385ecf513`. Normalizar `#L28-38` → `#L28-L38` defensivamente.
- Inline code `` `base/teoria/vendor/oasis/...` `` → `` `vendor/oasis/...` `` (cierto en el nuevo repo tras `modelador vendor`), así el test "cero restos de `base/teoria/vendor` en `public/`" es incondicional.
- Texto del enlace (`[L1145-1147]`) intacto. Fences intactas.

### Paquete `modelador_redes` (CLI `modelador`)
```
modelador-redes/
├── .github/workflows/pages.yml     (copia verbatim)
├── LICENSE (AIPLv1 remoto) · README.md · CHANGELOG.md · CITATION.cff · llms.md · pyproject.toml · .gitignore (+ vendor/)
├── modelador_redes/
│   ├── __init__.py (__version__ = "0.1.0")
│   ├── paths.py            PROJECT_ROOT, DOCS_TEORIA, SITE_DIR, PUBLIC_DIR, PUBLIC_CUADERNO, PUBLIC_FOSS, VENDOR_DIR, GITHUB_REPO, OASIS_REPO, OASIS_COMMIT="9a657b7"
│   ├── teoria/
│   │   ├── sync.py         copiar + reescribir enlaces + manifest
│   │   ├── enlaces.py      regex de reescritura (función pura, testeable)
│   │   ├── markdown.py     md→html con markdown-it-py (CommonMark: el <details> de pura.md L339-515 con tablas y fence dentro se renderiza bien; Python-Markdown lo trataría como HTML crudo) + plugin anchors (ids de encabezado → TOC) + enable("table")
│   │   └── backlog.py      parsea las 11 tablas de backlog.md por firma de cabecera (OP|Nombre|…, ID|Tarea|Dep.|Seam|T|P ×4, ID|RP|Seam|T|P, ID|Tarea|Dep.|T|P, Sprint|…, #|Riesgo|…) → data/backlog.json {ops, tasks[{id, grupo, tarea_md, dep_raw, dep_ids, seam_md, tamano, prioridad}], sprints, riesgos (prefijo R)} validado contra data/schema/backlog.schema.json; celdas se guardan como markdown y se renderizan inline en build
│   ├── site/brand.py       calcado (+ site_url para og:image/og:url/canonical absolutos; el og:image relativo de medidor es un bug, no se clona)
│   ├── vendor.py           `git init` + `git fetch --depth 1 origin <sha40>` + `checkout FETCH_HEAD`; verifica `rev-parse HEAD` == pin; `--path ../oasis` para reutilizar el clon existente; build no falla si vendor/ no existe
│   └── cli/main.py         subcomandos: sync [--src] [--check: exit 1 si hay deriva] · vendor [--path] [--update] · build [--target all|cuaderno|foss] · check (restos base/teoria en public/, enlaces internos rotos, ningún fichero en public/ > 300 KB)
├── data/
│   ├── backlog.json        (generado por sync; commiteado)
│   └── schema/backlog.schema.json
├── docs/
│   ├── teoria/{contexto,pura,backlog}.md + manifest.json   (snapshot sync)
│   ├── devops/aventura.md  guía larga: vendor → node 22 → install.sh (OASIS_AI=3) → oasis.sh → PUB → regtest faircoin3 (esqueleto andante de backlog §"Esqueleto andante")
│   └── prompts/activacion_agente.md  (prompt de activación v3, heredado del formato de contexto.md)
├── site/
│   ├── brand.json
│   ├── assets/{root,foss,cuaderno}/style.css + assets/shared/{theme.js,logo.png,logo_scriptorium.png}  (theme.js una sola vez; logos ≤512 px, ≤150 KB; se copian una vez a public/assets/ y se referencian con {{ base_href }}assets/)
│   └── templates/
│       ├── _partials/{provenance-footer,provenance-strip}.html
│       ├── root/index.html
│       ├── foss/{base,index,tecnico,funcional,devops,LICENSE}.html
│       └── cuaderno/{base,index,documento,backlog}.html
├── public/                 (generado, commiteado)
└── tests/{test_enlaces,test_sync,test_backlog,test_build}.py
```

**Portales** (mismo patrón índice raíz + 2 portales):
| Portal | Ruta | Contenido |
| :-- | :-- | :-- |
| Índice | `public/index.html` | Puerta: logos, serie, versión, dos tarjetas |
| **Cuaderno** (≈ centro de datos) | `public/cuaderno/` | `index` (estado del proyecto, manifest, hitos) · `auditoria.html` (pura.md) · `backlog.html` (backlog.md + tablas OP/TK/sprints/riesgos desde `backlog.json`, resumen de prioridades) · `contexto.html` (v1) |
| **Artefacto (FOSS)** | `public/foss/` | `index` · `tecnico` (arquitectura Oasis/SSB, Faircoin PoC, adaptador de moneda, seams fichero:línea) · `funcional` (ciclo: editar en base/teoria → sync → build → push) · `devops` (**la aventura**: vendor, instalar, regtest, PUB, tests, Pages) · `LICENSE` |

Cuaderno reutiliza la CSS de `foss` (sidebar) con nav propia y `<article class="md">` para el HTML renderizado; se añaden ~30 líneas para tablas anchas (`overflow-x:auto`), `<details>`, `blockquote`, `h2/h3` con `id` para TOC. El `<pre class="mermaid">` no aplica.

**brand.json**: mismo esquema; `producto.nombre = "Modelador de Redes"`, `producto.etiqueta = "Tu cuaderno de modelización de una república sobre redes distribuidas: Oasis/SSB + Faircoin3"`, `producto.logo = "logo.png"`. `serie`, `equipo`, `scriptorium`, `arg` idénticos a medidor-lawfare. Logo de producto: **placeholder** = logo_scriptorium reescalado (no existe logo propio); marcado en CHANGELOG como pendiente.

**Dependencias**: `jinja2>=3.1`, `jsonschema>=4.20`, `markdown-it-py>=3.0,<4`, `mdit-py-plugins>=0.4,<0.5` (no instaladas; `pip install -e ".[dev]"`), dev `pytest>=7.4`. Python ≥3.9 (local: 3.9.6): `from __future__ import annotations` en todos los módulos y sin uniones `X | Y` en runtime; classifiers coherentes con 3.9 (medidor los tiene mal).

**Determinismo**: el HTML lleva la fecha del `manifest.json`, no la de build, para que `build` sea reproducible (CI no construye; un test re-renderiza y compara con `public/` commiteado).

**Licencia**: se copia **verbatim** el LICENSE remoto de medidor-lawfare (AIPLv1 composite; política declarada del custodio: "All packages of this workspace receive the identical license treatment"), aunque mencione package.json/Angular. `pyproject` → `license = {file = "LICENSE"}`; `CITATION.cff` → `GPL-3.0-or-later`; footer "GPL-3.0 · AIPLv1". Se añade `THIRD_PARTY.md`: Oasis (epsylon, AGPL-3.0, commit pinneado) se obtiene con `modelador vendor`, va gitignorado y no se redistribuye; las citas de pura.md son breves y atribuidas. `foss/LICENSE.html` renderiza nuestro LICENSE, no el de Oasis.

## Pasos de ejecución

1. **Esqueleto local** en `/Users/morente/Desktop/IAIA_2000/base/teoria/vendor/modelador-redes`: `git init -b main`, copiar/adaptar los ficheros de referencia listados arriba (leer del clon MEDIDOR-LAWFER; LICENSE del remoto vía `gh api …/contents/LICENSE`). Logos: `sips -Z 256` sobre copias en `site/assets/shared/`.
2. **Código**: `paths.py`, `enlaces.py` (+tests primero), `sync.py`, `markdown.py`, `backlog.py` (+schema), `vendor.py`, `brand.py`, `build.py`, `cli/main.py`, `pyproject.toml` con entry point `modelador`.
3. **Plantillas y CSS** (root, foss, cuaderno, partials) y `brand.json`.
4. **Contenido propio**: `README.md` (misma estructura que medidor-lawfare: qué es, `site/→public/`, tres portales, ciclo operativo, CLI, estructura, Pages, tests, licencia), `llms.md` (onboarding agentes: rama, CI, sync unidireccional, commit conventions, "no editar public/ ni docs/teoria/ a mano"), `docs/devops/aventura.md`, `docs/prompts/activacion_agente.md`, `CHANGELOG.md` 0.1.0, `CITATION.cff`.
5. `pip install -e ".[dev]"` → `modelador sync` → `modelador vendor` (reutiliza `../oasis` si existe: symlink no; se documenta `--path ../oasis` para no clonar dos veces) → `modelador build --target all` → `modelador check` → `pytest`.
6. Commit inicial (`feat: modelador-redes 0.1.0 — cuaderno + foss + sync desde base/teoria`, trailer Co-Authored-By).
7. **GitHub** (gh local es 1.12.1, sin `--source/--push`; se usa la API): `gh api -X POST user/repos -f name=modelador-redes -F private=false -f description="Juguete-pasatiempo Animus Iocandi para modelizar una república sobre redes distribuidas (Oasis/SSB + Faircoin3)"` → `git remote add origin https://github.com/alephscriptorium-eng/modelador-redes.git` → `git push -u origin main` → `gh api -X POST repos/alephscriptorium-eng/modelador-redes/pages -f build_type=workflow` (409 ⇒ `PUT`) → si el primer run falló con "Get Pages site failed", re-ejecutar (`gh api -X POST repos/.../actions/workflows/pages.yml/dispatches -f ref=main`). Topics vía `gh api -X PUT repos/.../topics` (`animus-iocandi`, `oasis`, `ssb`, `faircoin`, `republica`, `foss`). Homepage = URL de Pages.
8. **Verificar** el despliegue (`gh run watch`; `curl -I https://alephscriptorium-eng.github.io/modelador-redes/`, `/cuaderno/backlog.html`, `/foss/devops.html`).
9. Memoria: guardar nota de proyecto (ubicación del clon, flujo sync unidireccional, commit Oasis pinneado).

## Verificación
- `pytest` verde: reescritura de enlaces (con/sin ancla, `-38`→`-L38`, directorios, inline code intacto), `sync` produce manifest con sha256 correcto, `backlog.json` valida contra schema y contiene TK-01…TK-90 sin duplicados + 7 sprints + 13 riesgos, `build` genera las 11 páginas y ninguna contiene `base/teoria/vendor`.
- `modelador check` sin errores; enlaces `github.com/epsylon/oasis/blob/9a657b7/...` muestreados con `curl -I` (200).
- Visual: abrir `public/index.html`, `public/cuaderno/backlog.html`, `public/foss/devops.html` en claro y oscuro; comparar con `https://alephscriptorium-eng.github.io/medidor-lawfare/` (misma retícula, misma cadena de proveniencia).
- Pages: run verde y las tres URLs responden 200 bajo la subruta `/modelador-redes/` (todas las rutas relativas; `og:image` relativo como en el original).
- `git -C IAIA_2000 status`: `base/` sigue untracked y `vendor/` ignorado; nada del nuevo repo se cuela en IAIA_2000.

## Fuera de alcance / avisos
- No se toca `base/teoria/*.md` ni el clon de `medidor-lawfare`.
- El vendor de Oasis (AGPL-3.0) **nunca se commitea**; solo se clona con `modelador vendor`. Los fragmentos citados en pura.md son cortos (cita).
- Logo de producto propio pendiente (placeholder).
- Faircoin3 (fork de `faircoin/faircoin`) no se vendoriza en 0.1.0; la página devops documenta el regtest y enlaza el backlog (TK-39…41).
