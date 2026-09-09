# SPDX-License-Identifier: GPL-3.0-or-later
"""SVG inline del grafo de modelizaciones: nodos en círculo, aristas como líneas. Sin dependencias."""

from __future__ import annotations

import math
from html import escape


def _posiciones(n: int, cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    if n == 1:
        return [(cx, cy)]
    return [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]


def grafo_svg(grafo: dict, href_base: str = "", ancho: int = 640, alto: int = 360) -> str:
    """grafo = {"nodos": [{id, nombre, estado, latest}], "aristas": [{id, nodos:[a,b], relacion, estado}]}."""
    nodos = grafo.get("nodos", [])
    aristas = grafo.get("aristas", [])
    cx, cy = ancho / 2, alto / 2
    r = min(ancho, alto) * 0.34
    pos = dict(zip((n["id"] for n in nodos), _posiciones(len(nodos), cx, cy, r)))
    partes = [
        f'<svg class="grafo-svg" viewBox="0 0 {ancho} {alto}" role="img" aria-label="Grafo de modelizaciones: {len(nodos)} nodos y {len(aristas)} aristas" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    ]
    for a in aristas:
        ids = a.get("nodos", [])
        if len(ids) != 2 or ids[0] not in pos or ids[1] not in pos:
            continue
        (x1, y1), (x2, y2) = pos[ids[0]], pos[ids[1]]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        href = f"{href_base}modelos/{a['id']}/index.html"
        clase = "arista" + (" arista-pausa" if a.get("estado") == "pausa" else "")
        etiqueta = escape(a.get("relacion") or "arista")
        partes.append(
            f'<a href="{escape(href)}" class="{clase}"><line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
            f'<text x="{mx:.1f}" y="{my - 6:.1f}" text-anchor="middle" class="arista-label">{etiqueta}</text></a>'
        )
    for n in nodos:
        x, y = pos[n["id"]]
        href = f"{href_base}modelos/{n['id']}/index.html"
        titulo = escape(n.get("nombre") or n["id"])
        partes.append(
            f'<a href="{escape(href)}" class="nodo"><title>{titulo}</title><circle cx="{x:.1f}" cy="{y:.1f}" r="22"/>'
            f'<text x="{x:.1f}" y="{y + 40:.1f}" text-anchor="middle" class="nodo-label">{escape(n["id"])}</text></a>'
        )
    partes.append("</svg>")
    return "".join(partes)
