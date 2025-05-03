# Death Cab
> Documento de diseño de videojuego.
> Versión 3 – 19 de Diciembre, 2023.
> - Adrián Castellanos Ormeño.
> - Daniel Moreno Álvarez.
> - Jiale He.
> - Nicolás Besteiro Martín.
> - Paula Sierra Luque.

## 1. Ficha técnica
- Título: Death Cab.
- Género: Conducción, Aventura conversacional.
- Target: Público amplio.
- Rating: Pegi 16+.
- Plataforma: Navegador Web.
- Modos de juego: Un jugador.

## 2. Descripción
La Muerte no puede permitirse pagar el alquiler en el inframundo, y por ello conseguirá trabajo como taxista. Cada día la radio del taxi informará de un crimen a La Muerte. Su objetivo será recoger gente por la ciudad ejerciendo su profesión, estos clientes tendrán o no que ver con el crimen. Al recogerlos, el taxista hablará con ellos. A medida que fluye la conversación con el cliente, la Muerte tendrá que decidir si llevar a su cliente al infierno, al cielo o dejarlo vivir dependiendo de la intuición del jugador y de la personalidad de los personajes, viendo si es una posible víctima o culpable del crimen o tan solo un viandante.
El jugador tendrá que decidir el destino de cada pasajero para ser recompensado y con ello perdurar en el juego.

## 3. Jugabilidad
### Cámara
En la fase de conducción, la cámara sería “Top Down” en el estilo de los juegos 2D de GTA. Seguirá al taxi de modo que esté centrado.

### Mecánicas de conducción
El jugador conducirá un taxi desde una vista cenital con una breve inclinación para dar sensación de profundidad.
- El coche se moverá con las teclas “W” (acelerar) “A” (izquierda) “S” (marcha atrás) “D” (derecha), cambiando su ángulo y movimiento en esa dirección.
- En el caso de que se consiga la mejora de ACELERAR, se podrá utilizar con la tecla de “SHIFT”. Esto aumentará la velocidad del taxi.

En el mapa se encuentran diferentes objetos con los que el taxi puede chocar: Edificios, Cubos de basura, Farolas, Semáforos, Coches…Que el jugador deberá esquivar para seguir avanzando por la carretera.
También encontrará NPCs que podrá atropellar si colisiona con ellos. En cada nivel, habrá uno o varios NPCs que serán los clientes. Entraremos en la escena de recogida al colisionar con ellos. Se distinguirán gracias a un icono encima de su cabeza con forma de bocadillo, con un taxi.

![Icono de Recogida](/assets/Imagenes/capturas/capturaIcono.png)

Algunos objetos con los que el coche puede colisionar, tendrán la posibilidad de explotar.
Las explosiones y atropellos no tienen efecto en la puntuación del juego.

### Mecánicas de diálogo
Tras entrar en la escena de recogida, se entrará en el minijuego conversacional, comenzará la conversación taxista-cliente. Aquí es donde aparece la temática de las personalidades, las conversaciones serán diferentes según el personaje al que se recoja. Se tendrá en cuenta lo malo y lo bueno de cada una, y si encajan con la descripción que da la radio todos los días. A partir de ahí construiremos los diálogos. Irán apareciendo y desapareciendo los bocadillos de conversación a medida que se elija la contestación. No se podrá volver atrás en la conversación para recordar qué se ha dicho.

Cada vez que el cliente cuente algo, aparecerán dos recuadros con las opciones para contestarle, haciendo más preguntas. Según lo que el jugador elija, tendrá que ir juzgando al cliente, y finalmente elegir entre las opciones de “CIELO”, “INFIERNO”, o “DEJAR VIVO”. Para elegir la opción, se usará el ratón y el click izquierdo.

### Sistema monetario
La moneda principal del juego son años de vida. Para ganar monedas, la Muerte tendrá que llevar a un cliente al infierno o al cielo. En este apartado hay que describir las distintas posibilidades en las que se podría ganar o perder dinero.
- Si dejas vivir a un cliente y es alguien que no tenía nada que ver con un crimen, no se ganará dinero pero no habrá penalización.
- Si se acierta, se ganarán 25 monedas. Acertar conlleva:
  - Llevar a un culpable al infierno.
  - Llevar a una víctima al cielo.
- Si se falla, se perderán 15 monedas. Fallar conlleva:
  - Llevar a un culpable al cielo.
  - Llevar a una víctima al infierno.
  - Si era culpable y se le deja vivo. Habrá consecuencias al día siguiente, ya que el culpable seguirá matando (enviando más trabajo al cielo/infierno) y por ello penalización de -10 monedas por gastos de gestión.
  - Si era víctima y se le deja vivo. Habrá consecuencias al día siguiente, ya que por su trauma, se suicidará (enviando más trabajo al cielo/infierno) y por ello penalización de -5 monedas por gastos de gestión.

