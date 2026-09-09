# Diez redes sobre Oasis

**Informe de tutoría · TFG «Modelador de Redes» · 2026-09-09.** Evaluación de los ejemplos presentados en su potencialidad, puntuación de la plasticidad del software base (Oasis 1.0.7 @ `9a657b7` + ecosistema FairCoop), catálogo de diez redes arquetípicas (tres iniciadas, siete propuestas) y vías para pasar del juguete *animus iocandi* a ciencia aplicada y a ciclos DevOps reales.

<dl class="ficha">
<dt>Objeto</dt><dd>Repo <code>alephscriptorium-eng/modelador-redes</code> v0.2.0, rama <code>main</code> en <code>162cc60</code> (23 commits, un autor)</dd>
<dt>Ramas</dt><dd><strong>Cuatro</strong>, no tres: tres nodos (<code>dev/res_publica</code>, <code>dev/colectivizaciones</code>, <code>dev/clase</code>) y una arista (<code>dev/res_publica+colectivizaciones</code>, en pausa), todas mergeadas con <code>--no-ff</code></dd>
<dt>Material</dt><dd>2.428 líneas de drafts y fichas · generador Python de 1.699 líneas con 8 ficheros de test · web estática publicada en Pages</dd>
<dt>Código auditado</dt><dd>Oasis 1.0.7: 70 modelos, 32.849 líneas, 67 vistas, 1.069 tests upstream. FairCoop: inventariado (12 repos) y <em>no</em> auditado</dd>
<dt>Veredicto corto</dt><dd>Lo que se demuestra no es la plasticidad del software sino la plasticidad del <strong>método de auditoría</strong>, que se ha doblado tres veces sin romperse. El software tiene plasticidad declarativa alta y plasticidad operativa casi nula: <strong>22/40 hoy, 34/40 con los parches del catálogo</strong></dd>
</dl>

## 1. Qué se ha presentado, leído desde la tutoría

El alumno sostiene que el proyecto es un «modelador dual (SNH, fair ecosystem) para sociedad y economía». Conviene fijar tres precisiones antes de puntuar nada.

**El catálogo es un grafo, y hay cuatro ramas.** El propio `llms.md` del repo lo define: nodos (doctrinas puras auditadas contra el mismo commit de Oasis) y aristas (híbridos o contrastes entre dos nodos). La cuarta rama, la arista `res_publica+colectivizaciones`, está en pausa por decisión correcta: no se puede contrastar dos constituciones hasta que ambas tengan auditoría propia. En la defensa hay que decir «tres nodos y una arista», porque la arista es precisamente la pieza que convierte una colección de ejemplos en un catálogo.

**La dualidad SNH / Fair está desequilibrada, y el trabajo lo sabe.** Las 33.000 líneas de Oasis están auditadas con `fichero:línea`; del ecosistema FairCoop hay cero líneas auditadas. El alumno verificó por API que `faircoin/faircoin` no recibe commits desde 2022-02-05, que los dominios de FairCoop y Bank of the Commons están caídos y que fair-coin.org anunció el «cooling down» en junio de 2024. La respuesta ha sido honesta y doble: sustituir Faircoin por lo que Oasis usa de verdad (ECOin vía el módulo `Banking`) y dejar planificado un génesis nuevo («Faircoin3», carril C) más un plan de vendorización de 12 repos (`vendor/plan.md`, sin ejecutar). El lado «fair» del título es hoy documental, no auditado. No es un defecto de ejecución sino de alcance: hay que declararlo así en el resumen.

**No se implementa nada, y eso está dicho en la primera línea.** «No se implementa ningún producto. El repo es documentación de backlog y el generador que la publica.» Los parches RP-1…10, CL-1…11 y EU-1…6 son especificaciones con punto de intervención, no código. La palabra «modelador» promete más de lo que hay si se lee como simulador; es exacta si se lee como *catálogo de modelizaciones*: doctrina → criterios → auditoría → confrontación → parches → backlog → revisión. Esa cadena de seis pasos es la tecnología real del trabajo y es lo que hay que evaluar.

### 1.1 El método en seis pasos, y sus tres flexiones

| Paso | res_publica | colectivizaciones | clase |
| :-- | :-- | :-- | :-- |
| 1. Corpus → unidades auditables | 7 criterios normativos | 8 criterios normativos | 7 **coordenadas** de análisis (no hay nada que «cumplir») |
| 2. Auditoría con `fichero:línea` | Parliament, Courts, Banking, L.A.R.P. | Tribes, Industry, Market, Transfers, Jobs, Housing, School, Inhabitants | Capa cortical: config, hops, update, panic, IA, Multiverse |
| 3. Confrontación | Cumple / Falla / Parcial / Ortogonal | Igual, más «existe y no manda» | **Trituración**: implementada / ausente / fusionada / en manos del operador |
| 4. Parches | RP-n que *reparan* un criterio | CL-n que *conectan* lo que ya existe | Solo EU-n de **eutaxia** (lo único que la doctrina licencia prescribir) |
| 5. Backlog por carriles con defaults | D → G → C → B → F → E → L | D' → G' → B' → E' → F' | D → T → EU |
| 6. Revisión retroalimentada | 8 fichas (Libro III, cap. a cap.) | 1 ficha (por tema) | 0 (por concepto, planificadas) |

