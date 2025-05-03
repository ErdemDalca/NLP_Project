# Dinosaurio: La aventura de las Monedas Perdidas

## GAME DESIGN DOCUMENT

Creado por: Nerea Trillo Pérez

Versión del documento: 2.0

## HISTORIAL DE REVISIONES

| Versión | Fecha | Comentarios |
| --- | --- | --- |
| 1.0 | 22/03/2024 | Documento inicial creado y secciones del resumen completadas. |
| 1.1 | 30/03/2024 | Diseño completado. |
| 1.2 | 31/03/2024 | Inicio del desarrollo de las Mecánicas de juego. |
| 1.3 | 09/04/2024 | Inicio y finalización de los Detalles Técnicos y del Audio. |
| 1.4 | 19/04/2024 | Inicio de la creación de la sección de Arte, faltan sprites y animaciones. |
| 1.5 | 21/04/2024 | Comienzo del desarrollo del Mundo del Juego. |
| 1.6 | 21/04/2024 | Se completó la sección de HUD y personajes, a excepción de las imágenes de los enemigos que están pendientes. |
| 1.7 | 23/04/2024 | Se completó el Mundo del Juego, aunque aún faltan algunas imágenes. |
| 1.8 | 24/04/2024 | Continuación de las Mecánicas del juego. |
| 1.9 | 28/04/2024 | Sección Arte y Mundo del Juego completados con las imágenes faltantes, Física del juego completado y desarrollo de la mecánica del juego|
| 2.0 | 29/04/2024 | GDD completado|

## RESUMEN

### Concepto

> Dinosaurio: La aventura de las Monedas Perdidas es un emocionante juego de plataformas 2D donde los jugadores asumen el papel de un valiente dinosaurio en su misión de recolectar las monedas perdidas. A través de 3 niveles desafiantes, los jugadores deben navegar por terrenos difíciles, evitar obstáculos y superar enemigos para avanzar.

### Puntos Clave

> **1. Personaje Principal**: El jugador controla a un dinosaurio en un mundo 2D de plataformas.
> **2. Objetivo**: El objetivo principal es recoger todas las monedas en cada nivel para avanzar al siguiente.
> **3. Movilidad**: El dinosaurio puede moverse hacia la izquierda y la derecha, subir y bajar escaleras, y saltar.
> **4. Enemigos y Trampas**: Hay enemigos móviles y trampas estáticas y móviles que pueden quitarle vida al dinosaurio.
> **5. Checkpoints**: Los checkpoints guardan el progreso del jugador, incluyendo las monedas recogidas, en caso de muerte.

### Género

> Plataformas, Aventura.

### Público Objetivo

> El juego está dirigido a jugadores de todas las edades que disfrutan de los juegos de plataformas y aventuras. No se requiere ninguna habilidad especial para jugar, por lo que es adecuado tanto para jugadores novatos como para los más experimentados. Los jugadores que disfrutan de juegos como “Super Mario Bros.” y “Donkey Kong” podrían encontrar este juego interesante.

### Experiencia de Juego

> En este juego de plataformas 2D, el jugador se embarcará en una aventura emocionante controlando a un dinosaurio. Desde el momento en que el jugador entra en el mundo del juego, se encontrará inmerso en un entorno lleno de desafíos y recompensas.
>
>Visualmente, el jugador se encontrará en un mundo vibrante y colorido, lleno de plataformas para saltar,escaleras para subir y bajar terrenos, rampas, monedas para recoger y enemigos para evitar. El dinosaurio, controlado por el jugador, se moverá fluidamente por el escenario para recoger todas las monedas.
>
>Auditivamente, el jugador estará acompañado por una música de fondo que complementa la acción en pantalla. Los efectos de sonido, como el sonido de las monedas al ser recogidas o el sonido de los enemigos al ser derrotados, añadirán una capa adicional de inmersión a la experiencia de juego.
>
>En cuanto a la interactividad, el jugador tendrá un control total sobre el dinosaurio. Podrá moverse a la izquierda y a la derecha, subir y bajar escaleras, saltar para superar obstáculos y recoger monedas. Además, el jugador deberá evitar a los enemigos, las trampas y no caerse al vacío para no perder vidas.
>
>A lo largo del juego, el jugador se enfrentará a niveles cada vez más difíciles, pero también tendrá la satisfacción de ver cómo su contador de monedas aumenta y cómo supera cada nivel. Y si en algún momento el juego se vuelve demasiado desafiante, el jugador siempre puede pausar el juego y retomarlo más tarde.
>
>En resumen, este juego ofrece una experiencia de juego emocionante y gratificante, llena de acción, desafíos y recompensas. ¡Es hora de saltar al mundo del juego y empezar a recoger esas monedas!

