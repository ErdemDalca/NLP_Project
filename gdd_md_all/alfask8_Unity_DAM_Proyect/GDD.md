# Sparge

## GAME DESIGN DOCUMENT

**Creado por:** Adrián Cendán  
**Versión del documento:** 1.0

## HISTORIAL DE REVISIONES

| Versión | Fecha       | Comentarios          |
| ------- | ----------- | -------------------- |
| 1.00    | 02/04/2024  | Creación del documento|

## RESUMEN

### Concepto

> *"Sparge" es un juego clásico de Arkanoid en 2D con un diseño de 5 niveles frenético enfocado en superarlos todos, y un modo extra de supervivencia (Survival Mode) que incita al jugador a practicar para entrenar sus reflejos y habilidades y poder superar todos los niveles del modo normal.*

### Puntos Clave

> - Juego clásico de Arkanoid en 2D
> - Diseño con 5 niveles únicos
> - Modo extra de supervivencia (Survival Mode)
> - Estilo arcade y rompecabezas

### Género

> Arcade, Rompecabezas

### Público Objetivo

> Todas las edades, jugadores que disfrutan de juegos clásicos del estilo arcade y rompecabezas.

### Experiencia de Juego

> Los jugadores experimentarán un desafío progresivo a medida que avanzan por los 5  niveles, encontrando ladrillos con diferentes propiedades. La música  y los efectos de sonido acompañar la acción del juego. El HUD proporcionará información como vidas restantes.

## DISEÑO

### Metas de Diseño

> - Ambientación clásica mezclada con tintes actuales
> - Enfoque en la jugabilidad
> - Niveles diseñados con desafíos únicos
> - Estímulo a la rejugabilidad
> - Progresión de dificultad equilibrada

## MECÁNICAS DE JUEGO

### Núcleo de Juego

> Los jugadores controlan una paleta con el movimiento del ratón para manejar una bola y destruir ladrillos en 5 niveles progresivamente más difíciles. El "Survival Mode" ofrece un nivel infinito con ladrillos generados aleatoriamente para practicar y mejorar habilidades.

### Flujo de Juego

> - Nivel completado: Completar un nivel con éxito
> - Victoria: Superar todos los niveles en el modo normal


### Fin de Juego

> - Derrota: Perder todas las vidas


### Física de Juego

> La física se aplica principalmente a la bola y su interacción con los ladrillos y la paleta, con una trayectoria que se acelera en niveles avanzados.

### Controles

> - Control de la paleta: Movimiento del ratón
> - Lanzamiento de la bola: Boton izquierdo del ratón
> - Reseteo de la bola: Boton derecho del ratón
> - Pausar el : Barra espaciadora del teclado
> - Salir del juego: Tecla "Esc" del teclado

## MUNDO DEL JUEGO

### Descripción General

> Estética clásica mezclada con tintes actuales, enfocado en la jugabilidad sobre la historia, diseños de niveles únicos con ladrillos y obstáculos distintos.

### Personajes

> - **Jugables**: Paleta del jugador
> - **Secundarios**:Bola
> - **Enemigos**: Ladrillos

### Objetos

> Paleta, bola, ladrillos,modificadores

## INTERFAZ

### Flujo de Pantallas

> Start,HTP,HTP1,HTP2,HTP3,Level1,Level2,Level3,Level4,Level5,Survival,GameOver.

### HUD

> **HUD**: Presentación de información con vidas restantes.

## ARTE

### Metas de Arte

> - Estilo de arte clásico mezclado con tintes actuales
> -  Estética en escenarios y musica de estilo arcade.

### Assets de Arte

> - Sprites para paleta, bola, ladrillos,escenas, botones,textos...

## AUDIO

### Metas de Audio

> - Banda sonora clásica y enérgica 
> - Efectos de sonido para rebote, colisión y destrucción de ladrillos

### Assets de Audio

> - **Música**: Banda sonora clásica para niveles  y transitoria entre escenas para niveles de victoria, derrota, etc
> - **Sonidos**: Rebote, colisión y destrucción de ladrillos

## DETALLES TÉCNICOS

### Plataformas Objetivo

> PC

### Herramientas de Desarrollo

> Unity Editor Version "2022.3.13f1"
