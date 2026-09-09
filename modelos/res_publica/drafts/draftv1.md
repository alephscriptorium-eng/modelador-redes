# Informe draft v1 · ¿Clon o parecido? El modelo de Trevijano frente a lo modelado

**2026-09-09.** Respuesta corta: **no hemos modelado un clon. Hemos auditado un sistema ajeno (Oasis 1.0.7) y propuesto diez parches.** Lo que existe hoy en código se parece a la República Constitucional de Trevijano en 3 de 14 elementos; con los parches RP-1…10 aplicados subiría a 8; y hay 4 elementos que **no admiten traducción** a una red sin territorio. Nada de RP-1…10 está implementado: son especificaciones.

Grado de certeza sobre la doctrina: **A** = tesis nuclear, repetida en toda la obra y en el ideario del MCRC; **B** = posición conocida pero sin verbatim a mano; **C** = reconstrucción probable, verificar en *Teoría Pura de la República Constitucional* antes de citar.

---

## Tabla 1 · El modelo, elemento a elemento

| # | Elemento del modelo trevijanista | Cert. | Oasis 1.0.7 (código real) | Tras RP-1…10 (propuesto) | Veredicto |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | **Libertad política colectiva** como bien distinto de las libertades civiles: un pueblo puede ser civilmente libre y políticamente esclavo | A | Libertades civiles máximas (cifrado, salida, sin identidad real). Voz política racionada: solo gobierna quien gana, 3 propuestas/mandato | RP-8 (iniciativa popular 10 %) abre la voz a todos. *Nota 2026-09-09: draftv2 TK-34 la reformula como iniciativa de mónada a través del representante, para no chocar con #13* | **Parecido** tras RP-8 |
| 2 | **Democracia formal**: la democracia es un *procedimiento* de origen del poder, no un contenido | A | El procedimiento está codificado, público y ejecutable (`parliament_model.js`) | — | **Clon**, y más literal que cualquier constitución en papel |
| 3 | **Período de libertad constituyente** previo a toda constitución; ruptura, no reforma | A | ANARCHY como estado por defecto cada 60 días si nadie alcanza el 25 %: constituyente latente y calculado | RP-9 lo formaliza (`constituentAssembly`, 80 %). *Nota 2026-09-09: draftv2 TK-D09 añade la apertura por **acción** (`constituentCall`), no solo por ausencia, y declara provisionales las constantes heredadas: el fork nace por constituyente, no por reforma* | **Clon accidental** hoy → **Clon** con TK-78 |
| 4 | **Separación de poderes en el origen**: ejecutivo y legislativo nacen de **dos elecciones distintas** | A | Una sola elección produce un solo poder; bajo DICTATORSHIP el mismo sujeto juzga | RP-1 (dos ramas, ciclos desfasados 30 d) | **Ausente** hoy → **Parecido** con RP-1 |
| 5 | **Presidente elegido por sufragio directo**, jefe del ejecutivo, no sale del parlamento; sin moción de censura ni disolución | A/B | No hay ejecutivo. El "gobierno" es quien legisla | RP-1 crea la rama, pero no define qué *ejecuta* (en una red: ¿claves admin de la cadena, tesorería?). *Nota 2026-09-09: draftv2 TK-D06/G06/TK-84 dan la materia (chain-admin + tesorería bajo ley y presupuesto), el Consejo nombrado y la regla "no disuelve sin dimitir"* | **Ausente** hoy → **Parecido** con G06 |
| 6 | **Representación por distrito uninominal**, mayoritario a doble vuelta, candidato personal responsable ante sus electores | A | Candidaturas personales **o de tribu**; voto único por ciclo; sin distritos: el censo es uno | RP-2 (solo personas al legislativo) | **Parecido a medias**: cae la lista, pero **no hay distrito** — no hay territorio. *Nota 2026-09-09: draftv2 TK-D01/G01 traduce el distrito como colegio de M inhabitants por hash; con ello pasaría a **Parecido*** |
| 7 | **Sin listas de partido**; partidos como asociaciones privadas sin financiación pública; el Estado de partidos es oligarquía | A | La tribu es el partido: gana y todos sus miembros legislan; concentra claves, invitaciones y poder | RP-2 los saca del legislativo; el backlog los deja como operadores (CVN, tesoro) | **Parecido**, con el riesgo R11 abierto: la partitocracia vuelve por la economía |
| 8 | **Sufragio universal e igual**; sin censo por renta ni mérito | A | Un voto por inhabitant, igual… hasta el desempate y KARMATOCRACY, donde decide el karma (actividad menos carbono) | RP-3 (sorteo verificable), RP-4 (karma separado de política) | **Ausente** hoy → **Clon** con RP-3+4 |
| 9 | **Legislativo que controla al ejecutivo** (comisiones, interpelación) sin poder derribarlo | B | No hay a quién controlar | Sin parche específico. *Nota 2026-09-09: draftv2 TK-D18/G10 (informe firmado, interpelación, reprobación de acto) lo cubre* | **Ausente** hoy → **Parecido** con G06+G10 |
| 10 | **Justicia independiente de los partidos**; jueces no nombrados por el poder político; jurado | B | Jueces electos por la red (`courtsNomination`), juicio cifrado, `DICTATOR` fusiona poderes | RP-5 (fuera DICTATOR), RP-7 (sentencias públicas) | **Parecido**: la elección popular de jueces es más que lo que Trevijano pedía; el secreto es menos. *Nota 2026-09-09: draftv2 TK-D07 sustituye la elección por nombramiento del Consejo con certificado de `School`, añade jurado por sorteo y control de constitucionalidad; con G07 pasaría a **Clon** salvo en la publicidad del proceso* |
| 11 | **Publicidad del poder**: el gobernante actúa a la vista; responsabilidad personal | B | Solo en L.A.R.P.: el muro de la casa gobernante se hace público | RP-10 lo porta al Parlamento | **Parecido** tras RP-10 |
| 12 | **Mandato definido** con responsabilidad; **revocable por deslealtad** al mandato (cap. I; divulgación MCRC verificada, ver draftv2 §Divulgación) — *corregido 2026-09-09: antes decía «sin revocatoria del cargo»*; leyes derogables con memoria | A/B | 60 días fijos por calendario; derogación = tombstone (ocultación) | RP-6 (derogación con memoria); RP-11/TK-G04 (revocación por la mónada) | **Parecido**: el calendario fijo es incluso mejor derecho; el olvido se corrige; la revocación llega con TK-G04 |
| 13 | **Referéndum** solo constituyente; rechazo de la democracia directa como sustituto de la representación | A | Módulos `Polls`/`Opinions`/`Votes` = consulta permanente; ANARCHY = todos proponen | RP-9 restringe la reforma constitucional al 80 %. *Nota 2026-09-09: draftv2 D10/G08 dejan `Polls` sin fuerza, TK-34 canaliza la iniciativa por la mónada y D09 convierte ANARCHY en período constituyente: el asamblearismo queda donde Trevijano lo admite* | **Divergente** hoy → **Parecido** con G08 |
| 15 | **Consejo de Legislación** con presidente elegido por la Cámara: la ley recibe su fuerza coactiva de un órgano distinto del que la vota *(fila añadida 2026-09-09, fuera del recuento)* | B | No existe: `enactApprovedChanges` promulga automáticamente al expirar el mandato, sin sujeto responsable | draftv2 TK-D05/G05: Presidente + Consejo, promulgación firmada en ≤ 7 d, devolución motivada | **Ausente** hoy → **Parecido** con G05 |
| 14 | **La República es forma de Estado, no ideología**; no es de izquierdas ni de derechas | A | Oasis es un *selector* de regímenes (democracia, dictadura, karmatocracia, anarquía) con manifiesto explícitamente anticapitalista | Los parches eliminan DICTATORSHIP y KARMATOCRACY del menú. *Nota 2026-09-09: draftv2 D12 neutraliza el manifiesto a texto de tribu y deja RBU/ECOin/carbono como leyes ordinarias, no constantes* | **Divergente** hoy → **Parecido** con D12/G11 |

