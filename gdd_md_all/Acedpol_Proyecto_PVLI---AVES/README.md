# AVES - Alfred Hitchcock film "The Birds" inspired videogame
 > EN: This will be the proyect for PVLI, whose proyect is a Phaser 3 implementation, in which we will use JavaScrypt, HTML5, CSS and JSON files. 
 
 > SP: Este repositorio está dedicado al proyecto de PVLI, cuyo proyecto será una implementación de Phaser 3, en el cual se usarán archivos de tipo JavaScrypt, HTML5, CSS y JSON.
 ___
 #### Proyecto desarrollado por: _WAID GAMES_
 ![Pantalla inicio][portada]
 ___
 #### IMPORTANTE:
 - En la carpeta **_videojuego_** se encuentran los archivos que componen el videojuego.
 - Contiene su propio _readme_ con información relevante para su uso.
 - En la carpeta **_assets_** se encuentran los archivos que componen el videojuego.
 
 ###### website: [visitar web][WEB]
 
 ###### Pivotal Tracker: [visualizar en la web][Pivotal Tracker]

 ###### Link Arquitectura: [visualizar UML][Nueva Arquitectura]
 
 ###### Video-demo final: [demo final][video]
 ___
 
 ##### Webs útiles:
 
 - Curso completo de edición de archivos CSS: https://www.w3schools.com/css/default.asp
 - Manual de uso de archivos JSON: https://www.json.org/json-es.html
 ___
 ___

 ##### GDD: Game Design Document / Documento de Diseño del Videojuego
 ## **AVES - Alfred Hitchcock's inspired film-videogame**
**Documento de Diseño - Grupo 12**

**Contribuidores:**
- Alejandro González Sánchez - Algonz39@ucm.es, 
- Jianuo Wen - Jwen@ucm.es, 
- Manuel Prada Mínguez - manuelpr@ucm.es, 
- Pedro Pablo Cubells Talavera - pablocub@ucm.es.

#### **Resumen**
**Géneros**: Aventura, Supervivencia.

**Modos**: Un jugador.

**Público objetivo**:

● Adolescentes y adultos jóvenes - PEGI-16.

● Idioma: Inglés.

**Plataformas**: Web con teclado y ratón.

**Cantidades**:

● Personaje principal.

● Pájaros - enemigos.

● Materiales.

**Versiones del documento**:

<!-- ![Captura del menú][capturamenu] -->

<!-- ![Captura de Juego][capturajuego] -->

**Descripción**

Aves es un juego top down de acción y supervivencia. Combina combate y sigilo e involucra mecánicas de aggro y distancia a los enemigos.

El protagonista es el líder nato del pueblo, con una personalidad humanista que intenta ayudar a los habitantes del pueblo a pasar la tormenta.

La dificultad avanza con cada nivel, las hordas de pájaros van aumentando y son cada vez son más letales. 

El objetivo principal es rescatar a los pueblerinos.

La puntuación final está basada en el número de niveles completados y pájaros eliminados.

**Índice**

**I. Aspectos generales**
• Vista general
• Relato de un nivel

**II. Controles de juego**
• Configuración
• Controles

**III. Jugabilidad**
• Mecánicas
• Dinámicas
• Estética

**IV. Contenidos**
• Historia
• Niveles
• Personajes
• Objetos y enemigos

**V. Referencias**

1. **Aspectos generales**

1.2 **Relato de un nivel :**
El jugador llegará al pueblo en coche, desde donde comenzará el nivel. 
Nada más comenzar el jugador será perseguido por bandadas de cuervos y deberá recorrer las calles para encontrar al habitante que esté en peligro. 
Una vez rescatado, el jugador tendrá que hacerse camino de vuelta al coche.

2. **Controles de juego**

2.1 **Configuración**
Al iniciar el juego desde el menú principal, se mostrará al personaje protagonista en su casa, 
este entorno hace de menú de inicio. 

2.2 **Interfaz y control**

2.2.1. **Interfaz**

