**Programación de Videojuegos en Lenguajes Interpretados
Game Design Document**

- Agustín Castro De Troya(acastrod@ucm.es)
- Pablo Cerrada Vega(pablce01@ucm.es)
- Pablo Cao Calvo(pablocao@ucm.es)
- Beatriz Rubio Rodríguez(berubi03@ucm.es) 


# FIESTA PAVANA by ***Triolic Games***
 

![Imagen Triolic Games](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/otras/TRIOLIC.png)


### 1. Ficha técnica
- **Título:** Fiesta Pavana 
- **Género:** Acción
- **Target:** Casual Gamers
- **Plataforma:** PC
- **Modo de juego:** Solitario


### 2. Descripción
Fiesta Pavana es un juego donde el jugador controla una pavana (gaviota) por diferentes escenarios con temática animada. ¿El objetivo? Sortear enemigos y obstáculos para evitar la derrota y llegar lo más lejos posible.


### 3.	Jugabilidad

#### 3.1. Movimiento del personaje
El movimiento del personaje estará acotado por la pantalla y controlado por WASD. Habrá una pequeña aceleración al iniciar el movimiento, llegando a una velocidad máxima y contando con una deceleración para frenar. Además podremos ir en diagonal.

#### 3.2. Cámara
La cámara estará fija y será el escenario el que se desplace horizontalmente.

#### 3.3. Mecánicas del jugador
La mecánica principal es la de movimiento, teniendo además una mecánica secundaria que es la recogida de monedas a través de peces dorados.

#### 3.4. Mecánicas de escenario
La mecánica principal del escenario es un scroll lateral hacia la izquierda, moviéndose con una velocidad incremental a lo largo de la partida. El escenario irá transicionando cuando la pavana recoge ciertos objetos (desbloqueables en la tienda), dando lugar a diferentes lugares y obstáculos:
- **Flotador:** el escenario cambia a uno sobre el mar.
- **Casco de astronauta:** le servirá a la pavana para viajar a un escenario en el espacio.
- **Camiseta hawaiana:** la pavana irá a un escenario estático con temática hawaiana.
- **Cono de tráfico:** el escenario cambia al de Tierra(escenario inicial que no hace falta desbloquear).

En cuanto a los obstáculos, irán apareciendo de manera pseudoaleatoria en los diferentes escenarios, como carteles en la carretera o barcos en el mar.


#### 3.5. Enemigos
Diferenciaremos obstáculos de enemigos en que estos no serán estáticos y tendrán otras características como el desplazamiento vertical o mayor velocidad de desplazamiento.

Aparecerán también en los diferentes escenarios, algunos son: águilas, asteroides en el espacio o coches en la carretera.



### 4. Diseño de nivel
#### 4.1. Imagen y explicación de los escenarios


- Tierra: escenario en el que la pavana viajará por tierra firme. Será el escenario principal y desde donde partiremos a los demás escenarios. Habrá coches, carteles de carretera, globos...


- Mar: escenario ubicado sobre el mar. Habrá barcos, delfines, aviones...


- Espacio exterior: nos iremos al espacio donde habrá obstáculos como asteroides, además de ovnis como enemigos.


- Fiesta(Hawaii): escenario estático sin scroll donde solo habrá monedas para recolectar, bajo un contrarreloj, que te devolverá a otro escenario aleatorio tras ese tiempo o tras recolectar todas las monedas.

Por ejemplo el escenario de Tierra podría quedar así:

![Imagen Escenario Tierra](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/escenarios/Carretera/Carretera.jpg)



#### 4.2. Generación de escenarios
Contamos en el juego con varios escenarios, nombrados y explicados anteriormente, a los cuales se acceden con objetos como el flotador. Partimos del escenario de Tierra, y mediante un scroll lateral movemos el fondo de manera que parezca que nos desplazamos.

Primero habrá que desbloquear los objetos de escenario que nos llevan a otros escenarios a través de la tienda. Cuando recogemos uno de esos objetos que provocan el cambio de escenario habrá una transición y cambiaremos de un fondo a otro. Los fondos serán más largos que la pantalla de juego, favoreciendo el scroll para que no sea aburrido.




### 5.	HUD
#### 5.1. Mockup del HUD

