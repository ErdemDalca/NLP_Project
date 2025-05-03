# <PLANET BARBER>

## GAME DESIGN DOCUMENT

Creado por: < ANTONIO MARTIN ANTON >

Versión del documento: < 0.1 >

## HISTORIAL DE REVISIONES

| Versión | Fecha | Comentarios |
| --- | --- | --- |
| 1.00 | < 03/05/2024 > | 03/05/2024 |




## RESUMEN

### Concepto
Un renegado, atrapado en una serie de planetas hostiles debe sobrevivir a oleadas de esferas enemigas mientras busca un monolito para avanzar al siguiente planeta. Cada nuevo planeta presenta desafíos mayores con enemigos más rápidos y numerosos, en un entorno que se expande y se vuelve más peligroso.


### Puntos Clave

Supervivencia Dinámica: El juego combina elementos de acción con un enfoque en la supervivencia contra enemigos que incrementan en velocidad y número.
Progresión Escalable: Cada nuevo planeta ofrece un mayor desafío, aumentando tanto en tamaño como en dificultad para encontrar el monolito.
Capacidad de Ataque: El personaje puede disparar a las esferas enemigas, permitiendo estrategias ofensivas y defensivas.
Ambientes Generativos(En proceso)
Los planetas y sus características serán generados aleatoriamente, ofreciendo una experiencia única en cada partida y aumentando la intensidad de la partida cuando grandes grupos de enemigos se acumulan.
### Género
Acción con elementos de shooter y supervivencia.
### Público Objetivo
Dirigido a jugadores de ambos sexos, principalmente entre 15 y 35 años, Es ideal para aquellos que disfrutan de juegos desafiantes y dinámicos. También capta la atención de jugadores de mayor edad que valoran los juegos de las primeras consolas, ofreciendo una mezcla de nostalgia y mecánicas contemporáneas. Los aficionados a títulos como "Enter the Gungeon" encontrarán este juego especialmente atractivo.
### Experiencia de Juego

El jugador se sumerge en un entorno hostil donde las esferas enemigas acercándose crea una atmósfera tensa. Visualmente, los planetas varían en colores y terrenos(en desarollo), mientras que el diseño de los enemigos es simple pero amenazante. Durante el juego, el jugador experimentará una mezcla de tensión por la supervivencia y satisfacción al eliminar enemigos y encontrar el monolito. La jugabilidad es rápida y requiere reflejos rápidos para avanzar de un planeta a otro.

## DISEÑO

### Metas de Diseño

Inmersión Total: Crear un ambiente que sumerja al jugador en cada planeta hostil a través de los gráficos , efectos de sonido y una banda sonora que se adapte al nivel de amenaza.
Desafío Progresivo: Asegurar que cada nuevo planeta ofrezca un desafío mayor, manteniendo al jugador comprometido y probando sus habilidades de manera continua. Esto se logrará aumentando la velocidad y número de enemigos y expandiendo el tamaño del mapa.
Jugabilidad Rejugable: Fomentar que los jugadores quieran volver a jugar mediante niveles generados procedimentalmente. Cada partida será única, ofreciendo nuevos desafíos y configuraciones de enemigos.

## MECÁNICAS DE JUEGO

### Núcleo de Juego

Supervivencia: Los jugadores deben evitar ser abrumados por enemigos mientras buscan el monolito para escapar del planeta.
Navegación: los jugadores deben explorar para encontrar el monolito que se genera de forma aleatoria en cada planeta.
Combate: Los jugadores pueden disparar a las esferas enemigas. Los enemigos varían en velocidad y número, y los jugadores deben usar tanto estrategias ofensivas como defensivas.

### Flujo de Juego

Inicio: El jugador comienza en un planeta pequeño.
Exploración: El jugador explora el planeta, evadiendo o combatiendo esferas enemigas.
Descubrimiento: El jugador encuentra el monolito después de sobrevivir un tiempo determinado.
Transición: Una vez que el jugador activa el monolito, se transporta al siguiente planeta.
Repetición: El ciclo se repite con aumento en la dificultad.

### Fin de Juego

Derrota: El jugador pierde si pierde las 3 vidas al ser alcanzado por los enemigos.
Victoria: Al ser fases generadas procedimentalmente no esta prevista una fase final.
Abandono: Si el jugador opta por salir del juego en cualquier momento se perdera el progreso y volverá a empezar desde el primer nivel en la siguiente partida.

### Física de Juego

Movimiento: Los jugadores pueden moverse libremente en todas direcciones gracias a una vista cenital del planeta, lo que permite un desplazamiento fluido y constante a través del entorno de juego.
Rotación y Disparo: La rotación del personaje se maneja con el ratón, facilitando el apuntar en cualquier dirección de manera independiente al movimiento. El disparo también se controla con el ratón, ofreciendo una mecánica de apuntado precisa y reactiva.
Zoom de la cámara: Utilizando la rueda del ratón, los jugadores pueden ajustar la distancia de la cámara para abarcar un mayor ángulo de visión del terreno, lo que permite una mejor planificación estratégica y anticipación de los movimientos enemigos.


### Controles

| Acción            | Teclado   | Ratón               |
|-------------------|-----------|---------------------|
| Moverse           | WASD      | N/A                 |
| Rotar/Apuntar     | N/A       | Movimiento del ratón|
| Disparar          | N/A       | Botón izquierdo     |
| Salir             | Esc       | N/A                 |
| Pausa             | p         | N/A                 |

