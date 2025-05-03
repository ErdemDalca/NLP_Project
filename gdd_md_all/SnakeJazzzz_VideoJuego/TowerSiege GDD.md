# **Tower Siege**

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

En "Tower Siege", dos jugadores se enfrentan en una batalla estratégica con el objetivo de destruir la torre principal del rival, con la ayuda de  mazos de cartas las cuales representan varias unidades para atacar al oponente mientras las suyas defienden. El dominio de creación de mazo, posicionamiento de unidades y la gestión de recursos es clave para la victoria en este competitivo juego 2D para computadoras.

---

### **Jugabilidad**

#### **General**
El juego empieza al enseñarle a los jugadores en que tablero (mapa) de la la partida. Después los jugdaores seleccionan un mazo prehecho o crean uno en el momento. Al usar una carta en el tablero hará que aparezca el personaje de la carta en el lugar colocado. Cada carta tiene un costo de recursos para desplegar y un cooldown después de que haya sido usada. El juego desafía a los jugadores a gestionar estos recursos, desplegar unidades estratégicamente, y conquistar las torres centrales para obtener una ventaja para poder destruir la torre principal del rival.

#### **Creación de Mazos**
El jugador crea un mazo de 40 cartas de un pool de 20 tipos de cartas, consistiendo en que el jugador pueda tener cartas repetidas si quiere. El jugador no sabe que baraja escogió su contrincante.

#### **Torres Centrales**
Al conquistar las torres centrales, estas amplían el espacio donde el jugador dueño puede colocar sus cartas. Al inicio de la partida las torres centrales son neutras y los jugadores tiene que pelear para conquistarlas. Para conquistar una torre central tus tropas tienen que hacer cierto daño, lo cual se vera reflejado en una barra de vida arriba de la torre. El jugador dueño de la unidad que le de el ultimo golpe de dicha barra a la torre central y haga que la barra se llene de nuevo; se vuelve dueño de la torre y obtiene sus ventajas.

#### **Mano, Mazos y Cooldown de cartas**
Los jugadores empiezan la partida con 6 cartas "en mano" o disponibles para colocar en campo de batalla. Al despegar una de estas se les dara otra carta proveniente de su mazo revuelto. El jugador puede colocar muchas cartas si es que tiene los recursos para hacerlo pero solo podra tener un maximo de 6 cartas en mano. Las cartas colocadas se descartan, y cuando todo el mazo del jugador sea descartado. Las cartas descartas se revolveran tras realizar su cooldown y podra volver a obtener 6 cartas en mano. Este proceso va durar 7s dandole al oponente una ventana de oportunidad al oponente donde podra atacar sin que el otro jugador pueda colocar cartas.

#### **Victoria**
La victoria se alcanza destruyendo las torres principales del oponente, en el caso de haberse acabado el tiempo de partida; el jugador que haya hecho más daño al oponente gana, por otra parte, en caso de que el daño realizado sean iguales, comenzará el "sudden death" donde gana el primero en hacer al menos un punto de daño a una torre principal.

---

### **Mentalidad**

El juego busca invocar una mentalidad de planificación estratégica y adaptabilidad. Los jugadores deberían sentir la tensión de la gestión de recursos, la emoción de romper las defensas exitosamente, y la necesidad de adaptarse constantemente al campo de batalla en evolución.

La estarategia del juego tiene muchas facetas, desde la creación de mazo, administración de recursos, el posicionamiento y control del tiempo para la colocación de cartas, la estarategia para llegar a las torres, etc.

---

## _Técnico_

---

### **Pantallas**

---

#### **Pantalla de Título**
La primera impresión del juego, donde los jugadores pueden acceder a todas las funcionalidades principales del juego. Esta pantalla incluye:

- **Iniciar Sesión/Registro**: Lleva a los jugadores a la pantalla de Log In para iniciar sesión o registrarse.
- **¿Cómo Jugar?**: Un tutorial interactivo y documento de instrucciones para nuevos jugadores.
- **Opciones**: Configuraciones del juego, incluyendo volumen y teclas personalizables.
- **Créditos**: Información sobre el equipo de desarrollo y agradecimientos.
- **Salir**: Opción para cerrar el juego.

#### **Pantalla de Log In/Registro**
Antes de acceder a la configuración de la partida y opciones del juego, los jugadores son dirigidos a la pantalla de Log In, asegurando que sus progresos y estadísticas puedan ser guardados y rastreados correctamente. Esta pantalla ofrece:

- **Log In**: Los jugadores existentes pueden ingresar su usuario y contraseña para acceder a sus perfiles.
- **Registro**: Nuevos jugadores pueden crear una cuenta, proporcionando un usuario, correo electrónico y contraseña.

