# **Ship Invasion**

## _Game Design Document_

---

##### Autores: Emily Rosenfeld, A01198339 / Marcos Dayan, A01782876/ Remy Patgher, A01784177

Equipo: REM Cycle

##

## _Índice_

1. [Índice](#índice)
2. [Diseño de Videojuego](#diseño-de-videojuego)
   1. [Resumen](#resumen)
3. [Índice](#índice)
4. [Diseño de Videojuego](#diseño-de-videojuego)
   1. [Resumen](#resumen)
   2. [Gameplay](#gameplay)
   3. [Mindset](#mindset)
5. [Técnico](#técnico)
   1. [Pantallas](#pantallas)
   2. [Controles](#controles)
   3. [Mecánicas](#mecánicas)
      1. [Cartas Ataque](#cartas-ataque)
      2. [Cartas Defensa](#cartas-defensa)
      3. [Mecánicas de Partida](#mecánicas-de-partida)
6. [Diseño de Nivel](#diseño-de-nivel)
   1. [Ambientación](#ambientación)
      1. [Mar Abierto](#mar-abierto)
      2. [Tormenta Eléctrica](#tormenta-eléctrica)
      3. [Río de Fuego](#río-de-fuego)
      4. [Pantano Tóxico](#pantano-tóxico)
7. [Hilo del Juego](#hilo-del-juego)
8. [Desarrollo](#desarrollo)
   1. [Clases](#clases)
9. [Gráficas](#gráficas)
   1. [Atributos de Estilo](#atributos-de-estilo)
   2. [Gráficas y Diseño](#gráficas-y-diseño)
10. [Sonido / Música](#sonido/música)
    1. [Atributos de Estilo](#atributos-de-estilo)
    2. [Sonido](#sonido)
    3. [Música](#música)
11. [Agenda](#agenda)

## _Diseño de Videojuego_

### **Resumen**

Ship Invasion es un videojuego de cartas TCG, en el que se juega en modo 1vs1 PvP local, y el objetivo principal es preservar la mayor parte de una flota naval dada, que será sometida a constantes ataques por turnos de diferentes proyectiles y misiles representados por cartas, que tanto el jugador como el contrincante, estarán usando constantemente para destruir la flota del competidor.

Hay dos principales tipos de cartas, las cartas de ataque, las cuales sirven para escoger cierta coordenada y lanzar un devastador ataque sobre ella, y las cartas de defensa, las cuales consisten en ya sea poner flotas, o proteger contra un ataque alguna flota. Dentro de éstas, existen diferentes calidades de cartas, Bronze, Silver y Gold, en donde una carta de ataque de mejor calidad, va a atacar un radio o una cantodad mayor de casillas, y una carta de defensa de mejor calidad, va a poner una embarcación de mayor tamaño, o proporcionar una protección mayor a una embarcación.

### **Gameplay**

Una partida consta de 2 etapas. La etapa del despliegue, y la etapa de destrucción.

La partida inicia con la etapa de despliegue. Una pantalla del territorio de la flota, este está representado con un grid, en el que se acomodarán 5 cartas de flota que serán repartidas aleatoriamente al jugador. Habrá un lapso de 30 segundos para cada jugador para que se acomoden esas 5 cartas iniciales, y pasado ese lapso, se tirará un volado digital para decidir si empieza de los dos jugadores.

En la etapa de la destrucción, se reparten 6 cartas a cada jugador, tres de ellas de ataque, y tres de ellas de defensa. Durante ésta etapa, se dará un lapso de 5 minutos en donde se repartirán en turnos de 15 segundos cada uno para que el jugador en turno escoja una carta para jugar. Acá es donde entra la estrategia, se debe escoger entre realizar una ataque con las cartas disponibles, o defender una posición y poniendo un escudo a un barco, o desplegando una embarcación.

¿Quién gana? Gana el jugador que destruya la embarcación del otro antes de que se acabe el tiempo, o en caso de que se acabe el tiempo, el jugador que tenga más unidades de embarcación desplegadas. En caso de que tengan la misma cantidad de unidades de embarcación, gana el jugador quien haya hecho más daño al otro, y en el final de los casos, se tiene un empate.

### **Mindset**

Este juego es una estrategia mental, el jugador tiene que estar constantemente concentrado para ganar. Por lo tanto el jugador se sentira poderoso al ganar, y ansioso de jugar mejor cuando pierda.

Al ver como el juego no tiene un patron exacto, el jugador no se aburrira pues no sera repetitivo.

De igual forma, el jugador tendrá la posibilidad de iniciar el juego con una apuesta. Esto con la finalidad de tratar de juntar la mayor cantidad de monedas, pues estás sirven para personalizar tus embarcaciones, así como el tablero de juego.

Por otro lado, las mismas monedas podrán ser utilizadas para comprar privilegios dentro del juego, es decir, el jugador puede pagar cierta cantidad de monedas para tirar doble turno o para duplicar el ataque de una de sus cartas, sin embargo, estas últimas tienen un costo algo, por ello, los jugadores querrán juntar más monedas.

## _Técnico_

---

### **Pantallas**

1. Pantalla de título
   1. Configuración
   2. Entrar a Pantalla de Menú
   3. Créditos
2. Menú
   1. Perfil del Jugador, stats, descripción
   2. Inventario de todas las cartas, sus estadísticas, descripción, entre otras características
   3. Selección de diferentes batallas y arenas (dificultad)
   4. Historia de partidas, estadísticas y datos de todas las partidas pasadas
3. Juego
   1. Tablero del Jugador con tablero del enemigo cerrado y cartas, en el que suceden todas las fases de la batalla
   2. Pantalla de resultados, en donde se anuncia el Ganador/Perdedor

### **Controles**

El jugador va a poder interactuar con el juego principalmente con el cursor del ratón y con el click izquierdo, seleccionando las diferentes cartas y ejecutando las acciones a través del cursor, y se puede aceptar diferentes opciones y botones presionando la tecla "Enter".

### **Mecánicas**

En Ship Invasion, hay dos tipos de cartas

1. Cartas de Ataque: Estas cartas se utilizan para lanzar ataques en ccordenadas específicas y patrones en el tablero enemigo, intentando golpear y hundir las flotas navales del oponente. Hay 3 tipos de cartas, las bronze, las silver y las gold, previamente descritas, entre mayor calidad, mayor su área de blanco

2. Cartas de Defensa: Estas cartas permiten a los jugadores colocar naves adicionales para reforzar la flota. Estas cartas juegan un rol crucial ya que la cantidad de espacios cubiertos por la flota naval van a determinar el vencedor de la partida, solo que hay que administrar bien los turnos ya que decidir jugar una carta de Defensa ocupará el turno de poder mandar un poryectil a alguna unbicación enemiga. De igual manera las cartas de defensa se dividen en calidades, en donde ewntre mejor calidad, mayor área del grid cubren.

El juego cuenta con 10 cartas de ataque y 10 de defensa:

#### **Cartas ataque:**

1. BRONZE, 1 cuadrado
2. ⁠BRONZE, 2 horizontal
3. ⁠BRONZE, 2 vertical
4. ⁠BRONZE, 3 horizontal
5. ⁠BRONZE, 3 vertical
6. ⁠SILVER, 3 horizontal
7. ⁠SILVER, 4 vertical
8. ⁠SILVER, 5 horizontal
9. ⁠GOLD, una L de 3x3
10. ⁠GOLD, 10 vertical

#### **Cartas defensa:**

1. BRONZE, 1 cuadrado
2. ⁠BRONZE, 1 cuadrado
3. ⁠BRONZE, 1 cuadrado
4. ⁠BRONZE, 2 cuadrados
5. ⁠BRONZE, 2 cuadrados
6. ⁠SILVER, 3 cuadrados
7. ⁠SILVER, 4 cuadrados
8. ⁠SILVER, 5 cuadrados
9. ⁠GOLD, una L de 3x3
10. ⁠GOLD, una X en un área de 3x3

#### Mecánicas de Partida

Una partida juego se desarrolla en dos fases principales: Despliegue y Combate, en donde en el despliegue el objetivo principal es ubicar las cartas de defensa en posiciones estratégicas para evitar a toda costa los ataques de los proyectiles enemigos en la fase de Destrucción.

Fase de Despliegue: La partida arranca en esta etapa, donde se presenta el mapa de batalla naval en forma de cuadrícula. A cada jugador se le otorgan aleatoriamente 5 cartas de flota para posicionar en el mapa durante un periodo inicial de 30 segundos. Finalizado este tiempo, se realiza un sorteo digital para determinar quién será el primero en jugar, si el jugador o el oponente controlado por el juego.

Fase de Combate: Una vez establecidas las posiciones iniciales, el juego avanza a la fase de combate, donde se asignan 6 cartas adicionales a cada jugador, divididas equitativamente entre cartas de ataque y defensa. Durante esta fase, los jugadores disponen de 5 minutos para utilizar sus cartas, alternando turnos cada 15 segundos. La elección estratégica de utilizar una carta para atacar, defender mediante la colocación de escudos, o desplegar nuevas unidades navales, es crucial en esta etapa.

Condiciones de Victoria: El vencedor es aquel que logre eliminar las unidades navales enemigas antes de que el tiempo límite expire. Si el tiempo se agota, gana el jugador con la mayor cantidad de unidades navales aún en juego. En caso de empate en número de unidades, se determinará un ganador basado en quién haya infligido mayor daño. Si aún persiste el empate, se declara un empate en la partida.

Arenas: Dadas las siguientes condiciones, habrán diferentes arenas de juego, en las que para algunas arenas será necesario un nivel mayor de experiencia, en las que el ambiente irá tomando mejores desiciones, administrando mejor sus cartas de ataque y desplegando con mayor inteligancia su flota, en cada etapa el oponente será un rival más sifisticado a vencer!

Sistema de monedas: Las arenas iniciales otorgarán una pequeña cantidad de monedas al conseguir una victoria, al ir obteniendo experiencia para poder jugar en las siguientes arenas, las partidas tendrán un costo inicial, pero en caso de salir victorioso, las recompensas monetarias serán mucho mayores! Se detalla la descripción de las diferentes arenas enseguida.

Uso de las monedas: El jugador podrá bien acceder a arenas que tengan un costo más elevado de entrada y una mayor recompensa al ganar, o comprar estilo para su tablero de juego, su flota naval, y su flota de misiles y proyectiles.

## _Diseño de Nivel_

### **Ambientación**

#### 1. Mar Abierto

Costo de partida: 0 Monedas
Recompensa de victoria: 20 Monedas

1.  Ambiente
    1. Caribeño, Soleado
2.  Objetos
    1. Mar Abierto
    2. Islas con Palmeras

#### 2. Tormenta Eléctrica

Costo de partida: 30 Monedas
Recompensa de victoria: 60 Monedas

1.  Ambiente
    1. Tormenta, Peligroso, Truenos, Relámpagos
2.  Objetos
    1. Lluvia, Truenos, Relámpagos
    2. Hojas volando

#### 3. Río de Fuego

Costo de partida: 50 Monedas
Recompensa de victoria: 120 Monedas

1.  Ambiente
    1. Peligro, Calor, Volcanes, fuego por doquier
2.  Objetos
    1. Meteoritos de fuego
    2. Erupciones volcánicas
    3. Mar de Lava

#### 4. Pantano Tóxico

Costo de partida: 100 Monedas
Recompensa de victoria: 250 Monedas

1.  Ambiente
    1. Veneno, lago tóxico, corrosión
2.  Objetos
    1. Barriles tóxicos
    2. Animales mutantes
    3. Árboles corroidos

### **Hilo del Juego**

1. Menú
2. Escoger arena
3. Fase de Despliegue
4. Fase de Destrucción
5. Anuncio de Ganador/Perdedor

## _Desarrollo_

### Clases

1. ShipInvController
2. TitleController
3. MenuController
4. GameController
5. Player
   1. Score
6. Ship
   1. PlaceShip
   2. Coordinates
7. Rocket
   1. LaunchRocket
   2. Coordinates
8. Play
   1. Match
9. Card
10. RandomizeCards
11. APIRequest
12. CreditsDisplay
13. SettingsConfig
14. MainTrack
15. SoundEffect

## _Gráficas_

### **Atributos de Estilo**

El videojuego tendrá un estilo caricaturesco con colores y contrastes llamativos, resaltando los elementosa de interacción como son las cartas y las diferentes arenas en las que se podrá jugar.

Además, estará planteado en ambientes surrealistas y fantásticos, en diferentes arenas que se sitúen en lugares remotos imaginarios con una historia de la arena por detrás que se vea reflejada en la ilustración de los diferentes escenarios. De igual manera, cada una de las cartas tanto de Ataque como de Defensa, tendrá elementos fantásticos en ella relfejando el estilo caricaturesco y especial de Ship Invasion.

Así se ven algunas de las cartas y de los diseños de las arenas que conforman Ship Invasion

### **Gráficas y Diseño**

1. Cartas
   1. Defensa 1. Bronze - Barcos Pequeños 2. Silver - Barcos Medianos 3. Gold - Barcos Grandes
      ![alt text](Fotos/33.png)
   2. Ataque 1. Bronze - Proyectiles Pequeños 2. Silver - Proyectiles Medianos 3. Gold - Proyectiles Grandes
      ![alt text](Fotos/13.png)
2. Arenas

   1. Mar Abierto

      1. Estilo visual vibrante y colorido, con una paleta que refleje el ambiente caribeño y soleado de la arena.
      2. Los fondos mostrarán el mar abierto y las islas con palmeras de manera detallada y atractiva, añadiendo vida al escenario.

![alt text](Fotos/ocean.png)

2.  Tormenta Eléctrica

    1. Estilo visual estará marcado por colores oscuros y contrastes intensos para reflejar el ambiente de tormenta y peligro.
    2. Los fondos mostrarán una atmósfera tensa con nubes oscuras y relámpagos, creando una sensación de urgencia y emoción en la arena.

![alt text](Fotos/storm.png)

3.  Río de Fuego

    1. El juego adoptará un estilo visual oscuro y amenazante, con una paleta de colores rojos, naranjas y negros para representar el peligro y la intensidad del ambiente de fuego.
    2. Los fondos mostrarán un río de lava y volcanes en erupción, creando una atmósfera desafiante y peligrosa en la arena.

![alt text](Fotos/fire.png)

4.  Pantano Tóxico
    1. Estilo visual estará marcado por tonos verdes y amarillos, con una atmósfera tóxica y corrosiva que se reflejará en el diseño de la arena.
    2. Los fondos mostrarán un pantano tóxico con barriles de desechos y árboles corroidos, creando una atmósfera inquietante y peligrosa en la arena.

![alt text](Fotos/swamp.png)

## _Sonido / Música_

### **Atributos de Estilo de Sonido**

El estilo de sonido es de una banda sonora de inspiración marítima y pirata con efectos de sonido realistas y estilizados, creando una atmósfera inmersiva de aventura y batalla naval. La música, estpa compuesta de instrumentos tradicionales como acordeones, tambores de guerra, flautas y violines. Los efectos de sonido, desde la explosión de cañones y proyectiles y el ambiente marino hasta señales audibles de eventos clave del juego, van a estar añadiendole emoción al juego y destacando todos los eventos importantes que sucedan. Desde el hundimiento de un barco, el lanzamiento de un proyectil, hasta la Victoria, asegurando que cada acción y reacción sean claras y contribuyan a la tensión y emoción del juego.

### **Sonidos**

1. Efectos de Sonido

   1. Sonidos de Ataque

      1. Explosiones de cañón
      2. Disparos de mortero
      3. Explosiones de misiles y proyectiles
      4. Hundimiento de flotas navales

   2. Sonidos Ambientales
      1. Ruido de olas
      2. chillidos de gaviotas
      3. Crujidos de la madera del barco
      4. Gritos de la tripulación

2. Feedback Auditivo
   1. Sonido de flota destruída
   2. Sonido de Victoria
   3. Sonido de Derrota
   4. Lanzamiento de proyectil
   5. Comienzo del turno

### **Música**

1. Tema Principal del Juego: Un tema épico y aventurero que use instrumentos tradicionales de música marítima y pirata, como acordeones, tambores de guerra, flautas y violines. Con un ritmo rápido y energético. Éste tema será tocado en la pantalla principal, el menú y los créditos

2. Música de Batalla: Pistas intensas y rítmicas que usan tambores pesados, trompetas, gritos de marineros y cuerdas rápidas para aumentar la emoción durante los enfrentamientos

## _Agenda_

1. Desarrollo de las clases base y primeras mecánicas de la partida

   1. Clases de Elementos de Modelo
      1. Clases de Cartas
      2. Clase de Jugador
      3. Clases de estilos visuales
      4. Clases de recopilación de estadísticas
   2. Clases del control del flujo del juego
      1. Título
      2. Menú
      3. Juego

2. Desarrollo de clases de acciones y lógica dentro de los diferentes controles de flujo del videojuego

   1. Ship
   2. Rocket
   3. Play
   4. Match
   5. PlaceShip
   6. LaunchRocket
   7. Scores
   8. CoordinateSystem
   9. RandomizeCards
   10. APIRequest
   11. CreditsDisplay
   12. SettingsConfig

3. Desarrollo de GameFlow

   1. Hilo principal del juego
   2. Lógica de las mecánicas
   3. Lógica e integración de todas las clasesAPI y base de datos para que entre todos los elementos de construya el hilo del juego
   4. Integración de todos los elementos escenciles de la jugabilidad del videojuego

4. Coordinación y ajustes en la interacción de todas las clases entre sí, su interacción con Unity, y ajustes en el balanceo de mecánicas y de reglas

   1. Ajuste de tiempos de partida
   2. Ajuste de errores y bugs en el GameFlow o en los menús

5. Desarrollo de clases de Coordinación de música y Efectos sonoros

   1. Track
   2. SoundEffect

6. Prueba unitarias de las funcionalidades, pruebas de calidad y corrección de ajustes mínimos