El método se dobló tres veces: de reparar (Trevijano) a conectar (colectividades) a triturar (Bueno). El generador tuvo que doblarse con él: la expresión regular de identificadores del extractor de backlog admite ya `TK|OP|RP|CL|EU` y carriles con apóstrofo (`TK-D'01`), y el commit `505868b` es la huella de esa adaptación. Esa es la plasticidad demostrada, y es más interesante que la del software.

## 2. Evaluación de los ejemplos en su potencialidad

Rúbrica de siete criterios, 0–5 cada uno. Se evalúa lo que el material *permite*, no lo que ejecuta.

| Criterio | res_publica | colectivizaciones | clase |
| :-- | --: | --: | --: |
| Corpus → criterios con certeza marcada | 4 | 4 | 3 |
| Auditoría verificable (`fichero:línea`) | 5 | 5 | 4 |
| Confrontación y hallazgos estructurales | 5 | 5 | 4 |
| Parches con seam y «lo que no se toca» | 4 | 5 | 3 |
| Backlog con caminos por defecto | 5 | 4 | 3 |
| Revisión que corrige aguas arriba | 4 | 2 | 0 |
| Honestidad epistémica (grados de certeza, «no verificado») | 5 | 5 | 5 |
| **Total / 35** | **32** | **30** | **22** |

### 2.1 res_publica (Trevijano): el nodo maduro

**Lo que vale.** Tres hallazgos que ningún manual de Oasis dice y que el código confirma: el karma es un solo escalar que decide desempate electoral, ley bajo KARMATOCRACY, orden de jueces y cuantía de renta básica (`parliament_model.js:422`, `courts_model.js:805`, `banking_model.js:932`); la fusión de poderes está implementada como comprobación de integridad (`courts_model.js:140-155` exige gobierno `DICTATORSHIP` para que el gobernante juzgue); y la «anarquía calculada» de `resolveElection` (`parliament_model.js:373-393`) es un período constituyente permanente que nadie diseñó. El backlog v3 con caminos por defecto (cada incógnita doctrinal tiene un default que deja avanzar al carril siguiente) es una técnica de gestión de incertidumbre exportable. Las ocho fichas de revisión corrigen tareas concretas aguas arriba con enlace de línea, y crearon tareas nuevas (D17, D18, G10, G11) al detectar huecos: el control del ejecutivo sin derribo, el test de constitucionalidad ejecutable.

**Lo que falta.** Nada está verificado contra el libro: las ocho fichas son «reconstrucción de memoria» con certeza A/B/C del revisor. El propio índice lo declara como deuda. El carril C (cadena Faircoin3 con génesis nuevo) multiplica el alcance por diez respecto al carril G y es donde el trabajo deja de ser auditoría para ser proyecto de infraestructura. La conclusión de `draftv1` («no es un clon y no puede serlo: falta el territorio y falta la escala») es la frase más honesta del repo y debería ir en el resumen de la memoria.

### 2.2 colectivizaciones (1936-37): la auditoría más fina

**Lo que vale.** Audita justo los módulos que el nodo anterior dejó «en una línea» y encuentra la estructura de propiedad del código: la tribu pertenece a su fundador (`tribes_model.js:721`, no puede irse; `:726-729`, si se le fuerza la tribu muere), la instalación industrial a quien firmó el mensaje raíz (`industry_model.js:164`, `:980`), y trabajo, material y ECOin entran en la misma bolsa de puntos (`:306-321`). El argumento por vocabulario (en 33.000 líneas no aparece *assembly*, *council*, *recall* ni *commons*; *salary* doce veces) es una técnica de auditoría barata y contundente. Y el hallazgo central es constructivo: la asamblea *ya existe* (todo parlamento de tribu nace en `ANARCHY`, `:1354-1384`) y solo hay que darle manos. La única ficha (`01-asamblea`) detectó que la asamblea podía votarse un dictador de tribu (`parliament_model.js:1443-1445`) y cerró la puerta en CL-1.

**Lo que falta.** Una ficha de seis. Toda la doctrina es paráfrasis sin página. Y hay un problema técnico no tratado que el tutor debe señalar: la unidad familiar (`household`, CL-9) es un tipo autodeclarado sobre una red donde ya «un feed = una persona» es una convención sin verificación (`inhabitants_model.js:86-88`). El salario familiar sobre hogares autodeclarados es un incentivo sybil de libro; la validación por asamblea que propone CL-9 mitiga pero no resuelve. También queda sin verificar si ECOin admite multisig k-de-n (CL-5 lo da por hecho).

### 2.3 clase (Bueno): la semilla más difícil y la más transversal

