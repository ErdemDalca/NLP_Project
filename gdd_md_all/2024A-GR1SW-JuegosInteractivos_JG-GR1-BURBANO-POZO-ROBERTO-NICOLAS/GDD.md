# <center>Game Design Document (GDD)

# 1. Portada

Título del juego: BikerStop

Versión: 1.0

Fecha: 28 de junio de 2024

Autor: Nicolás Burbano


# 2. INDICE

- [Game Design Document (GDD)](#game-design-document-gdd)
- [1. Portada](#1-portada)
- [2. INDICE](#2-indice)
    - [3. Visión General del Juego](#3-visión-general-del-juego)
      - [3.1 Descripción](#31-descripción)
      - [3.2 Objetivo](#32-objetivo)
      - [3.3 Género](#33-género)
      - [3.4 Plataformas](#34-plataformas)
      - [3.5 Público Objetivo](#35-público-objetivo)
      - [3.6 Inspiración e Influencias](#36-inspiración-e-influencias)
      - [3.7 Modelo de negocio](#37-modelo-de-negocio)
    - [4. Mecánicas del Juego](#4-mecánicas-del-juego)
      - [4.1 Descripción General de la Jugabilidad](#41-descripción-general-de-la-jugabilidad)
      - [4.2 Controles](#42-controles)
      - [4.3 Mecánicas](#43-mecánicas)
      - [4.4 Mejoras](#44-mejoras)
      - [4.5 Obstáculos](#45-obstáculos)
      - [4.6 Recolectables](#46-recolectables)
    - [5. Mundo del Juego](#5-mundo-del-juego)
      - [5.1. Historia](#51-historia)
      - [5.2. Descripción del Mundo](#52-descripción-del-mundo)
      - [5.3. Mapas y Niveles](#53-mapas-y-niveles)
      - [5.4. Personajes](#54-personajes)
    - [6. Estética del Juego](#6-estética-del-juego)
      - [6.1. Estilo Visual](#61-estilo-visual)
      - [6.2. Diseño de Personajes](#62-diseño-de-personajes)
      - [6.3. Diseño de Niveles](#63-diseño-de-niveles)

<div id='id3' />

### 3. Visión General del Juego

<div id='id31' />

#### 3.1 Descripción

"BikerStop" es un juego de exploración y puzzle 2D donde el personaje Doe tiene que recolectar partes para mejorar su bicicleta para ir la transformando en la motocicleta de sus sueños. Doe debe explorar diferentes partes de su cuidad para encontrar cajas con materiales que le permitirán realizar mejoras a su bicicleta al terminar cada nivel y poder ir superando los obstáculos que cada distrito de su cuidad le tiene preparado. 

<div id='id32' />

#### 3.2 Objetivo

Encontrar todas las cajas escondidas en el mapa para poder explorar en más zonas e ir mejorando la bicicleta hasta transformarla en una motocicleta.

<div id='id33' />

#### 3.3 Género

Exploración, recolección, puzzle.

<div id='id34' />

#### 3.4 Plataformas

PC

<div id='id35' />

#### 3.5 Público Objetivo

Para todo público, jugadores casuales que disfrutan de la exploración de mapas.

<div id='id36' />

#### 3.6 Inspiración e Influencias

El juego se inspira en juegos como: "Castlevania", "The legend of zelda".

<div id='id37' />

#### 3.7 Modelo de negocio

One time purchase.

<div id='id4' />

### 4. Mecánicas del Juego

<div id='id41' />

#### 4.1 Descripción General de la Jugabilidad

El jugador controla una bicicleta en una cuidad. Se debe usar las teclas de dirección (flechas o WASD) para aumentar la velocidad pedaleando, frenar y girar. El objetivo es encontrar todas la cajas ocultas en el mapa evitando atropellar o estrellarse con elementos del mapa.

<div id='id42' />

#### 4.2 Controles

• Flecha arriba (W): Pedalear.
• Flecha arriba (S): Frenar.
• Flecha arriba (A): Girar a la izquierda.
• Flecha arriba (D): Girar a la derecha.

<div id='id43' />

#### 4.3 Mecánicas

• Pedalear: La bicicleta puede pedalear para aumentar su velocidad.
• Conforme avanza la velocidad disminuye.
• Giro: El carrito gira en función de la velocidad y la dirección.
• Choques: En función de una velocidad determinada y el objeto de colisión el juego puede terminar ya que se sufre un accidente. 

<div id='id44' />

#### 4.4 Mejoras
Son elementos que se pueden conseguir al finalizar un nivel con las piezas adecuadas
• Motor: Se incluye un pequeño motor eléctrico que permite aumentar la velocidad máxima
• Frenos de disco: Permite detener la velocidad de la bicicleta más rápido
• Equipo de protección: Permite sobrevivir a ciertos tipos de choques.
• Llantas todo terreno: Permite desplazarse sobre zonas con terreno inestables sin perder el control. 

<div id='id45' />

#### 4.5 Obstáculos 
• Personas 
• Edificios 
• Animales
• Vehículos
• Arboles

<div id='id46' />

#### 4.6 Recolectables
• Cajas principales: Cajas que requieren ser recolectadas para pasar al siguiente nivel. 
• Cajas secundarias: contienen piezas random que pueden que puede ayudar a conseguir power ups.



<div id='id5' />

### 5. Mundo del Juego

<div id='id51' />

#### 5.1. Historia

Doe es un adolescente que siempre soño en tener una de las mejores motos del planeta una poderosa Hueley, recientemente consiguió un trabajo de repartido en donde se entero que un camión de partes de su marca favorita de motos había desaparecido y muchas partes se de las motos se encontraban exparsidas por su cuidad. Doe decide emprender un viaje de exploración sobre todas las zonas de su cuidad donde se han encontrado cajas del camión perdido y con ellas modificar su actual vehículo una bicicleta para transformarla en lo más parecido a la moto de sus sueños. Sin embargo Doe no sabe que para acceder a las piezas deberá encontrar maneras de acceder a lugares difíciles y tener el equipo adecuado para no morir en el intento. 

<div id='id52' />

#### 5.2. Descripción del Mundo

El mundo del juego es una cuidad de vista topdown ambientación colorida y caricaturesca de pixel art. Está inspirado en una zona sub urbana, incluyendo árboles y arbustos.

<div id='id53' />

#### 5.3. Mapas y Niveles

• Centro de la cuidad: Zona inicial del juego ambientada en el centro de una pueblo suburbana.
• Exteriores: Alrededores de la cuidad una zona boscosa.
• El desierto: Nivel con pocas casas con bastante arena cercano a una playa.
• El barrio chungo: Cuidad la zona peligrosa.
• Parte industrial: Zona de fabricas de la cuidad.

<div id='id54' />

#### 5.4. Personajes

• Personaje principal: Doe un adolescente montado en una bicicleta.

<div id='id6' />

### 6. Estética del Juego

<div id='id61' />

#### 6.1. Estilo Visual

• Estilo artístico: Gráficos en 2D con una estética pixel art.
• Paleta de colores: Colores brillantes y contrastantes.

<div id='id62' />

#### 6.2. Diseño de Personajes

• La bicicleta de Doe: Bicicleta al estilo caricatura donde se identifica a una persona subida.

<div id='id63' />

#### 6.3. Diseño de Niveles

• Cuidad: Una cuidad con varios edificios zonas verdes y calles llena de personas y vehiculos