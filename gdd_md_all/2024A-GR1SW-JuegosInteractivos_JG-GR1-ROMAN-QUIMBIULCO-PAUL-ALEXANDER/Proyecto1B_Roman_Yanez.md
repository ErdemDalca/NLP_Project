# ESCUELA POLITÉCNICA NACIONAL
## FACULTAD DE INGENIERÍA DE SISTEMAS
### Ingeniería de Software
### PERÍODO ACADÉMICO: 2024_A
### ASIGNATURA: Juegos Interactivos
### PROFESOR: VICENTE ADRIAN EGUEZ SARZOSA
### TIPO DE INSTRUMENTO: Proyecto – Game Design
### ESTUDIANTE:

- PAÚL ROMÁN
- DAVID YANEZ

---

## Contenido

1. [Introducción](#introduccion)  
    1.1. [Descripción](#descripcion)  
    1.2. [Objetivo](#objetivo)  
    1.3. [Género](#genero)  
    1.4. [Plataformas](#plataformas)  
    1.5. [Público Objetivo](#publico-objetivo)  
    1.6. [Inspiración e Influencias](#inspiracion-influencias)  
    1.7. [Modelo de Negocio](#modelo-negocio)  
2. [Mecánicas del Juego](#mecanicas)  
    2.1. [Descripción General de la Jugabilidad](#descripcion-jugabilidad)  
    2.2. [Controles](#controles)  
    2.3. [Mecánicas](#mecanicas-juego)  
3. [Mundo del Juego](#mundo-juego)  
    3.1. [Historia](#historia)  
    3.2. [Descripción del Mundo](#descripcion-mundo)  
    3.3. [Mapas y Niveles](#mapas-niveles)  
    3.4. [Personajes](#personajes)  
4. [Estilo Visual](#estilo-visual)  
    4.1. [Diseño de Personajes](#diseno-personajes)  
    4.2. [Diseño de Niveles](#diseno-niveles)  
5. [Puntos Clave](#puntos-clave)  

---

## Game Design Document (GDD)

<div id='introduccion' />

### 1. Introducción

<div id='descripcion' />

#### 1.1. Descripción

**Título del Juego:** Sports Shooter Showdown  
**Descripción:** "Sports Shooter Showdown" es un juego de disparos en primera persona (FPS) con una estética cartoon. Los jugadores usan armas inspiradas en equipos deportivos que disparan pelotas con diferentes poderes. La variedad de municiones incluye pelotas de fuego, hielo, eléctricas, veneno, curación, aturdimiento, ceguera, y fragmentación, cada una con sus propios efectos únicos en el campo de batalla.

<div id='objetivo' />

#### 1.2. Objetivo

El objetivo principal del juego es ganar partidas eliminando a los oponentes utilizando una variedad de armas deportivas y municiones especializadas. Los jugadores deben usar estrategias inteligentes y aprovechar los poderes únicos de las pelotas para superar a sus adversarios.

<div id='genero' />

#### 1.3. Género

Shooter en Primera Persona (FPS) con temática deportiva y estética cartoon.

<div id='plataformas' />

#### 1.4. Plataformas

- PC (Windows)
- Consolas (PlayStation, Xbox, Nintendo Switch)

<div id='publico-objetivo' />

#### 1.5. Público Objetivo

Jugadores de todas las edades que disfrutan de juegos de disparos y buscan una experiencia divertida y ligera con un toque deportivo.

<div id='inspiracion-influencias' />

#### 1.6. Inspiración e Influencias

**Juegos:** "Splatoon", "Overwatch", "Team Fortress 2"  
**Películas:** "Space Jam", "Ready Player One"

<div id='modelo-negocio' />

#### 1.7. Modelo de Negocio

- Compra única con posibles expansiones y DLCs que añaden nuevas armas, pelotas y mapas.

<div id='mecanicas' />

### 2. Mecánicas del Juego

<div id='descripcion-jugabilidad' />

#### 2.1. Descripción General de la Jugabilidad

El jugador elige un personaje y entra en una arena donde puede moverse libremente, disparar pelotas y usar habilidades especiales. El objetivo es eliminar a los oponentes y capturar objetivos en modos de juego variados como deathmatch, captura la bandera y control de puntos.

<div id='controles' />

#### 2.2. Controles

- **Movimiento:** WASD
- **Disparar:** Botón izquierdo del ratón
- **Habilidad Especial:** Botón derecho del ratón
- **Saltar:** Barra espaciadora
- **Recargar:** R
- **Cambiar Arma:** Q / E
- **Interacción:** F
- **Pausa/Menu:** Esc

<div id='mecanicas-juego' />

#### 2.3. Mecánicas

- **Movimiento y Salto:** Los jugadores pueden moverse libremente por la arena y saltar para evitar ataques.
- **Disparo de Pelotas:** Cada arma dispara un tipo específico de pelota con diferentes efectos.
- **Habilidades Especiales:** Cada personaje tiene una habilidad especial que puede usar para obtener ventaja en el combate.
- **Recolección de Munición:** Los jugadores deben recoger municiones en el campo de batalla para continuar disparando.
- **Efectos de Pelotas:** Cada tipo de pelota tiene efectos únicos:

    - **Pelotas Normales:** -20hp
    - **Pelotas de Fuego:** -30hp (Daño por quemadura: -5hp cada segundo por 3 segundos)
    - **Pelotas de Hielo:** -20hp (Ralentización: x0.7 por 3 segundos)
    - **Pelotas Eléctricas:** -25hp (Inmovilización por 1.5 segundos)
    - **Pelotas de Veneno:** -25hp (Daño por envenenamiento: -3hp cada segundo por 5 segundos)
    - **Pelotas de Curación:** +10hp
    - **Pelotas de Aturdimiento:** -20hp (Tiempo de aturdimiento: 3 segundos)
    - **Pelotas de Ceguera:** 0hp (Tiempo de cegado: 3 segundos)
    - **Pelotas de Fragmentación:** -50hp (Se fragmenta en 5 unidades: -10hp cada una)

<div id='mundo-juego' />

### 3. Mundo del Juego

<div id='historia' />

#### 3.1. Historia

En un mundo donde los deportes se han fusionado con la tecnología de combate, los jugadores se enfrentan en arenas deportivas especialmente diseñadas para determinar quién es el mejor atleta y guerrero. Los campeonatos son eventos masivos que atraen a espectadores de todo el mundo.

<div id='descripcion-mundo' />

#### 3.2. Descripción del Mundo

El mundo del juego es vibrante y colorido, lleno de estadios deportivos futuristas, cada uno con su propio tema y diseño único. Los escenarios incluyen campos de fútbol convertidos en arenas de batalla, canchas de tenis con trampas eléctricas y estadios de béisbol llenos de obstáculos dinámicos.

<div id='mapas-niveles' />

#### 3.3. Mapas y Niveles

- **Estadio de Fútbol:** Un campo de fútbol con amplias áreas abiertas y postes de gol que sirven como cobertura.
- **Canchas de Tenis:** Áreas pequeñas y cerradas con trampas eléctricas y redes que pueden bloquear los disparos.
- **Estadio de Béisbol:** Un gran estadio con bases y obstáculos móviles que cambian la dinámica del combate.

<div id='personajes' />

#### 3.4. Personajes

- **Atleta de Fútbol:** Especializado en velocidad y agilidad, puede disparar pelotas normales y de fuego.
- **Tenista:** Experto en precisión y disparos rápidos, usa pelotas eléctricas y de aturdimiento.
- **Beisbolista:** Fuerte y resistente, dispara pelotas de fragmentación y de veneno.

<div id='estilo-visual' />

### 4. Estilo Visual

<div id='diseno-personajes' />

#### 4.1. Diseño de Personajes

- **Atleta de Fútbol:** Un personaje ágil con uniforme de fútbol, colores brillantes y detalles caricaturescos.
- **Tenista:** Un personaje con ropa de tenis y una raqueta estilizada, con efectos visuales eléctricos.
- **Beisbolista:** Un personaje robusto con uniforme de béisbol, detalles oscuros y elementos intimidantes.

<div id='diseno-niveles' />

#### 4.2. Diseño de Niveles

Cada nivel está diseñado con una estética cartoon y detalles coloridos, presentando múltiples rutas, trampas interactivas y elementos dinámicos que reaccionan a las acciones del jugador.

<div id='puntos-clave' />

### 5. Puntos Clave

- **Narrativa Envolvente:** Una historia interesante que se desvela a través de diálogos y eventos en el juego.
- **Estilo Visual Único:** Gráficos en estilo cartoon con detalles modernos y vibrantes.
- **Mecánicas de Juego Innovadoras:**

 Combinación de elementos deportivos con disparos, habilidades especiales y efectos únicos de pelotas.
- **Explora y Descubre:** Mapas llenos de secretos y áreas ocultas que recompensan a los jugadores curiosos.
- **Sonido Dinámico:** Música y efectos de sonido que cambian según las acciones del jugador para una experiencia auditiva envolvente.
- **Desafíos y Puzles:** Variedad de desafíos, desde combates intensos hasta trampas ingeniosas.
- **Personajes Memorables:** Un elenco de personajes bien diseñados y desarrollados que enriquecen la historia y la jugabilidad.