**DENTRO DEL JUEGO:**
- Pausa: Pausa el juego
- Habilidades: Radio. (ON/OFF para evitar enemigos.)

2.2.2. **Control**
- Movimiento con wasd
- Esconderse con la "e"
- Atacar con la barra espaciadora

3. **Jugabilidad**

3.1. **Mecánicas**

**Jugador**:
El jugador tiene un movimiento ortodireccional controlado con WASD.
Se apunta con el cursor y ataca golpeando a melé con un bate en un área en forma de cono.
Interactúa con objetos pulsando la ‘E’.

**Sistema de Vida**:

● *Vida del personaje*: 
    Cuando el jugador entra en contacto con los pájaros se quita vida por segundo, cuantos más hay, más daño hacen. 
    Se regenera cuando se termina el nivel o recogiendo la “comida” repartida por el nivel.

**Objetivos**:
    Habrá dos objetivos a cumplir:

● *Principal*: 
    El objetivo principal es rescatar a las personas que se encuentran en apuros. 
    Se debe completar este objetivo para avanzar al siguiente nivel.

● *Flexible*:
    En cada zona se tienen que recoger suministros para poder mantener segura la casa donde se refugian los supervivientes.

**Sigilo**:
    Por los niveles hay cabinas telefónicas y otras estructuras repartidas por el mapa para poder esconderse.  
    Al entrar en ellas, las aves dejan de atacar y se empeziezan a mover de forma errática.

**Enemigos**:
	Los enemigos de este juego son las aves.  Estas aparecen por las esquinas de la pantalla y se accercan al jugador para atacarle. 
Hacen daño por contacto, el daño depende del número de aves atacando al jugador.
Hay enemigos individuales, representados por un ave además de enemigos bandada, varias aves juntas que cuentan como una sola entidad con mayor salud y daño.

3.2. **Dinámicas**

El juego está dividido en niveles. 
Se llega a la ubicación de cada nivel en coche, una vez ahí se tiene que completar el objetivo principal (rescatar al habitante) y volver al coche para completar el nivel. Además, de conseguir recursos para el hogar.

● Hay un tiempo límite indicado con un contador que tiene el objetivo de causar el estrés que infunde la película.
● La dificultad de los niveles aumenta con cada nivel completado y a medida que avanza el contador aumenta también la dificultad. 
● El juego es injugable (debido a la dificultad) una vez termina el contador.

3.3. **Estética**

● Años 60 en un pueblo pesquero.

● Vista cenital (top-down), claro-oscuro, paisaje exterior.

● Salpicaduras y charcos de sangre y cristales rotos.

 4. **Contenidos**

4.1. **Historia**

El protagonista regresa a su pueblo invadido por pájaros y sus amigos y vecinos en peligro, armado con su fiel bate intentará rescatar a todos o morirá en el intento.

5. **Arquitectura y Gestión**
- Pivotal como sistema de gestión.
- Discord como sistema de comunicación para realizar las reuniones grupales y whatsapp para planear reuniones.

6. **Referencias**

● Alfred Hitchcock - Pájaros

● AC - Assassin 's  Creed: tema de sigilo y agro.

● Counter strike: sistema de rehenes.

● Boxhead:  oleadas de pájaros y dinámica de la IA.

● Hotline Miami: Cámara, movimiento por la escena y combate a melé.

![begining][img1]
![attack][img2]
![hidden][img3]

[Nueva arquitectura]: assets/images/aves.drawio.png "Visualizador web"
[Pivotal Tracker]: https://www.pivotaltracker.com/n/projects/2534895 "Herramienta de gestión del Proyecto"
[WEB]: https://acedpol.github.io/Proyecto_PVLI---AVES/ "Web del Proyecto"
[Sprites]: https://www.spriters-resource.com/
[Otros Sprites]: https://www.spriters-resource.com/
[portada]: ./assets/images/Portada.png
[img1]: ./assets/images/begin.PNG
[img2]: ./assets/images/sangre.PNG
[img3]: ./assets/images/oculto.PNG
[video]: https://youtu.be/vDG3FNYQiNU
