![ImagenLogo](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/logo.png)

# Maria Pita's Revenge (A Vinganza de Maria Pita) - Pantheon Studios

## 1. Ficha técnica
| Ficha | Descripción |
| :---: | :---: |
| **Público objetivo** | Jugadores adolescentes y/o adultos jóvenes que busquen un reto y una épica aventura histórica |
| **Género** | RPG |
| **Plataforma** | Navegador |
| **Modo de juego** | 1 jugador |

## 2. Descripción
Maria Pita's Revenge es un RPG de combates por turnos ubicado en A Coruña del siglo XVI. En él encarnas a María Pita, la mujer que acabó con la vida de un alférez inglés con su propia bandera después de que los ingleses asesinaran a su marido. El jugador deberá ir derrotando a las tropas inglesas hasta llegar a este alférez.

## 3. **Mecánicas**
- **Personaje:** María Pita cuenta con unos valores de vida, defensa y ataque. 
La vida siempre será de 100 puntos, mientras que la defensa y el ataque dependen del arma que se tenga equipada. Estos puntos modifican el daño que recibe y hace María Pita respectivamente.

- **Combate:** El combate se basa en un sistema de turnos en los que el jugador y los enemigos pueden realizar sus acciones en su correspondiente turno. Además, al derrotar enemigos, estos pueden dejar caer objetos. El jugador tiene 4 opciones en su turno, las cuales son:
  - ***Ataque:*** El jugador selecciona un enemigo al que atacar y le realiza un daño dependiente del valor de defensa que tenga este.
  - ***Defender:*** El jugador puede decidir perder su turno en favor de una reducción de daño durante un número limitado de turnos y acumulable hasta un máximo y que, cada vez que lo vuelve a hacer, recupera el número de turnos que se mantiene.
  - ***Objetos:*** En los combates se pueden obtener objetos curativos que se pueden usar gastando un turno para aumentar la vida en caso de que se necesite.
  - ***¡QUE LOCURA!:*** Esta acción permite al jugador usar una habilidad especial que depende de cada arma. Esta acción será absolutamente necesaria para terminar el juego. Se carga atacando y se descarga completamente al usarla.

- **Selección de nivel** : Entre combates, el jugador accederá a un mapa donde se le irán desbloqueando niveles que puede seleccionar hasta llegar al final. Estos niveles son rejugables para obtener más objetos.

- **Equipamiento:**  En el mapa de selección de niveles habrá un botón desde el cual el jugador podrá ver los objetos que tenga (tanto armas como íiems curativos) y el arma equipada.

- **Fin de combate:** Hay dos desenlaces:
  - ***Perder el combate:*** aparecerá una escena de Game Over en la que se podrá decidir si quiere salir al mapa de niveles o reintentar el combate.
  
  ![ImagenGameOver](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/gameOver.png)
  
  - ***Ganar el combate:*** se recompensará al jugador con un posible arma de cierto nivel dependiendo del nivel en el que se encuentre y con comida (explicación de la probabilidad de cada arma en el siguiente punto).

  ![ImagenWin](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/win.png)
  
- **Sistema de recompensas:** siempre se recompensa al jugador con comida con una cantidad aleatoria entre 1 y 5. Luego, también le puede tocar un arma si es que no la posee. En cada nivel, hay diferentes probabilidades de que toque arma de nivel I, nivel II y nivel III (las armas de diferentes niveles se describen más abajo):

![ImagenProbMap](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/probmap.png)

Viendo la imagen del mapa, los números en negro representan el mayor nivel de arma que puede llegar a tocar. Los círculos negros señalan los niveles opcionales (niveles por los cuales no es obligatorio pasar por ellos para finalizar el juego) contienen mayores niveles de armas.

La lógica interna del sistema consiste en elegir un número aleatorio entre 0 y 100 que determina el nivel del arma teniendo en cuenta las probabilidades especificadas y otro número aleatorio entre 0 y 4 para determinar un arma en concreto de ese nivel. Si se da la casualidad de que el jugador ya tiene ese arma, solo se le da comida. Los rango de estas posibilidades (en porcentaje) son:

