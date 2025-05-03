GDD.

# GENERAL:

Título del Proyecto: Project Alpha.

Se han propuesto los siguientes nombres para el producto final:

- I, The Doctor.					
- Mr. Doctor.
- The Doc.					
- Sim doc.
- Doctor Sim (simulator).				
- Sim Doctor.
- Diagnostix.					
- Doctor EYE.
- Doctor Vision.
Género: Simulación.

Plataforma: Android.

**Descripción General:**

El jugador tomará el papel de un médico que deberá labrarse una reputación tratando a pacientes que pueden sufrir multitud de patologías, apoyándose en pruebas médicas de todo tipo tendrá que acertar en el diagnóstico y tratamiento si quiere avanzar en su carrera.

Controles: Pantalla táctil.

# MECÁNIAS GENERALES:

**Objetivos:**

Tratar a los pacientes que acudan a tu consulta, realizar pruebas médicas, lanzar un diagnóstico y acertar en el tratamiento que recibirá el paciente, con esto conseguirás reputación como médico que abrirá puertas a poder tratar más enfermedades y más complicadas, ascender como médico en el centro médico o poder aspirar a un hospital de prestigio, la vida del médico es muy complicada y sobre todo cara, habrá que esforzarse para poder cumplir tus objetivos.

**Progresión:**

Al ir ganando reputación como médico el centro en el que desempeñas tus labores te subirá el salario para poder vivir más cómodamente y pagar tus facturas, si el centro no cumple tus expectativas, siempre puedes escuchar las ofertas de otros centros públicos, y si tu reputación es lo suficientemente atractiva, quizás recibas ofertas de algún centro privado, regentado por otro jugador que valore tu trabajo y, sobre todo, que pague el precio que vales.

El poder trabajar en un centro con mayor prestigio no te dará la posibilidad de aumentar su salario, sino que te brindará la posibilidad de tratar a pacientes más complejos que repercutan un mayor aumento a tu reputación y así poder llegar a ser el mejor médico de la zona, o por que no, del mundo, demuestra tu valía en competiciones periódicas contra otros médicos o ayudando a tu centro en las ilustres competiciones de centros.

**NARRATIVA Y SITUACIÓN:**

El componente narrativo va a ser mínimo, quizás una pequeña historia para introducir al jugador en el juego, durante la progresión natural del juego se podría ir dando pinceladas de esta historia, pero teniendo en cuenta que la situación del jugador fluctúa ampliamente, hay que tener cuidado en cuándo ir dando estas “pinceladas”, porque por ejemplo, un jugador que se esfuerce puede alcanzar un estado en el juego que uno con mucho más tiempo de juego no alcance nunca y si tiene una mala racha poder descender a como estaba a inicios del juego, pensemos que la progresión va unida a la reputación que el médico y esta puede estar en niveles altos o bajos independientemente del tiempo que lleve el jugador en el juego, esta dependerá en gran medida de su habilidad.

**Personajes:**

Continuando con el punto anterior, se puede plantear una historia general, en el que incluya a personajes que ayuden al jugador a modo de tutorial interactivo o unos personajes en los que el jugador puede hablar en cualquier momento y estos le den pistas o ayudas sobre la situación actual del jugador.

**Escenarios:**

El escenario principal será la consulta del médico, en el que el jugador puede acceder a diferentes herramientas, archivos de pacientes, consultar enfermedades conocidas, un teléfono en que contactar con los personajes que se comentaron en el punto anterior, un terminal en el que recoger los datos del paciente actual, mandar pruebas, ver historial, etc.

Está pendiente hacer un boceto sobre la consulta para ver qué elementos introducir y de que forma.

Otros escenarios que el jugador podrá visitar serán:

