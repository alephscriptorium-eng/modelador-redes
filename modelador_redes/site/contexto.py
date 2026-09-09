# SPDX-License-Identifier: GPL-3.0-or-later
"""Enlaces relativos para GitHub Pages (sin barra inicial) y enlaces a GitHub."""

from __future__ import annotations

from modelador_redes.paths import GITHUB_BLOB, GITHUB_RAW, GITHUB_TREE


def hrefs(depth: int) -> dict:
    """depth = número de carpetas entre la página y public/."""
    base = "../" * depth
    return {
        "base_href": base,
        "root_href": f"{base}index.html",
        "portal_href": f"{base}index.html",
        "catalogo_href": f"{base}index.html",
        "foss_href": f"{base}foss/index.html",
        "show_inicio": depth > 0,
    }


def doc_links(rel_path: str, zip_href: str | None = None) -> dict:
    """rel_path: ruta POSIX del fichero fuente relativa a la raíz del repo."""
    return {"github": GITHUB_BLOB + rel_path, "raw": GITHUB_RAW + rel_path, "zip": zip_href}


def tree_link(rel_dir: str) -> str:
    return GITHUB_TREE + rel_dir