**Lo que vale.** Es un draft semilla, pero hace dos cosas que los otros no. Primera: corrige el chuletario generado por un LLM antes de usarlo (las «capas del Estado» del chuletario no son las de Bueno; las capas del cuerpo político son conjuntiva, basal y cortical; el diagrama que identifica géneros de materialidad con ejes antropológicos «se descarta»). Segunda: la tabla de las nueve ramas del poder contra Oasis produce el hallazgo más transversal del repo: **la red tiene poderes sin ramas**. Toda la capa cortical (caps del handshake, hops, invitaciones del PUB, puentes Multiverse, `POST /update`, modo pánico) y los parámetros constitutivos de la basal (constantes de carbono y de renta básica, `walletPub`) están en manos del operador del nodo, que no es un órgano del cuerpo político sino un poder exterior a él. Ese hallazgo afecta a los diez arquetipos del catálogo: ninguna constitución que se escriba en el log manda sobre el fichero de configuración.

**Lo que falta.** Todo lo demás. Y un riesgo: quedarse en filosofía. La salida está en el propio draft: los parches de eutaxia EU-1…6 (respaldo real de identidad, `POST /update` que no destruya `src/configs`, métrica de uptime, confirmación en dos pasos del modo pánico, constantes con procedencia) son *hardening* de seguridad y operación. Es el nodo más filosófico y el más DevOps a la vez.

### 2.4 La arista, y el generador

La arista en pausa es una decisión correcta y su draft conserva aún las ingenuidades del chuletario original (smart contracts en Faircoin, nodo central en SSB), marcadas para corregir. El generador (`modelador build|check|zip|indice`) es el contenido informático del TFG que más se parece a software: descubre modelos, valida el grafo, extrae backlogs de tablas heterogéneas, reescribe enlaces al blob del SHA auditado y falla si queda una ruta local o un enlace roto. Tiene tests y no tiene CI que los ejecute; `public/` va commiteado. Es un sitio estático bien hecho y debe presentarse como tal, no esconderse detrás de la doctrina.

## 3. Puntuación de la plasticidad del software base

Plasticidad, aquí: cuánto régimen distinto se obtiene por cuánto cambio. Ocho dimensiones, con la evidencia que los tres nodos ya han verificado, puntuadas «hoy» (código en `9a657b7`) y «potencial» (tras los parches de tamaño S/M que el catálogo propone; nada de tamaño L).

| # | Dimensión | Evidencia (`fichero:línea`) | Hoy | Potencial |
| :-- | :-- | :-- | --: | --: |
| P1 | **Parametría constitucional**: constantes que cambian el régimen | `parliament_model.js:17-26` (60 d, 25 %, 7 d, 15 d), `banking_model.js:14-21` (renta básica), `courts_model.js:8-11` (plazos). Todas hardcodeadas; `POST /update` borra `src/configs` (`backend.js:9552`) | 2 | 5 |
| P2 | **Selector de regímenes**: métodos de gobierno y de justicia | `METHODS` (`:22-23`): DEMOCRACY, MAJORITY, MINORITY, DICTATORSHIP, KARMATOCRACY, ANARCHY; Courts (`:139`): JUDGE, MEDIATION, POPULAR, KARMATOCRACY, DICTATOR. Menú amplio y cerrado: añadir un método es bifurcar | 4 | 4 |
| P3 | **Primitivas reutilizables** | Tribu cifrada anidable (`tribes_model.js:341`), parlamento por tribu (`:1354-1445`), voto con quórum y mayoría acotada (`industry_model.js:23-27`, `:98-101`), épocas selladas con hash (`banking_model.js:960-962`), vales `TIME`/`TRUST` (`transfers_model.js:25`), certificados (`school_model.js:1222`), muro público del gobernante (`larp_model.js:576`) | 4 | 5 |
| P4 | **Tipos de mensaje nuevos** sin tocar el protocolo | SSB es un log tipado: los tres nodos proponen más de quince tipos (`mandate`, `household`, `delegate`, `constituentCall`, `executiveReport`…) sin cambiar replicación ni cifrado. No hay cargador de módulos: cada tipo nuevo es un parche al backend | 4 | 5 |
| P5 | **Desacoplamiento** (inverso de los seams rígidos que golpean todos los modelos) | Cinco acoplamientos: karma escalar único (`banking_model.js:840` → `parliament:422`, `courts:805`, `banking:932`); autor = propietario (`tribes:721`, `industry:164`, `school:1222`); precio > 0 (`market:182`, `shops:415`); un feed = una persona (`inhabitants:86-88`); operador del nodo como poder exterior (config, hops, `backend.js:4651`) | 1 | 3 |
| P6 | **Ejecutabilidad**: ¿una ley cambia algo? | `enactApprovedChanges` (`:1102`) publica texto; nada lee un `parliamentLaw` para cambiar una constante ni un reparto. Rama ejecutiva ausente (nueve ramas, nodo `clase`) | 1 | 3 |
| P7 | **Capa económica intercambiable** | `Banking` es un adaptador RPC de 14 métodos; dinero solo en `sendtoaddress` (`:1004`); pero `^E` ×12 y `coin: "ECO"` ×7 hardcodeados; tesoro = cartera del PUB (`:913-917`) | 2 | 4 |
| P8 | **Observabilidad y trazabilidad** | Log de solo-anexado, votos firmados y visibles, karma publicado (`:501-506`), hash por época; sin uptime (`stats_model.js:438`); derogación = tombstone de cliente (`:1145`) | 4 | 5 |
| | **Total / 40** | | **22** | **34** |

