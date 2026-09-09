# SPDX-License-Identifier: GPL-3.0-or-later
"""Render markdown → HTML con markdown-it-py (CommonMark + tablas + anclas h2/h3)."""

from __future__ import annotations

import re

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.anchors import anchors_plugin

_PARSER: MarkdownIt | None = None


def parser() -> MarkdownIt:
    global _PARSER
    if _PARSER is None:
        _PARSER = (
            MarkdownIt("commonmark", {"html": True})
            .enable(["table", "strikethrough"])
            .use(anchors_plugin, min_level=2, max_level=3, permalink=False)
        )
    return _PARSER


def _texto_inline(tok: Token) -> str:
    return "".join(c.content for c in (tok.children or []) if c.type in ("text", "code_inline"))


def render(md: str) -> tuple[str, list[dict]]:
    """Devuelve (html, toc). toc = [{nivel, id, texto}] para h2/h3."""
    p = parser()
    tokens = p.parse(md)
    toc: list[dict] = []
    for i, t in enumerate(tokens):
        if t.type == "heading_open" and t.tag in ("h2", "h3") and i + 1 < len(tokens):
            toc.append({"nivel": int(t.tag[1]), "id": t.attrGet("id") or "", "texto": _texto_inline(tokens[i + 1])})
    html = p.renderer.render(tokens, p.options, {})
    html = html.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return html, toc


def render_inline(md: str) -> str:
    return parser().renderInline(md)


ENFASIS_RE = re.compile(r"[*_`]")


def titulo(md: str) -> str | None:
    for linea in md.splitlines():
        if linea.startswith("# "):
            return ENFASIS_RE.sub("", linea[2:]).strip()
    return None
