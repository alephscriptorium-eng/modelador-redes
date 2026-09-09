# SPDX-License-Identifier: GPL-3.0-or-later
"""Paquetes ZIP deterministas por modelo: -drafts, -revision, -todo."""

from __future__ import annotations

import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from modelador_redes.modelos.catalogo import Modelo
from modelador_redes.modelos.enlaces import reescribir_para_zip
from modelador_redes.paths import GITHUB_REPO, OASIS_REPO, OASIS_SHA

FECHA_FIJA = (1980, 1, 1, 0, 0, 0)
KINDS = ("drafts", "revision", "todo")


@dataclass
class PackContents:
    generated: list[tuple[str, str]] = field(default_factory=list)  # (arcname, texto)

    def arcnames(self) -> list[str]:
        return sorted(arc for arc, _ in self.generated)


def contenidos_modelo(modelo: Modelo, kind: str) -> PackContents:
    c = PackContents()
    if kind in ("drafts", "todo"):
        for d in modelo.drafts:
            c.generated.append((f"drafts/{d.name}", reescribir_para_zip(d.read_text(encoding="utf-8"))))
    if kind in ("revision", "todo"):
        fichas = ([modelo.indice] if modelo.indice else []) + list(modelo.fichas)
        for f in fichas:
            c.generated.append((f"revision/{f.name}", reescribir_para_zip(f.read_text(encoding="utf-8"))))
    if kind == "todo":
        c.generated.append(("modelo.json", (modelo.dir / "modelo.json").read_text(encoding="utf-8")))
    return c


def generar_readme(modelo: Modelo, kind: str, version: str, arcnames: list[str]) -> str:
    titulos = {
        "drafts": "Drafts (borradores sucesivos, el de sufijo mayor es el vigente)",
        "revision": "Revisión (índice de estado + fichas)",
        "todo": "Paquete completo del modelo",
    }
    lineas = [
        f"{modelo.nombre} — {titulos[kind]}",
        f"Modelo: {modelo.id} · rama {modelo.rama} · estado: {modelo.estado}",
        f"Draft vigente: {modelo.latest}.md",
        f"Modelador de Redes v{version} · {GITHUB_REPO}",
        "Licencia del contenido: GPL-3.0-or-later AND LicenseRef-Animus-Iocandi",
        "",
        f"Los enlaces a Oasis apuntan a {OASIS_REPO} en el commit auditado {OASIS_SHA}.",
        "Oasis (AGPL-3.0) no se incluye en este paquete.",
        "",
        "Archivos incluidos:",
    ]
    lineas.extend(f"  - {a}" for a in arcnames)
    lineas.append("")
    lineas.append("Generado con `modelador build`. Fuente canónica: el repositorio.")
    return "\n".join(lineas) + "\n"


def escribir_zip(dest: Path, contents: PackContents, readme: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    entradas = [("README.txt", readme)] + sorted(contents.generated)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for arcname, texto in entradas:
            zi = zipfile.ZipInfo(arcname, date_time=FECHA_FIJA)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            zf.writestr(zi, texto.encode("utf-8"))


def nombre_zip(modelo_id: str, kind: str) -> str:
    return f"{modelo_id}-{kind}.zip"


def generar_packs_modelo(modelo: Modelo, dest_dir: Path, version: str) -> list[Path]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    salidas: list[Path] = []
    for kind in KINDS:
        contents = contenidos_modelo(modelo, kind)
        dest = dest_dir / nombre_zip(modelo.id, kind)
        escribir_zip(dest, contents, generar_readme(modelo, kind, version, contents.arcnames()))
        salidas.append(dest)
    return salidas
