Reconstrucción de memoria, no verbatim. Es el capítulo que peor conozco: casi todo en **B/C**. Confírmalo en pp. 404-420.

**Puntos principales del cap. IV «Presidencia del Consejo de Legislación» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | Tres presidencias (Legislación, Justicia, Gobierno) con **la misma legitimidad de origen** pero de fuentes distintas: la de Legislación nace de la **Cámara**, que elige a su presidente por mayoría absoluta | B (divulgación nodulo) |
| 2 | El presidente **nombra su Consejo**; mismo patrón que en Justicia y Gobierno | B |
| 3 | Función: dar a la ley la **fuerza coactiva**. La Cámara decide el contenido (fuerza directiva); el Consejo lo convierte en norma obligatoria: sanción, promulgación, forma jurídica | A/B |
| 4 | Redacción técnica, **codificación** y coherencia del ordenamiento; vela por que la ley sea general y no medida | C |
| 5 | Puede **devolver** la ley a la Cámara para nueva deliberación (veto suspensivo), no bloquearla indefinidamente | C |
| 6 | El presidente de Legislación **no es el gobierno**: no ejecuta ni administra; separa el poder de hacer ley del de aplicarla | B |
| 7 | Mandato fijo e incompatibilidad con el escaño de representante | C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 1, 3, 5 → [TK-D05](../drafts/draftv2.md#L55) / [TK-G05](../drafts/draftv2.md#L79) (Cámara elige, Consejo promulga, veto suspensivo como alternativa). Tesis 6 → arquitectura del carril G ([línea 71](../drafts/draftv2.md#L71)): Legislación promulga, Gobierno ejecuta.
-   **Desviación del patrón:** el default de D05 decía «k representantes elegidos por la Cámara», un colegio sin presidente. El libro y D07 (Justicia) siguen el patrón **presidente elegido → nombra Consejo** (tesis 2). D05 era la excepción sin justificarlo.
-   **Hueco 1 (conceptual):** nadie decía qué es «fuerza coactiva» en una red donde nada se coacciona. La respuesta está en TK-84: la ley promulgada es la única que produce un `lawId` aceptado por las constantes y por `faircoin3-admin`. Coactiva = ejecutable. No estaba escrito.
-   **Hueco 2:** momento de la promulgación. Oasis promulga al morir el gobierno ([draftv0 §ciclo de vida](../drafts/draftv0.md#L101)); con un Consejo que promulga, hace falta plazo, silencio y devolución. G05 no lo fijaba.
-   **Hueco 3:** [TK-D15](../drafts/draftv2.md#L65) daba cronología a Cámara, Presidencia y Justicia, pero no al Consejo de Legislación.
-   **Hueco 4:** draftv1 no tenía fila para este órgano; la Tabla 1 saltaba de la Cámara a la Presidencia.

Veredicto: la pieza existía como caja («Consejo promulga») pero sin mecanismo: quién firma, cuándo, qué pasa si calla, qué vale la firma. Ahora tiene los cuatro.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md TK-D05](../drafts/draftv2.md#L55): default reescrito. Presidente elegido por absoluta de la Cámara, nombra Consejo, deja el escaño. Fuerza coactiva = ejecutabilidad vía `lawId` (TK-84). Promulgación firmada en ≤ 7 d; sin enmienda de texto; una devolución motivada; reaprobación por absoluta obliga a promulgar; silencio = promulgación tácita. Índice consolidado con RP-6. Alternativas: colegio sin presidente, sin veto, mayoría simple, conserva escaño.
-   [draftv2.md TK-D15](../drafts/draftv2.md#L65): Consejo de Legislación 60 d ligado a su Cámara; leyes aprobadas y no promulgadas pasan al Consejo entrante sin caducar.
-   [draftv2.md TK-G05](../drafts/draftv2.md#L79): tipos `legislationPresidentElection`, `legislationCouncil`, `lawReturn`, `lawIndex`; `parliamentLaw` con `lawId` y `promulgatedBy[]`; `enactApprovedChanges` deja de esperar al fin de mandato.
-   [draftv1.md #15](../drafts/draftv1.md#L26) (fila nueva, fuera del recuento): Consejo de Legislación ausente hoy, «Parecido» con G05.