## MUNDO DEL JUEGO

### Descripción General

Descripción General
El mundo del juego se ambienta en una serie de planetas alienígenas, cada uno con características únicas, pero unidos por un tema oscuro y espacial. La apariencia es una mezcla de terrenos rocosos y formaciones irregulares, con una paleta de colores fríos predominantes que incluyen azules, grises y negros. El ambiente es hostil y solitario, lo que refuerza la sensación de aislamiento y desafío. El jugador debe navegar por este entorno en busca de un monolito que permite la transición a nuevos planetas cada vez más desafiantes.

### Personajes

Jugables:

El Heroe/Renegado: El único personaje jugable, vestido con un traje espacial avanzado que permite la supervivencia en ambientes hostiles. Equipado con un arma para defenderse de las amenazas alienígenas. Ágil y capaz de disparar en todas direcciones.
Enemigos:

Esferas Enemigas: Criaturas robóticas alienígenas que parecen esferas con texturas que brillan en colores fríos. Son los principales adversarios del juego y varían en velocidad y agresividad. Su única misión es perseguir y destruir al jugador.

### Objetos

Objetos
Monolito: El objeto clave en cada nivel. Aparece de manera aleatoria en el planeta y es necesario encontrarlo para avanzar al siguiente mundo. Su apariencia es de una estructura alta, oscura y con símbolos alienígenas lumínicos.

### Flujo de Pantallas

Pantalla de Inicio: Menú principal con opciones de iniciar juego, configuración y salir.
Pantalla de Juego: La vista principal del juego donde el jugador navega por el planeta.
Pantalla de Pausa: Accesible durante el juego con opciones para continuar o salir.
Pantalla de Fin de Juego: Muestra resultados y permite reiniciar o regresar al menú principal.

### HUD
El HUD muestra información esencial para el jugador:

Número de Vidas: En la esquina superior izquierda, indica cuántas vidas quedan.
Nivel Actual: En el centro superior, muestra el nivel en que se encuentra el jugador.
Puntuación Actual (Score): En la esquina superior derecha, refleja los puntos acumulados.
Puntuación Máxima (Max Score): Al centro en la parte inferior, muestra la puntuación más alta alcanzada.



## ARTE

### Metas de Arte

El objetivo del arte en el juego es crear un ambiente espacial futurista y misterioso que realmente sumerja al jugador. Se busca un equilibrio entre lo atractivo visualmente y lo funcional, con un estilo que mezcla lo realista y lo fantástico.

Estilo de Arte: Se utilizan texturas realistas con iluminación dramática, empleando colores fríos y oscuros para dar un toque sombrío, pero se destacan elementos clave como enemigos y objetos importantes con colores vivos para captar la atención.
Concepto Visual: Se quiere que el jugador se sienta pequeño y vulnerable en un gran universo. Los escenarios son grandes y abiertos, con un fondo espacial.
Escenarios: Se presentan terrenos áridos y rocosos con estructuras alienígenas antiguas como el monolito.
Personajes: El 'player' luce equipado con tecnología avanzada, mientras que los enemigos, las esferas, tienen un look robótico-alienígena con texturas que brillan, mostrando un ambiente futurista y tecnológico.

### Assets de Arte
[Player](https://assetstore.unity.com/packages/3d/characters/robots/robot-hero-pbr-hp-polyart-106154)
[Skybox](https://assetstore.unity.com/packages/2d/textures-materials/sky/skybox-series-free-103633)
[explosion enemigo](https://assetstore.unity.com/packages/vfx/particles/legacy-particle-pack-73777)
[explosion player](https://assetstore.unity.com/packages/vfx/particles/fire-explosions/particle-dissolve-shader-package-33631)

[Texturas-Materiales](https://assetstore.unity.com/packages/2d/textures-materials/textures-free-122421)
[Texturas-Materiales](https://assetstore.unity.com/packages/2d/textures-materials/metals/yughues-free-metal-materials-12949)
[Graficos UI](https://assetstore.unity.com/packages/2d/gui/80-sci-fi-irregular-frame-in-one-248272)
logo y portada dall-e
Fonts - 
[Zecton free](https://assetstore.unity.com/packages/2d/gui/sci-fi-gui-skin-15606)
[Perfect futures](https://www.dafont.com/perfect-futures.font)
[Stacker](https://befonts.com/stacker-font.html)


## AUDIO

### Metas de Audio

Se busca una música de fondo que, a través de su repetición, logre inmersión total en la experiencia de juego, manteniendo al jugador envuelto en la
atmósfera del mundo virtual durante su sesión 

### Assets de Audio

[Explosión enemigo](https://assetstore.unity.com/packages/audio/sound-fx/grenade-sound-fx-147490)
gun
[game over](https://pixabay.com/sound-effects/gameover-86548/)
[explosion player](https://pixabay.com/sound-effects/whoosh-hit-163595/)
[Musica - The old switcheroo] Created by Antonio Martin
## DETALLES TÉCNICOS

### Plataformas Objetivo

> Desarrollado para plataformas Windows con la vista puesta en un futoro port a android.

### Herramientas de Desarrollo

aseprite para el sprite del cursor
Presonus studio one. - musica
Unity.
Gimp para editar imagenes.
Visual Studio Code


