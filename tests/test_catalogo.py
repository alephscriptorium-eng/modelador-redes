# SPDX-License-Identifier: GPL-3.0-or-later
import json

import pytest

from modelador_redes.modelos.catalogo import aristas_de, cargar_modelo, cargar_todos, grafo, latest_draft, listar_modelos, orden_draft, validar_grafo
from tests.conftest import crear_modelo


def test_orden_draft():
    assert orden_draft("draft") == (0, 0)
    assert orden_draft("draftv0.md") == (1, 0)
    assert orden_draft("draftv10") > orden_draft("draftv2") > orden_draft("draft")
    with pytest.raises(ValueError):
        orden_draft("borrador")


def test_cargar_modelo(modelos_dir):
    assert listar_modelos(modelos_dir) == ["prueba"]
    m = cargar_modelo("prueba", modelos_dir)
    assert [p.stem for p in m.drafts] == ["draftv0", "draftv1"]
    assert m.latest == "draftv1"
    assert [f.name for f in m.fichas] == ["01-a.md"]
    assert m.indice is not None and m.indice.name == "00-indice.md"
    assert m.rel_dir == "modelos/prueba"


def test_latest_vacio():
    assert latest_draft([]) is None


def test_modelo_json_invalido(modelos_dir):
    (modelos_dir / "prueba" / "modelo.json").write_text(json.dumps({"id": "otro", "nombre": "x", "rama": "r", "estado": "e", "descripcion": "d"}))
    with pytest.raises(ValueError):
        cargar_modelo("prueba", modelos_dir)


def test_nodo_por_defecto(modelos_dir):
    m = cargar_modelo("prueba", modelos_dir)
    assert m.tipo == "nodo" and m.nodos == [] and not m.es_arista


def test_arista_valida_y_grafo(grafo_dir):
    modelos = cargar_todos(grafo_dir)
    a = cargar_modelo("alfa+beta", grafo_dir)
    assert a.es_arista and a.nodos == ["alfa", "beta"] and a.relacion == "contraste"
    assert [x.id for x in aristas_de("alfa", modelos)] == ["alfa+beta"]
    assert validar_grafo(modelos) == []
    g = grafo(modelos)
    assert [n["id"] for n in g["nodos"]] == ["alfa", "beta"]
    assert g["nodos"][0]["aristas"] == ["alfa+beta"]
    assert g["aristas"][0]["estado"] == "pausa"


def test_arista_invalida(tmp_path):
    base = tmp_path / "m"
    with pytest.raises(ValueError):
        crear_modelo(base, "x+y", extra={"tipo": "arista", "nodos": ["x"]}); cargar_modelo("x+y", base)
    base2 = tmp_path / "m2"
    with pytest.raises(ValueError):
        crear_modelo(base2, "mal", extra={"tipo": "arista", "nodos": ["a", "b"]}); cargar_modelo("mal", base2)
    base3 = tmp_path / "m3"
    with pytest.raises(ValueError):
        crear_modelo(base3, "a+b", extra={"nodos": ["a", "b"]}); cargar_modelo("a+b", base3)


def test_arista_a_nodo_inexistente(grafo_dir):
    crear_modelo(grafo_dir, "alfa+gamma", extra={"tipo": "arista", "nodos": ["alfa", "gamma"]})
    errores = validar_grafo(cargar_todos(grafo_dir))
    assert len(errores) == 1 and "gamma" in errores[0]
