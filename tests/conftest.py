# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import json
from pathlib import Path

import pytest

DRAFT_A = """# Modelo de prueba v0

## Backlog

### OP-01 · Primera oportunidad

Resumen de la primera oportunidad en una frase.

| ID | Tarea | Dep. | T | P |
| :-- | :-- | :-- | :-- | :-- |
| **TK-01** | Hacer algo con `a \\| b` | — | S | H |
| **TK-02** | Otra cosa ([L5](base/teoria/vendor/oasis/src/x.js#L5-9)) | TK-01 | M | M |

| # | Elemento | Cert. |
| :-- | :-- | :-- |
| 1 | numérico, no es backlog | A |
"""

DRAFT_B = """# Modelo de prueba v1

Ver [la ficha](../revision/01-a.md) y [el anexo](../revision/01-a.md#L3).

```
| ID | dentro de fence, no es tabla |
| :-- | :-- |
| TK-99 | no debe extraerse |
```

## Carril D

| ID | Buscar | Dónde | Default | Alternativas | Desbloquea |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-D01 | Mónada | Cap. II | hash | PUB | TK-G01 |
| TK-D02 | Mandato | Cap. III | firmado | tribu | TK-G03 |

## Carril G

| ID | Tarea | Depende | Seam | T | P |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-G01 | Mónadas | D01 | `monad_model.js` | M | H |
| TK-G03 | Mandato | D02 | `parliament_view.js` | M | **C** |
"""

INDICE = """# Revisión de prueba

**Draft vigente:** [draftv1.md](../drafts/draftv1.md)

| Cap. | Ficha |
| :-- | :-- |
| I | [01-a.md](01-a.md) |
"""

FICHA = """# Ficha A

Ver [draftv1 L3](../drafts/draftv1.md#L3) y [draftv1](../drafts/draftv1.md).
"""


def crear_modelo(base: Path, mid: str = "prueba", con_indice: bool = True) -> Path:
    d = base / mid
    (d / "drafts").mkdir(parents=True)
    (d / "revision").mkdir()
    (d / "modelo.json").write_text(
        json.dumps({"id": mid, "nombre": "Modelo de prueba", "rama": f"dev/{mid}", "estado": "test", "descripcion": "desc"}),
        encoding="utf-8",
    )
    (d / "drafts" / "draftv0.md").write_text(DRAFT_A, encoding="utf-8")
    (d / "drafts" / "draftv1.md").write_text(DRAFT_B, encoding="utf-8")
    if con_indice:
        (d / "revision" / "00-indice.md").write_text(INDICE, encoding="utf-8")
    (d / "revision" / "01-a.md").write_text(FICHA, encoding="utf-8")
    return d


@pytest.fixture
def modelos_dir(tmp_path: Path) -> Path:
    base = tmp_path / "modelos"
    crear_modelo(base)
    return base
