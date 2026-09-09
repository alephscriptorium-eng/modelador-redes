# SPDX-License-Identifier: GPL-3.0-or-later
"""La línea «Draft vigente» de revision/00-indice.md.

Contrato: justo debajo del H1 (tras una línea en blanco) va exactamente
`**Draft vigente:** [draftvN.md](../drafts/draftvN.md)`. La escribe
`modelador indice --modelo X` y la valida `modelador check`.
"""

from __future__ import annotations

import re
from pathlib import Path

from modelador_redes.modelos.catalogo import Modelo

LINEA_RE = re.compile(
    r"^\*\*Draft vigente:\*\* \[(draft(?:v\d+)?)\.md\]\(\.\./drafts/\1\.md\)[ \t]*$",
    re.MULTILINE,
)


def linea_latest(latest: str) -> str:
    return f"**Draft vigente:** [{latest}.md](../drafts/{latest}.md)"


def leer_latest(texto: str) -> str | None:
    m = LINEA_RE.search(texto)
    return m.group(1) if m else None


def escribir_latest(path: Path, latest: str) -> bool:
    """Inserta o reemplaza la línea. Devuelve True si el fichero cambió."""
    texto = path.read_text(encoding="utf-8")
    nueva = linea_latest(latest)
    if LINEA_RE.search(texto):
        actualizado = LINEA_RE.sub(nueva, texto, count=1)
    else:
        lineas = texto.split("\n")
        pos = next((i for i, l in enumerate(lineas) if l.startswith("# ")), None)
        if pos is None:
            actualizado = nueva + "\n\n" + texto
        else:
            lineas[pos + 1:pos + 1] = ["", nueva]
            actualizado = "\n".join(lineas)
    if actualizado == texto:
        return False
    path.write_text(actualizado, encoding="utf-8")
    return True


def validar(modelo: Modelo) -> list[str]:
    errores: list[str] = []
    if not modelo.drafts:
        errores.append(f"{modelo.id}: sin drafts en {modelo.dir / 'drafts'}")
        return errores
    if modelo.indice is None:
        errores.append(f"{modelo.id}: falta revision/00-indice.md")
        return errores
    declarado = leer_latest(modelo.indice.read_text(encoding="utf-8"))
    if declarado is None:
        errores.append(f"{modelo.id}: 00-indice.md no tiene la línea «Draft vigente» (modelador indice --modelo {modelo.id})")
    elif declarado != modelo.latest:
        errores.append(f"{modelo.id}: 00-indice.md declara {declarado} pero el draft mayor es {modelo.latest}")
    return errores