**Lectura.** Oasis es plástico en lo que se *declara* (tipos, primitivas, menú de regímenes, trazabilidad) y rígido en lo que *pesa* (cinco seams que los tres nodos golpean en el mismo sitio, y una ley que no ejecuta nada). Tres de los cinco acoplamientos son cambios de una línea (`if (p <= 0)`, `tribe.author !== userId`, `1 + karma/100`); los otros dos (un feed = una persona; el operador como soberano de hecho) no son parches sino problemas abiertos de toda red sin territorio ni identidad verificada, y el trabajo hace bien en no fingir que los resuelve.

Hay un dato más que la puntuación no recoge y que el catálogo de la sección 4 hace visible: **el software no es neutral**. Tiene una doctrina implícita (karmatocracia: mérito por notoriedad, decaimiento exponencial, castigo por bytes) y de las diez redes arquetípicas hay exactamente una (la meritocracia política, nº 10) que le encaja con parches de tamaño S. La plasticidad de un sistema se mide mejor desde el arquetipo que le exige menos cambios, y ese arquetipo delata el sesgo del código.

## 4. Catálogo: diez redes arquetípicas

Tres iniciadas y siete propuestas, elegidas para que cada seam rígido de Oasis sea golpeado por al menos dos doctrinas distintas y para que cada una tenga un corpus con verbatim disponible (cosa que hoy ningún nodo tiene). Cada ficha lleva el mismo esqueleto que exige `llms.md` para abrir un nodo: corpus, criterios, lo que ya está en el código, lo que choca, parche clave, arista natural, coste (S/M/L) y valor para ciencia aplicada.

<div class="catalogo">

<article class="arq iniciado">

### 1 · `res_publica` — República constitucional (Trevijano)

- **Estado:** nodo, `draftv2`, 8 fichas, 10 parches RP, carriles D→G→C→B→F→E→L.
- **Criterios:** separación de poderes en origen; representación uninominal con mandato imperativo; sufragio igual sin karma; constituyente previo; república como forma, no ideología.
- **Ya está:** calendario fijo sin convocante (`parliament:17-38`); retorno a `ANARCHY` (`:373-393`); procedimiento codificado.
- **Choca:** karma (`:422`, `banking:840`); tribu candidata (`canPropose :1298`); `DICTATOR` (`courts:140-155`); derogación por tombstone (`:1145`).
- **Parche clave:** TK-32 (karma fuera de la política) y TK-78 (`constituent_model.js`).
- **Deuda:** verificar las 8 fichas contra el libro.

</article>

<article class="arq iniciado">

### 2 · `colectivizaciones` — Comunismo libertario 1936-37

- **Estado:** nodo, `draftv0`, 1 ficha de 6, 11 parches CL.
- **Criterios:** asamblea soberana que no puede abdicar; cargos rotatorios y revocables; propiedad colectiva; salario familiar; federación de delegados; intercambio sin precio; voluntariedad.
- **Ya está:** parlamento de tribu en `ANARCHY` (`:1354-1384`); suelo inmovible de la renta básica (`banking:941`); educación gratis por defecto (`school:320`); copyleft (`industry:439`).
- **Choca:** autor vitalicio (`tribes:721`); steward único (`industry:164`, `:980`); reparto pro rata a capital (`:306-321`); precio > 0 (`market:182`); sin hogar (`inhabitants:86-88`).
- **Parche clave:** CL-1 (la asamblea gobierna la tribu) y CL-9 (`household`).
- **Riesgo no tratado:** hogar autodeclarado = sybil de hogar.

</article>

<article class="arq iniciado">

### 3 · `clase` — Materialismo filosófico (Bueno)

- **Estado:** nodo semilla; coordenadas K1–K7; nueve ramas trituradas; EU-1…6 sin implementar.
- **Coordenadas:** tres géneros de materialidad; cierre categorial; espacio antropológico; capas conjuntiva/basal/cortical; nueve ramas; eutaxia; holización.
- **Hallazgo:** poderes sin ramas: la capa cortical entera está en manos del operador del nodo (`server-config.json`, `oasis-pub.js:41`, `backend.js:4651`, `:9552`).
- **Reducción detectada:** `karma = rawKarma − carbonGrams` (`banking:839-840`) reduce M₃ a M₁: fisicalismo, no materialismo.
- **Parche clave:** EU-1 (órgano para la capa cortical), EU-2/EU-3 (respaldo de identidad, `update` sin `reset --hard`).
- **Valor:** transversal; sus parches son hardening.

</article>

<article class="arq">

### 4 · `sorteo` — Democracia por sorteo

