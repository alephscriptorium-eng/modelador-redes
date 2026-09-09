# llms.md — Contexto para agentes LLM

Documento de onboarding para cualquier LLM que trabaje en este repositorio. **Leer antes de tocar ficheros.**

Repositorio: https://github.com/alephscriptorium-eng/modelador-redes
Web: https://alephscriptorium-eng.github.io/modelador-redes

---

## Qué es este proyecto

**Modelador de Redes** (`modelador-redes` v0.2.0) es un **catálogo de modelizaciones** políticas sobre redes distribuidas (Oasis/SSB + Faircoin) y el generador de sitio estático que lo publica.

- **No se implementa ningún producto.** No hay fork de Oasis, no hay cadena Faircoin3. Hay auditorías, drafts, fichas de revisión y backlogs. Cualquier tarea `TK-*` de un backlog es una especificación, no código.
- Todas las modelizaciones auditan **el mismo código**: `epsylon/oasis` @ `9a657b776fcafc7c24bf3ad61825316385ecf513` (release 1.0.7, AGPL-3.0). Vive en `vendor/oasis`, ignorado por git; ver `THIRD_PARTY.md`.
- La web muestra, por modelo: estado (índice de revisión), drafts, fichas, backlog (oportunidades + tareas) y descargas zip, con enlaces a github.com (blob/raw) como respaldo de ficheros.

---

## Nodos y aristas

El catálogo es un **grafo**:

- **Nodo** = doctrina pura auditada contra Oasis (`tipo: "nodo"`). Sin tensión con otros nodos: no cita a otro nodo como autoridad, solo hechos verificados del código.
- **Arista** = modelo híbrido o de contraste entre **dos** nodos (`tipo: "arista"`, `nodos: ["a", "b"]`, `relacion` libre: contraste, síntesis…). Id = `a+b`, carpeta `modelos/a+b/`, rama `dev/a+b`. Una arista se crea desde `main` y **nunca reescribe a sus nodos**; cuando un nodo cambia, la arista se revisa.
- `modelador check` valida el grafo (nodos existentes, id bien formado). La portada dibuja el SVG y publica `catalogo.json`.

Crear un nodo nuevo: `git checkout -b dev/<id> main` → `modelos/<id>/{modelo.json, drafts/draft.md, revision/00-indice.md}` → `modelador indice --modelo <id>` → commit → merge en main. Crear una arista: igual con `tipo: "arista"` y `nodos`.

## Los modelos

| id | Tipo | Rama | Nombre | Draft vigente | Estado |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `res_publica` | nodo | `dev/res_publica` | República Pura (Trevijano) sobre Oasis/SSB | `draftv2` | en revisión (8 fichas del Libro III cerradas; carril D pendiente de verificar contra el libro) |
| `colectivizaciones` | nodo | `dev/colectivizaciones` | Colectivizaciones libertarias 1936-37 sobre Oasis/SSB | `draftv1` | en revisión (auditoría CL-1…11; fichas 01-07; D'01-04 verificados en fuentes, D'05-08 deuda) |
| `clase` | nodo | `dev/clase` | Materialismo filosófico de Gustavo Bueno sobre Oasis | `draftv0` | auditoría escrita sin revisar (fichas pendientes) |
| `res_publica+colectivizaciones` | arista (contraste) | `dev/res_publica+colectivizaciones` | Las dos constituciones sobre el mismo código | `draft` | **pausa** hasta que el nodo `colectivizaciones` tenga auditoría |

Fuente de verdad de esta tabla: `modelos/*/modelo.json` y el disco. Si difieren, manda el disco.

---

## Reglas de ramas

| Rama | Toca | Prohibido |
| :-- | :-- | :-- |
| `dev/<modelo>` | **solo** `modelos/<modelo>/` | generador, `site/`, `docs/`, `llms.md`, `public/`, `data/` |
| `main` | todo; única rama con `public/` y `data/` | editar `modelos/*` directamente (hazlo en la rama y mergea) |

- `main` integra con `git merge --no-ff dev/<modelo>`. Como cada rama solo toca su carpeta, no hay conflictos.
- Infraestructura (generador, plantillas, docs, CI) **solo en main**. Excepción histórica: el primer commit del generador viajó en `dev/res_publica` porque `main` aún no existía.
- No crear más ramas salvo petición explícita. Un modelo nuevo = una carpeta `modelos/<id>/` con `modelo.json` + `drafts/draft.md` + `revision/00-indice.md` y su rama `dev/<id>` desde `main`.

---

## Regla del draft vigente

- Los drafts avanzan por sufijo: `draft.md` → `draftv0.md` → `draftv1.md` → … Nunca se reescribe uno anterior; se crea el siguiente. Orden numérico (`draftv10` > `draftv2`).
- `revision/00-indice.md` lleva, justo bajo el H1, la línea exacta:

  ```
  **Draft vigente:** [draftvN.md](../drafts/draftvN.md)
  ```

  La escribe `modelador indice --modelo <id>`; `modelador check` falla si no coincide con el sufijo mayor. Al añadir un draft, ejecuta el comando y commitea el índice junto con el draft.
- Las fichas `revision/NN-*.md` enlazan a los drafts con rutas relativas (`../drafts/draftv2.md#L58`). En la web, los enlaces con `#L…` van al blob de GitHub en `main` (línea exacta) y los enlaces sin ancla a la página HTML.