El precio del alquiler será de 100 años de vida. Se pagará al final de la semana, es decir, al haber superado todos los días. Si no se consigue pagar el alquiler, se habrá perdido el juego. Pero en cambio, si se consigue pagar, el jugador lo habrá completado con éxito.

### Tienda
El juego tiene implementadas mejoras para el modo de conducción. Para conseguirlas se podrán comprar en la tienda con la moneda del juego.

Las mejoras incluidas son las siguientes:
- GPS. Encima del taxi aparecerá una flecha que indicará dónde se encuentra el cliente a recoger. Su coste será de 100 monedas.
- Acelerador. Permitirá al taxi aumentar su velocidad pulsando la tecla SHIFT. Su coste será de 75 monedas.
- Tiempo extra. Se aumentará el tiempo para encontrar a los clientes. Su coste será de 50 monedas.

El jugador tendrá que administrar las ganancias que vaya adquiriendo de forma efectiva para superar cada nivel, por lo tanto no podrá abusar de los beneficios de la tienda. 


### Salud del taxi (extra)
El taxi conducido, podrá estrellarse con elementos de la carretera, especificados en el
contenido del juego. Si se estrella, perderá puntos de salud. Por lo que habrá que conducir
el taxi a una zona de reparación.
El juego empezará con el 100% de salud. Cada vez que se estrelle, perderá 25% de salud.
Si se llega al 0%, se perderá el juego, teniendo que volver a empezar desde el principio.
En las zonas de reparación habrá que pagar para reparar el taxi. Costará 10 monedas.

## 4. Dinámica
### Diseño de niveles: el mapa.
Es una zona del pueblo de Alcázar de San Juan donde conduciremos buscando clientes. Se
podrán distinguir las carreteras fácilmente. Habrá zonas de colisión (edificadas), elementos
que exploten (farolas, postes...). Cada nivel se distinguirá por las zonas de aparición de
clientes, pero siempre será el mismo mapa.

![Mapa](/assets/Mapas/mapa.png)

### Diseño de niveles: los crímenes.
Cada nivel (o cada día) se distingue por un crimen.
1. [Un robo.](/documentation/guion/guiond1.md)
2. [Caso de violencia de género.](/documentation/guion/guiond2.md)
3. [Creación de una plaga de chinches.](/documentation/guion/guiond3.md)
4. [Crimen falso.](/documentation/guion/guiond4.md)
5. [Asesino en serie.](/documentation/guion/guiond5.md)

En el guión se encontrará una descripción detallada de cada crimen, para ayudar a
desarrollar cada nivel, donde se informa de quién es el culpable y la víctima, o si hay alguna
persona no implicada. Se enseña también el guión de la radio, con datos que sí que
conocerá el jugador. En cada nivel se hablará con 3 clientes, por ello hay preguntas y
respuestas predeterminadas para cada uno, enfocadas en sus personalidades. El jugador
elige entre 4 preguntas para averiguar si el cliente es una víctima, un culpable, o alguien
que no está implicado.

### Descripción de partida típica
1. Presentación del día. Se muestran las noticias en la radio. Se explica un crimen que ha sucedido.
2. Conducción del taxi. 
Pasamos la vista desde arriba de la ciudad. Se buscan posibles clientes por el mapa. Habrá que colisionar con el cliente para poder recogerlo y continuar a la parte conversacional. Podremos colisionar con elementos de la ciudad o atropellar gente.
3. Cuando se suba un cliente, entraremos en el minijuego conversacional. En él el jugador tendrá que juzgar si su cliente es un posible culpable o víctima del crimen a través del diálogo y lo que conoce sobre el crimen que ha contado la radio. Al final de la conversación, el jugador tendrá que decidir si el cliente es una víctima, un culpable o nada. Así acabará en el cielo, infierno o se le dejará vivir, respectivamente.
4. Volveremos a la conducción en búsqueda de otros clientes. Se repetirán los pasos 2, 3 y 4 hasta pasar el número de personas del nivel.
5. Al pasarse un nivel, se vuelve al menú de días, y se habrá desbloqueado el siguiente. Se repetirán entonces todos los pasos hasta que se hayan completado todos los niveles.
6. Al acabar toda la semana, se hará un recuento de todas las ganancias y pérdidas. Se pedirá pagar el alquiler.

    6.1 Si no se puede pagar, se habrá perdido el juego y habrá que volver a jugarlo desde el principio.
  
    6.2 Si se puede pagar, se habrá completado el juego con éxito.


## 5. Estética

### Estilo artístico y paleta de colores
El estilo artístico utilizado ha sido el de Pixel Art. Se ha optado por un diseño sencillo. 

