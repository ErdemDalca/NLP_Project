# Dinosaurio: La aventura de las Monedas Perdidas

## GAME DESIGN DOCUMENT

Creado por: Nerea Trillo Pérez

Versión del documento: 2.5

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
| 2.1 | 22/11/2024 | Modificado la parte de Resumen para actualizarlo a la nueva versión del juego |
| 2.2 | 23/11/2024 | Modificado la parte de Diseño |
| 2.3 | 24/11/2024 | Actualizado la sección de mecánicas del juego y mundo del juego |
| 2.4 | 27/11/2024 | Añadido un índice al GDD |
| 2.5 | 29/11/2024 | Actualizado la sección de Arte, Audio y Detalles Técnicos |

## Índice

[1. **Concepto**](#concepto)

[2. **Puntos clave**](#puntos-clave)

[3. **Género**](#género)

[4. **Público Objetivo**](#público-objetivo)

[5. **Experiencia de juego**](#experiencia-de-juego)

[6. **Diseño**](#diseño)

- [6.1 Metas de Diseño](#metas-de-diseño)

[7. **Mecánicas de Juego**](#mecánicas-de-juego)

- [7.1 Núcleo de Juego](#núcleo-de-juego)
- [7.2 Flujo de Juego](#flujo-de-juego)
- [7.3 Fin de Juego](#fin-de-juego)

[8. **Físicas del Juego**](#física-de-juego)

[9. **Controles**](#controles)

[10. **Mundo del Juego**](#mundo-del-juego)

- [10.1 Descripción General](#descripción-general)
- [10.2 Personajes](#personajes)
- [10.3 Objetos](#objetos)
- [10.4 Flujo de Pantallas](#flujo-de-pantallas)
- [10.4 HUD](#hud)

[11. **Arte**](arte)

- [11.1 Metas de Arte](#metas-de-arte)
- [11.2 Assets de Arte](#assets-de-arte)

[12. **Audio**](#audio)

- [12.1 Metas de Audio](#metas-de-audio)
- [12.2 Assets de Audio](#assets-de-audio)

[13. **Detalles Técnicos**](#detalles-técnicos)

- [13.1 Plataformas Objetivo](#plataformas-objetivo)
- [13.2 Herramientas de Desarrollo](#herramientas-de-desarrollo)

## RESUMEN

### Concepto

> Dinosaurio: La aventura de las Monedas Perdidas es un emocionante juego de plataformas 2D donde los jugadores asumen el papel de un valiente dinosaurio en su misión de recolectar las monedas perdidas. A través de 4 niveles desafiantes, los jugadores deben navegar por terrenos difíciles, evitar obstáculos y superar enemigos para avanzar.

### Puntos Clave

> **1. Personaje Principal**: El jugador controla a un dinosaurio en un mundo 2D de plataformas.
> **2. Objetivo**: El objetivo principal es alcanzar la máxima puntuación posible para entrar en el ranking de los 5 mejores jugadores, con una puntuación mínima de 4000 puntos para clasificar.
> **3. Movilidad**: El dinosaurio puede moverse hacia la izquierda y la derecha, subir y bajar escaleras, y saltar.
> **4. Enemigos y Trampas**: Hay enemigos móviles y trampas estáticas y móviles que pueden quitarle vida al dinosaurio.
> **5. Checkpoints**: Los checkpoints guardan el progreso del jugador, su posición, en caso de muerte.

### Género

> Plataformas, Aventura.

### Público Objetivo

> El juego está dirigido a jugadores de todas las edades que disfrutan de los juegos de plataformas y aventuras. No se requiere ninguna habilidad especial para jugar, por lo que es adecuado tanto para jugadores novatos como para los más experimentados. Los jugadores que disfrutan de juegos como “Super Mario Bros.” y “Donkey Kong” podrían encontrar este juego interesante.

### Experiencia de Juego

> En este juego de plataformas 2D, el jugador se embarcará en una aventura emocionante controlando a un dinosaurio. Desde el momento en que el jugador entra en el mundo del juego, se encontrará inmerso en un entorno lleno de desafíos y recompensas.
>
>Visualmente, el jugador se encontrará en un mundo vibrante y colorido, lleno de plataformas para saltar,escaleras para subir y bajar terrenos, rampas, monedas para recoger y enemigos para evitar. El dinosaurio, controlado por el jugador, se moverá fluidamente por el escenario para recoger las monedas.
>
>Auditivamente, el jugador estará acompañado por una música de fondo que complementa la acción en pantalla. Los efectos de sonido, como el sonido de las monedas al ser recogidas o el sonido de los enemigos al ser derrotados, añadirán una capa adicional de inmersión a la experiencia de juego.
>
>En cuanto a la interactividad, el jugador tendrá un control total sobre el dinosaurio. Podrá moverse a la izquierda y a la derecha, subir y bajar escaleras, saltar para superar obstáculos y recoger monedas. Además, el jugador deberá evitar a los enemigos, las trampas y no caerse al vacío para no perder vidas.
>
>A lo largo del juego, el jugador se enfrentará a niveles cada vez más difíciles, pero también tendrá la satisfacción de ver cómo su contador de puntuación aumenta y cómo supera cada nivel. Y si en algún momento el juego se vuelve demasiado desafiante, el jugador siempre puede pausar el juego (en la versión Windows) y retomarlo más tarde.
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
>**- Retroalimentación**: Es importante que los jugadores reciban retroalimentación constante sobre su rendimiento. Para ello se contará con un contador de vidas y monedas (puntuación), así como respuestas visuales y sonoras a las distintas acciones del jugador.
>
>**- Rejugabilidad**: La meta es que los jugadores quieran volver a jugar una y otra vez. Mediante una variedad en el diseño de los niveles y la inclusión de elementos de desafío, como trampas y enemigos.
>
>**- Accesibilidad**: Queremos que el juego sea accesible para todos los jugadores, independientemente de su habilidad, por eso se utilizaron controles intuitivos y una curva de dificultad bien equilibrada.
>
>**- Diversión**: La meta final, por supuesto, es que los jugadores se diviertan. Por eso el diseño del juego está centrado en la diversión, en lugar de la frustración. La diversión se fomentará a través de la exploración, la recolección de monedas, y la satisfacción de superar los desafíos para superar los niveles.

## MECÁNICAS DE JUEGO

### Núcleo de Juego

>En este juego de plataformas 2D el jugador encarnará a un simpático dinosaurio cuyo objetivo principal es conseguir una puntuación lo suficientemente alta para entrar en el ranking de los 5 mejores jugadores. Aunque recoger monedas dispersas por los niveles ayuda a incrementar la puntuación, el enfoque es alcanzar la máxima puntuación posible, con una puntuación mínima de 4000 puntos para clasificar en el ranking. El objetivo final es ser el primero en el ranking, añadiendo un elemento de competencia y desafío al juego. Esto incentiva la exploración y la búsqueda de cada rincón del nivel para asegurarte de no dejar ninguna moneda atrás.
Con un enfoque puro en la diversión y la exploración, el juego no presenta enemigos a derrotar ni objetos ocultos que complicarían la experiencia.
>
>Controlas al dinosaurio con las teclas de dirección, moviéndolo hacia la izquierda y hacia la derecha, y haciendo uso de la tecla de espacio para saltar. En la versión Android, se usan las teclas virtuales que aparecen en la pantalla táctil, incluyendo un botón para saltar y flechas para moverse. Con estas habilidades básicas, te embarcarás en una aventura donde la agilidad y la precisión son tus mejores aliados.
Cada nivel es como un mundo propio, lleno de vida y sorpresas.Cada nivel está diseñado con cuidado, presentando una variedad de plataformas y obstáculos que desafiarán tus habilidades de salto y tu destreza, desde simples plataformas hasta trampas mortales como pinchos, el terreno está lleno de desafíos que pondrán a prueba tus reflejos y tu capacidad de adaptación.
A medida que avanzas a través de los niveles, te encuentras con nuevas y emocionantes mecánicas de juego. Los primeros niveles son como un suave paseo por el parque, donde te familiarizas con los controles y te acostumbras al ritmo del juego. Sin embargo, a medida que te adentras en territorio desconocido, los desafíos se vuelven más difíciles y exigentes, como trampas móviles y enemigos más numerosos, los cuales puedes matar saltándoles encima, lo que requiere que el jugador mejore sus habilidades de navegación y timing de saltos para superarlos. Sin embargo, el juego mantiene su enfoque en la diversión y la accesibilidad, evitando picos de dificultad excesivos que puedan frustrar al jugador.
Para desbloquear el siguiente nivel, simplemente tienes que llegar al final del nivel actual, sin necesidad de recoger todas las monedas. Esto facilita la progresión en el juego, enfocando la experiencia en la exploración y el avance.
>
>Para ayudarte en tu aventura, un contador de vidas te informa sobre cuántas oportunidades tienes antes de que el juego termine. Comienzas con tres vidas, y cada vez que caigas en una trampa mortal, te dañe un enemigo o caigas al vacío, perderás una vida. Mantén un ojo en tu contador de vidas para asegurarte de conservarlas hasta el final.
Además, un contador de monedas te ofrece una visión clara de tu progreso en cada nivel. Cada vez que recoges una moneda, el contador se actualiza, indicándote tu puntuación actual. Las monedas amarillas te dan 10 puntos, mientras que las monedas rojas te otorgan 50 puntos. Esta herramienta es invaluable para rastrear tu progreso y asegurarte de no pasar por alto ninguna moneda en tu búsqueda de la máxima puntuación y el éxito en el ranking.
>
>El juego también cuenta con un sistema de checkpoints que te permite reiniciar desde un punto específico del nivel en caso de que pierdas una vida. Estos checkpoints te dan un respiro y evitan que tengas que repetir secciones completas del nivel cada vez que falles.
Finalmente, el tercer nivel introduce un nuevo elemento, en forma de unas escaleras, que agregan un nuevo nivel de verticalidad al diseño de los niveles. Debes dominar tus habilidades de salto y precisión para superar estos nuevos desafíos y alcanzar la meta.
El juego no posee un sistema de puntuaje, ni unas reglas de combate.

### Flujo de Juego

> **Inicio**: El jugador inicia el juego desde la pantalla de Login, donde todos los jugadores, nuevos o antiguos, deben ingresar su correo electrónico y contraseña. Si el email ya está registrado, debe usar la misma contraseña que utilizó al registrarse.
**Menú principal**: Aquí, puede ajustar las opciones del idioma, salir del juego, ver la tabla de ranking, ir al menú de opciones o comenzar el juego.
**Instrucciones**: Al seleccionar “comenzar”, el jugador es llevado a una pantalla de instrucciones que explica brevemente los controles y el objetivo del juego. Para empezar el nivel, el jugador presiona la tecla “Enter”.
**Nivel 1**: El jugador comienza el primer nivel con 3 vidas y 0 monedas de puntuación. El objetivo es recoger tantas monedas como sea posible, para subir la puntuación y entrar en el ranking mientras evita trampas y enemigos.
**Checkpoints**: Si el jugador pasa por un checkpoint, se guarda la posición del jugador si muere, por lo que no tendría volver a iniciar el nivel desde el principio.
**Pérdida de vida**: Si el jugador cae al vacío, toca una trampa, o es tocado por un enemigo, pierde una vida. Si pierde una vida, la escena se recarga y el jugador aparece en el último checkpoint activado, si es que había activado alguno.
**Game Over**: Si el jugador pierde todas sus vidas, se muestra el mensaje de Game Over con la opción de comenzar de nuevo o volver al menú. Si elige comenzar de nuevo, siempre comienza desde el nivel 1.
**Pasar de nivel**: Si el jugador recoge todas las monedas en un nivel, se desbloquea automáticamente el siguiente nivel.
**Niveles 2, 3 y 4**: Estos niveles funcionan de la misma manera que el nivel 1, pero con diferentes diseños de nivel y posiblemente con más desafíos.
**Fin**: Al completar todos los niveles, el jugador verá una pantalla de Ranking que muestra la clasificación actual de los mejores jugadores y los créditos del juego. Desde esta pantalla, el jugador tendrá la opción de volver al menú principal o salir del juego.
![Flujo de diagrama](/doc/img/Diagramas/Diagrama%20de%20flujo.drawio.png)

### Fin de Juego

>**Derrotas**:
>
>- Pérdida de todas las vidas: Si el jugador pierde todas sus vidas, ya sea por caer al vacío, tocar una trampa o ser tocado por un enemigo, el juego termina. Se muestra la pantalla de Game Over con la opción de comenzar de nuevo o volver al menú principal.
>
>**Victorias**:
>
>- Completar todos los niveles: Sin embargo, la verdadera victoria radica en clasificarse como el primero en la tabla de ranking, lo cual requiere obtener una puntuación bastante alta. Al finalizar todos los niveles, se muestra una pantalla de ranking y los créditos del juego, ofreciendo al jugador la opción de volver al menú principal o salir del juego.
>
>**Otras situaciones**:
>
>- Pausa del juego: Si el jugador presiona la tecla “P” durante el juego, este se pausa. Puede reanudar el juego presionando “P” nuevamente (solo disponible en versión PC)
>- Salir del juego: En cualquier momento, el jugador puede presionar la tecla “ESC” para salir del juego. Esto también se considera una conclusión de la partida (solo disponible en versión PC).

### Física de Juego

> La física del juego se centra en simular el movimiento y la interacción de los personajes (principalmente el dinosaurio jugador) con el entorno del juego, incluidas las plataformas, las monedas y las trampas. Esto se logra mediante el uso de RigidBodies, colliders y fuerzas básicas como la gravedad y la aplicación de fuerzas de movimiento.
Al **Dinosaurio** se le aplica la física de movimiento básico, controlado por las teclas de dirección (<- y ->).
La física de salto se activa con la tecla de espacio, con una fuerza vertical que contrarresta la gravedad y permite al jugador saltar sobre obstáculos y alcanzar plataformas elevadas. Se utiliza un RigidBody para simular la masa del dinosaurio y permitir que interactúe con otros objetos y obstáculos en el juego, como las plataformas y las trampas, y sin fricción. Los colliders se utilizan para detectar colisiones con objetos en el mundo del juego, como las monedas, los enemigos y los elementos del entorno, como las plataformas y las trampas.
En la versión de Android, se utilizan botones virtuales que tienen colliders. Al tocarlos con el dedo en la pantalla táctil, se activa el salto o el movimiento del dinosaurio, proporcionando una experiencia de control adaptada a dispositivos móviles.
En los otros personajes, los **enemigos**, que son insectos, tienen una física de movimiento simple, como patrullar de un lado a otro en una plataforma o terreno. No se les aplica RigidBody, ya que no necesitan simular masa ni interactuar con la física del entorno de la misma manera que el dinosaurio. En cuanto a los demás objetos como monedas, plataformas, escaleras, etc, no tienen una física compleja, ya que no necesitan moverse ni hacer ninguna otra función, que no sea interactuar con el jugador, por eso tienen colliders.

### Controles

>**DURANTE PARTIDA**:

| **Acción** | **Tecla (PC)** | **Botón (Android)** |
| --- | --- | ---- |
| Mover el dinosaurio hacia la izquierda | Flecha izquierda (←) | Flecha izquierda (virtual) |
| Mover el dinosaurio hacia la derecha | Flecha derecha (→) | Flecha derecha (virtual) |
| Subir escalera | Flecha arriba (↑) | Flecha arriba (virtual) |
| Bajar escalera | Flecha abajo (↓) | Flecha abajo (virtual) |
| Hacer saltar al dinosaurio | Barra espacio | Botón de salto (virtual) |
| Pausar el juego | P | - |
| Reiniciar partida después de Game Over | Intro | Botón Reiniciar (virtual)|
| Volver al Menú después de Game Over | M | Botón Menú (virtual) |

>**EN EL LOGIN:**

| **Acción** | **Tecla (PC)** | **Botón (Android)** |
| --- | --- | --- |
| Ingresar correo electrónico| Teclado | Teclado virtual en pantalla |
| Moverse al campo de contraseña | Intro | Tocar el campo con el dedo |
| Ingresar contraseña| Teclado | Teclado virtual en pantalla |
| Enviar (Submit) | Intro | Botón Login |

>**EN EL MENÚ:**

| **Acción** | **Tecla (PC)** | **Botón (Android)** |
| --- | --- | --- |
| Navegar hacia arriba  | Flecha arriba (↑) | - |
| Navegar hacia abajo | Flecha abajo (↓) | - |
| Navegar hacia las banderas | Flecha derecha (→) | - |
| Volver a las opciones del menú | Flecha izquierda (←) | - |
| Seleccionar la opción resaltada | Barra espacio | Tocar con el dedo la opción |

>**EN EL MENÚ DE OPCIONES:**

| **Acción** | **Tecla (PC)** | **Botón (Android)** |
| --- | --- | --- |
| Navegar hacia arriba en el menú  | Flecha arriba (↑) | - |
| Navegar hacia abajo en el menú | Flecha abajo (↓) | - |
| Disminuir volumen | Flecha izquierda (←) | Deslizar con el dedo hacia la izquierda |
| Aumentar volumen | Flecha derecha (→) | Deslizar con el dedo hacia la derecha |
| Seleccionar la opción resaltada  | Barra espacio | Tocar con el dedo la opción |

## MUNDO DEL JUEGO

### Descripción General

> El juego se desarrolla en un mundo vibrante y colorido, lleno de vida y energía. El entorno es un paisaje de plataformas 2D que se extiende en todas las direcciones, con un cielo azul brillante arriba y un suelo sólido debajo. El mundo está lleno de plataformas flotantes, trampas y monedas brillantes que el jugador debe recoger.
>
>El personaje principal es un dinosaurio adorable y ágil que se mueve con gracia, su objetivo es recoger tantas monedas como sea posible para aumentar su puntuación y quedar como el mejor jugador en el ranking. El dinosaurio puede moverse hacia la izquierda y hacia la derecha usando las teclas de flecha y puede saltar con la tecla de espacio. En la versión de Android usará los botones virtuales que aparecen en cada nivel.
>
>El mundo está lleno de desafíos, pero no hay enemigos que derrotar ni objetos ocultos que encontrar. El objetivo principal es disfrutar del viaje y completar cada nivel recogiendo tantas monedas como sea posible. Las monedas, dispersas por todos los niveles, aumentan la puntuación del jugador. Un contador en la pantalla muestra las vidas del jugador (comenzando con 3) y la puntuación obtenida de las monedas recogidas en cada nivel. Las monedas amarillas otorgan 10 puntos, mientras que las monedas rojas otorgan 50 puntos.
>
>El juego comienza con una pantalla de login, donde el jugador debe ingresar un email y una contraseña. La primera vez que un jugador accede, se crea un nuevo registro. Si el mismo email se utiliza nuevamente, la contraseña ingresada debe coincidir con la registrada previamente; de lo contrario, se creará un nuevo registro con un email diferente. Los emails pueden ser inventados, pero deben tener un formato válido, como <xxx@xxxx.com> o <xxx@xxxx.es>, y la contraseña debe tener un mínimo de 6 caracteres.
El menú principal del juego ofrece varias opciones:
>
>- Comenzar el juego
>- Ver el ranking
>- Seleccionar el idioma
>- Ir al menú de opciones: donde se puede ajustar el volumen de la música y los sonidos
>- Salir del juego
>
>Además, hay una escena de instrucciones que guía al jugador a través de los controles y los objetivos del juego, asegurando que entiendan cómo jugar y cómo alcanzar la máxima puntuación para entrar en el ranking de los mejores jugadores.
>
>El juego consta de cuatro niveles, cada uno con su propio conjunto de imágenes y sprites. Los elementos visuales incluyen el dinosaurio, dos tipos de enemigos que son insectos, monedas para recoger (rojas y amarillas), terreno y plataformas creadas con sprites y tilemaps, trampas estáticas y móviles, y varios elementos de decoración. En el nivel 3, se añade un nuevo sprite de escaleras.
>
>La última escena, a la que se llega al completar todos los niveles o desde el menú, muestra una tabla de clasificación de los 5 mejores jugadores. Esta tabla incluye el ID del jugador (que es el email utilizado para iniciar sesión) y la puntuación alcanzada. La escena está decorada con dos copas de las que salen destellos en forma de estrella.
Además, se muestran los créditos, que se mueven de derecha a izquierda, saliendo y reentrando en pantalla. Desde esta pantalla, el jugador tiene la opción de volver al menú principal para comenzar una nueva partida, cambiar ajustes o idioma, o salir del juego.
>
>Las animaciones incluyen a los enemigos moviéndose, el dinosaurio saltando y moviéndose y las monedas, también tienen una animación en la que giran sobre sí mismas.
>
>El juego tiene un estilo visual atractivo, con gráficos coloridos y detallados. Los fondos son imágenes en paralaje que dan una sensación de profundidad y movimiento al mundo del juego.
>
>El sonido y la música del juego también juegan un papel importante en la creación de la atmósfera del juego. Los efectos de sonido proporcionan retroalimentación inmediata a las acciones del jugador, y la música de fondo establece el tono y el ritmo del juego.

### Personajes

>Este juego solo tiene 2  de personajes:
>
>1. **Jugables**: Dinosaurio (Jugador). Este es el personaje principal del juego, controlado por el jugador. Es un dinosaurio que se mueve con las teclas de flecha y salta con la tecla de espacio, en la versión PC, pero en la de Android usa los botones virtuales. Su objetivo es sacar la máxima puntuación recogiendo tantas monedas como pueda. No tiene habilidades especiales más allá de moverse y saltar.
>2. **Enemigos**: No atacan al dinosaurio, pero su presencia puede ser un obstáculo para el dinosaurio, ya que si tocan al jugador le resta una vida. No tienen habilidades especiales. Destacamos dos tipos de enemigos, los insectos marrones y los verdes.

### Objetos

>Los objetos con los que el jugador (dinosaurio) puede interactuar, es decir, recoger, activar o usar son:
>
>1. **Monedas (Coins)**
*Interfaz*: Representadas como pequeñas monedas brillantes dispersas por el nivel. El dinosaurio las recoge al pasar sobre ellas, sin necesidad de activación adicional.
>
>2. **Checkpoint**
*Interfaz*: Representado como una roca que es punto de guardado en el nivel. Al pasar sobre él, el dinosaurio activa el checkpoint (el cual cambia de color) para guardar su posición en el juego.
>
### Flujo de Pantallas

>El juego se compone de varias pantallas interconectadas, cuya interacción se representa en el siguiente [pdf](/doc/Diseño/Interface%20Flow.pdf).
>
>**Pantalla Login**
La experiencia del juego comienza en la Pantalla de Login, con un fondo que evoca un cielo, un bosque y una plataforma, similar al entorno de los niveles del juego. Aquí, el jugador debe ingresar un email y una contraseña. Para moverse de un campo a otro, se utiliza la tecla "Intro". Una vez ingresados ambos datos, se puede iniciar sesión presionando "Intro" o haciendo clic en el botón de "Login" que aparece en la pantalla. En la versión de Android, se toca con el dedo el campo deseado para escribir el email y la contraseña, y se inicia sesión tocando el botón de "Login".
![Pantalla Login](/doc/img/GUI/Login%20Screen.png)
>
>**Pantalla de Menú**
La Pantalla de Menú, que mantiene el mismo entorno visual que la Pantalla de Login, presenta al jugador cuatro opciones:
>
>- Salir
>- Ranking
>- Comenzar
>- Opciones
>
>Además, hay tres banderas para seleccionar el idioma (castellano, gallego o inglés). Para navegar por esta pantalla, se utilizan las flechas del teclado y para seleccionar una opción, se usa la tecla "Intro". Al seleccionar "Opciones", el jugador es dirigido a la Pantalla de Opciones. Al elegir "Comenzar", el jugador es llevado a la Pantalla de Instrucciones. En la versión Android bastaría con seleccionar la opción deseada con el dedo.
![Menu](/doc/img/GUI/Main%20Menu.png)
>
>**Pantalla de Opciones**
En esta pantalla, el jugador tiene la oportunidad de personalizar su experiencia de juego. Aquí, es posible ajustar el volumen de la música y los efectos de sonido del juego. Los controles son consistentes con los de la Pantalla de Menú, y además, se incluye un botón de “Volver”, que permite al jugador regresar a la Pantalla de Menú en cualquier momento.![Opciones](/doc/img/GUI/Option%20Menu.png)
>
>**Pantalla de Instrucciones**
La Pantalla de Instrucciones proporciona al jugador las instrucciones del juego y los controles que se tienen que usar, todo presentado en formato de texto e imágenes, y se presenta sobre el fondo del cielo usado en las demás pantallas. Para iniciar la partida y avanzar a la Pantalla del Nivel 1, el jugador debe presionar la tecla "Intro".![Instrucciones](/doc/img/GUI/Instructions%20Screen.png)
>
>**Pantalla de Nivel 1,2,3 y 4**
El juego consta de tres niveles distintos, cada uno con su propio diseño y desafíos únicos. La acción comienza en la Pantalla del Nivel 1, donde el jugador se encuentra con un entorno lleno de plataformas, trampas, enemigos, monedas y elementos ambientales. También se muestran contadores de vida y de monedas (puntuación), proporcionando al jugador información crucial durante el juego. Este tipo de entorno se mantiene en todos los niveles.
En cada nivel, el objetivo principal del jugador conseguir la máxima puntuación, recolectando las monedas disponibles. Sin embargo, si el jugador agota todas sus vidas el juego llegará a su fin, en este punto, se mostrará el mensaje “GameOver” y se le ofrecerá al jugador la opción de reiniciar la partida, lo que le llevará de vuelta a la Pantalla del Nivel 1, independientemente del nivel en el que se encontraba cuando ocurrió el GameOver, o volver a la pantalla Menú.
En la Pantalla del Nivel 4, una vez que el jugador ha pasado el nivel, se le permitirá avanzar a la Pantalla Final, que es la de Ranking.
![Nivel](/doc/img/GUI/GUI-HUD%20Windows.png)
![Nivel](/doc/img/GUI/GUI-HUD%20Android.png)
>
>**Pantalla Final**
La nueva Pantalla Final muestra un fondo de colinas verdes y un cielo azul. En la parte superior de la pantalla, dos trofeos dorados, con destellos, enmarcan el texto "RANKING" en letras grandes y amarillas. Debajo de esto, se presenta una tabla de Ranking de los 5 mejores jugadores con dos columnas, los jugadores y sus puntuaciones.
>
>En el centro de la pantalla, un personaje pequeño y verde con un solo ojo añade un toque de carácter. En la parte inferior de la pantalla, se despliega el texto de los créditos, mencionando a los desarrolladores y otros contribuyentes, moviéndose de derecha a izquierda y reingresando en pantalla. Desde esta pantalla podemos volver al menú o salir del juego.
![PantallaFinal](/doc/img/GUI/RankingScreen.png)

### HUD

>El HUD (Heads-Up Display) en este juego de plataformas 2D con un dinosaurio es bastante sencillo y directo, lo que permite a los jugadores concentrarse en la acción del juego. Aquí está la descripción de los elementos del HUD durante el desarrollo de la partida:
>
>- **Contador de Vidas**: Este es un elemento crucial del HUD. Muestra el número de vidas que le quedan al jugador (comienza con 3). Cada vez que el jugador pierde una vida, este número disminuye. Cuando llega a cero, se produce un GameOver, se finaliza esa partida. Su propósito es informar al jugador cuántas oportunidades le quedan para completar el nivel.
>
>- **Contador de Monedas**: Este elemento muestra la puntuación que el jugador ha ido acumulando en el nivel actual. Su propósito es informar al jugador sobre la puntuación obtenida a lo largo del juego, incentivándolo a mejorar su desempeño y a aspirar a alcanzar los primeros puestos en el ranking.

## ARTE

### Metas de Arte

>Los objetivos que se quieren lograr son las de crear un ambiente visualmente atractivo y amigable que sea coherente con la simplicidad y accesibilidad del juego, asegurar que los elementos visuales sean claros y fácilmente identificables identificables para facilitar la jugabilidad e implementar un diseño artístico que sea coherente en todos los niveles del juego, ofreciendo una experiencia visual fluida.
>
>**Estilo de Arte y Concepto Visual**:
>El estilo de arte es pixelado, reminiscente de los juegos clásicos de plataformas, pero con un toque moderno en la calidad gráfica. Los colores son vibrantes pero no saturados, creando un equilibrio visual que es agradable a la vista.
El concepto visual se centra en la simplicidad; cada elemento está diseñado para ser inmediatamente reconocible y funcional.
>
>**Apariencia General de Escenarios y Personajes:**
>
>- **Escenarios**: Los escenarios son sencillos pero detallados, con terrenos texturizados y fondos parallax para añadir profundidad. Las monedas están claramente visibles contra el fondo, y las trampas son identificables para evitarlas fácilmente.

![Escenario](/doc/img/GDD/Escenario.png)
>
>- **Personajes**: El dinosaurio jugador tiene un diseño caricaturesco con colores verdes suaves. Es expresivo pero simple, facilitando la identificación inmediata por parte del jugador.

![Dinosaurio](/doc/img/GDD/dinosaurio.png)

>Los enemigos, representados por insectos marrones y verdes, tienen un diseño simple pero efectivo que los hace fácilmente reconocibles, tienen cabeza, cuerpo y patas y se mueven.

![Enemigo](/doc/img/GDD/Animaciones/enemigo1Animacion.gif)

![Enemigo](/doc/img/GDD/Animaciones/enemigo2Animacion.gif)

### Assets de Arte

> 1. *Menú Login*:
>
>- Imagen de texto para Login

![Titulo](../img/GDD/Menu%20y%20opciones/LOGIN.png)
>
> 2. *Menú Principal y de Opciones*:
>
>- Imágenes de texto para las opciones:
>
>   1. “Titulo del juego”

![Titulo](../img/GDD/Menu%20y%20opciones/castellano/Titulo.png)

![Titulo](../img/GDD/Menu%20y%20opciones/ingles/DINOSAUR.png)

>   2. “Comenzar”:
**activo**:

![Comenzar](/doc/img/GDD/Menu%20y%20opciones/castellano/Comenzar_On.png)
![Comenzar](/doc/img/GDD/Menu%20y%20opciones/ingles/Start_on.png)
![Comenzar](/doc/img/GDD/Menu%20y%20opciones/gallego/comezar_on.png)

**inactivo**:

![Comenzar](/doc/img/GDD/Menu%20y%20opciones/castellano/Comenzar_Off.png)
![Comenzar](/doc/img/GDD/Menu%20y%20opciones/ingles/Start_off.png)
![Comenzar](/doc/img/GDD/Menu%20y%20opciones/gallego/comezar_off.png)

>   3. “Opciones”:
**activo**:

![Opciones](/doc/img/GDD/Menu%20y%20opciones/castellano/Opciones_On.png)
![Opciones](/doc/img/GDD/Menu%20y%20opciones/ingles/options_on.png)
![Opciones](/doc/img/GDD/Menu%20y%20opciones/gallego/opcions_on.png)

**inactivo**:

![Opciones](/doc/img/GDD/Menu%20y%20opciones/castellano/Opciones_Off.png)
![Opciones](/doc/img/GDD/Menu%20y%20opciones/ingles/options_off.png)
![Opciones](/doc/img/GDD/Menu%20y%20opciones/gallego/opcions_off.png)

>   4. "Ranking"
**activo**:

![Ranking](../img/GDD/Menu%20y%20opciones/ranking_on.png)

**inactivo**:

![Ranking](../img/GDD/Menu%20y%20opciones/ranking_off.png)

>   5. “Salir”:
**activo**:

![Salir](/doc/img/GDD/Menu%20y%20opciones/castellano/Salir_On.png)
![Salir](/doc/img/GDD/Menu%20y%20opciones/ingles/exit_on.png)
![Salir](/doc/img/GDD/Menu%20y%20opciones/gallego/sair_on.png)

**inactivo**:

![Salir](/doc/img/GDD/Menu%20y%20opciones/castellano/Salir_Off.png)
![Salir](/doc/img/GDD/Menu%20y%20opciones/ingles/exit_off.png)
![Salir](/doc/img/GDD/Menu%20y%20opciones/gallego/sair_off.png)

>   6. “Titulo de Opciones”:

![TituloOpc](/doc/img/GDD/Menu%20y%20opciones/castellano/TituloOpciones.png)
![TituloOpc](/doc/img/GDD/Menu%20y%20opciones/ingles/optionsTitle.png)
![TituloOpc](/doc/img/GDD/Menu%20y%20opciones/gallego/opcionsTitle.png)

>   7. “Música”:
**activo**:

![Música](/doc/img/GDD/Menu%20y%20opciones/castellano/Musica_on.png)
![Música](/doc/img/GDD/Menu%20y%20opciones/ingles/music_on.png)
![Música](/doc/img/GDD/Menu%20y%20opciones/gallego/Musica_on.png)

**inactivo**:

![Música](/doc/img/GDD/Menu%20y%20opciones/castellano/Musica_off.png)
![Música](/doc/img/GDD/Menu%20y%20opciones/ingles/music_off.png)
![Música](/doc/img/GDD/Menu%20y%20opciones/gallego/Musica_off.png)

>   8. “Sonido”:
**activo**:

![Sonido](/doc/img/GDD/Menu%20y%20opciones/castellano/Sonido_On.png)
![Sonido](/doc/img/GDD/Menu%20y%20opciones/gallego/son_on.png)
![Sonido](/doc/img/GDD/Menu%20y%20opciones/ingles/sound_on.png)

**inactivo**:

![Sonido](/doc/img/GDD/Menu%20y%20opciones/castellano/Sonido_Off.png)
![Sonido](/doc/img/GDD/Menu%20y%20opciones/gallego/son_off.png)
![Sonido](/doc/img/GDD/Menu%20y%20opciones/ingles/sound_off.png)

>   9. “Volver”:
**activo**:

![Volver](/doc/img/GDD/Menu%20y%20opciones/castellano/Volver_On.png)
![Volver](/doc/img/GDD/Menu%20y%20opciones/ingles/back_on.png)
![Volver](/doc/img/GDD/Menu%20y%20opciones/gallego/Volver_On.png)

**inactivo**:

![Volver](/doc/img/GDD/Menu%20y%20opciones/castellano/Volver_Off.png)
![Volver](/doc/img/GDD/Menu%20y%20opciones/ingles/back_off.png)
![Volver](/doc/img/GDD/Menu%20y%20opciones/gallego/Volver_Off.png)

>   10. Imágenes con barras para ajuste de volumen:
**activo**:

![Vol](/doc/img/GDD/Menu%20y%20opciones/Vol_On.png)

**inactivo**:

![Vol](/doc/img/GDD/Menu%20y%20opciones/Vol_off.png)

>   11. Imagen con una “X” para indicar sonido/música apagado:

![SinVol](/doc/img/GDD/Menu%20y%20opciones/VolX.png)
>
> 3. *Jugador (Dinosaurio)*:
>
>- Sprite del dinosaurio

![Dino](/doc/img/GDD/dinosaurio.png)

>- Animación de muerte

![Muerte](/doc/img/GDD/Animaciones/AnimMuerte.png)

>- Animación al moverse

![Moverse](/doc/img/GDD/Animaciones/AnimDino.gif)
>
> 4. *Enemigos*:
>
>- Sprite de insecto marrón

![enemigo Marrón](/doc/img/GDD/Animaciones/enemigo1Animacion.gif)

>- Sprite de insecto verde

![enemigo Verde](/doc/img/GDD/Animaciones/enemigo2Animacion.gif)
>
> 5. *Objetos Coleccionables y HUD*:
>
>- Sprites de monedas

![Monedas](/doc/img/GDD/Monedas.png)
![Monedas](/doc/img/GDD/redCoin.png)

>- Animación giratoria de las monedas

![AnimaciónMoneda](/doc/img/GDD/Animaciones/AnimaMonedas.gif)

>- Contador con las vidas del jugador (imagen)

![BarraSalud](/doc/img/GDD/BarraSalud.png)

>- Contador de puntuación (imagen)

![Contador monedas](/doc/img/GDD/contador%20monedas.png)
>
> 6. *Entorno y Plataformas*:
>
>- Terreno y plataformas (sprites usados con tilemaps)

![Terreno](/doc/img/GDD/Terreno.png)
>
> 7. *Trampas*:
>
>- Pincho quieto (sprite)

![Pincho](/doc/img/GDD/Trampas/pinchos.png)
![Mazo](/doc/img/GDD/Trampas/Mace.png)

>- Pincho móvil (sprite)

![PinchoMovil](/doc/img/GDD/Trampas/pinchoMovil.png)
>
> 8. *Decoraciones y Fondos*:
>
>- Señalización sobre muerte (sprite)

![Señal Peligro](/doc/img/GDD/Decoracion/señal.jpg)

>- Flores decorativas (sprites)

![FloresAmarillas](/doc/img/GDD/Decoracion/florAmar.png)

![FloresRojas](/doc/img/GDD/Decoracion/Flower-3.png)

>- Imágenes en parallax para el fondo del juego

![FondoLejos](/doc/img/GDD/FondoLejos.png) ![FondoMedio](/doc/img/GDD/FondoMedio.png)

>- Degradado negro para caída al vacío

![Degradado](/doc/img/GDD/DegradadoCaida.png)
>
> 9. *Checkpoint*:
>
>- Imagen checkpoint inactivo

![Checkpoint](/doc/img/GDD/CheckPointInactivo.png)

>- Imagen checkpoint activo

![Checkpoint](/doc/img/GDD/checkPointActivo.png)
>
> 10. *Nivel Específico – Nivel Tres y Cuatro*:
>
>- Sprite nuevo, escaleras

![Escalera](/doc/img/GDD/escalera.jpg)
>
> 11. *Escena Final*:
>
>- Imagen de texto para ranking

![RAnking](/doc/img/GDD/Menu%20y%20opciones/RANKING.png)

>- Animación copa girando

![Copa](/doc/img/GDD/Animaciones/AnimCopa.gif)
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
>Música de fondo del juego: [Música de Fondo](../img/GDD/Sonidos/sfx_fondo.wav)
>**Sonidos**:
>
>- *Sonidos del jugador*:
>
>   1. Sonido de muerte:  [Sonido de Muerte](../img/GDD/Sonidos/sfx_death.wav)
>   2. Sonido de salto: [Sonido de Salto](../img/GDD/Sonidos/sfx_jump.wav)
>   3. Sonido de daño recibido: [Sonido de Daño](../img/GDD/Sonidos/sfx_hit.wav)
>
>- *Sonidos del enemigo*:
>
>   1. Sonido cuando se mata al enemigo: [Sonido de Muerte Enemigo](../img/GDD/Sonidos/sfx_enemy_death.wav)
>   2. Sonido cuando el enemigo hace daño: [Sonido de Daño](../img/GDD/Sonidos/sfx_hit.wav)
>
>- *Sonidos de eventos*:
>
>   1. Sonido de Game Over: [Sonido de GameOver](../img/GDD/Sonidos/sfx_gameOver.wav)
>   2. Sonido de recogida de moneda: [Sonido de Moneda](../img/GDD/Sonidos/sfx_coins.wav)
>   3. Sonido de activación del checkpoint [Sonido de CheckPoint](../img/GDD/Sonidos/sfx_checkPoint.wav)
</audio>

## DETALLES TÉCNICOS

### Plataformas Objetivo

> El juego está diseñado para ser publicado en PC con Windows y en dispositivos Android. Pero llegado el caso, se podría diseñar para IOS. El juego se presenta en pantalla completa para proporcionar una experiencia de juego inmersiva.
>
>En cuanto a las especificaciones técnicas, aquí hay algunas consideraciones generales que podrían aplicarse:
>
>**Requisitos para Windows/PC**:
>
>- Sistema operativo: Windows 7 o posterior
>- Procesador: Intel Core i5 o equivalente
>- RAM: 8 GB de memoria RAM, recomendado 16 GB
>- Almacenamiento: al menos 200 MB de espacio disponible en el disco duro
>- Tarjeta gráfica: tarjeta gráfica con soporte para OpenGL 3.0 o superior
>- Resolución de pantalla: 1280x720 o superior, recomendado 1920x1080.
>
>**Requisitos para Android**:
>
>- Sistema operativo: Android 10 o posterior
>- Procesador: Procesador de 2.0 GHz o equivalente
>- RAM: Mínimo 8 GB de memoria RAM, recomendado 16 GB
>- Almacenamiento: Mínimo 2GB de espacio disponible en el dispositivo
>- Pantalla: Resolución mínima de 1280x720 (HD)

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
>- *Localization:* Para soportar múltiples idiomas en el juego. Esto incluye el uso de componentes como "Localize String Event" y tablas para strings y assets.
>- *SpriteRenderer:* Se utilizó el componente SpriteRenderer de Unity para mostrar las imágenes en el juego.
>- *Tilemaps:* Se usó para crear los niveles del juego y el terreno en el Menú.
>- *Cinemachine:* Se utilizó Cinemachine para crear una cámara que sigue al personaje a medida que se mueve por el nivel
>- *Coliders:* Para detectar las colisiones todas, por ejemplo: cuando el dinosaurio interactúa con las monedas, los enemigos, y las trampas.
>- *Vertical Layout Group y Horizontal Layout*Group: Se añadieron estos componentes para una mejor disposición de los elementos en la interfaz, especialmente en la versión Android.
>
>**2. Editor de Código:** *Visual Studio Code*. Es utilizado para escribir y editar los scripts del juego.
>
>**3. Otras Herramientas**:
>
>- *Firebase*: Se añadió la conexión a Firebase para la autenticación y el almacenamiento de datos, lo que incluye la configuración con los SDK y el archivo google-service.json.
>- *GIMP*: Se utilizó GIMP para crear nuevos assets gráficos, especialmente los usados en el menú del juego.
>- *Draw.io*: para la elaboración de diagramas (flowcharts, casos de uso, etc).
>
>**4. Recursos Adicionales**: Aparte de las herramientas mencionadas anteriormente, no se utilizó ningún otro programa durante el desarrollo del juego. Todas las restantes imágenes y sonidos fueron descargados ya creados de [Internet](https://pacobarba.com/blog/).
