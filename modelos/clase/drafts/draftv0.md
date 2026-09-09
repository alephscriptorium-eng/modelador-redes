# Materialismo filosófico · Trituración de OASIS 1.0.7 con las coordenadas K1-K7

**Revisión 0 — 2026-09-09.** La semilla (`draft.md`) fijó la panorámica de Bueno, corrigió los errores del chuletario y dejó un plan (b0 trituración, b1 nueve ramas, b2 backlog; carriles D → T → EU). Este documento es b0: audita el código real con las siete coordenadas, propone siete parches de eutaxia EU-1…EU-7 y abre el backlog por carriles. No prescribe un régimen: Bueno no lo hace. Tritura.

---

## 0. Qué cambia respecto de la semilla

| # | Hallazgo | Consecuencia |
| :-- | :-- | :-- |
| 1 | **Oasis politiza la capa conjuntiva y una rama basal; la capa cortical entera está en manos del operador del nodo.** Parlamento y tribunales existen como órganos; defensa, diplomacia y federación existen como fichero de configuración, shell y técnica criptográfica. | El producto central (las nueve ramas, §3.D) no es «qué falta», sino «qué poderes no tienen rama». El operador es un poder exterior al cuerpo político (§3.E). |
| 2 | **La red ejecuta una sola reducción entre géneros de materialidad, y la ejecuta dos veces.** `karmaScore = rawKarma − carbonGrams` y `engagementScore = rawScore − carbonGramsForScore`: peso político (M3) menos gramos de CO₂ (M1) en la misma resta. | K1 se viola en el único punto donde la red intenta articular géneros. No es materialismo, es fisicalismo (§3.C). |
| 3 | **La eutaxia de Oasis es un calendario.** Los mandatos se recurren en ventanas de 60 días desde 2020-01-01 sin convocante; si nadie gobierna, el ciclo es una anarquía virtual. Al lado, tres distaxias de código: el export excluye la clave, el pánico borra sin confirmación y `/update` hace `git reset --hard` sobre la configuración. | La eutaxia se puede medir con indicadores de código (§3.A) y es el único lugar donde este nodo licencia parches (§4). |
| 4 | **El log holiza y el karma des-holiza.** Un feed que ha publicado es un inhabitant; la población que fija el quórum sale de ese censo; la mayoría es mitad más uno de partes iguales. Pero los empates se resuelven por karma, `KARMATOCRACY` es un régimen propio y las sugerencias de contacto re-estratifican el círculo. | La democracia de Oasis es una forma aritmética sobre átomos definidos por autoría (§3.B), con una re-estratificación por notoriedad que la forma no reconoce. |
| 5 | **Siete costuras de la exploración previa citaban la línea vecina.** `steward` :163→:164, `ssbKeys.box` :319→:320, `SecretStack` :57→:56, `removeSSB` :7→:6, `if (file === 'secret')` :24→:25, `enactApprovedChanges` :1104→:1102, `TERM_EPOCH` :26→:25. | Corregidas aquí con `sed -n`; ninguna cambia la lectura. Las dos que afectan a `draft.md` van como correcciones al margen. |
| 6 | **La semilla heredaba cuatro supuestos técnicos falsos** (CVN, contratos en Faircoin, nodo central, Faircoin vivo) y un diagrama que identificaba géneros de materialidad con ejes antropológicos. | Descartados. La capa económica es ECOin por RPC (§1.2). Géneros y ejes son cortes distintos y se auditan por separado (§2). |

**Metodología.** Todo lo que aquí se afirma sobre Oasis está verificado contra el código fuente, no contra su documentación. Árbol auditado: `vendor/oasis` (ignorado por git; clónalo con `git clone --depth 1 https://github.com/epsylon/oasis.git`). Commit auditado: **`9a657b776fcafc7c24bf3ad61825316385ecf513`, "Oasis release 1.0.7", 2026-09-08**. Cada afirmación lleva `fichero:línea` y la línea contiene el símbolo nombrado. La doctrina de Bueno va con grado de certeza (A repetido en todas las fuentes, B conocido sin verbatim, C reconstrucción probable) y con la etiqueta **[doctrina, sin verbatim]** hasta que el carril D la verifique en los libros. Rutas: `models/` y `views/` relativas a `vendor/oasis/src/`; el resto con ruta completa.

---

## 1. Estado del arte verificado

### 1.1 OASIS 1.0.7

