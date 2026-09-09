# SPDX-License-Identifier: GPL-3.0-or-later
"""Reescritura de enlaces markdown, siempre fuera de bloques de código.

- Oasis: `](base/teoria/vendor/oasis/ruta#L1-L2)` → blob/tree en GitHub al SHA auditado.
- Inline code: `` `base/teoria/vendor/oasis/...` `` → `` `vendor/oasis/...` ``.
- Internos: `](x.md)` → `](x.html)` relativo a la página de salida; con `#L…` → blob en main.
"""

from __future__ import annotations

import posixpath
import re
from typing import Callable

from modelador_redes.paths import GITHUB_BLOB, OASIS_REPO, OASIS_SHA

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def _split_fences(md: str) -> list[tuple[bool, str]]:
    """Trocea en segmentos (es_fence, texto) conservando el texto íntegro."""
    segmentos: list[tuple[bool, str]] = []
    buf: list[str] = []
    en_fence = False
    marca = ""
    largo = 0
    for linea in md.splitlines(keepends=True):
        m = FENCE_RE.match(linea)
        if not en_fence and m:
            if buf:
                segmentos.append((False, "".join(buf)))
                buf = []
            en_fence, marca, largo = True, m.group(1)[0], len(m.group(1))
            buf.append(linea)
            continue
        buf.append(linea)
        if en_fence and m and m.group(1)[0] == marca and len(m.group(1)) >= largo and m.group(1) == m.group(1)[0] * len(m.group(1)):
            segmentos.append((True, "".join(buf)))
            buf = []
            en_fence = False
    if buf:
        segmentos.append((en_fence, "".join(buf)))
    return segmentos


def _fuera_de_fences(md: str, fn: Callable[[str], str]) -> str:
    return "".join(seg if es_fence else fn(seg) for es_fence, seg in _split_fences(md))


ANCLA_RE = re.compile(r"^#L(\d+)-(\d+)$")


def normalizar_ancla(ancla: str) -> str:
    m = ANCLA_RE.match(ancla)
    return f"#L{m.group(1)}-L{m.group(2)}" if m else ancla


OASIS_RE = re.compile(r"\]\(base/teoria/vendor/oasis/?([^)#\s]*)(#L\d+(?:-L?\d+)?)?\)")


def reescribir_oasis(md: str, repo: str = OASIS_REPO, sha: str = OASIS_SHA) -> str:
    def sub(m: re.Match) -> str:
        ruta, ancla = m.group(1), m.group(2) or ""
        if ruta == "" or ruta.endswith("/"):
            return f"]({repo}/tree/{sha}/{ruta})"
        return f"]({repo}/blob/{sha}/{ruta}{normalizar_ancla(ancla)})"

    return _fuera_de_fences(md, lambda s: OASIS_RE.sub(sub, s))


INLINE_RE = re.compile(r"`base/teoria/vendor((?:/[^`]*)?)`")


def reescribir_inline_code(md: str) -> str:
    """`base/teoria/vendor/<lo que sea>` → `vendor/<lo que sea>` (Oasis, Faircoin…)."""
    return _fuera_de_fences(md, lambda s: INLINE_RE.sub(r"`vendor\1`", s))


INTERNO_RE = re.compile(r"\]\((?!(?:[a-z][a-z0-9+.-]*:|#|/))([^)\s#]+?\.md)(#[^)\s]*)?\)")


def reescribir_internos(md: str, src_dir: str, out_dir: str, blob_base: str = GITHUB_BLOB) -> str:
    """src_dir/out_dir: rutas POSIX relativas a la raíz del repo (public/ replica modelos/)."""

    def sub(m: re.Match) -> str:
        destino, ancla = m.group(1), m.group(2) or ""
        absoluto = posixpath.normpath(posixpath.join(src_dir, destino))
        if ancla.startswith("#L"):
            return f"]({blob_base}{absoluto}{normalizar_ancla(ancla)})"
        html = absoluto[:-3] + ".html"
        return f"]({posixpath.relpath(html, out_dir)}{ancla})"

    return _fuera_de_fences(md, lambda s: INTERNO_RE.sub(sub, s))


def reescribir_para_web(md: str, src_dir: str, out_dir: str) -> str:
    return reescribir_internos(reescribir_inline_code(reescribir_oasis(md)), src_dir, out_dir)


def reescribir_para_zip(md: str) -> str:
    """Dentro del zip los enlaces relativos .md siguen siendo válidos: solo Oasis."""
    return reescribir_inline_code(reescribir_oasis(md))
