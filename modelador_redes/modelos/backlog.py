# SPDX-License-Identifier: GPL-3.0-or-later
"""Extracción tolerante del backlog de los drafts de un modelo.

No hay un backlog.md canónico: cada draft tiene tablas con formas distintas
(`ID | Buscar | Dónde | Default | …`, `ID | Tarea | Depende | Seam | T | P`,
`ID | Tarea | Default | Alternativas`, tablas RP…). Se recoge toda tabla cuya
primera celda de fila sea un identificador (TK-, OP-, RP-, Rn) y se guardan
las celdas como markdown. Las oportunidades OP-xx son encabezados con su
primer párrafo.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import asdict, dataclass, field

from modelador_redes.modelos.catalogo import Modelo
from modelador_redes.modelos.enlaces import _split_fences, reescribir_para_zip


@dataclass
class Tabla:
    draft: str
    seccion: str
    op: str | None
    kind: str
    carril: str
    headers: list[str]
    rows: list[list[str]] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)


@dataclass
class Op:
    draft: str
    id: str
    titulo: str
    resumen: str


ID_RE = re.compile(r"^(?:(?:TK|OP|RP|CL|EU)-[A-Za-z0-9.']+|R\d+)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
OP_HEAD_RE = re.compile(r"^#{2,6}\s*\**\s*(OP-\d+)\**\s*[:·—–-]?\s*(.*?)\s*\**\s*$")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")
LIMPIA_RE = re.compile(r"[*`_ ]")


def _limpiar_id(celda: str) -> str:
    return LIMPIA_RE.sub("", celda.strip())


def _split_row(linea: str) -> list[str]:
    s = linea.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    celdas = re.split(r"(?<!\\)\|", s)
    return [c.replace("\\|", "|").strip() for c in celdas]


def _es_fila(linea: str) -> bool:
    return "|" in linea and linea.strip() != "" and not linea.lstrip().startswith("#")


def carril(id_: str) -> str:
    m = re.match(r"^TK-([A-Z]+'?)\d", id_)
    if m:
        return m.group(1)
    if re.match(r"^TK-\d", id_):
        return "num"
    if id_.startswith("OP-"):
        return "OP"
    if id_.startswith("RP-"):
        return "RP"
    if re.match(r"^R\d+$", id_):
        return "R"
    m = re.match(r"^([A-Z]+)-", id_)
    return m.group(1) if m else "?"


def kind_de(ids: list[str]) -> str:
    c = Counter(carril(i) for i in ids)
    top = c.most_common(1)[0][0] if c else "?"
    if top in ("OP", "RP", "R"):
        return {"OP": "op", "RP": "rp", "R": "riesgo"}[top]
    return "tk"


def parse_tablas(md: str, draft: str) -> list[Tabla]:
    tablas: list[Tabla] = []
    seccion = ""
    op_actual: str | None = None
    for es_fence, seg in _split_fences(md):
        if es_fence:
            continue
        lineas = seg.split("\n")
        i = 0
        while i < len(lineas):
            linea = lineas[i]
            h = HEADING_RE.match(linea)
            if h:
                seccion = h.group(2)
                om = OP_HEAD_RE.match(linea)
                op_actual = om.group(1) if om else (op_actual if len(h.group(1)) > 3 else None)
                i += 1
                continue
            if _es_fila(linea) and i + 1 < len(lineas) and SEP_RE.match(lineas[i + 1]) and "|" in lineas[i + 1]:
                headers = _split_row(linea)
                rows: list[list[str]] = []
                avisos: list[str] = []
                j = i + 2
                while j < len(lineas) and _es_fila(lineas[j]):
                    fila = _split_row(lineas[j])
                    if len(fila) != len(headers):
                        avisos.append(f"fila {j + 1}: {len(fila)} celdas, esperadas {len(headers)}")
                        fila = (fila + [""] * len(headers))[: len(headers)]
                    rows.append(fila)
                    j += 1
                ids = [_limpiar_id(r[0]) for r in rows if r]
                ids_validos = [x for x in ids if ID_RE.match(x)]
                tablas.append(
                    Tabla(
                        draft=draft,
                        seccion=seccion,
                        op=op_actual,
                        kind=kind_de(ids_validos),
                        carril=Counter(carril(x) for x in ids_validos).most_common(1)[0][0] if ids_validos else "?",
                        headers=headers,
                        rows=rows,
                        avisos=avisos,
                    )
                )
                i = j
                continue
            i += 1
    return tablas


def es_backlog(t: Tabla) -> bool:
    if not t.rows:
        return False
    primera = _limpiar_id(t.headers[0]).upper() if t.headers else ""
    if primera not in ("ID", "#", "OP", "TAREA", "RP", "TK"):
        return False
    return any(ID_RE.match(_limpiar_id(r[0])) for r in t.rows if r)


def ops_de_headings(md: str, draft: str) -> list[Op]:
    ops: list[Op] = []
    for es_fence, seg in _split_fences(md):
        if es_fence:
            continue
        lineas = seg.split("\n")
        for i, linea in enumerate(lineas):
            m = OP_HEAD_RE.match(linea)
            if not m:
                continue
            resumen = ""
            for sig in lineas[i + 1:]:
                if HEADING_RE.match(sig):
                    break
                s = sig.strip()
                if not s or s.startswith("|") or SEP_RE.match(s):
                    if resumen:
                        break
                    continue
                resumen = (resumen + " " + s).strip()
                if len(resumen) > 400:
                    break
            ops.append(Op(draft=draft, id=m.group(1), titulo=m.group(2).strip(" *"), resumen=resumen[:600]))
    return ops


def _col_prioridad(headers: list[str]) -> int | None:
    for i, h in enumerate(headers):
        if _limpiar_id(h).upper() in ("P", "PRIORIDAD"):
            return i
    return None


def extraer(modelo: Modelo) -> dict:
    ops: list[Op] = []
    tablas: list[Tabla] = []
    for d in modelo.drafts:
        # Las celdas se guardan en markdown, ya con los enlaces al vendor reescritos a GitHub
        md = reescribir_para_zip(d.read_text(encoding="utf-8"))
        ops.extend(ops_de_headings(md, d.stem))
        tablas.extend(t for t in parse_tablas(md, d.stem) if es_backlog(t))
    # El backlog es acumulativo: un draft posterior no reescribe el anterior, solo
    # sustituye las tareas que vuelve a declarar. Se recorre del draft más reciente
    # al más antiguo y cada ID cuenta una sola vez, con su declaración más reciente.
    latest = modelo.latest
    orden = {d.stem: i for i, d in enumerate(modelo.drafts)}
    vistos: set[str] = set()
    por_carril: Counter = Counter()
    por_prioridad: Counter = Counter()
    for t in sorted(tablas, key=lambda t: orden.get(t.draft, -1), reverse=True):
        pcol = _col_prioridad(t.headers)
        for r in t.rows:
            id_ = _limpiar_id(r[0])
            if not id_.startswith("TK-") or id_ in vistos:
                continue
            vistos.add(id_)
            por_carril[carril(id_)] += 1
            if pcol is not None:
                por_prioridad[_limpiar_id(r[pcol]) or "—"] += 1
    ops_unicos: set[str] = set()
    for o in sorted(ops, key=lambda o: orden.get(o.draft, -1), reverse=True):
        ops_unicos.add(o.id)
    resumen = {
        "total_tk": len(vistos),
        "por_carril": dict(sorted(por_carril.items())),
        "por_prioridad": dict(sorted(por_prioridad.items())),
        "ops": len(ops_unicos),
        "ops_latest": sum(1 for o in ops if o.draft == latest),
        "ops_total": len(ops),
        "tablas_total": len(tablas),
    }
    return {
        "modelo": modelo.id,
        "latest": latest,
        "drafts": [p.stem for p in modelo.drafts],
        "ops": [asdict(o) for o in ops],
        "tablas": [asdict(t) for t in tablas],
        "resumen": resumen,
    }
