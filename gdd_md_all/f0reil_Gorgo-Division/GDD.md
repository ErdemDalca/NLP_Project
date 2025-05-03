<div align="center">
   
# Medusa's Requiem - Game Design Document

</div>

## Índice
1. [Descripción](#descripción)
2. [Historia](#historia)
3. [Jugabilidad](#jugabilidad)
   - [Mecánica](#mecánica)
   - [Dinámica](#dinámica)
   - [Estética](#estética)
4. [Menús y modos de juego](#menús-y-modos-de-juego) 
   - [Configuración](#configuración)
   - [Interfaz y control](#interfaz-y-control)
5. [Contenido](#contenido)
   - [Niveles](#niveles)
   - [Personajes y enemigos](#personajes-y-enemigos)
   - [Objetos](#objetos)
6. [Referencias](#referencias) 
## Descripción
Se trata de un juego de *thriller*-puzzles en vista *top-down* en que un héroe se introduce en la cueva de Medusa. Deberá sobrevivir a estatuas vivientes y finalmente a su creadora, haciendo un uso inteligente de su antorcha y desplazándose por las salas de la cueva de forma sigilosa, precavida y meticulosa.

## Historia  
El juego nos permitirá encarnar a un joven aspirante a héroe que, inspirado por las historias de los grandes (heracles, perseo, odiseo…), decide adentrarse en la cueva de la famosa gorgona Medusa en busca de fama y riquezas, sin tener en cuenta que tendrá que enfrentarse a todos los anteriores ingenuos que, como él, pensaron que podrían salir para contarlo. 
Armado con tan solo una antorcha, que se consume con rapidez, deberá mantener a raya a las estatuas que guardan la cueva y sus secretos.

## Jugabilidad
### Mecánica
  - **Mecánica del personaje**
    - Desplazamiento  por las salas de la cueva.
    - Arrastre de objetos (p. ej. piedras).
    - Abrir puertas/cambiar de sala.
    - Iluminación mediante la antorcha y recargue de la antorcha. Opción de colocar la antorcha en el suelo.
    - Vida: El personaje muere si entra en contacto con un enemigo.
    - Duración de la llama: Disminuye con el tiempo y se apaga al agotarse, dejando al jugador sin visibilidad.

  - **Mecánica del escenario**
      - Enemigos:
        - Estatuas genéricas: persiguen al protagonista siempre y cuando no estén iluminadas por la luz y hacen ruido al desplazarse para advertir al jugador. 
        - Medusa: enemigo único. Funciona a modo de jefe final, intentando atrapar al jugador y no se detiene si es iluminada. Además, el jugador no puede mirarla de frente porque quedará petrificado.
      - Trampas: 
        - Pinchos: El jugador muere en caso de que entre en contacto con ellos.
        - Corrientes de viento: Disminuye el tiempo de la barra de fuego si el jugador choca con ellas.
      - Puertas entre salas: 
        - En todos los niveles hay una puerta que te lleva a la siguiente sección. Para atravesarla el jugador tiene que llegar a ella, sin embargo puede suceder que la puerta esté bloqueada. En ese caso el jugador tendrá que superar algún puzzle o prueba para poder desbloquearla.
      - Objetos interactuables:
        - Algunos objetos funcionan a modo de llave, por lo que es necesario que el jugador los recoja para poder abrir una puerta o interactuar con otro objeto. Una vez recogidos, los objetos estarán en el inventario del protagonista y cuando se usen desaparecerán.
      - Antorchas
        - Iluminan el espacio alrededor del jugador.
      - PowerUps
        - Velocidad: Al cogerlo el jugador consigue mayor velocidad de movimiento.
        - Tiempo: Este PowerUp añade a la barra de fuego de la antorcha más tiempo. 

  - **Controles**
    - El jugador controla únicamente al protagonista de la historia. Con el teclado controla el movimiento en los ejes principales, X e Y, y con el ratón la dirección a la que mira.
    - Mapeo de acciones:
      - “WASD” o flechas del teclado para el movimiento del personaje.
      - Movimiento del ratón para el control de la dirección de apuntado del personaje.
      - “E” para interactuar con objetos.
      - “P” para acceder al menú de pausa.
      - “X” para colocar antorcha en el suelo.
      - “C” coger antorcha del suelo.

  - **Cámara**
    - Cámara estática en los niveles con una vista Top-Down. La cámara muestra el nivel, que estará sombreado en las zonas que no estén iluminadas por el jugador ni por antorchas que haya en el nivel.

### Dinámica
La dinámica principal del juego es avanzar por los distintos niveles, para ello, el jugador tendrá que llegar a una puerta o similar que dé acceso a la siguiente sección del juego. En ocasionees, la puerta estará bloqueada y habrá que buscar una llave para poder pasar.
En cada nivel, el jugador tiene una única vida, por lo que si las estatuas le atrapan, perderá y deberá  reintentar el nivel. 
Para progresar de manera más fácil, el jugador puede buscar power-ups escondidos en el nivel que le darán algún tipo de ventaja o ayuda para progresar, por ejemplo, más tiempo para la antorcha o incrementar la velocidad del jugador.

### Estética
El arte del juego tiene un estilo *pixel art*, destacando  el uso del claroscuro. Al tener lugar en la antigua Grecia encontraremos motivos griegos clásicos. También influirá la presencia natural de la cueva, esencialmente piedra.

## Menús y modos de juego
El juego tendrá un menú principal desde el cual se podrá iniciar la partida y configurar algunos aspectos de esta como el volumen. También se podrán ver los controles y créditos del juego, y las redes sociales.
Además contará con un menú de pausa que podrá ser accedido en medio de un nivel. En este menú se podrá volver al menú principal, acceder a la configuración del juego (volumen) y reiniciar el nivel, además de reanudar la partida.


<div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/Menu.png" width="350" />
  
<sub>*Menú de juego.*</sub>
</div>

### Configuración
El juego tiene un único modo de juego y por ello no es configurable la dificultad ni orden de las salas.

### Interfaz y control
- **HUD principal del juego**
<div align="center">
  <img height=200 src="https://github.com/f0reil/Gorgo-Division/blob/main/GDD%20Images/EjemploHUD.png" width="350" />
</div>

  - Medidor de fuego de la antorcha *(esquina superior izquierda)*
    - Indica cuánto tiempo le queda al jugador antes de que se apague el fuego de su antorcha. Al comienzo de cada nivel la barra se rellenará.
  - Inventario *(esquina inferior izquierda)
    - Indica qué objetos tiene el jugador en su inventario.
  - Menú de pausa *(esquina superior derecha)
    - Funciona a modo de botón. Una vez pulsado se desplegará dicho menú. Tambié es posible acceder a él utilizando la tecla "p".   

- **Menú de pausa** 
<div align="center">
   <img height=200 src="https://github.com/f0reil/Gorgo-Division/blob/main/GDD%20Images/menuDePausapng.png" width="350" />
</div>

Se compone de dos botones principales:
  - Reanudar partida.
  - Salir al menú.

## Contenido
Precisaremos de recursos de arte en *pixel art* de los personajes, fondo y objetos interaccionales, y música de ambiente para el juego con sonidos cuando las estatuas o el jugador están en movimieinto.

### Niveles 
 
Ideamos la existencia de una sala de introducción (meramente para adquirir la antorcha y probar los controles sin la intrusión de enemigos), tres salas de juego-laberinto con estatuas y una sala final de *boss-fight* con Medusa.
La dificultad de los niveles irá aumentando a medida que el jugador los realiza, por lo tanto el nivel de tutorial será el más fácil y el nivel final el más difícil.

  - En Morado: Jugador, PowerUp Tiempo.
  - Círculo blanco: Zona iluminada.
  - En gris: Estatuas
  - En azul: PowerUp Velocidad.
  - En verde: Puerta a otra sala.
  - Bolas verdes: Gemas recolectables
  - En amarillo: Llave
  - En marrón: cajas movibles
  - En azul claro: Trampa viento
  - En rojo: Trampa pinchos

<div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/NivelTutorial.jpg" width="350" />
  
<sub>*Nivel de introducción/tutorial.*</sub>
</div>
 
 <div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/Nivel1Concepto.jpg" width="350" />
  
<sub>*Nivel 1 concepto inicial*</sub>
</div>
 
 <div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/Nivel1.png" width="350" />
  
<sub>*Nivel 1.*</sub>
</div>
 
  <div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/Nivel2.png" width="350" />
  
<sub>*Nivel 2.*</sub>
</div>

  <div align="center">
  <img height=200 src="https://raw.githubusercontent.com/f0reil/Gorgo-Division/main/assets/LevelsGdd/NivelMedusa.jpg" width="350" />
  
<sub>*Nivel final/3.*</sub>
</div>

 
### Personajes y enemigos
- **Personaje principal:** El jugador controla al héroe. Tratando de  ganarse una reputación y contra todo quien le advirtió, se adentra en la cueva de Medusa. Se enfrentará a sus estatuas, que cobran vida.
- **Enemigos:** Como adversarios tenemos a dos tipos de enemigos. En primer lugar, están las estatuas, víctimas de Medusa que rondan por su cueva cuando un intruso es detectado. Por otro lado, el jugador se enfrenta a la propia Medusa, quien puede convertir en piedra. Las estatuas persiguen al jugador por la sala si entra dentro de su rango de detección, no obstante no pueden avanzar mientras les mire directamente y las ilumine. En cambio, en el caso de  Medusa deberá evitar ser visto o quedará convertido en piedra. Mientras no esté en el rango de ningún enemigo, estos tendrán un movimiento aleatorio por la sala.

### Objetos 

| Nombre  | Funcionalidad |
| ------------- | ------------- |
| Fuego  |  El jugador dispone de una antorcha encendida, sirve para iluminar lo que tenga alrededor y evitar que se mueva la estatua a la que llegue la luz.Esta antorcha no puede ser desequipada. Es decir, es un elemento que irá agotándose a medida que pasa el tiempo, pero no se pierde y se recarga con otras antorchas distribuidas por el mapa.  |
| Puerta  | Elemento al final de cada sala o nivel con el que se puede interactuar. No es una acción inmediata, tarda un tiempo. Al pasar ese tiempo, el jugador pasa a la siguiente sala. |
| Obstáculos | El jugador deberá arrastrarlas para poder acceder a lugares o para impedir el paso a enemigos. |
| Llave | Objeto necesario para poder interactuar con las puertas. Se encuentran escondidas por el nivel y el jugador tendrá que buscarlas para avanzar. |
| PowerUps  |  Están distribuidas por las distintas salas y niveles. Hay dos tipos, velocidad y tiempo. El primero aumenta la velocidad del jugador y el segundo el tiempo de la barra de fuego.
| Gemas  | Son imprescindibles para el nivel final. El jugador deberá coger las cinco gemas que hay por el nivel para poder pasárselo.

 <div align="center">
  <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/Torch/torch_1.png" width="100" />
   <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/Doors/Door.png" width="100" />
   <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/Block/block.png" width="100" />
   <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/Doors/Key.png" width="100" />
   <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/PowerUp/PowerUpTiempo.png" width="100" />
   <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/PowerUp/PowerUpVelocidad.png" width="100" />
    <img height=100 src="https://github.com/f0reil/Gorgo-Division/blob/main/assets/Items/Block/gem.png" width="100" />
</div>

## Referencias
- Iluminación antorcha y mécanica contra enemigos: <ins>Five Night's at Freddy's</ins>
- Estilo cámara y salas: <ins>The binding of Isaac</ins>
- Concepto de juego *(el jugador se queda encerrado, perdido e intenta buscar la manera de salir,  pasando a través de los diferentes retos y puzzles que le ofrece el juego, ofreciendo una trama y una narrativa)*: <ins>Ib</ins>, <ins>El réquiem de Chloe</ins>, <ins>The Witch's House</ins>
 

