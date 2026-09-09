# SPDX-License-Identifier: GPL-3.0-or-later
"""modelador indice --modelo X [--check] — mantiene la línea «Draft vigente»."""

from __future__ import annotations

from modelador_redes.modelos.catalogo import cargar_modelo
from modelador_redes.modelos.indice import escribir_latest, validar


def run(modelo_id: str, solo_check: bool = False) -> int:
    m = cargar_modelo(modelo_id)
    if solo_check:
        errores = validar(m)
        for e in errores:
            print(f"ERROR {e}")
        if not errores:
            print(f"{m.id}: Draft vigente = {m.latest} (OK)")
        return 1 if errores else 0
    if m.indice is None:
        print(f"ERROR {m.id}: falta revision/00-indice.md")
        return 1
    if m.latest is None:
        print(f"ERROR {m.id}: sin drafts")
        return 1
    cambiado = escribir_latest(m.indice, m.latest)
    print(f"{m.id}: Draft vigente = {m.latest} ({'actualizado' if cambiado else 'sin cambios'})")
    return 0
