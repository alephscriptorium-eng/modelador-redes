# SPDX-License-Identifier: GPL-3.0-or-later
"""modelador build — genera public/ (catálogo + modelos + foss) y data/<modelo>/backlog.json."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from modelador_redes import __version__
from modelador_redes.modelos.backlog import extraer
from modelador_redes.modelos.catalogo import Modelo, cargar_todos
from modelador_redes.modelos.enlaces import reescribir_para_web
from modelador_redes.modelos.markdown import render, render_inline, titulo
from modelador_redes.paths import (
    DATA_DIR,
    GITHUB_TREE,
    LICENSE,
    LLMS,
    MODELOS_DIR,
    OASIS_REPO,
    OASIS_SHA,
    OASIS_SHORT,
    PUBLIC_DIR,
    SITE_DIR,
)
from modelador_redes.site.brand import brand_context
from modelador_redes.site.contexto import doc_links, hrefs
from modelador_redes.site.packs import KINDS, generar_packs_modelo, nombre_zip


def _jinja_env(subdir: str) -> Environment:
    return Environment(
        loader=FileSystemLoader([str(SITE_DIR / "templates" / subdir), str(SITE_DIR / "templates" / "_partials")]),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _copiar_assets(public_dir: Path) -> None:
    src = SITE_DIR / "assets"
    if src.exists():
        shutil.copytree(src, public_dir / "assets", dirs_exist_ok=True)


def _write(path: Path, texto: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(texto, encoding="utf-8")


def _ctx(depth: int, **extra) -> dict:
    return {"version": __version__, "oasis_repo": OASIS_REPO, "oasis_sha": OASIS_SHA, "oasis_short": OASIS_SHORT, **brand_context(), **hrefs(depth), **extra}


def _rama_actual() -> str:
    try:
        return subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        return ""


def _resumen_modelo(m: Modelo, backlog: dict) -> dict:
    return {
        "id": m.id,
        "nombre": m.nombre,
        "rama": m.rama,
        "estado": m.estado,
        "descripcion": m.descripcion,
        "latest": m.latest,
        "n_drafts": len(m.drafts),
        "n_fichas": len(m.fichas),
        "total_tk": backlog["resumen"]["total_tk"],
        "ops": backlog["resumen"]["ops_latest"],
        "github": GITHUB_TREE + m.rel_dir,
    }


def _documento(env: Environment, m: Modelo, src: Path, tipo: str, out_html: Path, ctx_base: dict, zip_kind: str) -> None:
    src_dir = f"{m.rel_dir}/{src.parent.name}"
    md = src.read_text(encoding="utf-8")
    html, toc = render(reescribir_para_web(md, src_dir, src_dir))
    ctx = {
        **ctx_base,
        "pagina": src.stem,
        "tipo": tipo,
        "titulo": titulo(md) or src.stem,
        "nombre_fichero": src.name,
        "es_latest": tipo == "draft" and src.stem == m.latest,
        "contenido": html,
        "toc": toc,
        "links": doc_links(f"{src_dir}/{src.name}", f"../downloads/{nombre_zip(m.id, zip_kind)}"),
    }
    _write(out_html, env.get_template("documento.html").render(**ctx))


def build_modelo(m: Modelo, public_dir: Path, data_dir: Path) -> int:
    env = _jinja_env("modelo")
    out = public_dir / "modelos" / m.id
    for sub in ("drafts", "revision", "downloads"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    backlog = extraer(m)
    _write(data_dir / m.id / "backlog.json", json.dumps(backlog, ensure_ascii=False, indent=2) + "\n")
    shutil.copy(data_dir / m.id / "backlog.json", out / "backlog.json")
    generar_packs_modelo(m, out / "downloads", __version__)

    nav = {
        "drafts": [{"nombre": p.stem, "latest": p.stem == m.latest} for p in reversed(m.drafts)],
        "fichas": [{"nombre": f.stem, "titulo": titulo(f.read_text(encoding="utf-8")) or f.stem} for f in m.fichas],
        "zips": [{"kind": k, "nombre": nombre_zip(m.id, k)} for k in KINDS],
    }
    comun = {"modelo": m, "nav": nav, "modelo_github": GITHUB_TREE + m.rel_dir, "resumen": backlog["resumen"]}
    paginas = 0

    # Estado (índice de revisión renderizado en la raíz del modelo)
    if m.indice is not None:
        md = m.indice.read_text(encoding="utf-8")
        html, toc = render(reescribir_para_web(md, f"{m.rel_dir}/revision", m.rel_dir))
        links = doc_links(f"{m.rel_dir}/revision/{m.indice.name}", f"downloads/{nombre_zip(m.id, 'revision')}")
        tit = titulo(md)
    else:
        html, toc, links, tit = "", [], None, None
    _write(out / "index.html", env.get_template("index.html").render(**_ctx(2, mhref="", pagina="index", contenido=html, toc=toc, links=links, titulo_indice=tit, **comun)))
    paginas += 1

    # Backlog
    ops = sorted(backlog["ops"], key=lambda o: (backlog["drafts"].index(o["draft"]), o["id"]), reverse=True)
    ops_html = [{**o, "titulo_html": render_inline(o["titulo"]), "resumen_html": render_inline(reescribir_para_web(o["resumen"], f"{m.rel_dir}/drafts", m.rel_dir))} for o in ops]
    tablas_html = []
    for t in backlog["tablas"]:
        celdas = [[render_inline(reescribir_para_web(c, f"{m.rel_dir}/drafts", m.rel_dir)) for c in fila] for fila in t["rows"]]
        tablas_html.append({**t, "headers_html": [render_inline(h) for h in t["headers"]], "rows_html": celdas})
    tablas_html.sort(key=lambda t: (backlog["drafts"].index(t["draft"]),), reverse=True)
    _write(out / "backlog.html", env.get_template("backlog.html").render(**_ctx(2, mhref="", pagina="backlog", ops=ops_html, tablas=tablas_html, backlog=backlog, **comun)))
    paginas += 1

    ctx3 = _ctx(3, mhref="../", **comun)
    for d in m.drafts:
        _documento(env, m, d, "draft", out / "drafts" / f"{d.stem}.html", ctx3, "drafts")
        paginas += 1
    fichas = ([m.indice] if m.indice else []) + list(m.fichas)
    for f in fichas:
        _documento(env, m, f, "indice" if f == m.indice else "ficha", out / "revision" / f"{f.stem}.html", ctx3, "revision")
        paginas += 1
    return paginas


def build_root(modelos: list[Modelo], resumenes: list[dict], public_dir: Path) -> None:
    env = _jinja_env("root")
    _write(public_dir / "index.html", env.get_template("index.html").render(**_ctx(0, modelos=resumenes)))


def build_foss(resumenes: list[dict], public_dir: Path) -> int:
    env = _jinja_env("foss")
    out = public_dir / "foss"
    out.mkdir(parents=True, exist_ok=True)
    if LLMS.exists():
        shutil.copy(LLMS, out / "llms.md")
    ctx = _ctx(1, modelos=resumenes, license_text=LICENSE.read_text(encoding="utf-8") if LICENSE.exists() else "")
    paginas = ["index.html", "tecnico.html", "devops.html", "LICENSE.html"]
    for p in paginas:
        _write(out / p, env.get_template(p).render(**ctx, pagina=p[:-5]))
    return len(paginas)


def run_build(target: str = "all", public_dir: Path | None = None, data_dir: Path | None = None, modelos_dir: Path | None = None) -> dict:
    public_dir = public_dir or PUBLIC_DIR
    data_dir = data_dir or DATA_DIR
    rama = _rama_actual()
    if rama.startswith("dev/"):
        print(f"AVISO: estás en {rama}. public/ y data/ solo se commitean en main (ver llms.md).")
    modelos = cargar_todos(modelos_dir or MODELOS_DIR)
    if not modelos:
        raise FileNotFoundError("No hay modelos en modelos/")
    public_dir.mkdir(parents=True, exist_ok=True)
    _copiar_assets(public_dir)
    resumenes = [_resumen_modelo(m, extraer(m)) for m in modelos]
    conteo = {"paginas": 0, "zips": 0, "modelos": len(modelos)}
    if target in ("all", "catalogo"):
        build_root(modelos, resumenes, public_dir)
        conteo["paginas"] += 1
        for m in modelos:
            conteo["paginas"] += build_modelo(m, public_dir, data_dir)
            conteo["zips"] += len(KINDS)
            print(f"  modelo {m.id}: latest={m.latest}, {len(m.drafts)} drafts, {len(m.fichas)} fichas")
    if target in ("all", "foss"):
        conteo["paginas"] += build_foss(resumenes, public_dir)
    print(f"Generado en {public_dir}: {conteo['paginas']} páginas, {conteo['zips']} zips, {conteo['modelos']} modelos")
    return conteo