**Recuento.** Hoy: 2 clones (#2, #3), 1 parecido (#10), 6 ausentes o divergentes. Tras RP-1…10: 3 clones, 5 parecidos, 2 ausentes (#5 materia del ejecutivo, #9 control parlamentario), 2 divergentes (#13, #14), y 2 intraducibles (ver Tabla 2).

*Recuento tras la revisión capítulo a capítulo del Libro III (2026-09-09, ver `revision/`), condicionado a implementar todos los TK-G de draftv2: 4 clones (#2, #3, #8, #10), 11 parecidos (#1, #4, #5, #6, #7, #9, #11, #12, #13, #14, #15), 0 ausentes, 0 divergentes. De la Tabla 2 solo sigue intraducible la **escala**; distrito (D01), doble vuelta (D04) y materia del ejecutivo (TK-84) quedan traducidos.*

---

## Tabla 2 · Lo que no se puede clonar (y por qué)

| Elemento | Motivo | Qué hacemos en su lugar |
| :-- | :-- | :-- |
| **Distrito uninominal** (#6) | Presupone territorio y población fija. Una red SSB tiene un censo fluido (`inhabitantsCount` cuenta feeds con actividad) y ninguna geografía | Voto único por ciclo sobre candidatos personales. Alternativa a estudiar: "distritos" = PUBs (cada PUB elige un representante) — pero eso reintroduce al operador del PUB como cacique. *Superado por draftv2 TK-D01: colegios de tamaño M por hash determinista con semilla estable; el distrito sí es traducible sin territorio, a costa de la proximidad* |
| **Doble vuelta** | Requiere dos convocatorias; el ciclo de 60 días es aritmético y único | RP-3 (sorteo) solo desempata; no hay segunda vuelta. Podría simularse: primera mitad del ciclo = primera vuelta |
| **Escala** | Trevijano piensa en un Estado-nación (~350 diputados). Oasis tiene 19 estrellas en GitHub y un PUB | Todo lo modelado es una **maqueta 1:1 de un pueblo**, no de un Estado. Válida como laboratorio, no como prueba |
| **Poder ejecutivo con materia propia** (#5) | En un Estado el ejecutivo administra, recauda, hace cumplir. En Oasis nada se ejecuta: las leyes son textos en el log | El backlog v3 le da materia: claves chain-admin de Faircoin3 (`addcvn`, `addcoinsupply`, `setchainparameters`) y tesorería. Es el primer momento en que un "ejecutivo" digital tendría algo que ejecutar |

---

## Tabla 3 · Dónde Oasis es *más* republicano que el modelo

| Rasgo de Oasis | Trevijano | Lectura |
| :-- | :-- | :-- |
| Elecciones por calendario fijo desde 2020-01-01: nadie las convoca ni aplaza | Convocatoria por el poder constituido | Oasis blinda algo que Trevijano dejó a la ley electoral |
| Retorno automático a la anarquía si no hay quórum del 25 % | Período constituyente como momento excepcional | Oasis lo hace permanente y periódico |
| Jueces elegidos por la red | Independencia por carrera y jurado | Más democrático en origen; menos garantista |
| Transparencia obligatoria del gobernante (L.A.R.P.) | Publicidad como principio | Implementado como mecanismo, no como norma |

---

## Conclusión

1. **No es un clon y no puede serlo**: falta el territorio y falta la escala. Lo que cabe es una **república digital que herede los principios de origen** (formalidad, separación en el nacimiento, sufragio igual, constituyente previo) y renuncie honestamente a la geometría electoral (distritos, doble vuelta). *Nota 2026-09-09: la geometría se recupera en draftv2 (D01 mónadas por hash, D04 doble vuelta en ciclo partido); lo que sigue sin traducción es la escala.*
2. **Lo modelado hasta hoy es una auditoría + diez parches sin implementar.** El código real (Oasis 1.0.7) es un selector de regímenes con un sesgo censitario (karma) y una fusión de poderes verificada por el propio código.
3. **El punto más trevijanista de todo el ecosistema no lo diseñamos nosotros**: la anarquía calculada de `resolveElection` es un constituyente permanente. Convendría construir a partir de ahí, no a pesar de ello.
4. **El punto menos trevijanista tampoco**: Oasis tiene ideología (manifiesto), Trevijano la niega. El backlog v3 no resuelve esa tensión; la hereda. *Nota 2026-09-09: draftv2 D12 la resuelve por defecto (manifiesto neutralizado, constitución de solo forma, test de constitucionalidad G11); queda como alternativa divergente conservarlo.*

## Fuentes y certeza
- Doctrina: *Teoría Pura de la República* (3 vols.), *Teoría pura de la democracia*, ideario MCRC (mcrc.diarioerc.com, diariorc.com). Paráfrasis; las marcas B/C exigen verificación antes de citar.
- Código: `base/teoria/vendor/oasis` commit `9a657b7` (1.0.7, 2026-09-08). Detalle con fichero:línea en [draftv0.md (pura.md rev. 2) §2–§4](draftv0.md).
- Parches RP-1…10 y backlog v3: propuestos, no implementados. Plan en curso.