En el modo de conducción, la paleta de colores utilizada es bastante variada, destacando los colores primarios sobre fondo de distintas tonalidades de gris. Así podemos destacar cada elemento del mapa.

![capturaColores](/assets/Imagenes/capturas/capturaColores.png)

### Diseño de personajes
En cuanto al diseño de personajes que aparecen en el mapa, los hemos diferenciado también por los colores que se utilizan en la página de [16personalities]([URL_del_enlace](https://www.16personalities.com/es/descripcion-de-los-tipos)). Que también destacan sobre los fondos grises.

![capturaColores](/assets/Imagenes/Personajes/AzulDia1.png)

### Mapa
El mapa del juego, como ya se ha mostrado en el apartado de dinámica, da bastante espacio al taxi, lo que hace que el jugador se sienta cómodo a la hora de la conducción. Se pueden distinguir carreteras más estrechas, para aportar variedad. La iluminación es bastante clara, y hay zonas de vegetación (parques) para hacer que la ciudad sea más diversa.

![Mapa](/assets/Mapas/mapa.png)

### Animaciones
En cuanto a animaciones, son muy sencillas. Los ciudadanos están animados al andar. Se destaca la animación de la explosión al colisionar con ciertos elementos, y la animación al atropellar a un ciudadano, lo que puede satisfacer al jugador.

### UI
Hablando de la UI, no es muy cansada para la vista. Aparecen botones que destacan mucho sobre los fondos. 

![botonPlay](/assets/Imagenes/capturas/capturaBoton.png)
![botonOpciones](/assets/Imagenes/capturas/capturaOpciones.png)

En **menú inicial** será un menú intuitivo con dos únicos botones: PLAY y CONTROLES. El primero para acceder al menú de Días, y el segundo para aprender los controles básicos del juego.

![capturaInicio](/assets/Imagenes/capturas/capturaInicio.png)

En el **menú de días**, se podrá elegir el nivel que esté desbloqueado. Al acabar todos los niveles, se dará acceso al botón PAGAR EL ALQUILER. Con el que se podrá o no superar el juego. 
Desde aquí se podrá acceder a la TIENDA.

![capturaInicio](/assets/Imagenes/capturas/capturaMenuDias.png)

La **tienda** mostrará las monedas de las que dispones abajo a la derecha. Cada vez que se haga una compra, al pulsar uno de los botones (GPS, ACELERADOR ó TIEMPO EXTRA), se reproducirá un sonido de cajero para dar a entender al usuario que ha realizado una compra. Debajo de cada botón se incluye una descripción de la mejora que se consigue, tal y como se muestra en la imagen. También se incluye un botón para regresar al menú de días (ATRÁS).

![capturaTienda](/assets/Imagenes/capturas/capturaTienda.png)

En la **parte de conducción**, se mostrarán las monedas que tiene el jugador arriba a la derecha. Arriba a la izquierda, tendrá el contador de tiempo.

![capturaTienda](/assets/Imagenes/capturas/capturaJuego.png)

### Narrativa visual
Es importante la narrativa visual en el juego. Los textos son lo suficientemente grandes para que cualquier jugador sea capaz de leer. Se separan los textos grandes en distintas secuencias para no cansar al jugador, podrá pasar cuando se realice el click en la pantalla, haciendo que pueda tomarse su tiempo para leer.

La escena de la **radio** toma importancia aquí. Comienza antes de empezar cada nivel. Se muestra texto en blanco con un fondo negro, y con un sonido de radio con alguna voz indistinguible, ya que se comenta un crimen y se pretende dar sensación de estrés. 

Finalmente, la **parte conversacional**, con un fondo desde el punto de vista del asiento de atrás del taxi. Da un ambiente muy tenebroso que aporta mucha inseguridad al jugador. Aquí se puede elegir las opciones para hablar con el cliente.

![capturaJuegoConver](/assets/Imagenes/capturas/capturaJuegoConver.png)

Una vez terminada la conversación se dará a elegir la opción final, tal y como se muestra en la imagen.

![capDecision](/assets/Imagenes/capturas/capturaDecision.png)

### Sonidos
Destacamos algunos sonidos en el juego para hacerlo más inmersivo. Algunos de estos sonidos se han exagerado para producir en el jugador sensación de ironía.
- Al conducir, se puede escuchar el motor del coche.
- Al recoger un cliente, se escucha cómo cierra la puerta, y como arranca el taxi.
- Al atropellar a un NPC, se puede escuchar cómo grita.
- Al colisionar con ciertos elementos que explotan, se puede escuchar una explosión muy fuerte.
- Al poner el ratón sobre ciertos botones, se escuchan efectos de sonido.

En general, el jugador se sentirá cómodo conduciendo.

### Música
En algunos momentos del juego, se reproducirá música de fondo para entretener al jugador. Aquí destacamos la música de la tienda.

## 6. Contenido
### Personajes
Las personalidades de los clientes estarán basadas en los tipos del [indicador Myers-Briggs
o inventario tipológico de Myers-Briggs](https://www.16personalities.com/es/descripcion-de-los-tipos), (también conocido como MBTI), un cuestionario
autorreportado que evalúa cómo las personas perciben el entorno y toman decisiones.
Nuestras interacciones con estos estarán muy marcadas con la personalidad de los clientes
quienes se comportan de cierta forma dependiendo de su tipo de personalidad. Habrá
clientes basados en cada uno de los cuatro grupos principales de personalidad
(representado por colores) y debido a la mecánica de personalidades, alguno de los clientes
malos serán mucho más inesperados ya que algunas personalidades son naturalmente
relacionadas con gente buena.

| Personaje | Descripción |
|-------------|-------------|
| La Muerte   | Parado y con apenas dinero para pagar el alquiler del mes, este coge un trabajo como taxista para sobrevivir un poco más. Es el protagonista de nuestro juego, y el único personaje jugable. Tendrá la habilidad de conducir y de decidir quien vive y quien muere.   |
| Cliente Centinela   | Son cooperativos, prácticos y fundamentados. Se sienten cómodos con quienes son y se enorgullecen de su buen carácter y su competencia. Estos tipos de personalidad buscan orden, seguridad y estabilidad. Trabajan duro y aspiran a no defraudar a nadie, y esperan que otras personas también adopten esta misma ética.   |
| Cliente Analista   | Conocidos por su amor a la racionalidad, tomando decisiones con la cabeza. Caracterizados por idear estrategias creativas y por la motivación para explorar las cosas. Corren el riesgo de ser superados por aquellos que simplemente se sientan y hacen el trabajo. Además de ser lobos solitarios sin preocuparse por hacer amigos.   |
| Cliente Diplomático   | Se preocupan por ayudar y conectarse con los demás. Priorizan ser amables y generosos y, en general, prefieren cooperar que competir. Son sensibles a los sentimientos de otras personas y quieren empujar a las personas que los rodean en direcciones positivas. Sin embargo, si no se controla, este rasgo de personalidad puede desencadenar superioridad moral o determinación.   |
| Cliente Explorador   | Tienden a ser autosuficientes y de pensamiento rápido. Viven de manejar situaciones inciertas. Su flexibilidad les ayuda a adaptarse al momento. Generalmente prefieren la trabajabilidad y la utilidad a la perfección. Sin embargo no les gusta la monotonía y pueden desviarse de sus obligaciones para probar cosas nuevas.   |

### Elementos del minijuego de conducción
En el minijuego de conducción, nos encontraremos distintos elementos repartidos por la ciudad que tendrán físicas propias.
| Nombre del elemento | Utilidad | Descripción |
|-------------|-------------|-------------|
| Carreteras   | Zona por donde será posible la conducción.   | Carriles de color gris oscuro, con líneas blancas que lo delimitan.   |
| Aceras   | Zona donde aparecerán los clientes.   | De un color más claro que la carretera para que sea distinguible. Cuando haya un cliente parado en la acera, aparecerá un círculo, donde tendremos que parar el taxi para que se suba.   |
| Edificios   | Zona no transitable delimitada por un colisionador que no se podrá atravesar   | Edificios vistos desde arriba.   |
| Obstáculos   | Obstáculo en la carretera con el que el taxi podrá colisionar, y que producirá una fuerza opuesta a la dirección del taxi. Si se colisiona con alguno, explota y causará daños al taxi. Son farolas, postes, cubos de basura, semáforos y otros coches.   | De distintos colores.   |

### Diálogos
Al ser una aventura conversacional, destacarán los diálogos entre la Muerte y sus clientes. Se ha adjuntado un enlace al guión de cada día en el apartado de *Dinámica*.
Se definirán preguntas y respuestas predeterminadas, con las que el jugador tendrá que decidir finalmente si su cliente es culpable, una víctima o un simple transeúnte.

## 7. Referencias
Para el diseño y desarrollo de Death Cab, se han tomado los siguientes juegos como
inspiración y de referencia:
- Papers Please. El jugador toma la decisión, arriesgándose a perder dinero, de dejar
pasar o no a un viajero.
- Crazy Taxi. SEGA. La recogida de los clientes y la caótica conducción del juego.
- Grand Theft Auto 2. Rockstar Games. El caos de la conducción, la conducción en la
ciudad, la vista desde arriba.
- Phoenix Wright: Ace Attorney. Capcom. Interrogaciones a los clientes para juzgar si
es víctima o culpable.
