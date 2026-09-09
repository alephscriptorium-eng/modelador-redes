# SPDX-License-Identifier: GPL-3.0-or-later
import zipfile

from modelador_redes.modelos.catalogo import cargar_modelo
from modelador_redes.site.packs import generar_packs_modelo


def test_zips_deterministas_y_contenido(modelos_dir, tmp_path):
    m = cargar_modelo("prueba", modelos_dir)
    a = generar_packs_modelo(m, tmp_path / "a", "0.0")
    b = generar_packs_modelo(m, tmp_path / "b", "0.0")
    assert [p.name for p in a] == ["prueba-drafts.zip", "prueba-revision.zip", "prueba-todo.zip"]
    for x, y in zip(a, b):
        assert x.read_bytes() == y.read_bytes()
    with zipfile.ZipFile(a[2]) as zf:
        names = zf.namelist()
        assert names[0] == "README.txt"
        assert "drafts/draftv1.md" in names and "revision/00-indice.md" in names and "modelo.json" in names
        md = zf.read("drafts/draftv0.md").decode()
        assert "base/teoria/vendor" not in md and "blob/" in md
        assert all(zi.date_time == (1980, 1, 1, 0, 0, 0) for zi in zf.infolist())
