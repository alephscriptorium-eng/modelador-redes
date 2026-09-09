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

---

**Verificación en fuentes (2026-09-09, en línea)**

Verificadas las 7 tesis del cap. IV contra el párrafo verbatim del libro publicado por MCRC Alicante (2015), la reseña de El Catoblepas 118:13 (nodulo, con citas paginadas de otra edición) y el artículo doctrinal «Consejo de Legislación» de mcrc.es (2023, destino del enlace de diariorc.com). Confirmadas: 1 (presidente elegido por absoluta de la Cámara; misma legitimidad de origen), 2 (nombra libremente 8-10 consejeros; patrón de Justicia con 14) y 6 (la Nación legisla, no gobierna). Matizadas: 3 (vis directiva/coactiva y promulgación son verbatim, pero «las leyes no se sancionan»), 4 (la gener

- Tesis 1: **confirmada**. ««en elección de segundo grado […] la Cámara de representantes elige por mayoría absoluta al Presidente del Consejo de Legislación» · «la misma legitimidad de origen que la del poder legislativo de la Nación y la del pode» (https://mcrcalicante.wordpress.com/2015/01/21/teoria-pura-de-la-republica-libro-tercero-capitulo-iv-presidencia-del-consejo-de-legislacion-poder-legislativo-de-). Verbatim del cap. IV en MCRC Alicante; la frase de la legitimidad de origen la cita nodulo desde el cap. V (Justicia), paginación de otra edición. Certeza pasa de B a A.
- Tesis 2: **confirmada**. ««facultándolo para que designe libremente entre la diputación a los miembros restantes» · «nombra a 8 ó 10 consejeros de los diputados para integrarlos en su consejo»» (https://mcrcalicante.wordpress.com/2015/01/21/teoria-pura-de-la-republica-libro-tercero-capitulo-iv-presidencia-del-consejo-de-legislacion-poder-legislativo-de-). Patrón idéntico en Justicia (nodulo: el presidente «elegirá a catorce miembros de la jurisdicción»). Dato nuevo para D05: k = 8-10. Certeza A.
- Tesis 3: **matizada**. ««legitimado para promulgar las leyes nacionales con la vis coactiva sedente en la Nación y la vis directiva de la Cámara de Representantes monádicos» · «Las leyes no se sancionan, esto es una república constitucional»» (https://mcrcalicante.wordpress.com/2015/01/21/teoria-pura-de-la-republica-libro-tercero-capitulo-iv-presidencia-del-consejo-de-legislacion-poder-legislativo-de-). Núcleo confirmado verbatim (vis directiva/coactiva, promulgación y publicación en el «Boletín oficial de la Nación»). La palabra «sanción» de la reconstrucción está refutada: nodulo añade «no necesitan la sanción del Jefe del Estado». Coactiva = ejecutiva («vis coactiva necesaria para que las leyes 
- Tesis 4: **matizada**. ««decidir sobre la dimensión nacional de las iniciativas de ley, la constitucionalidad de las mismas y la generalidad de su contenido»» (https://www.mcrc.es/post/consejo-de-legislacion/). [doctrina, sin verbatim] B. La generalidad de la ley sí es criterio del Consejo, pero como filtro PREVIO de iniciativas, no como control de la ley votada. Codificación, redacción técnica y coherencia del ordenamiento: sin fuente en ninguna de las páginas consultadas.
- Tesis 5: **refutada**. ««La iniciativa de ley que no sea aprobada por el Consejo de Legislación será devuelta a su procedencia con un informe sobre los motivos del rechazo» · «Las proposiciones de ley aprobadas por ésta se promulgan y publican»» (https://www.mcrc.es/post/consejo-de-legislacion/ ; https://mcrcalicante.wordpress.com/2015/01/21/teoria-pura-de-la-republica-libro-tercero-capitulo-iv-presidenc). La devolución existe pero es ex ante y a la procedencia de la iniciativa (diputado, Gobierno o autoridad judicial), no a la Cámara tras la aprobación; el verbatim dice que el Consejo «recibe y filtra las iniciativas legislativas merecedoras de pasar a la Cámara» y mcrc.es que «la función de este se 
- Tesis 6: **confirmada**. ««El Estado es representado por el Presidente de la República y su Consejo de Ministros y la Nación es representada por el presidente del Consejo Legislativo […] Que la Nación legisle, pero que no gobierne»» (https://www.nodulo.org/ec/2011/n118p13.htm ; https://www.mcrc.es/post/consejo-de-legislacion/). Paráfrasis cercana al libro en nodulo; mcrc.es: «el Estado no ocupa ningún lugar durante la producción legislativa». Certeza A/B.
- Tesis 7: **matizada**. ««que son sustituidos en la Cámara de Representantes por sus suplentes» · «Los miembros del Consejo pierden su representación diputacional, y son sustituidos por los suplentes»» (https://www.nodulo.org/ec/2011/n118p13.htm ; https://www.mcrc.es/post/consejo-de-legislacion/). Incompatibilidad con el escaño confirmada (B, dos fuentes independientes, sin verbatim del libro). Mandato fijo del Consejo y su caducidad con la Cámara (TK-D15): sin fuente; sigue en C.
