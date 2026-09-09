# SPDX-License-Identifier: GPL-3.0-or-later
import json

import pytest

from modelador_redes.modelos.catalogo import cargar_modelo, latest_draft, listar_modelos, orden_draft


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
