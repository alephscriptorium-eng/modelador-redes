# Terceros

vendor/plan.md

| Componente | Origen | Licencia | Cómo se usa |
| :-- | :-- | :-- | :-- |
| **Oasis** (SolarNET.HuB) | https://github.com/epsylon/oasis · commit `9a657b776fcafc7c24bf3ad61825316385ecf513` (release 1.0.7, 2026-09-08) | AGPL-3.0 | Objeto de la auditoría. **Nunca se commitea**: se clona en `vendor/oasis` (ignorado por git). Los drafts lo citan y el build reescribe cada cita hacia ese commit exacto en GitHub. |
| Faircoin (`faircoin/faircoin`) | https://github.com/faircoin/faircoin | MIT | Solo documentado; no se vendoriza. |
| markdown-it-py, mdit-py-plugins | PyPI | MIT | Render de markdown en build. |
| Jinja2 | PyPI | BSD-3 | Plantillas. |
| jsonschema | PyPI | MIT | Reservado para validar `modelo.json` / `backlog.json`. |