- **Corpus:** Aristóteles, *Política* IV; Hansen, *The Athenian Democracy* (1991); Manin, *Los principios del gobierno representativo* (1997); Flanigan et al., «Fair algorithms for selecting citizens' assemblies», *Nature* 596 (2021).
- **Criterios:** cargos por sorteo entre voluntarios; mandatos cortos sin reelección; rendición de cuentas al cesar (*euthynai*); jurados grandes por sorteo; asamblea con iniciativa.
- **Ya está:** RP-3 ya pide sorteo verificable por hash del log; rotación por calendario (`:17-38`); turno sin elección en L.A.R.P. (`larp:164-166`); `juryDraw` propuesto en TK-G07.
- **Choca:** toda la elección (`:744-761`); karma en el desempate (`:422`); sin límite de mandatos; `POPULAR` en Courts es plebiscito, no jurado.
- **Parche clave:** `sortitionTerm`: `resolveElection` sorteado entre quienes publican `willingness`; `euthyna` obligatoria reutilizando `executiveReport` (TK-G10).
- **Arista:** `res_publica+sorteo` (elección frente a sorteo: el debate de Manin sobre el mismo código).
- **Coste:** S/M. **Valor:** alto; hay algoritmos de selección con cuotas contra los que comparar el hash-sorteo.

</article>

<article class="arq">

### 5 · `confederalismo` — Municipalismo libertario / confederalismo democrático

- **Corpus:** Bookchin, *The Next Revolution* (2015); Öcalan, *Confederalismo democrático* (2011); Contrato Social de Rojava (2014, 2016); Knapp, Flach & Ayboğa, *Revolution in Rojava* (2016).
- **Criterios:** asamblea de base como unidad; confederación de delegados con mandato revocable; copresidencia paritaria; ecología social (la economía subordinada a la ecología); poder dual.
- **Ya está:** anidamiento (`tribes:341`); la tasa de carbono es la única eutaxia ecológica del código (`banking:31-37`); parlamento por tribu.
- **Choca:** `parentTribeId` es privacidad, no delegación (CL-8 lo diagnostica); un solo `leaderId`; sin atributos de persona por diseño (la paridad no es representable); el carbono *resta karma individual* en vez de financiar el común.
- **Parche clave:** `delegate` con mandato (compartido con CL-8); `leaderIds[2]` con copresidencia; el impuesto de carbono ingresa en `tribeTreasury` (CL-5) en lugar de descontarse del karma.
- **Arista:** `colectivizaciones+confederalismo` (federación sindical de 1936 frente a federación territorial de Rojava).
- **Coste:** M. **Valor:** único arquetipo con implementación viva documentada; permite comparación etnográfica.

</article>

<article class="arq">

### 6 · `liquida` — Democracia líquida

- **Corpus:** Behrens, Kistner, Nitsche & Swierczek, *The Principles of LiquidFeedback* (2014); Blum & Zuber, «Liquid Democracy», *J. Political Philosophy* 24 (2016); Kling et al., «Voting behaviour and power in online democracy», ICWSM (2015).
- **Criterios:** delegación por tema, transitiva, revocable en cualquier momento; el voto directo anula la delegación; delegaciones públicas; una iniciativa entra a votación por quórum de apoyos; voto preferencial.
- **Ya está:** `FOLLOW_MAJORITY` (`votes:173`) es la única delegación del sistema; `tags_model.js` da los temas; el grafo de *follows* es una delegación latente; todo voto es firmado y visible.
- **Choca:** la delegación es al agregado anónimo, no a una persona; sin transitividad; `polls` sin quórum (`:84-86`); iniciativa racionada (`:1298`).
- **Parche clave:** tipo `delegation {topicTag, to, until}`; resolución transitiva con corte de ciclos en el recuento de `votes_model.js`; entrada por quórum de apoyos (RP-8 reformulada).
- **Arista:** `res_publica+liquida` (mandato imperativo frente a delegación revocable: parecidos peligrosos).
- **Coste:** M. **Valor:** **el más alto para ciencia aplicada**: existe software de referencia (LiquidFeedback) y datos empíricos del Partido Pirata sobre concentración en superdelegados; el karma de Oasis es una concentración ya medible.

</article>

<article class="arq">

### 7 · `mixta` — República mixta y republicanismo neorromano

- **Corpus:** Polibio, *Historias* VI; Maquiavelo, *Discursos* I; Pettit, *Republicanism* (1997); Skinner, *Liberty before Liberalism* (1998).
- **Criterios:** gobierno mixto; no-dominación: toda decisión es contestable; tribunado con veto; magistraturas colegiadas y anuales; *cursus honorum*; dictadura temporal con plazo y nombrada por otro poder.
- **Ya está:** revocación de leyes a 15 días (`:1145`) ≈ veto tribunicio; `TERM_DAYS` 60 ≈ anualidad; `DICTATORSHIP` como método (es el único arquetipo que puede conservarla, si le pone plazo); Courts como instancia de contestación; `MINORITY` al 20 % (`:240-242`).
- **Choca:** gobierno unipersonal; el candidato elige su propio método (`:81`); ninguna magistratura veta a otra; sin elegibilidad por historial.
- **Parche clave:** `collegiate: true` (dos `leaderId` con `intercessio` recíproca); `tribunate` = cargo elegido por el 20 % reutilizando el umbral `MINORITY` como voz de la minoría en lugar de como legislador; `DICTATORSHIP` con `expiresAt` y nombramiento por la Cámara.
- **Arista:** `res_publica+mixta` (dos republicanismos: separación en origen frente a contestabilidad).
- **Coste:** M. **Valor:** Pettit da un criterio computable sobre el log (dominación = capacidad de interferencia arbitraria: quién puede `tombstone` a quién).

