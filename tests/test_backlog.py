# SPDX-License-Identifier: GPL-3.0-or-later
from modelador_redes.modelos.backlog import carril, es_backlog, extraer, ops_de_headings, parse_tablas
from modelador_redes.modelos.catalogo import cargar_modelo
from tests.conftest import DRAFT_A, DRAFT_B


def test_tablas_detectadas_y_numericas_excluidas():
    tablas = parse_tablas(DRAFT_A, "draftv0")
    assert len(tablas) == 2
    backlog = [t for t in tablas if es_backlog(t)]
    assert len(backlog) == 1
    t = backlog[0]
    assert t.headers == ["ID", "Tarea", "Dep.", "T", "P"]
    assert t.rows[0][0] == "**TK-01**"
    assert t.rows[0][1] == "Hacer algo con `a | b`"
    assert t.op == "OP-01" and t.kind == "tk" and t.carril == "num"


def test_carriles_D_y_G():
    tablas = [t for t in parse_tablas(DRAFT_B, "draftv1") if es_backlog(t)]
    assert [t.carril for t in tablas] == ["D", "G"]
    assert carril("TK-D01") == "D" and carril("TK-31") == "num" and carril("RP-5") == "RP" and carril("R11") == "R"
    assert carril("TK-D'01") == "D'" and carril("TK-G'06") == "G'" and carril("CL-3") == "CL"


def test_ops_de_headings():
    ops = ops_de_headings(DRAFT_A, "draftv0")
    assert len(ops) == 1
    assert ops[0].id == "OP-01" and ops[0].titulo == "Primera oportunidad"
    assert ops[0].resumen.startswith("Resumen de la primera")


def test_fence_no_produce_tablas():
    assert parse_tablas("```\n| ID | x |\n| :-- | :-- |\n| TK-9 | y |\n```\n", "d") == []


def test_extraer_resumen_acumulado(modelos_dir):
    m = cargar_modelo("prueba", modelos_dir)
    b = extraer(m)
    assert b["latest"] == "draftv1"
    assert b["resumen"]["total_tk"] == 6  # acumulado: TK-01/02 de draftv0 + 4 de draftv1
    assert not any(_r[0].strip("*") == "TK-99" for t in b["tablas"] for _r in t["rows"])
    assert b["resumen"]["por_carril"] == {"D": 2, "G": 2, "num": 2}
    assert b["resumen"]["por_prioridad"] == {"C": 1, "H": 2, "M": 1}
    assert b["resumen"]["ops"] == 1 and b["resumen"]["ops_total"] == 1 and b["resumen"]["ops_latest"] == 0
    assert {t["draft"] for t in b["tablas"]} == {"draftv0", "draftv1"}
