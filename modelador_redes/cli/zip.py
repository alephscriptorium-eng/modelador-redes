# SPDX-License-Identifier: GPL-3.0-or-later
"""modelador zip — regenera solo los paquetes de descarga."""

from __future__ import annotations

from modelador_redes import __version__
from modelador_redes.modelos.catalogo import cargar_modelo, listar_modelos
from modelador_redes.paths import PUBLIC_DIR
from modelador_redes.site.packs import generar_packs_modelo


def run(modelo_id: str | None = None) -> int:
    ids = [modelo_id] if modelo_id else listar_modelos()
    for i in ids:
        m = cargar_modelo(i)
        salidas = generar_packs_modelo(m, PUBLIC_DIR / "modelos" / m.id / "downloads", __version__)
        for s in salidas:
            print(f"  {s.relative_to(PUBLIC_DIR)}")
    return 0
