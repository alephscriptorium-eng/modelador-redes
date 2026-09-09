# Teoría Pura de la República · Modelización sobre SolarNET.HuB / OASIS

**Revisión 2 — 2026-09-09.** La v1 de este documento (backlog Scrum SNH + Faircoin) se conserva íntegra en la §7. Esta revisión la corrige y la amplía tras auditar el código real.

---

## 0. Qué cambia respecto de la v1

| # | Hallazgo | Consecuencia |
| :-- | :-- | :-- |
| 1 | **Oasis ya no es un cliente de SSB: es un Estado completo en software.** Implementa Parlamento, Tribunales, Banca central con RBU, Industria, Escuela y una capa de rol (L.A.R.P.) con 9 casas. | La v1 pedía *diseñar* la gobernanza (TK-05, TK-13…). Ya está diseñada, y con decisiones tomadas. La tarea real es **auditarla y bifurcarla**, no inventarla. |
| 2 | **La capa Faircoin está muerta.** El repositorio `faircoin/faircoin` no recibe un commit desde el **2022-02-05**: cuatro años y medio de silencio. | OP-02 entera (TK-07…TK-12) queda inoperativa. La sustituye **ECOin** + el módulo `Banking` nativo. |
| 3 | **Karma es a la vez peso político y peso económico.** El mismo escalar desempata elecciones, decide leyes bajo KARMATOCRACY y pondera el reparto de la Renta Básica. | Es el hallazgo estructural más grave del informe: una fusión de poderes que ninguna separación posterior puede reparar. Ver §3.C. |
| 4 | El modelo trevijanista y el modelo Oasis **coinciden en un punto inesperado**: la ausencia de gobierno es el estado por defecto y se calcula, no se decide. | Ver §3.F — la anarquía virtual como período constituyente permanente. |

**Metodología.** Todo lo que aquí se afirma sobre Oasis está verificado contra el código fuente, no contra su documentación ni su propaganda. El árbol auditado está en `base/teoria/vendor/oasis` (ignorado por git; clónalo con `git clone --depth 1 https://github.com/epsylon/oasis.git`). Commit auditado: **`9a657b7`, "Oasis release 1.0.7", 2026-09-08**. Cuando cito la web y no el disco, lo digo. Cuando afirmo doctrina trevijanista sin cita literal, lo marco como **[doctrina, sin verbatim]**.

---

## 1. Estado del arte verificado

### 1.1 OASIS 1.0.7

- Paquete `@krakenslab/oasis` v1.0.7, licencia **AGPL-3.0**, autor `psy <epsylon@riseup.net>`, espejo en `code.03c8.net`.
- Node.js + HTML5 + CSS. **Cero JavaScript en el navegador**: toda interacción es `<form>` y POST. Consecuencia política, no estética: no hay superficie para telemetría de cliente ni para lógica oculta al usuario.
- Frontend `hyperaxe` (constructores de DOM en servidor), Koa + Express, `ssb-*` clásico, `epidemic-broadcast-trees` para el gossip.
- **~70 modelos y ~68 vistas** en [src/models/](base/teoria/vendor/oasis/src/models/) y [src/views/](base/teoria/vendor/oasis/src/views/). La lista de módulos del README es fiel al árbol.
- Novedades recientes relevantes: `Industry` (medios de producción colectivos), `School` (certificados), `Multiverse` (puentes a Mastodon y Telegram sin escribir contenido de terceros en el log SSB), IA local "42" vía `node-llama-cpp` + `@xenova/transformers`, y huella de carbono medida por inhabitante.
- 19 estrellas en GitHub. Esto no es una red social: es una **maqueta institucional a escala 1:1** con una población del tamaño de una asamblea de barrio. Conviene tenerlo presente antes de extraer conclusiones sobre "democracia digital".

### 1.2 La capa económica: acta de defunción de Faircoin

La v1 apostaba el eje económico entero a Faircoin. Estado real, verificado vía API de GitHub el 2026-09-09:

- `faircoin/faircoin`: último push **2022-02-05**. Sin archivar, sin mantener. Los últimos commits son documentación del *Fasito* (el token de firma de los CVN) y actas de una reunión de febrero de 2022.
- El white paper y las FAQ siguen en línea y siguen sin fecha: la última referencia temporal del FAQ es *"in 2021 the governance is being transferred to the fair ecosystem group"*. No hay comunicado de cierre. Tampoco hay señales de vida.
- Sobre la disolución formal de FairCoop no encuentro fuente concluyente; la literatura académica de 2023-2025 lo sigue tratando en presente. **Probabilidad alta de proyecto de facto abandonado, certeza baja sobre su estatus jurídico.** No lo afirmo: lo dejo como está para que se valide por cuenta propia.

Lo que sí está vivo, y es lo que Oasis usa de verdad:

- **ECOin** (`ecoin.03c8.net`), lanzada en 2014, **v0.0.4 de febrero de 2026**. Consenso híbrido: PoW (scrypt, halving cada 262.800 bloques) + PoS (interés por antigüedad de moneda) + **PoT (Proof-of-Transaction**: transacciones de más de 500 ECO capturan el 50% del subsidio de bloque por emparejamiento de hash). Coinbase estimado ~225 M ECO. Wallet Android v0.7.5.7.
- El módulo **`Banking`** ([banking_model.js](base/teoria/vendor/oasis/src/models/banking_model.js)), que no es un puente a un banco: **es el banco**. Calcula el valor de ECOin, mantiene un tesoro común y reparte una Renta Básica por épocas.

> Nota fría sobre PoT: premiar con la mitad del subsidio de bloque a quien mueve más de 500 ECO es, textualmente, un mecanismo de concentración. Es la única pieza del ecosistema cuyo diseño incentiva la acumulación. En un modelo que se reclama republicano conviene tenerla fichada.

### 1.3 El corpus trevijanista (recordatorio operativo)

Antonio García-Trevijano (1927-2018), fundador y presidente del **MCRC** (Movimiento de Ciudadanos hacia la República Constitucional, **2006**), asociación civil, prepolítica, que no concurre a elecciones y que se define como disoluble el día en que se abra la libertad constitucional. Obra de referencia: *Teoría Pura de la República* en tres volúmenes (*Sentido de la Revolución Francesa*, *El factor republicano*, *Teoría pura de la República Constitucional*) y *Teoría pura de la democracia*.

Núcleo doctrinal utilizable como criterio de auditoría **[doctrina, sin verbatim]**:

