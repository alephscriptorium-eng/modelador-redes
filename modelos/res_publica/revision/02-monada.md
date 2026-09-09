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

---

**Verificación en fuentes (2026-09-09, en línea)**

Verificación en línea de las 6 tesis de modelos/res_publica/revision/02-monada.md. Fuente principal: texto OCR del propio libro (ebook en archive.org, item TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano, PDF extraído con pdftotext al scratchpad; cap. II sin paginación en esa edición). Fuentes de divulgación: mcrcalicante 2014-10-15, diariorc (florilegios y «Libertad colectiva en la comarca electoral»), diarioerc (Cádiz 2017-10-21; 2017-05-11), mcrc.es, Cartagena Actualidad (y III), El Catoblepas 118:13 (Giménez; cita pp. 248, 374, 468). Wikipedia no aporta nada sobre la mónada; El Catoblepas 11

- Tesis 1: **confirmada**. «un pueblo se compone, por ejemplo, de 400 mónadas electorales de cien mil habitantes cada una. En tanto que unidad irreductible del universo político (… no puede ser el individuo aislado ni la célula familiar)» (Libro, cap. II (ebook OCR): https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; divulgación: https://mcrcalicante.wordpress.com/2014/10/). Verbatim del cap. II. Complementos: «La mónada de distrito, no los individuos ni los partidos, es el único sujeto posible de la acción política de representar» (libro y mcrc.es); mcrcalicante: «la primera unidad de poder sería el colegio electoral, no la familia ni el individuo ni el ayuntamiento» (
- Tesis 2: **confirmada**. «Leibniz introdujo el término monade en una carta de 13 marzo de 1696 […] «La mónada es una sustancia simple (sin partes) que entra en los compuestos» […] cada mónada es un pequeño espejo del universo» (Libro, cap. II: https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; https://www.diarioerc.com/2017/10/21/cadiz-monada-electoral-republic). Verbatim del cap. II; además «Son substancias indivisibles» y «Los distritos son auténticas mónadas respublicanas porque reproducen, en su microcosmos, la diversidad de componentes de la Res publica». Diarioerc: «tomando de Leibniz el concepto de mónada entendida como unidad irreductible, crea la no
- Tesis 3: **confirmada**. «la necesaria igualdad demográfica de las circunscripciones electorales exige que la unidad representativa de la pluralidad social, sea el censo electoral correspondiente a cien mil personas vecinales o comarcales» (Libro, cap. II: https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; https://www.diarioerc.com/2017/10/21/cadiz-monada-electoral-republic). Verbatim del cap. II (también reproducido en diarioerc). Refuerzos: «La mónada política debe reunir requisitos de igualdad cuantitativa, deslinde territorial y simultaneidad operativa»; «mónadas políticas de vecinos iguales en ciudadanía societaria»; mcrcalicante: «Similar numero de electores en cad
- Tesis 4: **matizada**. «sea porque la circunscripción electoral es demasiado grande o porque el programa del candidato elegido es indefinido, desaparece el carácter relacional de la representación, y ésta se polariza en poder independiente e ir» (Libro, cap. II: https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; https://www.cartagenaactualidad.com/pensando-en-voz-alta-pensando-co). Confirmado lo operativo: «Los dos poderes son mandatos imperativos y revocables. Ningún poder puede ser irrevocable sin perder su naturaleza»; «hace improbable, bajo pena de revocación, que transforme en poder propio la potencia representativa»; «revocación por los electores del titular»; la partido
- Tesis 5: **matizada**. «para que de ella emerja una sociedad política intermedia, que interprete las necesidades y represente los intereses de la sociedad civil ante el Estado Constitucional» (Libro, cap. VII y Libro II: https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; https://mcrcalicante.wordpress.com/2014/10/15/trevijano-). La tríada sociedad civil / sociedad política / sociedad estatal es de Trevijano (verbatim en cap. VII y Libro II: «Sin libertad política, sin sociedad política intermedia entre la Sociedad y el Estado, los partidos pasaron desde la clandestinidad al Estado»); mcrcalicante: «El juego se traduce en la
- Tesis 6: **refutada**. «la más pequeña unidad política representable es la comunidad vecinal, que no es una sociedad voluntaria, sino una comunidad involuntaria y espontánea, como la comarca, la región o la nación, anteriores al Estado» (Libro, cap. II: https://archive.org/details/TeoriaPuraDeLaRepublicaAntonioGarciaTrevijano ; https://diariorc.com/radio-tv/principios-y-fundamentos/nuestros-fund). Verbatim del cap. II (reproducido en diariorc). La territorialidad no es circunstancia práctica sino requisito y hecho natural: «La mónada política debe reunir requisitos de igualdad cuantitativa, deslinde territorial y simultaneidad operativa»; «La territorialidad, apego de lo humano a los horizont