#### **Iniciar Partida**
Esta pantalla guía a los jugadores a través de la configuración de una partida, incluyendo:

- **Mapa de Partida**: Selección de uno de los varios mapas disponibles, cada uno con sus propios desafíos y características.
- **Elegir Mazo**:
    - **Listas de Mazos Disponibles**: Visualización y selección de mazos previamente creados.
    - **Crear Mazo**: Herramienta para crear un nuevo mazo de cartas.

#### **Partida**
La pantalla principal del juego donde ocurre la acción. Incluye:

- **Mano (Cartas Disponibles)**: Muestra las cartas que el jugador puede jugar actualmente, con detalles sobre coste de recursos.
- **Menu de Pausa**: Accesible durante la partida para pausar el juego, con opciones para reanudar o salir de la partida.

#### **Pantalla de Victoria/Derrota**
Al finalizar una partida, los jugadores son dirigidos a esta pantalla, que muestra el resultado de la partida y ofrece opciones para volver al menú principal, jugar otra partida, o revisar las estadísticas del juego recién terminado.

#### **Selección de Mazo**
Una interfaz dedicada a la gestión de mazos, donde los jugadores pueden:

- **Crear Mazo**: Interface para la creación de nuevos mazos, con acceso a todas las cartas disponibles.
- **Listas de Mazos**: Visualización y edición de mazos existentes.
- **Todas las Cartas**: Exploración de todas las cartas disponibles, incluyendo descripciones y estadísticas.

#### **¿Cómo Jugar?**
Una sección educativa que proporciona:

- **Documento de Instrucciones**: Guía detallada sobre cómo jugar "Tower Siege", incluyendo reglas, consejos y estrategias.

#### **Opciones**
Permite a los jugadores personalizar su experiencia de juego, ajustando:

- **Volumen**: Control de volumen para música y efectos de sonido.
- **Teclas Personalizables**: Configuración de controles de teclado para adaptarse a las preferencias del jugador.

Al mejorar la descripción de las pantallas, se busca proporcionar una experiencia de usuario fluida y accesible, asegurando que los jugadores puedan navegar fácilmente por el juego y acceder a todo lo que necesitan para una experiencia de juego inmersiva y satisfactoria.

---

### **Controles**

- **Ratón**: Navegar por los menús, seleccionar cartas y mazos, colocar unidades.
- **Teclado**: Atajos para la selección de cartas, manejo de tropas, menu de pausa, etc.

---

### **Mecánicas**

---

### **Generación de Recursos**
- **Dinámica**: Los recursos son la moneda de juego utilizada para desplegar cartas en el campo de batalla. Los jugadores comienzan cada partida con una cantidad inicial de recursos y estos se generan automáticamente a una tasa constante a lo largo del juego.
- **Estrategia**: La gestión eficaz de recursos es crucial para el éxito. Los jugadores deben decidir cuándo ahorrar recursos para desplegar unidades más poderosas o cuándo gastarlos rápidamente para ganar ventaja táctica.

### **Despliegue de Unidades**
- **Mecánica**: Las unidades se despliegan en el campo de batalla mediante una interfaz de arrastrar y soltar, permitiendo a los jugadores elegir estratégicamente la posición inicial de sus unidades.
- **Estrategia**: La posición de las unidades puede afectar significativamente el resultado de la batalla. Colocar unidades defensivas al frente puede proteger a las unidades de ataque más vulnerables detrás.

### **Interacción con el Terreno**
- **Dinámica**: El campo de batalla cuenta con varios elementos de terreno, como montañas, bosques, ríos, y más. Cada tipo de terreno afecta a las unidades de manera diferente.
- **Estrategia**: Los jugadores deben usar el terreno a su favor, posicionando unidades en lugares que maximicen su efectividad mientras limitan las opciones de movimiento del oponente.

