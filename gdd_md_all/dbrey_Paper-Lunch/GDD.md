Grupo 11 - *Mango games Paper Lunch! -* Game Design Document

***Paper Lunch!***

Documento de diseño de videojuego *Mango games*

Versión 1.2 - 10 Octubre de 2022



|**Géneros:** Estrategia, Gestión de recursos|**Modos:** 1 jugador|
| - | - |
|<p>**Público objetivo:**</p><p>Jugadores casuales, a partir de 12 años sin importar genero</p>|**Plataformas:** Página web PC|
**Descripción**

Eres una vendedora de periódicos ambulante con un gran sueño: ¡Tener tu propia editorial de periódicos! Lucha por hacerte un hueco en esta peculiar ciudad dividida por la gastronomía.



|**Logotipo y portada del juego**|
| - |
|![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/logotipo.jfif)|
**Tabla de contenidos**

1. **Aspectos generales**

*“Paper Lunch!”* es un juego de gestión de recursos narrativo en el que el jugador encarna a Amelia, que empieza a montar su propia editorial de periódicos. Encargándose de la edición y el reparto el jugador deberá tratar de conseguir suficiente dinero para poder comprar su propio edificio editorial y no quedarse en bancarrota.

**1.1. Relato breve y parcial de una partida típica**

Al comenzar el juego, el jugador tendrá 4 opciones a elegir para publicar su periodico, las cuales afectan a su confianza en los distintos distritos. Además, también deberá decidir cuantos periódicos crear teniendo en cuenta el precio por periodico y que debe vender la mayor cantidad posible. Una vez creados los periódicos , el jugador irá hablando con varios NPCs o visitando kioskos, con la idea de venderlos todo. 

Y una vez vendidos todos o haya terminado el día, el jugador volverá a la pantalla de generar periódicos pero esta vez con la posibilidad de poner anuncios a costa de su propia confianza con los ciudadanos de ciertos distritos. A cambio, recibirá una cantidad de dinero

Este proceso se repetirá unas 7 veces más, como si fuera una semana dentro del juego, si durante esas 7 veces o al terminar, consigue suficiente dinero para lograr el objetivo, entonces gana la partida. Si llega al final de la semana sin suficiente dinero, pierde.


2. **Menús y modos de juego**

Solo habrá un modo de juego, en el que solo podrá jugar un jugador. Habra los menús clásicos que componen casi cualquier juego:

- Menú Principal
- Juego principal
  - Preparar el periodico
  - Ciudad
- Menú de pausa / Ver el mapa
- Menú de opciones

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/DiagramaEstados.jpeg)

1. **Configuración**

La única opción de configuración del juego será el volumen de la música y/o efectos de sonido. El jugador podrá aumentar o disminuir el volumen de estos desde el menú de pausa o el menú de opciones.

2. **Interfaz y control**

**Menú principal**

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/MenuPrinc.jpeg)

En este menú, siendo el principal del juego y el primero que ve el jugador, presentamos el nombre del juego, el nombre de nuestra “compañía” y un botón para empezar la partida. El fondo se trataría de un gif en el que observamos la ciudad del juego.

**Menú de pausa**

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/MenuPausa.jpeg)

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/MenuPausa2.jpeg)

En el menú de pausa el jugador podrá modificar la intensidad del volumen del juego o los efectos de sonido (o directamente mutearlos) así como ver el minimapa para que le sea más fácil moverse por la ciudad. También cuenta con dos botones: uno para volver al juego y otro para ir al menú principal.

**Juego principal (cuando esta el jugador en la ciudad)**

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/HUD.jpeg)

En el HUD habrá 2 estadísticas, el número de periódicos restantes y el dinero total del jugador, ambos se mostrarán con un símbolo y un valor al lado. La barra de la derecha simboliza la cantidad de confianza que tiene el distrito en el jugador. Este cambiará según el distrito en el que se encuentre (representando diferentes valores). Arriba a la derecha, está un temporizador que indica cuánto tiempo lleva el jugador en la ciudad

**Juego principal (cuando se esta preparando el periodico)**

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/Prep.jpeg)

El jugador deberá escoger un titular de entre las cuatro opciones (se selecciona haciendo click sobre él, y para seleccionar otro, debes hacer click antes para “deseleccionar” el anterior) viendo cómo afectará cada uno a su confianza en los distintos distritos. A continuación, sabiendo el número de monedas que tiene, introducirá el número de periódicos que desea producir ese día, con 2 flechas por dígito para subir o bajar de 0 a 9.

Habrá un botón de continuar que solo funciona tras seleccionar un tutorial y al menos tener 1 periodico a generar. Como detalle, se puede ver el titular de cada periodico en un pequeño cuadro.

