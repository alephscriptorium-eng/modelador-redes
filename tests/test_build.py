# SPDX-License-Identifier: GPL-3.0-or-later
from modelador_redes.cli.build import run_build
from modelador_redes.cli.check import check


def test_build_y_check(modelos_dir, tmp_path):
    public = tmp_path / "public"
    data = tmp_path / "data"
    conteo = run_build("all", public_dir=public, data_dir=data, modelos_dir=modelos_dir)
    # root + (index, backlog, 2 drafts, indice, 1 ficha) + 4 foss
    assert conteo["paginas"] == 1 + 6 + 4
    assert conteo["zips"] == 3
    assert (public / "modelos" / "prueba" / "backlog.json").is_file()
    assert (data / "prueba" / "backlog.json").is_file()
    assert (public / "foss" / "llms.md").is_file()
    assert check(public_dir=public, modelos_dir=modelos_dir) == []
    ficha = (public / "modelos" / "prueba" / "revision" / "01-a.html").read_text()
    assert 'href="../drafts/draftv1.html"' in ficha
    assert "blob/main/modelos/prueba/drafts/draftv1.md#L3" in ficha
    backlog = (public / "modelos" / "prueba" / "backlog.html").read_text()
    assert "OP-01" in backlog and "TK-D01" in backlog and "table-wrap" in backlog


def test_build_es_determinista(modelos_dir, tmp_path):
    public = tmp_path / "public"
    data = tmp_path / "data"
    run_build("all", public_dir=public, data_dir=data, modelos_dir=modelos_dir)
    antes = {p: p.read_bytes() for p in public.rglob("*") if p.is_file()}
    run_build("all", public_dir=public, data_dir=data, modelos_dir=modelos_dir)
    despues = {p: p.read_bytes() for p in public.rglob("*") if p.is_file()}
    assert antes == despues


def test_build_grafo(grafo_dir, tmp_path):
    public = tmp_path / "public"
    data = tmp_path / "data"
    conteo = run_build("all", public_dir=public, data_dir=data, modelos_dir=grafo_dir)
    assert conteo["modelos"] == 3
    assert (public / "catalogo.json").is_file() and (data / "catalogo.json").is_file()
    import json

    cat = json.loads((public / "catalogo.json").read_text())
    assert [n["id"] for n in cat["nodos"]] == ["alfa", "beta"] and cat["aristas"][0]["id"] == "alfa+beta"
    portada = (public / "index.html").read_text()
    assert portada.count("<circle") == 2 and portada.count("<line") == 1
    assert "badge-pausa" in portada
    arista = (public / "modelos" / "alfa+beta" / "index.html").read_text()
    assert 'href="../alfa/index.html"' in arista and "contraste" in arista
    assert check(public_dir=public, modelos_dir=grafo_dir) == []


def test_build_poda_modelos_obsoletos(modelos_dir, tmp_path):
    public = tmp_path / "public"
    data = tmp_path / "data"
    (public / "modelos" / "viejo").mkdir(parents=True)
    (public / "modelos" / "viejo" / "index.html").write_text("x")
    (data / "viejo").mkdir(parents=True)
    run_build("all", public_dir=public, data_dir=data, modelos_dir=modelos_dir)
    assert not (public / "modelos" / "viejo").exists() and not (data / "viejo").exists()
    assert (public / "modelos" / "prueba" / "index.html").is_file()