## DISEÑO

### Metas de Diseño

> **- Simplicidad**: El juego se centra en la simplicidad, tanto en su mecánica como en su diseño. La meta es mantener un juego fácil de entender y jugar, pero desafiante para completar. Esto se logrará manteniendo las reglas y controles simples, y diseñando niveles que requieran habilidad para superar.
>
>**- Progresión**: La meta es que los jugadores sientan una sensación de progresión a medida que avanzan en el juego. Esto se logrará a través de la recolección de monedas y la superación de niveles.
>
>**- Inmersión**: Queremos que los jugadores se sientan inmersos en el mundo del juego, a través de un diseño de niveles cuidadoso y una estética coherente.
>
>**- Retroalimentación**: Es importante que los jugadores reciban retroalimentación constante sobre su rendimiento. Para ello se contará con un contador de vidas y monedas, así como respuestas visuales y sonoras a las distintas acciones del jugador.
>
>**- Rejugabilidad**: La meta es que los jugadores quieran volver a jugar una y otra vez. Mediante una variedad en el diseño de los niveles y la inclusión de elementos de desafío, como trampas y enemigos.
>
>**- Accesibilidad**: Queremos que el juego sea accesible para todos los jugadores, independientemente de su habilidad, por eso se utilizaron controles intuitivos y una curva de dificultad bien equilibrada.
>
>**- Diversión**: La meta final, por supuesto, es que los jugadores se diviertan. Por eso esl diseño del juego está centrado en la diversión, en lugar de la frustración. La diversión se fomentará a través de la exploración, la recolección de monedas, y la satisfacción de superar los desafíos para superar los niveles.

## MECÁNICAS DE JUEGO

### Núcleo de Juego

>En este juego de plataformas 2D el jugador encarnará a un simpático dinosaurio cuya misión es recoger todas las monedas dispersas por los niveles para avanzar. Con un enfoque puro en la diversión y la exploración, el juego no presenta enemigos a derrotar ni objetos ocultos que complicarían la experiencia. El objetivo es simple: disfrutar de la acción de saltar y recoger monedas mientras exploras coloridos escenarios.
Controlas al dinosaurio con las teclas de dirección, moviéndolo hacia la izquierda y hacia la derecha, y haciendo uso de la tecla de espacio para saltar. Con estas habilidades básicas, te embarcarás en una aventura donde la agilidad y la precisión son tus mejores aliados.
Cada nivel es como un mundo propio, lleno de vida y sorpresas.Cada nivel está diseñado con cuidado, presentando una variedad de plataformas y obstáculos que desafiarán tus habilidades de salto y tu destreza, desde simples plataformas hasta trampas mortales como pinchos, el terreno está lleno de desafíos que pondrán a prueba tus reflejos y tu capacidad de adaptación.
A medida que avanzas a través de los niveles, te encuentras con nuevas y emocionantes mecánicas de juego. Los primeros niveles son como un suave paseo por el parque, donde te familiarizas con los controles y te acostumbras al ritmo del juego. Sin embargo, a medida que te adentras en territorio desconocido, los desafíos se vuelven más difíciles y exigentes, como trampas móviles y enemigos más numerosos, los cuales puedes matar saltándoles encima, lo que requiere que el jugador mejore sus habilidades de navegación y timing de saltos para superarlos. Sin embargo, el juego mantiene su enfoque en la diversión y la accesibilidad, evitando picos de dificultad excesivos que puedan frustrar al jugador.
Las monedas brillantes son el objetivo principal de cada nivel. Al recoger todas las monedas de un nivel, desbloqueas automáticamente el siguiente, sin necesidad de realizar ninguna acción adicional. Esto incentiva la exploración y la búsqueda de cada rincón del nivel para asegurarte de no dejar ninguna moneda atrás.
Para ayudarte en tu aventura, un contador de vidas te informa sobre cuántas oportunidades tienes antes de que el juego termine. Comienzas con tres vidas, y cada vez que caigas en una trampa mortal, te dañe un enemigo o caigas al vacío, perderás una vida. Mantén un ojo en tu contador de vidas para asegurarte de conservarlas hasta el final.
Además, un contador de monedas te ofrece una visión clara de tu progreso en cada nivel.Cada vez que recoges una moneda, el contador se actualiza, indicándote cuántas monedas has recolectado de las totales disponibles en el nivel. Esta herramienta es invaluable para rastrear tu progreso y asegurarte de no pasar por alto ninguna moneda en tu búsqueda del éxito. Esta herramienta es útil para saber si has pasado por alto alguna moneda y te ayuda a rastrear tu progreso en la recolección de monedas.
El juego también cuenta con un sistema de checkpoints que te permite reiniciar desde un punto específico del nivel en caso de que pierdas una vida. Estos checkpoints te dan un respiro y evitan que tengas que repetir secciones completas del nivel cada vez que falles.
Finalmente, el tercer nivel introduce un nuevo elemento, en forma de unas escaleras, que agregan un nuevo nivel de verticalidad al diseño de los niveles. Debes dominar tus habilidades de salto y precisión para superar estos nuevos desafíos y alcanzar la meta.
El juego no posee un sistema de puntuaje, ni unas reglas de combate.

