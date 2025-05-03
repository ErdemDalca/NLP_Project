# Stratum : Game Design Document


# Contenidos

[0. Introducción](#0-introducción)

[1. Reglamento](#1-reglamento)

* [1.1. Descripción del juego](#11-descripción-del-juego)

* [1.2. Facciones](#12-facciones)

* [1.3. Inicio de la partida](#13-inicio-de-la-partida)

* [1.4. Rondas y turnos](#14-rondas-y-turnos)

* [1.5. Ecosistema](#15-ecosistema)

* [1.6. Personajes](#16-personajes)

* [1.7. Cartas](#17-cartas)

[2. Interacción y Navegación](#2-interacción-y-navegación)

[3. Narrativa](#3-narrativa)

* [3.1. Historia del Juego](#31-historia-del-juego)

[4. Arte y apartado visual](#4-arte-y-apartado-visual)

* [4.1. Estilo visual general](#41-estilo-visual-general)

* [4.2. Arte de las cartas](#42-arte-de-las-cartas)

* [4.3. Fichas y arte de los personajes](#43-fichas-y-arte-de-los-personajes)

* [4.4. Escenarios y ambientación](#44-escenarios-y-ambientación)

* [4.5. El ecosistema](#45-el-ecosistema)

* [4.6. Iconografía y tipografía](#46-iconografía-y-tipografía)

[5. Sonido y Música](#5-sonido-y-música)

* [5.1. Visión General del Sonido](#51-visión-general-del-sonido)

* [5.2. Música](#52-música)

* [5.3. Efectos de Sonido (SFX)](#53-efectos-de-sonido-sfx)

[6. Modelo de negocio y monetización](#6-modelo-de-negocio-y-monetización)

* [6.1. Información sobre el usuario](#61-información-sobre-el-usuario)

* [6.2. Mapa de empatía](#62-mapa-de-empatía)

* [6.3. Caja de herramientas](#63-caja-de-herramientas)

* [6.4. Modelo de canvas](#64-modelo-de-canvas)

* [6.5. Monetización](#65-monetización)




# 0. Introducción

Este es el _Game Design Document_ de **Stratum**, donde se describen todos los aspectos del proyecto.

**Stratum** es un videojuego de cartas multijugador en línea para 4 jugadores, desarrollado como proyecto para varias asignaturas de 4° año de la carrera de Diseño y Desarrollo de Videojuegos en la Universidad Rey Juan Carlos. Cada apartado explica el videojuego desde distintos puntos de vista y detalla sus características principales, aunque lo esencial es que **Stratum** ofrece una experiencia "analógica" e inmersiva sin necesidad de una interfaz gráfica visible, permitiendo a los jugadores sumergirse en la creación de un ecosistema en constante cambio.


# 1. Reglamento
En esta sección se explicarán todas las mecánicas del juego. Al ser un juego de cartas, se seguirá la estructura que suelen tener los manuales de  juegos de cartas de mesa.

## 1.1. Descripción del juego
**Stratum** es un juego de cartas para 4 jugadores, en el que hay un ecosistema al que contribuyen todos los jugadores jugando **cartas de población**: plantas, herbívoros y carnívoros. Este ecosistema está vivo y va cambiando si está desequilibrado, para balancearse de forma natural. Cada jugador juega el papel de un personaje. Los 4 personajes están divididos en 3 facciones, cada una de las cuales busca imponer sus intereses sobre las demás, usando las leyes de la naturaleza a su favor para equilibrar o desequilibrar el ecosistema. Además, cada jugador tiene en su mazo **cartas de influencia**, únicas para cada personaje, las cuales puede usar para influir en el ecosistema de manera artificial.

## 1.2. Facciones

### Naturaleza
Compuesta por los personajes **Sagitario** y **Ygdra**, esta facción gana la partida si a lo largo de la partida consigue 7 crecimientos totales de herbívoros y/o carnívoros (poblaciones que pueden crecer).  

### Industria
Compuesta por el personaje **El Magnate**, esta facción gana la partida si, al final de una ronda, tiene construcciones en 2 territorios.

### Fungi
Compuesta por el personaje **Fu'ngaloth**, esta facción gana la partida si, al final de una ronda, tiene 2 macrohongos en la mesa.

## 1.3. Inicio de la partida
Los jugadores se disponen, uno a cada lado de una mesa cuadrada, siguiendo este orden, en el sentido inverso a las agujas del reloj: Sagitario, Fu'ngaloth, Ygdra, El Magnate.

Cada jugador tiene delante su **territorio**. Este está compuesto por 5 espacios de territorio. Cuando sea su turno, el jugador podrá jugar cartas de población en estos espacios.

Cada jugador empieza con 5 cartas.

El ecosistema (la mesa) empieza con 4 cartas de población: 2 plantas, 1 herbívoro y 1 carnívoro. Estas se disponen de manera aleatoria, cada una en el espacio de territorio situado más a la izquierda de cada jugador.

![Ejemplo Inicio](/Readme%20Files/EjemploComienzo.png)

Comienza jugando Sagitario, y el orden de turnos sigue el sentido inverso a las agujas del reloj.

![Orden de Juego](/Readme%20Files/OrdendeJuego.png)

## 1.4. Rondas y turnos
Una ronda consiste en los turnos de los 4 jugadores, y el turno del ecosistema.

Cada jugador en su turno tiene 2 acciones: una para jugar una **carta de población** y otra para jugar una **carta de influencia**. Puede elegir jugarlas en cualquier orden. 

Las cartas de población se pueden jugar sobre un espacio de territorio vacío. Cada jugador tiene que jugarlas en su territorio.

Cada carta de influencia explica cómo se debe jugar. Algunas se juegan poniéndolas sobre la mesa para aplicar su efecto y luego descartándolas, otras se ponen sobre cartas de población para concederles un efecto, ya sea inmediato o en el futuro, cuando se cumpla una condición.

El jugador puede usar una acción para descartar una carta, en vez de jugarla. También puede usar las 2 acciones y descartar 2 cartas. Si el jugador no puede jugar ninguna carta debe descartarse de 2 cartas, para siempre terminar su turno con 3 cartas en la mano.

Cuando ha terminado su turno el último jugador (Fu'ngaloth), es el turno del ecosistema. En este, las cartas de población que hay sobre la mesa pueden crecer o morir, según las Reglas del Ecosistema.

Cuando termina el turno del ecosistema, todos los jugadores roban 2 cartas, para volver a comenzar su turno con 5.

![Ronda](/Readme%20Files/Ronda.png)


## 1.5. Ecosistema
En su turno, el ecosistema cambia según las cartas de población que haya sobre la mesa. Si las plantas, herbívoros y carnívoros no están en equilibrio, sucede al menos 1 de estos 2 casos:

- Una o más cartas de población **mueren**: la carta muerta se retira de la mesa, y si ninguna carta de influencia lo impide, se añade una carta de hongo en el espacio de territorio en el que estaba puesta dicha carta.

- Una o más cartas de población **crecen**: en el mismo espacio de territorio, encima de la carta de población que crece, se añade una carta igual.

La última carta de población de cada tipo (planta, herbívoro o carnívoro) en haberse jugado, se marca con ficha. Estas cartas son las que, en el turno del ecosistema, podrían crecer o morir si se cumplen las condiciones.

### Reglas del ecosistema
Estas son las directrices que se usan para determinar si hay cartas de población que crecen o mueren.

Las condiciones se comprueban secuencialmente (una por una), y los cálculos se hacen con el número de cartas resultantes después de haber realizado el cálculo de la condición anterior. Es decir, si empieza el turno del ecosistema habiendo 4 herbívoros, y después de comprobar la primera condición muere 1  herbívoro, las siguientes condiciones se comprobarán con 3 herbívoros, no con 4.

Como mucho puede morir o crecer 1 carta de herbívoro y 1 carta de carnívoro en cada turno del ecosistema.

Las condiciones, en orden de comprobación, son:

#### 1. Condiciones para que **mueran herbívoros**:
- Tiene que haber al menos una carta de herbívoro.
- Se debe cumplir al menos una de estas condiciones:
    - No hay cartas de planta en la mesa.
    - Debe haber al menos 2 cartas más de herbívoros que de plantas.
    - Debe haber al menos 2 cartas más de carnívoros que de herbívoros.

#### 2. Condiciones para que **crezcan herbívoros**:
- No puede haber muerto ninguna carta de herbívoro en la condición anterior.
- Tiene que haber al menos una carta de herbívoro.
- Tiene que haber al menos una carta de planta.
- Se debe cumplir al menos una de estas condiciones:
    - No hay cartas de carnívoro en la mesa.
    - Debe haber al menos 2 cartas más de herbívoros que de carnívoros.
    - Debe haber al menos 2 cartas más de plantas que de herbívoros.

#### 3. Condiciones para que **mueran carnívoros**:
- Tiene que haber al menos una carta de carnívoro.
- Se debe cumplir al menos una de estas condiciones:
    - No hay cartas de herbívoros en la mesa.
    - Debe haber al menos 2 cartas más de carnívoros que de herbívoros.

#### 4. Condiciones para que **crezcan carnívoros**:
- No puede haber muerto ningún carnívoro en la condición anterior.
- Tiene que haber al menos una carta de carnívoro.
- Debe haber al menos 2 cartas más de herbívoros que de carnívoros.

## 1.6. Personajes
Cada personaje tiene un objetivo único para ganar el juego, excepto los dos de la facción Naturaleza, que comparten el mismo objetivo. Los personajes de las facciones Industria y Fungi cuentan con mecánicas exclusivas para alcanzar sus objetivos y ganar la partida. Además, todos los personajes disponen de cartas de influencia propias.

### Ygdra
Es el ente protector de los árboles y plantas. Sus cartas de influencia están orientadas a las plantas.

Para ganar, debe, junto con Sagitario, conseguir que al final de una ronda, después del turno del ecosistema, haya en la mesa al menos 4 plantas, 3 herbívoros y 3 carnívoros.


### Sagitario
Es el ente protector de los animales. Sus cartas de influencia están orientadas a los animales.

Para ganar, debe, junto con Ygdra, conseguir que al final de una ronda, después del turno del ecosistema, haya en la mesa al menos 4 plantas, 3 herbívoros y 3 carnívoros.


### El Magnate
Representa la voluntad indomable de la humanidad, el deseo de imponerse a la naturaleza.

Para ganar debe conseguir que al final de una ronda, después del turno del ecosistema, haya construcciones en los 4 territorios.

#### Construcción
Es una acción exclusiva de El Magnate. En su turno, puede elegir gastar una acción para construir sobre uno de los 4 territorios. Para poder construir sobre un territorio se deben cumplir las siguientes condiciones:
- El territorio no tiene una construcción.
- El territorio no tiene ninguna carta de población de carnívoros.
- El territorio no tiene ninguna carta de población con una  carta de influencia puesta que impida construir.
- El territorio tiene al menos 2 cartas de población de plantas.

Al construir, se pone una ficha en frente del territorio para indicar que tiene construcción. Mueren las 2 cartas de planta más recientes del territorio.

Después, se puede jugar con normalidad cartas de criatura sobre el territorio construido, y la construcción se puede destruir usando cartas de influencia que lo permitan.

Se puede construir nuevamente sobre un territorio que tuvo un terreno y fue destruido, si se cumplen las condiciones descritas.

### Fu'ngaloth
Es una deidad ancestral de los hongos, cuya voluntad es que los hongos se impongan sobre todas las otras formas de vida.

Para ganar debe conseguir que al final de una ronda, después del turno del ecosistema, haya en la mesa al menos 2 macrohongos.

#### Macrohongo
Es una acción exclusiva de Fu'ngaloth. En su turno, puede elegir gastar una acción para crear un macrohongo. Para poder crearlo, debe haber al menos 3 cartas de hongo en la mesa. La acción consiste en descartar 3 cartas de hongo, y poner una carta de macrohongo en uno de esos 3 espacios de territorio, a elección del jugador.

El macrohongo no puede ser destruido por cartas de influencia, a menos que la descripción de la carta lo indique explícitamente.

## 1.7. Cartas
### Cartas de población
- **Planta**
- **Herbívoro**
- **Carnívoro**

### Cartas de influencia
#### Ygdra
- **Madre Naturaleza:** Esta carta provoca un turno de ecosistema, comprueba las condiciones necesarias para aumentar o reducir las diferentes poblaciones y aplica los efectos. Si alguna población crece, este crecimiento contará para el contador de crecimientos para la victoria de Ygdra y Sagitario. 
- **Incendio Forestal:** Elige un territorio. Todas las cartas de población, hongo y macrohongo en ese territorio mueren. Si hay una construcción, también se destruye.
- **Fragancia de feromonas:** Elige una carta de herbívoro o carnívoro de otro territorio y muévela a un espacio vacío en tu territorio.
- **Hiedra Verde:** Coloca esta carta sobre una carta de planta. Al final de la ronda, si hay una construcción en su territorio, se destruye la construcción y descarta esta carta de la planta.


#### Sagitario
- **Madre Naturaleza:** Esta carta provoca un turno de ecosistema, comprueba las condiciones necesarias para aumentar o reducir las diferentes poblaciones y aplica los efectos. Si alguna población crece, este crecimiento contará para el contador de crecimientos para la victoria de Ygdra y Sagitario. 
- **Rabia:** Coloca esta carta sobre una carta de herbívoro. Mientras no muera, El Magnate no podrá construir en el territorio donde esté.
- **Migración:** Elige una carta de carnívoro o herbívoro de tu territorio y muévela a un espacio vacío en otro territorio.
- **Depredador de setas:** Coloca esta carta sobre una carta de herbívoro. Mientras no muera, al final de la ronda morirá la carta de hongo más reciente que haya en su territorio.


#### El Magnate
- **Incendio provocado:** Elige un territorio. Todas las cartas de población, hongo y macrohongo en ese territorio mueren. Si hay una construcción, también se destruye.
- **Fuegos artificiales:** Elige una carta de herbívoro o carnívoro y muévela a un espacio vacío en el territorio opuesto al que se encuentra.
- **Compost:** Elige un espacio vacío de un territorio. Coloca una carta de hongo y una carta de planta encima.
- **Correa:** Escoge una carta de herbívoro o carnívoro. Esta carta escogida no podrá ser movida con cartas de influencia. 


#### Fu'ngaloth
- **Esporas explosivas:** Elige un territorio donde haya al menos una carta de hongo o macrohongo. Todas las cartas de población en ese territorio mueren. Si hay una construcción también se destruye. Las cartas de hongo y macrohongo no mueren.
- **Putrefacción:** Muere una carta de planta de tu elección. Crece un hongo en su espacio de territorio.
- **Seta apetitosa:** Elige una carta de herbívoro o carnívoro y muévela a un espacio vacío en un territorio donde haya al menos una carta de hongo o macrohongo.
- **Moho:** Coloca una carta de hongo sobre un espacio vacío de un territorio con construcción.


# 2. Interacción y navegación

**Stratum** es un videojuego sin interfaz externa al escenario (Head-Up Display), por lo tanto todas las interacciones del usuario se realizan tocando, moviendo y manipulando objetos del escenario, tridimensionales. La cámara es en primera persona, con movimientos entre posiciones fijas. En esta sección se explicarán todas esas interacciones, y el flujo de pantallas del juego.

## 2.1. Menú principal
Es una escena que consta de un pasillo tipo vestíbulo, con una mesa alta al final, y 1 puerta a cada lado, también al final. El jugador podrá cambiar entre 2 posiciones fijas: lejos y cerca de la mesa. Al acercarse verá varios objetos con los que puede interactuar.

### Radio de onda corta:
![Radio de onda corta](https://c8.alamy.com/comp/2B41YF7/am-shortwave-radio-dial-2B41YF7.jpg)

Tiene 6 perillas con caracteres alfanuméricos encima que cambian cuando gira su manivela. Además tiene 2 botones: Crear sala y Unirse a sala. 

Pulsar el de crear sala hace que las perillas giren para mostrar el código de 6 caracteres de la sala, para compartirlo con el resto de jugadores. 

Pulsar el de unirse a sala hace que, cuando escribas un caracter con el teclado, se gire la manivela para mostrarlo, y se pase a la siguiente manivela. De esta forma se puede escribir el código, y cuando se haya escrito entero se intentará unir a esa sala.

Cuando haya 4 jugadores en la sala, se deseleccionará la radio en el juego de los 4, y se activará una animación de caminar hacia la puerta de la izquierda. Cuando llegue, se abrirá, y se transicionará a la habitación del juego.

### Gramófono
![Gramófono](https://djvitage.com/wp-content/uploads/2024/08/gramofono-retro-19645057.webp)

Tiene un vinilo, una manivela y una perilla. También tiene una nota sobre él, explicando el uso de cada elemento.

Al pulsar el disco, este cambia de lado, cambiando también el idioma del juego.

Al pulsar la manivela, va cambiando entre 3 estados, haciendo que el disco gire a 3 respectivas velocidades, cada una representa una configuración de gráficos: baja, media y alta.

Al pulsar la rueda va girando entre 5 estados de volumen, de menos a más. Al pulsarla en el estado de mayor volúmen, pasa al estado de 0 volumen.

### Libro de registro
![Libro de registro](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbXQIXsjSDk2vS0vi9g5FosehG5gd_0V73FQA_tYth6aq8Fm_nBGIXLb8WmYs5X2ZXQFP0v-yQtK5auyxeElZxf6-_ct2ztjjSwOxgVcNwqh7xPrvV5jknyDd_lVV1P2wmNylsW3gqOSmN/w1200-h630-p-k-no-nu/20180913_FLR_HistoricLedgers-56.jpg)

Al pulsarlo, se abre por la mitad y aparecen 2 páginas:
 1. **Créditos:** en la primera página aparecen los créditos del juego, escritos "a mano" en el libro.
 2. **Contacto:** en la segunda página hay iconos de las redes sociales del estudio. Al pulsarlos, abren en el navegador del jugador el vínculo elegido.

 ### **Manual de reglas:** 
 
 ![Reglas](https://static.wikia.nocookie.net/nickelodeon/images/a/a5/Darules.jpg/revision/latest/scale-to-width-down/250?cb=20170212060658)

 Al pulsarlo, se abre por el principio, y empieza una animacion de "entrar en el manual". Este transporta al jugador al tutorial del juego.


## 2.2. Habitación del juego

En esta escena el jugador empieza entrando por la puerta de la habitación, viendo que los otros 3 personajes ya están sentados en la mesa del centro de la habitación. El jugador avanza automáticamente y se sienta. y comienza la partida.

Cuando gana una de las facciones, sucede:

1. Aparece un orbe (o dos, si ha ganado la facción Naturaleza) en el centro de la mesa, y se dirige hacia la facción ganadora. 
2. Depende de si ha ganado Naturaleza o no, la facción ganadora absorbe el orbe, o lo destruye, para simbolizar fusionarse o imponerse con el ecosistema que estaba en disputa.
3. El jugador local se levanta el primero, y sale por la puerta, fundiendo al menú principal.


## 2.3. Controles

En una partida, se seleccionan las cartas con el cursor y se juegan arrastrándolas, haciendo click y manteniendo, y soltando sobre el elemento (carta, espacio de territorio, pila de descarte, etc.) donde se quiera jugarla. Con la rueda del ratón se cambia entre 2 perspectivas, una más enfocada en la mano de cartas, y otra enfocada en la mesa, vista desde arriba.

En móvil, igualmente, se pulsa para seleccionar y se mantiene pulsado para arrastrar cartas. Se desliza verticalmente para cambiar entre las 2 perspectivas.

Para interactuar con los objetos del menú principal, se usa el ratón para destacarlos con el cursor, y el clic para seleccionarlos al pulsar sobre ellos. Para introducir el código de sala en la radio se usa el teclado.

En móvil, al pulsar sobre un objeto se destaca, y al mantener pulsado se selecciona. 

Para introducir el código de sala en la radio, se despliega el teclado táctil mientras esté seleccionada. El equipo de **Against Software** pide perdón a todos los jugadores por este uso de interfaz gráfica, pues se ha tratado de evitar cualquier tipo de _HUD_, pero para que funcione la radio correctamente en navegadores móviles hemos tenido que recurrir a esto.

# 3. Narrativa

## 3.1. Historia del Juego

En un rincón olvidado del mundo, oculto del alcance de la humanidad, yace el legendario bosque de **Sylveria**, un lugar antiguo y sagrado donde la vida fluye en armonía. Este bosque es el centro de un conflicto ancestral entre tres facciones primordiales: **Naturaleza**, **Fungi**, y la reciente aparición de la **Industria**. Cada una busca imponer su visión sobre el destino de **Sylveria**, pues controlar este bosque es controlar la fuente de toda su vitalidad.

El equilibrio del bosque está determinado por un juego antiguo, conocido como **Stratum**, cuyas reglas han sido esculpidas por el tiempo y la magia que envuelve **Sylveria**. Desde la creación del bosque, el poder y la vida en este lugar han sido regidos por este misterioso juego de cartas, y ahora, como jugador, es tu turno de decidir quién tomará el control de **Sylveria**.

### **Sylveria: El Corazón del Bosque**

**Sylveria** es mucho más que un simple bosque; es el núcleo de toda la vida natural, y su influencia se extiende a todas las criaturas y plantas que residen dentro de sus límites. Sus árboles milenarios, cuyas raíces se adentran profundamente en la tierra, conectan con la esencia misma del mundo, sirviendo de refugio para las energías naturales que sostienen el equilibrio.

Cada facción tiene sus propios motivos para desear el control de **Sylveria**. Para la **Naturaleza**, es su santuario más preciado; para la **Industria**, una tierra rica en recursos que debe ser conquistada; y para los **Fungi**, es el lugar perfecto para extender su dominio micelial. **Stratum** es el medio por el cual este control será disputado, y quien gane dominará el destino del bosque y su futuro.

### **Naturaleza**

La facción de la **Naturaleza** es salvaguardada por dos guardianes primordiales: **Sagitario**, protector de los animales, e **Ygdra**, la guardiana de las plantas. Ellos han mantenido a **Sylveria** en equilibrio durante generaciones, asegurando que los ecosistemas dentro del bosque prosperen sin perturbaciones. Los ríos cristalinos y los densos bosques que definen este paisaje son testigos de su dedicación.

Los guardianes de la **Naturaleza** enfrentan amenazas constantes. Por un lado, las oscuras fuerzas de los **Fungi** buscan invadir y corromper **Sylveria**, transformando sus tierras fértiles en un reino fúngico. Por otro, la **Industria** avanza con sus máquinas, talando árboles y construyendo estructuras que contaminan el aire y la tierra. Los protectores naturales están decididos a evitar la destrucción del bosque, sabiendo que si **Sylveria** cae, el equilibrio de la vida en este lugar se romperá para siempre.

### **Industria**

La **Industria** ha surgido con el implacable avance humano, liderada por el ambicioso **Magnate**. Su visión es clara: transformar el bosque de **Sylveria** en una fuente de recursos y progreso. El avance de la **Industria** no se detiene ante nada, pues las verdes tierras son vistas como materiales en bruto, listos para ser explotados. Bajo su mando, el gris cemento y el frío metal han comenzado a reemplazar los árboles y ríos que una vez prosperaban aquí.

El **Magnate** ve a **Sylveria** como la joya que falta para completar su dominio. Cada fábrica que construye y cada bosque que arrasa lo acerca a su meta de controlar el último reducto de resistencia natural. **Stratum** es el camino para lograrlo, y bajo las reglas de este juego ancestral, la **Industria** hará lo que sea necesario para someter el bosque a su voluntad.

### **Fungi**

En lo más profundo de la tierra, **Fu'ngaloth**, la antigua deidad de los hongos, espera pacientemente. Su reino fúngico crece bajo la superficie de **Sylveria**, y aunque no se ve a simple vista, su influencia se extiende lentamente por el bosque. Los **Fungi** no buscan una conquista rápida; su estrategia es más sigilosa. Propagan sus esporas y sus macrohongos con el fin de asimilar todo lo que tocan, y en **Sylveria** encuentran el terreno fértil que necesitan para expandirse.

El poder de **Fu'ngaloth** reside en su capacidad para corromper la vida, transformando lo verde en descomposición, y conectando todo lo que ha tocado a su vasto reino micelial. Para él, **Sylveria** no es solo un lugar, sino el portal a la dominación total de la vida que habita en sus tierras. El control del bosque asegurará su expansión sin fin.

### **Conflicto**

El conflicto en **Sylveria** nace de la colisión de estas tres poderosas facciones. Cada una de ellas tiene sus propias ambiciones y motivos para desear el control del bosque, pero todas entienden que, sin **Sylveria**, sus planes están condenados al fracaso. Mientras que la **Naturaleza** busca mantener el equilibrio, tanto la **Industria** como los **Fungi** luchan por someter al bosque y dominar sus riquezas.

Aunque las facciones de **Industria** y **Fungi** podrían aliarse temporalmente para desestabilizar a la **Naturaleza**, sus ambiciones individuales son irreconciliables. El **Magnate** ansía someter el bosque a su maquinaria, mientras **Fu'ngaloth** desea absorber **Sylveria** en su red de hongos. La traición está asegurada, ya que ninguno de los dos está dispuesto a compartir el poder que este lugar otorga.

Como jugador, ahora es tu turno. **Stratum**, el juego ancestral que ha determinado el destino del bosque desde tiempos inmemoriales, está en tus manos. Navegarás esta compleja red de alianzas temporales y traiciones inevitables mientras luchas por controlar **Sylveria**. ¿Te aliarás con otros para lograr tus objetivos, o caerás víctima de las traiciones en esta batalla por el control del bosque?


# 4. Arte y apartado visual
## 4.1. Estilo visual general
El estilo visual de **Stratum** se inspira en una combinación de arte **low-poly** y elementos estilizados del **Art Nouveau**. Este enfoque se alinea con la temática del juego, que enfrenta la preservación de los ecosistemas contra su explotación industrial y la expansión de los hongos.

Inspiración:

![Cartas1](/Readme%20Files/Arte/Imagen1.jpg)  
![Cartas2](/Readme%20Files/Arte/Imagen2.jpg)  
![Sofá](/Readme%20Files/Arte/Imagen3.jpg)  
![Marcos](/Readme%20Files/Arte/Imagen4.png)  
![Paleta](/Readme%20Files/Arte/Imagen5.jpg)   
![Ascensor](/Readme%20Files/Arte/Imagen6.jpg)  
![Gato](/Readme%20Files/Arte/Imagen7.jpg)  

### Modelado 3D
Los modelos tridimensionales del entorno de juego y los personajes se desarrollarán con un estilo **low-poly**, evocando la estética de juegos de la era **PSX**. Este enfoque simplificado ayuda a capturar la esencia visual de cada elemento sin sobrecargar la representación gráfica, manteniendo un aspecto nítido y comprensible en un entorno 3D.

-	**Entornos**: Los territorios donde los jugadores colocarán sus cartas serán diseñados con geometría simple y texturas planas que respeten el estilo low-poly. Las texturas y colores de cada territorio reflejarán los temas de la facción a la que pertenecen (naturaleza, industria, hongos).   
![Escenario](/Readme%20Files/Arte/Imagen8.png)  
![Hongos1](/Readme%20Files/Arte/Imagen9.jpg)  
![Hongos2](/Readme%20Files/Arte/Imagen10.png)  
![Fabrica](/Readme%20Files/Arte/Imagen11.png)  
![Lobo](/Readme%20Files/Arte/Imagen12.jpg)  
![Ciervo](/Readme%20Files/Arte/Imagen13.jpg)  
![Animales](/Readme%20Files/Arte/Imagen14.jpg)  


    
### Renderizado y texturizado
El juego utilizará **cel-shading** para lograr un estilo visual estilizado. Este enfoque, junto con el uso de modelos **low-poly** y texturas simples y planas, se ha seleccionado para optimizar el rendimiento en todos los dispositivos, ofreciendo una experiencia fluida y accesible sin sacrificar el estilo visual del juego.

- **Volumetría y luces**: Se emplearán luces volumétricas sutiles para enfatizar momentos clave del juego, como cuando un jugador realiza una acción importante o cuando se producen cambios dramáticos en el ecosistema.

![Lethal Company](/Readme%20Files/Arte/Imagen25.jpg)  
![Jet Set Radio](/Readme%20Files/Arte/Imagen26.jpg)  

## 4.2. Arte de las cartas
### Cartas de población

Las cartas de población representan a plantas, herbívoros y carnívoros. Cada tipo de carta será ilustrada en 2D, manteniendo el estilo general del Art Nouveau con énfasis en líneas fluidas y detalles orgánicos.

## Plantas 
Diseñadas con tonos azulados. Las ilustración mostrará una flor enmarcada por patrones orgánicos.   

## Referencias
![Flor1](/Readme%20Files/Arte/Imagen27.jpg)   
![Flor2](/Readme%20Files/Arte/Imagen28.jpg)   
![Flor3](/Readme%20Files/Arte/Imagen29.jpg)

## Arte Final
![CartaPlantas](/Arte/Carta/cartas/plants.png)

## Herbívoros
Representados con colores cálidos y suaves destacando el equilibrio en el ecosistema.  
## Referencias
![Ciervo2](/Readme%20Files/Arte/Imagen30.jpg)  
![Ciervo3](/Readme%20Files/Arte/Imagen31.jpg)
## Arte Final
![Carta Herbívoros](/Arte/Carta/cartas/hervibores.png)

## Carnívoros
Con tonos más rojizos y formas agresivas, pero siempre respetando la estética estilizada y orgánica del juego.  
## Referencias
![Lobo2](/Readme%20Files/Arte/Imagen32.jpg)  
![Oso](/Readme%20Files/Arte/Imagen33.jpg)  
## Arte Final
![Carta Carnívoros](/Arte/Carta/cartas/carnivores.png)

## Hongos
Carta con colores morados. Con estética orgánica haciendo una representación de setas/hongos.
## Arte Final
![Carta Hongos](/Arte/Carta/cartas/fungus.png)

### Cartas de influencia
Cada facción tendrá cartas de influencia únicas que permitirán alterar el ecosistema. El estilo artístico variará según la facción:

- **Naturaleza**: las cartas de Sagitario y Ygdra tendrán ilustraciones en 2D que evoquen la vitalidad del ecosistema.
- **Industria**: las cartas de El magnate destacarán la maquinaria y la destrucción del ecosistema con tonos grises y metálicos.
- **Fungi**: las cartas de Fu’ngaloth tendrán elementos que evoquen corrupción y expansión de hongos, usando una paleta de colores oscuros y púrpuras.

## 4.3. Fichas y arte de los personajes
  ### Personajes

  Cada uno de los personajes será representado con **modelos 3D de baja resolución** que mantendrán características distintivas de sus facciones, mientras que sus detalles principales se concentrarán en las siluetas y colores característicos.
  ## Sagitario

  **Facción**: Naturaleza  
  **Rol**: Protector de la fauna / Guardián de las bestias  

  ## Descripción Física
  - **Edad**: Eterno, pero aparenta unos 30 años  
  - **Altura**: 2.10 m  
  - **Complexión**: Fuerte y atlética, con una figura estilizada y elegante  
  - **Rasgos físicos**: Sagitario tiene una presencia majestuosa, con rasgos faciales afilados y ojos dorados que reflejan sabiduría y ferocidad. Sus orejas son puntiagudas, y tiene cuernos que se curvan hacia atrás, reminiscentes de una cabra.  
  - **Vestimenta**: Su tren superior está recubierto por hojas de los árboles del bosque. Lleva una lanza imbuida con la esencia de las criaturas del bosque; la punta es de piedra lunar y brilla ligeramente en la oscuridad.  

  ## Personalidad
  - **Ferozmente protector**: Sagitario es el defensor absoluto de todas las criaturas de Sylveria. Está dispuesto a luchar hasta el final para proteger el equilibrio natural, y su instinto protector es tan salvaje como los animales que cuida.  
  - **Conexión primitiva**: Tiene una conexión profunda y casi mística con la fauna, lo que le permite comunicarse con los animales, entender sus necesidades y sentir su dolor. Esta habilidad le permite liderar ejércitos de bestias cuando es necesario.  
  - **Sabiduría ancestral**: Aunque es temible en la batalla, Sagitario es también una figura sabia y reflexiva. Su conocimiento de la naturaleza es vasto, y siempre busca armonía antes que conflicto, aunque no dudará en usar la fuerza si el equilibrio está amenazado.  
  - **Desconfianza hacia la humanidad**: Después de ver cómo la humanidad explota y destruye el entorno, Sagitario ha desarrollado una actitud distante y cautelosa hacia los humanos, especialmente aquellos que buscan explotar la naturaleza para su propio beneficio.  

  ## Historia
  Nacido del corazón del bosque de Sylveria, Sagitario es un ente creado por el poder mismo de la naturaleza. Surgió cuando las bestias se unieron para pedir protección contra la creciente amenaza humana. Durante siglos, ha sido el guardián silencioso de las criaturas del bosque, vigilando desde las sombras y actuando solo cuando es absolutamente necesario.

  Con la llegada de *El Magnate* y su sed de dominación industrial, Sagitario se ha visto obligado a abandonar su papel como observador pasivo para tomar acción directa. Ahora, lidera la resistencia de la naturaleza contra la invasión industrial, utilizando su conocimiento del terreno y su conexión con las bestias para enfrentarse a las máquinas de El Magnate.

  ## Motivaciones
  - **Proteger a Sylveria**: La misión principal de Sagitario es asegurar que el equilibrio natural de Sylveria se mantenga intacto, haciendo todo lo posible para evitar que los humanos destruyan el hogar de las criaturas que ha jurado proteger.
  - **Restaurar el equilibrio**: Sagitario no solo quiere detener la industrialización; también sueña con revertir el daño que se ha hecho. Desea un Sylveria donde la naturaleza pueda florecer sin interferencias externas, donde cada criatura tenga un lugar seguro.
  - **Venganza contra los explotadores**: Aunque prefiere la paz, la furia de Sagitario se desata contra aquellos que buscan explotar el mundo natural. No muestra misericordia hacia los cazadores, taladores o cualquiera que amenace la vida silvestre de Sylveria.
  
  ## Referencias

  ![Centauro1](/Readme%20Files/Arte/Imagen15.jpg)  
  ![Centauro2](/Readme%20Files/Arte/Imagen16.jpg) 
  ## Modelo Final
  ![Sagitario](/Readme%20Files/Arte/Sagitario.png)

  ## Ygdra
  Diosa del bosque.

  ## Referencias

  ![Ygdra1](/Readme%20Files/Arte/Imagen17.jpg)  
  ![Ygdra2](/Readme%20Files/Arte/Imagen18.jpg)  
  ![Ygdra3](/Readme%20Files/Arte/Imagen19.jpg)  

  ## El Magnate
  **Facción**: Industria  
  **Rol**: Líder de la industria / Visionario corporativo  

  ## Descripción Física
  - **Edad**: 55 años  
  - **Altura**: 1.65 m  
  - **Complexión**: Corpulento, de figura redondeada  
  - **Rasgos físicos**: El Magnate es un individuo de tez pálida, con una nariz prominente y un bigote característico. Su cabello, de tonos blancos y grises, está peinado hacia atrás.  
  - **Vestimenta**: Siempre utiliza trajes industriales hechos a medida en tonos oscuros, como gris metálico o negro. Lleva un sombrero de copa, un monóculo y un bastón, del que depende ligeramente al caminar.  

  ## Personalidad
  - **Ambición desmedida**: Movido por el deseo de control absoluto, El Magnate ve la naturaleza solo como un recurso que debe ser aprovechado. No se detendrá ante nada para imponer su visión de progreso.  
  - **Carisma frío**: Aunque es implacable, posee una presencia magnética que atrae a aquellos que buscan poder y éxito. Manipula y convence con facilidad, mostrando gran habilidad para persuadir en sus discursos y propuestas.  
  - **Visionario**: Cree firmemente en el avance de la tecnología y la industrialización como el futuro inevitable. Para él, la eficiencia y el orden son esenciales, y considera que la naturaleza es un obstáculo que debe ser superado.  
  - **Desprecio por la naturaleza**: No siente odio por la naturaleza, sino que la considera irrelevante en su visión de progreso. Para él, los árboles, ríos y animales representan barreras arcaicas. La preocupación de otros hacia la naturaleza le parece una debilidad sentimental.  
  - **Maquinador**: Aunque no tiene problema en aliarse temporalmente con otras facciones, siempre planea traicionarlas cuando ya no le son útiles.  

  ## Historia
  Nacido en una región devastada por la pobreza, El Magnate creció con una profunda desconfianza hacia la naturaleza, viendo en ella una fuerza que necesitaba ser dominada. Con una mente brillante para los negocios y la ingeniería, ascendió rápidamente en el mundo corporativo, acumulando riqueza y poder, y fundando un imperio industrial.

  Cuando descubrió los recursos invaluables de Sylveria, vio en este bosque la última barrera entre él y la dominación total del mundo. Para él, Sylveria no es un hogar de vida sino una mina de riquezas sin explotar, lista para ser transformada en progreso y grandeza bajo su liderazgo. Ha impulsado la construcción de fábricas y minas en los bordes del bosque, poniendo en marcha su plan de industrialización sin piedad.

  ## Motivaciones
  - **Dominar Sylveria**: Su objetivo es transformar Sylveria en una vasta ciudad industrial, reemplazando cada árbol y río con maquinaria, fábricas y recursos bajo su control.  
  - **Progreso tecnológico**: Para El Magnate, la naturaleza es obsoleta y debe ceder su lugar a la modernidad. Sueña con un mundo donde la tecnología domine todos los ámbitos de la vida.  
  - **Control y orden**: Desea imponer un orden rígido y absoluto en Sylveria, optimizando cada recurso y manteniendo todo bajo su dominio. La vida natural debe ser subordinada a sus planes de progreso y grandeza.
  ## Referencias

  ![Humano1](/Readme%20Files/Arte/Imagen20.png)   
  ![Humano2](/Readme%20Files/Arte/Imagen21.png)  
  
  ## Modelo Final
  ![ElMagnate](/Readme%20Files/Arte/ElMagnate.png)  

  ## Fu'ngaloth
  **Facción**: Fungi
  **Rol**:Deidad antigua de los hongos / Maestro del reino micelial.

  ## Descripción Física
  - **Edad**: Incalculable. Existe desde antes de que Sylveria fuera un bosque.
  - **Altura**: 2 m en posición erguida.
  - **Complexión**: Imponente y esquelética.
  - **Rasgos físicos**: Fu'ngaloth es una figura retorcida y majestuosa, con cuatro brazos largos y delgados, cada uno cubierto de pequeñas setas y hongos. De su espalda y cuerpo emergen agujeros que dispersan esporas con cada movimiento. Su cabeza está coronada por una seta colosal. Su piel es de un tono gris verdoso, quebrada y áspera como la corteza de un árbol en descomposición.
  - **Vestimenta**: No lleva ropa tradicional. En su lugar, está cubierto de una armadura natural hecha de hongos. Porta un báculo rústico, hecho de madera marchita, con una terminación en forma retorcida.

  ## Personalidad
  - **Paciencia infinita**: Fu'ngaloth es eterno y no tiene prisa. Todo lo que hace sigue el ritmo lento y constante de la decadencia y la renovación. Es metódico, sabiendo que todo se descompone tarde o temprano.
  - **Sabiduría ancestral**: Su mente está llena de los secretos más antiguos de Sylveria. Habla en enigmas y parábolas, con una voz reverberante que parece surgir de lo profundo de la tierra. Tiene un conocimiento abrumador de los ciclos naturales y cómo corromperlos.
  - **Devoción a la simbiosis**: Para Fu'ngaloth, todo en Sylveria debe rendirse a la simbiosis micelial. Cree que la verdadera forma de vida es la que se integra y conecta en su red fúngica. Lo que no puede ser asimilado, debe perecer.
  - **Desdén por el crecimiento lineal**: Detesta el avance de la industria y la persistente expansión de la naturaleza si no puede moldearla. La vida que no se corrompe o se renueva en su red le resulta antinatural.

  ## Historia
  Desde tiempos inmemoriales, Fu'ngaloth ha existido bajo la superficie de Sylveria, mucho antes de que los árboles milenarios extendieran sus ramas hacia el cielo. Cuando la primera semilla germinó, él ya había comenzado a corromper las raíces, estableciendo un imperio micelial que se extiende por todo el bosque. Adorado como un dios por las criaturas fúngicas, Fu'ngaloth vio a Sylveria como el terreno perfecto para extender su influencia.
  Durante eras, permaneció paciente, permitiendo que su reino creciera en las sombras. Sin embargo, la llegada de la industria ha comenzado a destruir su mundo subterráneo. A su vez, la naturaleza, con sus guardianes protectores, ha tratado de purgar sus hongos en repetidas ocasiones, impidiéndole dominar la superficie. Ahora, el tiempo de esperar ha terminado. Fu'ngaloth ha decidido actuar, usando el antiguo juego de Stratum para garantizar que Sylveria se convierta en un vasto reino micelial, donde todo y todos estén bajo su influencia.

  ## Motivaciones
  - **Corromper Sylveria**: Fu'ngaloth desea extender su red micelial por todo el bosque, transformando cada planta y criatura en parte de su vasto imperio fúngico. Quiere ver el ciclo de la vida convertido en uno de descomposición y renacimiento bajo su control.
  - **Erradicar a la Industria**: Ve la expansión industrial como algo que debe ser destruido. No puede permitir que perjudique a la tierra fértil donde sus hongos prosperan.
  - **Convertir a la Naturaleza**: Para Fu'ngaloth, la naturaleza no debe ser protegida, debe ser transformada. Los árboles deben caer y los animales deben someterse a su red, convirtiéndose en extensiones de su voluntad.

  ## Referencias

  ![Fu'ngaloth1](/Readme%20Files/Arte/Imagen22.jpg)  
  ![Fu'ngaloth2](/Readme%20Files/Arte/Imagen23.png)  
  ![Fu'ngaloth3](/Readme%20Files/Arte/Imagen24.png)  

  ## Modelo Final
  ![Fu'ngaloth](/Readme%20Files/Arte/Fu'ngaloth.png)  

## 4.4. Escenarios y ambientación
En **Stratum**, el entorno de juego se divide en dos planos principales: la mesa de juego física y el ecosistema en el centro de la mesa.

### La mesa de juego
La mesa, que sirve de escenario principal, está diseñada con una decoración estilo Art Nouveau. El jugador verá su propia mano de cartas en primer plano y alrededor podrá observar a los demás personajes que se encuentran en las otras posiciones de la mesa.

-	**Decoración de la mesa**: la mesa está adornada con elementos temáticos que evocan el mundo de **Sylveria**, el bosque legendario donde tiene lugar el conflicto. Los bordes de la mesa pueden estar decorados con grabados de ramas y hojas que representen a la naturaleza, tuberías o engranajes industriales que evoquen a la industria, y hongos que brotan del borde en representación de fungi. La ambientación busca transmitir la sensación de que la mesa es un reflejo físico del conflicto entre las facciones.

-	**Los personajes**: además de ver su propia mano, el jugador puede ver representaciones estilizadas en **low-poly** de los otros personajes (Sagitario, Ygdra, El magnate, Fu’ngaloth) sentados alrededor de la mesa.

-	**Detalles en la habitación**: Más allá de la mesa, el entorno visible puede incluir una habitación decorada con objetos que aluden al lore del juego. 


### El ecosistema
El ecosistema es la manifestación visual de las cartas jugadas en la mesa, cobrando vida en un espacio mágico sobre la superficie de juego. Cada vez que un jugador coloca una carta de población (plantas, herbívoros, carnívoros, fábricas o macrohongos), esta se traduce en una representación tridimensional en el ecosistema.

-	**Visualización del ecosistema**: El ecosistema se expande sobre el centro de la mesa, con cada carta jugada reflejándose en el entorno. Este espacio mágico se desarrolla frente a los ojos del jugador, cambiando de forma constante en función de las jugadas.

-	**Reacción del escenario**: El ecosistema no es estático. A medida que se desequilibra o se estabiliza con nuevas cartas, el ambiente responde: cuando la naturaleza predomina, el entorno se llena de vida, con colores verdes vibrantes, crecimiento de plantas y fauna visible. Si la industria gana terreno, la atmósfera se vuelve más fría y mecánica, con humo y fábricas emergiendo. Si fungi toma el control, el entorno se cubre de hongos, la vegetación se marchita y el escenario adquiere un tono oscuro y decadente.

-	**Interacción visual**: Cuando se coloca una carta en uno de los cinco espacios del jugador, su efecto se proyecta instantáneamente en el ecosistema. Este cambio en el ecosistema es dinámico y afecta a la atmósfera general, añadiendo una capa de interacción visual entre las decisiones de los jugadores y el estado del juego.

## 4.5. El ecosistema
Las animaciones y efectos especiales no solo añaden dinamismo visual al juego, sino que también refuerzan la narrativa y el impacto de las jugadas, haciendo que las interacciones entre los jugadores y el ecosistema sean más inmersivas. Cada jugada cobra vida con animaciones que destacan tanto el acto de colocar cartas como los efectos de las cartas de influencia.

### Colocación de cartas
Cuando un jugador coloca una carta en uno de sus cinco espacios de territorio, el personaje correspondiente realiza una animación para posicionarla en el tablero:

-	**Animación de colocación**: desde la perspectiva en primera persona, el jugador ve la mano del personaje levantarse, tomar una carta de la mano disponible, y colocarla suavemente sobre el espacio seleccionado en la mesa. Simultáneamente, la representación visual de esa carta en el ecosistema (planta, animal, fábrica o hongo) aparece mágicamente en su lugar sobre la mesa.

### Cartas de influencia con animaciones especiales
Varias cartas de influencia tienen efectos visuales únicos que afectan tanto al ecosistema como al escenario general, reflejando el poder de las facciones en el conflicto.

-	**Animación del incendio**: cuando un jugador usa una carta de incendio, se muestra una rápida propagación de fuego a partir del territorio seleccionado. El fuego consume todas las cartas de población y construcciones en esa área, con animaciones de llamas naranjas y rojas que devoran el ecosistema.

-	**Animación de fuegos artificiales**: al activarse, varios cohetes luminosos se disparan hacia el cielo desde el territorio seleccionado, estallando en luces brillantes de diferentes colores. Las criaturas en ese territorio, ya sean herbívoros o carnívoros, se sobresaltan y son movidas a otro espacio vacío en el tablero.

-	**Animación de esporas explosivas**: cuando se juega esta carta, se ve cómo el territorio objetivo es cubierto por una nube densa de esporas púrpuras que se extiende rápidamente por el área, cubriendo a todas las cartas de población en una neblina tóxica. Las cartas afectadas mueren al instante, y la nube de esporas permanece unos momentos, antes de disiparse lentamente, dejando el territorio vacío y sin vida.

### Impacto general en el ecosistema
Cada vez que una carta de influencia es jugada, los cambios en el ecosistema afectan el ambiente visual general. Si el ecosistema es dominado por la naturaleza, el escenario se vuelve más brillante y lleno de vida. Si la industria toma el control, el ambiente se torna más sombrío, con tonos metálicos y nubes de humo. Cuando fungi prevalece, el escenario se oscurece y se cubre de hongos y esporas.
Estas animaciones no solo complementan el aspecto estratégico del juego, sino que también crean una atmósfera envolvente que mantiene al jugador inmerso en el conflicto entre las facciones, reforzando el impacto de cada jugada.

## 4.6. Iconografía y tipografía
La iconografía y tipografía en **Stratum** jugarán un papel crucial en la transmisión clara de información sin romper la inmersión, ya que todo estará integrado en el entorno de manera diegética. No habrá una interfaz convencional en pantalla; en su lugar, los elementos visuales y textuales estarán presentes directamente en los objetos del entorno, asegurando que el jugador reciba la información necesaria sin salir de la experiencia.

### Iconografía
La iconografía y tipografía en **Stratum** jugarán un papel crucial en la transmisión clara de información sin romper la inmersión, ya que todo estará integrado en el entorno de manera diegética. No habrá una interfaz convencional en pantalla; en su lugar, los elementos visuales y textuales estarán presentes directamente en los objetos del entorno, asegurando que el jugador reciba la información necesaria sin salir de la experiencia.

### Tipografía
La tipografía en el juego será simple, mínima y sutil, utilizada únicamente cuando sea estrictamente necesario para transmitir información clave, como nombres de cartas, reglas, o descripciones. Esta información estará integrada en el entorno de juego, siguiendo el concepto de interfaz diegética

# 5. Sonido y Música


## 5.1. Visión General del Sonido


**Estilo y atmósfera:**  
El juego presenta una estética visual art nouveau por lo que la banda sonora busca continuar esta atmósfera. Por ello, se aparecen dos temas diferentes de jazz, uno más calmado para el menú principal y uno más animado para la pantalla de la partida.  

## 5.2. Música
**Estilo de la banda sonora:**  
La banda sonora está inspirada en el jazz de los años 1930s compuesto principalmente para piano.  

**Temas principales:**  
  - **Tema principal:** Se reproducirá durante la partida.  
  - **Tema del menú principal:** Se escuchará en el menú principal y en las pantallas de búsqueda de partida.

**Looping y duración:**  
Todos los temas están diseñados para repetirse en bucle sin interrupciones perceptibles. Las pistas tienen una duración de entre 2 y 4 minutos antes de reiniciarse.

## 5.3. Efectos de Sonido (SFX)
**Sonidos de interacción del jugador:**  
  - Poner cartas de población sobre la mesa: Un sonido correspondiente al tipo  de carta sea este planta, herbívoro o carnívoro.
  - Jugar una carta de influencia: Un sonido con un suave destello de energía y un toque de reverberación.
  - Descartar una carta en la pila de descartes: Sonido similar a quemar un objeto en un fuego.
  - Colocar una construcción (El Magnate): Sonido sólido de madera o piedra ligera.
  - Finalización de turno: Suave campana o susurro de viento.
 
**Sonidos ambientales:**  
  Durante la partida, se escucharán efectos ambientales naturales:
  - Cantos de aves lejanas.
  - Viento meciendo árboles.
  - Insectos y pequeños animales moviéndose en el fondo.
  - Animales caminando.
  
 Estos sonidos ambientales variarán dinámicamente según el estado de la simulación del ecosistema y las cartas jugadas. 


# 6. Modelo de negocio y monetización
## 6.1. Información sobre el usuario

El juego está dirigido a jugadores de +13 años, que pueden ser tanto casuales como veteranos aficionados a los juegos competitivos de mesa y cartas. Es accesible incluso para aquellos usuarios que no cuenten con equipos potentes, ya que el juego está disponible incluso para dispositivos móviles. El juego sigue un modelo freemium: la versión completa es gratuita, pero sin acceso a matchmaking. Los jugadores podrán disfrutar de partidas privadas con amigos. Para acceder al Matchmaking Competitivo, obtener recompensas y participar en clasificaciones, deberán pagar una suscripción mensual.


## 6.2. Mapa de empatía

![Mapa de empatía](/Readme%20Files/Empathy_Map_Canvas.png)

## 6.3. Caja de herramientas
En este documento, se presenta una "caja de herramientas" que examina seis bloques principales de stakeholders, detallando sus responsabilidades y cómo interactúan entre sí para fortalecer la escena competitiva. Cada grupo contribuye a su manera a la evolución del juego, desde la creación de contenido y la organización de eventos hasta la promoción y financiamiento.
Todos ellos con un **objetivo común: mantener viva y activa la comunidad, asegurar un entorno competitivo atractivo y garantizar la viabilidad del negocio.**

### Siete bloques principales (stakeholders):
#### 1. Jugadores y comunidad de fans (clientes y usuarios finales):
Este bloque representa a los usuarios del juego, quienes no solo participan activamente en las partidas competitivas, sino que también son una comunidad que crea y consume contenido alrededor del juego (streams, vídeos, foros, etc.). Estos jugadores buscan mejorar sus habilidades, ganar torneos, obtener reconocimiento, y también contribuyen al crecimiento del juego al compartir sus experiencias, estrategias y generar discusiones.

Su rol va más allá del juego en sí: son embajadores del mismo, promoviendo el juego competitivo en redes sociales, organizando partidas informales, y contribuyendo al ambiente competitivo y colaborativo que mantiene viva la comunidad. Además, pueden influir en las tendencias de las estrategias y en la evolución del juego a través de su participación activa y feedback.

#### 2. Organizadores de torneos presenciales con el juego en físico (facilitadores de competencia):
Los responsables de organizar y gestionar los torneos a diferentes niveles (locales, nacionales, internacionales). Garantizan que las reglas sean justas, el ambiente sea competitivo, y los premios atractivos.

#### 3. Desarrolladores y diseñadores del juego (productores):
Son quienes crean y mantienen el juego competitivo, ajustando las mecánicas, balanceando las cartas y lanzando expansiones para mantener el interés del juego.

#### 4. Distribuidores y tiendas (canales de distribución):
Los encargados de la venta y distribución del juego de cartas y sus actualizaciones, ya sea de forma física en tiendas o en línea. También pueden ofrecer productos relacionados con los torneos (entradas, merchandising, las cartas en físico…).

#### 5. Sponsors e inversores (financiadores):
Empresas o marcas que patrocinan torneos y eventos competitivos, ofreciendo recursos para premios y financiando la organización. Buscan visibilidad y retorno en la comunidad de jugadores.

#### 6. Marketing y comunicación (mediadores):
Los encargados de hacer llegar el juego al público objetivo, a través de estrategias de branding, redes sociales, eventos de lanzamiento, campañas publicitarias y colaboración con influencers de juegos de mesa y rol.

#### 7. Unity:
La empresa paga a Unity por el uso de sus servicios de Unity Cloud, incluyendo Unity Relay y Unity Matchmaking, para alojar los servidores y gestionar las partidas en línea. A cambio, Unity proporciona la infraestructura necesaria para el hosting, conexión entre jugadores y organización de partidas multijugador. Además, la empresa hace uso del motor de juego para el desarrollo del videojuego.


### Relaciones entre los bloques:
#### Jugadores y comunidad - Torneos:
Los jugadores participan en los torneos organizados de forma presencial, aportan la cuota de inscripción y reciben premios a cambio.

Además, proveen feedback y opiniones sobre la experiencia en torneos, que los organizadores pueden usar para ajustar sus eventos.

#### Jugadores y comunidad - Empresa:
Los jugadores proporcionan retroalimentación valiosa sobre la mecánica del juego, sugiriendo mejoras y ajustes para equilibrar las cartas y otros elementos. Además, pueden participar en pruebas de nuevas actualizaciones.

A cambio, la empresa (desarrolladores y diseñadores) les ofrece un producto de calidad, el videojuego, junto con actualizaciones constantes que se ajustan a las necesidades de la comunidad. Además, crean contenido dirigido a atraer a jugadores competitivos, quienes, si desean participar en partidas avanzadas, pagarán una suscripción mensual.

Por su parte, la comunidad genera contenido (streams, guías, videos) que incrementa la popularidad del juego y lo mantiene activo.

#### Jugadores y comunidad - Marketing:
El equipo de marketing desarrolla campañas publicitarias dirigidas a atraer nuevos jugadores y mantener activa la comunidad existente. Para maximizar el alcance y el impacto de estas campañas, colaboran con influencers dentro de la comunidad, quienes generan una mayor visibilidad del juego.

#### Torneos - Empresa:
La empresa y los organizadores de torneos colaboran para asegurar que las reglas y las cartas estén debidamente equilibradas para las competiciones. Los torneos, a su vez, proporcionan feedback a los desarrolladores sobre el comportamiento de las mecánicas del juego en un entorno competitivo.

En respuesta, la empresa implementa ajustes en el juego, introduciendo cambios en el metajuego y variando las cartas más jugadas, con el fin de mantener un entorno competitivo dinámico y equilibrado.

#### Torneos - Sponsors e inversores:
Los organizadores buscan sponsors para financiar los torneos, obteniendo apoyo económico para premios, logística y marketing. Los sponsors buscan visibilidad y conexión con la audiencia a través de estos eventos.

#### Marketing - Torneos:
Promocionan torneos y eventos organizados, asegurándose de captar la atención de los  jugadores y así aumentar el número de participantes.

#### Distribuidores y tiendas - Empresa:
La empresa paga a estas tiendas para que realicen los productos que quieren y a cambio, esas tiendas producen esos productos y los distribuyen (merch).

#### Empresa - Sponsors e inversores:
Los inversores pueden financiar el desarrollo y actualizaciones del juego, eventos y otras actividades relacionadas con el crecimiento del juego  a cambio de beneficios financieros.

#### Empresa - Marketing:
La empresa trabaja con el equipo de marketing para lanzar campañas promocionales del juego, novedades y eventos en torno al juego.

#### Distribuidores y tiendas - Torneos:
Los organizadores y distribuidores colaboran en la promoción de los torneos. Las tiendas pueden vender entradas o productos promocionales relacionados con los eventos.

#### Distribuidores y tiendas - Marketing:
Colaboran en la creación de campañas para incrementar el número de ventas y dar mayor visibilidad al juego.

#### Sponsors e inversores - Marketing:
Los sponsors también colaboran con el equipo de marketing para asegurarse de tener la visibilidad adecuada en todas las campañas de marketing.

#### Empresa - Unity:
La empresa paga por los servicios en la nube de Unity (Unity cloud, relay y matchmaking), garantizando la infraestructura y soporte necesarios para el juego en línea.
Unity proporciona el motor de juego gratuito y servicios de infraestructura que facilitan el hosting y el emparejamiento de jugadores.

### Esquema
![Caja de Herramientas](/Readme%20Files/Caja_de_Herramientas.png)

### Leyenda

![Leyenda Caja de Herramientas](/Readme%20Files/Leyenda_caja_herramientas.png)

### Resumen
Este modelo de negocio captura la naturaleza competitiva de un juego de cartas con torneos, destacando la importancia de la comunidad de jugadores, los eventos y las interacciones entre los diferentes stakeholders.


## 6.4. Modelo de canvas

![Modelo de canvas](/Readme%20Files/Business_Model_Canvas.png)

## 6.5. Monetización
### Modelo de monetización principal

El juego seguirá un modelo **free-to-play (F2P)** con una monetización basada en suscripción. El acceso a la versión gratuita ofrecerá un nivel limitado del juego, mientras que los jugadores que opten por la **suscripción mensual** tendrán acceso completo a las funciones competitivas del juego.

### 1. Versión gratuita (F2P)
Los jugadores podrán descargar y jugar el juego sin costo, pero tendrán acceso solo a un conjunto limitado de características, lo cual incluye:

#### Partidas amistosas (solo con amigos)
- Los jugadores podrán crear partidas privadas en las que invitarán a sus amigos utilizando un código de sesión generado al crear una sala. 
- No tendrán acceso al matchmaking automatizado ni a las modalidades competitivas.

#### Acceso a torneos oficiales
- Los jugadores podrán participar en torneos presenciales, donde podrán obtener **recompensas** y ganar prestigio en la comunidad.

#### Limitaciones:
- **Sin acceso a matchmaking competitivo**: Solo podrán jugar en sesiones privadas con amigos.
- **Sin recompensas competitivas**: No participarán en el sistema de recompensas de temporada o torneos.

### 2. Suscripción mensual (modelo competitivo)
Los jugadores que opten por la **suscripción mensual** desbloquearán una serie de funciones orientadas a la **experiencia competitiva**, diseñada para los jugadores que buscan una mayor inmersión y el acceso al sistema de recompensas.

#### Acceso al matchmaking competitivo:
- Los suscriptores podrán participar en partidas rankeadas a través del matchmaking competitivo, enfrentándose contra jugadores de su mismo nivel.
- Este matchmaking estará basado en un **sistema de MMR** (matchmaking rating), que ajustará los oponentes según su nivel de habilidad.

#### Recompensas y progresión:
- **Sistema de clasificación (ranking)**: Los jugadores suscriptores podrán subir en el sistema de clasificación global, compitiendo por una mejor posición en las tablas de clasificación (leaderboards).
- **Recompensas de temporada**: Al final de cada temporada competitiva (3 meses de duración), se otorgarán recompensas físicas por rango.
- **Estadísticas del modo competitivo**: Tendrán acceso a un **panel de estadísticas** de sus partidas competitivas, que incluirán datos como el porcentaje de victorias por tipo de mazo, entre otras cosas.

### 3. Desarrollo continuo del juego y eventos especiales
El juego incluirá actualizaciones frecuentes tanto para jugadores F2P como suscriptores:

#### Actualización de contenido:
- Se lanzarán regularmente **parches** que mantendrán fresco el entorno competitivo.
- Estos cambios para balancear las cartas estarán disponibles para todos los jugadores.

### 4. Ajustes importantes y éticos en la monetización
El modelo de monetización de este juego está diseñado para ser **justo** y **no invasivo**, evitando los sistemas de "pagar para ganar" (pay-to-win) y asegurando que todos los jugadores, independientemente de si pagan o no, tengan acceso a las mismas cartas y mecánicas del juego.

#### Sin ventaja competitiva pagada:
- Todas las cartas y mecánicas estarán disponibles tanto para jugadores gratuitos como para suscriptores, asegurando que **la habilidad sea lo único que determine el éxito** en el juego.
- La suscripción solo ofrecerá acceso al entorno competitivo y a las características de progreso vinculadas a ese modo.

#### Transparencia en la oferta:
- El sistema de suscripción será transparente en cuanto a los beneficios ofrecidos, dejando claro a los jugadores qué funciones están pagando y garantizando una experiencia justa para los jugadores F2P.

### Conclusión

Este modelo de monetización ofrece a los jugadores la posibilidad de disfrutar de todas las cartas y mecánicas del juego sin necesidad de gastar dinero, mientras que aquellos que busquen una experiencia más competitiva y progresiva pueden optar por una suscripción mensual. Esto no solo evita las controversias relacionadas con modelos "pay-to-win", sino que también asegura una experiencia equilibrada y justa para toda la base de jugadores.