- Panel de centro médico: Pantalla en el que se podrá observar los detalles del centro médico en el que trabaja actualmente el médico, nivel de reputación, enfermedades que conoce, enfermedades que tiene capacidad de tratar, personal, estado, etc.
- Competiciones: El médico podrá ver el estado en el que quedó en la ultima competición, si es que participó en alguna, si no, se informará que puede inscribirse para la siguiente continuado por todos los detalles necesarios que necesitará saber. De igual manera, si el centro al que pertenece, o del que es propietario, ha competido o está en alguna competición en este momento, podrá ver los detalles y el estado, actual o pasado si ya finalizó.
- Pruebas: Habrá que desarrollar los escenarios para las diferentes pruebas, en los que a modo de mini-juego (aún por determinar el tipo) el médico podrá interpretar las pruebas realizadas al paciente y así poder saber la enfermedad que padece el paciente y decantarse por un tratamiento u otro.
ARTE Y DISEÑO VISUAL:

Aún por concretar.

**SONIDO Y MÚSICA:**

Se ha pensado en una pequeña melodía de fondo y sonidos para las acciones ¿Se podría hacer esto con alguna IA?

# DESCRIPCIÓN DE MECÁNICAS PROPUESTAS:

A continuación, se detalla las mecánicas que se han pensado, estas pueden cambiar, eliminar o añadirse nuevas durante los siguientes procesos de desarrollo:

- Cómo médico podrás trabajar como temporal en un centro médico de diferentes niveles dependiendo de tu reputación.
- La reputación se calculará sobre toda la carrera del médico:
- Habrá dos reputaciones, la Global (de toda la carrera) y de temporada (que solo contendrá la temporada actual y se resetea al cambiar de temporada), al terminar la temporada el resultado de esta tendrá recompensas que afectarán a la reputación Global
- Cómo médico tendrás tu reputación (dos como se comentaba en el punto anterior) pero también existe la reputación del centro al que pertenezca el médico
- Las pruebas disponibles para los pacientes vendrán dictadas por el nivel del centro médico al que pertenezca el jugador.
- Las pruebas costarán dinero (No real) que pagará el médico que las mande.
- El médico obtendrá dinero de los pacientes cuándo estos se recuperen de la enfermedad que padecían o con paquetes que se podrán comprar (con dinero real), adicionalmente el médico obtendrá un salario periódico que pagará el centro al que pertenece, el médico puede obtener ascensos, cambiar de centro o renegociar su situación en su actual centro.
## PACIENTES:

Habrá diferentes tipos de paciente:

- Común: Este paciente no tiene seguro médico y costea él mismo su tratamiento, siempre que se recupere.
- Común +: Paciente con seguro médico, el seguro se hará cargo de los costes del tratamiento y pruebas si este se recupera, o si fallece. Si no se recupera de su enfermedad, pero el paciente no fallece el seguro no pagará nada.
- VIP: Paciente que pagará el tratamiento y pruebas al momento (Coste + pequeño plus), si se recupera pagará un plus por el proceso completo, pero si no, habrá una penalización de reputación mayor que con los otros tipos de pacientes.
- Especial: Paciente con características especiales, cómo podrían ser los pacientes de algunos eventos.
ENFERMEDADES

- Cada nivel de centro viene provisto de un nivel de enfermedades (NE) (¿Como un pack de enfermedades?), si por ejemplo un centro tiene un NE de 4, este podrá actuar sobre enfermedades de nivel 4 e inferiores, aunque un centro puede recibir pacientes con una enfermedad de nivel superior al del centro, por las que el centro no la conoce o no puede tratarlas con seguridad.
- Cada enfermedad tiene unas pruebas idóneas para su diagnóstico, hacer pruebas aumentará el coste global del tratamiento, las pruebas idóneas acercarán más al médico al diagnóstico, las pruebas neutrales acercarán menos que las idóneas y las no recomendadas pueden dar pistas sobre un tratamiento erróneo.
- Cada pista dadas por las pruebas o dato facilitado por el paciente aumentará el % de la posible cura y cuánto más alto sea este % dará una sugerencia mas acertada sobre cuál es la posible cura.
- El médico podrá decidir en cualquier momento mandar al paciente una posible cura.
- Un tipo de cura, por ejemplo, un jarabe para la tos, puede tener diferentes variables, tener un % más alto sobre la “posible cura” ayudará a saber que variante es la mejor para cada caso.
- Cada NE puede contener alguna enfermedad que se tenga que estudiar para conocer todos sus detalles.
CURAS

