Reconstrucción de memoria, no verbatim. Confírmalo en pp. 467-493.

**Puntos principales del cap. VII «Filosofía de la acción constituyente» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | **Poder constituyente ≠ poderes constituidos** (Sieyès): una constitución pactada entre poderes ya constituidos no es constitución, es reparto. La Transición fue eso: reforma «de la ley a la ley», consenso de élites | A |
| 2 | **Ruptura, no reforma**: la acción constituyente exige discontinuidad con la legalidad anterior. Ningún poder constituido puede abrir ni cerrar el período | A |
| 3 | La libertad constituyente es un **período**, no un acto: sin constitución vigente, el pueblo delibera libremente sobre la forma de Estado y de Gobierno | A |
| 4 | El constituyente es **acción**, no doctrina: la libertad no se otorga, se conquista. La **abstención activa** frente a las elecciones del Estado de partidos es la única acción constituyente disponible al ciudadano | A/B |
| 5 | Secuencia: ruptura → gobierno provisional → asamblea constituyente elegida por distritos uninominales → texto → **referéndum** sobre la forma de Estado y sobre la constitución | B |
| 6 | La asamblea constituyente es de **propósito único**: redacta y se disuelve; no legisla ni gobierna | B |
| 7 | La constitución fija la **forma**, no el contenido: sin programa ideológico ni «derechos» otorgados como concesión | B |
| 8 | Fondo filosófico: la acción como origen de la libertad política (Arendt, *Sobre la revolución*), frente al contractualismo y al consenso | C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 3 → [draftv1 #3](../drafts/draftv1.md#L15) («clon accidental»: ANARCHY como constituyente latente, [draftv0 §3.F](../drafts/draftv0.md#L204)). Tesis 5 y 6 → [TK-D09](../drafts/draftv2.md#L59) / [TK-78](../drafts/draftv2.md#L92) (asamblea ad hoc, 80 %, referéndum). Tesis 7 → TK-D12 (sin programa) y TK-D10/G08 (referéndum solo constituyente).
-   **Hueco 1 (el central):** Oasis abre el constituyente **por ausencia** (nadie llega al 25 %). Trevijano lo abre **por acción**. D09 no distinguía, y RP-9 heredaba la apertura accidental. Faltaba un acto: la llamada constituyente firmada por una fracción del censo, análogo de la abstención activa.
-   **Hueco 2 (génesis):** las constantes de Oasis (60 días, 25 %, umbrales) las escribió epsylon. Nadie las constituyó. El fork las tomaba como dadas y las reformaba por parches RP. Eso es exactamente la «reforma de la ley a la ley» que el libro rechaza. El fork debe nacer por constituyente y tratar lo heredado como provisional.
-   **Hueco 3:** D09 no decía si los poderes constituidos siguen funcionando durante el período ni si pueden tocar constantes (tesis 2).
-   **Hueco 4:** «ratificación por referéndum de censo» sin mayoría ni quórum definidos; sin regla de disolución de la asamblea ni de elegibilidad de sus miembros (tesis 6).
-   **Sin hueco:** tesis 7, ya cubierta por D12.

Veredicto: era la pieza mejor valorada del sistema («clon accidental») y por eso la menos trabajada. El accidente hay que convertirlo en acto, y el fork tiene que aplicarse a sí mismo la doctrina: no reformar Oasis, constituirse.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md TK-D09](../drafts/draftv2.md#L59): preguntas ampliadas (apertura por acción, ruptura vs reforma, génesis, disolución, elegibilidad). Default: apertura por (i) génesis, (ii) 2 ciclos ANARCHY, (iii) `constituentCall` con ≥ 25 % del censo; constantes heredadas = `provisionalConstants`; asamblea ≠ Cámara, elegida por mónadas, solo redacta; poderes constituidos siguen pero no tocan constantes; 80 % del texto; referéndum por mayoría con quórum del 50 %; disolución al ratificar; miembros elegibles; solo forma, nunca programa. Alternativas: RP-9 tal cual, apertura por abstención, inelegibilidad, sin quórum.
-   [draftv2.md TK-78](../drafts/draftv2.md#L92): modelo `constituent_model.js` con `provisionalConstants`, `constituentCall`, `constituentPeriod`, `constitutionDraft`, `ratificationReferendum`; prioridad sube a **H** (es el acto fundacional del fork).
-   [draftv1.md #3](../drafts/draftv1.md#L15): «Clon accidental» hoy → «Clon» con TK-78.
