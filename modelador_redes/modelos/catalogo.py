# SPDX-License-Identifier: GPL-3.0-or-later
"""Catálogo de modelos: descubrimiento por convención de ficheros.

Un modelo es una carpeta `modelos/<id>/` con `modelo.json` (id, nombre, rama,
estado, descripcion). Drafts, latest y fichas se derivan del disco:

- drafts: `drafts/draft.md`, `drafts/draftv0.md`, `drafts/draftv1.md`, …
  ordenados numéricamente por sufijo (draft < draftv0 < … < draftv10).
- latest: el draft de sufijo mayor.
- fichas: `revision/NN-*.md`; `00-indice.md` es la página de estado.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from modelador_redes.paths import MODELOS_DIR

DRAFT_RE = re.compile(r"^draft(?:v(\d+))?$")
FICHA_GLOB = "[0-9][0-9]-*.md"
INDICE_NOMBRE = "00-indice.md"
CAMPOS = ("id", "nombre", "rama", "estado", "descripcion")
TIPOS = ("nodo", "arista")
SEP_ARISTA = "+"


@dataclass
class Modelo:
    id: str
    nombre: str
    rama: str
    estado: str
    descripcion: str
    dir: Path
    tipo: str = "nodo"
    nodos: list[str] = field(default_factory=list)
    relacion: str = ""
    drafts: list[Path] = field(default_factory=list)
    fichas: list[Path] = field(default_factory=list)
    indice: Path | None = None

    @property
    def es_arista(self) -> bool:
        return self.tipo == "arista"

    @property
    def latest(self) -> str | None:
        return latest_draft(self.drafts)

    @property
    def rel_dir(self) -> str:
        return f"modelos/{self.id}"


def orden_draft(nombre: str) -> tuple[int, int]:
    """Clave de orden: draft → (0,0); draftvN → (1,N). Lanza si no es draft."""
    stem = nombre[:-3] if nombre.endswith(".md") else nombre
    m = DRAFT_RE.match(stem)
    if not m:
        raise ValueError(f"nombre de draft no reconocido: {nombre!r}")
    return (0, 0) if m.group(1) is None else (1, int(m.group(1)))


def es_draft(path: Path) -> bool:
    return path.suffix == ".md" and DRAFT_RE.match(path.stem) is not None


def listar_drafts(dir_drafts: Path) -> list[Path]:
    if not dir_drafts.is_dir():
        return []
    return sorted((p for p in dir_drafts.glob("*.md") if es_draft(p)), key=lambda p: orden_draft(p.stem))


def latest_draft(drafts: list[Path]) -> str | None:
    if not drafts:
        return None
    return max(drafts, key=lambda p: orden_draft(p.stem)).stem


def listar_modelos(modelos_dir: Path | None = None) -> list[str]:
    base = modelos_dir or MODELOS_DIR
    if not base.is_dir():
        return []
    return sorted(p.name for p in base.iterdir() if (p / "modelo.json").is_file())


def cargar_modelo(modelo_id: str, modelos_dir: Path | None = None) -> Modelo:
    base = (modelos_dir or MODELOS_DIR) / modelo_id
    meta_path = base / "modelo.json"
    with open(meta_path, encoding="utf-8") as f:
        meta = json.load(f)
    faltan = [c for c in CAMPOS if c not in meta or not isinstance(meta[c], str) or not meta[c].strip()]
    if faltan:
        raise ValueError(f"{meta_path}: faltan campos {faltan}")
    if meta["id"] != modelo_id:
        raise ValueError(f"{meta_path}: id {meta['id']!r} no coincide con la carpeta {modelo_id!r}")
    tipo = meta.get("tipo", "nodo")
    if tipo not in TIPOS:
        raise ValueError(f"{meta_path}: tipo {tipo!r} no es {TIPOS}")
    nodos = list(meta.get("nodos", []))
    if tipo == "arista":
        if len(nodos) != 2 or any(not isinstance(n, str) or not n for n in nodos):
            raise ValueError(f"{meta_path}: una arista necesita exactamente dos nodos")
        if meta["id"] != SEP_ARISTA.join(nodos):
            raise ValueError(f"{meta_path}: el id de una arista es '{SEP_ARISTA.join(nodos)}'")
    else:
        if nodos:
            raise ValueError(f"{meta_path}: un nodo no declara 'nodos'")
        if SEP_ARISTA in meta["id"]:
            raise ValueError(f"{meta_path}: el id de un nodo no lleva '{SEP_ARISTA}'")
    rev = base / "revision"
    fichas = sorted(rev.glob(FICHA_GLOB)) if rev.is_dir() else []
    indice = rev / INDICE_NOMBRE
    return Modelo(
        id=meta["id"],
        nombre=meta["nombre"],
        rama=meta["rama"],
        estado=meta["estado"],
        descripcion=meta["descripcion"],
        dir=base,
        tipo=tipo,
        nodos=nodos,
        relacion=str(meta.get("relacion", "")),
        drafts=listar_drafts(base / "drafts"),
        fichas=[f for f in fichas if f.name != INDICE_NOMBRE],
        indice=indice if indice.is_file() else None,
    )


def cargar_todos(modelos_dir: Path | None = None) -> list[Modelo]:
    return [cargar_modelo(i, modelos_dir) for i in listar_modelos(modelos_dir)]


def aristas_de(nodo_id: str, modelos: list[Modelo]) -> list[Modelo]:
    return [m for m in modelos if m.es_arista and nodo_id in m.nodos]


def validar_grafo(modelos: list[Modelo]) -> list[str]:
    ids_nodos = {m.id for m in modelos if not m.es_arista}
    errores: list[str] = []
    for m in modelos:
        if m.es_arista:
            for n in m.nodos:
                if n not in ids_nodos:
                    errores.append(f"{m.id}: la arista apunta al nodo {n!r}, que no existe")
            if m.nodos[0] == m.nodos[1]:
                errores.append(f"{m.id}: una arista une dos nodos distintos")
    return errores


def grafo(modelos: list[Modelo]) -> dict:
    """Representación serializable del catálogo como grafo."""
    nodos = [
        {
            "id": m.id,
            "nombre": m.nombre,
            "rama": m.rama,
            "estado": m.estado,
            "latest": m.latest,
            "aristas": [a.id for a in aristas_de(m.id, modelos)],
        }
        for m in modelos
        if not m.es_arista
    ]
    aristas = [
        {"id": m.id, "nombre": m.nombre, "nodos": list(m.nodos), "relacion": m.relacion, "rama": m.rama, "estado": m.estado, "latest": m.latest}
        for m in modelos
        if m.es_arista
    ]
    return {"nodos": nodos, "aristas": aristas}