Según vayan pasando los días, se irán desbloqueando los anuncios. Hasta entonces, estarán bloqueados (indicandolo con dibujos de candados)

**Menú de opciones**

![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/Opciones.jpeg)

En este menú el jugador podrá ver los controles del juego y ajustar el volumen del mismo a su gusto (como si decide eliminarlo por completo). Será accesible desde el menú principal y desde el menú de pausa (como se observa en el diagrama de flujo de la página 2)

3. **Jugabilidad**

Al iniciar la partida, el jugador tiene 7 días para reunir cierta cantidad de dinero para montar una editorial. Cada día implica unos X minutos de juego (5-10 minutos aprox)

Cada día, el jugador empieza preparando los periódicos, y tras personalizar sus noticias, empieza desde el centro del mapa. El jugador se moverá por el mapa, buscando personas a las que venderles sus periódicos y consiguiendo comida para pasar el día

4. **Controles**

- Andar/Correr: WASD y mantener SHIFT para correr
- E : Vender periódicos
- ESC : Abrir menú de pausa
- Hacer click en diferentes botones, en la escena de preparacion del periodico


5. **Mecánicas**

Podemos dividir las mecánicas del juego en 4 secciones distintas:

- MOVIMIENTO
- PREPARACIÓN DEL PERIÓDICO
- CIUDAD
  - Estaciones de bus
  - Interacción con kioskos: 

6. **Movimiento**

El jugador puede moverse en un mapa topdown hacia el norte,sur este u oeste. Puede moverse caminando o corriendo

7. **Estadísticas**
- *Confianza*
  - Hay un valor de confianza por cada distrito. Este puede subir o bajar solo al crear nuevos periódicos, dependiendo de cual elija el jugador
- *Dinero*
  - Necesario para poder llegar a la meta final y generar nuevos periódicos
Puede conseguirse vendiendo periódicos. 1 venta = 2 monedas
Puede conseguirse poniendo anuncios, a cambio de confianza

8. **Preparación del periodico**

*Periódicos*: Sirven para obtener dinero y confianza.

Al inicio del dia, el jugador prepara el periodico en el que tiene en cuenta las siguientes características:

- Titular:
  - Dependiendo del titular, éste aumentará o reducirá la confianza en determinados distritos
- Número de periódicos:
  - Generar periódicos cuesta 1 moneda por periodico. Lo ideal es generar suficientes periódicos teniendo en cuenta cuantos va a poder vender en el día según el titular y la confianza entre los vecinos
- Anuncios:
  - Para poder incluir anuncios, es necesario un nivel mínimo de confianza , ya que poner anuncios consume esta estadística, a cambio de ganar 0.25 monedas por periodico. 

9. **CIUDAD**
- *Bono del bus*

  - El jugador puede comprar un ticket para el bus y así poder moverse de un punto a otro de la ciudad, permitiéndole llegar mucho más lejos y así vender en más zonas. Un ticket a otro punto del mapa cuesta 5 monedas
- *Kioskos*
  - Alcanzado cierto nivel de confianza en un distrito será posible vender varios periódicos en ese distrito
- *Interacción con NPCs*
  - Es posible interactuar con los NPCs que rondan los distritos para tratar de venderles un periódico. Dependiendo de la confianza que mantengas en el distrito podrás venderselo o no

10. **Dinámica**

Tras pasar 7 días, si el jugador ha conseguido la cantidad de dinero necesaria, consigue montar una editorial y ganar el juego, si no llega a esa cantidad, pierde la partida y obtiene un final negativo.

El jugador tendrá que balancear los periódicos que produce con el dinero que tiene y con el tiempo del que dispone. También será necesario balancear la confianza  en los distritos y vigilar la cantidad de anuncios introducidos. Conforme vaya avanzando en el juego y gane más confianza, la venta en kioskos permitirá vender mayores cantidades de una sola vez.

11. **Estética**

Nos hemos decantado por el estilo artístico Pixel-art. Varios recursos se sacarán de Itch.io u otros lados, y posiblemente se modifiquen para adaptarse mejor al juego. Otros, los haremos nosotros, como puede ser el caso de los NPCs, desarrollados a partir de una plantilla

12. **Sonido**

Toda la banda sonora y efectos de sonido del juego son originales

13. **Contenido**

Serán necesarios sonidos de ambiente y se crearán dos temas musicales, uno para el momento en el que se crea el periódico y otro mientras se reparten los periódicos.

Visualmente se usarán tilesets de ciudad (preferentemente representativos de cada cultura) y modelos de NPCs genéricos. Se creará un modelo específico para el personaje principal.

15. **Historia**