</article>

<article class="arq">

### 8 · `comunes` — Gobierno de los bienes comunes (Ostrom)

- **Corpus:** Ostrom, *Governing the Commons* (1990); Ostrom, *Understanding Institutional Diversity* (2005, marco IAD); Cox, Arnold & Villamayor, meta-análisis de los 8 principios, *Ecology & Society* 15 (2010); Hess & Ostrom, *Understanding Knowledge as a Commons* (2007); Frey & Schneider, «Modular politics», *CSCW* (2021).
- **Criterios (los 8 principios):** límites claros; congruencia con condiciones locales; elección colectiva de las reglas; monitoreo por los propios; sanciones graduadas; resolución barata de conflictos; reconocimiento externo; empresas anidadas.
- **Ya está:** límites = tribu con clave rotada (`tribes:533-541`); elección colectiva parcial en Industry (`:211-223`); `MEDIATION` (`courts:139`); anidamiento (`:341`); log público = monitoreo gratis; copyleft (`industry:439`).
- **Choca:** ninguna sanción graduada: solo expulsión (`:533`) o tombstone; las reglas son constantes globales, no locales por tribu; `laborRate` lo fija el steward (`:438`). El seam es `reports_model.js` (361 líneas, sin auditar por ningún nodo).
- **Parche clave:** `sanction {level}` en Reports → Courts (aviso, suspensión temporal del voto, expulsión); `tribeRules` con constantes de Industry y Banking por tribu (principio 2).
- **Arista:** `colectivizaciones+comunes` (Aragón 1936 leído como recurso de uso común) o `cooperativa+comunes`.
- **Coste:** M. **Valor:** **muy alto**: el marco empírico más validado para instituciones autogestionadas; los principios son ya una rúbrica y las «situaciones de acción» del IAD mapean uno a uno a los modelos de Oasis.

</article>

<article class="arq">

### 9 · `cooperativa` — Cooperativismo (ACI, Mondragón, FairCoop)

- **Corpus:** Declaración de la Alianza Cooperativa Internacional (1995, 7 principios); estatutos de Rochdale (1844); Ley 27/1999 de Cooperativas; Arizmendiarrieta y el modelo Mondragón (ratio salarial, fondos COFIP/FRO); FairCoop como cooperativa integral y Bank of the Commons; `FreedomCoop/valuenetwork` (contabilidad REA), ya en el plan de vendorización.
- **Criterios:** adhesión voluntaria; un socio, un voto; retorno proporcional a la actividad, nunca al capital; fondos irrepartibles; autonomía; educación; intercooperación; ratio salarial máxima.
- **Ya está:** un miembro, un voto en Industry (`:98-101`, `:211-223`); School gratis (`:320`); Projects (financiación con objetivo); arte previo en `valuenetwork`.
- **Choca:** `computeShares` (`:306-321`) mezcla capital y trabajo (retorno por capital = anticooperativo); excedente repartido al 100 % (`:960-970`), sin fondo irrepartible; steward (`:164`); sin ratio; renta por karma.
- **Parche clave:** `eco` fuera del numerador de `computeShares` (capital remunerado a interés limitado); `reserveFund` como porcentaje obligatorio del `pot` hacia `tribeTreasury` (CL-5); `maxRatio` de puntos por hora entre miembros.
- **Arista:** `colectivizaciones+cooperativa` (colectividad ≠ cooperativa: el debate de la CNT) y **`cooperativa+faircoin`**, la arista que reconecta el lado «fair» del título.
- **Coste:** S/M. **Valor:** alto y con **derecho positivo**: hay ley y estatutos contra los que auditar con verbatim, cosa que ningún nodo actual tiene.

</article>

<article class="arq">

### 10 · `meritocracia` — Meritocracia política

- **Corpus:** Bell, *The China Model* (2015); Platón, *República* V–VII; el examen imperial confuciano; Young, *The Rise of the Meritocracy* (1958) como crítica; Sandel, *The Tyranny of Merit* (2020).
- **Criterios:** selección por examen o certificación; promoción por desempeño; deliberación de expertos; legitimidad por resultados; democracia en la base y mérito en la cúspide.
- **Ya está: casi todo.** `KARMATOCRACY` (`:22-23`): la ley del proponente con más karma; karma como mérito acumulado con decaimiento (`banking:525-607`); certificados de School (`:1222`); desempate por karma (`:422`); jueces por karma (`courts:805`); TK-D07 ya propone jueces con certificado. La estructura tribu/general de Oasis es exactamente «democracia abajo, mérito arriba».
- **Choca:** el «mérito» es notoriedad (un `post` vale 10, un `like` 2), no competencia; el carbono resta (`:840`); ningún examen condiciona el cargo; no hay evaluación del desempeño del gobierno (TK-G10 la daría).
- **Parche clave:** `merit = f(certificados, veredictos confirmados, leyes no revocadas)` en lugar de `karma` por volumen; elegibilidad = certificado; `ANARCHY`/`DEMOCRACY` en tribus, `KARMATOCRACY` en el general.
- **Arista:** `meritocracia+res_publica` es **la arista de mayor contraste del catálogo**: el escalar que Trevijano exige abolir es aquí el principio constitutivo. También `meritocracia+clase` (holización y karma).
- **Coste:** S. **Valor:** metodológicamente decisivo: es el arquetipo *nativo* del código y demuestra que Oasis tiene doctrina implícita.

