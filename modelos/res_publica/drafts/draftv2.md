# Plan: backlog v3 — reflotar Faircoin (génesis nuevo) con Oasis/Banking, carriles enlazados y camino por defecto trevijanista

## Contexto

`contexto.md` produjo el backlog v1 (SNH + Faircoin al servicio de la República Pura). `pura.md` (rev. 2) auditó Oasis 1.0.7 y propuso RP-1…10. `draftv1.md` concluyó que no hay clon: hay auditoría + parches sin implementar, y que faltan piezas (materia del ejecutivo, ideología, verificación doctrinal).

Decisiones del usuario: **génesis nuevo (Faircoin3)** · **Banking multi-moneda** (ECOin y FAIR) · alcance **moneda + banco + economía real + gobernanza** · entregable **nuevo `base/teoria/backlog.md`**, `pura.md §5` → puntero · **menos decisiones mías, más hilado**: cada incógnita es una tarea de investigación con *camino por defecto* y *alternativas*, y los carriles se enlazan para que tras investigar se pueda seguir.

El usuario tiene el libro (edición en un tomo: Libro I *Actualidad de la Revolución Francesa* · Libro II *El factor republicano* · Libro III *Teoría pura de la República*, caps. I Lealtad republicana p.340 · II Mónada republicana 363 · III Cámara de Representantes Monádicos 381 · IV Presidencia del Consejo de Legislación 404 · V Presidencia del Consejo de Justicia 421 · VI Presidencia del Consejo de Gobierno 442 · VII Filosofía de la acción constituyente 467 · VIII República Constitucional 494 · Epílogo (el índice impreso dice 426: errata, va tras la p. 494) · Índice de nombres 536).

### Lo que la divulgación ya fija (verificado hoy en mcrcalicante.wordpress.com y nodulo.org/ec/2011/n118p13) — a confirmar en el libro
| Pieza | Divulgación | Cap. del libro |
| :-- | :-- | :-- |
| **Mónada** = distrito electoral (~100.000 hab.); "la primera unidad de poder sería el colegio electoral, no la familia ni el individuo ni el municipio" | mcrcalicante | II (363) |
| **Representante monádico**: uninominal, **mayoría absoluta a doble vuelta**, distritos de tamaño similar, **mandato imperativo del electorado**, **revocable "en caso de deslealtad"** | mcrcalicante | I (340), III (381) |
| **Cámara de Representantes** da a la ley su *fuerza directiva*; el **Consejo de Legislación** (elegido por la Cámara) le confiere la *fuerza coactiva* | nodulo, mcrcalicante | III–IV |
| **Presidente** (del Consejo de Gobierno) por **sufragio universal directo**; no legisla por decreto; **no disuelve la Cámara sin dimitir**; designa su Consejo | nodulo | VI (442) |
| **Consejo de Justicia**: su presidente elegido por mayoría absoluta del mundo judicial; nombra su Consejo; control de constitucionalidad; "misma legitimidad de origen" | nodulo, MCRC | V (421) |
| **Partidos**: asociaciones de la sociedad civil sin financiación pública | nodulo | Libro II "Partidos estatales" (289) |
| Crítica externa (Giménez): formalismo, mandato imperativo = Antiguo Régimen, utopismo | nodulo | — |

### Hechos técnicos verificados (resumen; detalle en pura.md y sesión)
- FairCoop/BotC/FairMarket: DNS muertos. fair-coin.org: "Cooling down FairCoin" 2024-06-17. Explorador offline. `seed1:40404` abierto.
- `faircoin/faircoin`: Bitcoin 0.12 + PoC, MIT, último commit 2022-02-05, `depends/`, `--with-cvn`, **`-cvn=file`** (`cvn.pem`), RPC admin `addcvn/removecvn/bancvn/setchainparameters/addcoinsupply/getactivecvns/getactiveadmins`, `getinfo.coinsupply` (no `moneysupply`), **sin `getmininginfo`**. Chain-admin y CVN pubkeys hardcodeadas en `chainparams.cpp`.
- Oasis Banking: seam de 14 métodos RPC; dinero solo en `sendtoaddress` (banking_model.js:1004, :1416); regex `^E` ×12; `coin:"ECO"` ×7; timeout 1500 ms → doble envío; `processPendingClaims` ≠ `computeEpoch`; hash de época no publicado; `POST /update` borra `src/configs/*.json` trackeados.
- Módulos Oasis: sin loader; adaptador dentro de Banking mejor que módulo nuevo.