### Flujo de Juego

> **Inicio**: El jugador inicia el juego desde el menú principal. Aquí, puede ajustar las opciones de sonido o comenzar el juego.
**Instrucciones**: Al seleccionar “comenzar”, el jugador es llevado a una pantalla de instrucciones que explica brevemente los controles y el objetivo del juego. Para empezar el nivel, el jugador presiona la tecla “Enter”.
**Nivel 1**: El jugador comienza el primer nivel con 3 vidas y 0 monedas. El objetivo es recoger todas las monedas en el nivel mientras evita trampas y enemigos.
**Checkpoints**: Si el jugador pasa por un checkpoint, se guarda la posción del jugador y el número de monedas recogidas si muere, por lo que no tendría que volver a recoger las que ya tenía.
**Pérdida de vida**: Si el jugador cae al vacío, toca una trampa, o es tocado por un enemigo, pierde una vida. Si pierde una vida, la escena se recarga y el jugador aparece en el último checkpoint activado con las monedas que tenía en ese momento.
**Game Over**: Si el jugador pierde todas sus vidas, se muestra la pantalla de Game Over con la opción de comenzar de nuevo o volver al menú. Si elige comenzar de nuevo, siempre comienza desde el nivel 1.
**Pasar de nivel**: Si el jugador recoge todas las monedas en un nivel, se desbloquea automáticamente el siguiente nivel.
**Niveles 2 y 3**: Los niveles 2 y 3 funcionan de la misma manera que el nivel 1, pero con diferentes diseños de nivel y posiblemente con más desafíos.
**Fin**: Si el jugador completa todos los niveles, se muestra una pantalla de victoria (Fin).
![Flujo de diagrama](/Doc/Imagenes/flujo_diagrama.png)

### Fin de Juego

>**Derrotas**:
>
>- Pérdida de todas las vidas: Si el jugador pierde todas sus vidas, ya sea por caer al vacío, tocar una trampa o ser tocado por un enemigo, el juego termina. Se muestra la pantalla de Game Over con la opción de comenzar de nuevo o volver al menú principal.
>
>**Victorias**:
>
>- Completar todos los niveles: Si el jugador recoge todas las monedas en cada nivel y logra superar los tres niveles, se considera que ha ganado el juego. Se muestra una pantalla de victoria y luego se acaba el juego.
>
>**Otras situaciones**:
>
>- Pausa del juego: Si el jugador presiona la tecla “P” durante el juego, este se pausa. Puede reanudar el juego presionando “P” nuevament.
>- Salir del juego: En cualquier momento, el jugador puede presionar la tecla “ESC” para salir del juego. Esto también se considera una conclusión de la partida.

### Física de Juego

> La física del juego se centra en simular el movimiento y la interacción de los personajes (principalmente el dinosaurio jugador) con el entorno del juego, incluidas las plataformas, las monedas y las trampas. Esto se logra mediante el uso de RigidBodies, colliders y fuerzas básicas como la gravedad y la aplicación de fuerzas de movimiento.
Al **Dinosaurio** se le aplica la física de movimiento básico, controlado por las teclas de dirección (<- y ->).
La física de salto se activa con la tecla de espacio, con una fuerza vertical que contrarresta la gravedad y permite al jugador saltar sobre obstáculos y alcanzar plataformas elevadas. Se utiliza un RigidBody para simular la masa del dinosaurio y permitir que interactúe con otros objetos y obstáculos en el juego, como las plataformas y las trampas, y sin fricción. Los colliders se utilizan para detectar colisiones con objetos en el mundo del juego, como las monedas, los enemigos y los elementos del entorno, como las plataformas y las trampas.
En los otros personajes, los **enemigos**, que son insectos, tienen una física de movimiento simple, como patrullar de un lado a otro en una plataforma o terreno. No se les aplica RigidBody, ya que no necesitan simular masa ni interactuar con la física del entorno de la misma manera que el dinosaurio. En cuanto a los demás objetos como monedas, plataformas, escaleras, etc, no tienen una física compleja, ya que no necesitan moverse ni hacer ninguna otra función, que no sea interactuar con el jugador, por eso tienen colliders.