</article>

</div>

**Suplentes**, por si el tribunal prefiere otra cobertura: *orden espontáneo* (Hayek, *Derecho, legislación y libertad*: el gossip y `ANARCHY` como catalaxia, el precio > 0 como virtud, aboliría `Banking`); *decisionismo* (Schmitt: `DICTATORSHIP` y estado de excepción; el único que legitima al operador del nodo como soberano; útil como control negativo); *sociocracia* (consentimiento, círculos enlazados, elección sin candidatos; `Tasks`, `Agenda` y `Workflows` ya existen y es el arquetipo más cercano a un equipo DevOps).

### 4.1 Cobertura de seams

Cada columna es un seam rígido o un módulo; cada fila, un arquetipo. El objetivo del catálogo es que ninguna columna dependa de un solo modelo.

| Arquetipo | Parliament | Courts | Banking / karma | Tribes | Industry | Market | School | Cortical (operador) |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 res_publica | ● | ● | ● | ○ | | | ○ | |
| 2 colectivizaciones | ● | | ● | ● | ● | ● | ○ | |
| 3 clase | ○ | ○ | ● | | ○ | | | ● |
| 4 sorteo | ● | ● | ○ | | | | | |
| 5 confederalismo | ○ | | ● | ● | | | | |
| 6 liquida | ● | | | ○ | | | | |
| 7 mixta | ● | ● | | | | | ○ | |
| 8 comunes | | ● | ○ | ● | ● | | | ○ |
| 9 cooperativa | | | ● | ○ | ● | ○ | ● | |
| 10 meritocracia | ● | ● | ● | | | | ● | |

● seam central del modelo · ○ seam tocado.

## 5. Del juguete a la ciencia aplicada y a DevOps

La licencia compuesta (GPL-3.0 + capa Animus Iocandi) y el eslogan «juguete-pasatiempo» son una zona experimental legítima. Bajar de ella no exige cambiar de licencia ni de tono: exige que alguna afirmación del catálogo pueda ser **falsada** y que algún parche pueda ser **desplegado**. Seis vías, ordenadas por coste, con el primer paso concreto de cada una.

### 5.1 Ciencia aplicada

**A. Constitución ejecutable: parches como tests de aceptación.** Oasis trae 1.069 tests en 82 ficheros, un runner con aislamiento de `~/.ssb` y un `seed.js`. Cada RP/CL/EU tiene ya un seam; convertirlo en un test que hoy falla (rojo) y que el parche pone en verde es el paso mínimo entre especificación e ingeniería. TK-G11 lo propone (`test/constitutional.js` con los cinco criterios de constitucionalidad). *Primer paso:* escribir el test de RP-4 («ningún resultado electoral depende del karma») contra `chooseWinnerFromCandidaturesAsync` y verlo fallar en `9a657b7`. Ampliación natural: pruebas basadas en propiedades (invariantes: sufragio igual, ninguna ley sin quórum, ningún tombstone resucita) con `fast-check`.

**B. Simulación multiagente sobre nodos reales.** N contenedores con `ssb-server` y agentes sintéticos que publican, votan y forman tribus según perfiles; el log de solo-anexado es el dataset. Métricas: Gini del karma por ciclo, frecuencia de `ANARCHY`, captura del legislativo por tribus, dispersión de la renta básica. Hipótesis falsables que ya están implícitas en el repo: «el acoplamiento karma-renta produce un Gini superior a *x* en *k* ciclos»; «el sorteo (nº 4) reduce la captura respecto a la elección»; «la delegación transitiva (nº 6) concentra en superdelegados como en LiquidFeedback». *Primer paso:* `docker-compose` con un PUB (receta en `docs/PUB/deploy.md`: Node 22, `server-config.json`) y tres clientes sembrados con `test/seed.js`.

**C. Estudio observacional en La Plaza.** El PUB público del proyecto es una población real y el karma se publica en el log (`banking:501-506`): la distribución de mérito, los mandatos y las leyes son observables sin instrumentar nada. Requiere consentimiento y un protocolo ético (los datos son públicos por diseño, pero las personas no son sujetos de experimento por defecto). *Primer paso:* un `modelador observar` que lea un log SSB y emita `data/observaciones.json` con las mismas métricas de B, para comparar simulación y campo.