## Ficheros
1. **Crear `base/teoria/backlog.md`** (estructura en §"Estructura del entregable").
2. **Modificar `base/teoria/pura.md`**: §5 → puntero de 5 líneas a `backlog.md`; §1.2 + 4 viñetas (DNS, cooling down, `-cvn=file`, `addcoinsupply`).
3. `contexto.md`, `draftv1.md`: sin cambios (draftv1 se enlaza desde backlog §0).

## Estructura del entregable `backlog.md`
0. Estado y método (hechos, commit auditado `9a657b7`, enlaces a pura.md/draftv1.md).
1. Prompt de activación v3.
2. **Mapa de carriles** (diagrama de dependencias entre carriles D → G → C → B → F → E → L) y regla de lectura: *toda tarea D tiene "camino por defecto"; si no se investiga, el carril siguiente usa el default; si se investiga y la respuesta difiere, la tarea D indica qué tareas aguas abajo cambian*.
3. Carril **D · Investigación doctrinal** (libro + divulgación).
4. Carril **G · Gobernanza republicana** (RP-1…12, rediseñado sobre Cámara + tres Consejos).
5. Carril **C · Cadena Faircoin3**.
6. Carril **B · Banking multi-moneda**.
7. Carril **F · Tesorería distribuida / federación CVN**.
8. Carril **E · Economía real**.
9. Carril **L · Legal, marca, comunidad, proyecto**.
10. Esqueleto andante · Sprints · Riesgos · Mapeos v1/v2 → v3 · Fuentes y certeza.

## Carril D · Investigación doctrinal (nuevo)
Formato de cada tarea: *qué buscar · dónde (cap./pág. del índice; divulgación) · **default** si no se investiga · alternativas · desbloquea*.