### Controles

>**DURANTE PARTIDA**:

| **Acción** | **Tecla** |
| --- | --- |
| Mover el dinosaurio hacia la izquierda | Flecha izquierda (<-) |
| Mover el dinosaurio hacia la derecha | Flecha derecha (->) |
| Hacer saltar al dinosaurio | Barra espacio |
| Pausar el juego | P |
| Reiniciar partida después de Game Over | Intro |
| Volver al Menú después de Game Over | M |
>**EN EL MENÚ:**

| **Acción** | **Tecla** |
| --- | --- |
| Navegar hacia arriba en el menú  | Flecha arriba (↑) |
| Navegar hacia abajo en el menú | Flecha abajo (↓) |
| Seleccionar la opcion resaltada | Barra espacio |
>**EN EL MENÚ DE OPCIONES:**

| **Acción** | **Tecla** |
| --- | --- |
| Navegar hacia arriba en el menú  | Flecha arriba (↑) |
| Navegar hacia abajo en el menú | Flecha abajo (↓) |
| Disminuir volumen | Flecha izquierda (<-) |
| Aumentar volumen | Flecha derecha (->) |
| Seleccionar la opcion resaltada  | Barra espacio |

## MUNDO DEL JUEGO

### Descripción General

> El juego se desarrolla en un mundo vibrante y colorido, lleno de vida y energía. El entorno es un paisaje de plataformas 2D que se extiende en todas las direcciones, con un cielo azul brillante arriba y un suelo sólido debajo. El mundo está lleno de plataformas flotantes, trampas y monedas brillantes que el jugador debe recoger.
>
>El personaje principal es un dinosaurio adorable y ágil que se mueve con gracia, su objetivo es recoger todas las monedas en cada nivel para avanzar al siguiente. El dinosaurio puede moverse hacia la izquierda y hacia la derecha usando las teclas de flecha y puede saltar con la tecla de espacio.
>
>El mundo está lleno de desafíos, pero no hay enemigos que derrotar ni objetos ocultos que encontrar. El objetivo principal es simplemente disfrutar del viaje y completar cada nivel recogiendo todas las monedas, las cuales están dispersas por todo los niveles. Un contador en la pantalla muestra las vidas del jugador (comenzando con 3) y la cantidad de monedas recogidas en cada nivel.
>
>El juego tiene un menú con opciones para comenzar el juego, ajustar el volumen (de la musica y sonidos) y salir. También hay una escena de instrucciones con texto que guía al jugador a través de los controles y objetivos del juego.
>
>El juego consta de tres niveles, cada uno con su propio conjunto de imágenes y sprites. Los elementos visuales incluyen el dinosaurio, dos tipos de enemigos que son insectos, monedas para recoger, terreno y plataformas creadas con sprites y tilemaps, trampas estáticas y móviles, y varios elementos de decoración. En el nivel 3, se añade un nuevo sprite de escaleras.
>
>La última escena, a la que solo se llega si se pasan todos los niveles, muestra una imagen de una copa con el texto “Winner” que cambia de tamaño y de color de blanco a amarillo, con destellos en forma de estrella saliendo de la copa.
>
>Las animaciones incluyen a los enemigos moviéndose, el dinosaurio saltando y moviéndose, y la copa “Winner” girando sobre sí misma. Las monedas también tienen una animación en la que giran sobre sí mismas.
>
>El juego tiene un estilo visual atractivo, con gráficos coloridos y detallados. Los fondos son imágenes en paralaje que dan una sensación de profundidad y movimiento al mundo del juego.
>
>El sonido y la música del juego también juegan un papel importante en la creación de la atmósfera del juego. Los efectos de sonido proporcionan retroalimentación inmediata a las acciones del jugador, y la música de fondo establece el tono y el ritmo del juego.

### Personajes

>Este juego solo tiene 2  de personajes:
>
>1. **Jugables**: Dinosaurio (Jugador). Este es el personaje principal del juego, controlado por el jugador. Es un dinosaurio que se mueve con las teclas de flecha y salta con la tecla de espacio. Su objetivo es recoger todas las monedas en cada nivel para avanzar al siguiente. No tiene habilidades especiales más allá de moverse y saltar.
![Dinosaurio](/Doc/Imagenes/dinosaurio.png)
>3. **Enemigos**: No atacan al dinosaurio, pero su presencia puede ser un obstáculo para el dinosaurio, ya que si tocan al jugador le resta una vida. No tienen habilidades especiales. Destacamos dos tipos de enemigos, los insectos marrones y los verdes.
![Enemigos](/Doc/Imagenes/Animaciones/enemigo1Animacion.gif)
![Enemigos](/Doc/Imagenes/Animaciones/enemigo2Animacion.gif)

