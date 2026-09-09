# Changelog

All notable changes to **Modelador de Redes** follow [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-09-09

### Added

- Generador de sitio estático (Python + Jinja2 + markdown-it-py) con CLI `modelador build | check | zip | indice`.
- Convención `modelos/<modelo>/{modelo.json, drafts/draftvN.md, revision/NN-*.md}` y una rama `dev/<modelo>` por modelización.
- Modelo **res_publica**: 4 drafts (auditoría de Oasis 1.0.7 contra Trevijano, informe «¿clon o parecido?», plan del backlog v3) y 9 fichas de revisión del Libro III de *Teoría pura de la República*.
- Modelos **colectividades** (colectivizaciones 1936-37) y **clase** (materialismo filosófico de Gustavo Bueno) con su draft semilla.
- Backlog extraído de los drafts: oportunidades (encabezados `OP-nn`) y tablas de tareas por carril, publicadas como HTML y `backlog.json`.
- Descargas zip deterministas por modelo (`-drafts`, `-revision`, `-todo`).
- Reescritura de enlaces al vendor de Oasis hacia el commit auditado `9a657b7` en GitHub; `modelador check` garantiza que no queda ninguna ruta local.
- Portal FOSS con `llms.md` publicado para agentes.
- Logo de producto: placeholder (logo de Scriptorium reescalado); pendiente logo propio.
