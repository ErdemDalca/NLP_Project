# Game Design Document

## Resumen del juego

El juego es un homenaje del juego Exerion de 1983, un matamarcianos sencillo estilo arcade que además de recreativas también estuvo en ordenadores personales como MSX.

Genero: Shoot'em up estilo retro pixelado, vertical.
Audiencia: Jugadores de todas las edades, que disfruten de juegos de naves espaciales y de estilo retro, especialmente quienes jugaron en su infancia a juegos como Exerion.
Estilo de juego: El jugador maneja una nave y varias hordas de marcianos aparecen en pantalla, siendo necesario matarlos a todos para pasar a la siguiente pantalla. La dificultad aumenta progresivamente tras cada pantalla.
Otras características: Puntuación y tabla de puntuaciones al estilo de las recreativas clásicas.
Repositorio oficial: https://github.com/jbiosca78/extranion

## Estilo visual

El estilo visual del juego es retro pixelado, los marcianos serán los mismos assets que el juego Exerion del que nos inspiramos excepto la nave del jugador, que se ha mejorado considerablemente pero sin perder el estilo retro.

La nave del jugador se ha generado mediante Stable Diffusion 3 medium (instalación local). Tras generar múltiples naves se ha seleccionado una. El prompt usado finalmente ha sido:
"rear back view of videogame war spaceship, the background is entirely black without stars or planets. the propulsors are powered on with red energy inside. we are alone in space and see the spaceship in front of us moving towards."
Y el prompt negativo: "background planet stars"
La imagen generada se ha recortado y reducido para la secuencia inicial de vuelo y se ha girado 10 grados para la nave llegando al destino. Esas mismas imágenes se han reducido 32x32 pixels para los spritesheets del juego (con unos pequeños retoques pixel a pixel en los propulsores para la animación usando Gimp).

Finalmente para el logo de inicio se ha utilizado también Stable Diffusion 3.

Nota: Debido a que se reutilizan los assets de Exerion, es posible que no se pueda distribuir el juego ni siquiera como Open Source. Si alguna vez fuera necesario habría que reemplazar los assets de Exerion por otros distintos.
Se podrían generar con alguna herramienta de creación de sprites aleatoria como por ejemplo: https://ianburnette.itch.io/random-sprite-generator

## Interface

La pantalla inicial consta de una presentación y logotipo del juego.

Al iniciar el juego se muestra una breve animación de la nave del jugador viajando a máxima velocidad durante unos segundos.

La interface del juego es sencilla, basada en el estilo de Exerion. En la parte central se encuentra el espacio de juego y a la derecha el interfaz informativo, que consta de un registro de la puntuación máxima conseguida, la puntuación de la partida actual, el nivel de carga que tenemos para los disparos rápidos, la escena en la que nos encontramos y finalmente un contador de vidas.

Excepto el contador de vidas que se corresponde con iconos de naves, el resto de elementos son texto, usando una fuente pixelada sin antialiasing (fuente open font específica para terminales llamada terminus) y así conseguimos un aspecto retro.
Referencia a la fuente: https://files.ax86.net/terminus-ttf/

## Mecánicas

### Movimiento de la nave

El movimiento de la nave es el básico de una nave espacial vista desde arriba, pero dispone de un sistema de inercia que hace que la nave siga moviéndose en la dirección en la que se movió por última vez, aunque el jugador deje de pulsar las teclas de dirección. De esta manera se consigue un efecto de ingravidez.
Además el movimiento con los cursores no será directo sino que la nave se moverá en la dirección pulsada con una aceleración y velocidad máxima. Con esto damos un poco de complejidad y realismo al movimiento de la nave para que no sea tan sencillo esquivar las balas y enemigos.

### Movimiento de los enemigos

Al igual que en Exerion, cada tipo de enemigo tiene un movimiento distinto. Se ha intentando simular los movimientos originales, pero con algunas diferencias, consiguiendo un movimiento mas orgánico que en el juego original. Posiblemente gracias a que podemos utilizar variables en coma flotante que en la época de Exerion no se podía usar fácilmente.

Los enemigos 1 y 3 del juego original se han intercambiado, ya que ambos tienen un movimiento similar que persigue al jugador, pero el 3 lo hace directamente en lugar de en zig zag, haciendo que sea mucho mas fácil. En el juego original ya ocurría esto y la fase 3 era una especie de "bonus" gracias a lo sencillo que era. Al intercambiarlas conseguimos un incremento mas gradual de la dificultad.

### Disparos de la nave

La nave del jugador tiene dos tipos de disparo distintos:
Disparo normal: Consiste en dos balas paralelas. No se puede volver a disparar hasta que al menos una de las balas acierte en un enemigo o hayan salido de la pantalla. Al ser dos balas individuales es posible que una bala mate a un enemigo y la otra continué y mate a otro enemigo. Cada enemigo acercado otorga un punto de carga para el disparo rápido.
Disparo rápido: Consiste en ráfagas rápidas de disparos individuales. Son muy efectivas pero gastan carga. Cuando la carga llega a 0 no se puede continuar utilizando este disparo, siendo necesario utilizar el disparo normal para incrementar la carga.

### Disparos de los enemigos

Los enemigos disparan misiles que caen hacia abajo, mas lentos que los disparos del jugador. A medida que se progresa en el juego cada vez hay mas misiles enemigos, incrementando la complejidad.

## Puntuación y vidas

Los puntos se consiguen matando enemigos. A medida que avanza el juego los enemigos otorgan mas puntos. Cada 10.000 puntos se otorga una vida extra.
Cada vez que el jugador choca con un enemigo o misil enemigo, se pierde una vida. Cuando ya no quedan vidas y el jugador colisiona, se acaba la partida.

## Música y efectos sonoros

La música del juego se han obtenido de Pixabay, que ofrece multitud de recursos libres de derechos de autor.
La música elegida ha sido:

Pantalla inicial:
MARTIAN - u_4bplvbk4dw
https://pixabay.com/sound-effects/martian-131602/

Gameplay:
Neon Gaming - dopestuff
https://pixabay.com/music/synthwave-neon-gaming-128925/

Fin de partida:
Born to the Earth - nojisuma
https://pixabay.com/music/upbeat-born-to-the-earth-207192/

Otra versión usada anteriormente para el gameplay:
8 Bit Retro Funk (Slower Version) - David Renda
https://www.fesliyanstudios.com/royalty-free-music/download/8-bit-retro-funk/883

Los efectos sonoros también se han descargado de Pixabay, siendo necesario retocarlos para ajustar algunos volumenes y sobre todo cortar los espacios iniciales que tenían casi todos los efectos. Se ha utilizado la herramienta Audacity para modificarlos.