### Objetos

>Los objetos con los que el juagdor (dinosaurio) puede interactuar, es decir, recogr, activar o usar son:
>
>1. **Monedas (Coins)**
*Interfaz*: Representadas como pequeñas monedas brillantes dispersas por el nivel. El dinosaurio las recoge al pasar sobre ellas, sin necesidad de activación adicional.
>
>2. **Checkpoint**
*Interfaz*: Representado como una roca que es punto de guardado en el nivel. Al pasar sobre él, el dinosaurio activa el checkpoint (el cual cambia de color) para guardar su progreso en el juego.
>
### Flujo de Pantallas

>El juego se compone de varias pantallas interconectadas, cuya interacción se representa en el diagrama de flujo adjunto.![Diagrama](/Doc/Imagenes/diagrama_flujo_pantallas.png)
>
>**Pantalla de Menú**
La experiencia del juego comienza en la Pantalla de Menú, que se presenta sobre un fondo que evoca un cielo, un bosque y una plataforma, similar al entorno de los niveles del juego. Esta pantalla presenta al jugador tres opciones: “Salir”, “Comenzar” y “Opciones”. Para moverse por esta pantalla se usan las flechas del teclado y para seleccionar una opción la tecla “Return”. Al seleccionar “Opciones”, el jugador es dirigido a la Pantalla de Opciones. Al elegir “Comenzar”, el jugador es llevado a la Pantalla de Instrucciones.![Menu](/Doc/Imagenes/Pantallas/pantalla%20menu.png)
>
>**Pantalla de Opciones**
En esta pantalla, el jugador tiene la oportunidad de personalizar su experiencia de juego. Aquí, es posible ajustar el volumen de la música y los efectos de sonido del juego. Los controles son consistentes con los de la Pantalla de Menú, y además, se incluye un botón de “Volver”, que permite al jugador regresar a la Pantalla de Menú en cualquier momento.![Opciones](/Doc/Imagenes/Pantallas/menOpciones.png)
>
>**Pantalla de Instrucciones**
La Pantalla de Instrucciones proporciona al jugador las instrucciones del juego y los controles que se tienen que usar, todo presentado en formato de texto e imagenes, y se presenta sobre el fondo del cielo usado en las demás pantallas. Para iniciar la partida y avanzar a la Pantalla del Nivel 1, el jugador debe presionar la tecla “Return”.![Instrucciones](/Doc/Imagenes/Pantallas/pantalla%20instrucciones.gif)
>
>**Pantalla de Nivel 1,2,3**
El juego consta de tres niveles distintos, cada uno con su propio diseño y desafíos únicos. La acción comienza en la Pantalla del Nivel 1, donde el jugador se encuentra con un entorno lleno de plataformas, trampas, enemigos, monedas y elementos ambientales. También se muestran contadores de vida y de monedas, proporcionando al jugador información crucial durante el juego. Este tipo de entorno se mantiene en todos los niveles.
En cada nivel, el objetivo principal del jugador es recolectar todas las monedas disponibles, lo que le permitirá avanzar al siguiente nivel. Sin embargo, si el jugador agota todas sus vidas el juego llegará a su fin, en este punto, se mostrará el mensaje “GameOver” y se le ofrecerá al jugador la opción de reiniciar la partida, lo que le llevará de vuelta a la Pantalla del Nivel 1, independientemente del nivel en el que se encontraba cuando ocurrió el GameOver, o volver a la pantalla Menú.
En la Pantalla del Nivel 3, una vez que el jugador ha recolectado todas las monedas, se le permitirá avanzar a la Pantalla Final.![Nivel](/Doc/Imagenes/Pantallas/escenaNivel.png)
>
>**Pantalla Final**
La Pantalla Final celebra el éxito del jugador mostrando una imagen de una copa con destellos y el texto “Winner”, que se va agrandando y cambiando de color.
>![PantallaFinal](/Doc/Imagenes/Pantallas/pantalla%20winner.gif)

### HUD

