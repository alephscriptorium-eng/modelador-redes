# SPDX-License-Identifier: GPL-3.0-or-later
from modelador_redes.modelos.catalogo import cargar_modelo
from modelador_redes.modelos.indice import escribir_latest, leer_latest, linea_latest, validar


def test_leer_y_escribir(modelos_dir):
    m = cargar_modelo("prueba", modelos_dir)
    assert leer_latest(m.indice.read_text()) == "draftv1"
    assert validar(m) == []
    (modelos_dir / "prueba" / "drafts" / "draftv2.md").write_text("# v2\n")
    m = cargar_modelo("prueba", modelos_dir)
    assert len(validar(m)) == 1 and "draftv2" in validar(m)[0]
    assert escribir_latest(m.indice, m.latest) is True
    assert escribir_latest(m.indice, m.latest) is False
    assert leer_latest(m.indice.read_text()) == "draftv2"
    assert validar(cargar_modelo("prueba", modelos_dir)) == []


def test_insertar_si_falta(tmp_path):
    p = tmp_path / "00-indice.md"
    p.write_text("# Título\n\nTexto.\n")
    assert escribir_latest(p, "draftv3") is True
    assert p.read_text().split("\n")[:3] == ["# Título", "", linea_latest("draftv3")]