| ID | Buscar | Dónde | Default | Alternativas | Desbloquea |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-D01 | Definición y tamaño de la **mónada**; si es territorial por necesidad o por circunstancia | Cap. II (363); mcrcalicante 2014-10-15 | Mónada = colegio electoral de tamaño fijo; en red sin territorio, colegio de **M inhabitants asignado por hash determinista del feed con semilla estable entre ciclos** (igualdad de tamaño, verificable, sin caciques; cada mónada es muestra aleatoria del censo y **refleja el todo**, cap. II). **Criterio de decisión:** el hash maximiza la igualdad y sacrifica la proximidad (el representante no es conocido por sus electores); (a) y (b) salvan la proximidad y sacrifican la igualdad | (a) mónada = PUB de pertenencia; (b) mónada = tribu-distrito; (c) sin mónadas, cámara = censo; (d) rebarajar la semilla cada ciclo (sin comunidad persistente que sostenga D02/D03) | TK-G01, TK-D03 |
| TK-D02 | **Mandato imperativo**: contenido, cómo se fija, quién lo custodia | Cap. III (381), Cap. I (340) | El candidato publica un *mandato* firmado (SSB `mandate`) antes de la 1ª vuelta; cada voto suyo se coteja contra él en el log | mandato = programa de tribu (rechazado: reintroduce lista) | TK-G03 |
| TK-D03 | **Revocación por deslealtad**: quién revoca, con qué mayoría, procedimiento | Cap. I, III | Mayoría absoluta del censo de la mónada; causa objetiva = voto contrario al mandato publicado; sin plazo de gracia | (a) revocación libre sin causa; (b) solo al final del mandato | TK-G04 |
| TK-D04 | **Doble vuelta**: mayoría absoluta ¿de votantes o de censo?; segunda vuelta ¿entre dos o abierta? | Cap. III | Ciclo de 60 d partido: días 1-30 primera vuelta; 31-60 segunda entre los dos más votados si nadie supera 50 % de votantes | mayoría del censo (más exigente, más ANARCHY) | TK-G02 |
| TK-D05 | **Cámara vs Consejo de Legislación**: qué es "fuerza directiva" vs "coactiva"; cómo elige la Cámara al Consejo; tamaño; ¿puede el Consejo vetar?; **mayoría interna** para aprobar ley (simple/absoluta); **qué es una ley** en la red (norma general vs cambio de constante vs medida); ¿tiene el Consejo iniciativa?; **voto nominal público** | Cap. III–IV (381-420) | Cámara = representantes monádicos que **proponen y votan** (`parliamentProposal`). **Presidente del Consejo de Legislación elegido por mayoría absoluta de la Cámara; nombra su Consejo (k)**, mismo patrón que Justicia y Gobierno; deja el escaño (su mónada elige sustituto, D03). **Fuerza coactiva = ejecutabilidad**: solo la ley promulgada produce `lawId`, y solo un `lawId` cambia constantes o autoriza actos chain-admin (TK-84). Promulgación = acto firmado del Consejo en **≤ 7 d** desde la aprobación (hoy Oasis promulga al morir el gobierno, `enactApprovedChanges` L1102: se elimina esa espera); el Consejo **no enmienda el texto**: promulga o **devuelve una vez con motivación** (veto suspensivo); la Cámara reaprueba por absoluta y entonces promulgación obligada; silencio al vencer el plazo = promulgación tácita. El Consejo mantiene el **índice consolidado** de leyes (con RP-6). Ley por **mayoría absoluta de la Cámara**; ley = texto + cambio de constantes, nunca acto singular sobre un inhabitant; iniciativa solo de representantes; todo voto es mensaje SSB firmado y visible (ya lo es: se documenta como garantía, RP-10) | Consejo = k representantes en colegio sin presidente; sin veto (promulgación automática); mayoría simple; el presidente conserva el escaño | TK-G05, TK-G10, TK-84 |
| TK-D06 | **Presidente del Consejo de Gobierno**: mandato, reelección, incompatibilidad con la Cámara, qué *ejecuta*, límites (decreto, disolución); **nombra su Consejo** (¿qué carteras en una red?); **"no disuelve sin dimitir"**: ¿apelación al pueblo?; **presupuesto** como ley previa a toda tesorería; ¿reglamentos de ejecución?; ¿veto?; ¿jefatura del Estado separada?; ¿poderes de excepción? | Cap. VI (442) | Elección directa a doble vuelta, ciclo desfasado 30 d respecto a la Cámara; mandato 60 d, reelección libre, sin revocación (responde ante las urnas y ante el Consejo de Justicia, D07); **nombra `governmentCouncil`** (carteras: tesorería, admin de cadena, puentes Multiverse; los PUB quedan en la sociedad civil, D11); incompatibilidad con el escaño. **No puede proponer leyes ni vetarlas** (la devolución es de Legislación, D05). **Materia** = claves chain-admin de Faircoin3 (`addcvn`, `addcoinsupply`, `setchainparameters`) y tesorería multisig k-de-n con el Consejo (TK-82), **solo con ley promulgada** (`lawId`, TK-84) y **dentro de la `budgetLaw` del ciclo** (sin presupuesto: prórroga del anterior). `executiveOrder` solo de ejecución, cita `lawId`, público, impugnable ante Justicia. **Disolución solo con dimisión**: `dissolutionAndResignation` lleva a Cámara y Presidencia a elecciones en el ciclo siguiente (el desfase de D15 se restablece después); nunca disolución sin dimitir. Sin jefatura de Estado separada; sin poderes de excepción (en una red no hay estado de sitio que declarar) | ejecutivo colegiado (Consejo elegido); sin disolución en ningún caso; máximo 3 ciclos consecutivos; veto suspensivo presidencial | TK-G06, TK-84, TK-66, TK-82, TK-D18 |
| TK-D07 | **Consejo de Justicia**: quién es "el mundo judicial" en la red; **cómo se accede a la judicatura** (Trevijano no elige jueces por sufragio: mérito + independencia); control de constitucionalidad (quién lo insta, cuándo, efecto); **jurado** vs voto popular del caso; ¿juzga el Consejo los actos de la Presidencia?; publicidad del proceso vs cifrado | Cap. V (421) | **Acceso**: juez = inhabitant nombrado por el Consejo de Justicia entre quienes tienen **certificado de `School`** (curso de constitución de la red) y ≥ 2 ciclos de antigüedad; `courtsNomination` deja de ser elección popular (bootstrap: la constituyente D09 nombra el primer Consejo). "Mundo judicial" = jueces en activo + mediadores con ≥ 1 caso; eligen por mayoría absoluta al Presidente del Consejo de Justicia, que nombra su Consejo. **Jurado** = sorteo verificable (mecanismo RP-3) de J inhabitants por caso: el jurado da el veredicto, el juez la orden; `POPULAR` (plebiscito de 14 d sobre el caso) se elimina. **Constitucionalidad**: cualquier representante, la Presidencia o una parte pueden instar `constitutionalChallenge` contra una ley promulgada; el Consejo resuelve en 21 d con `lawAnnulment` motivado y público; la ley queda suspendida mientras tanto. El Consejo **juzga los actos de la Presidencia** (una `censureAct` de la Cámara, D18, vale como prueba, no como condena). Publicidad: RP-7 tal cual (instrucción cifrable, veredicto y órdenes en claro); divergencia asumida con el proceso público trevijanista por el riesgo real de las partes en una red | acceso por elección popular (actual `courtsNomination`); jueces por sorteo puro; mundo judicial = todo el censo; proceso público obligatorio | TK-G07, TK-76, TK-77, TK-D18, TK-D09 |
| TK-D08 | **Lealtad republicana**: definición; ¿es la lealtad al mandato, a la forma de Estado, a la mónada?; **lealtad vs fidelidad** (¿es la fidelidad de la tribu a su líder deslealtad republicana por definición?) | Cap. I (340) | Lealtad = compromiso con el mandato publicado + con la separación de poderes; deslealtad medible en el log (votos, propuestas). Fidelidad a persona/tribu no computa ni como lealtad ni como deslealtad: solo se cotejan actos contra mandato | lealtad como virtud no codificable → sin revocación automática; (b) voto disciplinado de tribu = deslealtad presunta | TK-G04, TK-G09, TK-D11, TK-D17 |
| TK-D09 | **Acción constituyente**: qué abre el período (¿por ausencia, como ANARCHY, o por **acción**, como la abstención activa?), quién redacta, ratificación (referéndum), ¿asamblea distinta de la Cámara?; **ruptura vs reforma**: ¿pueden los poderes constituidos tocar las constantes?; ¿siguen funcionando durante el período?; **génesis**: las constantes heredadas de Oasis (`TERM_DAYS` 60, umbral 25 %) nunca fueron constituidas por nadie; ¿se disuelve la asamblea al ratificar?; ¿elegibles sus miembros? | Cap. VII (467), VIII (494) | **Apertura por acción, no solo por ausencia**: (i) génesis del fork, (ii) 2 ciclos ANARCHY consecutivos, o (iii) `constituentCall` firmado por ≥ 25 % del censo dentro de un ciclo. **Las constantes heredadas son régimen provisional** (`provisionalConstants`) hasta la primera constituyente: el fork **no reforma Oasis por ley, abre constituyente** (ruptura, no reforma). Asamblea constituyente ≠ Cámara: elegida ad hoc por mónadas con la ley electoral ordinaria (G01/G02), de propósito único; los poderes constituidos siguen funcionando pero **no pueden tocar constantes** (rigidez, D07 anula); la asamblea **solo redacta**, no legisla. 80 % de la asamblea para el texto; **ratificación por referéndum**: mayoría de votantes con participación ≥ 50 % del censo (el referéndum decide la *forma*: sin menú de regímenes, TK-32). La asamblea se disuelve al ratificar; sus miembros elegibles. La constitución fija solo forma (órganos, ciclos, umbrales, quién es inhabitant), nunca programa (D12) | RP-9 tal cual (Cámara en ANARCHY, apertura solo por ausencia); apertura por abstención (participación < 50 % dos ciclos); miembros inelegibles el primer ciclo; ratificación sin quórum | TK-78, TK-G08, TK-D12, TK-D07 |
| TK-D10 | **Referéndum**: ¿solo constituyente o también legislativo/abrogatorio? | Cap. VIII; Libro II "Elecciones" (302) | Solo constituyente y ratificatorio; `Polls`/`Opinions` quedan como consulta sin fuerza | referéndum abrogatorio → nueva tarea G | TK-G08 |
| TK-D11 | **Partidos/tribus**: estatuto, financiación, ¿pueden presentar candidatos aunque el mandato sea personal? | Libro II "Partidos estatales" (289), "Unidad, consenso, pluralidad" (271) | Tribus = asociaciones civiles: pueden apoyar candidatos, no presentarlos; **sin RBU ni tesoro a tribus como tales**; roles operativos (CVN, PUB) sí | tribus como distritos (=D01 alt. b) | TK-75, TK-63, R11 |
| TK-D12 | **Ideología**: pasaje donde niega que la república sea ideología; "materia/forma/espíritu republicano"; **qué hace constitucional a una constitución** (criterio del art. 16 de 1789: separación de poderes en origen + representación; tener constantes escritas no basta); ¿constitución breve y rígida, sin catálogo de derechos-programa? | Libro II (171-222), Cap. VIII (494) | El fork **neutraliza el manifiesto** de Oasis a texto de tribu opcional; la constitución técnica (TK-25 → G11) fija **solo forma**: órganos, ciclos, umbrales, quién es inhabitant, rigidez (D09); ningún programa económico ni social (la RBU, ECOin y la fiscalidad de carbono son **leyes ordinarias**, derogables, no constantes). **Test de constitucionalidad** ejecutable (G11): dos elecciones distintas para legislativo y ejecutivo, jueces no nombrados por poder político, mandato imperativo, constantes solo mutables en período constituyente, karma fuera de la política. Si falla, el fork no es república constitucional, sea cual sea su texto | conservar manifiesto como preámbulo (divergente); RBU como constante | TK-25, TK-G11, R14, TK-D09 |
| TK-D13 | **Unitario vs federal**; mónada y municipio | Cap. II, VIII | Parlamentos de tribu se conservan como **autogobierno civil**, sin potestad legislativa general | federación de parlamentos de tribu | TK-63, TK-67 |
| TK-D14 | **Sufragio**: universal e igual; ¿voto obligatorio?; ¿censo? | Libro II "Elecciones" (302) | Universal e igual; elegible = inhabitant con ≥1 ciclo de antigüedad; karma nunca pesa | — | TK-32, TK-31 |
| TK-D15 | **Cronología**: mandatos, escalonamiento entre poderes; ¿caduca el Consejo de Legislación con la Cámara que lo eligió? | Caps. III–VI | Cámara 60 d, **Consejo de Legislación 60 d ligado a su Cámara** (las leyes aprobadas y no promulgadas al expirar las promulga el Consejo entrante, sin caducidad), Presidencia 60 d desfasada 30 d, Consejo de Justicia 120 d | todos coincidentes; Legislación 120 d independiente de la Cámara | TK-74, TK-G05 |
| TK-D17 | **Lealtad del ciudadano** (no solo del representante): qué le debe el inhabitant a la República; ¿tiene consecuencias codificables (elegibilidad, censo) o es solo virtud cívica? | Cap. I (340); Libro II "Espíritu republicano" (208) | Sin consecuencia codificable: la lealtad ciudadana es virtud, no dato. Solo se registra la del representante (G09). El sufragio nunca se condiciona a ella (D14) | (a) elegibilidad ligada a antigüedad/actividad (ya en D14); (b) karma como proxy (rechazado: RP-4) | TK-D14, TK-G09 |
| TK-D18 | **Control de la Cámara sobre la Presidencia** sin poder derribarla: interpelación, comisiones, rendición de cuentas de tesorería y claves de cadena | Cap. III (381), VI (442) | Presidencia publica **informe firmado por ciclo** (tesorería, actos chain-admin); cualquier representante puede **interpelar** con respuesta obligatoria en 7 d; la Cámara puede **reprobar** un acto (sin efecto sobre el cargo, con efecto de publicidad y de prueba para el Consejo de Justicia); **sin moción de censura** | (a) comisión de investigación con acceso a claves de solo lectura; (b) reprobación bloquea la siguiente ejecución de tesorería | TK-G10, TK-D06 |
| TK-D16 | Rastreo de **divulgación** adicional (diariorc.com, mcrcalicante, Octavio Plaza "extracto república", vídeos) y contraste con el libro | web | — | — | todas D |

