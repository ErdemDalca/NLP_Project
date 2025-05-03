# Myself #

## INTRODUCCIÓN ##
Este documento especifica un diseño para nuestro proyecto de videojuego llamado _Myself_, que será creado en el segundo cuatrimestre del curso 2023-2024. En este proyecto están involucrados los siguientes miembros del equipo _AntzTeam_, Raúl Arellano Jorge, Mario Alcolea Alcolea y Jorge López Carrión.

## RESUMEN ## 
_Myself_ es un single-player de tipo metroid, compuesto de 4 zonas diferentes por las que se deberá pasar para terminar el juego.

## ESPECIFICACIÓN ##
### Concepto: ###
El objetivo de _Myself_ es ser un juego entretenido single-player de tipo metroid, para pasarselo bien durante un largo periodo de tiempo. Para ello se busca tener un mapa amplio y fácil de jugar para que no sea tedioso el moverte por el mismo, y una movilidad y ataque del protagonista disfrutables. Este juego es rejugable dada su amplitud de mapa y sus mecánicas agradables para el jugador.

### Historia: ###
El juego estará situado en un mundo de fantasía en el que el protagonista está perdido, debe enfrentarse a diferentes bestias que habitan dicho mundo hasta encontrarse con su enemigo final que le ha estado observando desde las sombras, cuando se enfrente a él descubrirá todos los secretos que deseaba saber sobre su existencia. Este enemigo final no será ni más ni menos que tu versión original, ya que el protagonista es la creación de todo lo que deseó ser, la culminación de su existencia y la batalla tiene lugar por la envidia de este hacia ti.

### Estructura del juego: ###
Habrá 4 zonas distintas, de manera que cada zona tendrá unas características concretas y un tipo de enemigo concreto. En las 3 primeras zonas se conseguirán diferentes poderes al matar al enemigo final y la última será para enfrentarse al boss final del juego, donde aparecerán todos los tipos de enemigos vistos en las anteriores zonas. Todas las zonas estarán conectadas entre si y además será posible desbloquear ciertos caminos(atajos), obteniendo los distintos poderes de los bosses al eliminarlos de las diferentes zonas.


### Objetivo: ###
Derrotar los bosses para conseguir los poderes correspondientes de cada zona y poder avanzar hacia la siguiente hasta llegar al boss final.

## GAMEPLAY ##

### Gráficos ###
Graficos 2D pixelart, de manera que la cámara se centrará en el personaje y los fondos se moverán con el personaje, y según el gameplay, en algunas zonas habrá cambios de pantlla/carga de mapa.

### Mundo: ###
Las 4 zonas del mundo están ambientadas de diferente forma:
- La zona 1 se basa en una zona terrenal, con mucha hierba
- La zona 2 al estar en el mapa en una zona más alta, está basada en la montaña, y más concretamente, en una montaña nevada
- La zona 3 es una cueva, ya que se encuentra en la zona más baja del mapa.
- La zona 4 que es la última zona y conectada únicamente con la zona 3, es un castillo que es donde se encuentra refugiado el enemigo final.

Para diferenciar dichas zonas, habrá un fondo que muestre claramente la zona del mundo en la que te encuentras, además de la música correspondiente en el caso de que la tenga.

### Enemigos: ### 
En cuanto a los enemigos, vamos a diferenciar entre los enemigos comunes y los bosses.

#### Enemigos comunes ####
![Lobo](./assets/sprites/Wolf/LoboComun.png)
Los lobos son los enemigos que se encuentran en la primera zona, son enemigos grandes que disponen de un ataque normal a melee y no son especialmente rápidos.

![Minotauro](./assets/sprites/128x80Minotaur_Idle.gif)
Los minotauros nos los encontraremos en la segunda zona, son enemigos pequeños pero fuertes que disponen al igual que los lobos un ataque normal a melee.

![Araña](./assets/sprites/spider_walk.gif)
Las arañas se encuentran en la tercera zona, son enemigos rápidos con una cadencia de ataque mayor aunque con menor daño que los otros enemigos.

Estos tres tipos de enemigos nos los encontraremos a la vez en la última zona.

#### Bosses ####
![Boss1](./assets/sprites/Wolf/LoboBoss.png)
Este boss será el primero al que se enfrentará el jugador, se encuentra en la zona 1 y tiene un tipo de ataque más que el lobo común, es más grande y quita bastante más vida.
Al derrotarlo el jugador obtendrá el poder del dash.

![Boss2](./assets/sprites/128x80Minotaur_Idle.gif)
Este boss será el segundo que se enfrente, como con el anterior, sigue la temática de su zona, la zona 2 y será un minotauro mucho más grande, con más rango de ataque y más daño.
Al derrotarlo, te otorgará el poder del doble salto.

![Boss3](./assets/sprites/spider_walk.gif)
Los bosses anteriores eran bestias salvajes del propio mundo, sin embargo, este boss es una mascota del enemigo final y sigue los mismos pasos que los bosses anteriores.
Al derrotarlo, obtienes el poder de encogerte y volver a tu tamaño original.

![BossFinal](./assets/sprites/dwarf_2_walk.gif)
Este boss se encuentra en la zona 4, y tiene un tamaño parecido al del jugador, con más daño pero menos rango que los demás bosses.

### Personaje principal ###
![Protagonista](./assets/sprites/Viking/Viking.png)
El protagonista será este vikingo que portará un hacha como arma para atacar a los enemigos.

### Control: ###
Se juega con teclado.

## Mecánicas ##
- Moverse (izquierda/derecha) - para ello se deberá pulsar 'a' para moverse a la izquierda y 'd' para moverse a la derecha
- Saltar -> Salto doble - pulsa 'w' para saltar una vez y si se ha obtenido el poder del doble salto, otra vez 'w' una vez en esté el jugador en el aire. Con el doble salto se alcanzarán zonas antes inaccesibles con un único salto.
- Golpear a meleé  - para poder atacar a los enemigos hay que pulsar 'j'
- Encogerse/Agrandarse - pulsar 'ctrl' para poder encogerse, y si está encogido pulsar otra vez 'ctrl' para volver al tamaño original. Encogerte te permitirá moverte por rincones por los que antes no era posible.
- Dash - pulsar 'shift' para poder realizar un dash, ya sea en el aire y en el suelo. El dash te permitirá ir más rápido y también llegar a zonas más lejanas.