- Paquete `@krakenslab/oasis` v1.0.7, AGPL-3.0 (`src/server/package.json:2-3,9`). Node.js en el servidor y HTML+CSS sin JavaScript en el navegador (README, «No browser JavaScript», fuente primaria del proyecto). 70 ficheros en [src/models/](vendor/oasis/src/models/) (32.849 líneas), 67 vistas, un `backend.js` de 10.556 líneas.
- Los módulos que importan a la trituración: [parliament_model.js](vendor/oasis/src/models/parliament_model.js) (1.615 líneas), [courts_model.js](vendor/oasis/src/models/courts_model.js) (961), [industry_model.js](vendor/oasis/src/models/industry_model.js) (991), [banking_model.js](vendor/oasis/src/models/banking_model.js) (1.479), [tribes_model.js](vendor/oasis/src/models/tribes_model.js) (939), [crypto.js](vendor/oasis/src/models/crypto.js) (571), [inhabitants_model.js](vendor/oasis/src/models/inhabitants_model.js) (505), [stats_model.js](vendor/oasis/src/models/stats_model.js) (634), [logs_model.js](vendor/oasis/src/models/logs_model.js) (380), [larp_model.js](vendor/oasis/src/models/larp_model.js) (953), [melody_model.js](vendor/oasis/src/models/melody_model.js) (181), [fediverse_model.js](vendor/oasis/src/models/fediverse_model.js) (749) y los ficheros pequeños que deciden la persistencia: [panicmode_model.js](vendor/oasis/src/models/panicmode_model.js) (15), [exportmode_model.js](vendor/oasis/src/models/exportmode_model.js) (52), [onboarding_model.js](vendor/oasis/src/models/onboarding_model.js) (182).
- **Todo el mundo institucional es un log leído por tipo.** `readTyped(ssbClient, types, opts)` ([L77](vendor/oasis/src/models/typed_log.js#L77)) es la única puerta: parlamentos, tribunales, industrias y bancos son mensajes con un `type`, indexados en cliente. No hay base de datos de estado, hay un feed por clave y una reconstrucción por lectura.
- **La derogación es un tombstone que cada cliente valida por su cuenta.** `tombstone_validator.js` acepta el mensaje si `c.type === 'tombstone'` y `c.target` es una cadena ([L12](vendor/oasis/src/models/tombstone_validator.js#L12)) y lo descarta si el autor no coincide con el del objetivo ([L26](vendor/oasis/src/models/tombstone_validator.js#L26)). Nada obliga fuera de la interfaz.

### 1.2 La capa económica

- **ECOin por RPC.** Todo el dinero pasa por `makeClient(url, user, pass)` y `clientrpc.request({ method, params })` ([L22-L23](vendor/oasis/src/models/wallet_model.js#L22-L23)) sobre `@open-rpc/client-js` ([L5](vendor/oasis/src/models/wallet_model.js#L5)). El pago real de la RBU es un `sendtoaddress` desde la cartera del PUB ([L1004](vendor/oasis/src/models/banking_model.js#L1004)). Oasis no emite; lee la oferta de fuera.
- **Quién redistribuye: el nodo que se autodeclara PUB.** `isPubNode()` ([L214](vendor/oasis/src/models/banking_model.js#L214)) compara `walletPub.pubId` del fichero de configuración con `config.keys.id` ([L215-L217](vendor/oasis/src/models/banking_model.js#L215-L217)). Ese nodo ejecuta `executeEpoch` y `processPendingClaims` en un `setInterval` de 30 minutos ([L10265-L10273](vendor/oasis/src/backend/backend.js#L10265-L10273)).
- Consecuencia: la rama redistribuidora existe, es automática, y su titular es una entrada de JSON. Faircoin, Proof-of-Cooperation, CVN y contratos no aparecen en este árbol y no se usan en este nodo.

### 1.3 El corpus: siete coordenadas, no criterios

Bueno no prescribe un régimen; ofrece coordenadas de análisis. La única norma que sí ofrece, la eutaxia (K6), es la que se convierte en prueba de aceptación en §4. Escala A/B/C de `draft.md` §1; todo **[doctrina, sin verbatim]** hasta que el carril D lo verifique.

| # | Coordenada | Qué se le pregunta al código | Fuente | Cert. |
| :-- | :-- | :-- | :-- | :-- |
| K1 | **Tres géneros de materialidad** M1 (físico), M2 (fenomenológico), M3 (abstracto), inconmensurables y en *symploké* | ¿Qué es M1, M2 y M3 en cada módulo? ¿Ejecuta la red alguna reducción de un género a otro? | *Ensayos materialistas* (1972) | A |
| K2 | **Cierre categorial**: una categoría se cierra cuando concatena sus partes por operaciones propias; la filosofía es saber de segundo grado que coordina cierres | ¿Qué capas de la red son ciencia cerrada, técnica abierta o dependencia externa? | *Teoría del cierre categorial* (1992-93), *¿Qué es la ciencia?* (1995) | A |
| K3 | **Espacio antropológico**: ejes radial (cosas), circular (otros sujetos humanos), angular (númenes: sujetos no humanos con conocimiento o apetición) | ¿Qué relaciones habita cada eje en Oasis? ¿Está gobernado el eje angular? | *Ensayos materialistas*, *El animal divino* (1985) | A; extender el angular a IA y máquinas es lectura nuestra: **C** |
| K4 | **Capas del cuerpo político**: conjuntiva (el cuerpo consigo mismo), basal (con la naturaleza y la producción), cortical (con otras sociedades) | ¿Qué módulos pertenecen a cada capa? | *Primer ensayo sobre las categorías de las ciencias políticas* (1991) | B |
| K5 | **Nueve ramas del poder**: conjuntiva = ejecutiva, legislativa, judicial · basal = planificadora, redistribuidora, gestora · cortical = militar, diplomática, federativa | Por rama: implementada, ausente, fusionada o en manos del operador; quién la controla | *Primer ensayo…* | B |
| K6 | **Eutaxia / distaxia**: buen orden como capacidad de la sociedad política para recurrir, para persistir en el tiempo; no un fundamento moral | ¿Qué hace durar al sistema? ¿Qué lo mata? ¿Se mide a sí mismo en el tiempo? | *Primer ensayo…* | B |
| K7 | **Holización**: la democracia exige reducir la sociedad a partes homogéneas (ciudadanos iguales); la democracia es una forma, no un valor | ¿Qué holiza la red (qué es un átomo)? ¿Qué la re-estratifica? | *El fundamentalismo democrático* (2010), *Panfleto contra la democracia realmente existente* (2004) | B |

Dos nociones auxiliares que uso sin coordenada propia: **trituración** (análisis que descompone una idea en sus partes materiales para mostrar qué queda de ella), B; y **operador** de una institución (quien sostiene la capa basal sin ser parte formal del cuerpo político), reconstrucción nuestra, C, a verificar en D07.

---

## 2. Anatomía de los módulos leída con las categorías

Cada bloque dice qué es M1, M2 y M3 en el módulo (K1), en qué eje se mueve (K3) y a qué capa y rama pertenece (K4/K5).

### 2.1 Parliament — [parliament_model.js](vendor/oasis/src/models/parliament_model.js) · conjuntiva legislativa

**M3 fijado en constantes.** `TERM_DAYS = 60`, `PROPOSAL_DAYS = 7`, `REVOCATION_DAYS = 15`, `PROPOSAL_QUORUM = 2`, `QUORUM_RATIO = 0.25` ([L17-L21](vendor/oasis/src/models/parliament_model.js#L17-L21)); el catálogo de regímenes elegibles es `METHODS = ['DEMOCRACY', 'MAJORITY', 'MINORITY', 'DICTATORSHIP', 'KARMATOCRACY']` ([L23](vendor/oasis/src/models/parliament_model.js#L23)) y `ANARCHY` solo existe como método de voto, no como candidatura ([L22](vendor/oasis/src/models/parliament_model.js#L22)). Los umbrales son aritmética pura: 80 % para `MAJORITY`, 20 % para `MINORITY`, mitad más uno para `DEMOCRACY` ([L240-L242](vendor/oasis/src/models/parliament_model.js#L240-L242)); quórum de propuesta `max(2, ceil(n × 0,25))` ([L257-L259](vendor/oasis/src/models/parliament_model.js#L257-L259)). Ninguna de estas reglas constitutivas la ha votado nadie: son M3 sin sujeto.

**El tiempo del cuerpo político es un calendario.** `TERM_EPOCH = Date.UTC(2020, 0, 1)` y `TERM_SPAN_MS = TERM_DAYS × 86400000` ([L25-L26](vendor/oasis/src/models/parliament_model.js#L25-L26)): las legislaturas son ventanas fijas desde el 1 de enero de 2020, sin convocante. Si en una ventana no hay mandato, `virtualAnarchyTerm` ([L373](vendor/oasis/src/models/parliament_model.js#L373)) fabrica uno con `method: 'ANARCHY'` y `powerType: 'none'` ([L379-L380](vendor/oasis/src/models/parliament_model.js#L379-L380)). La sociedad política persiste sin gobierno por defecto de código.

**Quién propone y quién enacta.** `canPropose` ([L1298-L1311](vendor/oasis/src/models/parliament_model.js#L1298-L1311)): todos bajo `ANARCHY`, solo el titular bajo gobierno de persona, todos los miembros bajo gobierno de tribu. `enactApprovedChanges(expiringTerm)` ([L1102](vendor/oasis/src/models/parliament_model.js#L1102)) se invoca al expirar el mandato ([L1167](vendor/oasis/src/models/parliament_model.js#L1167)) y publica las leyes aprobadas como mensajes. Eso es todo lo que «ejecuta»: la rama legislativa está implementada; la ejecutiva no existe.

**Holización y karma.** La población que fija el quórum es `inhabitantsCount()` ([L244](vendor/oasis/src/models/parliament_model.js#L244), usado en [L1191](vendor/oasis/src/models/parliament_model.js#L1191)). Los empates electorales se resuelven por `maxKarma` ([L422-L423](vendor/oasis/src/models/parliament_model.js#L422-L423)); las propuestas se ordenan por karma descendente ([L576](vendor/oasis/src/models/parliament_model.js#L576)); bajo `DICTATORSHIP` o `KARMATOCRACY` la revocación sigue otro camino ([L650](vendor/oasis/src/models/parliament_model.js#L650)). El mismo módulo cuenta partes iguales y las pesa por notoriedad.

Eje: circular. M2: ninguna (el módulo no registra vivencia alguna, solo votos tipificados).

### 2.2 Courts — [courts_model.js](vendor/oasis/src/models/courts_model.js) · conjuntiva judicial

Cinco formas de resolver: `ALLOWED = new Set(['JUDGE', 'DICTATOR', 'POPULAR', 'MEDIATION', 'KARMATOCRACY'])` ([L139](vendor/oasis/src/models/courts_model.js#L139)). El veredicto `JUDGE` solo vale si lo firma `judgeId` ([L363](vendor/oasis/src/models/courts_model.js#L363)); `MEDIATION` si lo firma uno de los mediadores aceptados ([L364](vendor/oasis/src/models/courts_model.js#L364)); `POPULAR` y `KARMATOCRACY` abren una votación pública con un plazo `POPULAR_DAYS = 14` ([L11](vendor/oasis/src/models/courts_model.js#L11), [L368](vendor/oasis/src/models/courts_model.js#L368)).

**Fusión bajo dictadura.** `DICTATOR` exige que el gobierno vigente sea `DICTATORSHIP` y toma `dictatorId` del `powerId` del mandato ([L142-L151](vendor/oasis/src/models/courts_model.js#L142-L151)): la rama judicial se funde con la legislativa en una sola persona. Es la única fusión de ramas que el código declara explícitamente.

Eje: circular. M3: el catálogo de métodos. Rama judicial implementada; en `KARMATOCRACY` vuelve a entrar el karma como criterio de justicia.

### 2.3 Industry — [industry_model.js](vendor/oasis/src/models/industry_model.js) · basal planificadora

El `steward` es el autor del mensaje raíz ([L164](vendor/oasis/src/models/industry_model.js#L164)); toda mutación de la instalación exige `g.facility.steward === ssbClient.id` o lanza `Unauthorized` ([L457](vendor/oasis/src/models/industry_model.js#L457), [L484](vendor/oasis/src/models/industry_model.js#L484)). Las materias votables son `SUBJECTS = ["admit", "dissolve", "pause", "bpUpdate", "bpDelete", "buildUpdate", "buildDelete"]` ([L532](vendor/oasis/src/models/industry_model.js#L532)) con `passesThreshold` = máximo entre quórum y mayoría ([L98-L101](vendor/oasis/src/models/industry_model.js#L98-L101)). La planificación de la producción tiene un titular personal derivado de la autoría y un voto para lo demás.

Eje: radial (relación con lo producido) y circular (miembros). M1: el objeto producido no está en la red, solo su plano y su lote. Rama planificadora implementada, en manos de una persona.

### 2.4 Banking — [banking_model.js](vendor/oasis/src/models/banking_model.js) · basal redistribuidora y la única reducción entre géneros

**M3 basal en constantes.** `DEFAULT_RULES` ([L14-L21](vendor/oasis/src/models/banking_model.js#L14-L21)): épocas mensuales, `alpha 0.2`, reserva 500, tope 2.000 por época, tope 50 y suelo 1 por persona, pesos [0,2, 6], 30 días de gracia. El fondo es el 20 % del saldo del PUB acotado por reserva y tope ([L913-L917](vendor/oasis/src/models/banking_model.js#L913-L917)); `computeEpoch` ([L920](vendor/oasis/src/models/banking_model.js#L920)) pesa a cada persona con `clamp(1 + score / 100, wMin, wMax)` ([L932](vendor/oasis/src/models/banking_model.js#L932)) y paga `max(floorUbi, min(pool × w / W, capUser))` ([L941](vendor/oasis/src/models/banking_model.js#L941)).

**M1: el cuerpo físico del inhabitant es lo que pesa su feed.** `getCarbonGramsForUser` ([L609](vendor/oasis/src/models/banking_model.js#L609)) suma `Buffer.byteLength(JSON.stringify(m.value))` de cada mensaje ([L617](vendor/oasis/src/models/banking_model.js#L617)); `carbonGramsFromBytes = bytes / ONE_MIB × 0.095` ([L35](vendor/oasis/src/models/banking_model.js#L35)) traduce bytes a gramos de CO₂ con una constante sin procedencia; el bloque de constantes ([L31-L37](vendor/oasis/src/models/banking_model.js#L31-L37)) añade `ECOIN_PER_GRAM_CO2 = 0.1` y `ecoinTaxFromGrams` ([L36](vendor/oasis/src/models/banking_model.js#L36)). Es la única traducción de M1 a mundo físico que hay en la red.

**La reducción.** `rawKarma = scoreFromActions(actions)` ([L838](vendor/oasis/src/models/banking_model.js#L838)), `carbonGrams = await getCarbonGramsForUser(uid)` ([L839](vendor/oasis/src/models/banking_model.js#L839)), `karmaScore = Math.max(0, Math.round(rawKarma − carbonGrams))` ([L840](vendor/oasis/src/models/banking_model.js#L840)). Y otra vez para la RBU: `engagementScore = Math.max(0, Math.round(rawScore − carbonGramsForScore))` ([L1151](vendor/oasis/src/models/banking_model.js#L1151)). Un peso político (M3, acciones sociales) menos una magnitud física (M1, gramos) en la misma resta.

Eje: radial (bytes, carbono) y circular (acciones). Rama redistribuidora implementada y automática (`backend.js:10265-10273`); titular: el nodo autodeclarado PUB (§1.2).

### 2.5 Tribes y crypto — [tribes_model.js](vendor/oasis/src/models/tribes_model.js), [crypto.js](vendor/oasis/src/models/crypto.js) · cortical militar y federativa como técnica

Los campos estructurales de la tribu, con `parentTribeId`, están en `STRUCTURAL_FIELDS` ([L11](vendor/oasis/src/models/tribes_model.js#L11)); `parentTribeId` se fija al crear ([L341](vendor/oasis/src/models/tribes_model.js#L341)) y anida círculos en jerarquía padre-hijo sin ningún órgano federativo por encima. La defensa es cifrado: `crypto.createCipheriv('aes-256-gcm', key, iv)` ([L146](vendor/oasis/src/models/crypto.js#L146)) y reparto de la clave a cada miembro con `ssbKeys.box(tribeKeyHex, [memberFeedId])` ([L319-L320](vendor/oasis/src/models/crypto.js#L319-L320)). Al expulsar, `rotateTribeKey` genera una clave nueva y la redistribuye a los que quedan ([L753-L760](vendor/oasis/src/models/tribes_model.js#L753-L760)): la frontera del círculo se repara sola.

Eje: circular (pertenencia). Capa cortical: la tribu se defiende de las demás por técnica, no por poder; se federa por herencia de campo, no por delegación.

### 2.6 Servidor, configuración, PUB y Multiverse · la capa cortical en manos del operador

- **Cierre criptográfico importado.** `const caps = require('ssb-caps')` ([L8](vendor/oasis/src/server/SSB_server.js#L8)) y `const Server = SecretStack({ caps })` ([L56](vendor/oasis/src/server/SSB_server.js#L56)); la `caps.shs` viene de `server-config.json` ([L6](vendor/oasis/src/configs/server-config.json#L6)). Replicación por `ssb-ebt` y `ssb-friends` ([L60-L61](vendor/oasis/src/server/SSB_server.js#L60-L61)) con horizonte `"hops": 2` ([L12](vendor/oasis/src/configs/server-config.json#L12)). Quién puede hablar con quién y hasta dónde se replica son parámetros de fichero.
- **El círculo inicial viene de fábrica.** `"autofollow"` ([L25-L27](vendor/oasis/src/configs/server-config.json#L25-L27)) lo procesa el servidor en `config.autofollow.feeds` ([L88-L93](vendor/oasis/src/server/SSB_server.js#L88-L93)). En este commit está `"enabled": false` con `feeds: []`, pero el mecanismo existe y lo controla el operador.
- **La frontera individual.** `POST /block/:feed` llama a `friend.block` ([L7306-L7307](vendor/oasis/src/backend/backend.js#L7306-L7307)): la exclusión del círculo es una decisión de cada feed, sin órgano.
- **Federación desde shell.** Los invites del PUB se crean con `ssb.invite.create` desde `scripts/oasis-pub.js` con `uses` por argumento ([L40-L41](vendor/oasis/scripts/oasis-pub.js#L40-L41)); el plugin de invite depende de `config.pub` ([L70](vendor/oasis/src/server/SSB_server.js#L70)).
- **Diplomacia sin guard.** `POST /settings/fediverse` ([L4651](vendor/oasis/src/backend/backend.js#L4651)) y `POST /settings/fediverse/disconnect` ([L4663](vendor/oasis/src/backend/backend.js#L4663)) no llaman a `isLoopbackRequest` ([L170](vendor/oasis/src/backend/backend.js#L170)), a diferencia de `POST /update` ([L9552-L9553](vendor/oasis/src/backend/backend.js#L9552-L9553)); la cuenta de Mastodon se guarda en `configs/fediverse-accounts.json` ([L5](vendor/oasis/src/models/fediverse_model.js#L5)). Cualquier petición que alcance el puerto puede conectar o desconectar la red de otra red.

Eje: circular hacia dentro, cortical hacia fuera. M3: ficheros JSON. Titular: el operador del nodo.

### 2.7 Inhabitants, Polls y Opinions · holización y M2

- **El censo.** `authorsMsgs` = mensajes con autor y sin `tombstone` ([L87](vendor/oasis/src/models/inhabitants_model.js#L87)): un feed que ha publicado es un inhabitant. La presencia se reduce a tres cubos, `green` <2w, `orange` 2w-6m, `red` ≥6m ([L65-L73](vendor/oasis/src/models/inhabitants_model.js#L65-L73)).
- **La re-estratificación.** Las sugerencias de contacto suman `karmaBonus ≤ 20`, `skillBonus = 4 × habilidad común`, `activityBonus` 5/2/0 por cubo ([L217-L220](vendor/oasis/src/models/inhabitants_model.js#L217-L220)): el círculo se ordena por notoriedad, competencia y recencia.
- **Un feed, un voto.** Las consultas deduplican por `entry.voters.includes(v.author)` ([L99](vendor/oasis/src/models/polls_model.js#L99)); la unidad de cuenta es la clave.
- **M2 tipificado.** Las opiniones solo admiten categorías del catálogo `positive`, `constructive`, `moderation` ([L1](vendor/oasis/src/backend/opinion_categories.js#L1), [L18](vendor/oasis/src/backend/opinion_categories.js#L18), [L45](vendor/oasis/src/backend/opinion_categories.js#L45)); fuera del catálogo, `Invalid voting category` ([L59](vendor/oasis/src/models/opinions_model.js#L59)). La única M2 que entra en el feed lo hace convertida en M3. El tema visual vive en `oasis-config.json` del nodo, `themes.current || "Dark-SNH"` ([L24](vendor/oasis/src/views/settings_view.js#L24)): la experiencia es local, no replicada.

### 2.8 El eje angular: AI 42, L.A.R.P. y Melody

- **Un sujeto no humano que escribe en el feed.** `createAI` ([L235](vendor/oasis/src/models/logs_model.js#L235)) lee las acciones del usuario, las manda a `http://localhost:4001/ai` ([L137](vendor/oasis/src/models/logs_model.js#L137)) y publica hasta `MAX_ACTIONS = 40` ([L243](vendor/oasis/src/models/logs_model.js#L243)) mensajes `log` con `mode: 'ai'` ([L263](vendor/oasis/src/models/logs_model.js#L263), vía `publishLog`, [L166](vendor/oasis/src/models/logs_model.js#L166)). El humano aprueba con `POST /ai/approve` ([L61](vendor/oasis/src/views/AI_view.js#L61)). El servicio carga `oasis-42-1-chat.Q4_K_M.gguf` ([L32](vendor/oasis/src/AI/ai_service.mjs#L32)), escucha en `4001` sin autenticación ([L89](vendor/oasis/src/AI/ai_service.mjs#L89)) y se defiende de la inyección con una regex de siete palabras ([L52](vendor/oasis/src/AI/ai_service.mjs#L52)).
- **Calendario mítico.** `HOUSE_KEYS` con nueve casas ([L9](vendor/oasis/src/models/larp_model.js#L9)), `SOLAR_AGE_OFFSET = 10000000 − 2026` ([L139](vendor/oasis/src/models/larp_model.js#L139)), casa del mes por `monthIdx % HOUSE_KEYS.length` ([L149](vendor/oasis/src/models/larp_model.js#L149)). Una estructura numinosa embebida en el código, con turno rotatorio.
- **Comunicación oculta.** `embedTextInWav` ([L124](vendor/oasis/src/models/melody_model.js#L124)) esconde bits en el LSB de cada muestra a partir del byte 44 ([L140-L141](vendor/oasis/src/models/melody_model.js#L140-L141)): mensajes para quien sabe leerlos, fuera del círculo visible.

Lectura C **[doctrina, sin verbatim]**: para Bueno el eje angular es la relación con númenes (animales, dioses). Que una IA local que narra la vida del usuario y un calendario de casas sean númenes es extensión nuestra; el hecho verificado es que Oasis tiene un sujeto no humano que publica en el feed y una liturgia de tiempo propia, y que ninguno de los dos está gobernado por ningún órgano.

### 2.9 Persistencia: pánico, export, onboarding, update, stats · los indicadores de eutaxia

- `removeSSB` ([L6](vendor/oasis/src/models/panicmode_model.js#L6)) hace `fs.promises.rm(ssbPath, { recursive: true, force: true })` ([L10](vendor/oasis/src/models/panicmode_model.js#L10)); la ruta `POST` correspondiente llama a `panicmodeModel.removeSSB()`, mata el servidor con `pkill` y sale del proceso ([L8054-L8057](vendor/oasis/src/backend/backend.js#L8054-L8057)). Borrar M1 (el directorio) borra M3 (la clave): muerte sin confirmación en dos pasos.
- El export excluye `secret` ([L25-L26](vendor/oasis/src/models/exportmode_model.js#L25-L26)). El onboarding tiene un paso `backup` en `STEPS` ([L5](vendor/oasis/src/models/onboarding_model.js#L5)) que solo escribe un fichero bandera con `writeFileSync` ([L116](vendor/oasis/src/models/onboarding_model.js#L116)) desde `markStep` ([L123-L125](vendor/oasis/src/models/onboarding_model.js#L123-L125)). No hay camino de respaldo de la identidad.
- `POST /update` ejecuta `git reset --hard && git pull` sobre `repoRoot` ([L9556](vendor/oasis/src/backend/backend.js#L9556)), que contiene `src/configs/*.json` (caps, hops, wallet, cuentas). Actualizar destruye la configuración local.
- `stats_model.js` mide el disco de `~/.ssb` con `getFolderSize` ([L71](vendor/oasis/src/models/stats_model.js#L71), [L438](vendor/oasis/src/models/stats_model.js#L438)) y lista pubs desde `~/.ssb/ebt` ([L24](vendor/oasis/src/models/stats_model.js#L24)); `grep -ci uptime` = 0. La red mide su tamaño y sus pares, no su duración.

---

## 3. Confrontación: las coordenadas contra el código

Leyenda: ✅ la coordenada encuentra en el código una articulación reconocible · ⚠️ articulación parcial o fusionada · ❌ ausente, o violada.

| # | Coordenada / criterio | Estado en Oasis 1.0.7 | Veredicto |
| :-- | :-- | :-- | :-- |
| K1.a | Tres géneros presentes y distinguibles | M1 = bytes, disco, CO₂ (`banking_model.js:609-617`, `:35`; `stats_model.js:438`). M2 = opiniones tipificadas, tema local, cubos de actividad (`opinions_model.js:59`; `settings_view.js:24`; `inhabitants_model.js:65-73`). M3 = constantes y tipos de mensaje (`parliament_model.js:17-23`; `typed_log.js:77`) | ✅ **Distinguibles**, con M2 casi vacío: la vivencia solo entra como categoría |
| K1.b | Inconmensurabilidad: ninguna reducción entre géneros | `karmaScore = rawKarma − carbonGrams` (`banking_model.js:840`) y `engagementScore = rawScore − carbonGramsForScore` (`:1151`) | ❌ **Violada** en el único punto donde la red articula géneros (§3.C) |
| K2.a | Categorías cerradas | Criptografía (`SSB_server.js:56`, `crypto.js:146`) y replicación (`SSB_server.js:60-61`, `server-config.json:12`) son cierres importados y parametrizados por fichero | ✅ **Cerradas**, pero ajenas: Oasis no las reabre ni las gobierna |
| K2.b | Categorías abiertas o dependientes | Gobernanza cerrada en el log y abierta en la ejecución (`tombstone_validator.js:12,26`; `parliament_model.js:1102`); banca dependiente de RPC externo (`wallet_model.js:22-23`); IA sin cierre (`ai_service.mjs:52,89`) | ⚠️ **Lo propio de Oasis está abierto**; lo cerrado es de otros (§3.G) |
| K3.a | Eje radial | Infraestructura: pubs de `~/.ssb/ebt` (`stats_model.js:24`), disco (`:438`), bytes y carbono (`banking_model.js:617`, `:35`) | ✅ Radial = infraestructura, no naturaleza |
| K3.b | Eje circular | Follows y hops (`server-config.json:12`), block individual (`backend.js:7306-7307`), autofollow de fábrica (`server-config.json:25-27`), tribus anidadas (`tribes_model.js:11`, `:341`) | ⚠️ El círculo lo trazan decisiones individuales y ficheros del operador |
| K3.c | Eje angular | IA que publica 40 mensajes por clic (`logs_model.js:243`, `:263`), calendario de nueve casas (`larp_model.js:9`, `:139`), esteganografía (`melody_model.js:124`); único gobierno: `POST /ai/approve` (`AI_view.js:61`) | ⚠️ **Poblado y sin gobernar** (§3.F; lectura C) |
| K4 | Tres capas identificables | Conjuntiva: parlamento y tribunales. Basal: industria, banca, mercado. Cortical: caps, hops, invites, Multiverse, cifrado | ✅ Identificables; la cortical no es política sino técnica y configuración |
| K5 | Nueve ramas con órgano y titular | Legislativa y judicial implementadas; ejecutiva ausente; planificadora en manos del `steward` (`industry_model.js:164`, `:457`); redistribuidora automática en el nodo autodeclarado PUB (`banking_model.js:214-217`; `backend.js:10265-10273`); militar, diplomática y federativa sin órgano (`crypto.js:146`; `backend.js:4651`; `oasis-pub.js:40-41`) | ❌ **Poderes sin ramas**: 2 implementadas, 1 fusionable, 1 ausente, 2 personales, 3 en manos del operador (§3.D, §3.E) |
| K6.a | Eutaxia: mecanismos de recurrencia | Calendario fijo desde `TERM_EPOCH` (`parliament_model.js:25-26`), anarquía virtual (`:373-380`), rotación de clave de tribu (`tribes_model.js:753-760`), motor de épocas cada 30 min (`backend.js:10273`) | ✅ **La red recurre sola**, por reloj y por defecto de código |
| K6.b | Distaxia: qué mata al sistema | Export sin `secret` (`exportmode_model.js:25-26`), `backup` que solo escribe una bandera (`onboarding_model.js:116`), pánico sin confirmación (`backend.js:8054-8057`), `git reset --hard` sobre configs (`backend.js:9556`), sin medida de uptime (`stats_model.js`, 0 resultados) | ❌ **Cuatro distaxias y ninguna medida del tiempo** (§3.A) |
| K7.a | Holización: partes homogéneas | Censo por autoría (`inhabitants_model.js:87`), población = censo (`parliament_model.js:1191`), mayoría = mitad más uno (`parliament_view.js:21`), un feed un voto (`polls_model.js:99`) | ✅ **El log holiza**: el átomo es la clave que ha publicado (§3.B) |
| K7.b | Democracia como forma, sin re-estratificación oculta | Empates por karma (`parliament_model.js:422-423`), `KARMATOCRACY` como régimen (`:650`), propuestas ordenadas por karma (`:576`), sugerencias por karma (`inhabitants_model.js:217-220`), justicia karmática (`courts_model.js:139`) | ❌ **El karma des-holiza** lo que el log holizó (§3.C) |

**Recuento.** 6 ✅, 4 ⚠️, 4 ❌. Las cuatro violaciones son una sola cosa vista desde cuatro coordenadas: el karma (K1.b, K7.b) y el operador (K5, K6.b). Los hallazgos que siguen ordenan el diagnóstico.

### A. Eutaxia del sistema: ¿qué lo hace durar?

Lo que hace durar a Oasis no es un gobierno sino un reloj. Las legislaturas son ventanas de `TERM_SPAN_MS` contadas desde `TERM_EPOCH` (L25-L26 de `parliament_model.js`); nadie convoca y nadie puede no convocar. Si nadie gobierna, `virtualAnarchyTerm` (L373) devuelve un mandato con `powerType: 'none'` (L380): el cuerpo político existe aunque no tenga cabeza. La tribu que expulsa rota su clave y la reparte (`tribes_model.js:753-760`): la frontera se repara sin órgano. El PUB ejecuta épocas cada 30 minutos (`backend.js:10273`) aunque nadie mire. Con Bueno (K6, B, **[doctrina, sin verbatim]**): eutaxia es la capacidad de la sociedad política para recurrir, y Oasis recurre por automatismo.

Pero lo que la mata está a un clic. El export nunca incluye `secret` (`exportmode_model.js:25-26`), y el paso `backup` del onboarding escribe una bandera y nada más (`onboarding_model.js:116`, `:123-125`): quien pierde el disco pierde la identidad y con ella todos sus votos, cargos y saldos. El modo pánico borra `~/.ssb`, mata el servidor y sale del proceso (`panicmode_model.js:10`; `backend.js:8054-8057`) sin segunda confirmación. `POST /update` hace `git reset --hard` sobre el repositorio que contiene `src/configs/` (`backend.js:9556`): actualizar el software destruye caps, hops, wallet y cuentas del Multiverse. Y la red no se mide en el tiempo: `stats_model.js` conoce su disco (L438) y sus pares (L24), no su uptime. Un sistema que recurre por reloj pero no sabe cuánto lleva vivo no puede saber si es eutáxico. De aquí salen EU-2, EU-3, EU-4 y EU-6.

### B. Holización: un feed es un átomo

Para Bueno (K7, B, **[doctrina, sin verbatim]**) la democracia exige holizar: descomponer la sociedad en partes homogéneas e intercambiables, los ciudadanos, para poder contarlos. Oasis holiza con el log: un inhabitant es un autor con mensajes no tombstone (`inhabitants_model.js:87`), la población que fija el quórum es ese censo (`parliament_model.js:244`, `:1191`), la mayoría es `floor(total / 2) + 1` (`parliament_view.js:21`) y cada consulta cuenta un voto por `v.author` (`polls_model.js:99`). El átomo es la clave ed25519 que ha publicado. No hay persona, hogar ni edad: hay feeds.

Esto tiene dos consecuencias que la doctrina permite ver. Primera: el demos se define por haber hablado, no por pertenecer; quien calla seis meses cae al cubo `red` (`inhabitants_model.js:65-73`) pero sigue contando en el censo mientras tenga un mensaje. Segunda: la unidad de cuenta es técnica, no jurídica; nada impide a una persona ser dos feeds, ni a un feed ser una IA (§2.8). La holización de Oasis es perfecta como aritmética y vacía como antropología. Material para D03.

### C. El karma como cierre categorial fallido

El karma quiere ser la categoría que concatena todas las demás: se calcula desde acciones sociales (`scoreFromActions`, `banking_model.js:838`), decide empates electorales (`parliament_model.js:422-423`), ordena propuestas (`:576`), funda un régimen (`KARMATOCRACY`, `:23`, `:650`), una forma de justicia (`courts_model.js:139`), el peso de la renta (`banking_model.js:932`) y las sugerencias de contacto (`inhabitants_model.js:217`). Un cierre categorial (K2, A) exigiría que esas operaciones fueran propias de un campo y volvieran sobre sus términos. El karma no cierra nada: para constituirse tiene que salir de su campo y restar gramos de CO₂ (`banking_model.js:840`, `:1151`), es decir, tiene que reducir M3 a M1. Y esa resta se apoya en una constante, `0.095` gramos por MiB (`:35`), sin procedencia.

El resultado es doble. Contra K1: la única *symploké* que la red ejecuta es una identificación, no una articulación; no es materialismo, es fisicalismo. Contra K7: el karma reintroduce partes heterogéneas (notorio / silencioso, ligero / pesado) en un demos que el log había hecho homogéneo, y lo hace por debajo de la forma democrática, en el desempate y en el orden de la lista. Bueno diría (C) que una democracia que se holiza por el log y se re-estratifica por el karma es una democracia con una aristocracia no declarada. De aquí sale EU-5 y el carril T06-T07.

### D. Las nueve ramas: poderes sin ramas

| Capa | Rama | Módulo / costura | Estado | Quién la controla |
| :-- | :-- | :-- | :-- | :-- |
| Conjuntiva | Legislativa | `parliament_model.js:17-27`, `canPropose` `:1298-1311`, `enactApprovedChanges` `:1102` | **Implementada** | Voto del censo / titular del mandato |
| Conjuntiva | Judicial | `courts_model.js:139`, `:363-368` | **Implementada**; **fusionada** con la legislativa bajo `DICTATORSHIP` (`:142-151`) | Juez, mediadores, voto público o dictador |
| Conjuntiva | Ejecutiva | ninguna: `enactApprovedChanges` publica mensajes (`parliament_model.js:1102`, `:1167`) y nadie fuera de la interfaz obedece | **Ausente** | Nadie |
| Basal | Planificadora | `industry_model.js:164`, `:457`, `:484`, `SUBJECTS` `:532` | **Implementada** | `steward` único = autor del mensaje raíz |
| Basal | Redistribuidora | `banking_model.js:14-21`, `:913-917`, `:920-941`; motor `backend.js:10265-10273` | **Implementada y autónoma** | Nodo autodeclarado PUB (`banking_model.js:214-217`); constantes sin voto |
| Basal | Gestora | `wallet_model.js:22-23` (RPC), `banking_model.js:1004` (`sendtoaddress`) | **Dependiente** de una cartera externa | Autor del feed; operador de la cartera |
| Cortical | Militar (defensa) | `crypto.js:146`, `:319-320`; `caps.shs` `server-config.json:6`; `hops` `:12`; block `backend.js:7306-7307`; pánico `panicmode_model.js:6-10` | Existe como **técnica**, no como poder | Operador del nodo (fichero, loopback); cada feed para el block |
| Cortical | Diplomática | `backend.js:4651`, `:4663` sin `isLoopbackRequest` (`:170`); `fediverse_model.js:5` | Existe, **sin órgano** | Operador del nodo; cualquier petición que alcance el puerto |
| Cortical | Federativa | `oasis-pub.js:40-41`; `ssb-invite` si `config.pub` (`SSB_server.js:70`); `autofollow` (`server-config.json:25-27`, `SSB_server.js:88-93`); `parentTribeId` (`tribes_model.js:341`) | Existe, **sin órgano** | Quien tiene shell en el PUB; el proyecto upstream |

**Hallazgo estructural.** Oasis politiza la capa conjuntiva (dos ramas de tres) y da forma personal o automática a la basal. Toda la capa cortical, y los parámetros constitutivos de la basal (constantes de carbono y de RBU, `walletPub`, `hops`, `caps`), están en manos del operador del nodo. En términos de Bueno (K5, B): la red tiene poderes sin ramas. Esta tabla es el producto b1 en bruto; T01 la pasa a limpio con columna de certeza.

### E. El operador como poder exterior al cuerpo político

El operador no vota, no es elegido, no aparece en el censo como tal, y sin embargo decide: el `caps.shs` que separa esta red de cualquier otra (`server-config.json:6`), los `hops` que fijan el horizonte de replicación (`:12`), el `autofollow` que forma el círculo inicial (`:25-27`), el `walletPub.pubId` que lo convierte en redistribuidor (`banking_model.js:215-217`), los invites que federan (`oasis-pub.js:40-41`), y con `POST /update` reescribe todo eso desde el repositorio remoto (`backend.js:9556`). Las rutas que exigen `isLoopbackRequest` (`backend.js:170`, `:9553`) reconocen implícitamente que hay un sujeto distinto del usuario: el que está sentado en la máquina.

Bueno (C, **[doctrina, sin verbatim]**, a verificar en D07) no tiene, que sepamos, una figura para «el que sostiene la institución sin ser parte de ella». La lectura que proponemos: el operador es el resto no holizado del cuerpo político, la parte que la forma democrática no puede contar porque no es un feed sino una máquina y un fichero. De aquí sale EU-1: no eliminar al operador, sino darle rama, es decir, que sus decisiones corticales pasen por el log.

### F. El eje angular, poblado y sin gobernar

Oasis tiene tres habitantes no humanos con capacidad de escribir o de ordenar el tiempo: la IA 42, que narra las acciones del usuario y publica hasta 40 mensajes `log` por clic (`logs_model.js:235-263`) desde un proceso en `localhost:4001` sin autenticación (`ai_service.mjs:89`); el calendario de nueve casas con año 10.000.000 (`larp_model.js:9`, `:139`, `:149`); y la esteganografía de `melody_model.js:124-141`, que abre un canal para quien sepa leerlo. El único gobierno del eje es un formulario individual, `POST /ai/approve` (`AI_view.js:61`), que no deja registro de la decisión y no cubre ni al calendario ni al canal oculto.

Con la cautela de K3 (angular→máquinas es C): si se acepta la extensión, Oasis es una sociedad con númenes activos y sin culto reglado; si no se acepta, sigue siendo cierto que hay un sujeto no humano escribiendo en el feed y que ninguna rama lo controla. D04 decide la doctrina; T03 documenta el hecho en cualquier caso.

### G. Cierres: lo cerrado es de otros, lo propio está abierto

Las dos categorías cerradas de Oasis, criptografía (`SSB_server.js:56`, `crypto.js:146`) y replicación (`SSB_server.js:60-61`), son ciencia importada, parametrizada por fichero (`server-config.json:6`, `:12`) y nunca reabierta por el código propio. Lo que Oasis añade (gobernanza, banca, IA) está abierto: la gobernanza cierra en el log y no en la ejecución (`tombstone_validator.js:12`, `:26`; `parliament_model.js:1102`), la banca depende de una wallet por RPC (`wallet_model.js:22-23`) y la IA se defiende con una regex (`ai_service.mjs:52`). En términos de K2 (A): Oasis es una técnica (categoría del hacer) montada sobre dos ciencias ajenas; no hay cierre propio de la «gobernanza digital», y la pregunta de si puede haberlo (D05) es la única pregunta gnoseológica de este nodo.

---

## 4. Especificación EU-OASIS: parches de eutaxia

Bueno no licencia prescribir un régimen; licencia una sola cosa: aumentar la capacidad de la sociedad política para persistir. Cada parche repara una coordenada de K6 y, de paso, cierra un hueco de K5 o K1. Se documentan; no se implementan en este nodo.

| # | Cambio | Punto de intervención | Coordenada que repara |
| :-- | :-- | :-- | :-- |
| **EU-1** | **Órgano para la capa cortical.** Las decisiones del operador que afectan a la frontera de la red (conectar o desconectar el Multiverse, crear invites del PUB, cambiar `hops` y `autofollow`) se publican como mensajes `corticalRule` en el log, con firma del operador y, si hay gobierno, del titular del mandato; `POST /settings/fediverse` y `/disconnect` exigen `isLoopbackRequest` y publican el hecho | `backend.js:4651`, `:4663`, `:170`; `oasis-pub.js:40-41`; `server-config.json:12`, `:25-27` | K5 (militar, diplomática, federativa: de poder a rama), K6 |
| **EU-2** | **Respaldo real de la identidad.** El export incluye `secret` cifrado con passphrase; el paso `backup` del onboarding solo se marca cuando existe un export verificado | `exportmode_model.js:25-26`; `onboarding_model.js:5`, `:116`, `:123-125` | K6.b (muerte de identidad por accidente) |
| **EU-3** | **Actualización sin destruir la configuración.** `POST /update` mueve `src/configs/*.json` fuera del árbol de git o los restaura tras el `pull`; token CSRF además del loopback | `backend.js:9552-9556` | K6.b (destrucción de config al actualizar) |
| **EU-4** | **Medida del tiempo.** `stats` publica uptime del proceso, edad del feed más antiguo, número de legislaturas transcurridas desde `TERM_EPOCH` y cuántas fueron `ANARCHY` virtual | `stats_model.js:24`, `:438`; `parliament_model.js:25-26`, `:373` | K6.a (la red se mide en el tiempo; la eutaxia se vuelve observable) |
| **EU-5** | **Parámetros basales con procedencia.** `carbonGramsFromBytes`, `ECOIN_PER_GRAM_CO2` y `DEFAULT_RULES` pasan a un mensaje `basalRule` con fuente y fecha, modificable por el parlamento con el quórum general; el karma deja de restar gramos y el carbono se cobra como tasa aparte, sin tocar el peso político | `banking_model.js:14-21`, `:31-37`, `:840`, `:1151`, `:932` | K1.b (fin de la reducción M3→M1), K5 (redistribuidora con sujeto), K7.b |
| **EU-6** | **Confirmación en dos pasos para el pánico.** Token de un solo uso y ventana de 60 s entre `POST /panic` y `removeSSB`; el export con `secret` (EU-2) se ofrece antes | `backend.js:8054-8057`; `panicmode_model.js:6-10` | K6.b (irreversibilidad sin fricción) |
| **EU-7** | **Registro del eje angular.** Cada aprobación en `/ai/approve` se publica como `aiApproval` con el hash de lo aprobado; el servicio de `4001` exige un token local; el calendario de casas se declara en un mensaje `larpCalendar` en lugar de constantes | `AI_view.js:61`; `ai_service.mjs:89`, `:52`; `larp_model.js:9`, `:139` | K3.c (eje angular gobernado), K2.b (cierre mínimo de la IA) |

**Lo que no se toca, y por qué.** El calendario fijo desde `TERM_EPOCH` y la anarquía virtual (`parliament_model.js:25-26`, `:373-380`): son la eutaxia que ya existe, recurrencia sin convocante. La rotación de claves de tribu (`tribes_model.js:753-760`): una frontera que se repara sola. La holización por el log (`inhabitants_model.js:87`; `polls_model.js:99`): Bueno no pide otra unidad de cuenta, pide saber cuál es. Los cierres importados (`SSB_server.js:56`, `:60-61`): no se reabre lo que está cerrado. Y el catálogo `METHODS` (`parliament_model.js:23`), incluida `KARMATOCRACY`: la democracia es una forma entre otras (K7), y este nodo no la privilegia; solo exige que la forma que rija sea la declarada, sin re-estratificación oculta (EU-5).

---

## 5. Backlog v0

Leyenda: T = tamaño (S/M/L) · P = prioridad (C crítica, H alta, M media). Cada tarea D tiene **camino por defecto**: si no se investiga, el carril siguiente usa el default; si se investiga y la respuesta difiere, la tarea dice qué cambia aguas abajo. Mapa de carriles: **D → T → EU**.

### Carril D · Investigación en fuentes de Bueno

| ID | Buscar | Dónde | Default | Alternativas | Desbloquea |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-D01 | **Nombres exactos y definición de las nueve ramas**; si «ejecutiva» es rama o poder; si la gestora es «gestora» o «económica» | *Primer ensayo sobre las categorías de las ciencias políticas* (1991) | Tabla §3.D tal cual (K5 en B) | otra partición de la basal; ramas no exhaustivas | TK-T01, TK-EU01 |
| TK-D02 | **Definición de eutaxia**: ¿duración, recurrencia, prudencia? ¿Es medible? ¿Distingue Bueno eutaxia de estabilidad? | *Primer ensayo…* | Eutaxia = capacidad de recurrencia; indicadores de §2.9 y §3.A; el automatismo del PUB cuenta como eutaxia | eutaxia exige prudencia de un sujeto (el automatismo no cuenta); eutaxia no medible | TK-T05, TK-EU04, TK-EU02 |
| TK-D03 | **Holización** y democracia como forma; qué diría Bueno de un demos definido por haber publicado | *El fundamentalismo democrático* (2010), *Panfleto contra la democracia realmente existente* (2004) | Holización por el log; karma como des-holización; una persona = una clave es holización técnica, no jurídica | Bueno exige holización jurídica (persona, no clave); la re-estratificación es inevitable y no crítica | TK-T06, TK-EU05 |
| TK-D04 | **Eje angular**: ¿admite Bueno sujetos no humanos artificiales? ¿Es la IA númen o instrumento? | *El animal divino* (1985), *Ensayos materialistas* (1972) | IA 42, calendario y esteganografía en el eje angular, marcados C | IA como instrumento (eje radial); solo el calendario es angular | TK-T03, TK-EU07 |
| TK-D05 | ¿Es la «gobernanza digital» una categoría del hacer con cierre posible, o una ideología? ¿Qué es una técnica sobre dos ciencias ajenas? | *TCC* (1992-93), *¿Qué es la ciencia?* (1995) | Técnica sin cierre; solo criptografía y replicación cerradas | cierre posible como categoría del hacer; toda la red es ideología | TK-T02 |
| TK-D06 | Capa **cortical**, imperio generador / depredador: ¿aplica a puentes con otras redes (Mastodon, Telegram)? | *España frente a Europa* (1999), *Primer ensayo…* | Los puentes son diplomacia sin órgano; no se abre la cuestión imperial | los puentes son absorción (imperio depredador de la red mayor) | TK-T04, TK-EU01 |
| TK-D07 | Qué dice Bueno del **operador** de una institución (quien sostiene la basal sin ser parte formal); ¿hay figura para el resto no holizado? | *Primer ensayo…*; *El fundamentalismo democrático* | El operador es poder exterior al cuerpo político (C) | el operador es parte de la basal; el operador es la clase política real | TK-T01, TK-EU01 |
| TK-D08 | Rastreo de divulgación y contraste con los libros: fgbueno.es, *El Catoblepas*, Symploké; localizar verbatim para K4-K7 | web | ninguno: cada K4-K7 conserva B hasta el verbatim | ascenso a A de las coordenadas con verbatim | todas D |

### OP-01 · Trituración por coordenada (carril T)

Documentos de revisión, uno por concepto, con el formato de ficha (tesis, certeza, mapeado/acierto/hueco/contradicción, veredicto). Producen `revision/01-…06-…`.

| ID | Tarea | Depende | Seam | T | P |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-T01 | Nueve ramas en limpio (b1 = `draftv1`): una fila por rama, columna de certeza de la rama y de la lectura, «quién controla» verificado | D01, D07 | `parliament_model.js:1102`, `:1298`; `courts_model.js:139`; `industry_model.js:164`; `banking_model.js:214`; `backend.js:4651`, `:10265`; `oasis-pub.js:40-41` | M | **C** |
| TK-T02 | Cierres: ficha por capa (cripto, replicación, gobernanza, banca, IA) con veredicto cerrada / abierta / dependiente | D05 | `SSB_server.js:56`, `:60-61`; `tombstone_validator.js:12`, `:26`; `wallet_model.js:22-23`; `ai_service.mjs:52`, `:89` | M | H |
| TK-T03 | Espacio antropológico: radial, circular, angular con las tres piezas del angular y su (no) gobierno | D04 | `stats_model.js:24`; `backend.js:7306-7307`; `logs_model.js:235-263`; `larp_model.js:9`, `:139`; `melody_model.js:124`; `AI_view.js:61` | M | H |
| TK-T04 | Capa cortical completa: Multiverse, PUB, hops, caps, autofollow, pánico, update; inventario de lo que decide el operador | D06, D07 | `backend.js:4651`, `:4663`, `:9556`, `:8054-8057`; `server-config.json:6`, `:12`, `:25-27`; `SSB_server.js:70`, `:88-93` | M | H |
| TK-T05 | Eutaxia con indicadores: tabla mecanismo / seam / eutaxia o distaxia, base de EU-2…EU-6 | D02 | `parliament_model.js:25-26`, `:373-380`; `tribes_model.js:753-760`; `exportmode_model.js:25-26`; `onboarding_model.js:116`; `backend.js:9556`; `stats_model.js:438` | M | **C** |
| TK-T06 | Holización y karma: dónde holiza el log, dónde des-holiza el karma; la clave como unidad de cuenta | D03 | `inhabitants_model.js:87`, `:217-220`; `parliament_model.js:244`, `:422-423`, `:576`, `:650`; `parliament_view.js:21`; `polls_model.js:99` | M | H |
| TK-T07 | Materialidades y la reducción M3→M1: inventario M1/M2/M3 por módulo (§2) y las dos restas del karma | — | `banking_model.js:35`, `:609-617`, `:838-840`, `:1151`; `opinions_model.js:59`; `settings_view.js:24`; `typed_log.js:77` | S | H |

### OP-02 · Parches de eutaxia (carril EU)

Especificación de cada EU-n como tarea documental: qué cambia, qué invariante conserva, cómo se verifica. Default del plan: **se documenta, no se implementa**.

| ID | Tarea | Depende | Seam | T | P |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-EU01 | EU-1: `corticalRule` en el log para Multiverse, invites, hops y autofollow; loopback en `/settings/fediverse*` | D01, D06, D07, T04 | `backend.js:4651`, `:4663`, `:170`; `oasis-pub.js:40-41`; `server-config.json:12`, `:25-27` | L | **C** |
| TK-EU02 | EU-2: export con `secret` cifrado por passphrase; `backup` verificado | D02, T05 | `exportmode_model.js:25-26`; `onboarding_model.js:5`, `:116`, `:123-125` | M | **C** |
| TK-EU03 | EU-3: `/update` sin `git reset --hard` sobre `src/configs/`; CSRF | T05 | `backend.js:9552-9556` | S | H |
| TK-EU04 | EU-4: uptime, edad del feed, legislaturas transcurridas y anárquicas en `stats` | D02, T05 | `stats_model.js:24`, `:438`; `parliament_model.js:25-26`, `:373` | M | H |
| TK-EU05 | EU-5: `basalRule` con procedencia; karma sin resta de gramos; carbono como tasa aparte | D03, T06, T07 | `banking_model.js:14-21`, `:31-37`, `:840`, `:1151`, `:932` | M | H |
| TK-EU06 | EU-6: dos pasos para el pánico con export previo | T05, EU02 | `backend.js:8054-8057`; `panicmode_model.js:6-10` | S | M |
| TK-EU07 | EU-7: `aiApproval` registrado, token local en `4001`, `larpCalendar` como mensaje | D04, T03 | `AI_view.js:61`; `ai_service.mjs:52`, `:89`; `larp_model.js:9`, `:139` | M | M |

### OP-03 · Verificación y fichas

| ID | Tarea | Depende | Seam | T | P |
| :-- | :-- | :-- | :-- | :-- | :-- |
| TK-V01 | Script de lectura: cada `fichero:línea` de `modelos/clase/*.md` existe en `vendor/oasis` y la línea contiene el símbolo nombrado | — | todos | S | H |
| TK-V02 | Fichas `revision/01-materialidades.md` … `06-holizacion-democracia.md` con el formato de ficha; cada K con al menos un hueco o un «sin hueco» | T01-T07 | — | L | H |
| TK-V03 | Notas al margen (2026-09-09) en `draft.md` con las dos correcciones de línea de §0.5 (`steward` :164/:457, `box` :320) | — | `industry_model.js:164`, `:457`; `crypto.js:320` | S | M |

### Resumen de prioridades v0

| Prioridad | Tareas |
| :-- | :-- |
| **Crítica** | TK-T01, TK-T05, TK-EU01, TK-EU02 |
| **Alta** | TK-T02, TK-T03, TK-T04, TK-T06, TK-T07, TK-EU03, TK-EU04, TK-EU05, TK-V01, TK-V02 |
| **Media** | TK-EU06, TK-EU07, TK-V03 |

El carril D no lleva prioridad propia: cada D tiene default y solo bloquea el ascenso de certeza. Decisión pendiente para el usuario (heredada del plan): si el carril EU se queda en documentación o se abre a tareas de código. Default: documentación.

---

## 6. Fuentes

**Código auditado (disco):** `vendor/oasis` @ `9a657b776fcafc7c24bf3ad61825316385ecf513` (release 1.0.7, 2026-09-08). Clonado con `git clone --depth 1 https://github.com/epsylon/oasis.git`. Versión y licencia en `src/server/package.json`.

**Fuente primaria del proyecto:** `README.md` de Oasis («No browser JavaScript. Just pure HTML+CSS»), no verificada de forma independiente.

**Doctrina:** `draft.md` §Panorámica y §1 (chuletario corregido). Obras: *Ensayos materialistas* (1972), *El animal divino* (1985), *Primer ensayo sobre las categorías de las ciencias políticas* (1991), *Teoría del cierre categorial* (1992-93), *¿Qué es la ciencia?* (1995), *España frente a Europa* (1999), *Panfleto contra la democracia realmente existente* (2004), *El fundamentalismo democrático* (2010). Sin páginas: todo lo doctrinal es **[doctrina, sin verbatim]** con grado A/B/C hasta que el carril D lo verifique.

**Grado de certeza.** Cuatro niveles: *verificado en código con fichero y línea* (todo §1.1-1.2, §2 y §3, con `sed -n` sobre el commit) · *fuente primaria del proyecto, no verificada de forma independiente* (README de Oasis) · *inferido de la actividad del repositorio* (ninguno en este draft: Faircoin no se usa) · *paráfrasis marcada, no cita* (coordenadas K1-K7 con A/B/C; las lecturas del operador y del eje angular como extensiones C).
