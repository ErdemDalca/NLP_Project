<p align="center">
 <img width=1000 heigth=1000 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/GDDSCR3DTitulo.png"> <br>
</p>
LinkTree con los enlaces del proyecto:(https://linktr.ee/wildclawstudio)

# Índice
---

 1. [Introducción](#introducción)
    * [Concepto](#concepto)
    * [Historia y trama](#historia-y-trama)
    * [Propósito, público objetivo y plataformas](#propósito-público-objetivo-y-plataformas)
 3. [Mecánicas y elementos del juego](#mecánicas-y-elementos-del-juego)
    * [Descripción detallada del concepto de juego](#descripción-detallada-del-concepto-de-juego)
    * [Descripción de mecánicas de juego](#descripción-de-mecánicas-de-juego)
    * [Controles](#controles)
    * [Objetivo](#objetivo)
    * [Elementos del mapa](#elementos-del-mapa)
    * [Mapas](#mapas)
    * [Personajes](#personajes)
    * [Objetos, armas y power ups](#objetos-armas-y-power-ups)
 5. [Arte](#arte)
    * [Estética general del juego](#estética-general-del-juego)
    * [Referencias del arte Space Combar Rush 2D](#referencias-del-arte-space-combar-rush-2d)
    * [Concepts](#concepts)
    * [Modelos 3D](#modelos-3d)
 7. [Sonido](#sonido)
    * [Música de ambiente](#música-de-ambiente)
    * [SFX](#sfx)
 9. [Interfaz](#interfaz)
    * [Referencias de interfaz](#referencias-de-interfaz)
    * [Diseños de menús](#diseños-de-menús)
    * [Diagrama de flujo](#diagrama-de-flujo)
 13. [Monetización](#monetización)
     * [Modelo de negocio](#modelo-de-negocio)
     * [Roadmap](#roadmap)
     * [Información del usuario](#información-del-usuario)
     * [Mapa de empatía](#mapa-de-empatía)
     * [Modelo de caja de herramientas](#modelo-de-caja-de-herramientas)
     * [Modelo de canvas o lienzo](#modelo-de-canvas-o-lienzo)
     * [Modelo de monetización](#modelo-de-monetización)
     * [Tabla de productos y precios](#tabla-de-productos-y-precios)
 15. [Planificación y costes](#planificación-y-costes)
     * [Equipo humano](#equipo-humano)
     * [Estimación temporal del desarrollo](#estimación-temporal-del-desarrollo)
     * [Costes asociados](#costes-asociados)
     * [Hoja de ruta del desarrollo](#hoja-de-ruta-del-desarrollo)
 17. [Marketing](#marketing)
     * [Redes sociales](#redes-sociales)
     * [Porfolio](#porfolio)
 19. [Post mortem (lecciones aprendidas)](#post-mortem-lecciones-aprendidas)
     * [Trabajo individual realizado](#trabajo-individual-realizado)
         * [Anastasia Ihnatsenka Shakhova](#anastasia-ihnatsenka-shakhova)
         * [José Antonio González Mesado](#josé-antonio-gonzález-mesado)
         * [Jesús Bastante López](#jesús-bastante-lópez)
         * [Jorge Juan Xuclá Esparza](#jorge-juan-xuclá-esparza)
         * [Miguel Ángel Jiménez Montemayor](#miguel-ángel-jiménez-montemayor)
     * [Trabajo colectivo realizado](#trabajo-colectivo-realizado)
 20. [Control de Versionado](#control-de-versionado)

# Introducción
---
## Concepto
"Space Combat Rush" es un juego multijugador con vista cenital en el que dos o más jugadores se enfrentarán en batallas de naves espaciales en un campo de asteroides. Cada jugador controlará una nave y su misión será acabar con el resto de jugadores.
## Historia y trama
Con el avance de la tecnología y la ingeniería espacial, la humanidad se ha extendido por los vastos confines del cosmos. La población crece exponencialmente y, para subsistir, debe establecer colonias a través de la galaxia, en una constante búsqueda de nuevos y valiosos recursos para seguir esta expansión sin límites.

Pero estos tiempos de prosperidad no han llegado solo a las grandes empresas y naciones que gobiernan la Gran Expansión, como es denominado el proceso de colonización espacial; el espacio también es lugar de piratas y bandidos. Los grupos de saqueadores asedian el comercio en todos los sectores conocidos, y por ello, la UGE (Unión de la Gran Expansión), la asociación terrícola encargada de regular el tránsito y seguridad espacial a lo largo del Dominio, ha declarado la guerra a los piratas, movilizando toda su flota contra ellos con el objetivo de restablecer la ley.

Sin embargo, los bandidos no son su único enemigos; varias cultos a dioses antiguos del Infinito y civilizaciones perdidas del firmamento han surgido a lo largo del nuevo territorio. Con frecuencia, estos oscuros cultos secuestran inocentes para llevarlos a sus antiguos santuarios y sacrificarlos a sus divinidades. 

En este contexto, varios grupos de renegados han encontrado refugio en el borde exterior, formando sus propias colonias y construyendo grandes estaciones. En ellas nació Space Combat Rush, el deporte mortal más famoso y lucrativo del Dominio. Cada piloto lucha en la arena con su propia nave, símbolo de su ferocidad y testimonio de sus combates, dispuestos a jugarselo todo por el oro y la gloria.

¿Quién caerá?

¿Quién saldrá victorioso?

Las preguntas solo se contestan en la arena.

## Propósito, público objetivo y plataformas
Con este juego se buscará ocupar el tiempo muerto de cualquier jugador en momentos como un viaje en el metro, la espera del comienzo de una clase o similar. Principalmente nos centraremos en el público masculino entre las edades de 12 a 18 años, con posibilidad a adultos jóvenes entre los 18 y 25, y se subirá a los navegadores de Google Chrome, Edge y Mozilla Firefox para que tengan fácil acceso al juego.

# Mecánicas y elementos del juego
---
## Descripción detallada del concepto de juego
Space Combat Rush 3D se basará fuertemente en el juego ya creado previamente Space Combat Rush. Se podría considerar como la transferencia de la versión original a un mundo 3D; pero con algunas diferencias. El juego buscará destacar por su sencillez donde, a parte de los menús a través de los que puede navegar el jugador, solamente habrá una única pantalla de juego.

La pantalla de juego consistirá en un entorno cerrado (un mundo con límites) que simulará el espacio. Aquí el jugador podrá encontrar al enemigo al que tendrá que enfrentarse (el otro jugador con el que ha sido emparejado en un 1vs1, se replanteará en un futuro si aumentarlo a batallas por equipos) y elementos como meteoritos y debris espacial (elementos que el jugador podrá destruir disparándoles).

El usuario jugará en tercera persona desde una vista cenital controlando una nave. Esta nave se personalizará antes de empezar la partida, donde el jugador puede tanto escoger una nave con sus propias habilidades, como personalizar esa propia nave con clases de proyectiles o apoyos. Además, el jugador podrá hacer o uso de las skins básicas para la personalización o adquiriendo, con los pases de batalla, skins especiales. En un principio estas skins serán meramente estéticas, pero se reevaluará en el futuro si añadir efectos especiales que puedan tener algunas.

Una vez en partida, el objetivo del jugador es acabar con el enemigo. Para ello, debe destruir meteoritos y enemigos para conseguir experiencia; la cual usará para subir de nivel su nave y conseguir habilidades para poder acabar con su enemigo. A vista de futuro, se plantea la inclusión de boosters especiales que aparezcan en el mapa como drops con aviso para obligar una lucha más encarecida entre los jugadors.
## Descripción de mecánicas de juego
Mecánicas prepartida:
1. El jugador escoge un personaje/nave, la cual posee sus propias estadísticas y habilidades.
2. El jugador escoge una skin del personaje.
3. El jugador escoge una mejora de apoyo.
4. El jugador escoge una mejora de arma.

Mecánicas en partida:
1. La victoria de la partida consiste en ganar un mejor de 3 rondas.
2. Cada ronda el ganador es el jugador superviviente.
3. Cada ronda dura 60 segundos, tras ello se genera un aro de fuego que hace daño, el cual se va cerrando poco a poco hasta que un jugador muera
4. Los jugadores comienzan en extremos opuestos de la arena.
5. Los jugadores usan su arma para destruir al rival, los meteoritos distribuidos en la arena (ambas les dan experiencia) y los satélites que restauran vida al jugador.
6. La experiencia se traduce en subidas de nivel y este nivel, de cada jugador, se comparte entre rondas.
7. Las subidas de nivel aportan mejoras de estadísticas, desbloquean habilidades y desbloquean las mejoras elegidas en la pantalla prepartida.

## Controles
Para el movimieto de la nave, en versión dispositivo con teclado, se usarán WAD (donde W es para acelerar y AD es para el control de la dirección, no se puede volar hacia atrás). Para la versión en móvil se utilzan dos botones táctiles para girar a izquierda y derecha y un tercer botón para acelerar. 

En cuanto a los disparos, en versión ordenador se utilizará la barra espaciadora. En cuanto a la versión dispositivo táctil se dispone de un botón en la pantalla.

Ambas versiones soportan controles con mando, que utilizan el D-Pad para girar (botones izquierdo y derecho), botón "A" en mando de XBOX (boton inferior) para acelerar y botón "X" en mando de XBOX (botón izquierdo) para disparar.

Y, finalmente, para navegar entre las distintas pantallas, se utilizará el ratón para clickar sobre los distintos botones. En versión móvil se hará utilizando la funcionalidad táctil de esta o el mando.
## Objetivo
El objetivo en este juego es simple, conseguir matar a todo jugador al que te enfrentes para ascender en el ranking que se visualizará al terminar una partida. Se apelará a la competitividad de los jugadores para que busquen conseguir estar en el top entre todos los usuarios.

## Elementos del mapa
Los elementos del mapa cambian de posición cada ronda.

### Meteoritos
Los meteoritos son objetos distribuidos por el mapa que, al destruirlos, dan experiencia al que haya dado el disparo final.

### Satélites
El debris espacial son una pequeña cantidad de objetos distribuido por el mapa. Al hacerles daño regenera vida al jugador, y al destruirlo, da una curación mayor.

## Mapas
### Centro del Coliseo

Mapa básico del juego. Consiste en una arena circular con meteoritos y varios satélites distribuidos mapa.

La ambientación de la zona es una arena en medio de una gran estación espacial con una cupula espacial.

### Hangares
<img width=800 heigth=800 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/LayoutHangares.png">

### Generador de la Arena

<img width=800 heigth=800 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/LayoutGenerador.png">

## Personajes
Space Combat Rush 3D cuenta con varios personajes entre los que el jugador puede escoger para luchar. Cada uno de estos personajes cuenta con diferentes estadísticas, habilidades pasivas y habilidades activas.

### Ravager
Ravager es símbolo de velocidad, cuenta con una gran movilidad para emboscar a sus enemigos y escapar recibiendo el menor daño posible.

- **Pasiva.** Blindaje antikinético: no recibe daño de choque.
- **Activa.** Motores turbo: habilidad que no tiene tiempo de enfriamiento, sino que usa energía que se va consumiendo al usarla y se regenera con el tiempo. Al presionar avanzas más rápido que a velocidad normal.

### Cargo Queen
Cargo Queen es un personaje defensivo y de gran aguante. Es capaz de atacar y defenderse cuando es necesario, llevando el combate en sus propias condiciones.

- **Pasiva.** Experta en reparaciones: el debris espacial restaura más vida.
- **Activa.** Generador de escudo: genera un escudo horizontal delante de ella durante unos segundos, bloqueando todos los proyectiles que choquen con él. No puede disparar mientras usa esta habilidad.

### Pandora
Pandora es la elegida de la Plaga, y como tal debe conseguir la aniquilación de sus enemigos a cualquier coste. Es un personaje capaz de causar un daño devastador, pero debe saber cuando retirarse para no morir en el intento.

- **Pasiva.** Nave viviente: posee regeneración de vida pasiva.
- **Activa.** Rezo atroz: no tiene tiempo de enfriamiento. Al activarlo pasa a un estado en el que sus balas hacen más daño, pero pierde vida cada segundo. Al volver a usarlo vuelve al modo normal.

### Albatross
Albatross es una nave con un gran control en largas distancias, evita que sus enemigos se acerquen y exploten su poca resistencia mediante un gran daño desde lejos.

- **Pasiva.** Ejecutor: si el enemigo tiene menos de 30% de vida, sus proyectiles y habilidad le aplican más daño.
- **Activa.** Granada de tormenta: lanza una granada que estalla en un circulo de rayos que daña cada segundo que alguien está dentro.

### Ironsmith
Ironsmith posee poco daño a distancia; sin embargo posee un gran pode ren combate cercano gracias a la cabeza de martillo, aplastando a rivales cercanos.

- **Pasiva.** Cabeza de martillo: hace daño con la cabeza de martillo mientras rota.
- **Activa.** Martillo arrasador: hace un deslizamiento hacia atrás haciendo daño en el camino.

## Objetos, armas y power ups

**Componentes de arma**
- **Ametralladora:** Cañón con mayor cadencia de disparo.
- **Dobleyectil:** Cañón que dispara 2 proyectiles en vez de 1.
- **Lanzamisiles:** Cañón de baja cadencia de disparo que lanza misiles de gran daño.

**Componentes de apoyo**
- **Reductor:** reduce el recurso necesario que consume una habilidad un 10%.
- **Escudo:** incorpora un escudo que actua como vida adicional no recargable.
    

# Arte
---
## Estética general del juego
El juego buscará simular una estética arcade en 3D. Por lo que se apelará a una mezcla futurista/retro con modelos low poly. Buscaremos tener una mezcla de diseños que recuerden a los tiempos de antaño, pero con detalles de luces neón y elementos futurísticos para dar la sensación de que nos encontramos ante una sociedad más desarrollada de lo que fueron esos tiempos.
<p align="center">
 <img width=145 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/50e92bb3f19423b47d032f11a80fe288.jpg">
 <img width=200 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/raf%2C360x360%2C075%2Ct%2Cfafafa_ca443f4786.jpg">
 <img width=400 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/retrofuturyzm-5.jpeg"> <br>
</p>
<p align="center">
 <img width=200 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/thumbnail_8b978dc5-9927-441c-85ba-44224c1fe562.jpg.256x256_q85.jpg">
 <img width=200 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/77a7a10aca1740618fa4ad57e0c7eed9.jpg">
 <img width=355 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/scifi_spaceship_1_preview_5.jpg"> <br>
</p>

## Referencias del arte Space Combar Rush 2D
El juego original se diseñó para una estética pixelar apelando en su totalidad a los juegos retro del pasado. A continuación se podrá ver algunas imágenes de dicho juego y se pondrá el enlace al juego para poder probarlo.

<p align="center">
 <img width=400 heigth=400 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Capturas%20de%20Pantalla/Menu%20Principal.JPG">
 <img width=400 heigth=400 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Capturas%20de%20Pantalla/Pantalla%20Principal.JPG">
</p>
Link al GDD de Space Combat Rush:(https://github.com/JesusBL24/JeR-SCR)

Link al juego de Space Combat Rush: (https://tasiatas.itch.io/space-combat-rush)

## Concepts
Principalmente nos centraremos en los diseños de las naves, pero elementos del entorno como los meteoritos y el debris espacial también deberán ser diseñados. Así como los distintos boostes y escenarios.

A continuación, se presentan los diseños de las naves.

Diseño de la nave **RAVAGER**:
<p align="center">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/RavagerCD.png"> <br>
</p>

Diseño de la nave **ALBATROSS**:
<p align="center">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Albatross.png"> <br>
</p>

Diseño de la nave **CARGO QUEEN**:
<p align="center">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/CargoQueen.png"> <br>
</p>

Diseño de la nave **PANDORA**:
<p align="center">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/PandoraPA.png">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/PandoraInfeccionPA.png"> <br>
</p>

Diseño de otras naves múltiples:
<p align="center">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Concept_coloresNaves.png"> <br>
</p>

Seguidamente, se pueden visualizar dos diseños sencillos de los dos entornos importantes (ring de combate y hangar para personalizar la nave):
<p align="center">
 <img width=400 heigth=400 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/RingCombate.png">
 <img width=400 heigth=400 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Hangar.png"> <br>
</p>

## Modelos 3D
En este apartado se mostrarán las versiones 3D de los concepts para tener una clara comprensión del contenido visual dentro del juego.
<p align="center">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/AlbatrossAVATAR.png">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/CargoQueenAVATAR.png"> <br>
</p>
<p align="center">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/PandoraAVATAR.png">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/RavagerAVATAR.png"> <br>
</p>

Las skins que tienen siguen esta representación sencilla en la UI (son 3 skins por nave). Los 3 primeros son de Albatross (nave morada de los modelos 3D), los 3 siguientes son de Pandora (la nave roja con líneas blancas de los modelos en 3D), las 3 siguientes son de Cargo Queen (la nave negra con rallas amarillas) y las 3 finales son de Ravager (nave azul con rasguños rojos de los modelos 3D).
<p align="center">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/SkinsSymbols.png"> <br>
</p>

Durante el desarollo del juego, se han añadido elementos como una nueva nave (Ironsmith) y se han modificado y añadido skins por probelmas o la necesidad del juego. Estas nuevas modificaciones se pueden ver a continuación:

<p align="center">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/IronsmithAVATAR.png">
 <img width=600 heigth=600 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Avatares/TodasSkinsFinales.png"> <br>
</p>

# Sonido
Para el apartado sonoro del juego, se buscará que todos los elementos de sonido tengan coherencia dentro del tema espacial. Ello buscará transmitir las sensaciones del espacio para dar una mejor inmersión al jugador. Para ello, a continuación, se describen las prinipales melodías y los efectos sonoros planteados para el juego.

## Música de ambiente
   ### Menús
   - **Música de fondo:** Se utilizará una melodía suave y envolvente, inspirada en el estilo de la banda sonora de "Interestellar", para crear una atmósfera relajante y contemplativa. La música debe incluir elementos electrónicos y orquestales que inviten al jugador a explorar el menú sin prisas.

   ### In-game
   - **Música de fondo:** Durante las partidas, se reproducirá una música animada con un estilo de rock espacial. Esta música debe ser energética, con guitarras eléctricas y sintetizadores que transmitan una sensación de acción y aventura en el espacio. La mezcla de ritmos acelerados y melodías pegajosas mantendrá a los jugadores inmersos y motivados mientras compiten.

## SFX
   ### Interfaz
   - Sonido “pop” mecánico al pulsar un botón.
   - Efecto de sonido de ganar partida.
   - Efecto de sonido de perder partida.

   ### Naves
   - Sonido de propulsión al acelerar.
   - Sonido de destrucción de nave.
   - Sonido de colisión de nave con meteorito/muro/nave.
   - Sonido de disparo (dependiente del tipo de proyectil).
   - Sonido de colisión de disparo (dependiente del proyectil también).

   ### Meteoritos
   - Sonido de destrucción.

# Interfaz
---
## Referencias de interfaz
Aunque este juego se basa en su versión arcade, para adaptarlo al nuevo público y añadir el toque futurista que  buscamos en el concepto del juego en su versión 3D, las interfaces tomarán referencia de juegos con mayor tendencia a lo tecnológico-futurista. Sin embargo, buscaremos mantener la idea del arcade en cuanto a los colores utilizados; por lo que habrá una tendencia a añadir colores fosforitos y chillones.

Además, al ser un juego competitivo con la necesidad de tener buen manejo o control de la nave y la mayor velocidad posible para acabar con el enemigo, tomará influencias también de las interfaces de juegos de carreras. Algunas de estas referencias, de forma general, son las siguientes:

<p align="center">
 <img width=320 heigth=320 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/login-form-page-on-blue-background-technology-futuristic-interface-background-vector.jpg">
 <img width=210 heigth=210 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/sign-form-on-hud-futuristic-260nw-2341185149.jpg">
 <img width=360 heigth=200 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/blastonui24.png"> <br>
</p>
<p align="center">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/598f6625615359.57cc2076364ef.png">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ff34f1da872e07410f4bd1a0ef3f4743.jpg">
 <img width=300 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/z4dyiyu6amb71.jpg"> <br>
</p>

## Diseños de menús
Antes de diseñar los distintos elementos finales de los menús, se realizan unos concepts para visualizar de manera rápida y sencilla la navegación visual de cada una de ellas. Estos diseños son los siguientes:

<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/1.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/2.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/3.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/4.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/5.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/8.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/9.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/17.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/10.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/11.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/14.editado2.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/12.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/13.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/14.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=300 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/15.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/6.editado3.jpg"> <br>
</p>
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/7.editado3.jpg">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/17.editado3.jpg"> <br>
</p>

Tras estos primeros diseños, según van surgiendo necesidades, se rediseñan algunas pantallas. Principalmente la pantalla del menú principal donde se personaliza la nave y la pantalla del battle pass ya que no nos convencían los diseños.

<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/13-Modificada.png">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/6-Modificada.png"> <br>
</p>

Con ello, generamos su aspecto final y creamos la sprite sheet que usaremos en Unity para montar dichas interfaces. Esta spritesheet es representativa ya que se han añadido más elementos en la UI de las mostradas aquí.

<p align="center">
 <img width=1000 heigth=1000 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ConceptsInterfaceGDD-SCR3D/UI_SpriteSheet_ConFondo.png"> <br>
</p>

## Diagrama de flujo
Teniendo el diseño de las interfaces conceptuales, se diseña además cómo se pasa dentre las distintas pantallas. Para ello, creamos el siguiente flujograma.

<p align="center">
 <img width=100% heigth=100% src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Flujograma%20SCR3D.editado3.png"> <br>
</p>

# Monetización
---
## Modelo de negocio
Se plantea un modelo Freemium ya que daremos el juego con acceso gratuito para todos los jugadores. Sin embargo, para todo aquel que desee más contenido, se le dará la opción de poder optar a la compra de Battle Passes. En él, se podrá realizar colaboraciones con otras empresas para crear skins o elementos similares con los que se pueden publicitar estas empresas.

Además, se realizarán tornos bianuales de pago como eventos que mantengan la base de nuetra comunidad activa constantemente y fidelizada.
## Roadmap
En este apartado, en primer lugar, se presenta un diagrama visual inicial de cara al planteamiento de trabajo durante el desarrollo del producto. En él dividimos en los sectores de trabajo existentes en el equipo y las tareas mas importantes que engloban los paquetes de trabajo, además de indicar las fechas de duración de cada tarea.
<p align="center">
 <img width=100% heigth=100% src="https://github.com/jagonmes/Imagenes-JeR/blob/main/RoadmapDesarrollo.jpg"> <br>
</p>

Y, seguido a ello, presentamos un roadmap simplificado para visualizar el mantenimiento del juego en los próximos dos años para generar ganancias.
<p align="center">
 <img width=100% heigth=100% src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Roadmap2A%C3%B1osVistaCorrecto.jpg"> <br>
</p>

## Información del usuario
El usuario destinatario de nuestro juego tendrá las siguientes características:

  * Pertenece al segmento de edad entre los 12 y 18 años.
  * Son estudiantes.
  * Se apelará al género masculino principalmente.
  * Son personas con mucho tiempo libre.
  * Tienden a tener falta de socialización en persona.
  * Son competitivos.
## Mapa de empatía
Conociendo las características base de quienes serán nuestros principales jugadores, procedemos a estudiarlo más de cerca con un mapa de empatía.

<p align="center">
 <img width=1000 heigth=1000 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Mapa%20Empat%C3%ADa%20SCR3D_editado2.png"> <br>
</p>

## Modelo de caja de herramientas
Utilizando este modelo, construimos nuestra empresa en base a una serie de bloques y las relaciones existentes entre ellos. Esto nos permite visualizar la estructura general del funcionamiento de Wild Claw Estudio (específicamente basado en el juego de Space Combat Rush 3D).

<p align="center">
 <img width=1000 heigth=1000 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Caja%20de%20Herramientas%20SCR3D_editado2.png"> <br>
</p>

## Modelo de canvas o lienzo
Gracias al modelo de lienzo, podemos representar nuetra infraestructura orientada al producto de Space Combat Rush 3D de manera más detallada. Ello se puede visualizar en la siguiente representación gráfica:
<p align="center">
 <img width=1000 heigth=1000 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/ModeloLienzo.png"> <br>
</p>

## Modelo de monetización
Space Combat Rush se centrará en el modelo de Battle Pass (estos contendrán nuevas naves con skins distintas que puede coleccionar el jugador, pudiendo realizar colaboraciones con otras empresas que pagen por poner skins especiales en nuestro juego) y la generación de torneos bianuales con entrada de pago. Para poder conocer el nivel de éxito de nuestro juego, se establecen unas métricas para saber en qué situación se encuentra nuestro producto:

- **Caso pesimista:** se da una base de jugadores pequeña. Por lo que únicamente se gana lo suficiente para recuperar los costes y mantener los servidores.
- **Caso normal:** hay una base de jugadores amplia. Con ello se consiguen ganancias suficientes para el mantenimiento del juego y poder seguir desarrollándolo (o permitir costear un nuevo proyecto).
- **Caso optimista:** la base de jugadores es extensa. El juego consigue ser uno de los populares del momento pudiendo llegar a vender el propio juego a otros interesados.

## Tabla de productos y precios
| Producto | Precio |
|--------|-------|
| Juego | Gratuito|
| Battle Pass | 10€ cada 3 meses |
| Torneos Bianuales | 3€ cada 6 meses |

# Planificación y costes
---
## Equipo humano
El equipo constará de 5 miembros core. Estos serán los siguientes; junto al departamente al que pertenecen:

  * **Miguel Ángel Jimenez Montemayor**: departamentos de arte y diseño.
  * **Jesús Bastante López**: departamentos de diseño y programación.
  * **Jorge Juan Xuclá Esparza**: departamentos de programación y música.
  * **Anastasia Ihnatsenka Shakhova**: departamentos de arte y diseño.
  * **José Antonio González Mesado**: departamento de programación.

Independientemente del departamento al que pertenezca cada uno y de su especialización, se buscará la participación en todos los aspectos del proyecto tanto de opinión como en las ayudas que se necesiten dependiendo de las necesidades del proyecto en el momento.
## Estimación temporal del desarrollo
La duración del desarrollo del proyecto tiene una estimación de un periodo de 3 a 4 meses; incluyendo un tiempo añadido para incoventientes y posibles arreglos de errores.
## Costes asociados
El coste del desarrollo se estima en unos **50.000€**. Esto equivaldría a 4 meses de sueldo de los miembros del equipo (1.400€ brutos más las cotizaciones, aproximadamente 37.500€), unos 5.000€ para el hardware y software, 2.500€ para los servidores y otras infraestructuras, y otros 5.000€ para la publicidad. Véase la siguiente tabla para tenerlo de forma más visual:

| Elemento | Coste |
|----------|-------|
| Equipo 5 personas | 37.500€ |
| Hardware y software | 5.000€ |
| Servidores y otras infraestructuras | 5.000€ |
| Publicidad | 5.000€ |
| **Total** | **50.000€** |

# Marketing
---
En este apartado se detalla el trabajo de cara a la publicidad de la empresa y el juego que acontece: Space Combat Rush 3D. Uno de los elementos principales a tener en cuenta es la imagen que buscamos transmitir; por un lado de la propia empresa Wild Claw Studio y, por otro, del juego.

Comencemos por la imagen de la empresa. Como empresa, contamos con una serie de valores que siempre queremos que se asocien a nosotros: familia, fuerza, determinación y libertad. Por ello, una de las claves para diseñar nuestra huella, es comprender qué colores nos vamos a asociar y las figuras o formas predomintantes.

Nuestros colores principales serán el rojo, el negro y el blanco, combinados con una mezcla equilibrada de formas redondeadas y picudas como base de nuestra esencia. En cuanto a los colores, buscamos un contraste muy marcado entre el blanco y el negro: el negro aporta elegancia y estabilidad a la imagen, mientras que el blanco proporciona legibilidad y transmite pureza o inocencia. Por su parte, el rojo añade un toque de poder, pasión y atracción visual.

Estas tonalidades, combinadas con las formas (por ejemplo, en el logotipo), evocan diferentes conceptos. Las letras redondeadas, como la D, la C o la O, que son casi círculos perfectos, sugieren niñez, suavidad y amabilidad. Sin embargo, las serifas de estas mismas letras aportan elegancia gracias a sus trazos terminados, mientras que el zarpazo detrás de las letras refuerza la idea de poder y agresividad.

Con esta combinación, transmitimos que somos fieros al proteger lo que es nuestro y fuertes al luchar por lo que queremos. Sin embargo, al igual que los animales —con la zarpa como símbolo identificativo de nuestra marca—, cuidamos de nuestra familia y, por ende, de nuestro producto.

Además, los daños visibles en las letras, provocados por el zarpazo, reflejan que somos un equipo que siempre busca superarse a sí mismo, sin temor a salir de nuestra zona de confort y explorar nuevos caminos. Tal como una mariposa que se transforma al salir de la crisálida, nosotros evolucionamos constantemente para alcanzar nuevas metas.

Esta filosofía queda reflejada en el logotipo de nuestra empresa, que podéis ver a continuación:

<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/WildClawLogo2.png"> <br>
</p>

Toda esta idea se transmite a nuestra pagina web y todas nuestras redes sociales cuando hablamos de nosotros.

En cuanto al propio juego, se trata de un juego de naves inspirado en el clásico arcade Asteroids, pero renovado con una estética 3D más actual. El diseño se centra en ofrecer una gran libertad de personalización a los jugadores, así como partidas cortas y dinámicas. Por ello, la imagen que buscamos transmitir es la de un juego intenso, rápido y emocionante.

La estética del juego es futurista, limpia y minimalista, con una paleta de colores basada en negro, azul y rojo como principales. Estos colores están presentes en las dos naves más representativas del juego: Pandora (roja) y Ravager (azul). El negro actúa como contenedor y base para todos los demás colores (similar a la esencia visual de la empresa). Por otro lado, los tonos azules metálicos y los rojos intensos aportan una sensación de futurismo, agresividad y dinamismo, elementos que reflejan perfectamente la esencia que queremos evocar con este proyecto.

Además, queremos que este juego sea percibido como accesible y atractivo para todos los públicos, especialmente dentro de nuestro rango de edad objetivo (12-18 años). Para reforzar esta percepción, hemos elegido una tipografía de estilo "pizarra" (chalky/gredoso) para la presencia visual inicial del juego. Este tipo de letra transmite cercanía y un aire juvenil, evocando recuerdos de pizarras antiguas y escritura con tiza.

En contraste, dentro del propio juego, las tipografías utilizadas tienden a ser más impactantes y futuristas, alineándose con la estética de expansión y guerra galáctica. La letra de tiza se reserva exclusivamente para atraer a los jugadores y transmitirles la sensación de que son bienvenidos, mientras que las tipografías futuristas refuerzan la experiencia inmersiva de tomar el control de naves espaciales y asumir decisiones importantes.

Entendida la imagen que deseamos proyectar tanto para la empresa como para el juego, procedemos a analizar el trabajo realizado en los apartados de redes sociales y portfolio.

## Redes sociales

De cara a las redes sociales, hemos establecido un plan de publicación mínimo de dos posts semanales, los martes y los sábados. Aunque sabemos que los lunes y jueves suelen ser los días con más visualizaciones, priorizamos la calidad del contenido y el tiempo necesario para producirlo en paralelo con el desarrollo del juego. Las publicaciones se programan en horarios cercanos al mediodía y la tarde, considerando que las horas pico de actividad suelen ser las 3 p.m. y las 8 p.m.

Además, hemos implementado la Estrategia de Objetivos SMART, la cual detallamos a continuación:

- **Specific:** nuestro objetivo es construir una base mínima de jugadores para garantizar partidas fluidas en línea. Para ello, buscamos que al menos 50 personas visualicen el juego, aumentando así las probabilidades de coincidencias entre jugadores. Asimismo, buscamos incrementar la cantidad de seguidores en redes sociales en al menos un 5%, un objetivo asequible considerando que somos una empresa indie en crecimiento.
- **Measurable:** medimos los resultados utilizando las métricas disponibles en Instagram e Itch.io, y evaluamos el progreso de la siguiente manera:
  - **Instragram:** hemos registrado un incremento del 60% en el número de seguidores, pasando de 36 seguidores iniciales a 58 seguidores tras la campaña del juego. En cuanto a las visualizaciones, alcanzamos una media de 216 visualizaciones por publicación, con picos que llegan a las 886 visualizaciones.
  - **Twitter/X:** reconocemos que nuestra presencia en esta plataforma ha sido limitada, con poca interacción con el contenido. En consecuencia, hemos decidido enfocar nuestros esfuerzos en Instagram, mientras evaluamos estrategias para mejorar nuestra presencia en Twitter/X de cara al futuro.
  - **Itchi.io:** la plataforma ha mostrado un aumento de interés, con picos notables asociados a las publicaciones de nuevas versiones. No obstante, se detecta una menor interacción posterior al lanzamiento final del juego, probablemente debido a la irregularidad en las campañas de marketing posteriores. Este problema podría resolverse con una dedicación exclusiva al marketing, algo que consideraremos al crecer como empresa en un futuro. Estas estadísticas se pueden ver a continuación:
 
<p align="center">
 <img width=500 heigth=500 src="https://github.com/jagonmes/Imagenes-JeR/blob/main/Captura%20de%20pantalla%20(133).png"> <br>
</p>

- **Achievable:** este proyecto fortalece nuestro posicionamiento como desarrolladores de videojuegos interesantes y comprometidos con la experiencia de los jugadores. Todos nuestros enlaces oficiales (a otros juegos, YouTube y nuestra página web) están disponibles en el perfil de Instagram y nuestra página web, facilitando el acceso a nuestros contenidos. También hemos promocionado el Discord del juego mediante QR, con la intención de adaptarlo en el futuro a un servidor de empresa.
- **Timely:** hemos establecido plazos claros para la promoción del juego, publicando un mínimo de dos veces por semana. Los posts incluyen avances del proyecto y presentaciones de nuestra comunidad interna (nuestros integrantes), un aspecto esencial para reflejar los valores de nuestra empresa. Esto nos ha permitido, en un plazo relativamente corto, aumentar el número de seguidores y el alcance de nuestras cuentas.

De esta manera, hemos logrado un incremento significativo de nuestra presencia en redes sociales, tanto para el juego como para la empresa. Sin embargo, también identificamos áreas con menor impacto, como Twitter y YouTube (únicamente usado actualmente para comunicados importantes como trailers). Esto nos proporciona una dirección clara sobre las áreas a mejorar como empresa.

## Porfolio
De cara al portfolio, buscábamos una página web simple y atractiva que reflejara la imagen de la empresa descrita al inicio de esta sección. Por ello, los colores empleados son siempre negro, blanco y rojo. La tipografía utilizada (sin serifas) difiere de la de nuestro logotipo, ya que está demostrado que las serifas dificultan la legibilidad y aumentan el tiempo de lectura. Nosotros buscamos transmitir que somos una empresa ágil, capaz de adaptarse rápidamente. No obstante, la tipografía sigue siendo formal y con un estilo de letras redondeadas. Además, hemos añadido pequeños símbolos, como líneas con estrellas, para reforzar esa sensación de niñez y amabilidad.

La estructura definida para el portfolio consta de dos páginas HTML principales: una para la página principal y otra (o varias en el futuro) para el contenido de lectura. De esta manera, se diferencia claramente el contenido relacionado con la empresa del relacionado con el juego que estamos desarrollando actualmente.

Las secciones elegidas para mostrar son: Noticias, Portfolio, Nuestro Equipo y Sobre Nosotros. La primera tiene como objetivo generar interés por el juego actual mientras se lleva a cabo su campaña de publicidad (más adelante, se valorará la opción de moverla a otro lugar). La segunda sección está destinada a informar al jugador sobre los juegos que tenemos como empresa, mostrando pequeñas imágenes o vídeos de cada juego, junto con descripciones para que el jugador sepa de qué trata cada uno, además de un enlace para su descarga. La tercera sección, Nuestro equipo, permite conocer a cada integrante de la empresa y refleja que nos cuidamos como una familia, razón por la cual esta sección es tan importante. Por último, la sección Sobre nosotros refuerza la sensación de equipo, ya que no hablamos de cada integrante por separado, sino de la empresa como un grupo unido.

Otro elemento visual clave que hemos incorporado es el banner con pequeños fragmentos de nuestros juegos. Esta idea la hemos tomado como referencia de las páginas web de empresas reconocidas y consolidadas, como Guerrilla Games. Como empresa emergente, es fundamental realizar un estudio de mercado y comprender qué herramientas y estrategias ya funcionan. Una página visualmente atractiva y sencilla, como la de Guerrilla Games, es una de esas herramientas clave.

Finalmente, en cuanto al contacto, hemos decidido, por ahora, permitir el acceso a todas nuestras redes sociales, pero no al correo empresarial. Esto se debe a que, en primer lugar, queremos centrarnos en establecer una imagen adecuada de la empresa, evitando mensajes no deseados (como trolls o spam). Y ya, una vez consideremos que es el momento adecuado, añadiremos el correo empresarial en el footer de la página.

Además, es importante resaltar que buscamos ser una empresa más internacional. Por ello, nos hemos centrado en comunicar todo en inglés. Sin embargo, durante el próximo año, planeamos añadir el español y anunciarlo a todos nuestros seguidores como parte de una campaña titulada "Nuestras raíces". De esta forma, queremos que nuestros usuarios y seguidores vean que estamos orgullosos de dónde venimos y del camino que hemos recorrido, para inspirarlos con nuestra historia.

# Hoja de ruta del desarrollo
---
A continuación se detallan las fechas estimadas.

| Fecha | Información |
|-------|-------------|
| 23/09/2024 | Inicio del proyecto |
| 14/10/2024 | Inicio del desarrollo del prototipo |
| 27/10/2024 | Entrega del primer prototipo jugable |
| 24/11/2024 | Entrega de la beta con todos los sistemas del videojuego funcionales |
| 08/12/2024 | Entrega de la versión gold master |
| 18/12/2024 | Lanzamiento del juego y del primer battle pass |
| 01/04/2025 | Lanzamiento del segundo battle pass |
| 15/06/2025 - 30/06/2025 | Primer Torneo de SCR 3D |
| 01/07/2025 | Lanzamiento del tercer battle pass |
| 01/10/2025 | Lanzamiento del cuarto battle pass |
| 15/12/2025 - 31/12/2025 | Segundo Torneo de SCR 3D |
| 01/01/2026 | Lanzamiento del quinto battle pass |
| 01/04/2026 | Lanzamiento del sexto battle pass |
| 15/06/2026 - 30/06/2026 | Tercer Torneo de SCR 3D |
| 01/07/2026 | Lanzamiento del séptimo battle pass |
| 01/10/2026 | Lanzamiento del octavo battle pass |
| 15/12/2026 - 31/12/2026 | Cuarto Torneo de SCR 3D |

# Post mortem (lecciones aprendidas)
---
## Trabajo individual realizado
### Anastasia Ihnatsenka Shakhova
#### Versión Alfa
Mi trabajo ha consistido en generar el matrial audiovisual para las redes sociales, el control de calidad y la estructura del gdd, el control del aspecto final de la página web, la creación de algunos concepts de naves y el diseño inicial de las interfaces.

Considero que he podido plasmar bien la estética que buscábamos del juego. Sin embargo, he de admitir que ha habido fallos de comunicación donde no he comprendido quién formaba parte del equipo de arte a gestionar o ciertos elementos de funcionalidad del juego para generar los diseños de las interfaces y se ha tenido que subsanar cuanto antes.

#### Versión Beta
Durante el desarrollo de la beta mi trabajo ha sido la generáción de todo el diseño final de la UI (se completarán los botones que falte para la Gold), el modelado y la texturización del entorno principal del juego (ring y assets para poblar el escenario como los materiales PBR de los meteoritos y el debris espacial), el texturizado de la nave Pandora y Ravager junto al apoyo en bakeo de las texturas de las naves Cargo Queen y Albatross, he estado generando el contenido para las redes sociales y he actualizado la página web y el itchiio con la nueva carátula del título modelado, texturizado y renderizado en 3D con postproceso.

Como cosas a cambiar considero que debo probar más las cosas, previo a su subida al github, ya que a veces se me pasa probar todo para ver si mis cambios, al subir los elementos visuales al juego y ponerlos a disposición de los programadores, han afectado a algo.
#### Versión Gold
En la versión Gold mi trabajo ha sido principalmente la de dar apoyo en los elementos artísticos que surgieran de última hora. Entre ellos se incluye el pintado de una nueva nave (Ironsmith) con sus dos skins, nuevas interfaces necesarias (como la pantalla del lore de cada nave y la de ajustes), ajustes de UI de última hora (sticker para el botón de battle pass, modificación del color de la barra de XP, etc) y arreglos de elementos del entorno (nuevo ring más ancho, menor peso en todas las texturas sin pérdida de calidad, nuevas texturas para los satélites...). Adicionalmente he estado editando el trailer para mejorarlo, editando la página web y a cargo de generar material para las redes sociales.

Considero que en esta entrega he trabajado de manera correcta y aunque ha habido pequeños malentendidos de cara a lo que me pedían mis compañeros, han sido errores mínimos que se han arreglado rápido y no han afectado al desarrollo de esta versión. Considero que hemos trabajado todos muy bien como equipo esta vez; teniendo mucha comunicación y feedback constructivo que nos hemos ido dando. Además de haber compartido conocimiento entre nosotros de las áreas que nos interesaban pero que unos no sabían de ello mientras otros sí.

### José Antonio González Mesado
#### Versión Alfa
Me he encargado fundamentalmente de la infraestructura de red, la lógica de la partida y los controles. En menor medida he revisado y parcheado las funcionalidades de movimiento y disparo de la nave, así como el funcionamiento y diseño de las interfaces.
 
Esta forma de trabajar me ha permitido trabajar más rápido en ciertas áreas, pero debido a la falta de comunicación se han tenido que ir adaptando distintas partes para que se diera un correcto funcionamiento del conjunto.

Para las siguientes iteraciones del proyecto habría que mejorar la comunicación o definir mejor las cosas antes de ponerse a trabajar.

#### Versión Beta
Me he encargado fundamentalmente de la lógica de conexión y desconexión entre cliente y servidor, la lógica de la partida y la gestión de los usuarios, su historial y la persistencia de dichos datos. En menor medida he revisado y parcheado las funcionalidades de movimiento.

Esta forma de trabajar me ha permitido trabajar sin interferir en otras áreas del desarrollo.

Para las siguientes iteraciones del proyecto habría que definir en piedra los objetivos, expectativas y realidad del proyecto antes de ponerse a trabajar.

#### Versión Gold
Me he encargado fundamentalmente de mejorar la lógica de conexión y desconexión entre cliente y servidor, también me he encargado de la implementación de un servidor público al que se puede acceder sin necesidad de introducir un código. En menor medida, he arreglado bugs varios y he aumentado la fiabilidad de la gestión de los datos de usuario.

Esta forma de trabajar me ha permitido trabajar sin interferir en otras áreas del desarrollo.

Para las siguientes iteraciones del proyecto habría que definir mejor los objetivos finales, pero no ha habido complicaciones mayores en esta iteración.

### Jesús Bastante López
#### Versión Alfa
Me he encargado del game design; la programación proyectiles, la barra de vida, la experiencia y elementos varios sobre la partida; he sido coresponsable de las redes sociales y he ayudadado en la sección del portfolio en la página web.

Aunque se ha mejorado la idea principal del juego a lo largo de esta iteración, me ha faltado comunicación dentro del equipo y el GDD. Además de definir mejor las especificaciones, pues esto ha llevado a confusiones a la hora de trabajar e irregularidades en diferentes secciones. 

Por otra parte, se ha conseguido implementar la gran mayoría de ideas; por lo que, en cuanto a trabajo realizado se refiere, ha sido correcto.

#### Versión Beta
Me he dedicado a redes sociales, específicamente X y texto; diseño de mecánicas, diseño de mapas e implementación de scripts varios enfocados en UI y elementos propios de la partida.

Durante el desarrollo de la Beta del juego se ha mejorado mucho el ritmo de trabajo en el proyecto, aunque seguimos cometiendo errores varios en cuanto al ajuste al tiempo límite.Y en cuanto a la comunicación entre el equipo, hemos conseguido que toda la información vital este al alcance de todos los miembros. No obstante, es cierto que me ha faltado comunicar algún detalle que ha ocasionado un demora o tiempo perdido. Seguiremos, y yo personalmente, mejorando las habilidades de comunicación y especificación.

Aunque el juego ha mejorado mucho y, en general, hemos conseguido los objetivos establecidos, ha faltado tiempo para testeo de balanceo. Intentaremos conseguir gente para que pruebe la beta y solucionar de esa forma el error.  En cuanto a las mecánicas, todo el juego ha mejorado mucho y estoy orgulloso de como marcha el proyecto, falta ver la recepción de los jugadores.

En redes sociales, no hemos conseguido un buena recepción en la plataforma X, por lo que tendré que trabajar más en hacer que la cuenta sea más atractiva y llamar a más usuarios.
#### Versión Gold
Me he dedicado a redes sociales, específicamente X y texto; diseño de mecánicas, diseño del mapa e implementación de scripts varios enfocados en UI y elementos propios de la partida.

Durante el desarrollo de la Golden el ritmo de trabajo se ha mantenido en buen nivel, todos hemos aportado un gran esfuerzo. Sin embargo, debido a la cantidad de tiempo que le he dedicado a juego en sí, no he podido dedicarme a mejorar la cuenta de X. Además, debo intentar mejorar mi capacidad de resolución de errores en código; ya que esto me ha tomado mucho tiempo.

En cuanto a la comunicación entre el equipo, no han surgido errores durante esta iteración, lo que cuenta como una gran victoria para el equipo entero.

Finalmente, respecto al juego, hemos sabido tomar el feedback de nuestros multiplos testers y mejorar el producto. Como game designer, he tenido que tomar algunas decisiones de diseño para intentar adpatar el juego a la mayoría, pero ya era muy tarde para cambiar el tipo de movimiento sin que esto supusiera un lastre muy gordo.

### Jorge Juan Xuclá Esparza
#### Versión Alfa
Para esta entrega, he hecho el modelo 3D de la primera nave y he programado el control de esta en ordenador, el matchmaking, la funcionalidad de la pestaña de personalización y el funcionamiento de los proyectiles básicos. También he escrito en el GDD el apartado de música y sonido, y en la página web del portfolio he hecho el footer.

Creo que del trabajo realizado, se mantendrá para futuras entregas tanto el modelo de la nave como lo escrito en el GDD y la página web. Sin embargo, a nivel de programación, tendremos que hacer cambios para mantener el código más limpio, organizado y mejorar el funcionamiento de las mecánicas. Por ejemplo habrá que cambiar los controles de la nave, los cuales se retocarán para que sean más cómodos y suaves
#### Versión Beta
Tal y como se dijo al final de la entrega anterior, para la beta he refactorizado gran parte del código hecho en la alfa para facilitar la implementación de las mecánicas nuevas. También he implementado la funcionalidad básica de las habilidades, los objetos de apoyo y la elección de skins. Además he hecho el modelo 3D de una nave más, las dos canciones que salen en el juego y he editado los distintos SFX.

Es posible que para la próxima entrega haya que volver a estructurar algunas partes del código para optimizar el juego, además de añadir una sección de ajustes y un tutorial. Pero creo que prácticamente todo lo que hemos añadido se mantendrá para la última entrega, a excepción de algunas texturas.
#### Versión Gold
En esta entrega final, he creado todos los VFX del juego y los he implementado para que funcionen tanto en Windows como en WebGL. También he corregido varios bugs, he programado el anillo de fuego que aparece al final de cada ronda, he ajustado el movimiento de las naves y he programado la funcionalidad del menú de ajustes. Además, he modelado y programado una nueva nave para el juego y he participado en el testing para balancear las mecánicas.

Lo que más me ha costado ha sido desarrollar el sistema de VFX, ya que inicialmente pensaba que los Visual Effects de Unity eran compatibles con WebGL, lo cual no era el caso. A pesar de ello, considero que el juego ha mejorado significativamente en estas semanas, tanto en el apartado artístico como en el mecánico. Creo que hemos logrado un muy buen resultado y que es un proyecto con potencial para seguir desarrollándose.

### Miguel Ángel Jiménez Montemayor
#### Versión Alfa
Para esta entrega, me he encargado principalmente de realizar varios conceptos de naves; además de aportar mis datos para la página web e ideas para el pase de batalla y otras interfaces. En las siguientes fases, procederé a desarrollar los modelos 3D basados en estos conceptos.

Considero que necesito mejorar mi organización para las próximas etapas, lo cual me permitirá obtener mejores resultados. Me hubiera gustado tener al menos un concepto más pulido y uno o dos modelos completos en esta entrega. Para la siguiente fase, intentaré completar dos naves por semana y pulir mis concept art.

#### Versión Beta
Para esta entrega, me he encargado principalmente en modelar y texturizar las naves Albatross y la Cargo Queen.

Durante esta etapa considero que me ha faltado una mejor comunicación con el equipo. Además, he tenido errores al intentar texturizar en blender por primera vez y al importar esas texturas en Unity de manera errónea haciendo que se atrase el trabajo de mis compañeros. Para la Golden no cometeré los fallos que he tenido en esta versión para conseguir el resultado que desean mis compañeros.
#### Versión Gold
En esta entrega, me he enfocado principalmente en corregir las texturas de Albatross Militar y Cargo Queen Ambulance. Durante esta etapa, he prestado especial atención a los problemas relacionados con las skins, esforzándome por solucionarlos de manera rápida y eficiente.

Uno de los desafíos que he enfrentado ha sido gestionar ciertas controversias relacionadas con el diseño de las skins. Por ejemplo, desconocía que el uso de estrellas rojas podría infringir las normativas del copyright de la Convención de Ginebra. Además, el incluir una calavera en la bandera española podría generar conflictos.

Para futuros proyectos, seré más cuidadoso al diseñar skins, verificando previamente si los elementos que deseo incorporar si son viables o si será necesario considerar alternativas.

## Trabajo colectivo realizado
#### Versión Alfa
Como equipo hemos sido capaces de completar la alfa incluyendo la funcionalidad base del juego para conseguir el flujo principal de este siendo, además, la primera vez en crear un juego multijugador desde cero por completo. Ello incluye toda la programación referente a la batalla interna del juego y las interfaces necesarias para acceder a esta. Además, hemos conseguido pulir la idea del juego que queremos y comprender la dirección que llevará este proyecto.

Por primera vez en esta carrera hemos tenido un problema de comunicación que hemos notado en el equipo y que ha afectado al desarrollo del proyecto. Por suerte, hemos comprendido este fallo y hemos conseguido empezar a arreglarlo justo antes de la entrega del primer prototipo. Ello implica que para las siguientes entregas nos esforzaremos más de cara a mantener una comunicación más abierta y preparar una mejor planificación previa antes de comenzar cada uno de los prototipos siguientes.

#### Versión Beta
Durante el desarrollo de la Beta del juego se ha conseguido mejorar considerablemente el juego, aunque quedan elementos por pulir que se completarán en la Gold.

Nuestro juego ha aumentado en su complejidad con las estadísticas de las naves y el método de combate. Además de tener un aspecto visual más atractivo. La actividad del marketing se ha seguido llevando de forma regular (tal como postear en las redes sociales) y se ha ido informando a los jugadores de los avances.

Si bien es cierto, el marketing podría haber sido mejor orientado a presentar esos avances. Y, de cara a la siguiente entrega, hay que pulir tanto el aspecto visual como algunos elementos de funcionalidad.

El juego, actualmente, se ha modificado también de tal forma que se pueda tener servidores privados para poder jugar con amigos. Algo que no teníamos en cuenta previamente y que, estudiando el público destino, hemos visto necesario para que estos pueda tener batallas entre amigos sin la necesidad de jugar con personas externas y donde hay pocas probabilidades de hacer match cuantos más jugadores hayan.

Seguimos ante un producto que es más de nicho y es algo que juega en desventaja nuestra. Sin embargo, al mismo tiempo, para estos jugadores, tener un juego antiguo puesto en una estética más actualizada puede resultar interesante y llamativo. Por lo que se hará una campaña publicitaria en las redes sociales antes de subir la Gold donde buscaremos atraer más a los jugadores de este nicho.

#### Versión Gold
Durante la Gold, el equipo ha logrado avances significativos en el desarrollo del juego. Uno de los mayores cambios ha sido la migración a URP, que permitió la adición de VFX. Aunque surgieron fallos con esto en un principio, como la falta de soporte en WebGL de dichos VFX, se logró implementar una solución efectiva utilizando spritesheets, lo que dio una mejora visual al juego. Además, se habilitó un servidor público funcional, permitiendo a los jugadores disfrutar de partidas multijugador sin la necesidad de configurar servidores privados, lo que ha mejorado la accesibilidad al juego. También se realizaron ajustes en el balanceo de controles y ataques, junto con otras modificaciones visuales, para garantizar una experiencia más equilibrada y atractiva.

El equipo, durante este periodo, ha conseguido generar una cultura interna buena, generando una sensación de familia dentro del equipo. Compartimos nuestros logros y nos apoyamos en los momentos más difíciles, lo que fue fundamental para superar obstáculos y mantener la motivación. Esta colaboración nos ha permitido no solo avanzar en el desarrollo del juego, sino darnos más unidad como empresa y ayudarnos a mejorar entre nosotros.

Actualmente, el juego se encuentra listo para el público objetivo. Destaca al dar una amplia personalización y variedad en las estrategias de juego, lo que permite rejugabilidad y que los jugadores lo adapten a sus preferencias. La estética del juego combina el arcade Asteroids con un diseño modernizado y más atractivo, dando una mezcla entre nostalgia y frescura. Aunque el producto está enfocado a un nicho específico, las partidas rápidas y cortas, junto con su atractivo visual, lo hacen ideal para un público más amplio, incluyendo tanto jugadores casuales como competitivos.

A partir de ahora, se pondrán todos los esfuerzos en la promoción del juego a través de las redes sociales. Se tratará de generar contenido atractivo y dinámico para captar la atención de potenciales jugadores y generar interés en probar el juego. Se busca no solo atraer usuarios nuevos, sino mantenerlos gracias a la competitividad y de poder jugar el juego en cualquier tiempo muerto del día a día.

En resumen, consideramos que con esta versión del juego tenemos una alta probabilidad de tener un juego que guste al público y, por ende, un producto que pueda generar beneficios. Además de que ha servido para ser un juego a través del que, el equipo, ha sido capaz de aprender mucho de cómo gestionar un proyecto mucho más amplio e ir paso a paso hasta llegar a la meta final.


# Control de Versionado
-----------------------
| Versión | Trabajo |
|-------|-------------|
|  0.1.0 | Implementada la infraestructura de red, pueden conectarse dos clienteso |
|  0.2.0 | Implementada una primera versión de las interfaces |
|  0.3.0 | Implementado el movimiento y los atributos de las naves |
|  0.4.0 | Implementado comportamiento de los proyectiles |
|  0.5.0 | Implementada la lógica de la partida, puede jugarse una partida de principio a fin |
|  0.6.0 | Implementados controles táctiles y con mando |
|  0.7.0 | Implementado el comportamiento de los meteoritos |
|  0.8.0 | Implementada una versión funcional del mapa de juego |
|  0.9.0 | Implementado el sistema de nivel de las naves en la partida |
|  0.10.0 | Implementada una primera aproximación a las interfaces de personalización y partida |
|  1.0.0 | Refactorización del código |
|  1.1.0 | Implementadas todas las habilidades de la nave |
|  1.2.0 | Implementación de los apoyos |
|  1.3.0 | UI y mapa rehechos |
|  1.4.0 | Implementación de nuevos niveles de mejora de armas y habilidades |
|  2.0.0 | Cambio del motor de renderizado a URP y actualización de la UI |
|  2.1.0 | Introducción de Aerosmith como nueva nave |
|  2.2.0 | Mejora de las habilidades |
|  2.3.0 | Introducción de efectos visuales en la versión de WebGL|