- Tipos:
- Farmacéuticas: Jarabes, pastillas, suplementos vitamínicos…
- Quirúrgicas: Pueden ir por nivel de peligrosidad.
- Nucleares: Quimioterapia, Radioterapia, Inmunoterapia…
- Especiales: Curas para enfermedades raras, o experimentales.
- Las curas pueden ser aplicadas de tres formas dependiendo el tipo:
- Se lo aplica el paciente (como puede ser un jarabe que el paciente se lo aplica en su propia casa).
- Al momento (cirujías).
- Periódicas: El paciente tendrá que acudir de forma periódica al centro para su tratamiento.
MÉDICO

- El médico empezará trabajando en un centro público, con reputación 0 y bajo salario.
- En cuánto gane algo de reputación podrá trabajar para otros centros, pedir aumento, renegociar salario o incluso pasar un centro médico privado (se explican más adelante).
- El médico podrá realizar tests o titulaciones para poder subir su reputación (hasta cierto nivel de reputación, esto se ha pensado para aquellos jugadores con cierto nivel que han pedido gran parte de su reputación por alguna mala decisión o circunstancia, así aunque no recuperarán como estaban, al menos algo si).

## CENTROS

- Tipos:
- Públicos:
- Centro médico: En este tipo de centros el médico no se encarga de nada más allá de hacer pruebas y dictar tratamientos, si cree que no puede tratar esta enfermedad, puede mandar al paciente a un hospital público o privado, si este paciente se cura en este hospital, recibirá una recompensa, si el centro al que lo manda es privado, la recompensa será mayor.
- En estos centros se obtiene poca recompensa de reputación, poco salario, si el médico toma malas decisiones la reputación solo puede disminuir hasta cierto nivel, pero nunca a 0.
- Los centros tienen su nivel de reputación y NE.
- Hospital: Tras llegar a cierta reputación el médico podrá ser contratado por unos de estos centros, su NE más bajo siempre será superior al de un Centro Médico normal, en este tipo de centros el médico obtendrá mayores recompensas
- Privados:
- Los centros privados están administrados por otros jugadores, los salarios que se pagan a los médicos no están regulados, por lo que cada médico tendrá que negociar el suyo con el centro, como pasa con los públicos cada uno tiene su NE y el de los hospitales siempre será superior al de los centros médicos.
Los jugadores podrán crear y gestionar su propio centro médico, ya sea centro o hospital, esta posibilidad se dará cuándo el jugador llegue a cierto nivel de reputación y aparte le costará dinero poder construirlo, un jugador que no vea rentable un centro o quiera construir otro, se está estudiando las posibilidades para que esto pase, podrá venderlo a otro jugador o abandonarlo, cuando un jugador quiera hacer su propio hospital se le brindará la opción de comprar el de otro jugador o coger un hospital abandonado y reconstruirlo.

La gestión del centro médico o hospital tendrá diferentes opciones dependiendo del tipo y nivel, todos tendrán un coste periódico que deberá pagar el administrador del centro.

El centro repercutirá beneficios al administrador por curaciones realizadas satisfactoriamente, venta de bebida y comida, alquiler de alguna instalación a otro centro, aceptar eventos en su hospital, etc.

## COMPETICIONES:

Se han pensado tres tipos de competiciones (nombre provisional)

- Individual: Cada jugador podrá participar como competidor individual.
- En Grupo o Equipo de Médicos: Como parte de un equipo de doctores, el jugador unirá sus esfuerzos a otros jugadores (irá por número de participantes), los equipos se crearán los propios jugadores, uno creará el equipo y enviará invitaciones a otros para unirse o se anunciará en algún tablón para que otros que busquen equipo se puedan unir.
- Por Centros: Para estas competiciones, el jugador debe poseer un centro o ser parte de uno.
En principio los objetivos a cumplir serán parecidos entre sí, conforme se vayan ganando o perdiendo se subirá o bajará de rango, la recompensa se dividirá entre los participantes en caso de quipo y si es de centro será el administrador de este el que decidirá la repartición de las recompensas, las recompensas pueden ser (uno o más):

- Dinero.
- Reputación.
- Objetos.
- Boosts