| **Nivel** | **Tier I** | **Tier II** | **Tier III** |
| :---: | :---: | :---: | :---: |
| 1-2-3-5 | 100 | 0 | 0 |
| 4-7 | 40 | 60 | 0 |
| 6-9-11 | 0 | 40 | 60 |
| 8-10 | 0 | 100 | 0 |
| 12 | 0 | 0 | 100 |

Siempre al completar un nivel se dará comida, habiendo la misma probabilidad de:
- Recibir cualquiera de las 3 comidas disponibles.
- Recibir de 3 a 5 piezas de la misma.


## 4. Dinámica
El objetivo del juego es animar al jugador a pensar en cada movimiento que haga para poder avanzar, desarrollando una estrategia que le permita llegar al final y pasarse el juego. 
También se busca un grado de acción y tensión al poner al jugador frente a combates de dificultad moderada.

![ImagenDinamica](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/dinamica.png)

Al jugador se le dará la oportunidad de rejugar niveles que ya haya pasado para obtener más objetos y armás que se adapten más a su estilo de combate. Junto a esto, los enemigos formarán parte fundamental de la experiencia de juego, ya que habrá enemigos variados con habilidades diferentes y que serán reconocibles por el jugador, permitiendo a este formar una estrategia teniendo en cuenta estos enemigos y formar una lista de prioridades a la hora de atacar y defender.

Se busca también que, de perder un combate, el jugador pueda reintentarlo inmediatamente para fomentar que afronte el combate con una nueva estrategia. 

## 5. Contenido
### Objetos
Habrá dos tipos de objetos:

- ***Curativos:*** los objetos curativos permiten al jugador sanar una cantidad de puntos determinada:

| **Nombre del objeto** | **Puntos curativos** |
| :---: | :---: |
| Polbo á feira (pulpo a la gallega) | 90 |
| Caldo gallego | 60 |
| Bolla de pan | 35 |

- ***Armas:*** las armas serán objetos de distintas clases las cuales permitirán al jugador hacer más daño. El jugador, al principio del juego, de base contará con el "Puño", un arma con 10 de ataque, 0 de defensa y ninuna habilidad especial.

Durante la partida se podrá encontrar con más armas que se le añadirán automáticamente al inventario, las cuales son:

| **Nivel** | **Cimitarra** | **Daga** | **Alabarda** | **Ropera** | **Sacho** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Cimitarra de madera | Daga oxidada | Alabarda de marca blanca | Ropera inglesa | Sacho |
| **2** | Cimitarra de acero | Daga afilada | Alabarda de verdad | Ropera castellana | Fouciño |
| **3** | Cimitarra loca | Daga excéntrica | Alabarda demencial | Ropera alocada | Guadaña extravagante |

Adicionalmente, contará con una habilidad llamada "**¡Qué locura!**" con las siguientes características:
| **Característica** | **Descripción** | **NI** | **NII** | **NIII** |
| :---: | :--- | :---: | :---: | :---: |
| ***Ataque en área*** | Divide el daño base entre el número de enemigos y le suma un porcentaje de ataque según el nivel del arma | 10% | 20% | 30% |
| ***Sangrado*** | Resta vida al enemigo equivalente a cierto porcentaje de la vida durante 3 turnos según el nivel del arma | 2% | 3% | 4% |
| ***Aturdimiento*** | Impide al enemigo atacar en su siguiente turno y podrá no hacerlo durante 2 turnos más dependiendo del nivel del arma del jugador | 100% | 100-70% | 100-70-30% |
| ***Ataque múltiple*** | Ataca a un enemigo concreto un número de veces con el 60% del daño base según el nivel del arma | 2 | 3 | 4 |
| ***Robo de vida*** | Recupera en forma de vida un porcentaje del daño infligido al enemigo | 30% | 40% | 50% |