### **Manejo de Unidades Desplegadas**
- **Mecánica de Ataque de Unidades**: Una vez desplegadas, las unidades siguen patrones de ataque específicos basados en su tipo. Algunas unidades atacan al oponente o torre más cercano, siguiendo un enfoque de ataque general. Otras están especializadas y solo atacan las torres enemigas más cercanas, lo que las hace ideales para objetivos específicos de destrucción de estructuras.
- **Dirección y Reubicación**: Las unidades pueden ser dirigidas hacia objetivos específicos o reubicadas dentro del alcance de su movimiento mediante comandos simples. Esto permite a los jugadores adaptar su estrategia en tiempo real, reaccionando a los movimientos del oponente y al despliegue de unidades.
- **Estrategia de Despliegue y Ataque**: La elección de cuándo y dónde desplegar tipos específicos de unidades puede cambiar drásticamente el curso de la batalla. Utilizar unidades enfocadas en atacar enemigos para proteger o apoyar a las unidades especializadas en asedio puede crear una sinergia efectiva, permitiendo a los jugadores realizar ataques dirigidos y defender sus propias estructuras simultáneamente.
- **Adaptabilidad en el Campo de Batalla**: La habilidad para adaptar la formación de unidades y su enfoque de ataque es clave. Los jugadores deben gestionar estratégicamente el despliegue de unidades para aprovechar sus fortalezas, como realizar emboscadas, proteger unidades valiosas, o retirar unidades dañadas del combate para su recuperación.

### **Combate y Confrontación**
- **Dinámica**: Cuando las unidades entran en contacto con unidades enemigas, automáticamente entran en combate. La fuerza, velocidad, y habilidades especiales de cada unidad determinarán el resultado del enfrentamiento.
- **Estrategia**: Elegir el momento y lugar del combate es vital. Atacar cuando el oponente está recargando recursos o desde una posición ventajosa puede ser decisivo para ganar la batalla.

### **Conquista de Torres**
- **Mecánica**: Los jugadores pueden desplegar cartas específicas para atacar y conquistar torres enemigas, ganando ventajas estratégicas y puntos de victoria.
- **Estrategia**: Decidir cuándo centrarse en la conquista de torres frente a la defensa o el ataque directo al oponente requiere un equilibrio cuidadoso y puede cambiar la dinámica del juego.

---

## _Diseño de Niveles_

---

### **Temas**

#### **Campo de Batalla**
- **Ambiente**: Campo de batalla medieval; muy forestal, con caminos, arboles, lagos, ríos, torres de piedra, etc.
- **Ambientes Detallados**:
  - **Bosques Espesos**: Los árboles no solo añaden complejidad visual, sino que también pueden ofrecer cobertura táctica o ser obstáculos que los jugadores deben navegar.
  - **Cuerpos de Agua**: Lagos añaden barreras naturales, forzando a los jugadores a adaptar sus estrategias de movimiento y posicionamiento.
  - **Torres**: Elementos icónicos del paisaje que sirven como objetivos críticos y puntos de fortaleza para ambos competidores.
    
![Map1](/VideoGame/map1.png)

- **Objetos en el Campo de Batalla**:
  - **Interactivos**:
    - **Obstáculos Naturales**: Rocas y árboles pueden bloquear o desviar el avance, mientras que ríos y lagos limitan el acceso a ciertas áreas, requiriendo estrategias adaptativas.
    - **Objetivos Estratégicos**: La torre principal y torres centrales actúan como catalizadores de confrontaciones, con su conquista ofreciendo ventajas tácticas decisivas.
  - **Decorativos**: Elementos como rocas, estanques pequeños, y árboles añaden profundidad al mundo del juego, mejorando la inmersión sin afectar directamente la jugabilidad.

---

### **Flujo de Juego Estratégico**

1. **Selección de Mazo**: Cada jugador elige cuidadosamente un mazo de batalla, planeando su estrategia basada en las cartas disponibles y potenciales tácticas enemigas.

2. **Generación de Recursos**: Al inicio de la batalla, los jugadores comienzan a acumular recursos esenciales para el despliegue de unidades, estableciendo la base para la estrategia económica del juego.

3. **Despliegue Táctico de Unidades**: Utilizando el mazo seleccionado, los jugadores colocan unidades en el campo de batalla, con cada decisión influenciada por el diseño del nivel, la composición del mazo enemigo, y los objetivos estratégicos inmediatos.

4. **Conquista y Defensa**: La interacción dinámica entre atacar y defender torres centrales y la torre principal enemiga dicta el ritmo de la partida, con el terreno jugando un papel crucial en el éxito de estas maniobras.

5. **Victorias Condicionales**: La partida culmina con la destrucción de la torre principal de un jugador, pero las estrategias para llegar a este punto varían enormemente, influenciadas por el diseño del nivel y las decisiones tácticas.

---

## _Desarrollo_

---

### **Clases Abstractas / Componentes**

1. **Carta**
    - Atributos: Descripción, Vida, Velocidad, Daño, Velocidad de Ataque, Rango, Costo, Enemigos Objetivo, Tipo (Ataque/Defensa).

2. **Unidad**
    - Derivado de Carta: Soldado, Caballero, Arquero, Catapulta, Trol, Gigante, Fantasma, Goblin, Orco, Escudo, Healer, Mago, Dragon, Bruja, Sacerdote, Lanzador de Javalina, Asesino, Elemental de Fuego, Centauro, Nigromante.

