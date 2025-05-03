# **Protect the Egg**

## _GDD: Documento de Diseño de Juego_

---

##### **Aviso de derechos de autor**

Pedro Mauri Mtz - A01029143

Michael Andrew Devlyn - A01781041

Tomás Molina Pérez Diez - A01784116

---

## _Índice_

---

1. [Índice](#índice)
2. [Diseño de Juego](#diseño-de-juego)
    1. [Resumen](#resumen)
    2. [Jugabilidad](#jugabilidad)
    3. [Mentalidad](#mentalidad)
3. [Técnico](#técnico)
    1. [Pantallas](#pantallas)
    2. [Controles](#controles)
    3. [Mecánicas](#mecánicas)
4. [Diseño de Niveles](#diseño-de-niveles)
    1. [Temas](#temas)
    2. [Flujo de Juego](#flujo-de-juego)
5. [Desarrollo](#desarrollo)
6. [Gráficos](#gráficos)
7. [Sonidos/Música](#sonidosmúsica)
8. [Cronograma](#cronograma)

## _Diseño de Juego_

---

### **Resumen**

En "Protect the Egg" participarás en una batalla estratégica contra hordas de monstruos. Con la ayuda de cartas convocarás a tus tropas con el objetivo de defender un huevo de dragón. El dominio de la creación de cubiertas, posicionamiento de unidades y estructuras, más la gestión de recursos es clave para la victoria en este competitivo juego de ordenador en 2D. ¿Durante cuántas hordas podrás protegerlo?

---

### **Jugabilidad**

#### **Juego**

Cada orda de monstruos es más dificil que la anterior, mientras que la misma orda en dos partida diferentes tienen resultados distintos con la misma dificultad. Esto le da una buena jugabilidad al tener variación entre las partidas.

#### **Premios / Recompensas**

Tras acabar cada partida, el juego guardará los datos de la partida (la horda máxima y mapa usado), los cuales se rankearán y presentarán en la página web, dandole un toque de competibidad por ver quien consigue más puntos.

---

### **Mentalidad**

El juego provoca una mentalidad de estratégica y adaptabilidad. Los jugadores deberían sentir la tensión de la gestión de recursos, la emoción de sobrevivir las ordas de monstruos. La estarategia del juego tiene muchas facetas, desde la creación de mazo, administración de recursos, el posicionamiento y control del tiempo para la colocación de cartas, etc.

---

## _Técnico_

---

### **Pantallas**

---

#### **Pantalla de "LogIn"**
Primer pantalla al entrar al juego.
**Iniciar Sesión**: Los jugadores existentes pueden ingresar su usuario y contraseña en esta escena para acceder al juego con la información de sus perfiles.
- **Boton a "CreateAccount"**: Lleva a los jugadores a la pantalla de Create Account.
- **Boton a salir**: Boton que permite salir del juego.

![LogIn](./fotos/LogIn.png)

#### **Pantalla de "CreateAccount"**
**Crear cuenta**: En esta escena, los jugadores podran crear una cuenta del juego proporcionando un username y una contraseña, la cual se guardará en la base de datos.
- **Boton a "LogIn"**: Lleva a los jugadores a la pantalla de Log In.
- **Boton a salir**: Boton que permite salir del juego.

![CreateAccount](./fotos/CreateAccount.png)

#### **Pantalla de Menu**
- **Boton de "Play"**: Lleva a los jugadores a la escena "MapsMenu".
- **Boton de "Decks"**: Lleva a los jugadores a la escena de selección de "DecksMenu".
- **Boton de Opciones de audio**: Abre el marco para poder manipular los niveles de sonido del juego.
- **Boton de "Log Out"**: Opción para cerrar sesión y regresar a la pantalla de "LogIn".

![Menu](./fotos/Menu.png)

#### **Marco de opciones de audio**
- **Barra de "Music Volume"**: Barra para editar el volumen de la musica del juego.
- **Barra de "SFX Vokume"**: Barra para editar el volumen de los efectos de sonido del juego.
- **Boton de regresar**: Boton para regresar a la escena de Menu.

![MenuVolume](./fotos/MenuVolume.png)

#### **Pantalla de "MapsMenu"**
- **Boton de "Sea Side"**: Si el jugador tiene un mazo seleccionado, lleva al jugador la escena de GUI en conjunto con la escena de "SeaSide".
- **Boton de "Village"**: Si el jugador tiene un mazo seleccionado, lleva al jugador la escena de GUI en conjunto con la escena de "Village".
- **Boton de "Enchanted Forest"**: Si el jugador tiene un mazo seleccionado, lleva al jugador la escena de GUI en conjunto con la escena de "EnchantedForest".
- **Boton de regresar**: Boton para regresar a la escena de Menu.

![MapsMenu](./fotos/MapsMenu.png)

#### **Pantalla de "DecksMenu"**
- **Boton de "Create new deck"**: Este boton llevará al jugador a la escena de "CreateDeck"
- **Boton de primer mazo**: Al seleccionar este boton, se seleccionará el mazo guardado y aparecerán los botones de "Edit Deck" y "Delete Deck".
- **Boton de segundo mazo**: Al seleccionar este boton, se seleccionará el mazo guardado y aparecerán los botones de "Edit Deck" y "Delete Deck".
- **Boton de tercer mazo**: Al seleccionar este boton, se seleccionará el mazo guardado y aparecerán los botones de "Edit Deck" y "Delete Deck".
- **Boton de cuarto mazo**: Al seleccionar este boton, se seleccionará el mazo guardado y aparecerán los botones de "Edit Deck" y "Delete Deck".
- **Boton de quinto mazo**: Al seleccionar este boton, se seleccionará el mazo guardado y aparecerán los botones de "Edit Deck" y "Delete Deck".
- **Boton de "Edit deck"**: Este boton llevará al jugador a la escena de "CreateDeck" para editar el mazo seleccionado.
- **Boton de "Delete deck"**: Este boton borrará el deck seleccionado.
- **Boton de regresar**: Boton para regresar a la escena de Menu.

![DecksMenu](./fotos/DecksMenu.png)

#### **Pantalla de "CreateDeck"**
- **Interfaz de cartas**: Se ve una imagen de todas las cartas del juego con botones de "+" y "-" a un lado para agregar o eliminar las cartas del mazo, cada imagen de carta es un boton que muestra la "interfaz de stats".
- **Interfaz de stats**: Se ve una lista las stats de la carta seleccionada.
- **Nombre del mazo**: Espacio para escribir y guardar el nombre del mazo.
- **Boton de aceptar**: Este boton guardará el mazo tras finalizarlo.
- **Boton de regresar**: Boton para regresar a la escena de "DecksMenu".

![CreateDeck](./fotos/CreateDeck.png)

#### **Pantalla de GUI**
- **Mapa de Partida**: Mapa seleccionado desde la escena de "MapsMenu".
- **Cartas en mano**: Cartas disponibles para usar, junto con su costo de elixir.
- **Mazo**: Mazo con contador de cartas restantes.
- **Elixir**: Contador de elixir más su barra de valor.
- **Hordas**: Contador de horda de mosntruos actual.
- **Boton de pausa**: Muetra a los jugadores el menu de pausa.

![GUI](./fotos/GUI.png)

#### **Pantalla de Menu de pausa**
- **Pantalla de partida de fondo**: Momento de la partida en la que se pausoó el juego.
- **Boton de reanudar**: Reanuda la partida.
- **Boton de regresar**: Boton para regresar a la escena de Menu.
- **Boton de Opciones de audio**: Abre el marco para poder manipular los niveles de sonido del juego.

![Pause](./fotos/Pause.png)

#### **Pantalla de EndGame**
Al finalizar una partida, los jugadores son dirigidos a esta pantalla, que muestra el resultado de la partida.
- **Boton de regresar**: Boton para regresar a la escena de Menu.
- **Salir**: Saca a los jugadores del juego.

![EndGame](./fotos/EndGame.png)

---

### **Controles**

- **Ratón**: Navegar por los menús, seleccionar cartas y mazos, colocar unidades.
- **Teclado**: Atajos para la selección de cartas, manejo de tropas, menu de pausa, etc.

---

### **Mecánicas**

---

#### Antes de partida:

Antes de la partida deberas seleccionar un mazo para usar, si no lo haces no podras jugar. Y finalmente tras elegir el mapa en el que quieres jugar, comenzará la partida!

#### Selección y Creación de mazos:

Para jugar, debes crear almenos un mazo de los 5 disponibles, cada mazo debe de tener 20 cartas exactas y un nombre para poderse guardar, las cartas se pueden repetir siempre y cuando el total sea 20, tambien se encontrará toda la información de cada carta para poder elegir con conciencia cliqueando en el 'Artwork' de la carta.

#### Selección de Mapa:

Tras elegir tu mazo, debes de elegir en cual de los 3 mapas jugarás, al clickear en el botón del mapa elegido, se comenzará la partida con tu mazo seleccionado y mapa elegido.

#### En partida:

El objetivo principal del juego consiste en proteger un huevo de dragón el cual es atacado por hordas de monstruos, por medio de cartas de invocación de personajes (NPC) y estrucutras.

#### Elixir:

Para invocar cartas, dispones de elixir de dragón como recurso de invocación, la cantidad inicial es de 10 puntos de elixir y aumenta en 10 puntos cada 10 segundos, el límite de almacenamiento es de 50 puntos totales de elixir al mismo tiempo, si intentas ahorrar una cantidad mayor a esta, los puntos de elixir correspondientes se quemarán. Cada carta tiene un costo para desplegar y puedes ver la cantidad de elixir que dispones en la esquina superior izquierda de cada carta.

#### Para usar una carta:

Para moverte entre las cartas de tu mano; se seleccionan con las teclas; 1, 2, 3, 4, 5 y 6. Mientras que con click derecho en el mapa, el personaje o estrucutra se colocará en la posición del mouse. Ten en cuenta que hay una zona limitada para invocar cartas, si intentas colocarla fuera de esta zona,
no se colocará la carta y se marcará el límite de la zona para que lo vuelvas a intentar.

Revolver mazo:
Tras haber usado las 20 cartas de tu mazo; estas se volverán a revolver para que las puedas volver a usar, este proceso dura 5 segundos, en los cuales no podrás usar ninguna carta, pon atención al lado derecho de las cartas "en mano", ya que se encuentra el contador de cartas restantes en el mazo.

#### Hordas de monstruos:

Las hordas de monstruos irán subiendo su dificultad progresivamente hasta que pierdas, el contador de la orda en la que te encuentras se ubica en el centro de la parte superior.

---

## _Diseño de Niveles_

---

### **Temas**

#### **Sea Side**
- **Ambiente**: Campo de batalla medieval; muy forestal; con arboles y casas delimitando los límites del nivel junto con una enorme costa de con un enorme cuerpo de agua.
- **Ambientes Detallados**:
  - **Torres**: Elementos icónicos del paisaje que sirven como objetivos críticos y puntos de fortaleza.
  - **Casas**: Casas diseñadas en la época en la que esta inspirado el juego, para darle ese toque medieval.
  - **Arboles**: Pinos que le dan el toque forestal al nivel.
  - **Cuerpo de Agua**: Cuerpo de agua natural que le da una ambientación distinta a la de un bosque común.

![SeaSide](./fotos/SeaSide.png)

#### **Village**
- **Ambiente**: Campo de batalla medieval; con casas y edificios colocados por todo el mapa, muros de piedra que delimitan el limite del campo y casas de decoración.
- **Ambientes Detallados**:
  - **Torres**: Elementos icónicos del paisaje que sirven como objetivos críticos y puntos de fortaleza.
- **Casas y muralla**: Casas diseñadas en la época en la que esta inspirado el juego, para darle ese toque medieval.
  - **Arboles**: Pinos que le dan el toque forestal al nivel.

![Village](./fotos/EnchantedForest.png)

#### **Enchanted Forest**
- **Ambiente**: Campo de batalla medieval; muy forestal; con arboles colocados por todo el mapa y delimitando los límites del nivel.
- **Ambientes Detallados**:
  - **Torres**: Elementos icónicos del paisaje que sirven como objetivos críticos y puntos de fortaleza.
  - **Arboles**: Pinos que le dan el toque forestal al nivel.

![EnchantedForest](./fotos/EnchantedForest.png)

- **Objetos en el Campo de Batalla**:
  - **Interactivos**:
    - **Obstáculos Naturales**: Rocas y árboles pueden bloquear o desviar el avance, mientras que ríos y lagos limitan el acceso a ciertas áreas, requiriendo estrategias adaptativas.
    - **Objetivos Estratégicos**: La posición del huevo y de las torres de protección actúan como catalizadores de confrontaciones, con su destrucción ofreciendo ventajas tácticas decisivas.
  - **Decorativos**: Elementos como los árboles que le añaden profundidad al mundo del juego, mejorando la inmersión sin afectar directamente la jugabilidad.

---

### **Flujo de Juego Estratégico**

1. **Selección de Mazo**: Cada jugador elige cuidadosamente un mazo de batalla, planeando su estrategia basada en las cartas disponibles.

2. **Generación de Recursos**: Al inicio de la batalla, el jugador comienza a acumular el elixir esencial para el despliegue de unidades, estableciendo la base para la estrategia económica del juego.

3. **Despliegue Táctico de Unidades**: Utilizando el mazo seleccionado, los jugadores colocan unidades en el campo de batalla, con cada decisión influenciada por el diseño del nivel, la composición del mazo enemigo, y los objetivos estratégicos inmediatos.

4. **Victorias Condicionales**: La partida culmina con la destrucción del huevo de dragón del jugador, el objetivo principal del jugador consiste en sobrevivir la mayor cantidad de hordas que le sea posible con el maso que utiliza.

---

## _Desarrollo_

---

### **Clases Abstractas / Componentes**

1. **Carta**
    - Atributos: cardName, description, cost, numberOfNPCs y IDNPC.

2. **Unidades**
    - Derivado de Carta: Knight, Archer, Goblin, Giant, Mage, Ghost, Orc, Assasin, Centaur, Elf, Berserker, Ice Sorceress, Stone Golem, Troll, Scout, Cannon, Mortar Tower, Archer Tower, Inferno Tower, Wizard Tower.
    - Atributos: name, health, speed, sttack, attackCooldown, range, isStructure, attackTowers, attackEnemies.
    3. **Torre Default**
    - Atributos: name, health, speed, sttack, attackCooldown, range, isStructure, attackTowers, attackEnemies.
    4. **Huevo de dragón**
    - Atributos: health.

---

### **Listado de Scripts a Programar**

- **Clase `Cards`**:
  - **Card**
  - **CardDisplay**
  - **CardUICounter**
  - **MenuCard**

- **Clase `CardSpawner`**:
  - **AlertsManager**
  - **CardSOSystem**
  - **CardsUIManager**
  - **ClickArea**
  - **InputSystem 1**
  - **Shuffler**
  - **Spawner**
  - **Starter**

- **Clase `DeckBuild`**:
  - **CardAdder**
  - **CardCounter**
  - **DeckBuilder**
  - **DeckBuilderManager**
  - **DeckData**
  - **GetAllCards**
  - **Populator**
  - **PostDeck**
  - **PostDeck**
  - **PutDeck**
  - **SaveLocal**
  - **StatsShower**

- **Clase `DeckBuild`**:
  - **Elixir**
  - **ElixirGenerator**
  - **ElixirSetter**
  - **ElixirUI**

- **Clase `Events`**:
  - **GameEvent**
  - **GameEventListener**
  - **GameOver**

- **Clase `LogIn`**:
  - **Button**
  - **CreateAccountEndpoint**
  - **LogInCheck**
  - **LogInEndpoint**
  - **UserInformation**
  - **UsernameValidator**

- **Clase `Mazos`**:
  - **DeckClasses**
  - **LoadDecks**

- **Clase `Menus`**:
  - **GUIGetter**
  - **MainMenu**
  - **PauseMenu**
  - **DeckButton**
  - **DeckMenuSceneButton**
  - **DeleteDeck**
  - **PopulateButtons**
  - **SceneLoader**
  - **Selector**
  - **mapsMenu**

- **Clase `NPC Manager`**:
  - **NPCManager**

- **Clase `PlayStats`**:
  - **PartidaInfo**
  - **ScoreManager**
  - **SessionAPIHandler**

- **Clase `PrefabScripts`**:
  - **ClosestFinder**
  - **Damageable**
  - **Destruction**
  - **HBar**
  - **HealthBarColor**
  - **HealthBarValue**
  - **Health**
  - **NPCController**
  - **NPCSystem**
  - **ProyectileAttack**
  - **PushMovement**
  - **RangeFinder**
  - **SingleAttack**
  - **SplashAttack**
  - **StopMovement**

- **Clase `ProyectileScripts`**:
  - **PController**
  - **PMovement**
  - **PParabolaMovement**
  - **PSingleAttack**
  - **PSplashDamage**

- **Clase `RuntimeSets`**:
  - **RSCards**
  - **RSGameObject**
  - **RSNPCStats**
  - **RSRCards**
  - **RSRGameObject**
  - **RuntimeSet**

- **Clase `SoundManager`**:
  - **OptionsController**
  - **SoundManager**

- **Clase `Stats`**:
  - **NPCStats**

- **Clase `TeamColorSO`**:
  - **TeamColors**

- **Clase `Waves`**:
  - **EnemyInfo**
  - **WaveCounter**
  - **WaveOverChecker**
  - **WaveSpawner**
  - **Wave**
  - **WaveList**

---

### **Cartas:**

---

#### **Unidades**

- **Knight**:
  - Health: 400
  - Speed: 1
  - Attack: 70
  - Attack Cooldown: 1.5
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Front-line combat"
  - Coste: 5
  - Numero de NPCs: 1
  - ID: 1

- **Archer**:
  - Health: 150
  - Speed: 1
  - Attack: 40
  - Attack Cooldown: 0.8
  - Range: 10
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Quick and ranged"
  - Coste: 10
  - Numero de NPCs: 2
  - ID: 2

- **Goblin**:
  - Health: 50
  - Speed: 2
  - Attack: 35
  - Attack Cooldown: 0.5
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Strikes and distractions"
  - Coste: 5
  - Numero de NPCs: 3
  - ID: 3

- **Giant**:
  - Health: 1000
  - Speed: 1
  - Attack: 450
  - Attack Cooldown: 1.5
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Very resilient"
  - Coste: 30
  - Numero de NPCs: 1
  - ID: 4

- **Mage**:
  - Health: 250
  - Speed: 1
  - Attack: 30
  - Attack Cooldown: 1.5
  - Range: 10
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Can deal area damage"
  - Coste: 15
  - Numero de NPCs: 1
  - ID: 5

- **Ghost**:
  - Health: 200
  - Speed: 1
  - Attack: 55
  - Attack Cooldown: 0.8
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Sumons other ghost"
  - Coste: 12
  - Numero de NPCs: 4
  - ID: 6

- **Orc**:
  - Health: 350
  - Speed: 1.5
  - Attack: 65
  - Attack Cooldown: 1
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Strong and study"
  - Coste: 8
  - Numero de NPCs: 1
  - ID: 7

- **Assasin**:
  - Health: 250
  - Speed: 2
  - Attack: 150
  - Attack Cooldown: 0.5
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "High damage and speed"
  - Coste: 12
  - Numero de NPCs: 1
  - ID: 8

- **Centaur**:
  - Health: 450
  - Speed: 1
  - Attack: 100
  - Attack Cooldown: 1.5
  - Range: 2
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Versatile"
  - Coste: 8
  - Numero de NPCs: 1
  - ID: 9

- **Elf**:
  - Health: 200
  - Speed: 1.5
  - Attack: 70
  - Attack Cooldown: 1.5
  - Range: 15
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Long-range arracks"
  - Coste: 25
  - Numero de NPCs: 1
  - ID: 10


- **Berserker**:
  - Health: 450
  - Speed: 1
  - Attack: 100
  - Attack Cooldown: 0.8
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Fierce warriors causing"
  - Coste: 10
  - Numero de NPCs: 1
  - ID: 11

- **Ice Sorceress**:
  - Health: 500
  - Speed: 1
  - Attack: 50
  - Attack Cooldown: 0.8
  - Range: 5
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Tactical advantage"
  - Coste: 12
  - Numero de NPCs: 1
  - ID: 12

- **Stone Golem**:
  - Health: 1250
  - Speed: 1
  - Attack: 150
  - Attack Cooldown: 3
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "A living tank"
  - Coste: 20
  - Numero de NPCs: 1
  - ID: 13

- **Troll**:
  - Health: 650
  - Speed: 1
  - Attack: 120
  - Attack Cooldown: 2
  - Range: 1
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Strong and resilient"
  - Coste: 7
  - Numero de NPCs: 1
  - ID: 14

- **Scout**:
  - Health: 200
  - Speed: 3
  - Attack: 50
  - Attack Cooldown: 1
  - Range: 2
  - isStructure?: 0
  - Attack Towers?: 1
  - Attack Enemies?: 1

  - Description: "Fast and agile"
  - Coste: 6
  - Numero de NPCs: 2
  - ID: 15

#### **Estructuras**:

- **Cannon**:
  - Health: 500
  - Speed: 0
  - Attack: 80
  - Attack Cooldown: 1.5
  - Range: 8
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Ideal for defense"
  - Coste: 25
  - Numero de NPCs: 1
  - ID: 16

- **Catapult**:
  - Health: 400
  - Speed: 1
  - Attack: 50
  - Attack Cooldown: 3
  - Range: 17
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Great range"
  - Coste: 40
  - Numero de NPCs: 1
  - ID: 17

- **Mortar Tower**:
  - Health: 450
  - Speed: 0
  - Attack: 45
  - Attack Cooldown: 1
  - Range: 8
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Fortified position"
  - Coste: 35
  - Numero de NPCs: 1
  - ID: 18

- **Archer tower**:
  - Health: 650
  - Speed: 0
  - Attack: 45
  - Attack Cooldown: 1
  - Range: 8
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Coverting/ range"
  - Coste: 35
  - Numero de NPCs: 1
  - ID: 19

- **Inferno Tower**:
  - Health: 1500
  - Speed: 0
  - Attack: 800
  - Attack Cooldown: 2.5
  - Range: 10
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Ideal bigDamage"
  - Coste: 40
  - Numero de NPCs: 1
  - ID: 20

- **Wizard Tower**:
  - Health: 700
  - Speed: 0
  - Attack: 60
  - Attack Cooldown: 1.5
  - Range: 10
  - isStructure?: 1
  - Attack Towers?: 0
  - Attack Enemies?: 1

  - Description: "Casts spells"
  - Coste: 40
  - Numero de NPCs: 1
  - ID: 21

---

## _Gráficos_

---

### **Atributos de Estilo**

- **Colores**: Vibrantes, colores de equipo distintos para claridad
- **Estilo**: Semi-realista con elementos estilizados, asegurando que las unidades y el terreno sean fácilmente distinguibles.
- **Retroalimentación**: Explosiones para unidades destruidas, contornos brillantes para unidades seleccionables.

### **Gráficos Necesarios**

1. **Unidades**: Sprites animados para cada tipo de unidad.
2. **Terreno**: Texturas variadas para diferentes terrenos (césped, agua, arbol).
3. **Efectos**: Efectos visuales para ataques, recolección de recursos.

### **Listado de Assets**

- Sprites de personajes
- Texturas de terreno
- Elementos de UI (botones, barras de vida, indicadores de recursos)
- Iconos de habilidades y hechizos
- Efectos visuales (explosiones, efectos mágicos, etc.)
- Fondos y paisajes
- Assets de decoración (árboles, rocas, estructuras)

## _Sonidos/Música_

---

### **Atributos de Estilo**

- **Instrumentos**: Partituras orquestales con un ritmo dinámico que refleja la intensidad del juego.
- **Efectos de Sonido**: Choque de espadas, pasos de marcha y ruidos de construcción para una jugabilidad inmersiva.

---

### **Sonidos Necesarios**

1. **Movimientos de Unidades**: Cada tipo de unidad tiene sonidos de pasos distintos.
2. **Combate**: Diferentes sonidos para ataques cuerpo a cuerpo, a distancia y de asedio.
3. **Ambientales**: Ambiente de fondo que refleja el terreno actual.

---

### **Música Necesaria**

1. **Tema Principal**: Una pieza orquestal heroica que establece el tono épico del juego.
2. **Música de Batalla**: Música rápida e intensa que se reproduce durante el combate, con variaciones dependiendo de la etapa de la batalla.
3. **Temas de Victoria/Derrota**: Temas distintos que se reproducen al ganar o perder una partida, capturando el ambiente de triunfo o pérdida.
4. **Música de Menú**: Música de fondo sutil y atmosférica para los menús del juego y la pantalla de selección de mazo.

---

## _Cronograma_

---

1. **Fase de Concepto y Diseño** (sem 1-2)
    - Finalizar concepto de juego, mecánicas y documento de diseño.
    - Comenzar arte preliminar y bocetos conceptuales.

2. **Fase de Desarrollo** (sem  3-5)
    - Desarrollar mecánicas de juego principales e implementar jugabilidad básica.
    - Crear niveles iniciales y probar equilibrio.
    - Implementar elementos básicos de UI y controles.

3. **Producción de Arte y Sonido** (sem 6-8)
    - Finalizar todos los activos gráficos incluyendo personajes, entornos y UI.
    - Grabar e integrar efectos de sonido y pistas musicales.

4. **Pruebas y Refinamiento** (sem 9-10)
    - Realizar sesiones de prueba para recopilar comentarios.
    - Refinar jugabilidad, equilibrar unidades y pulir gráficos/sonido.

5. **Preparación para el Lanzamiento** (sem 11)
    - Lanzar el juego.

6. **Soporte Post-Lanzamiento** (Continuo)
    - Monitorear comentarios de los jugadores y abordar cualquier problema con actualizaciones.
    - Lanzar contenido adicional (p.ej., nuevas unidades, mapas) basado en la demanda de los jugadores.

---