Además existe un arma que se obtiene al final de la aventura y que es necesaria para el último combate: **El asta de bandera** (una bandera inglesa con una punta de lanza). Se usará para poder acabar con el **Hermano de Drake** y cuyo “**¡Qué locura!**” será un ataque del 200% y que aumenta un 30% el ataque durante el resto del combate.

Cabe destacar que el jugador podrá cambiar de arma en todo momento (menú de niveles y combate), con la principal diferencia de que cambiar de arma en el menú de opciones no supondrá ninguna penalización, mientras que durante el combate *deberá gastar un turno* para hacerlo.

### Enemigos
| **Enemigo** | **Vida** | **Ataque** | **Habilidad especial** |
| :---: | :---: | :---: | :--- |
| ***Rufián embriagado*** | 100 | 10 | - |
| ***Pirata maloliente*** | 150 | 20 | - |
| ***Marinero escorbutado*** | 200 | 30 | Tiene una probabilidad del 15% de envenenar en cada ataque (ver sangrado de tier I) |
| ***Bucanero experimentado*** | 250 | 40 | Probabilidad del 15% de golpear con daño crítico, aumentado un 40% el daño |
| ***Corsario enajenado*** | 300 | 50 | Probabilidad del 15% de robar un 50% del daño infligido |
| ***Alférez Drake (hermano)*** | 500 | 45 | Probabilidad del 20% de hacer aleatoriamente alguna de las otras tres habilidades especiales que tienen los otros enemigos |

### Diseño de niveles
Los niveles estarán compuestos por un único combate diferente en cada uno, en dificultad creciente hasta llegar al último nivel. La siguiente distribución de los niveles es orientativa y está sujeta a cambios tras el testing.
| **Enemigo** | **Siglas** |
| :---: | :---: |
| *Rufián Embriagado* | RE |
| *Pirata Maloliente* | PM |
| *Marinero Escorbutado* | ME |
| *Bucanero Experimentado* | BE |
| *Corsario Enajenado* | CE |

- **Nivel 1:** El combate será sencillo, contra un RE nada más en la que el jugador podrá descubrir el combate sin mucho peligro.
- **Nivel 2:** Este combate será contra 2 RE para que el jugador se acostumbre a combates contra varios enemigos.
- **Nivel 3:** Este combate será contra un PM y un RE, presentando un nuevo enemigo con la dificultad añadida de uno ya conocido.
- **Nivel 4:** Este combate será con un PM y dos RE para presentar los combates con hasta 3 enemigos y sirva de prueba al jugador de la dificultad de los combates siguientes.
- **Nivel 5:** Este combate será contra un ME y un PM.
- **Nivel 6:** Este combate será contra un BE y dos RE para equilibrar la fuerza que el jugador debería tener a este punto (se supone un arma de nivel II).
- **Nivel 7:** Este combate será contra un ME y un BE, en el que el jugador probará un combate contra dos enemigos con habilidades especiales por primera vez, pero al ser solo dos, todavía no resultará un desafío mayor.
- **Nivel 8:** En este punto, se entiende que el jugador ya ha ido recolectando varios objetos curativos y armas poderosas, por lo que los combates a partir de este punto serán algo más desafiantes, presentando al CE y enfrentando además a dos ME.
- **Nivel 9:** Este combate será contra un CE, un ME y un BE, donde el jugador deberá tener en cuenta que ahora son 3 enemigos con habilidades especiales diferentes, con lo que se quiere lograr un aumento del requerimiento de estrategia en un combate.
- **Nivel 10:** Este combate será con 2 PM y 1 CE para bajar un poco la dificultad hasta el momento y dar al jugador una recompensa de nivel alto por una batalla de un nivel inferior.
- **Nivel 11:** Este combate será contra 1 CE y un BE para, al igual que el anterior, ir dándole al jugador la oportunidad de recolectar un buen botín antes del jefe final sin mucho esfuerzo.

