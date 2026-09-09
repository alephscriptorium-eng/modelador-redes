Reconstrucción de memoria a partir de Leval, Souchy y Casanova, sin páginas a mano: certeza **B** en el núcleo y **C** en los detalles de procedimiento, según la escala de `draft.md` §2. Confírmalo en Leval (*Colectividades libertarias en España*, capítulos de Aragón y Levante) y en Simoni (Cretas) antes de citar.

**Puntos principales del tema «Asamblea soberana» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | **La asamblea general es el órgano soberano** de la colectividad: de pueblo en el campo, de fábrica o taller en la ciudad. Toda decisión de fondo (admisión, reparto, obras, relaciones con otras colectividades) nace de ella | A |
| 2 | **Todos los miembros forman la asamblea** con voz y voto; en muchas colectividades agrarias votaban también las mujeres y los jóvenes, práctica desigual según el pueblo | B |
| 3 | **Periodicidad y convocatoria**: asamblea ordinaria semanal o mensual según el tamaño; extraordinaria a petición de un grupo de miembros o de la comisión administrativa | B/C |
| 4 | **Deliberación abierta y voto a mano alzada**; sin voto secreto salvo casos personales. La publicidad de la decisión es parte de la decisión | B |
| 5 | **La comisión administrativa es un cargo, no un gobierno**: elegida por la asamblea, sin poder propio, rinde cuentas en cada asamblea y es revocable en cualquier momento. La asamblea **no puede delegar su soberanía** en un consejo ni en un líder | A |
| 6 | **La asamblea decide el reparto**: el salario familiar, las escalas y las excepciones se aprueban en asamblea, y la comisión solo ejecuta | A |
| 7 | **Los delegados a la federación llevan mandato de la asamblea**, imperativo y revocable; informan al volver | A |
| 8 | **Quórum informal**: se decidía con los presentes; la legitimidad venía de la convocatoria pública, no de un umbral aritmético | C |
| 9 | **Los individualistas quedan fuera sin coerción**: no participan en la asamblea de la colectividad pero conviven en el municipio | B |

**Ficha de confirmación del mapeo** (fuente: [draftv0.md](../drafts/draftv0.md))

-   **Mapeado:** tesis 1 y 5 → [CL-1](../drafts/draftv0.md#L168) (la asamblea gobierna campos, miembros y expulsiones) y [TK-G'01](../drafts/draftv0.md#L207); tesis 6 → [CL-3](../drafts/draftv0.md#L170) y [CL-5](../drafts/draftv0.md#L172) (reparto y tesoro); tesis 7 → [CL-8](../drafts/draftv0.md#L175), [TK-D'04](../drafts/draftv0.md#L195) y [TK-F'01](../drafts/draftv0.md#L242); tesis 2 y 8 → [TK-D'01](../drafts/draftv0.md#L192) (quién forma la asamblea, quórum); tesis 4 → [TK-G'05](../drafts/draftv0.md#L211) (publicidad interna). El hallazgo [B](../drafts/draftv0.md#L138) es exactamente la tesis 1 leída contra el código: la asamblea existe (`ANARCHY` por defecto, todos proponen) y no manda.
-   **Acierto no explicitado:** el hallazgo [G](../drafts/draftv0.md#L158) señala que `ANARCHY` es el estado normal de una colectividad. La tesis 5 lo confirma desde la doctrina: la colectividad no tiene gobierno, tiene comisiones. Conviene decirlo con esas palabras en «[Lo que no se toca](../drafts/draftv0.md#L180)».
-   **Hueco 1 (grave):** la tesis 5 dice que la asamblea **no puede abdicar**. En Oasis el parlamento de tribu admite candidaturas con cualquier método, incluida `DICTATORSHIP`: una asamblea puede votarse un dictador de tribu. CL-1 no lo impedía.
-   **Hueco 2:** la tesis 3 (convocatoria y periodicidad) no tenía tarea. El ciclo de 60 días del `tribeParliamentTerm` sirve de asamblea ordinaria, pero nadie podía convocar una extraordinaria.
-   **Hueco 3:** la tesis 6 («la asamblea decide el reparto») solo estaba cubierta por la validación de necesidades de CL-3; el **plan de reparto** seguía siendo un acto del steward, aunque electo (`industry_model.js:980`). Falta que repartir sea una materia votable.
-   **Hueco 4:** la tesis 4 (voto a mano alzada) y la tesis 8 (quórum informal) no aparecían como pregunta en TK-D'01. Importa: el quórum del 25 % de Oasis es un default razonable, pero es aritmética de Estado, no de asamblea de pueblo.
-   **Sin hueco:** tesis 9 (individualistas), cubierta por [TK-D'05](../drafts/draftv0.md#L196) y CL-11.

Veredicto: la asamblea está mapeada en su existencia (hallazgos B y G) y en sus competencias sobre miembros y tesoro, no en su procedimiento (convocatoria, forma del voto) ni en su límite (no puede abdicar ni ceder el reparto).

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv0.md TK-D'01](../drafts/draftv0.md#L192): añadidas las preguntas de convocatoria y periodicidad, voto a mano alzada o secreto y delegación en líder o consejo (huecos 2 y 4); default: ordinaria = ciclo de 60 d, extraordinaria por el 10 % de los miembros, voto público firmado, **la asamblea no puede abdicar**; desbloquea TK-G'06.
-   [draftv0.md CL-1](../drafts/draftv0.md#L168): el parlamento de tribu solo admite `ANARCHY`; se eliminan las candidaturas a líder de tribu (`parliament_model.js:1443-1445`); las comisiones son cargos de CL-2, nunca gobierno (hueco 1).
-   [draftv0.md CL-3](../drafts/draftv0.md#L170): el plan de reparto pasa a ser materia votable (`subject: "distribute"`); nadie reparte sin acuerdo de la asamblea, ni el steward electo; repara también el criterio 1 (hueco 3). [TK-B'03](../drafts/draftv0.md#L222) hereda el seam y depende de D'01.
-   [draftv0.md TK-G'06](../drafts/draftv0.md#L212) (nueva, prioridad alta): convocatoria y periodicidad, `assemblyCall` extraordinaria, solo `ANARCHY` como método de tribu (hueco 2).
-   [draftv0.md hallazgo B](../drafts/draftv0.md#L138): añadido el riesgo de abdicación (`parliament_model.js:1443-1445`) y que CL-1 lo cierra.
