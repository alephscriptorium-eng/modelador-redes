De memoria y con la misma cautela: reconstrucción, no verbatim. Confírmalo en pp. 363-380.

**Puntos principales del cap. II «Mónada republicana» (reconstrucción)**

| # | Tesis | Cert. |
| --- | --- | --- |
| 1 | La **unidad elemental del poder político** es el distrito electoral (la mónada), no el individuo, la familia, el municipio ni el partido. Tamaño orientativo ~100.000 hab. | A (divulgación MCRC) |
| 2 | Toma el término de Leibniz: cada mónada es **simple e indivisible** políticamente y **refleja la República entera**; la misma estructura se repite en todas | B |
| 3 | Mónadas de **igual tamaño** → igualdad real del sufragio. La geometría electoral es la garantía material del «un ciudadano, un voto» | A/B |
| 4 | La mónada es el ámbito donde el representante es **conocido personalmente**, donde se forma el mandato y donde se ejerce la revocación. Sin mónada no hay responsabilidad personal | B |
| 5 | Separa **sociedad política** (mónadas → Cámara) de **sociedad civil** (municipio, asociaciones, partidos). La mónada sustituye al partido como mediador entre sociedad y Estado | B |
| 6 | La mónada es territorial por necesidad práctica (censo fijo, vecindad), pero su esencia es la **comunidad de electores**, no el territorio | C |

**Ficha de confirmación del mapeo** (fuente: [draftv2.md](../drafts/draftv2.md))

-   **Mapeado:** tesis 1, 3 y 6 → [TK-D01](../drafts/draftv2.md#L51) (definición, tamaño, territorialidad) con implementación en [TK-G01](../drafts/draftv2.md#L73) (`monad_model.js`, asignación por hash). Tesis 5 → [TK-D13](../drafts/draftv2.md#L63) (parlamentos de tribu como autogobierno civil sin potestad legislativa). Tesis 4 → [TK-D03](../drafts/draftv2.md#L53) (revoca el censo de la mónada).
-   **Acierto no explicitado:** el default de D01 (colegios por hash aleatorio) cumple la tesis 2 mejor que un distrito territorial. Cada mónada es una muestra estadística del censo entero. Conviene anotarlo como argumento a favor del default.
-   **Tensión no señalada:** ese mismo default rompe la tesis 4. Un representante asignado por hash no es conocido por sus electores. La alternativa (a) de D01, mónada = PUB, salva la proximidad y sacrifica la igualdad. D01 debería nombrar este intercambio como criterio de decisión.
-   **Hueco:** D01 asigna la mónada «al inicio de ciclo». Si se rebaraja cada 60 días no hay comunidad persistente que sostenga mandato y revocación (D02, D03). Falta decidir si la semilla es estable entre ciclos.
-   **Contradicción a corregir:** [draftv1.md:36](../drafts/draftv1.md#L36) declara el distrito uninominal intraducible. Draftv2 lo traduce vía D01. Draftv1 queda desactualizado también aquí.

Veredicto: capítulo mapeado en su núcleo (unidad, tamaño, igualdad). Falta explicitar la tensión igualdad/proximidad y la persistencia de la mónada entre ciclos.

---

**Correcciones aplicadas (2026-09-09)**

-   [draftv2.md TK-D01](../drafts/draftv2.md#L51): default con **semilla estable entre ciclos**; añadido el argumento «refleja el todo» (tesis 2) y el **criterio de decisión** igualdad/proximidad; nueva alternativa (d) rebarajar cada ciclo; desbloquea también TK-D03.
-   [draftv2.md TK-G01](../drafts/draftv2.md#L73): `seedHash` fijo desde el ciclo fundacional; altas nuevas entran por el mismo hash.
-   [draftv1.md #6](../drafts/draftv1.md#L18): nota de que con TK-D01/G01 el veredicto pasaría a **Parecido**.
-   [draftv1.md Tabla 2](../drafts/draftv1.md#L36): fila «Distrito uninominal» marcada como superada por TK-D01.
-   Pendiente: las correcciones de [01-lealtad.md](01-lealtad.md) (draftv1 #12 y huecos de TK-D08) no se han aplicado.
