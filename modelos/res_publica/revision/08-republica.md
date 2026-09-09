Reconstrucción de memoria, no verbatim. Confírmalo en pp. 494 y ss. El Epílogo va después (el índice impreso dice 426: errata).

**Puntos principales del cap. VIII «República Constitucional» y Epílogo (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | República ≠ ausencia de rey. República = *res publica*: forma de Estado en la que el poder **se origina en la sociedad** y no en el Estado. Frente a ella, la monarquía de partidos y el Estado de partidos, sea cual sea su nombre | A |
| 2 | **Tener constitución no es ser constitucional** (art. 16 de la Declaración de 1789): sin separación de poderes en el origen y sin representación no hay constitución, hay reparto escrito | A |
| 3 | Síntesis del modelo: mónada → Cámara → Consejo de Legislación · Presidente directo → Consejo de Gobierno · Consejo de Justicia elegido por el mundo judicial; tres legitimidades de origen distintas e iguales | A (síntesis de III–VI) |
| 4 | La República es **forma, no ideología**: ni de izquierdas ni de derechas; cualquier programa económico cabe bajo ella si nace del procedimiento | A |
| 5 | Constitución **breve, formal y rígida**: fija órganos y procedimientos; no catálogo de derechos-programa ni concesiones sociales que conviertan la norma en propaganda | B |
| 6 | Democracia **formal** (procedimiento de origen del poder) frente a «democracia material o social», que es la coartada ideológica del Estado de partidos | A |
| 7 | República unitaria con autonomía municipal; el federalismo de partidos regionales es otra forma de oligarquía | B/C |
| 8 | La República como lugar de la **verdad** política: la mentira es el principio del Estado de partidos, la lealtad y la verdad el de la República (enlaza con cap. I) | B |
| 9 | **Epílogo**: llamamiento a la acción constituyente en España; el MCRC como instrumento; confianza en que la libertad política se conquista, no se espera | C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 3 → arquitectura del carril G ([línea 71](../drafts/draftv2.md#L71)) tras las revisiones I–VII. Tesis 4 → [TK-D12](../drafts/draftv2.md#L62) (manifiesto neutralizado) y [draftv1 #14](../drafts/draftv1.md#L27). Tesis 6 → draftv1 #2 (clon). Tesis 7 → TK-D13 (parlamentos de tribu como autogobierno civil). Tesis 1 → D01 (mónada como origen del poder).
-   **Hueco 1 (criterio):** nadie había fijado **qué hace constitucional al fork**. Las constantes de Oasis son una constitución escrita que no es constitucional (fusión de poderes verificada en draftv0 §3). Faltaba el criterio del art. 16 como prueba de aceptación ejecutable de todo el carril G.
-   **Hueco 2 (forma vs programa):** TK-25 «Constitución técnica» estaba en prioridad baja y sin alcance. Con D09 (el fork nace por constituyente) pasa a ser el borrador que la primera asamblea ratifica, y debe ser de **solo forma**. Quedaba sin decidir si RBU, ECOin y la fiscalidad de carbono son constantes o leyes: con la tesis 5 son leyes ordinarias, derogables.
-   **Hueco 3:** draftv1 seguía diciendo en su conclusión que la geometría electoral es intraducible y que el backlog hereda la ideología de Oasis. Ambas cosas dejaron de ser ciertas en las revisiones II, III y VIII.
-   **Recuento desactualizado:** draftv1 contaba 2 clones y 6 ausentes o divergentes. Tras las ocho fichas y condicionado a implementar todos los TK-G: 4 clones, 11 parecidos, 0 ausentes, 0 divergentes; solo la escala sigue intraducible.
-   **Sin mapeo posible:** tesis 8 (verdad) y 9 (Epílogo): no son codificables; la verdad se apoya en lo que ya está (voto público, log inmutable, RP-7, RP-10).

Veredicto: el capítulo es la síntesis, y la síntesis ya estaba montada pieza a pieza. Lo que faltaba era el criterio de aceptación: una prueba que diga si el fork es república constitucional o solo tiene constantes.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md línea 9](../drafts/draftv2.md#L9): errata del Epílogo anotada.
-   [draftv2.md TK-D12](../drafts/draftv2.md#L62): preguntas ampliadas (criterio art. 16, constitución breve y rígida). Default: constitución técnica de solo forma; RBU, ECOin y carbono como leyes ordinarias, no constantes; test de constitucionalidad con 5 criterios. Alternativa: RBU como constante.
-   [draftv2.md TK-G11](../drafts/draftv2.md#L84) (nueva, absorbe TK-25): `constitutionDraft` inicial de solo forma, propuesto y no impuesto a la primera constituyente; suite `test/constitutional.js` como prueba de aceptación del carril G. Prioridad alta.
-   [draftv1.md #13](../drafts/draftv1.md#L25): «Divergente» → «Parecido» con G08 (Polls sin fuerza, iniciativa por mónada, ANARCHY como constituyente).
-   [draftv1.md #14](../drafts/draftv1.md#L27): «Divergente» → «Parecido» con D12/G11.
-   [draftv1.md recuento](../drafts/draftv1.md#L31): añadido el recuento posterior a la revisión, condicionado a implementación.
-   [draftv1.md conclusiones 1 y 4](../drafts/draftv1.md): notas de que la geometría electoral se recupera y la tensión ideológica se resuelve por defecto.
