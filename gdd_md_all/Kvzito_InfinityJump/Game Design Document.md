# InfinityDrive 



#### _Participantes_
Creado por el estudio Silver Way

- Santiago Cordova Molina
- Maria Rivera Gutierrez
- Kevin Javier Esquivel Villafuerte

  
###### **Aviso de derechos de autor/Información del autor**

## _Game Design Document_

## _Índice_

---

1. [Índice](#índice)
2. [Diseño del juego](#diseño-del-juego)
    1. [Resumen](#resumen)
    2. [Juego](#juego)
    4. [Mentalidad](#mentalidad)
3. [Técnico](#técnico)
    1. [Pantallas](#pantallas)
    2. [Controles](#controles)
    3. [Mecánicas](#mecánicas)
2. [Diseño de niveles](#diseño-de-niveles)
    1. [Tema](#tema)
        1. Ambiente
        2. Objetos
            1. Ambiente
            2. Interactivo
        3. Desafíos
    2. [Flujo de juego](#flujo-de-juego)
3. [Desarrollo](#desarrollo)
    1. [Clases abstractas](#clases-abstractas)
    2. [Clases derivadas](#clases-derivadas)
4. [Gráficos](#gráficos)
5. [Sonidos y Música](#sonidos-y-música)
    1. [Atributos de estilo](#atributos-de-estilo)
    2. [Sonidos Necesarios](#sonidos-necesarios)
    3. [Música Necesaria](#música-necesaria)
6. [Itinerario](#itinerario)

## _Diseño del Juego_

---

### **Resumen**

Los jugadores controlan un coche que debe navegar a través de mapas dinámicos e ilustrados, superando obstáculos y recogiendo monedas para mejorar su vehículo y alcanzar la meta. Con cada desafío, deben adaptarse, optimizar su carro y perfeccionar sus habilidades para progresar más. 

### **Juego**

El objetivo del juego es conducir durante el mayor tiempo posible, cubriendo la mayor distancia posible, evitando con habilidad los obstáculos a lo largo del camino. A medida que los jugadores progresan, el entorno cambia, introduciendo nuevos desafíos que requieren un pensamiento rápido y un control preciso. Dado que el juego tiene lugar en una ciudad con un estilo de arte ilustrado, los obstáculos incluirán baches, puentes y plataformas que el jugador debe navegar. El coche se controla mediante las teclas de flecha, lo que requiere que el jugador controle cuidadosamente la velocidad-ralentización para evitar peligros o acelerar para despejar los huecos y maximizar la distancia. La toma de decisiones estratégicas es crucial, ya que los jugadores deben analizar los mejores caminos para tomar mientras recogen monedas. Estas monedas se pueden usar para comprar mejoras, ya sea aumentos temporales o mejoras permanentes, para mejorar el rendimiento del carro y aumentar sus posibilidades de lograr una puntuación más alta. 

### **Mentalidad**

El juego está diseñado para desafiar y involucrar a los jugadores, fomentando una mentalidad de adaptación, estrategia y mejora continua. Los mapas dinámicos e ilustrados, junto con la dificultad cada vez mayor, crean una sensación de emoción y logro. Los jugadores se sentirán motivados para perfeccionar sus habilidades y superar sus límites a medida que progresan. Al manejar cuidadosamente la velocidad, navegar por los obstáculos y hacer un uso estratégico de las mejoras, experimentarán un equilibrio entre el riesgo y la recompensa. Este enfoque fomenta un sentido de aventura y determinación, manteniendo a los jugadores comprometidos y ansiosos por mejorar con cada intento.

## _Técnico_

---

### **Pantallas**

1. Pantalla de título
2. Selección de inicio de juego
    1. Pantalla de tienda
    2. Pantalla de inventario
4. Pantalla de juego
    1. Fondo Principal
    2. Obstaulos
    3. Pantalla de meta
5. Créditos finales

_(ejemplo)_

### **Controles**

- La flecha derecha hará que el coche avance y si la dejas presionada el coche empezará a acelerar.
- La flecha izquierda hará que el coche frene si está en movimiento y que vaya para atrás si se deja presionado.
- Con la flecha de arriba el coche podrá hacer un pequeño salto. Este salto será disponible solo al adquirir la mejora de salto.
- Con la barra espaciadora el jugador podrá hacer un turbo que dura 1 segundo y hace que el coche sea mas veloz. Esta mejora está disponible en la tienda.
- Con la tecla esc el jugador salirse de las diferentes pantallas y regresar a la anterior
- Presionando la tecla “T” el jugador entrara a la tienda
- Con la tecla “P” el jugador podrá poner el juego en pausa.

### **Mecánicas**

EL juego se basa en un carro que debe superar diversos obstáculos mientras controla su velocidad. La mecánica más compleja de implmentar es el sisite de aceleración y frenado.

Cuando el jugador mantiene presionada la tecla de la flecha derecha, el carro incrementa su velocidad progresivamente. Esto permite completar el nivel en menos tiempo y facilita el cruce de ciertos obstáculos que requieren impulso. Sin embargo, al presionar la tecla de la flecha izquierda, se aplicará una fuerza de fricción que reducirá la velocidad del vehículo o permitirá detenerlo por completo.

Para lograr esta mecánica, utilizaremos principios de física dentro del algoritmo del juego, específicamente:

- **Aceleración:** Se implementará un sistema donde la velocidad del carro aumente progresivamente al mantener la tecla de avance presionada, con un límite máximo establecido.
- **Desaceleración y frenado:** Se simulará la pérdida de velocidad cuando el jugador deja de acelerar o presiona la tecla de frenado. Se calculará la fricción entre las ruedas y la superficie del camino.
- **Impacto con obstáculos:** Si el carro choca con un obstáculo, su velocidad disminuirá bruscamente o se detendrá dependiendo del tipo de colisión.
- **Física de salto y caída:** Algunos obstáculos pueden requerir que el carro tome impulso para cruzar plataformas o esquivar huecos. La velocidad influirá en la distancia que el vehículo pueda recorrer en el aire.

Cada una de estas interacciones estará integrada en el algoritmo del juego, activándose en respuesta a las acciones del jugador. Además, si el jugador no logra superar un obstáculo y pierde la partida, se reiniciará la simulación con nuevas variables para mantener la rejugabilidad.

## _Diseño de Niveles_

---

### **Tema**

1. Cuidad
    1. Estado
        1. Divertido, atento, movido, activo
    2. Objetos
        1. _Ambiente_
            1. Calle
            2. Edificios
            3. Sol
            4. Ventanas con luces
            5. Fondo cuadrado
        2. _Interactivo_
            1. Puentes
            2. Baches
            3. Fuego
            4. Plataformas
            5. Subidas
            6. Bajadas
            7. Curvas

### **Flujo de Juego**

1. El jugador empieza a la izquierda de la pantalla.
2. Debe avanzar hacia el frente, comenzando con poca velocidad.
3. Mientras más tiempo mantenga presionada la tecla de avance, más rápido avanzará el carro.
4. Al encontrarse con un bache, deberá reducir su velocidad para evitar perder el control.
5. Si encuentra una curva, necesitará la velocidad adecuada para girar sin problemas.
6. Si se encuentra con una plataforma, deberá avanzar con paciencia y controlar bien el carro para superarla.
7. Si hay una pendiente, ya sea de subida o bajada, deberá ajustarse a la velocidad correcta para no perder el equilibrio ni dañar el vehículo.
8. Después de superar cierto número de obstáculos, llegará a una bandera que indica que el nivel ha sido completado.
9. El siguiente nivel tendrá obstáculos más difíciles.
10. Este proceso se repetirá hasta que el jugador pierda al no lograr superar un obstáculo.

## _Desarrollo_

---

### **Clases abstractas**

1. JugadorBase
2. ObstaculoBase
3. ObjetoBase
4. MejoraBase


### **Clases derivadas**

1. JugadorBase
    1. JugadorPrincipal
    2. JugadorModificable
2. ObstaculoBase
    1. Bache
    2. Fuego
    3. Puente
    4. Caracol
    5. Rampa
    6. Elevacion
3. ObjetoBase
    1. Moneda
    2. Piso
    3. Fondo
    4. Meta
4. MejoraBase
    1. Parachoques
    2. LlantasResistentes
    3. Nitro



## _Gráficos_

---

Para este juego vamos a usar un estilo de caricatura, para ser más específico sería un estilo como si un niño lo hubiera dibujado. Este estilo se podrá ver alrededor de todo el juego, tanto en el coche, en los obstáculos, como en los menús. Esto con la finalidad de hacer que el juego se sienta amigable desde la primera vez que lo juegas. 

Los colores que usaremos en el juego serán simples para mantener ese estilo visual que mencionamos anteriormente. El coche comenzará con un color rojo el cual podrás cambiar en la tienda por costo de monedas. Los obstáculos seran creados todos de color negro a menos que tengan partes que lo necesiten, por ejemplo si un obstaculo tiene fuego este si sera de los colores del fuego. 

Queremos hacer un nivel de tutorial el cual funcione como herramienta para que el jugador pueda aprender las mecánicas de los controles y del juego en general. Además de esto cada vez que un jugador termine un nivel y regrese a la pantalla de inicio de juego le pondremos un recordatorio de que puede entrar a la tienda a gastar su dinero en mejoras temporales o permanentes. Antes de comprarla se verá una pequeña descripción de qué es lo que hace dicha mejora.


Diseños: 

1. Coches
    1. Coche color rojo principal
     ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalCoche.PNG)
    2. Coche color verde
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalVerde.PNG)
    3. Coche color azul
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalAzul.PNG)

    4. Coche color morado
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalMorado.PNG)

    5. Coche color amarillo
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalAmarillo.PNG)

    6. Coche color naranja
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ModeloPrincipalNaranja.PNG)

2. Obstaculos
    1. Línea recta: Este obstáculo no tiene ninguna dificultad y solo es una línea recta
       
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoLinea.jpg)

    2. Triángulo: Este obstáculo empieza con una línea recta y después de convierte en un triángulo en el que el coche tiene que subir y bajar con cuidado
       
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoTriangulo.jpg)

    3. Caida:  En este obstáculo el coche debe frenar para no caer de manera agresiva y estropearse, el coche tendrá que bajar y subir el obstáculo.
       
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoCaida.jpg)

    4. Rampa: El coche deberá subir la rampa con buena velocidad para que la pueda saltar eficazmente, de otra manera el coche puede que se voltee.
       
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoRampa.jpg)

    5. Baches: El coche tendrá que bajar la velocidad al llegar para que las llantas no se le pongan. Este obstáculo se puede evitar con la mejora de resistencia de la llanta.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoBache.jpg)

    6. Loop: El coche tendrá que tener una velocidad constante para que pueda subirse al loop y dar una vuelta completa sin que el coche se caiga.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoLoop.jpg)

    7. Montaña: En este obstáculo el coche tiene que subir por una rampa, pasar por una línea y luego bajar por una rampa.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoMonta%C3%B1a.jpg)

    8. Plataforma  Movediza: En este obstáculo las dos líneas que están en medio se irán moviendo de arriba a abajo y el coche tiene que calcular el momento exacto para avanzar y no caer.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoPlataformasMovedizas.jpg)

    9. Puente Movedizo: Las dos líneas que están verticales se moverán para formar una línea. Cuando llegue este punto el coche deberá avanzar antes de que se vuelvan a levantar.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoPuenteMovediso.jpg)

    10. Bola: Esta bola se estará moviendo en un péndulo y el jugador tiene que calcular en qué momento avanzar para que la bola no golpee el coche.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoBola.jpg)

    11. Caída en contacto: En el momento que el coche toque una de las líneas rojas, estas empezaran a caer obligando al jugador a no frenar.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoCaidaEnContacto.jpg)

    12. Fuego: Este obstáculo tiene 4 plataformas pequeñas que avientan fuego para arriba. Estas están sincronizadas en números pares y nones (Cuando las nones están prendidas las partes no). El jugador tiene que esperar el momento adecuado para avanzar y que no se queme su coche.
        
    ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/ObstaculoFuego.jpg)


3. Fondos
    1. Fondo de edificios:
       ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/FondoJuego.png)

4. Mejoras
    1. Permanentes:
         1. Turbo
            
            ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/TurboMejora.JPG)
    2. Temporales
         1. Escudo
            
            ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/EscudoMejora.JPG)
            
         2. Monedas Dobles
            
            ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/MonedasMejora.JPG)
            
         3. Llantas resistentes
            
            ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/LlantaMejora.JPG)

