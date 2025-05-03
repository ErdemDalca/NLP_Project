# GAME DESIGN DOCUMENT (GDD)

## PRESENTACIÓN/RESUMEN

### Título

Macedonia Game

### Concepto

El juego es una versión inspirada en *Suika Game*, donde el jugador controla una cesta desde la que puede lanzar frutas dentro de una caja. A medida que las frutas se acumulan, se combinan para formar frutas más grandes, pero si la caja se llena completamente, la partida termina. La evolución de las frutas es circular de forma que cuando se llega a la fruta más grande, la sandía, si se combina con otra, vuelve a crearse la primera fruta de la evolución, la cereza.

### Género

- Arcade



### Público (Target Audience)

- Todas las edades
- Jugadores casuales



### Plataforma

- PC
- Smartphones (iOS, Android)
- Tablets

## GAMEPLAY

### Objetivos

- **Principal**: Mantener la caja lo más despejada posible evitando que se llene.



### Jugabilidad

- El jugador controla una cesta que puede moverse horizontalmente.
- Desde la cesta, se lanzan frutas hacia la caja.
- Las frutas caen siguiendo un sistema de físicas y pueden combinarse en frutas más grandes.
- Cuando la caja se llena hasta cierto límite, la partida termina.
- Se otorgan puntos cuando se combinan frutas del mismo tipo.



### Progresión

- La dificultad aumenta con el tiempo: las frutas pueden aparecer más rápido o con mayor variedad.
- Se pueden incluir niveles con distintos desafíos o modos de juego.

### GUI

- Marcador de puntuación en la parte superior.
- Indicador del próximo tipo de fruta.
- Barra de progreso indicando el llenado de la caja.
- Botones de pausa y reinicio.

## MECÁNICAS

### Reglas

- **Condiciones de victoria**: No hay una victoria definida, el objetivo es lograr la máxima puntuación posible.
- **Condiciones de pérdida**: La partida termina cuando la caja está completamente llena.
- **Reglas adicionales**: Las frutas pueden combinarse si son del mismo tipo.

### Interacción

- **Controles**:
  - Arrastrar la cesta para moverla horizontalmente.
  - Pulsar A para crear una fruta y D para lanzarla.
- **Acciones posibles**:
  - Mover la cesta.

  - Crear frutas en la caja.

  - Tirar frutas de la caja.

  - Combinar frutas mediante colisiones.
- **Interacción con elementos**:
  - Físicas de gravedad y rebote.
  - Diferentes tipos de frutas con propiedades visuales y físicas.

### Puntaje

- Se obtiene puntuación al fusionar frutas iguales.



### Dificultad

- Se introducen frutas más grandes para dificultar la organización.

## ELEMENTOS DEL VIDEOJUEGO

### Caracterización del mundo

- **Leyes físicas**: Gravedad y colisiones basadas en Unity Physics.
- **Historia**: No hay una narrativa formal, es un juego de estilo arcade.
- **Personajes**: Frutas con diferentes diseños y expresiones animadas.
-

## ASSETS

- **Música**: Música de fondo animada.
- **Efectos de sonido**: Sonidos para las caídas y fusiones de frutas.
- **Modelos 2D/3D**:
  - Frutas con diseño atractivo.
  - Animaciones suaves y efectos visuales.
  - Cesta y caja con diseño claro y fácilmente distinguible.

---

Este documento sirve como base para el desarrollo del juego, y se puede ampliar con más detalles técnicos o diseños específicos según avance el desarrollo.