---

## Ciclo operativo

```bash
# 1. en la rama del modelo
git checkout dev/<modelo>
#    añadir drafts/draftvN.md · fichas · actualizar revision/00-indice.md
.venv/bin/modelador indice --modelo <modelo>
git add modelos/<modelo> && git commit -m "feat(<modelo>): …"

# 2. en main
git checkout main && git merge --no-ff dev/<modelo>
.venv/bin/modelador build && .venv/bin/modelador check && .venv/bin/pytest
git add public data && git commit -m "build: public/ (+<modelo>)"
git push origin main dev/<modelo>
```

Instalación: `python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"` (Python ≥ 3.9; el código evita `X | Y` en runtime y `match`).

---

## CI / GitHub Pages

| Workflow | Fichero | Trigger | Qué hace |
| :-- | :-- | :-- | :-- |
| Deploy GitHub Pages | `.github/workflows/pages.yml` | push a `main` | sube `public/` **tal cual**; no construye |

Pages tiene origen **GitHub Actions** (`build_type=workflow`). No hay CI de pytest: ejecutar en local antes de push.

**Gotcha verificado (2026-09-09):** al activar Pages por API con varias ramas ya subidas, GitHub creó el entorno `github-pages` con una política de despliegue restringida a la primera rama que vio (`dev/clase`), y el job `deploy` fallaba **sin ejecutar ningún paso**. Arreglo:

```bash
R=repos/alephscriptorium-eng/modelador-redes
gh api -X POST $R/environments/github-pages/deployment-branch-policies -f name=main   # permitir main
gh api $R/environments/github-pages/deployment-branch-policies -q '.branch_policies[].name'  # debe listar solo main
gh api -X POST $R/actions/workflows/pages.yml/dispatches -f ref=main                # relanzar
```

El primer push de `main` tampoco disparó el workflow (Actions aún no estaba inicializado): usar el `dispatch` de arriba. `gh 1.12.1` no tiene `gh run list --json`; consultar `gh api $R/actions/runs`.

---

## Estructura del repositorio

```
modelos/<modelo>/{modelo.json, drafts/, revision/}   # contenido (ramas dev/*)
modelador_redes/
  paths.py                 constantes (repo, SHA de Oasis, rutas)
  modelos/catalogo.py      descubre modelos, ordena drafts, draft vigente; grafo nodos/aristas
  site/grafo.py            SVG del grafo
  modelos/indice.py        línea «Draft vigente»
  modelos/enlaces.py       reescritura de enlaces (Oasis → blob/<sha>; .md → .html; #L → blob main)
  modelos/markdown.py      markdown-it-py + anclas h2/h3 + .table-wrap
  modelos/backlog.py       extracción tolerante de OP (encabezados) y tablas TK/RP
  site/{brand,contexto,packs}.py
  cli/{main,build,check,zip,indice}.py
site/{brand.json, assets/, templates/{_partials,root,modelo,foss}}
public/   data/            generados por `modelador build`, commiteados solo en main
docs/plan-web.md           plan histórico (superado)
tests/                     pytest
```

---

## CLI

```bash
modelador build [--target all|catalogo|foss]
modelador check
modelador zip [--modelo X]
modelador indice --modelo X [--check]
```

---

## Backlog: cómo se extrae

No hay `backlog.md` canónico. `backlog.py` recorre cada draft y recoge **toda tabla** cuya primera celda de fila sea `TK-…`, `OP-…`, `RP-…` o `Rn`, guardando las celdas como markdown (`data/<modelo>/backlog.json`). Las oportunidades son encabezados `OP-nn` con su primer párrafo. En la web, el draft vigente lleva badge `latest` y los anteriores conservan su etiqueta. Si añades una tabla de tareas en un draft, respeta: primera columna = ID, fila separadora `| :-- |`, pipes dentro de celdas escapados como `\|`.

---

## Qué NO hacer

- **Nunca commitear `vendor/`** (80 MB, AGPL). Está en `.gitignore`; comprueba `git ls-files | grep vendor` vacío.
- **Nunca editar ni commitear `public/` o `data/` en ramas `dev/*`.** Solo en `main`, y siempre regenerados con `modelador build`, nunca a mano.
- **Nunca `modelador build` en una rama `dev/*`** como paso de trabajo (avisa, pero ensucia el árbol).
- No cambiar la clave `ml-theme` de `theme.js`: la comparten los sitios de `alephscriptorium-eng.github.io`.
- No vendorizar Faircoin ni ningún código de terceros.
- No reescribir drafts anteriores: crea el siguiente sufijo.
- No dejar rutas locales al vendor (las de la forma `base/teoria/…/oasis`) en nada publicado: `modelador check` busca ese prefijo y falla.
- No commitear sin que el usuario lo pida.

---

## Checklist antes de cerrar una tarea

- [ ] `pytest` verde.
- [ ] Si tocaste un modelo: `modelador indice --modelo <id> --check` OK y solo cambió `modelos/<id>/`.
- [ ] Si estás en `main` y algo publicable cambió: `modelador build` + `modelador check` + `git add public data`.
- [ ] `git ls-files | grep vendor` vacío.
- [ ] CHANGELOG.md si es release.
