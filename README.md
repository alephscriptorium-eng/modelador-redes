# Modelador de Redes

**Catálogo de modelizaciones políticas sobre redes distribuidas** (Oasis/SSB + Faircoin). Cada modelización audita el mismo código (Oasis 1.0.7, commit `9a657b7`) desde una doctrina distinta, avanza por drafts sucesivos, se revisa capítulo a capítulo y deja un backlog. Esta web lo publica todo: en línea, enlazado al repositorio y en zip.

**Web:** https://alephscriptorium-eng.github.io/modelador-redes · **Versión:** 0.1.0 · **Licencia:** GPL-3.0-or-later AND LicenseRef-Animus-Iocandi

> [!WARNING]
> **GitHub queda *deprecated* como remoto canónico.** El original de este repo pasará a [Radicle](https://radicle.xyz) (git distribuido P2P, sin servidor central), semillado por un nodo propio en `rad.escrivivir.co`.
>
> **Pendiente:** ni el repo está inicializado en Radicle ni el nodo está desplegado. Hasta entonces `origin` (GitHub) sigue siendo el remoto que publica la web y no se borra nada. Guía y estado de la migración: [`docs/radicle.md`](docs/radicle.md).

No se implementa ningún producto. El repo es documentación de backlog y el generador que la publica.

## Modelos

| Modelo | Rama | Qué modela |
| :-- | :-- | :-- |
| `res_publica` | `dev/res_publica` | La República Constitucional de Trevijano (*Teoría pura de la República*) sobre Oasis |
| `colectividades` | `dev/colectividades` | Las colectivizaciones de 1936-37 en contraste con la República Pura |
| `clase` | `dev/clase` | El materialismo filosófico de Gustavo Bueno (M₁/M₂/M₃, cierre categorial, eutaxia) sobre Oasis |

## Convención

```
modelos/<modelo>/
├── modelo.json          id · nombre · rama · estado · descripcion
├── drafts/              draft.md, draftv0.md, draftv1.md, …  (sufijo mayor = draft vigente)
└── revision/
    ├── 00-indice.md     estado; línea «Draft vigente» mantenida por `modelador indice`
    └── NN-*.md          fichas de revisión
```

Una rama `dev/<modelo>` por modelo que **solo toca su carpeta**; `main` las integra y es la única rama con `public/` y `data/`.

## Generar la web

```bash
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
.venv/bin/modelador build      # public/ + data/
.venv/bin/modelador check      # exit 1 si algo está roto
.venv/bin/pytest
```

`.github/workflows/pages.yml` sube el `public/` commiteado en `main` a GitHub Pages; no construye nada.

## Oasis

El código auditado es AGPL-3.0 y **no se commitea**: se clona en `vendor/oasis` (ignorado). Ver `THIRD_PARTY.md`.

## Agentes

Leer `llms.md` antes de tocar nada.
