# SPDX-License-Identifier: GPL-3.0-or-later
"""modelador check — validaciones de public/ y de los modelos. Exit 1 si algo falla."""

from __future__ import annotations

import posixpath
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from modelador_redes.modelos.catalogo import cargar_todos, validar_grafo
from modelador_redes.modelos.indice import validar
from modelador_redes.paths import MAX_PUBLIC_FILE_BYTES, MODELOS_DIR, PUBLIC_DIR

RESTO_PROHIBIDO = "base/teoria/vendor"


class _Enlaces(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.refs.append(v)


def _es_relativo(ref: str) -> bool:
    u = urlsplit(ref)
    return not u.scheme and not u.netloc and not ref.startswith("#") and not ref.startswith("/")


def enlaces_rotos(public_dir: Path) -> list[str]:
    errores: list[str] = []
    for html in sorted(public_dir.rglob("*.html")):
        p = _Enlaces()
        p.feed(html.read_text(encoding="utf-8"))
        for ref in p.refs:
            if not _es_relativo(ref):
                continue
            ruta = urlsplit(ref).path
            if not ruta:
                continue
            destino = Path(posixpath.normpath(posixpath.join(html.parent.relative_to(public_dir).as_posix(), ruta)))
            abs_dest = public_dir / destino
            if abs_dest.is_dir():
                abs_dest = abs_dest / "index.html"
            if not abs_dest.is_file():
                errores.append(f"{html.relative_to(public_dir)}: enlace roto → {ref}")
    return errores


def restos_prohibidos(public_dir: Path) -> list[str]:
    errores = []
    for f in sorted(public_dir.rglob("*")):
        if f.suffix in (".html", ".md", ".json", ".txt") and f.is_file():
            if RESTO_PROHIBIDO in f.read_text(encoding="utf-8", errors="replace"):
                errores.append(f"{f.relative_to(public_dir)}: contiene {RESTO_PROHIBIDO!r}")
    return errores


def ficheros_grandes(public_dir: Path) -> list[str]:
    return [
        f"{f.relative_to(public_dir)}: {f.stat().st_size // 1024} KB > {MAX_PUBLIC_FILE_BYTES // 1024} KB"
        for f in sorted(public_dir.rglob("*"))
        if f.is_file() and f.stat().st_size > MAX_PUBLIC_FILE_BYTES
    ]


def check(public_dir: Path | None = None, modelos_dir: Path | None = None) -> list[str]:
    public_dir = public_dir or PUBLIC_DIR
    errores: list[str] = []
    try:
        modelos = cargar_todos(modelos_dir or MODELOS_DIR)
        for m in modelos:
            errores.extend(validar(m))
        errores.extend(validar_grafo(modelos))
    except (ValueError, OSError) as e:
        errores.append(f"modelos: {e}")
    if not public_dir.is_dir():
        errores.append(f"{public_dir} no existe: ejecuta `modelador build`")
        return errores
    errores.extend(restos_prohibidos(public_dir))
    errores.extend(enlaces_rotos(public_dir))
    errores.extend(ficheros_grandes(public_dir))
    return errores


def run() -> int:
    errores = check()
    for e in errores:
        print(f"ERROR {e}")
    if errores:
        print(f"{len(errores)} problema(s)")
        return 1
    print("check: OK")
    return 0