La venta de periódicos, sus titulares, los anuncios entre otros, son dependientes de la historia y su temática: *la gastronomía*. Para este juego se han elegido (a priori) las siguientes cocinas:

- Gastronomía española: Representada por la paella, la tortilla, el cocido montañés, el pulpo gallego, el cachopo, el gazpacho, entre otros platos típicos. Cuidado con mencionar la cebolla cerca, ya que puede incitar a una pelea sobre si una tortilla de patata debe llevar cebolla o no

- Gastronomía italiana: Representado por la pasta, la pizza, la lasaña, el risotto, el carpaccio… Literalmente, son capaces de ir a la guerra como un trozo de piña caiga cerca de su pizzería local de su distrito

- Gastronomía japonesa: Representada por el ramen, el sushi, el takoyaki, los onigiris, la sopa de miso, el gyudon. Como la lies, se crea una revuelta donde encienden antorchas recubiertas de wasabi y te persiguen hasta la frontera de su distrito

- Gastronomía Vegana: Nada como una buena ensalada para ser sano. Cualquier comida de origen vegetal es bienvenida en este distrito. Tan solo asegurarse de que ninguna carne o pescado pisa este barrio a menos que quieras sufrir miradas de odio

El jugador jugará como el personaje Amelia, la nieta de Leoncia, a quien la representaron como una hermosa estatua de una repartidora de periódicos. Para cumplir el sueño de su abuela, quiere montar una editorial en su honor.

Para cumplirlo, tiene que vender periódicos en una ciudad dividida por sus gustos culinarios.

La historia de la ciudad se contará a través de los titulares de los periódicos, por lo tanto el jugador la descubrirá según vayan pasando los días y se repartirá de la siguiente forma:

- ***Día 1 Introducción:***

Se muestran las tensiones que hay entre los distritos con titulares crispados, recalcando la tensión entre distritos.

- ***Día 2 Llegada:***

El crítico culinario va a estar visitando los distritos.

- ***Día 3 Intoxicación:***

El crítico culinario sufrió una intoxicación tras terminar su visita, no sé sabe cuál de los restaurantes es el culpable y esto no hace más que aumentar las tensiones.

- ***Día 4 Culpable:***

Las autoridades demuestran que el crítico culinario fue el culpable de su propia intoxicación, al llevar sus propios cubiertos, que no estaban lo suficientemente limpios. Esto detiene las acusaciones, sin embargo las tensiones se encuentran en un máximo histórico.

- ***Día 5 Expectación y Tensiones:***

Se acerca el gran festival de la ciudad en el que se juntan todos los distritos para mostrar sus comidas y hacer colaboraciones. Sin embargo este año es una incógnita cómo resultará.

- ***Día 6 El Evento:***

Es el día del evento. Dependiendo de la reputación que el jugador haya mantenido con los distritos saldrá bien o mal.

- ***Día 7 Consecuencias:***
- Día 7: El evento ha salido bien, la ciudad se ha recuperado de las tensiones y todo ha vuelto a la normalidad.

16. **Mapa**

El mapa es una ciudad dividida en 4 distritos temáticos divididos por su estilo de comida.
Cada distrito se diferencia estéticamente para reflejar la gastronomía que representa.

El jugador aparece en el centro del mapa y a lo largo de las calles de la ciudad el jugador encontrará NPCs con los que interactuar y a los que vender periódicos.

Cada distrito tiene un parque, 1 kiosko y una parada de bus:

- Los parques se encuentran en el centro de cada distrito y en ellos se encuentra una mayor cantidad de NPCs
- Los kioskos están repartidos de forma aleatoria, pero al menos uno por distrito. Ahí el jugador puede vender X periodicos de una sola vez siempre que cuente con la confianza suficiente del distrito
- Las paradas de bus permiten transportarse rápidamente a otras paradas de otros distritos, los cuales están situados en las esquinas del mapa. 


![](https://github.com/dbrey/Paper-Lunch/blob/main/assets/GDDImages/minimap.jpeg)

3. **Personajes**
- *Amelia*: Personaje principal del juego que el jugador controla. Es la nieta de Leoncia,

personaje de Cáceres que tiene una estatua en la que se basa el juego. Se mueve por la ciudad en bicicleta, donde reparte periódicos editados por ella, con la esperanza de ahorrar suficiente dinero para montar su propia editorial.

- *NPCs varios*: Se encuentran repartidos por la ciudad, moviéndose o estáticos. No

tienen una distinción característica.

**Referencias**

2016. *Stardew Valley.* Barone, E.
2018. *Graveyard Keeper*. St. Petersburg, Russia: Lazy Bear Games.
2020. *No Umbrellas Allowed*. Hoochoo Game Studios.
2018. *Moonlighter*. Digital Sun.