1. **Democracia formal, no material.** La democracia es un *procedimiento* de constitución del poder, no un contenido ni un programa. Un sistema es democrático por cómo se origina el poder, no por lo que hace con él.
2. **Separación de poderes en el origen.** No basta que legislativo y ejecutivo se controlen: deben **nacer de elecciones distintas**. Si una sola votación produce ambos, no hay separación, hay reparto.
3. **Representación auténtica.** Distrito uninominal, candidatura personal, responsabilidad personal ante el elector. La lista de partido rompe el vínculo representativo: el diputado responde ante quien lo colocó en la lista, no ante quien lo votó.
4. **Estado de partidos ≠ Estado de derecho.** La partitocracia es un régimen oligárquico que se legitima por sufragio pero no representa.
5. **Libertad política colectiva** como bien distinto de las libertades individuales. Se puede ser individualmente libre en un pueblo políticamente esclavo.
6. **La República es forma de Estado, no ideología.** No es de izquierdas ni de derechas; es la alternativa a la monarquía y a la partitocracia.
7. **Libertad constituyente primero, Constitución después.** Sin un período de libertad constituyente previo, toda constitución es un pacto entre poderes constituidos.

Con estos siete criterios se puede auditar cualquier institución. Los aplico al código en la §3.

---

## 2. Anatomía institucional de OASIS (lo que el código hace de verdad)

### 2.1 Parliament — [parliament_model.js](base/teoria/vendor/oasis/src/models/parliament_model.js) · 1.615 líneas

