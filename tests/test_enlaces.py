# SPDX-License-Identifier: GPL-3.0-or-later
from modelador_redes.modelos.enlaces import (
    _split_fences,
    reescribir_inline_code,
    reescribir_internos,
    reescribir_oasis,
    reescribir_para_web,
)
from modelador_redes.paths import OASIS_REPO, OASIS_SHA

B = f"{OASIS_REPO}/blob/{OASIS_SHA}/"
T = f"{OASIS_REPO}/tree/{OASIS_SHA}/"


def test_fichero_y_anclas():
    assert reescribir_oasis("[x](base/teoria/vendor/oasis/src/a.js)") == f"[x]({B}src/a.js)"
    assert reescribir_oasis("[x](base/teoria/vendor/oasis/src/a.js#L5)") == f"[x]({B}src/a.js#L5)"
    assert reescribir_oasis("[x](base/teoria/vendor/oasis/src/a.js#L17-L26)") == f"[x]({B}src/a.js#L17-L26)"


def test_ancla_sin_L_se_normaliza():
    assert reescribir_oasis("[x](base/teoria/vendor/oasis/src/a.js#L28-38)") == f"[x]({B}src/a.js#L28-L38)"


def test_directorios_van_a_tree():
    assert reescribir_oasis("[d](base/teoria/vendor/oasis/src/models/)") == f"[d]({T}src/models/)"
    assert reescribir_oasis("[r](base/teoria/vendor/oasis)") == f"[r]({T})"


def test_fences_intactos():
    md = "a [x](base/teoria/vendor/oasis/a.js)\n```\n[y](base/teoria/vendor/oasis/b.js)\n```\n[z](base/teoria/vendor/oasis/c.js)\n"
    out = reescribir_oasis(md)
    assert "[y](base/teoria/vendor/oasis/b.js)" in out
    assert f"[x]({B}a.js)" in out and f"[z]({B}c.js)" in out
    assert len(_split_fences(md)) == 3


def test_inline_code():
    assert reescribir_inline_code("`base/teoria/vendor/oasis/src/x.js`") == "`vendor/oasis/src/x.js`"
    assert reescribir_inline_code("`base/teoria/vendor/oasis`") == "`vendor/oasis`"


def test_internos_html_y_blob():
    md = "[a](../drafts/draftv2.md) [b](../drafts/draftv2.md#L58) [c](01-x.md#sec) [h](https://e.com/x.md)"
    out = reescribir_internos(md, "modelos/m/revision", "modelos/m/revision", blob_base="https://gh/blob/main/")
    assert "[a](../drafts/draftv2.html)" in out
    assert "[b](https://gh/blob/main/modelos/m/drafts/draftv2.md#L58)" in out
    assert "[c](01-x.html#sec)" in out
    assert "[h](https://e.com/x.md)" in out


def test_internos_salida_en_otro_directorio():
    out = reescribir_internos("[a](01-x.md) [b](../drafts/draftv2.md)", "modelos/m/revision", "modelos/m")
    assert "[a](revision/01-x.html)" in out and "[b](drafts/draftv2.html)" in out


def test_para_web_no_deja_rutas_locales():
    out = reescribir_para_web("[x](base/teoria/vendor/oasis/README.md) `base/teoria/vendor/oasis`", "m/d", "m/d")
    assert "base/teoria/vendor" not in out