![Imagen HUD](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/otras/HUD.png)

#### 5.2. Explicación de los elementos del HUD y su funcionamiento**

Plumas:  nuestro personaje contará con 2 vidas en forma de plumas(arriba a la izquierda) de manera inicial. Se podrá comprar en la tienda hasta un máximo de 5 vidas.
Score: puntuación de la partida actual(arriba).
HighScore: puntuación máxima que ha alcanzado el jugador en las partidas jugadas(arriba).
Peces dorados(monedas): contador de peces conseguidos(arriba a la derecha).



### **6. Visual**
El videojuego tiene un estilo de dibujo animado, ya que la escultura elegida proviene de un cómic y queríamos que nuestro proyecto tuviera dicho estilo. Además esta estética más familiar está enfocada a todos los públicos.

Los recursos estéticos se conseguirán mediante la página web “Flaticon” y de nuestra encargada de arte. Algunos ejemplos visuales serían:
![Imagen Pavana](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/otras/gaviotalogo.png)
![Imagen Shirt](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/objetos/shirt.png)
![Imagen Flotador](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/objetos/lifebuoy.png)

### **7. Contenido**

#### **7.1. Entidades**

| Nombre    | Descripción | Tipo | Escenario |
|-----------|:-----------:|:----:|----------:|
|Pavana     |Es el personaje que manejamos durante el juego. Movimiento uniformemente acelerado hacia arriba, abajo, izquierda, derecha y en diagonal.|Protagonista|Todos|
|Águilas   |Aves un poco más grandes que la Pavana que realizan un movimiento vertical en picado.|Enemigo|Carretera|
|Ovnis      |Naves que hacen un movimiento de teletransporte.|Enemigos|Espacio|
|Coches     |Vehículos que van a una velocidad mayor que el escenario.|Enemigo|Tierra|
|Isla    |Montículo de tierra con un cocotero.|Obstáculo|Mar|
|Avion  |Tienen mayor tamaño que la Pavana y dos tipos de movimiento.|Enemigo|Tierra y Mar| 
|Cartel  |Señales de tráfico. Se esquivan por arriba.|Obstáculo|Tierra|
|Barcos     |Tendrán un balanceo sobre el mar.|Enemigo|Mar|
|Asteroides |Obstáculo que contará con una animación de rotación.|Enemigo|Espacio|
|Globo      |Tienen un tamaño similar al avion, apareciendo por todo el cielo.|Enemigo|Tierra y Mar|
|Delfín      |Realizan un movimiento propio de un delfín. Tienen tamaño similar a la Pavana.|Enemigo|Mar|
|Árbol     |Aparecen como los carteles, en la carretera.|Obstáculo|Carretera|
|Bomba     |Aparecen como castigo al quedarte quieto. Caen desde arriba y te restan una vida si no las esquivas.|Enemigo|Todos|
|Flotador   |Provoca el cambio al escenario marítimo.|Objeto|Tierra, Espacio|
|Casco Astronauta|Con esto iremos al escenario en el espacio.|Objeto|Tierra y Mar|
|Camisa Hawaiiana|Lo encontramos con una baja probabilidad. Cambia al escenario de la Fiesta(Hawaii).|Objeto|Todos|
|Cono de tráfico|Provoca el cambio al escenario terrestre.|Objeto|Espacio, Mar|
|Peces Dorados|Bonificaciones con las que el jugador podrá comprar elementos en la tienda.|Objeto|Todos|




#### **7.2. Tienda del juego**

En la tienda se podrá mejorar distintas características para poder obtener un mejor récord y objetos de escenario que harán cambiar el fondo, los obstáculos y los enemigos.
Se podrán aumentar el número de vidas y aumentar el multiplicador de puntuación.

Una imagen de cómo se podría ver la tienda:

![Imagen Tienda](https://raw.githubusercontent.com/AgusCDT/FiestaPavana/main/assets/imagenes/otras/shopScreenshot.PNG)


### **8. Referencias**

**Flappy Bird**
- **Género:** Acción
- **Modo de Juego:** Solitario 
- **Plataforma:** PC



**Dinosaurio de Chrome**
- **Género:** Acción
- **Modo de Juego:** Solitario
- **Plataforma:** PC