**Constantes constitucionales** ([líneas 17-26](base/teoria/vendor/oasis/src/models/parliament_model.js#L17-L26)):

```
TERM_DAYS       = 60      // mandato
PROPOSAL_DAYS   = 7       // vida de una proposición
REVOCATION_DAYS = 15      // vida de una revocación
PROPOSAL_QUORUM = 2       // suelo absoluto de quórum
QUORUM_RATIO    = 0.25    // 25% del censo
TERM_EPOCH      = 2020-01-01T00:00:00Z
```

Los mandatos **no empiezan cuando alguien gana**: se derivan de una época fija por aritmética modular (`termWindowFor`, [L28-38](base/teoria/vendor/oasis/src/models/parliament_model.js#L28-L38)). Toda la red comparte el mismo calendario de ciclos de 60 días desde el 1 de enero de 2020, sin coordinación ni autoridad. Es un calendario litúrgico calculado. Elegante y, políticamente, importante: **nadie puede convocar ni aplazar elecciones**.

**Métodos de gobierno** ([L22-23](base/teoria/vendor/oasis/src/models/parliament_model.js#L22-L23)): `DEMOCRACY`, `MAJORITY`, `MINORITY`, `DICTATORSHIP`, `KARMATOCRACY`, más `ANARCHY` como estado por defecto. El método **no lo elige la red: lo elige el candidato al presentarse**. Se vota una persona *y su forma de Estado* en la misma papeleta.

**Umbrales** ([L240-242](base/teoria/vendor/oasis/src/models/parliament_model.js#L240-L242)):

| Método | Umbral de aprobación | Lectura |
| :-- | :-- | :-- |
| DEMOCRACY / ANARCHY | `floor(total/2)+1` | mayoría simple de votantes |
| MAJORITY | `ceil(total*0.8)` | supermayoría del 80% |
| MINORITY | `ceil(total*0.2)` | **el 20% legisla** |
| DICTATORSHIP | — | no se abre votación: aprobado al vencer el plazo |
| KARMATOCRACY | — | gana la propuesta del proponente con más karma; el resto, `REJECTED` |

Quórum: `max(2, ceil(censo * 0.25))`, donde el censo son todos los inhabitants con actividad ([L257-260](base/teoria/vendor/oasis/src/models/parliament_model.js#L257-L260)).

**Elecciones.** Cualquiera propone hasta 3 candidaturas por ciclo; cada inhabitant emite **un único voto por ciclo** entre todas las candidaturas abiertas ([L744-761](base/teoria/vendor/oasis/src/models/parliament_model.js#L744-L761)); no se puede votar a uno mismo. El candidato puede ser **un inhabitant o una tribu**.

Cascada de desempate ([L408-437](base/teoria/vendor/oasis/src/models/parliament_model.js#L408-L437)): votos → **karma** → antigüedad del perfil → primera candidatura publicada → orden lexicográfico del feed ID. Determinista y auditable; también, en su segundo escalón, censitaria.

**Quién legisla** (`canPropose`, [L1298](base/teoria/vendor/oasis/src/models/parliament_model.js#L1298)): bajo ANARCHY, todos. Con gobierno de inhabitant, **solo él**. Con gobierno de tribu, **cualquier miembro de la tribu**. El resto del censo no tiene iniciativa legislativa: solo vota lo que el poder propone (y ni eso bajo DICTATORSHIP o KARMATOCRACY).

**Ciclo de vida de una ley.** Proposición (`parliamentProposal`, 7 días, máx. 3 por mandato y persona) → votación asociada (`votes`) → `APPROVED`/`REJECTED` → y aquí lo notable: **la ley no nace hasta que el gobierno muere**. `enactApprovedChanges` ([L1102](base/teoria/vendor/oasis/src/models/parliament_model.js#L1102)) se ejecuta al detectar el mandato expirado, revalida el umbral y solo entonces publica el `parliamentLaw`. El gobierno saliente legisla en el acto de expirar.

**Revocación** (`parliamentRevocation`, 15 días): revoca **leyes**, no mandatos. No existe revocatoria del cargo. Y su ejecución es un `tombstone` sobre el mensaje de la ley ([L1145-1147](base/teoria/vendor/oasis/src/models/parliament_model.js#L1145-L1147)) — es decir, la ley derogada **desaparece de la interfaz**. Matiz técnico que importa: SSB es un log de solo-anexado, el mensaje original sigue existiendo en cada réplica; el tombstone es una convención de cliente (`buildValidatedTombstoneSet`). La memoria no se destruye: se deja de mostrar. La distinción entre "derogar" y "hacer invisible" queda, hoy, del lado del cliente.

**Parlamento de segundo nivel.** Cada tribu tiene su propio ciclo de 60 días (`tribeParliamentTerm`, `tribeParliamentCandidature`, `tribeParliamentRule`, [L1354-1445](base/teoria/vendor/oasis/src/models/parliament_model.js#L1354-L1445)), con quórum `max(2, ceil(miembros*0.25))` y ANARCHY por defecto. Federalismo real: hay tantos parlamentos como tribus, más uno general.

### 2.2 Courts — [courts_model.js](base/teoria/vendor/oasis/src/models/courts_model.js) · 961 líneas

Plazos procesales fijos: **contestación 7 días, prueba 14, resolución 21**; voto popular 14 ([L8-11](base/teoria/vendor/oasis/src/models/courts_model.js#L8-L11)).

Cinco métodos de resolución ([L139](base/teoria/vendor/oasis/src/models/courts_model.js#L139)): `JUDGE`, `MEDIATION`, `POPULAR`, `KARMATOCRACY`, `DICTATOR`.

- **Jueces electos**: `courtsNomination` + `courtsNominationVote`. La judicatura se provee por elección, no por nombramiento — aunque el orden de las candidaturas se resuelve por apoyos y, en empate, por **karma** ([L805](base/teoria/vendor/oasis/src/models/courts_model.js#L805)).
- `POPULAR` y `KARMATOCRACY` se resuelven ambos por **votación pública de 14 días** ([L368](base/teoria/vendor/oasis/src/models/courts_model.js#L368), [L694](base/teoria/vendor/oasis/src/models/courts_model.js#L694)); en Tribunales, a diferencia del Parlamento, el karma no dicta sentencia.
- **`DICTATOR` exige que el gobierno vigente sea `DICTATORSHIP`** y asigna como juez al inhabitant que gobierna ([L140-155](base/teoria/vendor/oasis/src/models/courts_model.js#L140-L155)). El código lo verifica explícitamente contra `parliament.getGovernmentCard()`. Es decir: **la fusión de poderes está implementada como una comprobación de integridad**. No es un fallo; es una función.
- **Instrucción cifrada por defecto**: título, acusador, acusado y mediadores viajan cifrados campo a campo con una clave por caso, distribuida solo al demandado (y al dictador, si lo hay). La publicidad del proceso es opt-in (`courtsVisibility`, `setPublicPreference`).
- Una parte no puede dictar veredicto sobre su propio caso; la validez del veredicto se comprueba contra el método (`verdictValid`, [L361-366](base/teoria/vendor/oasis/src/models/courts_model.js#L361-L366)).

### 2.3 Banking, karma y ECOin — [banking_model.js](base/teoria/vendor/oasis/src/models/banking_model.js) · 1.479 líneas

**Reglas de la Renta Básica** ([L14-21](base/teoria/vendor/oasis/src/models/banking_model.js#L14-L21)): épocas mensuales, `alpha 0.2`, reserva mínima 500, tope por época 2.000, tope por usuario y época 50, suelo por usuario 1, pesos acotados entre 0,2 y 6, gracia de 30 días. El reparto es **ponderado por karma** dentro de esos topes.

**Cómo se calcula el karma** (`scoreFromActions`, [L525-607](base/teoria/vendor/oasis/src/models/banking_model.js#L525-L607)). Es un baremo de puntos por acto publicado, con decaimiento temporal (×1 hasta 30 días, ×0,5 hasta 90, ×0,25 después). Extracto significativo:

| Acto | Puntos | Acto | Puntos |
| :-- | --: | :-- | --: |
| `parliamentTerm` (ganar el gobierno) | **25** | `larpJoinHouse` | 15 |
| `parliamentLaw` | 16 | `video` | 12 |
| `parliamentCandidature` | 12 | `schoolCertificate` | 12 |
| `courtsVerdict` | 10 | `post` | 10 |
| `parliamentRevocation` | 10 | `comment` | 5 |
| `industryAllocation` | 10 | `like` | 2 |

Y el remate ([L840](base/teoria/vendor/oasis/src/models/banking_model.js#L840)):

```js
const karmaScore = Math.max(0, Math.round(rawKarma - carbonGrams));
```

**La huella de carbono se resta del karma.** Y el carbono se computa por bytes del propio feed: `0,095 g CO₂ por MiB` ([L35](base/teoria/vendor/oasis/src/models/banking_model.js#L35)), con un impuesto de `0,1 ECOin por gramo`. Quien más publica, más pesa; quien más pesa, más contamina; quien más contamina, menos cobra y menos desempata. Hay una teoría política entera comprimida en esa línea de código, y no es la de Trevijano.

### 2.4 L.A.R.P. — [larp_model.js](base/teoria/vendor/oasis/src/models/larp_model.js) · 953 líneas

Nueve casas: **ACADEMIA** (donde todos entran) más **SolarIS** (gobierno, ley, diplomacia), **ARRakis** (ingeniería), **TERRA.VErDE** (salud, alimento, ecología), **UNSYSTem** (caos táctico), **DogmA** (conocimiento, información, IA), **HeliX** (cultura, humor, rito), **QuarK** (seguridad, defensa), **HERmanDAD** (construcción, logística, producción).

Mecánica verificada:

- **La casa gobernante se determina por el mes del calendario**: `HOUSE_KEYS[now.getMonth() % 9]` ([L164-166](base/teoria/vendor/oasis/src/models/larp_model.js#L164-L166)). No hay elección, ni sorteo, ni mérito. Hay **turno**. La wiki lo confirma: *"no traditional elections occur — governance derives from this predetermined cyclical succession"*.
- Nueve casas y doce meses: el ciclo **no cierra con el año**. La rotación se desfasa cada enero. Probablemente no es intencionado; políticamente es lo más interesante del mecanismo, porque impide que ninguna casa capture nunca el mismo mes.
- **Adscripción por test**: 10 preguntas con pesos por casa ([L14-136](base/teoria/vendor/oasis/src/models/larp_model.js#L14-L136)), reintento con **30 días de enfriamiento**. El resultado se pondera además por el número de miembros de cada casa (compensación de tamaño). Es un Sorting Hat con corrección demográfica.
- **Los muros son secretos salvo dos excepciones** ([`wallIsPublic`](base/teoria/vendor/oasis/src/models/larp_model.js#L576)): ACADEMIA, y **la casa que gobierna ese mes**. Gobernar cuesta transparencia. Es la única implementación de *publicidad del poder* que hay en todo el sistema, y está en la capa que se declara "juego".
- Las casas son tribus reales etiquetadas `larp-<Casa>`, con auto-invitaciones y claves de tribu. La ficción se ejecuta sobre las mismas primitivas que lo "serio".
- Calendario propio: `día.solsticio.edad_solar.casa.ciclo`, con `SOLAR_AGE_OFFSET = 10000000 - 2026` — el año 2026 es el año **10.000.000**. Datación de civilización larga.

### 2.5 Lo demás, en una línea

`Industry` (medios de producción con propiedad y voto de sus miembros), `School` (cursos, exámenes, certificados con karma), `Tribes` (grupos cifrados, invitación estricta o abierta, anidables), `Market`/`Shops`/`Projects` (economía real en ECOin), `Opinions`/`Polls`/`Votes` (opinión y consulta, mínimo 7 días de votación), `Blockchain`/`Melody` (explorar y *sonificar* el log), `AI 42` (LLM local entrenado con el contenido de la red), `Multiverse` (puentes a Mastodon y Telegram sin persistir contenido ajeno).

---

## 3. Confrontación: los siete criterios contra el código

| # | Criterio trevijanista | Estado en Oasis 1.0.7 | Veredicto |
| :-- | :-- | :-- | :-- |
| 1 | Democracia **formal**, procedimiento antes que contenido | El procedimiento está codificado, es público, auditable y ejecutable. Nadie puede alterar plazos ni quórums sin bifurcar el software. | ✅ **Cumple**, y con una literalidad que ninguna constitución en papel alcanza |
| 2 | **Separación de poderes en el origen** | Una sola votación produce el único poder. Bajo `DICTATORSHIP`, el mismo sujeto legisla y juzga, y el código lo comprueba. No existe ejecutivo separado. | ❌ **Falla en la raíz** |
| 3 | Representación auténtica, distrito uninominal | Las **tribus pueden ser candidatas**; ganar una tribu otorga iniciativa legislativa a todos sus miembros. Es una lista de partido con otro nombre. | ❌ **Falla** |
| 4 | Estado de partidos ≠ Estado de derecho | La tribu es el partido. Además concentra las claves de cifrado, las invitaciones y ahora el poder legislativo. | ❌ **Reproduce la partitocracia** |
| 5 | Libertad política colectiva | Existe la salida (`publishLeaveLarp`, salir de una tribu, correr el propio nodo) pero la **voz** está racionada: 3 propuestas por mandato, y solo para quien gobierna. | ⚠️ **Parcial**: mucha libertad de salida, poca libertad política |
| 6 | La República como forma, no ideología | El sistema es **agnóstico de forma**: ofrece democracia, dictadura, karmatocracia y anarquía como opciones de menú. | ⚠️ **Ortogonal**: no es una república, es un *selector* de regímenes |
| 7 | Libertad constituyente previa | El estado por defecto es ANARCHY, y en ANARCHY **todos pueden proponer**. La libertad constituyente no es un momento fundacional: es la línea base a la que el sistema retorna cada 60 días si nadie alcanza quórum. | ✅ **Cumple, y por una vía que Trevijano no previó** |

### A. La fusión de poderes es una *feature*

`courts_model.js` verifica que el gobierno sea `DICTATORSHIP` **antes de permitir** que el gobernante juzgue. Un sistema que valida la concentración de poderes como precondición de una función no tiene un problema de diseño: tiene una doctrina. Es coherente consigo mismo y es exactamente lo que la Teoría Pura combate.

### B. La tribu es el partido

Los criterios trevijanistas 3 y 4 caen juntos. `canPropose()` devuelve `true` para **todo miembro** de la tribu gobernante. El vínculo representativo no va del elector al representante, sino del elector a la organización. Quien vota a una tribu no sabe quién legislará en su nombre — se lo dirán después, o no.

### C. El karma: renta y poder en un solo escalar

Este es el hallazgo central.

```
karma  →  desempate electoral        (parliament_model.js:422)
karma  →  quién legisla bajo KARMATOCRACY (parliament_model.js:560-588)
karma  →  orden y desempate de las candidaturas a juez (courts_model.js:805)
karma  →  cuánta Renta Básica cobras      (banking_model.js:938-958)
```

Un mismo número decide tu peso político y tu ingreso. En términos trevijanistas esto no es una separación de poderes imperfecta: **es la abolición del problema**, porque no hay dos fuentes que separar. Y como el karma se acumula por publicar, el sistema tiene un nombre clásico: **sufragio censitario**, donde el censo ya no es la renta ni la propiedad sino la actividad. La aristocracia de la notoriedad, con métrica pública y decaimiento exponencial.

El agravante técnico: el karma **se publica en el propio log** (`karmaScore`, [L501-506](base/teoria/vendor/oasis/src/models/banking_model.js#L501-L506)). Es un rango visible, permanente y comparable. Un catastro moral.

### D. La ley que nace muerta y el olvido como derogación

Las leyes se promulgan cuando expira el gobierno que las votó, y las revocadas se hacen invisibles con un tombstone. La nota final de la v1 de este documento exigía *"transparencia y trazabilidad en todos sus procesos"*. El mecanismo de derogación va justo en la dirección contraria — atenuado, eso sí, por la naturaleza append-only de SSB: el dato sobrevive aunque el cliente lo esconda. La reparación es barata (RP-6, §4) y merece la pena.

### E. La justicia secreta

Los tribunales cifran la instrucción por defecto y la publicidad es opcional. Sin publicidad del proceso no hay control del juez por el pueblo, que es la razón última del jurado en toda la tradición liberal-republicana. Aquí el compromiso privacidad ↔ publicidad se resolvió por defecto a favor de la privacidad; para un modelo republicano hay que invertirlo al menos para la sentencia.

### F. La anarquía calculada (donde el sistema es mejor de lo que pretende)

Si ninguna candidatura alcanza el 25% del censo, `resolveElection` no proclama a nadie: devuelve un `virtualAnarchyTerm` ([L373-393](base/teoria/vendor/oasis/src/models/parliament_model.js#L373-L393)) que **ni siquiera se publica en el log**. Un gobierno inexistente, con identificador (`anarchy:<ciclo>`), duración y efectos jurídicos: bajo él, todo el mundo recupera la iniciativa legislativa.

Esto es, sin proponérselo, una implementación del **período constituyente permanente**. El poder constituyente no se delega ni se agota: vuelve al cuerpo político por defecto, cada 60 días, salvo que una mayoría cualificada lo constituya expresamente. Es la pieza más aprovechable del sistema para una variante republicana, y es la única que la v1 de este documento no había imaginado.

### G. El turno como forma de Estado (L.A.R.P.)

La rotación mensual de las 9 casas no es representación ni sorteo: es **turno estamental por función** (los que saben, los que guardan, los que construyen, los que ríen, los que sabotean). El precedente no es la república moderna; es el gremio medieval y el organicismo corporativo. Trevijano lo rechazaría sin matices: no hay representación política donde el poder se adscribe por función social.

Y aun así, esta capa contiene la única transparencia obligatoria del sistema (el muro del gobernante se abre mientras gobierna) y el único poder que **nadie puede retener**, porque lo quita el calendario. Que el juego sea más republicano que el parlamento es el chiste estructural de todo el ecosistema, y conviene no dejarlo pasar.

---

## 4. Especificación RP-OASIS: la bifurcación republicana

No una red nueva: un **conjunto de parches sobre 1.0.7**, cada uno mapeado a su punto de intervención. La AGPL-3.0 lo permite y lo obliga a devolver.

| # | Cambio | Punto de intervención | Criterio que repara |
| :-- | :-- | :-- | :-- |
| **RP-1** | **Dos poderes, dos elecciones.** Añadir `powerBranch: 'LEGISLATIVE' \| 'EXECUTIVE'` a `parliamentTerm`, con dos papeletas independientes y **ciclos desfasados 30 días** para que jamás coincidan en origen. | `termWindowFor`, `resolveElectionImpl`, `proposeCandidature` | crit. 2 |
| **RP-2** | **Solo personas al legislativo.** Rechazar `targetType === 'tribe'` para la rama legislativa. Las tribus pueden concurrir al ejecutivo (donde la unidad de acción tiene sentido), nunca a la representación. | `resolveTarget`, `proposeCandidature` | crit. 3 y 4 |
| **RP-3** | **Sorteo verificable en lugar de karma** para el desempate: hash del último mensaje del log al cierre del ciclo. Reproducible, impredecible, no censitario. | `chooseWinnerFromCandidaturesAsync` L422 | crit. 3 |
| **RP-4** | **Desacoplar el escalar.** Dos métricas distintas y no convertibles: `contributionScore` (economía, RBU) y **elegibilidad política binaria** (censo: cumple / no cumple). Eliminar `KARMATOCRACY` de `METHODS`. | `banking_model.js`, `parliament_model.js:23` | crit. 2 y 3 |
| **RP-5** | **Romper la fusión judicial.** Eliminar `DICTATOR` de los métodos de Courts. El juez es electo (ya existe `courtsNomination`) o sorteado entre el censo — jurado. | `courts_model.js:139-155` | crit. 2 |
| **RP-6** | **Derogación con memoria.** Sustituir el `tombstone` sobre leyes por `parliamentLawRepeal` con `repealedAt`, `repealedBy` y motivación. La ley derogada se muestra tachada, no desaparece. | `enactApprovedChanges` L1145 | crit. 1, trazabilidad |
| **RP-7** | **Publicidad de la sentencia.** Cifrado permitido en instrucción; **veredicto y órdenes siempre en claro**. | `issueVerdict`, `courtsVisibility` | crit. 1 |
| **RP-8** | **Iniciativa legislativa popular.** Una proposición avalada por el 10% del censo entra a votación sin pasar por `canPropose()`. | `canPropose` L1298, `createProposal` | crit. 5 |
| **RP-9** | **Formalizar el constituyente.** Tipo `constituentAssembly` que, en ciclos ANARCHY consecutivos, habilite la modificación de las propias constantes (`TERM_DAYS`, umbrales) con supermayoría del 80%. Constitución rígida, reformable solo desde el estado de libertad constituyente. | nuevo modelo | crit. 7 |
| **RP-10** | **Publicidad del poder, generalizada.** Portar `wallIsPublic` del L.A.R.P. al parlamento: mientras gobiernas, tu actividad en la red es pública. | `larp_model.js:576` → `parliament_view.js` | crit. 1 |

**Lo que no se toca, y por qué.** El calendario fijo desde `TERM_EPOCH` (nadie convoca elecciones), el voto único por ciclo, el tope de 3 propuestas, el quórum del 25%, el retorno automático a ANARCHY. Son buen derecho constitucional escrito en aritmética.

---

## 5. Backlog v2

Estado de las tareas de la v1: **✅ hecho por upstream** · **♻️ reformulada** · **☠️ obsoleta** · **▶️ vigente**.

### OP-01 · Infraestructura de red y comunicación soberana

| ID | Task | Estado | Nota |
| :-- | :-- | :-- | :-- |
| TK-01 | Desplegar nodo SSB local | ▶️ | Sigue siendo el paso 1. [docs/install/install.md](base/teoria/vendor/oasis/docs/install/install.md) |
| TK-02 | Conectar a "La Plaza" | ▶️ | `pub.solarnethub.com`, stats en `laplaza.solarnethub.com` |
| TK-03 | Configurar cliente Oasis | ▶️ | v1.0.7. `install.sh` + `oasis.sh` |
| TK-04 | Identidad soberana (sigchain) | ✅ | Automática al arrancar; onboarding de 7 pasos ([onboarding_model.js:5](base/teoria/vendor/oasis/src/models/onboarding_model.js#L5)) |
| TK-05 | Diseñar gobernanza sobre SSB | ☠️→♻️ | **Ya existe.** Se convierte en TK-26 (auditoría) |
| TK-06 | Red de confianza "amigos de amigos" | ✅ | Trustnet + invitaciones + modos `strict`/`open` en tribus |

### OP-02 · Capa económica ~~(Faircoin)~~ → ECOin + Banking

| ID | Task | Estado | Nota |
| :-- | :-- | :-- | :-- |
| TK-07…TK-12 | Todo el eje Faircoin/CVN/BotC/FairMarket | ☠️ | Repositorio sin commits desde 2022-02-05 |
| **TK-27** | Desplegar wallet ECOin y enlazarla a Oasis | ▶️ Alta | v0.0.4 (feb 2026). `ecoin.03c8.net` |
| **TK-28** | Auditar el reparto de RBU por épocas | ▶️ Alta | [banking_model.js:930-990](base/teoria/vendor/oasis/src/models/banking_model.js#L930-L990). Verificar `alpha`, topes y `hash` del snapshot |
| **TK-29** | Documentar la fiscalidad de carbono | ▶️ Media | 0,095 g CO₂/MiB · 0,1 ECOin/g. ¿Quién fijó esas constantes y con qué legitimidad? |
| **TK-30** | Evaluar el sesgo concentrador de PoT | ▶️ Media | El 50% del subsidio de bloque a transacciones >500 ECO |

### OP-03 · Gobernanza y separación de poderes → **auditoría y bifurcación**

| ID | Task | Estado | Prioridad |
| :-- | :-- | :-- | :-- |
| **TK-26** | Auditoría formal de `parliament_model.js` contra los 7 criterios (§1.3, evaluados en §3) | ▶️ | Alta |
| TK-13 | Definir poder legislativo | ♻️ → **RP-1, RP-2** | Alta |
| TK-14 | Definir poder ejecutivo | ♻️ → **RP-1** | Alta |
| TK-15 | Definir poder judicial | ♻️ → **RP-5, RP-7** | Alta |
| TK-16 | Asamblea constituyente digital | ♻️ → **RP-9** | Media |
| TK-17 | Documentar la separación en origen | ▶️ | Baja |
| **TK-31** | Parche RP-3: sorteo verificable | ▶️ | Media |
| **TK-32** | Parche RP-4: desacoplar karma político de karma económico | ▶️ | **Crítica** |
| **TK-33** | Parche RP-6: derogación con memoria | ▶️ | Media |
| **TK-34** | Parche RP-8: iniciativa legislativa popular | ▶️ | Alta |

### OP-04 · Soberanía y autogestión

| ID | Task | Estado | Nota |
| :-- | :-- | :-- | :-- |
| TK-18 | Modo offline-first | ✅ | Nativo en SSB |
| TK-19 | Sistema de invitaciones | ✅ | PUBs y tribus, más auto-invitaciones L.A.R.P. |
| TK-20 | TOR / red onion | ▶️ Media | Ver [docs/security.md](base/teoria/vendor/oasis/docs/security.md) |
| TK-21 | Documentar la autogestión | ▶️ Baja | |

### OP-05 · Integración

| ID | Task | Estado | Nota |
| :-- | :-- | :-- | :-- |
| TK-22 | Wallet en la interfaz | ✅ | Módulo `Wallet` + `wallet-addresses.json` |
| TK-23 | Dashboard de gobierno | ✅ | `parliamentGovernmentCard` en [parliament_view.js:157](base/teoria/vendor/oasis/src/views/parliament_view.js#L157) |
| TK-24 | Impuestos cooperativos | ✅ | Implementado como **impuesto de carbono**, no como cuota |
| TK-25 | Constitución técnica | ▶️ Baja | Debe escribirse **después** de RP-1…RP-10 |

### OP-06 · Nueva: la capa L.A.R.P. como laboratorio constitucional

| ID | Task | Descripción | Prioridad |
| :-- | :-- | :-- | :-- |
| **TK-35** | Documentar la rotación de 9 casas sobre 12 meses y su desfase anual | Verificar si es intencionado; si no lo es, defenderlo igualmente | Media |
| **TK-36** | Portar `wallIsPublic` al parlamento (RP-10) | La transparencia del gobernante es la mejor idea del sistema y está en el juego | Alta |
| **TK-37** | Contrastar el modelo estamental de casas con la crítica trevijanista al organicismo | Documento teórico | Baja |
| **TK-38** | Medir empíricamente el sesgo del test de 10 preguntas | ¿La corrección por tamaño de casa basta? | Baja |

### Resumen de prioridades v2

| Prioridad | Tasks |
| :-- | :-- |
| **Crítica** | TK-32 |
| **Alta** | TK-01, TK-02, TK-03, TK-26, TK-27, TK-28, TK-34, TK-36, y los parches RP-1/RP-2/RP-5 |
| **Media** | TK-20, TK-29, TK-30, TK-31, TK-33, TK-35 |
| **Baja** | TK-17, TK-21, TK-25, TK-37, TK-38 |

---

## 6. Fuentes

**Código auditado (disco).** [`base/teoria/vendor/oasis`](base/teoria/vendor/oasis/) — commit `9a657b7`, release 1.0.7, 2026-09-08. Reproducible: `git clone --depth 1 https://github.com/epsylon/oasis.git`.

**Red.**
- Oasis: https://github.com/epsylon/oasis · https://wiki.solarnethub.com/socialnet/overview
- Rol L.A.R.P.: https://wiki.solarnethub.com/socialnet/roleplaying
- ECOin: https://ecoin.03c8.net · https://wiki.solarnethub.com/ecoin/overview
- PUB "La Plaza": https://pub.solarnethub.com · https://laplaza.solarnethub.com
- SNH: https://solarnethub.com · https://wiki.solarnethub.com
- Faircoin (histórico): https://github.com/faircoin/faircoin · https://fair-coin.org
- MCRC: https://mcrc.diarioerc.com · https://www.diariorc.com
- Trevijano: https://www.antoniogarciatrevijano.info

**Grado de certeza.** Lo dicho sobre Oasis: **verificado en código**, con fichero y línea. Lo dicho sobre ECOin y la wiki de SNH: **fuente primaria del proyecto, no verificada de forma independiente**. Lo dicho sobre el abandono de Faircoin: **inferido de la actividad del repositorio** (hecho duro: cero commits desde 2022-02-05) y no de un comunicado de cierre. Lo dicho sobre doctrina trevijanista: **paráfrasis marcada**, no cita.

---

## 7. Anexo · Documento v1 (2025, conservado íntegro)

> Se conserva sin ediciones. Sus tablas OP/TK siguen siendo la referencia de numeración; la §5 indica cuáles quedan vivas.

<details>
<summary>Desplegar v1</summary>

Entendido. Quieres usar la infraestructura de SolarNET.HuB y el ecosistema Faircoin como **soporte técnico y económico** para una implementación práctica del modelo de **República Pura** de Antonio García-Trevijano.

Te he preparado dos cosas:

1.  Un **prompt de activación** listo para copiar y pegar a tu agente, con todas las fuentes y enlaces necesarios.
2.  Un **backlog de tareas Scrum** estructurado en `Opportunity` (visión) y `Task` (ejecución) para que el agente sepa por dónde empezar.

---

## 1. PROMPT DE ACTIVACIÓN PARA EL AGENTE

Copia y pega esto en tu agente. Incluye las URLs de los repositorios que has bajado para que las analice.

```markdown
# PROMPT DE ACTIVACIÓN: MODELIZACIÓN DE LA REPÚBLICA PURA (TREVIJANO) CON SNH + FAIRCOIN

## OBJETIVO PRINCIPAL
Modelizar una implementación práctica del modelo de "República Pura" de Antonio García-Trevijano utilizando como infraestructura:
- **SolarNET.HuB (SNH)** para la capa de comunicación, red y gobernanza comunitaria.
- **Ecosistema Faircoin-FairCoop-Bank of the Commons** para la capa económica, monetaria y financiera.

## CONTEXTO FILOSÓFICO: MODELO DE TREVIJANO
- **Fundamento**: La "Teoría Pura de la República" de Antonio García-Trevijano propone una República Constitucional basada en:
  - **Soberanía popular** como poder constituyente.
  - **Democracia formal**: representación política auténtica, elección directa del ejecutivo y separación de poderes en origen.
  - **Ausencia de ideología**: la república se entiende como forma de Estado, no como ideología.
  - **Libertad política colectiva** como eje del sistema.
- **Fuentes primarias**:
  - "Teoría Pura de la República" y "Teoría Pura de la Democracia" (Antonio García-Trevijano).
  - Asociación MCRC (Movimiento por la Constitución y la República).
  - Web de referencia: https://www.antoniogarciatrevijano.info

## INFRAESTRUCTURA DISPONIBLE

### SolarNET.HuB (SNH) - Capa de Comunicación y Gobernanza
- **Arquitectura**: Red distribuida con nodo central de control + nodos autónomos【0†L5-L8 del documento del usuario】.
- **Protocolo principal**: Gossip protocol (propagación epidémica de información)【0†L10-L16 del documento del usuario】.
- **Red subyacente**: Secure Scuttlebutt (SSB) - malla P2P con "sigchains" (blockchains personales)【0†L18-L27 del documento del usuario】.
- **Cliente**: Oasis - frontend HTML+CSS puro, sin JavaScript, cifrado extremo a extremo【0†L28-L38 del documento del usuario】.
- **PUB desplegado**: "La Plaza" - uno de los mayores PUBs del mundo.
- **Repositorio oficial**: https://github.com/epsylon/oasis
- **Wiki técnica**: https://wiki.solarnethub.com

### Ecosistema Faircoin - Capa Económica y Financiera
- **FairCoin**: Criptomoneda con algoritmo de consenso **Proof-of-Cooperation (PoC)**.
  - Bloques creados por CVNs (Cooperatively Validated Nodes) en turno rotatorio.
  - Fork de Bitcoin 0.12.
  - Documentación técnica: https://github.com/faircoin/faircoin/blob/master/doc/on-proof-of-cooperation.md
  - White Paper: https://fair-coin.org
- **FairCoop**: Cooperativa global que coordina el ecosistema.
- **Bank of the Commons (BotC)**: Cooperativa bancaria alternativa, co-fundada por FairCoop.
- **FreedomCoop**: Marco legal europeo para el ecosistema.
- **FairMarket, Fairbnb**: Aplicaciones de economía real.

## TAREA DEL AGENTE
1. Analiza los repositorios de código que te he proporcionado (SNH/Oasis y Faircoin).
2. Identifica los componentes técnicos que pueden mapearse a los principios de la República Pura de Trevijano.
3. Genera un backlog de tareas Scrum con la siguiente estructura:
   - **Epic**: Modelización de la República Pura con SNH + Faircoin.
   - **Opportunity (OP)**: Grandes bloques de oportunidad (visión, qué se quiere lograr).
   - **Task (TK)**: Tareas concretas de ejecución (código, configuración, documentación).
4. Para cada tarea, indica:
   - Dependencias técnicas.
   - Fuentes de información relevantes (de las listadas arriba).
   - Prioridad (Alta/Media/Baja).

## FORMATO DE SALIDA ESPERADO
- Lista numerada de Opportunities (OP-01, OP-02, ...).
- Lista numerada de Tasks (TK-01, TK-02, ...) agrupadas por Opportunity.
- Enlaces a documentación y repositorios en cada tarea.

## RESTRICCIONES
- El agente NO debe buscar información libremente. Solo debe usar:
  - Los repositorios proporcionados.
  - Las URLs y documentos citados en este prompt.
  - El conocimiento incorporado en su entrenamiento sobre Trevijano, SNH y Faircoin.
```

---

## 2. BACKLOG DE TAREAS SCRUM (OPPORTUNITY + TASK)

Aquí tienes el backlog generado a partir de la información disponible. Está estructurado para que el agente sepa exactamente qué hacer y en qué orden.

---

### EPIC: Modelización de la República Pura (Trevijano) con SolarNET.HuB + Faircoin

---

#### OP-01: Infraestructura de Red y Comunicación Soberana

**Descripción**: Establecer una red de comunicación descentralizada, resistente a la censura y basada en la confianza comunitaria, que refleje la soberanía popular del modelo trevijano.

| ID | Task | Descripción | Dependencias | Fuentes | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TK-01** | Desplegar nodo SSB local | Instalar y configurar un nodo Secure Scuttlebutt (SSB) siguiendo la documentación de SNH. | Repositorio Oasis | [Wiki SNH Engineering](https://wiki.solarnethub.com/socialnet/engineering) | Alta |
| **TK-02** | Conectar a "La Plaza" (PUB) | Obtener un código de invitación para el PUB "La Plaza" y conectar el nodo a la red. | TK-01 | https://laplaza.solarnethub.com | Alta |
| **TK-03** | Configurar cliente Oasis | Compilar/instalar el cliente Oasis desde el repositorio `epsylon/oasis`. | TK-01 | https://github.com/epsylon/oasis | Alta |
| **TK-04** | Crear identidad soberana (sigchain) | Generar una identidad SSB (sigchain personal) sin email ni teléfono【0†L36-L38 del usuario】. | TK-02 | [Wiki SNH Engineering](https://wiki.solarnethub.com/socialnet/engineering) | Alta |
| **TK-05** | Documentar modelo de gobernanza en SSB | Diseñar un sistema de votación/consenso basado en los feeds de SSB para simular la "representación política auténtica". | TK-04 | [Wiki SNH Engineering](https://wiki.solarnethub.com/socialnet/engineering) | Media |
| **TK-06** | Implementar sistema de "amigos de amigos" | Configurar la red de confianza (trustnet) para que solo se repliquen feeds de miembros validados. | TK-04 | [Wiki SNH Engineering](https://wiki.solarnethub.com/socialnet/engineering) | Media |

---

#### OP-02: Capa Económica y Monetaria (Faircoin + Bank of the Commons)

**Descripción**: Integrar el ecosistema Faircoin como mecanismo de intercambio económico y financiero, alineado con la soberanía económica de la república.

| ID | Task | Descripción | Dependencias | Fuentes | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TK-07** | Desplegar nodo Faircoin (CVN) | Configurar un nodo Faircoin2 como Cooperatively Validated Node (CVN). | Repositorio Faircoin | [Doc PoC](https://github.com/faircoin/faircoin/blob/master/doc/on-proof-of-cooperation.md); [CVN Guide](https://github.com/faircoin/faircoin/blob/master/doc/CVN-operators-guide.md) | Alta |
| **TK-08** | Sincronizar blockchain Faircoin | Descargar y sincronizar la cadena de bloques Faircoin. | TK-07 | [Faircoin White Paper](https://fair-coin.org) | Alta |
| **TK-09** | Crear wallet Faircoin | Generar una cartera Faircoin para la tesorería de la república. | TK-08 | [Faircoin GitHub](https://github.com/faircoin/faircoin) | Alta |
| **TK-10** | Integrar Bank of the Commons | Configurar servicios bancarios cooperativos (cuentas, transferencias) usando la infraestructura de BotC. | TK-08 | [Faircoin PoC](https://github.com/faircoin/faircoin/blob/master/doc/on-proof-of-cooperation.md) | Media |
| **TK-11** | Implementar sistema de "FairMarket" local | Desplegar una instancia de FairMarket para intercambio de bienes y servicios dentro de la comunidad. | TK-10 | [OCE GitBook](https://oce.gitbook.io) | Media |
| **TK-12** | Documentar modelo de "distribución igualitaria" | Diseñar un mecanismo de distribución inicial de FairCoin basado en la participación comunitaria (no especulación). | TK-09 | [Faircoin Story](https://fair-coin.org) | Media |

---

#### OP-03: Gobernanza y Separación de Poderes (Modelo Trevijano)

**Descripción**: Mapear los principios de la República Pura (separación de poderes, representación auténtica, soberanía popular) a la arquitectura SNH + Faircoin.

| ID | Task | Descripción | Dependencias | Fuentes | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TK-13** | Definir "Poder Legislativo" en SNH | Diseñar un sistema de propuestas y votación en SSB (feeds firmados) que simule la representación política. | TK-05 | [Teoría Pura Trevijano](https://www.antoniogarciatrevijano.info) | Alta |
| **TK-14** | Definir "Poder Ejecutivo" en SNH | Establecer un rol de administración central (nodo central de SNH) con capacidades limitadas y rotativas【0†L5-L8 del usuario】. | TK-13 | [Wiki SNH Engineering](https://wiki.solarnethub.com/socialnet/engineering) | Alta |
| **TK-15** | Definir "Poder Judicial" en SNH | Implementar un sistema de resolución de conflictos basado en la validación por pares (CVNs + feeds). | TK-14 | [Teoría Pura Trevijano](https://www.antoniogarciatrevijano.info) | Media |
| **TK-16** | Crear "Asamblea Constituyente" digital | Utilizar la red SSB + Oasis para celebrar una asamblea virtual donde se debatan y voten las reglas de la república. | TK-04, TK-13 | [Wiki SNH Ecosystem](https://wiki.solarnethub.com) | Media |
| **TK-17** | Documentar el modelo de "separación en origen" | Redactar un documento técnico que explique cómo la arquitectura SNH + Faircoin implementa la separación de poderes. | TK-13, TK-14, TK-15 | [Teoría Pura Trevijano](https://www.antoniogarciatrevijano.info) | Baja |

---

#### OP-04: Soberanía y Autogestión (Offline-first, Invite-only)

**Descripción**: Asegurar que la red pueda funcionar de forma autónoma, incluso sin conexión a internet, y que la membresía sea por invitación (comunidad de confianza).

| ID | Task | Descripción | Dependencias | Fuentes | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TK-18** | Configurar modo offline-first | Asegurar que el nodo SSB pueda operar y sincronizarse cuando haya conectividad. | TK-02 | [SNH Digital Survival Kit](https://solarnethub.com) | Alta |
| **TK-19** | Implementar sistema de invitaciones | Crear un flujo de generación y distribución de códigos de invitación para nuevos miembros. | TK-04 | [GitHub Oasis](https://github.com/epsylon/oasis) | Alta |
| **TK-20** | Configurar TOR / red onion | Añadir capa de anonimato y resistencia a la censura mediante TOR. | TK-18 | [SNH Digital Survival Kit](https://solarnethub.com) | Media |
| **TK-21** | Documentar el modelo de "autogestión" | Explicar cómo la combinación de SNH + Faircoin permite la autosuficiencia de la comunidad. | TK-19, TK-20 | [Wiki SNH](https://wiki.solarnethub.com) | Baja |

---

#### OP-05: Integración y Sostenibilidad del Ecosistema

**Descripción**: Conectar todas las capas (comunicación, economía, gobernanza) en un ecosistema funcional y sostenible.

| ID | Task | Descripción | Dependencias | Fuentes | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TK-22** | Integrar wallet Faircoin con Oasis | Permitir que los usuarios de Oasis vean su saldo y realicen transferencias desde la interfaz. | TK-03, TK-09 | [OCE GitBook](https://oce.gitbook.io) | Alta |
| **TK-23** | Crear dashboard de gobierno | Desarrollar un panel en Oasis que muestre propuestas activas, votaciones y estado de la red. | TK-16, TK-22 | [Wiki SNH](https://wiki.solarnethub.com) | Media |
| **TK-24** | Implementar sistema de "impuestos" cooperativos | Diseñar un mecanismo de contribución voluntaria en FairCoin para el mantenimiento de la red (CVNs, PUBs). | TK-10 | [Faircoin PoC](https://github.com/faircoin/faircoin/blob/master/doc/on-proof-of-cooperation.md) | Media |
| **TK-25** | Redactar "Constitución Técnica" | Documento final que integre todos los principios de Trevijano con la implementación técnica realizada. | Todas las anteriores | [Teoría Pura Trevijano](https://www.antoniogarciatrevijano.info) | Baja |

---

### Resumen de Prioridades

| Prioridad | Tasks |
| :--- | :--- |
| **Alta** | TK-01, TK-02, TK-03, TK-04, TK-07, TK-08, TK-09, TK-13, TK-14, TK-18, TK-19, TK-22 |
| **Media** | TK-05, TK-06, TK-10, TK-11, TK-12, TK-15, TK-16, TK-20, TK-23, TK-24 |
| **Baja** | TK-17, TK-21, TK-25 |

---

### 📌 Nota para el agente

Este backlog parte de la documentación disponible y de los repositorios que has bajado. Si encuentras que algún componente no está documentado o falta, prioriza la **creación de documentación** antes que el código. La República Pura de Trevijano exige **transparencia y trazabilidad** en todos sus procesos.
</details>
