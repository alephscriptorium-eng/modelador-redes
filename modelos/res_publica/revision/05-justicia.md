Reconstrucción de memoria, no verbatim. Confírmalo en pp. 421-441.

**Puntos principales del cap. V «Presidencia del Consejo de Justicia» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | La justicia es un **poder con legitimidad de origen propia**: su presidente lo elige por mayoría absoluta el **mundo judicial**, no el poder político; nombra su Consejo | A/B (divulgación nodulo, MCRC) |
| 2 | Crítica al CGPJ y al Tribunal Constitucional como órganos de cuota de partido: en el Estado de partidos la justicia es **dependiente en el origen** aunque sea independiente en el ejercicio | A |
| 3 | El **control de constitucionalidad** corresponde al Consejo de Justicia, no a un tribunal político | B |
| 4 | Los jueces **no se eligen por sufragio**: acceso por mérito, independencia garantizada por el propio Consejo, no por el Gobierno | B |
| 5 | **Jurado** como participación popular en la justicia y garantía frente a la judicatura burocrática | B/C |
| 6 | **Publicidad del proceso** como condición del control del juez por el pueblo | B |
| 7 | El Consejo de Justicia **juzga la responsabilidad del ejecutivo**; la misma legitimidad de origen le permite enfrentarse a las otras dos presidencias | B/C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 1 y 3 → [TK-D07](../drafts/draftv2.md#L57) / [TK-G07](../drafts/draftv2.md#L81) (mundo judicial elige Presidente, nombra Consejo, anula leyes contra constantes). Tesis 2 → RP-5 / TK-76 (fuera `DICTATOR`). Tesis 6 → RP-7 / TK-77 (veredictos en claro).
-   **Hueco 1 (circular):** el «mundo judicial» del default eran los que habían actuado como juez, y los jueces los elegía el censo (`courtsNomination`). El origen seguía siendo popular, contra la tesis 4. [draftv1 #10](../drafts/draftv1.md#L22) ya lo notaba («más que lo que Trevijano pedía») pero no lo corregía. Faltaba el equivalente de la oposición: el módulo `School` de Oasis emite certificados y sirve como puerta de acceso por mérito.
-   **Hueco 2:** D07 preguntaba por el jurado y el default no respondía. `POPULAR` de Oasis es un plebiscito de 14 días sobre el caso, no un jurado. El sorteo verificable de RP-3 ya existía como mecanismo para otro fin.
-   **Hueco 3:** control de constitucionalidad sin procedimiento (quién insta, plazo, efecto cautelar).
-   **Hueco 4:** nadie conectaba la reprobación de la Cámara (D18) con un juicio del Consejo sobre la Presidencia (tesis 7).
-   **Divergencia asumida:** proceso público (tesis 6) frente a instrucción cifrada de RP-7. En una red sin territorio las partes corren riesgo real; se mantiene RP-7 y se deja la publicidad plena como alternativa.
-   **Resto de karma:** TK-32 (RP-4) no incluía el desempate de candidaturas a juez por karma (`courts_model.js:805`).

Veredicto: la caja «Consejo de Justicia» existía con el patrón correcto (presidente elegido → Consejo). Fallaba la base: quién es juez y por qué. Ahora hay acceso por mérito, jurado por sorteo y procedimiento de constitucionalidad.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md TK-D07](../drafts/draftv2.md#L57): preguntas ampliadas (acceso, jurado, procedimiento, juicio a la Presidencia, publicidad). Default: juez nombrado por el Consejo entre inhabitants con certificado `School` y ≥ 2 ciclos; bootstrap por la constituyente (D09); jurado por sorteo verificable (veredicto de jurado, orden de juez), `POPULAR` eliminado; `constitutionalChallenge` con resolución en 21 d, `lawAnnulment` público y suspensión cautelar; el Consejo juzga actos de la Presidencia con `censureAct` como prueba; RP-7 mantenido. Alternativas: elección popular, sorteo puro, censo entero, proceso público obligatorio.
-   [draftv2.md TK-G07](../drafts/draftv2.md#L81): tipos `judgeAppointment`, `justiceCouncil`, `juryDraw`, `constitutionalChallenge`, `lawAnnulment`; eliminar `POPULAR` y `DICTATOR`; lectura de `school_model.js`.
-   [draftv2.md TK-32](../drafts/draftv2.md#L87): añadido `courts_model.js:805` (karma en candidaturas a juez).
-   [draftv1.md #10](../drafts/draftv1.md#L22): nota de que con G07 pasaría a «Clon» salvo en la publicidad del proceso.