**D. Elección social computacional.** Cada método de `METHODS` es una regla de agregación y la cascada de desempate (`:408-437`) es una función de elección social determinista. Sus propiedades formales (monotonía, resistencia a la manipulación, tratamiento de la abstención) se pueden demostrar o refutar con la literatura COMSOC, y la máquina de estados proposición → voto → promulgación → revocación cabe en un modelo TLA+ o Alloy pequeño. *Primer paso:* especificar `enactApprovedChanges` y `tombstone` en Alloy y comprobar «ninguna ley revocada vuelve a mostrarse».

### 5.2 Ciclos DevOps reales

**E. Externalizar la constitución y devolver un parche upstream.** El paso que más plasticidad compra por menos código: un bloque `constitution` en `oasis-config.json` con las constantes de `parliament:17-26`, `banking:14-21` y `courts:8-11`, con procedencia registrada (EU-5), y que `POST /update` deje de destruir `src/configs` (EU-3). Con eso P1 pasa de 2 a 5 y todos los arquetipos se vuelven configuraciones en lugar de forks. La AGPL obliga a devolver: un *pull request* aceptado en `epsylon/oasis` convierte el juguete en contribución. *Primer paso:* elegir el parche más pequeño y más decisivo (RP-6, derogación con memoria, tamaño S; o TK-32) e implementarlo con su test de A.

**F. Integración continua del propio catálogo.** El repo tiene tests y no tiene CI. Añadir un workflow que ejecute `pytest`, `modelador build` y `modelador check`, más dos comprobaciones nuevas: `scripts/vendor.sh --check` (del plan de vendorización) y un `modelador citas` permanente que verifique que cada `fichero:línea` citado en `modelos/` existe en el vendor al SHA y contiene el símbolo nombrado. Con eso la auditoría es reproducible y se rompe visiblemente si upstream cambia. *Primer paso:* promover el script de un solo uso `check_citas.py` a subcomando con test.

**G. Pipeline especificación → parche → prueba → despliegue.** Cada TK con seam nace como rama `oasis-<modelo>/<TK>` en un fork; el id del TK va en el commit; el generador publica el estado de cada tarea (especificada / implementada / probada / desplegada) leyendo el fork. El testnet constitucional de B es el entorno de despliegue; para la capa económica, `fairchains-tool` crea una cadena PoC desde JSON sin recompilar (verificado en `vendor/plan.md`), lo que da una *regtest* Faircoin3 sin tocar mainnet. *Primer paso:* un `modelador parches --modelo X` que emita el esqueleto de la serie de parches con sus seams.

**H. Eutaxia como SRE.** El nodo `clase` define eutaxia como capacidad de recurrencia. Traducida: uptime, réplicas alcanzables, épocas ejecutadas a tiempo, identidades con respaldo. `faircoin_exporter` (Prometheus, en el plan de vendorización) y EU-4 (uptime en `stats`) dan las métricas; un panel con objetivos de nivel de servicio es la primera implementación operativa de una categoría de Bueno. Y el propio repo puede comer su comida: completar la migración a Radicle (anunciada, no ejecutada) y tomar las decisiones del catálogo (qué nodo abrir, qué arista cerrar) en una instancia de Oasis cuya primera población sea el equipo del proyecto.

### 5.3 Orden recomendado

| Hito | Contenido | Vías | Horizonte |
| :-- | :-- | :-- | :-- |
| 1 | CI con `pytest`, `check`, `vendor --check` y citas verificadas; constantes externalizadas a config | F, E | Semanas |
| 2 | Testnet en contenedores; un parche S implementado con test y enviado upstream; suite constitucional | A, B, E, G | Meses |
| 3 | Simulación con métricas, estudio observacional con protocolo ético, un artículo comparando dos arquetipos (sorteo frente a elección, o líquida frente a mandato) | B, C, D | Un semestre |

## 6. Observaciones para la defensa

- **Decir «tres nodos y una arista»**, y explicar que la arista en pausa es la prueba de que el catálogo es un grafo y no una lista.
- **Declarar la asimetría de la dualidad:** Oasis auditado línea a línea, FairCoop inventariado y muerto desde 2022; la sustitución por ECOin/Banking y el plan de vendorización son la respuesta, no una omisión.
- **Declarar la deuda doctrinal en el resumen:** ninguna de las nueve fichas está verificada contra su fuente; la certeza A/B/C es la del revisor. La rúbrica de la sección 2 premia haberlo dicho; el tribunal castigará no decirlo.
- **Presentar el generador como el software del TFG** (1.699 líneas, tests, validación de grafo y enlaces, extractor tolerante de backlogs) y los parches como especificaciones. Si hay tiempo antes de la defensa, implementar uno de tamaño S (RP-6 o TK-32) con su test: cambia la naturaleza del trabajo.
- **Corregir `CITATION.cff`:** «Modelador de Redes Contributors» no sirve para un trabajo de fin de grado; debe constar el autor.
- **Llevar la sección 3 como resultado:** la plasticidad de Oasis es 22/40 hoy y 34/40 con parches S/M; tres de los cinco acoplamientos rígidos son cambios de una línea; el software tiene doctrina implícita y el arquetipo que la delata es la meritocracia.