>El HUD (Heads-Up Display) en este juego de plataformas 2D con un dinosaurio es bastante sencillo y directo, lo que permite a los jugadores concentrarse en la acción del juego. Aquí está la descripción de los elementos del HUD durante el desarrollo de la partida:
>
>- **Contador de Vidas**: Este es un elemento crucial del HUD. Muestra el número de vidas que le quedan al jugador (comienza con 3). Cada vez que el jugador pierde una vida, este número disminuye. Cuando llega a cero, se produce un GameOver, se finaliza esa partida. Su propósito es informar al jugador cuántas oportunidades le quedan para completar el nivel.
>
>- **Contador de Monedas**: Este elemento muestra el número de monedas que el jugador ha recogido en el nivel actual, así como el número total de monedas en ese nivel (por ejemplo, “5/20”). Su propósito es informar al jugador cuántas monedas ha recogido y cuántas le faltan para completar el nivel y pasar al siguiente.

## ARTE

### Metas de Arte

>Los objetivos que se quieren lograr son las de crear un ambiente visualmente atractivo y amigable que sea coherente con la simplicidad y accesibilidad del juego, asegurar que los elementos visuales sean claros y fácilmente identificables identificables para facilitar la jugabilidad e implementar un diseño artístico que sea ccoherente en todos los niveles del juego, ofreciendo una experiencia visual fluida.
>
>**Estilo de Arte y Concepto Visual**:
>El estilo de arte es pixelado, reminiscente de los juegos clásicos de plataformas, pero con un toque moderno en la calidad gráfica. Los colores son vibrantes pero no saturados, creando un equilibrio visual que es agradable a la vista.
El concepto visual se centra en la simplicidad; cada elemento está diseñado para ser inmediatamente reconocible y funcional.
>
>**Apariencia General de Escenarios y Personajes:**
>
>- **Escenarios**: Los escenarios son sencillos pero detallados, con terrenos texturizados y fondos parallax para añadir profundidad. Las monedas están claramente visibles contra el fondo, y las trampas son identificables para evitarlas fácilmente.
>![Escenario](/Doc/Imagenes/Escenario.png)
>
>- **Personajes**: El dinosaurio jugador tiene un diseño caricaturesco con colores verdes suaves. Es expresivo pero simple, facilitando la identificación inmediata por parte del jugador.
![Dinosaurio](/Doc/Imagenes/dinosaurio.png)
>Los enemigos, representados por insectos marrones y verdes, tienen un diseño simple pero efectivo que los hace fácilmente reconocibles, tienen cabeza, cuerpo y patas y se mueven.
![Enemigo](/Doc/Imagenes/Animaciones/enemigo1Animacion.gif)
![Enemigo](/Doc/Imagenes/Animaciones/enemigo2Animacion.gif)

### Assets de Arte