3. **Torre**
    - Atributos: Vida, Daño, Rango de Ataque.

---
## **Listado de Clases a Programar**

- **Clase `Game`**:
  - **Responsabilidad**: Administrar el flujo del juego, el estado de la partida y las transiciones entre diferentes pantallas (menús, juego, victoria/derrota).
  - **Métodos importantes**:
    - `startGame()`: Inicia una nueva partida.
    - `pauseGame()`: Pausa la partida en curso.
    - `endGame()`: Finaliza la partida y muestra resultados.

- **Clase `Player`**:
  - **Responsabilidad**: Representar a cada jugador, manteniendo su puntuación, mazo de cartas y acciones disponibles.
  - **Propiedades**:
    - `deck`: Una colección de objetos `Card`.
    - `score`: Puntuación actual del jugador.
  - **Métodos**:
    - `playCard()`: Juega una carta del mazo.
    - `calculateScore()`: Actualiza la puntuación basada en el juego.

- **Clase `Card`**:
  - **Responsabilidad**: Definir las características y comportamiento de las cartas utilizadas en el juego.
  - **Propiedades**:
    - `cost`: Recursos necesarios para jugar la carta.
    - `cooldown`: Tiempo de espera antes de que la carta pueda ser utilizada nuevamente.
  - **Métodos**:
    - `activate()`: Ejecuta la acción de la carta cuando se juega.

- **Clase `Unit`**:
  - **Responsabilidad**: Actuar como la superclase para todas las unidades de combate en el juego, definiendo propiedades comunes y métodos.
  - **Propiedades**:
    - `health`: La salud actual de la unidad.
    - `damage`: El daño que la unidad puede infligir.
  - **Métodos**:
    - `move()`: Mueve la unidad en el campo de batalla.
    - `attack()`: Realiza un ataque a enemigos o estructuras.

- **Clase `Tower`**:
  - **Responsabilidad**: Controlar el estado y la defensa de las torres en el juego.
  - **Propiedades**:
    - `location`: La posición de la torre en el mapa.
    - `defense`: La capacidad defensiva de la torre.
  - **Métodos**:
    - `receiveDamage()`: Reduce la salud de la torre cuando es atacada.

- **Clase `Resource`**:
  - **Responsabilidad**: Gestionar los recursos del jugador, que son necesarios para desplegar unidades y realizar acciones.
  - **Propiedades**:
    - `amount`: La cantidad actual de recursos disponibles.
  - **Métodos**:
    - `generate()`: Incrementa los recursos con el tiempo.
    - `spend()`: Deduce los recursos al jugar cartas o realizar acciones.

- **Clase `AI`**:
  - **Responsabilidad**: Dirigir la lógica de los oponentes controlados por la computadora, permitiendo una jugabilidad desafiante y dinámica.
  - **Métodos**:
    - `determineStrategy()`: Decide una estrategia basada en el estado actual del juego.
    - `executeAction()`: Realiza una acción basada en la estrategia determinada.
---

### **Clases Derivadas / Composiciones de Componentes**

#### **Unidades**
![Map1](/VideoGame/sampleDeck.png)

- **Soldado**: 
  - Tipo: Común
  - Costo: 1
  - Daño: 15
  - Vida: 50
  - Alcance: 1 tile
  - Velocidad de movimiento: 1 tile/s
  - Velocidad de ataque: 1.5 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Caballero**: 
  - Tipo: Raro
  - Costo: 5
  - Daño: 25
  - Vida: 120
  - Alcance: 1 tile
  - Velocidad de movimiento: 2 tiles/s
  - Velocidad de ataque: 2 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Arquero**: 
  - Tipo: Común
  - Costo: 2
  - Daño: 20
  - Vida: 30
  - Alcance: 3 tiles
  - Velocidad de movimiento: 1 tile/s
  - Velocidad de ataque: 1 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Catapulta**: 
  - Tipo: Épico
  - Costo: 6
  - Daño: 40
  - Vida: 60
  - Alcance: 5 tiles
  - Velocidad de movimiento: 0.5 tile/s
  - Velocidad de ataque: 3 s
  - Enemigos objetivo: Estructuras
  - Tipo: Ataque