## Carril G · Gobernanza republicana (rediseño por defecto)
Arquitectura por defecto (de D01–D15): **mónadas → Cámara de Representantes Monádicos → Consejo de Legislación (promulga)** · **Presidente del Consejo de Gobierno (directo, ejecuta cadena y tesoro)** · **Consejo de Justicia (elegido por el mundo judicial)** · **Asamblea constituyente ad hoc**.

| ID | Tarea | Depende | Seam | T | P |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-G01 | Mónadas: asignación determinista de censo a colegios de tamaño M (`monad_model.js`), publicada como `monadAssignment {cycle, seedHash, M}`; `seedHash` fijo desde el ciclo fundacional (D01 default; alt. (d) lo rota), altas nuevas entran por el mismo hash | D01 (default) | nuevo modelo; `inhabitants_model.js` | M | H |
| TK-G02 | Doble vuelta dentro del ciclo de 60 d (primera 1-30, segunda 31-60) | D04, G01 | parliament_model.js:28 `termWindowFor`, `resolveElectionImpl` | M | H |
| TK-G03 | Mandato imperativo: `mandate` firmado por candidato; vista de cotejo voto-mandato | D02 | nuevo tipo; parliament_view.js | M | H |
| TK-G04 | Revocación por deslealtad (RP-11): `recall` iniciado por la mónada, mayoría absoluta del censo de la mónada | D03, D08, G03 | nuevo tipo; `parliamentTerm` por representante | M | H |
| TK-G05 | Cámara + Consejo de Legislación: propuestas solo de representantes monádicos; `legislationPresidentElection` por la Cámara (absoluta) y `legislationCouncil` nombrado por el Presidente; promulgación = `parliamentLaw` con `lawId`, `promulgatedBy[]` (Presidente + Consejo) en ≤ 7 d; `lawReturn` (devolución motivada, una vez); promulgación tácita al vencer plazo; `enactApprovedChanges` deja de esperar al fin de mandato; `lawIndex` consolidado | D05, D15, G01 | `canPropose` L1298, `enactApprovedChanges` L1102 | L | H |
| TK-G06 | Presidencia del Consejo de Gobierno (RP-1 rediseñada): elección directa, ciclo desfasado, sin iniciativa legislativa ni veto; `governmentCouncil` nombrado (carteras); **materia** = claves chain-admin + tesorería multisig k-de-n (TK-84, TK-82) bajo `budgetLaw` del ciclo; `executiveOrder{lawId}` público e impugnable; `dissolutionAndResignation` (elecciones dobles en el ciclo siguiente) | D06, D15, D18 | parliament_model.js; `faircoin3-admin`; banking_model.js (tesoro) | L | H |
| TK-G07 | Consejo de Justicia: `judgeAppointment` por el Consejo (requiere certificado `School` + antigüedad); electorado del Presidente = mundo judicial; `justiceCouncil` nombrado por el Presidente; `juryDraw` (sorteo verificable por caso, veredicto de jurado + orden de juez); `constitutionalChallenge` / `lawAnnulment` (21 d, suspensión cautelar); eliminar `POPULAR` y `DICTATOR` de los métodos | D07, D09, G10 | courts_model.js `nominateJudge`/`voteNomination` L139-155, L368; school_model.js (lectura de certificados) | L | H |
| TK-G08 | Referéndum solo constituyente/ratificatorio; `Polls` sin fuerza | D10 | polls_model.js (sin cambio), doc | S | M |
| TK-G09 | Lealtad medible: informe automático mandato vs votos por representante | D08, G03 | vista | M | M |
| TK-G11 | Constitución técnica (absorbe TK-25): `constitutionDraft` inicial de **solo forma** que el equipo del fork *propone* a la primera constituyente (TK-78), nunca impone; suite `test/constitutional.js` con los 5 criterios de D12 como prueba de aceptación de todo el carril G | D12, D09, G05, G06, G07, G01 | nuevo doc + test; parliament_model.js:17-26 | M | H |
| TK-G10 | Control sin derribo: `executiveReport` firmado por ciclo; `interpellation` con plazo; `censureAct` (reprobación de acto, no de cargo); vista de cuentas en Parliament | D18, D05, G06 | nuevos tipos; parliament_view.js; banking_model.js (lectura) | M | H |
| TK-75 | RP-2 solo personas al legislativo | D11 | `resolveTarget` | S | H |
| TK-31 | RP-3 sorteo verificable en empates | D14 | L408-437 | S | M |
| TK-32 | RP-4 karma fuera de la política; eliminar KARMATOCRACY/DICTATORSHIP del menú; karma fuera del orden de candidaturas a juez | D14 | banking_model.js:832-840, parliament_model.js:23, courts_model.js:805 | M | **C** |
| TK-76 | RP-5 quitar DICTATOR de Courts | D07 | courts_model.js:139-155 | S | H |
| TK-33 | RP-6 derogación con memoria | — | L1145-1147 | S | M |
| TK-77 | RP-7 sentencias públicas | D07 | `issueVerdict` | M | H |
| TK-34 | RP-8 reformulada: **iniciativa de mónada** (10 % del censo de la mónada obliga a su representante a presentar la propuesta, vía mandato imperativo); la iniciativa popular directa al 10 % del censo general pasa a alternativa (divergente: D10, draftv1 #13) | D02, D05, G01 | `canPropose` | M | H |
| TK-78 | RP-9 asamblea constituyente ad hoc: `provisionalConstants` en génesis; `constituentCall` (25 % del censo) o 2× ANARCHY abren `constituentPeriod`; elección de asamblea por mónadas; `constitutionDraft` (80 %); `ratificationReferendum` (mayoría, quórum 50 %); constantes solo mutables desde el período; disolución al ratificar | D09, D07, G01, G02, G08 | nuevo modelo `constituent_model.js`; parliament_model.js:17-26 (constantes), L373-393 (`virtualAnarchyTerm`) | L | **H** |
| TK-36 | RP-10 transparencia del gobernante | — | larp_model.js:576 → parliament_view.js | M | H |
| TK-79 | `kind` + payload en propuestas (CVN_ADMISSION, COIN_SUPPLY, BANKING_RULES) | — | `createProposal` | M | H |
| TK-84 | Materia del ejecutivo: mapa acción-admin ↔ ley promulgada; CLI rechaza sin `lawId` | D06, TK-79 | `faircoin3-admin` | M | H |
| TK-26 | Re-auditoría contra los 14 elementos de draftv1 tras los parches | todas G | doc | S | H |

*Nota de hilado:* RP-1 (TK-74 en el plan anterior) se **absorbe** en TK-G05+TK-G06; TK-74 queda como alias.

## Carril C · Cadena Faircoin3 — sin cambios respecto al plan anterior (TK-39…49, TK-90), más:
| ID | Tarea | Default | Alternativas |
| :-- | :-- | :-- | :-- |
| TK-C00 | Clonar `faircoin/faircoin` en `base/teoria/vendor/faircoin` para citar fichero:línea | sí (80 MB más, ignorado por git) | citar solo en línea |
| TK-48 | Distribución (v1 TK-12) | **A) emisión solo a tesoro multisig vía `addcoinsupply`, por ley promulgada** | B) snapshot UTXO Faircoin2; C) híbrido |
| TK-49 | Puente asamblea→cadena | admin = Presidencia (G06); doble voto tribu+general para CVN | solo Cámara |