>1. *Menú Principal*:
>
>- Imágenes de texto para las opciones:
>
>   1. “Titulo del juego”
![Titulo](/Doc/Imagenes/MenuPrincipal/Titulo.png)
>   2. “Comenzar”:
**activo**:
![Comenzar](/Doc/Imagenes/MenuPrincipal/Comenzar_On.png)
**inactivo**:
![Comenzar](/Doc/Imagenes/MenuPrincipal/Comenzar_Off.png)
>   3. “Opciones”:
**activo**:
![Opciones](/Doc/Imagenes/MenuPrincipal/Opciones_On.png)
**inactivo**:
![Opciones](/Doc/Imagenes/MenuPrincipal/Opciones_Off.png)
>   4. “Salir”:
**activo**:
![Salir](/Doc/Imagenes/MenuPrincipal/Salir_On.png)
**inactivo**:
![Salir](/Doc/Imagenes/MenuPrincipal/Salir_Off.png)
>   5. “Titulo de Opciones”:
![TituloOpc](/Doc/Imagenes/MenuPrincipal/TituloOpciones.png)
>   6. “Musica”:
**activo**:
![Musica](/Doc/Imagenes/MenuPrincipal/Musica_on.png)
**inactivo**:
![Musica](/Doc/Imagenes/MenuPrincipal/Musica_off.png)
>   7. “Sonido”:
**activo**:
![Sonido](/Doc/Imagenes/MenuPrincipal/Sonido_On.png)
inactivo**:
![Sonido](/Doc/Imagenes/MenuPrincipal/Sonido_Off.png)
>   8. “Volver”:
**activo**:
![Volver](/Doc/Imagenes/MenuPrincipal/Volver_On.png)
**inactivo**:
![Volver](/Doc/Imagenes/MenuPrincipal/Volver_Off.png)
>
>- Imágenes con barras para ajuste de volumen
**activo**:
![Vol](/Doc/Imagenes/MenuPrincipal/Vol_On.png)
**inactivo**:
![Vol](/Doc/Imagenes/MenuPrincipal/Vol_off.png)
>- Imagen con una “X” para indicar sonido/música apagado
>![SinVol](/Doc/Imagenes/MenuPrincipal/VolX.png)
>
>2. *Jugador (Dinosaurio)*:
>
>- Sprite del dinosaurio
![Dino](/Doc/Imagenes/dinosaurio.png)
>- Animación de muerte
>![Muerte](/Doc/Imagenes/Animaciones/AnimMuerte.png)
>- Animación al moverse
>- Animación de salto
>![Moverse](/Doc/Imagenes/Animaciones/AnimDino.gif)
>
>3. *Enemigos*:
>
>- Sprite de insecto marrón
![enemigo Marrón](/Doc/Imagenes/Animaciones/enemigo2Animacion.gif)
>- Sprite de insecto verde
![enemigo Verde](/Doc/Imagenes/Animaciones/enemigo1Animacion.gif)
>- Animaciones correspondientes a los movimientos
>
>4. *Objetos Coleccionables y HUD*:
>
>- Sprites de monedas
>![Monedas](/Doc/Imagenes/Monedas.png)
>- Animación giratoria de las monedas
>![AnimacionMoneda](/Doc/Imagenes/Animaciones/AnimaMonedas.gif)
>- Contador con las vidas del jugador (imagen)
>![BarraSalud](/Doc/Imagenes/BarraSalud.png)
>- Contador de monedas recogidas/total (imagen)
>![Contador monedas](/Doc/Imagenes/contador%20monedas.png)
>
>5. *Entorno y Plataformas*:
>
>- Terreno y plataformas (sprites usados con tilemaps)
![Terreno](/Doc/Imagenes/Terreno.png)
>
>6. *Trampas*:
>
>- Pincho quieto (sprite)
![Pincho](/Doc/Imagenes/Trampas/pinchos.png)
![Mazo](/Doc/Imagenes/Trampas/Mace.png)
>- Pincho móvil (sprite)
![PinchoMovil](/Doc/Imagenes/Trampas/pinchoMovil.png)
>
>7. *Decoraciones y Fondos*:
>
>- Señalización sobre muerte (sprite)
![Señal Peligro](/Doc/Imagenes/Decoracion/señal.jpg)
>- Flores decorativas (sprites)
![FloresAarillas](/Doc/Imagenes/Decoracion/florAmar.png)
![FloresRojas](/Doc/Imagenes/Decoracion/Flower-3.png)
>- Imágenes en parallax para el fondo del juego
![FondoLejos](/Doc/Imagenes/FondoLejos.png) ![FondoMedio](/Doc/Imagenes/FondoMedio.png)
>- Degradado negro para caída al vacío
![Degradado](/Doc/Imagenes/DegradadoCaida.png)
>
>8. *Checkpoint*:
>
>- Imagen checkpoint inactivo
>![Checkpoint](/Doc/Imagenes/CheckPointInactivo.png)
>- Imagen checkpoint activo
>![Chheckpoint](/Doc/Imagenes/checkPointActivo.png)
>
>9. *Nivel Específico – Nivel Tres*:
>
>- Sprite nuevo, escaleras
>![Escalera](/Doc/Imagenes/escalera.jpg)
>
>10. *Escena Final*:
>
>- Animación copa girando
>![Copa](/Doc/Imagenes/Animaciones/AnimCopa.gif)
>

## AUDIO

### Metas de Audio

> El enfoque musical y sonoro del juego se centra en mejorar la experiencia del jugador y aumentar la inmersión en el mundo del juego. La música de fondo establece el tono y el ambiente del juego, mientras que los efectos de sonido proporcionan retroalimentación inmediata a las acciones del jugador y refuerzan la interactividad del juego.
>El objetivo general del audio en el juego es complementar la jugabilidad y la narrativa, creando una experiencia cohesiva y envolvente. Esto, se logró a través de una cuidadosa selección y diseño de la música y los efectos de sonido, asegurándonos de que cada elemento de audio se alinee con el tema y el estilo del juego.
>
> - **Música**: *La música es ambiental y evocadora, diseñada para complementar la estética del juego sin distraer al jugador. La música de fondo establece el tono y el ambiente del juego, ayudando a sumergir al jugador en el mundo del juego*.
>
> - **Efectos de sonido**: *Los efectos de sonido son claros y distintivos, proporcionando una retroalimentación táctil a las acciones del jugador. Estos sonidos refuerzan la interactividad del juego y mejoran la experiencia del jugador. Los sonidos incluyen efectos para cuando el jugador muere, salta, recibe daño, mata a un enemigo, recoge una moneda, y activa un checkpoint. Cada uno de estos sonidos están diseñados para proporcionar retroalimentación inmediata a las acciones específicas del jugador, ayudando a hacer que el juego sea más reactivo y satisfactorio*.

