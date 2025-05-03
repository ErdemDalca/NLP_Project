# Game Design Document (GDD)

### El despertar de los dioses

**![](https://lh7-us.googleusercontent.com/S2tFSjQ9pkwz0DEzPe4HG8SldZW1898bwRIrbVsBTNgd668wFKCutV26ERfU9Bgd6QNww8sIyh9lnCBLF8GtOwQHprxDw-p_6pasD8fNRUbJ50rbdPnBVYJbz5qkv0dd7MoHDs0Q2mj3bhiKeUhwaGw)**

Por GIM Studios:

Gonzalo Ramos
Isabel Zamarrón
Marta Sampedro



# 1.  Introducción
## 1.1. Concepto del juego
### 1.1.1 Información básica

**Título:** El despertar de los dioses

**Estudio/Diseñadores:** GIM Studios

**Género:** Plataformas

**Plataformas:** Web

**Versión:** 1.0

### 1.1.2. Descripción

El despertar de los dioses es un juego de plataformas en el que deberás ayudar a Laura a escapar de las profundidades de la pirámide donde se ha quedado atrapada. Para ello se deberán explorar los diferentes niveles en busca de las puertas que nos permitan salir. Deberá sobrevivir a las numerosas trampas y criaturas que se encuentran protegiendo la antigua estructura.

### 1.1.3. Objetivo

El objetivo final es salir de la pirámide. Para ello deberá superar los distintos niveles y derrotar a los jefes finales para conseguir todos los medallones que te permitirán abrir la compuerta final.

### 1.1.4. Riesgos

Las principales dificultades encontradas han sido el poder controlar correctamente los movimientos del personaje y los enemigos con sus correspondientes colisiones. También aquellos problemas derivados de las colisiones con elementos del fondo de cada nivel.

Otra de las dificultades, al no tener experiencia diseñando, es la creacióm de los sprites tanto de los movimientos del personaje, como de los enemigos. Además, de la automatización de los movimiento de los jefes, al ser cada uno diferentes. 

1.2 Estetica
------------

### 1.2.1. Arte

Las principales herramientas que hemos empleado han sido pixelart para la creación de los distintos objetos, del personaje principal y de los enemigos. Junto con paint que se utilizó para retoques más específicos.

Para el fondo se ha utilizado el programa Tiled a continuación se detalla los pasos que se siguieron:

En primer lugar los fondos de los distintos niveles se han creado utilizando diversos tileset.
**![](https://lh7-us.googleusercontent.com/NBoCY0XpwqEYRl25ZpWQsxebbcwpwtm7pAXe3pZzMiJ6tF_Xg0V3sVBSGGCZw70ba9ouH63DepeEOd1fddQl-C-nT6OOug_7-KptuGw8aRtHre2MsArRB_J6ZKId8KAydOxeQCx0XjGsGMgJHgJlZ68)**

Y  en cuanto a estructuras se refiere optamos por el uso de capas de objetos donde declaramos la posición determinada que queríamos que tuviera un determinado objeto. 

### 1.2.2. Sonidos

En el despertar de los dioses queríamos que la experiencia auditiva del usuario fuera lo mejor posible, por lo que consideramos que la música de fondo jugaría un papel crucial en la inmersión del juego. Para ello, hemos escogido en cada escena unas melodías principalmente compuestas por instrumentos tradicionales egipcios con los que se pretende transportar a los jugadores al corazón del antiguo Egipto.

Además, se han incluido diversos sonidos tanto al personaje como a los enemigos y a los objetos, haciendo más inmersivo el juego.

Los sonidos del juego se han sacado de [https://freesound.org/](https://freesound.org/).

 # 2. Elementos principales
    
   ## 2.1 El jugador
        
La protagonista de nuestra historia va a ser Laura Cruz, una joven estudiante de arqueología a la que el encargo de un trabajo de investigación en una nueva sala que se ha descubierto en una de las pirámides de Guiza en Egipto se convertirá en una aventura. Tras pisar una baldosa suelta, cae en una trampa y queda atrapada en las profundidades de la antigua estructura. Al seguir investigando en la nueva sala, descubre un sarcófago que al abrirlo deja escapar los espíritus de los dioses del Antiguo Egipto que protegían los secretos de la pirámide. Tras un temblor, el estudiante se da cuenta que la sala se está empezando a inundar. Deberá usar sus habilidades para esquivar trampas, vencer enemigos y encontrar una salida antes de que sea demasiado tarde y quede ahogado entre las paredes de la pirámide.

Al principio del nivel el personaje podrá atacar a sus enemigos golpeándolos y según vaya consiguiendo objetos y poderes podrá usarlos contra ellos.

| **Jugador** |  |
|--|--|
| Desplazamiento por el mapa | ![personajeAndar](https://github.com/marsampe/ProyectoDVI/assets/99255110/f3c086f8-b2b8-4e80-8bda-152803d0117a)|
|Escalar|![personajeEscalar](https://github.com/marsampe/ProyectoDVI/assets/99255110/4c0b3875-0a79-43ba-a081-c4b4fcb04b3b)|
|Saltar|![personajeSalto](https://github.com/marsampe/ProyectoDVI/assets/99255110/c613a98e-f4a6-4c68-8680-2a1b3f9f9169)|
|Ataque con puños|![personajeAtaquePuno](https://github.com/marsampe/ProyectoDVI/assets/99255110/960e0caa-9b13-4292-a17f-669d2a72ed4a)|
|Ataque con antorcha|![personajeAtaque](https://github.com/marsampe/ProyectoDVI/assets/99255110/25b2f400-30bb-49c9-8654-0d27c4241a08)|
|Ataque con bola de fuego|![bolaFuego](https://github.com/marsampe/ProyectoDVI/assets/99255110/13ede2d7-36e7-43e2-bad9-f9681feb3b99)|
|Coger y utilizar objetos| / |
    

Va a poseer una mochila que en el juego se muestra como casillas de inventario, pudiendo tener un espacio máximo de 3 objetos que recoja en el a medida que avanza y podrá usarlos exclusivamente en ese nivel, Cuando termine el nivel el inventario de la mochila se vaciará, pero los poderes se mantendrán. 

También contará con una interfaz compuesta por una barra de vida, a la que a partir nivel 2 se le añadirá una nueva barra que será el  escudo.
Los distintos enemigos y obstáculos que vaya encontrando a lo largo de los mapas le restarán vida a la barra en distintas proporciones y podrá recuperar vida usando objetos que recoja ya sea matando enemigos como en los distintos cofres. Cada vez que este muera (la barra de vida se acabe) volverá al punto de inicio del nivel, perderá los objetos que haya encontrado (excepto los medallones).

El nivel de vida que posee es : 180

El daño que sufre y las curas se explican en sus apartados.

## 2.2 Enemigos
    
Los enemigos son más difíciles de superar de forma progresiva. Todos ellos quitan vida en distintas proporciones y te pueden aportar o no objetos.


| **Momia** |  |
|--|--|
| Descripción | Enemigo cuyo objetivo es matar a nuestro personaje. Lo podemos encontrar rondando por las plataformas y cuando nuestro personaje se acerca recibe un ataque. Su debilidad principal es la antorcha |
|Ataque|Golpe de la Eternidad: - 30 vida|
|Vida|100|
 |Niveles|1, 2, 3|
|Recompensa|Vendas|
|Spritesheet|**![](https://lh7-us.googleusercontent.com/GoDee3zv6Ey1kHn0XZQyMtGKdEej9Zbg4j2tX78fCseqEufiTh0pCxf4X5eQxVsIoDQMM1SVqSNEvAGuVjpg-SvNC7KvkN1sxaHVGFukcB91HzBYtF9zpP7PPALnpBoz1R8DjM2LZhTKxFrJIXyMOxM)**|

----

| **Serpiente** |  |
|--|--|
| Descripción | Enemigo cuyo objetivo es matar a nuestro personaje, cuando este se encuentra cerca le persigue y ataca. Si consigue morder al personaje, este queda paralizado durante 4 segundos. |
|Ataque|Mordedura venenosa: - 60 vida|
|Vida|100|
 |Niveles| 2, 3|
|Recompensa|Antídoto|
|Spritesheet|**![](https://lh7-us.googleusercontent.com/pJ3J-GVQs-qp9gFFxCO2Cu0V0ZUHeHTy703unZJdCwgmJmxUWXwWEATcVQHwwS95FJM5Q8_BqDfImHYVVcU3C2ts8nJnGWZu8xTonXM0fgOrfn5xly1OdZZgjX53W2Riu5DYPgGK533x8_OeLLmRgA4)**|

****


| **Escarabajo** |  |
|--|--|
| Descripción |Enemigo cuyo objetivo es matar al personaje escupiendo bolas de veneno. Es inmune al ataque cuerpo a cuerpo del jugador o con la antorcha.|
|Ataque|Bola de veneno: - 30 vida|
|Vida|100|
|Niveles|3|
|Recompensa|Ninguna|
|Spritesheet|**![](https://lh7-us.googleusercontent.com/_QMtWJSpguKQMTOqFCxBKxklIkVi-cWaXGkVNvjCEk-Dx9LOi9sPv_HtcXyPXGFa8KA4REwBgmIAmS_cGZYPvIDDBUTAVejLpbukgdrjBU_9hth3vbiU3738oBLwOmdhXkKtQFyMa3CDcJ7q0yNKDLY)**|

----

## 2.3 Items
    

### 2.3.1 Objetos nivel

| **Objetos del nivel** |  | |
|--|--|--|
| Puerta |Nos permitirá cambiar de una escena a otra, se encuentran en el extremo derecho del nivel, basta con que el personaje se acerque a ella.|![puerta](https://github.com/marsampe/ProyectoDVI/assets/99255110/953d6eed-3216-41b5-80e4-84ec57e86630)|
|Cofre|Objetos dispuestos en el nivel que el jugador deberá abrir para obtener objetos que guardará en su inventario|![cofre](https://github.com/marsampe/ProyectoDVI/assets/99255110/17529a43-7954-43bb-bd57-42174a417f39)|
|Escalera|Objeto que permite al jugador llegar a zonas de nivel donde no podría solo saltando|![escalera](https://github.com/marsampe/ProyectoDVI/assets/99255110/f7371fda-21bd-4382-b886-bc2ad99075c0)|
|Plataforma rompible|Plataforma por la que puede avanzar el jugador, pero que al ser pisada por este empezará a romperse hasta desaparecer después de 3 segundos.|![plataformaRompible](https://github.com/marsampe/ProyectoDVI/assets/99255110/b171e9e7-c676-4bc9-bfb6-7601d208f45e)|

### 2.3.2 Interfaz de usuario

| **Interfaz de usuario** |  | |
|--|--|--|
| Inventario |Lugar donde se almacenarán los distintos objetos que se vayan recogiendo. Tiene 3 espacios.|![inventario](https://github.com/marsampe/ProyectoDVI/assets/99255110/33f6583d-155e-402d-ac7d-38ddaae88759)|
|Barra de salud|Indica cuánto le queda al jugador para morir|![barraVida](https://github.com/marsampe/ProyectoDVI/assets/99255110/80ee78c4-f653-4148-ae9f-3dedbed2571c)|
|Barra de escudo|Indica cuánto le queda al jugador de escudo. Una vez llegado a cero la barra, el jugador perderá vida en los siguientes ataques recibidos|![barraEscudo](https://github.com/marsampe/ProyectoDVI/assets/99255110/c7977918-5984-4a49-ad90-1c30d41b147e)|
|Medallón de escudo|Indica que el jugador ha superado el nivel 1 y que ahora posee la barra de escudo|![medallonEscudo](https://github.com/marsampe/ProyectoDVI/assets/99255110/4fae3451-d356-4f6f-a447-4b280cd828d8)|
|Medallón del sol|Indica que el jugador ha superado el nivel 2 y que ahora posee el poder de lanzar bolas de fuego|![medallonSol](https://github.com/marsampe/ProyectoDVI/assets/99255110/76918881-13e7-43d7-b537-3222ee7b50fe)|


### 2.3.3 Objetos inventario
    
Son objetos que el personaje podrá obtener ya sea en un cofre o al matar a un enemigo. A continuación se detallan sus características principales:

| **Objetos inventario** |  | |
|--|--|--|
| Vendas |Aumentan la vida del personaje: 30|![venda](https://github.com/marsampe/ProyectoDVI/assets/99255110/9aca8af1-a5ed-4979-9069-c304ebec5299)|
|Antídoto|Permite volver a moverse al personaje una vez ha sido paralizado por la serpiente|![antidoto](https://github.com/marsampe/ProyectoDVI/assets/99255110/1241e6a9-0430-4b9a-8b07-c3beea74467f)|
|Antorcha|Herramienta que el personaje utiliza como arma y mientras ataca no le pueden hacer daño. Mata de un golpe|![antorcha](https://github.com/marsampe/ProyectoDVI/assets/99255110/30e9c5a1-7f2a-4405-8111-f0fc1a81e120)|


### 2.3.4 Trampas
    

Son objetos que se encuentran estáticos en las distintas escenas y que provocan daño en la vida del personaje. Pueden ser de varios tipos:

| **Trampas** |  | |
|--|--|--|
| Estacas |Daño que causa: 30|![trampaEstacas](https://github.com/marsampe/ProyectoDVI/assets/99255110/e60c34c7-7300-4782-a767-07ce025d3c7a)|
|Trampa lateral|Daño que causa: 30|![trampaLateral](https://github.com/marsampe/ProyectoDVI/assets/99255110/dee0fe44-60c0-448e-822a-19b19df14daa)|
|Flechas|Daño que causa: 30|![flecha](https://github.com/marsampe/ProyectoDVI/assets/99255110/3df2feff-8f09-41c9-85ea-2b9ea3b14d73)|


## 2.4 Mecánicas
    
A continuación se mostraran las principales mecánicas del juego con una breve descripción, indicando que teclas realizan dicha acción y en que momento de la partida están disponibles:


| **Mecánicas** |  |  |  |
|--|--|--|--|
|Mecánica|Descripción|Control|Disponibilidad|
| Movimiento |El jugador podrá moverse de izquierda a derecha por todo el mapa|-Flecha izquierda: Moverse hacia la izquierda <br> -Flecha derecha: Moverse hacia la derecha|Desde el principio del juego|
|Salto|El jugador podrá saltar para ascender a plataformas superiores |-Flecha arriba|Desde el principio del juego|
|Subir escaleras|El jugador podrá usar la escalera para poder ascender a lugares que no llega saltando|-Flecha arriba en frente de la escalera|Desde el principio del juego|
|Atacar sin arma|El jugador podrá hacer daño a los enemigos con sus puños, pero sufriendo daño él mismo|-Tecla S|Desde el principio del juego|
|Atacar con antorcha|El jugador podrá atacar con una antorcha lo que le permitirá no sufrir daños al atacar.|-Tecla S|Al tener una antorcha en su inventario|
|Coger objetos|El jugador podrá recoger objetos acercándose a ellos|-Entrar en contacto con el objeto|Desde el principio del juego|
|Bola de fuego|El jugador podrá lanzar una bola de fuego para matar a los enemigos|-Tecla D|Nivel 3|
|Usar inventario|El jugador podrá usar cualquier objeto que tenga en el inventario|-Tecla Q: Usar objeto <br> -Tecla Tab: Mover el marcador del inventario|Desde el principio del juego|
|Abrir cofre|El jugador podrá abrir un cofre al estar en contacto con este y obtener objeto|-Tecla E|Desde el principio del juego|

### 2.4.1 Mundo del juego

Nuestro juego se conforma de 3 niveles de plataformas más uno de tutorial. El jugador deberá sortear los diferentes retos que le plantean cada nivel. Para poder finalizarlos con éxito el jugador tendrá que encontrar la puerta del nivel antes de morir. En cada escenario se usará una cámara 2D que permitirá hacer zoom y seguir al jugador a través del nivel.

#### Nivel tutorial

En este nivel se enseñan las principales mecánicas del juego, además de algunos elementos como las trampas y enemigos.
    
#### Nivel 1

En el primer nivel podemos encontrar como enemigos a las momias. Contará con todas las trampas y también habrá cofres para que el jugador pueda conseguir objetos. 

![image](https://github.com/marsampe/ProyectoDVI/assets/99255110/99bd6bbc-c130-4f2f-85ba-7617fdf53e84)

    
#### Nivel 2

Este nivel cuenta con todos los elementos del anterior, además que se añade como enemigo la serpiente, la cual dará como recompensa un antídoto para hacer frente a futuras serpientes. El jugador como recompensa por haber superado el nivel 1 conseguirá una barra de escudo que le permitirá soportar más daño.

![image](https://github.com/marsampe/ProyectoDVI/assets/99255110/9d1e1973-a99e-4d2b-8821-24794b6df99d)

#### Nivel 3

Este nivel cuenta con todo los elementos del anterior y se añade como enemigo el escarabajo, el cual realiza ataques a distancia. Como recompensa por haber superado el nivel 2 el jugador obtendrá el poder de lanzar bolas de fuego, que también le permitirá atacar a los enemigos a distancia.

![image](https://github.com/marsampe/ProyectoDVI/assets/99255110/f7f22f75-4c10-4ef3-a2f1-009b664fc999)

#### Otras escenas
    

*Menú principal*: se muestra al usuario dos botones, uno para realizar el nivel tutorial (botón “tutorial”) y otro para comenzar el juego (botón “start”). Se muestra nada más acceder a la página web y una vez se finaliza el juego.

![image](https://github.com/marsampe/ProyectoDVI/assets/99255110/689ccb7c-ffe8-4a94-b1de-ea6455944fc9)

*Escena fin de partida*: una vez se finalizan los niveles se muestra una pantalla y despues pulsando la tecla enter se vuelve al menu principal.

![image](https://github.com/marsampe/ProyectoDVI/assets/99255110/328dba63-e175-4f17-934d-81b5092512df)











