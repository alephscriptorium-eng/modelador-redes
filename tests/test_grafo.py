# SPDX-License-Identifier: GPL-3.0-or-later
from modelador_redes.site.grafo import grafo_svg


def test_svg_nodos_y_aristas():
    g = {
        "nodos": [{"id": "a", "nombre": "A"}, {"id": "b", "nombre": "B"}, {"id": "c", "nombre": "C"}],
        "aristas": [{"id": "a+b", "nodos": ["a", "b"], "relacion": "contraste", "estado": "pausa"}],
    }
    svg = grafo_svg(g, "../")
    assert svg.count("<circle") == 3
    assert svg.count("<line") == 1
    assert 'href="../modelos/a+b/index.html"' in svg
    assert "arista-pausa" in svg and "contraste" in svg


def test_svg_arista_con_nodo_desconocido_se_omite():
    svg = grafo_svg({"nodos": [{"id": "a", "nombre": "A"}], "aristas": [{"id": "a+z", "nodos": ["a", "z"]}]}, "")
    assert svg.count("<line") == 0 and svg.count("<circle") == 1