### Assets de Audio

> Aquí está la lista ordenada de todos los audios incluidos en el juego:
>
>**Música**:
>Música de fondo del juego: [Música de Fondo](/Doc/Sonidos/sfx_fondo.wav)
>**Sonidos**:
>
>- *Sonidos del jugador*:
>
>   1. Sonido de muerte:  [Sonido de Muerte](/Doc/Sonidos/sfx_death.wav)
>   2. Sonido de salto: [Sonido de Salto](/Doc/Sonidos/sfx_jump.wav)
>   3. Sonido de daño recibido: [Sonido de Daño](/Doc/Sonidos/sfx_hit.wav)
>
>- *Sonidos del enemigo*:
>
>   1. Sonido cuando se mata al enemigo: [Sonido de Muerte Enemigo](/Doc/Sonidos/sfx_enemy_death.wav)
>   2. Sonido cuando el enemigo hace daño: [Sonido de Daño](/Doc/Sonidos/sfx_hit.wav)
>
>- *Sonidos de eventos*:
>
>   1. Sonido de Game Over: [Sonido de GameOver](/Doc/Sonidos/sfx_gameOver.wav)
>   2. Sonido de recogida de moneda: [Sonido de Moneda](/Doc/Sonidos/sfx_coins.wav)
>   3. Sonido de activación del checkpoint [Sonido de CheckPoint](/Doc/Sonidos/sfx_checkPoint.wav)
</audio>

## DETALLES TÉCNICOS

### Plataformas Objetivo

> El juego está diseñado para ser publicado en PC con Windows. Pero llegado el caso, se podría diseñar para otras plataformas. Se juega a pantalla completa para proporcionar una experiencia de juego inmersiva.
>
>En cuanto a las especificaciones técnicas, aquí hay algunas consideraciones generales que podrían aplicarse:
>
>- **Sistema Operativo**: El juego debería ser compatible con las versiones más recientes de Windows.
>- **Memoria**: mínimo memoria RAM 8GB .
>- **Espacio de Almacenamiento**: El juego requerirá cierto espacio de almacenamiento en el disco duro del usuario.
>- **Resolución de Pantalla**: Como el juego se juega a pantalla completa, debería ser compatible con una variedad de resoluciones de pantalla.
>- **Controladores**: El juego se controla con el teclado, por lo que no se requieren controladores especiales.

### Herramientas de Desarrollo

>El juego "Dinosaurio: La aventura de las Monedas Perdidas" fue desarrollado utilizando una variedad de herramientas para asegurar una experiencia de juego de alta calidad:
>
>**1. Motor de Juego:** El motor principal utilizado para el desarrollo del juego es Unity. Los complementos usados fueron:
>
>- *Rigidbody:* Se utilizó el componente Rigidbody de Unity para dar físicas realistas al dinosaurio y otros elementos del juego.
>- *AudioSource:* Se usó el componente AudioSource de Unity para reproducir los efectos de sonido y la música de fondo.
>- *Canvas:* Se usaron objetos Canvas para mostrar elementos de la interfaz de usuario, como la barra de salud, el contador de monedas y todos los textos del juego.
>- *Animator:* Se utilizó el componente Animator de Unity para controlar las animaciones del dinosaurio, las monedas y los enemigos.
>- *EventSystem:* Para manejar los eventos de entrada del usuario, como clics del mouse o pulsaciones de teclas.
>- *ParticleSystem:* Fue usado para crear el efecto de trail de las monedas y también de la copa de Ganador en la escena final.
>- *SpriteRenderer:* Se utilizó el componente SpriteRenderer de Unity para mostrar las imágenes en el juego.
>- *Tilemaps:* Se usó para crear los niveles del juego y el terreno en el Menú.
>- *Cinemachine:* Se utilizó Cinemachine para crear una cámara que sigue al personaje a medida que se mueve por el nivel
>- *Coliders:* Para detectar las colisiones todas, por ejemplo: cuando el dinosaurio interactúa con las monedas, los enemigos, y las trampas.
>
>**2. Editor de Código:** *Visual Studio Code*. Es utilizado para escribir y editar los scripts del juego.
>
>No se ha usado ningun otro programa durante el desarrollo del juego, ni siquiera en el arte y la música, ya que todas las imagenes y sonidos se descargaron ya creados, de [Internet](https://pacobarba.com/blog/)