5. Icono del  juego
   
   ![](https://github.com/Kvzito/InfinityDrivee/blob/main/Videojuegos/Imagenes/IconoJuego.png)




## _Sonidos y Música_

---

### **Atributos de estilo**

La música del juego será alegre y enérgica, manteniendo un ritmo constante que haga que la experiencia de conducción se sienta dinámica y divertida. Queremos que los jugadores disfruten el recorrido como si estuvieran manejando en una ciudad animada.

El juego contará con un solo track musical que se reproducirá en bucle durante la partida. Este tema será movido y entretenido, con instrumentos como sintetizadores, percusión rítmica y melodías pegajosas para mantener la emoción sin volverse repetitivo.

Para los efectos de sonido, buscamos que sean claros y funcionales, proporcionando retroalimentación sin saturar la experiencia auditiva. Queremos que cada sonido ayude al jugador a reaccionar a lo que sucede en la pantalla sin distraerlo.

### **Sonidos Necesarios**

1. Efectos
    1. Fuego
    2. Estruendo (al chocar con un objeto)
    3. Motor (cuando haces una mejora de valocidad)
    4. Freno (cuando se desacelera el carro)
2. Feedback
    1. Tinteo (al agarrar una moneda)
    2. Start (cuando empieza un nivel)
    3. Aplauso (cuando acabas el nivel)

### **Música Necesaria**

El juego tendrá un único track musical en bucle, diseñado para complementar la acción sin volverse monótono. Este track será:

1. Alegre y rítmico, reflejando la sensación de velocidad y dinamismo.
2. Divertido y enérgico, con un tempo constante que mantenga la emoción.
3. Lo suficientemente neutro para no cansar al jugador en sesiones largas.


## _Itinerario_

---

1. Determinar el concepto general del juego (primeras 3 semanas)
    1. Mecánicas
        1. compra de habilidades
        2. aleatoriedad de mapas
        3. movimiento
  2. Reglas
        1. Gestión de habilidades
        2. Requerimientos de 
2. Desarrollo de documentación/issues del proyecto (semana 4)
    1. Historias de usuario
    2. Casos de uso
    3. Issues
4. Primer sprint (semana 5)
    1. Inicialización base de datos
    2. Assets del videojuego 
5. Segundo sprint (semana 6)
    1. Programación de clases abstractas del juego
        1. Habilidades
        2. Jugador
        3. Obstáculos
        4. Entorno
6. Tercer sprint (semana 7)
    1. Desarrollo de clases derivadas
    2. Desarrollo de web
7. Cuarto sprint (semana 8)
    1. Conexión de web con base de datos y videojuego
    2. Sprites y visuales
8. Quinto sprint (semana 9)
    1. Terminar visuales y audio
    2. Web completamente terminada y funcional
9. Semana 10
    1. Presentación final del videojuego