### Historia
En 1589, los ingleses llegan a A Coruña bajo la orden de atacar el reino. Durante este periodo, asesinan al marido de María Pita, y esta, por venganza, comienza a enfrentarse contra ellos hasta llegar al hermano del capitán que dirigía el ataque, Francis Drake, y asesinarlo con una lanza que les había arrebatado.

## 6. HUD
### En combate
Los combates serán en un entorno estático y se verán de la siguiente forma:

![ImagenDiagramaCombate](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/combate.jpg)

El HUD mostrará la vida restante de los enemigos y del jugador, así como un cuadro con diálogos, un botón de ataque, un botón para la acción de defensa, un botón para la acción de ¡Qué locura! (el cual se activará cuando esta esté disponible) y un botón para acceder al menú de objetos (donde se podrá elegir qué objeto usar).

### Entre combates
Para ir de combate a combate, el jugador debe navegar a través de un mapa de puntos (estilo árbol). Cada punto del mapa se desbloquea de forma progresiva según se vaya avanzando en los combates, habiendo bifurcaciones por el camino con más combates.

Estas bifurcaciones no son obligatorias, ya que el jugador puede perfectamente seguir el camino que lleva hasta el final sin pasar por ellas. Aun así, librar los combates opcionales permitirá al jugador hacerse con un más/mejores armas y más items de curación.

![ImagenDiagramaMapa](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/mapa.jpg)

### Inventario
Para ver el inventario de objetos, se hará click en un botón predeterminado para desplegarlo de forma que el jugador podrá ver el arma actual que está usando (cuadro columna izquierda), otras armas (cuadro superior columna derecha), la comida (cuadro inferior columna derecha) y la información del objeto seleccionado (cuadro inferior).

![ImagenDiagramaInventario](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/inventario.jpeg)

## 7. Visual
Toda la estética será Pixel Art con entidades de juego de tipo Chibi.

Aparecerá un cuadro de texto cada vez que haya una conversación entre los personajes, un monólogo, onomatopeyas, acotaciones… Este cuadro contendrá texto animado al igual que muchos juegos de consola de modo que dé la sensación de que el jugador esté “escuchando” al personaje hablar simultáneamente. Los posibles botones para ir a los diferentes menús o cambiar de escena brillarán cuando pase el cursor por encima de estos.

Finalmente, en momentos críticos del juego habrá animaciones.

Imágenes de referencia:

![ImagenMariaPita](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/mariaPita.png)
*Referencia de sprites, María Pita - Maria Pita's Revenge (2022). Pantheon Studios.*

![ImagenRefBatalla](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/pokemon.png)
*Referencia de batalla - Pokemon Diamante y Perla (2007). Nintendo.*

![ImagenRefDialogo](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/animalCrossing.png)
*Referencia de diálogos - Animal Crossing New Horizons (2022). Nintendo.*

![ImagenRefBotones](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/finalFantasy.png)
*Referencia de botones - Final Fantasy 7 (1997). Square Enix.*

## 8. Menús y flujo del juego
El jugador podrá acceder a los siguientes menús:
- Pantalla de título
- Menú de pausa
- Selección de niveles
- Inventario (objetos)

La estructura del juego contendrá varias escenas que contribuirán al flujo del juego, y el flujo entre ellas será el siguiente:
![ImagenFlujo](https://github.com/PabloGonzalezArroyoo/G6-PVLI/blob/main/assets/gdd/escenas.png)

## 9. Referencias
- *Pokemon.* (1996). The Pokemon Company.
- *Final Fantasy 7.* (1997). Square Enix.
- *Fireboy & WaterGirl.* (2009). Oslo Albet.
- *Animal Crossing New Horizons.* (2020). Nintendo.
- *Bloodborne.* (2015). From Software.
- *Dark Souls.* (2011). From Software.

### Pantheon Studios ©2022
