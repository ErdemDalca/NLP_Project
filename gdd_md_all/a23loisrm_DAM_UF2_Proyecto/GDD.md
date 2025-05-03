## GDD - FROG JUMPING

### PRESENTACIÓN/RESUMEN

- **FROG JUMPING**
- **Concepto:** Es un juego de plataformas basado en *Super Mario Bros*, donde el objetivo es pasarse los niveles llegando al final del mismo.
- **Género:** Videojuego de Plataformas.
- **Público:** Todo el público.
- **Plataforma:** En principio en PC, pero en un futuro se puede adaptar a otras plataformas.

### GAMEPLAY

#### Objetivos

El objetivo principal del juego es completar los niveles llegando al final del mismo. Completando así todos los niveles del mundo. En un futuro se pueden implementar monedas secretas para hacer los niveles más difíciles y con mayor jugabilidad.

#### Jugabilidad

El jugador cuenta con una serie de vidas (5). Se pueden conseguir más vidas consiguiendo monedas en el propio nivel. Cuando llegas a 50 monedas, se suma una vida, dando oportunidad a no perder el progreso. Si pierdes todas las vidas, perderías el progreso del nivel volviendo a la escena de la elección de niveles.

#### Progresión

El avance en el juego consiste en superar cada nivel uno tras otro. La idea a implementar en un futuro es crear diferentes biomas con una cantidad total de niveles, siendo la progresión pasarse todos los biomas.

#### GUI

1. La primera pantalla mostrada es la de inicio (*Pulsa una tecla para continuar*).
2. Posteriormente nos lleva a la página de elección de niveles, donde podemos seleccionar el nivel que queremos jugar.
3. No será posible acceder a un nivel sin haber completado el anterior.
4. Una vez seleccionado el nivel, el jugador entra y lo juega.
5. Al llegar al final del nivel, se regresa a la selección de niveles con ese nivel marcado como completado.

### MECÁNICAS

- **Reglas:**
  - Condiciones de victoria: Llegar al final del nivel.
  - Condiciones de pérdida: Perder todas las vidas.
- **Interacción:**
  - Moverse: `A` y `D` o `←` y `→`
  - Saltar: `W` o `↑`
  - Correr: `Shift`
  - Entrar a nivel: `E`
- **Puntaje:**
  - No hay un sistema de puntaje tradicional.
  - Cada moneda cuenta como un punto.
  - Al recolectar 50 monedas, se obtiene una vida extra.
- **Dificultad:**
  - La idea es que la dificultad aumente progresivamente a medida que se completan los niveles.

### ELEMENTOS DEL VIDEOJUEGO

Caracterización del mundo/entorno en el que se desarrolla el videojuego (*Worldbuilding*):

- **Leyes físicas:** Similares a la gravedad y físicas de un juego de plataformas clásico.
- **Historia:** No hay una historia como si, pero sería algo que se podría implementar en un futuro.
- **Personajes:**
  - Protagonista: Una rana ninja con habilidades de salto y desplazamiento.
- **Enemigos:**
  - Son unos bloques que caen contra el suelo en un determinado tiempo y luego suben. No hay opción de matarlos, solo se pueden esquivar.
- **Niveles:**
  - Diferentes entornos y biomas en el futuro.
- **Elementos culturales o geográficos:**
  - Inspirado en entornos naturales con distintos obstáculos y desafíos.


### ASSETS

- **Modelos 2D/3D:**
  - Diseño de personaje y enemigos en PixelAdventure 1 y fondos y elementos en BayatGames
  - **Escenas**
  - Escena de inicio, seleccion de niveles y niveles
- **Scripts:**
  - Scripts del movimiento del personaje, la puntuacion, los enemigos, etc.
- **Otros elementos gráficos:**
  - Fondos, interfaz, animaciones, etc.

