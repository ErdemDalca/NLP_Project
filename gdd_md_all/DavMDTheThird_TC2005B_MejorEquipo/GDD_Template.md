# **Darkest Times**

## _Game Design Document_

---

##### **Copyright notice / author information / boring legal stuff nobody likes**

David Medina Domínguez A01783155

Juan Pablo Cruz Rodriguez A01783208

Angel Adrian Afonso Castellanos A01782545

Daniel Soult Gómez A01782985



## _Index_

---

- [**Darkest Times**](#darkest-times)
  - [_Game Design Document_](#game-design-document)
        - [**Copyright notice / author information / boring legal stuff nobody likes**](#copyright-notice--author-information--boring-legal-stuff-nobody-likes)
  - [_Index_](#index)
  - [_Game Design_](#game-design)
    - [**Summary**](#summary)
        - [***Narrativa***](#narrativa)
      - [***Historia y Dialogos***](#historia-y-dialogos)
      - [***Personajes***](#personajes)
      - [***Generos***](#generos)
        - [**Subgeneros**](#subgeneros)
    - [**Gameplay**](#gameplay)
    - [**Obstaculos**](#obstaculos)
    - [**Estrategia**](#estrategia)
    - [**Mindset**](#mindset)
  - [_Technical_](#technical)
    - [**Screens**](#screens)
    - [**Controls**](#controls)
    - [**Mechanics**](#mechanics)
  - [_Level Design_](#level-design)
    - [**Themes**](#themes)
    - [**Game Flow**](#game-flow)
  - [_Development_](#development)
    - [**Abstract Classes / Components**](#abstract-classes--components)
    - [**Derived Classes / Component Compositions**](#derived-classes--component-compositions)
  - [_Graphics_](#graphics)
    - [**Style Attributes**](#style-attributes)
    - [**Graphics Needed**](#graphics-needed)
  - [_Sounds/Music_](#soundsmusic)
    - [**Style Attributes**](#style-attributes-1)
    - [**Sounds Needed**](#sounds-needed)
  - [_Schedule_](#schedule)

## _Game Design_

---

### **Summary**

##### ***Narrativa***

Eres ______ saliendo de tu trabajo en SCP Inc (Safe Control Places "Guiño a Special Contaiment Procedures"). De camino a la salida comienzas a sentir un ambiente inquietante y tenso. Comienzas a tambalearte, tienes nauseas y vas perdiendo tu consiencia. Luego, ves una puerta al final de un pasillo largo; decides atravesar la puerta de manera apresurada.

 No era lo que esperabas, ya que te encuentras en un es un espacio expansivo no euclidiano, que se asemeja a las habitaciones traseras de una tienda minorista. Todas las habitaciones en el Nivel 0 comparten las mismas características superficiales, como el papel tapiz monoamarillo gastado, la alfombra vieja y húmeda, los enchufes eléctricos dispersos y la iluminación fluorescente colocada de manera inconsistente. 

Preocupado y asustado empizas a buscar una salida, pero es en vano, ya que el espacio liminal en el que te encuentra es infinito. Sin embargo no todo es desesperacion, ya que encuntras una sala enorme con mas personas y tres puertas (dos puertas niveles y una puerta boss.). La sala esta marcada con el logo de tu empresa y encuentras varias notas de compañeros pasados que supuestamente habian despedido.

"Que esta ocurriendo"?
"Donde estoy"?
"Como salgo"?
Son las preguntas que te invaden la cabeza. Conforme avanzas en los diferentes escenarios, te vas dando cuenta del verdadero proposito de tu empresa SPC.

![Fotografia de una idea de los backrooms](https://i0.wp.com/culturacolectiva.com/wp-content/uploads/2023/02/PH644P4BUNDQHOYWTQAS5ASZFY.jpg?w=1024&ssl=1)

####  ***Historia y Dialogos***

1. Escenario 1(Epilogo) "Welcome to the #H$3@1?L#": 
   
**-Al fin acabé con mi turno. (Expresa cansancio).**

De pronto suena una radio que emite un mensaje únicamente para miembros de la empresa SCP (Safe Control Places: Empresa encargada de reducir accidentes de trabajo como una de seguridad industrial).

**-A todos los trabajadores, por favor, regresar inmediatamente a su casa debido a una falla en el sistema. Deberán volver hasta nuevo aviso.**

**-No otra vez. Ya es la cuarta falla en este mes.**

**-Debo volver lo antes posible. Mi capibara (Zack) me está esperando. Debe estar hambriento y preocupado.**

El jugador sale del cuarto principal y se dirige hacia la salida. Conforme el jugador avanza, el ambiente del lugar irá cambiando a la forma de un laberinto. Cada vez que se acerque a la puerta correcta, la atmósfera lo hará entrar en pánico (Los caminos tendrán un diseño glitcheado y tétrico).

**-Vaya, no me acordaba de que este lugar tuviera tantos pasillos.
¿Desde cuándo las paredes son de color _____? Algo anda mal. (Se muestra preocupado).**

Más adelante se encuentra con un cartel de publicidad de su compañía.

**-SCP (Safe Control Places): La mejor decisión de tu vida. Desde que entré a esta empresa, no he vuelto a sonreír.**

Luego encuentra otro cartel que indica que están reclutando personal.

**-SCP te necesita. Llámanos ya. No entiendo por qué siguen reclutando a nuevo personal si ellos son los responsables de despedir a casi 10 trabajadores por mes.**

**-Pero, ¿qué...? ¿Dónde está la salida? (Se encuentra asustado y enojado).**

El jugador se acerca al pasillo final, la música se apaga, la iluminación comienza a titilar y varios jumpscare aparecen para darle tensión al ambiente.

**-¿Qué está sucediendo? (Se encuentra asustado).**

Al frente aparece una persona sin cara, pero luego desaparece.

**-¿Quién está ahí? (Se encuentra enojado, asustado y lo dice en tono agresivo).**

**-¿Quienquiera que esté haciendo esto, para de una maldita vez.**

De pronto, la persona sin cara aparece detrás del jugador y comienza a perseguirlo mientras se escucha una música de fondo de miedo.

**-¡Alto, alto, aléjate de mí! ¡No des un paso más! ¡ALTO!**

**-¡Ah! (De asombro y alivio). Ahí está la salida.**

El jugador llega a la salida que lo llevará al siguiente escenario.

**Cierre del nivel**

**Dialogos de Interaccion**

- Creo que esta cerrada.
- Esta no es la salida.

2. Escenario 2(Lobby) "Welcome to the Back1200|\/|$":
   
EL personaje se encuentra desconsertado en el lobby por lo que comienza a explorar sus alrededores. Se da cuenta que hay 3 lugares: un bosque, un hospital y una especie de puerta de salida.

A lo lejos divisa a 5 personajes (NPC).

A lo lejos divisa una tienda.

El jugador escogera entre cuatro personajes principales con una historia y stats diferentes.

1. Samurai - David
2. Futbolista - Angel
3. Arqueologo Juanpa
4. Vikingo - Daniel

**Poner 4 historias**

- 1. Nota: No se cuanto tiempo llevo en este lugar dias,meses o incluso años ya perdi la cuenta. Lo unico de que me acuerdo es de haber visto a alguien parecido a mi pero sin cara.

- 2. Nota: Siento que estos lugares no tienen salida como si alguna manera fueran infinitos. Debo de conseguir las llaves para abrir la puerta.

- 3. Nota: Ya no puedo soportarlo mas, quiero que esto acabe pronto. Ya se , si agarro el arma que vi en el bosque , tal vez pueda .....

- 4. Nota: AHHHHHHHHHHHHHHHH, quiero borrar esas imagenes de mi mente, nunca habia visto algo asi. Quiero volver a mi casa mi familia me esta esperando PORFAVOR.

- 5. Nota: He encontrado una serie de símbolos extraños en las paredes de este laberinto interminable. Parecen formar un patrón, pero no logro descifrar su significado. Cada vez que los miro, siento una extraña sensación de inquietud.

- 6. Nota: Escucho voces susurrantes en los pasillos, pero nunca puedo encontrar a nadie. Las palabras son incomprensibles, pero me llenan de miedo y paranoia. No sé si son reales o simplemente producto de mi mente deteriorada.

- 7. Nota: Me encontre unos cuerpos en un hospital con un uniforme que parecia tener el logo de mi empresa. Creo que SCP es una fachada para algo mas oscuro.

- 8.  Nota: Los sonidos en este lugar son ensordecedores y discordantes. Gritos desgarradores, risas macabras y susurros inquietantes llenan el aire. Parece que el laberinto está vivo con el sonido de la locura y el tormento.

- 9. Hay una presencia siniestra que acecha en las sombras. Puedo sentir sus ojos fijos en mí, observándome constantemente. Cada vez que intento escapar, su presencia se intensifica, recordándome que no estoy solo en este laberinto oscuro.

- 10. Cada vez que cierro los ojos, me encuentro en un recuerdo del pasado. Son fragmentos de mi vida que se repiten una y otra vez. No importa cuánto intente evitarlos, siempre regreso a esos momentos dolorosos. Estoy atrapado en mis propios recuerdos.

3. Hospital: 

**Que es este lugar? No veo nada!!**

El jugador aparece en el lobby de hospital y se encunetra confundido y asustado.

**mmm parece un hopital.**

**Deberia revisar las habitaciones para encontrar la llave de la salida.**

El jugador explora a sus alrededores y se encuentra con diferentes enemigos y armas.

**Este hospital le pertenece a esa compañia SCP.**

**Al parecer realizaban experimentos con humanos. De seguro son los causantes de que desapareciera.**

**Bitacora#56: Los experimentos se salieron de control no se si pueda esconderme por mucho mas tiempo.**

**Bitacora#30: Creo que encontre una debilidad y es cualquier fuente de luz. Sin embargo, ya casi me quedo sin baterias.**

**Bitacora#1: El sujeto no aguanto el procedimiento comenzaremos con la limpieza.**

**Anuncio SCP: Recordemos que debemos asegurar, contener y protejer.**

**Proyecto DT: El proyecto desea abrir portales a diferentes partes y epocas. Comenzar a probar con distintos sujetos de prueba....**

**Creo que ya estoy cerca de la salida, pero que es ese ruido?**
El jugador llega a la entrada del siguiente piso y encuentra un subboss final.

#### ***Personajes***

Cada personaje interpretara un jugador relacionado al temas de los backrooms y spc: 

1.David->Hacker

    Stats:
    1.Hp: 8
    2.Lck: 85%
    3.Stamina: 3
    4.x Atk: 5
    5.x Monedas: 1.0

2.Angel->Futbolista

    Stats:
    1.Hp: 8
    2.Lck: 70%
    3.Stamina: 5
    4.Atk: 5
    5.x Monedas: 2

3.Daniel->Vikingo

    Stats:
    1.Hp: 8
    2.Lck: 85%
    3.Stamina: 3
    4.Atk: 4
    5.x Monedas: 1.0

4.Juan->

    Stats:
    1.Hp: 6
    2.Lck: 80%
    3.Stamina: 4
    4.Atk: 4
    5.x Monedas: 1.0


#### ***Generos***

Es un RPG (Role-Playing Game) que contiene elementos o generos como:

##### **Subgeneros**

1. Shooter: Este genero se encuentra en uno de los escenarios o espacios liminales.
   
2. Survival Horror: Este genero se encuentra en uno de los escenarios o espacios liminales.
   
3. Roguelike, Shooter, Survival RPG: Es el subgenero principal de nuestro videojuego. Se basa en mazmorras aleatorias con combate a larga distancia.


![Fotografia de una idea sobre roguelike](https://static.wikia.nocookie.net/bindingofisaac/images/4/43/Habitaci%C3%B3n_Home.png/revision/latest?cb=20221002180239&path-prefix=es)

![Fotografia de una idea de los shooter](https://cdn.akamai.steamstatic.com/steam/apps/311690/ss_9a74ab65fb19e85cac6a64b7dbe05da5411cfb7b.1920x1080.jpg?t=1666986657)

![Fotografia de una idea de los survival horro](https://e00-marca.uecdn.es/assets/multimedia/imagenes/2019/07/18/15634789301233.jpg)

### **Gameplay**

El gameplay debe de contener elementos del RPG.

1. El jugador podra elegir entre cuatro personajes. Cada personaje tiene stats diferentes.

2. Narrativa: El jugador se imserse dentro de la historia. Desea conocer el origen del lugar.

3. Interaccion con el mundo: El jugador podra interactuar con los escenario, npc y objetos del juego.

4. Progresion de personaje/mundo: El jugador podra intercambiar entre mejores objetos o consumiendo varios consumibles para que se facilite las misiones.

5. Sobrevivir: El jugador debe de utilizar las armas y objetos que tenga a su dispocicion para sobrevivir por los diferentes niveles.

### **Obstaculos**

La meta de juego es sobrevivir y escapar de los backrooms utilizando las herremientas que se encuentran en los distintos escenarios. Debes de realizar varias misiones principales para recolectar varias llaves con las cuales podras abrir la puerta al boss final. 

Los obstaculos que se encuntran en nuestro videojuego son varios puzzles que se deben de resolver para abrir diferentes zonas. Luego, los principales obstaculos son los diferentes enemigos (fobias) y la oscuridad que intentara asesinar al jugador.

El jugador encontrara enemigos y puzzles dentro de los diferentes niveles. Debera de pasarlos para encontrar una de las llaves para abrir la salida.




![Fotografia de una idea de los obstaculos](https://i.ytimg.com/vi/5bc8on9ujxQ/maxresdefault.jpg)

![Fotografia de una idea de los obstaculos](https://itstimetoescape.com/wp-content/uploads/2021/04/Tut_E-800-min.jpg)

### **Estrategia**

Sobrevivir, escapar, aprender, apostar y pelear de regreso son palabras clave a lo largo del desarrollo de la historia.  El jugador deberá utilizar todas las herramientas a su disposición para lograr sobrevivir, por lo que la escasez de estos, y la toma de decisiones del jugador a la hora de interactuar con el mundo repercutirán el desarrollo de la historia.

![Fotografia de videojuegos de Binding of isaac referencia hacia un gameplay parecido](https://imgs.search.brave.com/wv4ztwWMCFwYdh1IIjY3_NDzGnm11SxvOFKGNh9I4e4/rs:fit:960:540:1/g:ce/aHR0cHM6Ly9tZXRp/bWVnYW1lci5maWxl/cy53b3JkcHJlc3Mu/Y29tLzIwMTQvMTEv/aXNhYWNfaGVhZHRy/YXVtYS5wbmc)

### **Mindset**

El jugador se debe de sentir confundido, intrigado, atento, analítico, cuidadoso y aventurero pero con cierto nerviosismo.
Estas emociones se van a conseguir al poner el jugador en diferentes situaciones que implican su supervivencia, junto con el pensamiento de ahorro de recursos dado a que serán limitados.

A lo largo de la historia, existen dos caminos que puede tomar, por lo que en uno de ellos se va a sentir empoderado dado a que puede pelear en contra de los que lo quieren herir, mientras que en el otro se va a sentir totalmente en desventaja dado a que solo puede escapar y preocuparse de los recursos a sus disposición. 

![Fotografia de un ejemplo de como se debe de sentir el jugador](https://cdn.cheatcc.com/news_images/stress.jpg)
![Fotografia de un ejemplo de como se debe de sentir el jugador](https://desaludpsicologos.es/wp-content/uploads/2020/07/desaludpsicologos-fobiasocial21.jpg)

## _Technical_

---

### **Screens**

1. Title Screen
   1. Nueva Partida
      1. Seleccionar entre cuatro personajes
      2. Salida de pestaña
   2. Cargar Partida
      1. Muestra las partidas creadas con anterioridad (max 2)
   3. Logros
      1. Muestra los logros que obtuvo el jugador
      2. Muestra los easter eggs que obtuvo
   4. Opciones
      1. Brillo
      2. Sonido
      3. Controles 
      4. Lenguaje
   5. Creditos
   6. Salida del juego

2. Pantalla de pausa:
    1. Continuar
    2. Reiniciar
    3. Salir al menu

3. Pantalla (Tutorial):
   1. Escena Principal
   2. Dialogos
   3. Pausa

4. Pantalla (Lobby):
   1. Escena Principal
   2. Dialogos
   3. Pausa

5. Pantalla (Hospital):
   1. Escena Principal
   2. Dialogos
   3. Pausa

6. Pantalla (Bosque):
   1. Escena Principal
   2. Dialogos
   3. Pausa

7. Pantalla (Final):
   1. Escena Principal
   2. Dialogos
   3. Pausa

### **Controls**

How will the player interact with the game? Will they be able to choose the controls? What kind of in-game events are they going to be able to trigger, and how? (e.g. pressing buttons, opening doors, etc.)

Pc:

    1. Movimento: w,a,s,d
    2. Correr: shift izquierdo
    3. Interactuar con objetos y NPCs: e
    4. Abrir inventario: f
    5. Utilizar objeto o arma: click izquierdo
    6. Cambiar arma: click derecho

### **Mechanics**

**Debemos de dividir las mecanicas pasivas y activas para un mejor enfoque. Las pasivas son aquellas que se realizan automaticamente y las activas son expresadas a traves de los controles o teclas que debe de oprimir el jugador**

Las mecanicas activas que tenemos planteadas para nuestro videojuego son las siguientes: 

1. Movimiento basico: Tenemos planeado implementar el movimiento horizontal y vetical sobre un plano 2d. La mecanica se realizara con las w,a,s,d o con las flechas que se encunetran a mano derecha.

2. Movimiento avanzado: Tenemos planeado implementar la opcion de correr a traves de la tecla del "shift izquierdo". Esta mecanica le permitira al jugador evadir varios enemigos y moverse de manera rapida por el mapa.

3. Combate: Tenemos planeado implementar la mecanica de combate cuerpo a cuerpo y a distancia dependiendo de la arma que este utilizando el jugador en su momento. Esta mecanica se podra utilizar al oprimir el boton izquierdo del mouse, al igual que rotar por las diferentes armas con click derecho.

4. Consumir Objetos: Tenemos planeado que el jugador pueda consumir varios de los objetos consumibles (vida, escudo, stamina, atk) utilizando el click izquierdo.

5. Interactuar: El jugador podra interactuar con el entorno y los distintos objetos a traves de la tecla E.
   
Las mecanicas pasivas que tenemos planteadas para nuestro videojuego son las siguientes:

1. Recolectar objetos: El jugador podra recoger varios de los objetos del juego unicamente pasando por encima de estos.

2. Dropeo de Items: Los enemigos al morir doprearan objetos.
   
## _Level Design_

### **Themes**

En este apartado nos enfocamos en los diferentes niveles y las caracteristicas que cada uno posee:

1. Introduccion/Tutorial:
    1. Ambiente:
        1. Dark, calm, foreboding
        2. Escenario Oficina
     2. Objetos y elementos:
        1. _Ambient_
            1. Escritorios
            2. Sillas
            3. Maquinas exprendedoras
            4. Pizarrones
            5. Sofas
            6. Macetas
        2. _Interactive_
            1. Puertas
            2. NPC Mueble
2. Lobby:
    1. Ambiente:
        1. Calm, broad, warm
     2. Objetos y elementos:
        1. _Ambient_
            1. Arboles
            2. Caminos
            3. Pilares
            4. Flores
            5. Fuentes
            6. Sillas
        2. _Interactive_
            1. Tienda
            2. Notas
            3. NPC
3. Hospital:
    1. Ambiente:
        1. Dangerous, tense, active
    2. Objetos y elementos:
        1. _Ambient_
            1. Camillas
            2. Sillas
            3. Agujas
            4. Cortinas
            5. Herramientas medicas
        2. _Interactive_
            1. Armas de Luz
            2. Enemigos
            3. Puertas
            4. Cofres
4. Bosque:
    1. Ambiente: 
        1. Dangerous, tense, active
    2. Objetos y elementos:
        1. _Ambient_
            1. Arboles
            2. Telarañas
            3. Estatuas
            4. Agua
            5. Esqueletos
            6. Arbustos
            7. Rocas
            8. Caminos
            9. Antorchas
        2. _Interactive_
            1. Armas
            2. Enemigos
            3. Cofres



### **Game Flow**

Los pasos o estado los cuales el jugador va a vivir o tendra que experimentar. Basicamente, los pasos que debe de seguir para pasar el nivel:

1. Tutorial:
   1. El jugador inicia en el nivel introductorio.
   2. El juego se desplaza de la oficina principal y entra en un laberinto.
   3. Recorre los diferentes pasillos y habitaciones, mientras aprende los controles basicos.
   4. El jugador debe de encontrar e interactuar con diferentes elementos dentro del laberinto.
   5. Cerca de la salida el jugador vive la experiencia de ser perseguido por una especie de ente o criatura.
   6. El jugador alcanza la salida hacia el siguiente escenario.

2. Lobby:
   1. Despues de la introduccion, el jugador despertará en la entrada de un ruinas/bosque.
   2. El jugador esta desconcertado y confundido.
   3. Podra hablar con toda la gama de NPCs que estan dentro del area, de los cuales los mas importantes son:
      1. La tienda
      2. La bruja
      3. Multitud alrededor de una ejecución
      4. Un vikingo
      5. Una serie de animales
      6. E intentar hablar con una niña que corre de ti
   4. Se dará a entender que para llegar al boss final, se requieren llaves para abrir la puerta.
   5. El juego te dara dos opciones, aventurarte al bosque o entrar al hospital


3. Bosque:
   1. En la entrada te atiende el dueño de la tienda, y despues de una introduccion a las mecanicas, te dara la opcion del arma principal de acuerdo al personaje que el jugador escogio.(se pierden las armas si se ingresa al hospital primero).
   2.  Despues entraras al bosque obscuro, donde mataras mobs y obtendras recursos.
   3.  El jugador debera de recorrer 3 mazmorras para conseguir una de las llaves para el boss final.
   4.  El gameplay y dificultad del bosque incrementará cada vez que se ingrese al bosque obscuro, y de esa manera la posibilidad de comprar mejores armas y desarrollar la historia.
   5. Durante su recorrido podra encontrar mas información sobre que esta ocurriendo, al igual que recolectar items y dinero que le ayudaran a sobrevivir su estancia.


4. Hospital:
   1. Se colocara el personaje en un ambiente hostil y de total supervivencia. Existe la obsuridad que asechará al personaje en todo momento (se pierden las armas si se ingresa al bosque primero).
   2. En el hospital, el jugador nunca puede quedarse sin luz dado a que seria consumido por la obscuridad.
   3. En este lugar estaran otros mobs que quieren igual consumir al personaje principal, pero con la ayuda de fuentes de luz y el movimiento del personaje, este escapara de ellos.
   4.El jugador debera de recorrer 3 mazmorras para conseguir una de las llaves para el boss final.
   5. Durante su recorrido podra encontrar mas información sobre que esta ocurriendo, al igual que recolectar items y dinero que le ayudaran a sobrevivir su estancia.

5. Boss Final:
   1. Al obtener ambas llaves, el jugador principal entra a la ultima etapa del juego, que combinara ambas mecanicas del hospital y bosque (la obscuridad y armas para pelear de regreso).
   2. Morir en esta etapa del juego, acabará el juego y se obtendra el final donde pierde el personaje principal.
   3. Matar al boss final, descubrir la causa de los backrooms y escapar acabará el juego con el final de escapar del glitch (backrooms).

## _Development_

---

### **Abstract Classes / Components**

En este apartado nos enfocamos en las diferentes clases u objetos/elementos que tendra nuestro videojuego:

1. Objetos Fisicos Vivientes:
    1. Jugador principal
    2. Jugadores no jugables (NPC)
    3. Enemigos (Phobias)
    4. Enemigos (Oscuridad)
2. Objetos Fisicos No Vivientes (Obstaculos):
   1. Muros
   2. Pisos
   3. Amoblados o elementos de estética
   4. Plantas
   5. Puertas
   6. Ventanas
   7. Iluminacion (luces estaticas)
   8.  Utencilios o herramientas
3. Objetos Iteractivos o Especiales:
   1. Objetos Consumibles
   2. Dinero (Huesos)
   3. Armas de Fuego
   4. Armas de Luz
   5. Easter Eggs

### **Derived Classes / Component Compositions**

Las clases derivadas son aquellas que definen a nuestra clases principales a un nivel mucho mas especifico:

1. Jugador Principal
    1. Samurai
    2. Futbolista
    3. Arqueologo
    4. NULL
2. Jugadores no jugables (NPC)
    1. La bruja
    2. The hanged man
    3. Dueño de la tienda
    4. Niña del pueblo
    5. Vikingo
    6. Multitud
    7. Town´s men
3. Enemigos (Phobias)
   1. Arañas
   2. Arañas toxicas
4. Enemigos (Oscuridad)
    1. Clumps
    2. Smilers
5. Muros
    1.Muros oficina
    2.Muros lobby (Arboles)
    3.Muros hospital
    4.Muros bosque (Arboles)
6. Pisos
    1.Pisos oficina
    2.Pisos lobby (Arboles)
    3.Pisos hospital
    4.Pisos bosque (Arboles)
7. Decorativos
   1. Amoblados
   2. Plantas
   3.  Puertas
   4.  Ventanas 
   5.  Iluminacion
   6.  Utencilios o Herramientas
8.  Objetos Consumibles
    1.  Vida
    2.  Escudo
    3.  Stamina
    4.  Atk
9.  Dinero
    1.  Huesos
10. Armas
    1. Rifle
    2. Ballesta
    3. Espada
    4. Bate
    5. Baston
11. Armas de Luz
    1.  Linterna
    2.  Antorcha
    3.  Mechero
    4.  Pistola de Bengalas

## _Graphics_

2D con perspectiva desde arriba. El jugador utilizara una perspectiva top down , donde podra moverse de manera vertical y horizontal.

### **Style Attributes**

Utilizaremos una paleta colores amplio. Sin embargo nos enfocaremos en colores oscuros u opacos para generar un ambiente tenso.

El diseño de los personajes asi como el de los escenarios sera en pixel art (algunos dibujos estara dibijados en 16pixeles, 32pixeles o incluso mas para un mejor detalle).

La estetica que tendra los escenarios y los personajes mostrara una apariencia cansada, terrorifica, lastimada, abandonada, etc.

Cada elemento viviente tendra animaciones para cada accion como correr, atacar, ser golpeado, interactuar, etc.

Cada objeto consumible tendra cierta animacion o particulas para dar sensacion de que el objeto fue utilizado.

### **Graphics Needed**

1. Characters
    1. Human-like
        1. Personaje #1 (idle, walking, attacking)
        2. Personaje #2 (idle, walking, attacking)
        3. Personaje #3 (idle, walking, attacking)
        4. Personaje #4 (idle, walking, attacking)
        5. Niña (idle, walking)
        6. Vikingo (idle)
        7. Dueño de tienda #1 (idle)
    2. Other
        1. Dueño de tienda #2 (idle)
        2. Araña (idle, walking, attacking)
        3. Arañas toxicas (idle, walking, attacking)
        4. Estatuas (idle, walking, attacking)
        5. Zombies (idle, walking, attacking)
        6. Zombies toxicos (idle, walking, attacking)
        7. Fantasmas (idle, walking, attacking)
        8. Personas locas (idle, walking, attacking)
        9. Occultist (idle, walking, attacking)
2. Blocks
    1. Dirt
    2. Dirt/Grass
    3. Stone Block
    4. Stone Bricks
    5. Tiled Floor
    6. Weathered Stone Block
    7. Weathered Stone Bricks
3. Ambient
    1. Tall Grass
    2. Rodent (idle, scurrying)
    3. Torch
    4. Armored Suit
    5. Chains (matching Weathered Stone Bricks)
    6. Blood stains (matching Weathered Stone Bricks)
4. Other
    1. Chest
    2. Door (matching Stone Bricks)
    3. Gate
    4. Button (matching Weathered Stone Bricks)

_(example)_


## _Sounds/Music_

---

### **Style Attributes**

Again, consistency is key. Define that consistency here. What kind of instruments do you want to use in your music? Any particular tempo, key? Influences, genre? Mood?

Stylistically, what kind of sound effects are you looking for? Do you want to exaggerate actions with lengthy, cartoony sounds (e.g. mario&#39;s jump), or use just enough to let the player know something happened (e.g. mega man&#39;s landing)? Going for realism? You can use the music style as a bit of a reference too.

 Remember, auditory feedback should stand out from the music and other sound effects so the player hears it well. Volume, panning, and frequency/pitch are all important aspects to consider in both music _and_ sounds - so plan accordingly!

 Para nuestro juego es necesario que el jugador se sienta dentro de la situacion en la que esté, que se pueda sentir como si el fuera quien esta viviendo dentro del juego, por lo tanto es necesaria la implementacion de efectos auditivos en el mismo. A continuación se presentan los sonidos que serán necesarios para ello:

### **Sounds Needed**

1. Effects
    1. Musica en el inicio del juego.
    2. Sonidos al caminar (dependiendo del suelo que este tocando este sera variable).
    3. Sonido al abrir el menu de pausa.
    4. Efecto de sonido al recoger un arma.
    5. Efecto de sonido cuando recoja habilidades.
    6. Sonido de abrir puerta.
    7. Sonido al morir.
    8. Sonido de los enemigos al aparecer y ser golpeados.
    9. Entre otros que vayan surgiendo con el desarrollo del juego


## _Schedule_

Como hemos venido trabajando, no han sido fijadas fechas límite para tener secciones listas debido a que es necesaria la aprobación de ideas de los profesores para poder organizarnos y empezar a distruibuir la carga de trabajo entre nosotros.

_(define the main activities and the expected dates when they should be finished. This is only a reference, and can change as the project is developed)_

1. develop base classes
    1. base entity
        1. base player
        2. base enemy
        3. base block
  2. base app state
        1. game world
        2. menu world
2. develop player and basic block classes
    1. physics / collisions
3. find some smooth controls/physics
4. develop other derived classes
    1. blocks
        1. moving
        2. falling
        3. breaking
        4. cloud
    2. enemies
        1. soldier
        2. rat
        3. etc.
5. design levels
    1. introduce motion/jumping
    2. introduce throwing
    3. mind the pacing, let the player play between lessons
6. design sounds
7. design music

_(example)_
