# Madness
Grupo 07- NextStationGames
 
## RESUMEN

**Género:** RPG, mazmorras, aventura

**Modo:** Un jugador

**Público objetivo:** 14+ años con experiencia en el medio

**Plataforma:** Web

**Autores:** Maria Eduarda Beckers, Haoshuang Hou, Mauro Martínez y Bingcheng Wang

## Descripción
Madness es un juego RPG en el que disfrutarás de una emocionante aventura junto a Julie, nuestra protagonista. Julie, una joven obsesionada con el póker, es secuestrada y llevada al mundo de las cartas por el Joker. Al llegar allí, se olvida de su pasado y lo único que sabe es que, para recuperar su libertad, deberá encontrar al Joker, quien la espera en el último piso. A lo largo de la travesía, te enfrentarás a numerosos enemigos mientras descubres los misterios del pasado de Julie.

## Índice
- [1. Jugabilidad](#1-jugabilidad)
  - [1.1. Movimiento del personaje](#11-movimiento-del-personaje)
  - [1.2. Cámara](#12-cámara)
  - [1.3. Mecánicas del jugador](#13-mecánicas-del-jugador)
  - [1.4. Mecánicas de escenario](#14-mecánicas-de-escenario)
  - [1.5. Enemigos y Bosses](#15-enemigos-y-bosses)
- [2. Diseño de nivel](#2-diseño-de-nivel)
  - [2.1. Descripción de partida típica](#21-descripción-de-partida-típica)
- [3. HUD](#3-hud)
  - [3.1. Mockup del HUD](#31-mockup-del-hud)
  - [3.2. Explicación de los elementos del HUD y su funcionamiento](#32-explicación-de-los-elementos-del-hud-y-su-funcionamiento)
- [4. Moodboard](#4-moodboard)
- [5. Menús y flujo de juego](#5-menús-y-flujo-de-juego)
  - [5.1. Menú inicial](#51-menú-inicial)
  - [5.2. Menú pausa](#52-menú-pausa)
  - [5.2. Menú logros](#53-menú-logros)
  - [5.2. Menú habilidades](#54-menú-habilidades)
  - [5.5. Flujo de juego](#55-flujo-de-juego)
- [6. Contenido](#6-contenido)
  - [6.1. Historia](#61-historia)
  - [6.2. Personajes](#62-personajes)
  - [6.3. Enemigos](#63-enemigos)
  - [6.4. Objetos](#64-objetos)
  - [6.5. Logros](#65-logros)
- [7. Referencias](#7-referencias)

## Descripción:   
**Madness** es un juego RPG en el que disfrutarás de una emocionante aventura junto a Julie, nuestra protagonista.   
Julie, una joven obsesionada con el póker, es secuestrada y llevada al mundo de las cartas por el Joker.
Al llegar allí, se olvida de su pasado y lo único que sabe es que, para recuperar su libertad, deberá encontrar al Joker quien la espera en el último piso. A lo largo de la travesía, te enfrentarás a numerosos enemigos mientras descubres los misterios del pasado de Julie.   

## 1. Jugabilidad:

### 1.1. Movimiento del personaje
El movimiento será en un entorno 2D utilizando los controles estándar de WASD (W para arriba, D para la derecha, A para la izquierda y S para abajo) para desplazarse tanto de manera vertical como horizontal. Además, los controles podrán combinarse para moverse en diagonal. El personaje se moverá a una velocidad máxima uniforme. 

### 1.2. Cámara
La cámara tendrá una perspectiva top-down que estará siguiendo al jugador, manteniéndolo siempre en el centro de la vista.

### 1.3. Mecánicas del jugador
El personaje atacará con el botón izquierdo del ratón disparando proyectiles hacia la dirección donde esté ubicado el cursor (el disparo irá esa ubicación al ser pulsado el botón). Además, el personaje podrá interactuar con ciertos objetos y NPCs en el escenario al presionar la tecla E.

Al derrotar a los enemigos, soltarán fichas (experiencia) que te permitirán subir de nivel. Con cada subida de nivel, obtendrás un punto de status, que podrás usar para mejorar diferentes atributos. Además, cada 3 niveles recibirás un punto de habilidad, que podrás utilizar en el árbol de habilidades. Para potenciar tus habilidades, necesitarás un número específico fichas que obtendrás al vencer a los enemigos.

#### Árboles de habilidades
  - **<ins>Juego de proyectiles</ins>:**
    1. Disparar dos proyectiles
    2. Disparar tres proyectiles
    3. Disparar cuatro proyectiles
   
  - **<ins>Francotirador explosivo</ins>:**
    1. Aumentar el 50% de tamaño del proyectil.
    2. Cuando un proyectil llega al final de su trayecto o se choca con un enemigo, se explota e inflige más daño.
  
  - **<ins>Utilidad</ins>:**
    1. Desbloquear nuevo control: “clic derecho ratón”: generar una torreta que no se mueve y dispara los enemigos que están dentro de su rango de ataque. Se destruye si después de un intervalo de tiempo. No puede coexistir 2 torretas a la vez;
    2. Tener un dron que te persigue y ataca automáticamente a los enemigos.
  - **<ins>Mejorar status</ins>:**
    1. <ins>Más vida</ins> (hasta 5 veces, n vida más por cada mejora, siendo n el número de veces que has mejorado este status)
    2. <ins>Más velocidad de movimiento</ins> (hasta 5 veces, un 15% por cada mejora).
    3. <ins>Más velocidad de disparo</ins> (hasta 5 veces, un 20% por cada mejora).
    4. <ins>Más ataque</ins> (hasta 5 veces, +2 por cada mejora).
    5. <ins>Más probabilidad de hacer un ataque crítico</ins> que inflige el doble de daño (hasta 5 veces, un 5% por cada mejora).
 
![Juego de proyectiles](https://github.com/user-attachments/assets/39f53189-3736-41c7-8299-423ee501844e)

*Concept art del arbol de habilididades y mejoras de status*

### 1.4. Mecánicas de escenario
  En el escenario, el jugador se encontrará con objetos interactuables que estarán relacionados con la historia. También habrá algunos objetos que desbloquearán logros y que funcionarán como easter eggs.

  #### Trampas
  + <ins>Pinchos en el suelo</ins>: Suben y bajan periódicamente, haciendo daño si el jugador entra en contacto cuando están subidos.
  + <ins>Espinas</ins>: Pinchos estáticas que causan daño al contacto.
  + <ins>Estatua</ins>: dispara proyectiles hacia delante.

### 1.5 Enemigos y Bosses
  En cada piso habrá una serie de enemigos y un boss, aumentando su dificultad de forma gradual conforme avances. La parte estética de los bosses está inspirada en las figuras de las cartas de póker, añadiendo un toque temático a su diseño.

  #### **Enemigos base**
  + **Bob** (enemigo de ataque cuerpo a cuerpo): Un enemigo sencillo que persigue al jugador. Tiene menor velocidad y tamaño que la protagonista.
    + Vida(5), Daño(1)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/bob_G.png" alt="Bob" width="100" />
      
  + **Crac** (enemigo que lanza proyectiles): Cuenta con un radio de visión que determina cuándo empieza a atacar. Tiene velocidad normal.
    + Vida (3), Daño (1)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/crac_G.png" alt="Bob" width="100"  />

 + **Letus** (enemigo que vuela y ataca cuerpo a cuerpo): Se asemeja a un murciélago.
    + Vida (5), Daño (2)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/letus_G.png" alt="Bob" width="100" />
      
  + **Zaro** (enemigo que puede teletransportarse): Ataca a distancia, similar al enemigo que lanza proyectiles (fantasma).
    + Vida (4), Daño (6)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/zaro_G.png" alt="Bob" width="100" />

  + **Mutum** (enemigo bomba): Un ataque de hit kill, pero explota y causa daño en área. Si el jugador entra en su campo de ataque, se suicida. Persigue al jugador.
    + Vida (4), Daño (16)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/mutum_G.png" alt="Bob" width="100" />

  + **Estaka** (enemigo de daño en área): Si el jugador entra en su área, provoca una explosión.
    + Vida (12), Daño (10)

      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/GDD/estaka_G.png" alt="Bob" width="100" />
  + **!** los enemigos que aparecen en el nivel anterior y vuelven a salir en el nuevo nivel son más fuertes

#### **Boss**
  + **Joker**: Se teleporta y causa daño en área y cuerpo a cuerpo.
    + **Mecánica 1**: Dispara 2 cartas.
    + **Mecánica 2**: Se activa cuando su vida llega a la mitda. Crea 5 cartas en el suelo. Por cada carta que destruyes, le haces daño al Joker. Si no las destruyes a tiempo, él te causará daño.
    + **Mecánica 3**: Se crean tres orbes que persiguen al jugador.
    + **Mecánica 4**: Se crea un daño en área.
      
      <img src="https://raw.githubusercontent.com/bingoo30/PVLI-C2024-2025-Grupo7/main/Juego/assets/enemies/joker/joker.png" alt="Joker" width="100" />

## 2. Diseño de nivel

El jugador deberá explorar el mapa y encontrar llaves en las salas para poder ascender de planta. Cada planta representará un nivel, y dentro de cada nivel habrá diferentes salas donde el jugador tendrá que explorar y enfrentarse a enemigos para obtener la llave poder pasar a la siguiente sala.

![image](https://github.com/user-attachments/assets/f02e9fd8-f368-4593-a62e-9eddb2a85add)

### 2.1. Descripción de partida típica

En una partida normal el jugador empezará en el hall del primer piso, donde se encontrará con un NPC que le dará una explicación sobre ese mundo. Al finalizar la explicación el jugador podrá salir del hall y empezar su busca por la puerta del próximo piso y buscar la llave para abrirla. Al largo de los niveles, el jugador aprenderá sobre la historia de la protagonista mientras ella va recuperando sus recuerdos y también aprenderás mejor sobre como funciona ese mundo. Al llegar a último piso, el jugador tendrá que derrotar al Joker para que se acabe el juego.

Si el jugador muere en el camino, volverá al checkpoint de cada piso, es decir, se reinicia el nivel.


## 3. HUD

### 3.1. Mockup del HUD
![image](https://github.com/user-attachments/assets/7e38b5b6-474b-423f-81dd-6844a75d8549)

### 3.2. Explicación de los elementos del HUD y su funcionamiento.
**Vida:** Barra que muestra el porcentaje de salud que le queda al jugador.

**Experiencia:** Barra que muestra la cantidad de experiencia que tiene el personaje respecto a cuanto le queda para subir al siguiente nivel.

**Habilidades que se puede usar:** Lista de las Habilidades de Utilidad desbloqueadas, con sus cooldowns y una letra en el canto inferior indicando cual es la tecla para activar la habilidad.

//**Mapa:** Minimapa que muestra de forma esquemática la ubicación del personaje. Solo indica la habitación en la que está el personaje y las habitaciones que ha visitado en forma de cuadrados conectados por líneas. Los cuadrados serán rellenados con diferentes colores dependiendo de si el personaje está ahí o no. (no implementado)

**Imagen de quién está hablando:** Autodescriptivo, muestra un retrato del personaje que está hablando en ese momento.

**Diálogos:** Autodescriptivo, diálogos del juego.4.	Visual

El apartado visual será bastante abstracto, cada nivel tendrá muchos elementos que no se relacionan unos con otros y algunas salas con colores vibrantes y otras con colores muy oscuros, con la intención de pasar una sensación de que ese mundo es una extensión de la personalidad del Joker, el amo de ese mundo.

## 4. Moodboard
[Pinterest](https://pin.it/5GXh8RoGd)


## 5. Menús y flujo de juego
En cuanto a los menús, se trata de una cosa bastante simple. Tendremos un botón de jugar, logros y tutorial. Para mostrar el menú de pausa hay que pulsar la tecla “P”. Aparecerán opciones como continuar el juego, volver a la pantalla y guardar el progreso (opcional) //(implementado).

### 5.1. Menú inicial
![image](https://github.com/user-attachments/assets/6fda0409-ad94-4653-b42a-08055dc6600f)

### 5.2. Menú pausa
![image](https://github.com/user-attachments/assets/0d6b8af2-0957-4ed7-ad1f-52f568e7dcbf)

### 5.3. Menú logros
![image](https://github.com/user-attachments/assets/99227751-638c-4fca-ad4e-f2c5e450661b)

### 5.4. Menú habilidades
![image](https://github.com/user-attachments/assets/2b3e56ef-526c-4b35-8c57-f7ed8cbf0b7a)

### 5.5. Flujo de juego
![pdf](https://github.com/user-attachments/assets/596f17ab-4388-43c9-afb0-1b0a162a6aac)


## 6. Contenido

### 6.1. Historia

La protagonista se despierta en una sala donde un NPC le explica que se encuentra en el mundo creado por Joker, conocido como el mundo de las cartas. Gracias a la explicación del NPC, la protagonista comprende que está en la primera planta y que debe llegar hasta la cuarta planta para enfrentarse a Joker y así poder salir de ese mundo. Para lograrlo, necesita encontrar la escalera y la llave, las cuales están escondidas en las salas que pueden contener peligros. Además, se da cuenta de que no recuerda nada, ni siquiera quién es. Solo sabe que debe salir de este mundo tan abstracto. Siente que podría recuperar todos sus recuerdos cuando se enfrente a Joker. Durante su aventura, se encuentra con diferentes cartas que complican su camino.

**Diálogos**: https://docs.google.com/document/d/1oQPfke9P-dSs6Ti84vxHJZ5maxgCPH4xZX8zxMSC6SQ/edit?tab=t.0

### 6.2. Personajes


**Julie:** Una chica joven de unos 22 años que ha olvidado quién era. Según lo que han contado, fue secuestrada al mundo extraño de Joker. Durante su aventura, irá recordando su pasado

**NPCs:**

***Flush:*** un señor mayor que estará en el hall del primer piso, será el responsable de introducir al jugador el objetivo y reglas principales del juego.

***Weiyoung:*** una amiga próxima de la protagonista que estará en el segundo piso y con ella la protagonista recordará de sus sueños y las esperanzas que tenía junto a su amiga.

//***Romeo:*** El ex novio de Julie, al encontrarle, la protagonista se recordará de su adolescencia y todos los momentos bonitos que pasaron juntos . Estará en el tercer piso. (no se va a hacer)

 ***Piu:*** Gato de Julie, estará en el cuarto piso y se recordará de los momentos felices antes de apostar.


### 6.3. Enemigos

**Bosses:**
***Joker:*** Personaje que secuestra a la protagonista y es el amo del mundo de las cartas y actúa como jefe final. (Es la parte de culpa de la prota, quien le dice las cosas malas que ha hecho, y se entera de está intentando cambiar)

**Enemigos normales:** Criaturas inspiradas en cartas de poker.

### 6.4. Objetos

**Llave:** Es esencial para poder subir de piso y estará escondida en alguna sala.

**Fichas de póker:** Actúan como puntos de experiencia que se obtendrán al derrotar enemigos.

**Hierbas:** Sirven como cura para recuperar la vida del jugador.

**Memorias:** Los recuerdos de la protagonista.

**Objetos relacionados con los logros:** Estarán distribuidos en diferentes lugares del mapa.

Casco.

Lápiz roto.

Teclado sin teclas.

### 6.5. Logros

Salir del primer piso.

Salir del segundo piso.

Salir del tercer piso.

Desbloquear el árbol entero.

Encontrar a Joker.

Matar a x enemigos.

Llegar al nivel x.

Morir x veces.

Derrotar a J/Q/K/Joker.

Encontrar los cascos perdidos.

Encontrar un lápiz roto.

Encontrar teclado sin teclas.

Hablar con Flush: Has conocido al señor Flush, un señor amable que te explicó donde estas.

Hablar con Weiyoung: Has encontrado a tu amiga.

Encontrar a Piu.

## 7. Referencias
Mecánicas: The Binding of isaac, Darkest Dungeon.

Temática: Poker.

Estilo del cuadro de diálogo: Angels of Death.

Personalidad de Joker: Balatro.

Estética: Alicia en el país de las maravillas.

Temática: Poker.
Estilo del cuadro de diálogo: Angels of Death.
Personalidad de Joker: Balatro.
Estética: Alicia en el país de las maravillas.