- **Trol**: 
  - Tipo: Raro
  - Costo: 7
  - Daño: 30
  - Vida: 150
  - Alcance: 1 tile
  - Velocidad de movimiento: 0.75 tile/s
  - Velocidad de ataque: 2.5 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Gigante**: 
  - Tipo: Legendario
  - Costo: 10
  - Daño: 70
  - Vida: 200
  - Alcance: 2 tiles
  - Velocidad de movimiento: 0.6 tile/s
  - Velocidad de ataque: 3 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Fantasma**:
  - Tipo: Épico
  - Costo: 7
  - Daño: 10 (ataque pasante)
  - Vida: 80
  - Alcance: 0 (ataque pasante)
  - Velocidad de movimiento: 1.5 tiles/s
  - Velocidad de ataque: 1 ataque cada que atraviesa una unidad
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque especial

- **Goblin**:
  - Tipo: Común
  - Costo: 2
  - Daño: 5
  - Vida: 25
  - Alcance: 1 tile
  - Velocidad de movimiento: 2.5 tiles/s
  - Velocidad de ataque: 1 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Orco**:
  - Tipo: Común
  - Costo: 3
  - Daño: 30
  - Vida: 100
  - Alcance: 1 tile
  - Velocidad de movimiento: 1 tile/s
  - Velocidad de ataque: 1.8 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Escudo**:
  - Tipo: Raro
  - Costo: 4
  - Daño: 10
  - Vida: 150
  - Alcance: 1 tile
  - Velocidad de movimiento: 0.8 tile/s
  - Velocidad de ataque: 2 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Defensa

- **Healer**:
  - Tipo: Épico
  - Costo: 6
  - Daño: 0
  - Vida: 40
  - Alcance: 3 tiles
  - Velocidad de movimiento: 1 tile/s
  - Velocidad de ataque: 2 s (ritmo de curación)
  - Enemigos objetivo: N/A (aliados)
  - Tipo: Soporte

- **Mago**:
  - Tipo: Raro
  - Costo: 7
  - Daño: 40 (daño en área)
  - Vida: 50
  - Alcance: 3 tiles
  - Velocidad de movimiento: 0.8 tile/s
  - Velocidad de ataque: 2.5 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Dragon**:
  - Tipo: Legendario
  - Costo: 10
  - Daño: 50 (daño en área)
  - Vida: 150
  - Alcance: 4 tiles
  - Velocidad de movimiento: 1 tile/s (vuelo)
  - Velocidad de ataque: 3 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Bruja**:
  - Tipo: Raro
  - Costo: 8
  - Daño: 25
  - Vida: 60
  - Alcance: 3 tiles
  - Velocidad de movimiento: 0.7 tile/s
  - Velocidad de ataque: 2 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque mágico

- **Sacerdote**:
  - Tipo: Épico
  - Costo: 7
  - Daño: 0
  - Vida: 70
  - Alcance: 3 tiles
  - Velocidad de movimiento: 1 tile/s
  - Velocidad de ataque: 2 s (ritmo de beneficio)
  - Enemigos objetivo: N/A (aliados)
  - Tipo: Soporte

- **Lanzador de Javalina**:
  - Tipo: Común
  - Costo: 4
  - Daño: 25
  - Vida: 40
  - Alcance: 3 tiles
  - Velocidad de movimiento: 1.2 tile/s
  - Velocidad de ataque: 1.7 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Asesino**:
  - Tipo: Raro
  - Costo: 6
  - Daño: 60
  - Vida: 30
  - Alcance: 1 tile
  - Velocidad de movimiento: 3 tiles/s
  - Velocidad de ataque: 1 s
  - Enemigos objetivo: Alta prioridad (healers, unidades de rango)
  - Tipo: Ataque

- **Elemental de Fuego**:
  - Tipo: Épico
  - Costo: 9
  - Daño: 45 (daño por quemadura)
  - Vida: 80
  - Alcance: 2 tiles
  - Velocidad de movimiento: 0.9 tile/s
  - Velocidad de ataque: 2 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Centauro**:
  - Tipo: Común
  - Costo: 5
  - Daño: 35
  - Vida: 80
  - Alcance: 2 tiles
  - Velocidad de movimiento: 2 tiles/s
  - Velocidad de ataque: 1.5 s
  - Enemigos objetivo: Cualquiera
  - Tipo: Ataque

- **Nigromante**:
  - Tipo: Legendario
  - Costo: 10
  - Daño: 20
  - Vida: 60
  - Alcance: 3 tiles
  - Velocidad de movimiento: 0.6 tile/s
  - Velocidad de ataque: 2.5 s (ritmo de invocación)
  - Enemigos objetivo: Cualquiera
  - Tipo: Soporte/Ataque


#### **Obstáculos**

- **Árbol&Roca**: Proporciona cobertura y es un obstaculo.
- **Lago**: Obstáculo natural que limita el movimiento; solo ciertas unidades pueden cruzarlo.

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
