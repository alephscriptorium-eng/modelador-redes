Reconstrucción de memoria, no verbatim. Confírmalo en pp. 442-466.

**Puntos principales del cap. VI «Presidencia del Consejo de Gobierno» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | Presidente elegido por **sufragio universal directo** a doble vuelta; jefe del ejecutivo con legitimidad propia, no derivada de la Cámara | A |
| 2 | **Nombra su Consejo** (ministros); ninguno es miembro de la Cámara; incompatibilidad con el escaño | A/B |
| 3 | Régimen presidencial, no parlamentario: **sin moción de censura**. **«No disuelve la Cámara sin dimitir»**: el conflicto entre poderes lo resuelve el pueblo, no uno de los poderes | A/B (divulgación nodulo) |
| 4 | **No legisla por decreto**: sin decreto-ley; solo reglamentos de ejecución dentro de la ley | B |
| 5 | Responsabilidad política ante las urnas y **responsabilidad jurídica ante el Consejo de Justicia**; sin inmunidad | B |
| 6 | Sin jefatura de Estado separada por encima de los poderes: el resto monárquico del «árbitro neutral» desaparece | C |
| 7 | Materia propia: administración, tesoro público bajo presupuesto aprobado por la Cámara, relaciones exteriores | B/C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 1 y 4 → [TK-D06](../drafts/draftv2.md#L56) / [TK-G06](../drafts/draftv2.md#L80) (elección directa, ciclo desfasado, sin iniciativa). Tesis 7 → TK-84 (materia = chain-admin + tesorería solo con `lawId`). Tesis 5 → D07 (el Consejo de Justicia juzga a la Presidencia) y D18 (control sin derribo).
-   **Hueco 1:** D06 decía «no disuelve la Cámara» a secas. La regla del libro es «no disuelve **sin dimitir**»: la disolución existe como apelación al pueblo y cuesta el cargo. Cambia el mecanismo.
-   **Hueco 2:** el patrón «presidente → nombra Consejo», ya aplicado a Legislación y Justicia, faltaba aquí. Sin Consejo no hay carteras ni multisig con quien repartir claves (TK-82).
-   **Hueco 3:** la tesorería se ejecutaba «con ley promulgada» pero sin **presupuesto**. Toda ley de gasto es previa; faltaba la ley de presupuesto del ciclo y la prórroga.
-   **Hueco 4:** reglamentos, veto, reelección, jefatura de Estado y poderes de excepción no tenían respuesta. Los tres últimos son fáciles en una red: sin veto (la devolución es de Legislación), sin jefatura separada, sin estado de sitio que declarar.
-   **Sin hueco:** tesis 2 (incompatibilidad) y tesis 5 (ya cubiertas por D07 y D18 tras las revisiones anteriores).

Veredicto: [draftv1 #5](../drafts/draftv1.md#L17) decía «el parche da la forma, falta la materia». La materia llegó con TK-84; lo que faltaba era el **régimen** del ejecutivo: Consejo, presupuesto, reglamentos y la regla de disolución. Ahora está.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md TK-D06](../drafts/draftv2.md#L56): preguntas ampliadas (Consejo, disolución con dimisión, presupuesto, reglamentos, veto, jefatura, excepción). Default: mandato 60 d, reelección libre, sin revocación; `governmentCouncil` con carteras (tesorería, cadena, puentes Multiverse; PUB en sociedad civil); sin iniciativa ni veto; tesorería multisig k-de-n bajo `budgetLaw` del ciclo con prórroga; `executiveOrder` solo de ejecución con `lawId`, público e impugnable; `dissolutionAndResignation` (elecciones dobles, desfase restablecido); sin jefatura separada ni poderes de excepción. Alternativas: colegiado, sin disolución, 3 ciclos máximo, veto suspensivo.
-   [draftv2.md TK-G06](../drafts/draftv2.md#L80): tipos `governmentCouncil`, `executiveOrder{lawId}`, `budgetLaw`, `dissolutionAndResignation`; multisig con TK-82; depende también de D18.
-   [draftv1.md #5](../drafts/draftv1.md#L17): veredicto pasa a «Parecido» con G06.