## Carril B · Banking multi-moneda — TK-50…60 sin cambios. Carril F · TK-61…67. Carril E · TK-68…73.
(Tablas completas ya redactadas en la versión anterior del plan; se vuelcan tal cual en backlog.md con la columna "depende" enlazando a D/G donde aplica: TK-60→D10/TK-79; TK-63/67→D11/D13; TK-66→D06.)

## Carril L · Legal, marca, comunidad, proyecto
| ID | Tarea | Default | Alternativas |
| :-- | :-- | :-- | :-- |
| TK-80 | Nombre/marca | contactar a rasos (fair-coin.org) y usar "Faircoin3" si no hay objeción en 30 días | ticker nuevo desde ya |
| TK-81 | Licencias | daemon+CLI MIT; Oasis AGPL | — |
| TK-82 | Custodia | multisig + topes + "moneda social" | — |
| TK-83 | Comunicación / antiguos tenedores | tras TK-48 | — |
| TK-P01 | Operadores iniciales: ¿cuántas personas/tribus para 3 CVN + 2 PUB? | 3 CVN, 2 PUB, 1 explorador | — |
| TK-P02 | Ideología del fork (D12) | neutralizar manifiesto | conservar |

## Mapa de carriles (para backlog §2)
```
D (doctrina) ──defaults──▶ G (gobernanza) ──G06/TK-84──▶ C (cadena: admin = ejecutivo)
                                  │                          │
                                  └──TK-79──▶ B (banking) ◀──┘ TK-47/50
                                                  │
                                                  ▼
                                            F (federación) ──▶ E (economía real)
L (legal/proyecto) corre en paralelo; TK-48 y TK-80 bloquean TK-90 (mainnet)
```
Sprints: 0 rescate (TK-39, 40, 41, 57, C00, 80, 48, D16) · 1 esqueleto andante (B) · 2 endurecer B · 3 testnet + puente (C) ∥ 3' G con defaults (D pendientes no bloquean: cada G declara su default) · 4 F · 5 E · 6 constitución (D12, TK-25) + mainnet.

## Verificación
1. Script sobre `backlog.md`: IDs únicos (TK-01…90, TK-D01…16, TK-G01…09, TK-C00, TK-P01…02); cada "depende" existe; cada ruta `vendor/oasis/...` citada existe y la línea contiene el símbolo.
2. Cada TK-D tiene las 5 columnas (buscar/dónde/default/alternativas/desbloquea) y cada "desbloquea" apunta a un ID existente; cada TK-G tiene al menos un D o "—".
3. Mapeos v1 (25) y v2 (13 + RP-10) presentes una vez; TK-74 marcado alias de G05/G06.
4. `pura.md` §5 → puntero; referencias internas intactas.
5. `git status`: solo `backlog.md` nuevo y `pura.md` modificado; `vendor/` ignorado.
