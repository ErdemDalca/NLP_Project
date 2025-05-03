# Zungax
SinPC game design document - Zungax
 
Game overview
Project background
SinPC entertainment se basa en crear experiencias cautivadoras y envolventes, en este caso se estará experimentando con tecnología de realidad aumentada para tratar de traer de vuelto juegos de antaño que se encontraba en los arcades, como los fps en rieles en los cuales solo tenias que disparar a los objetivos y el personaje se movía solo por el mapa.
Zungax es un videojuego en el que se deberá disparar a través de taps en la pantalla a androides que salen del spawnpoint de la realidad.
High-level concept
Nombre del juego: Zungax AR
Dispositivos objetivos:Dispositivos de mediana a alta gama, Android y IOS
Audiencia objetivo: Jugadores de juegos de acción: Individuos que disfrutan de experiencias de juego emocionantes y desafiantes, especialmente aquellos interesados en juegos de disparos y combate.
Aficionados a los juegos de realidad aumentada (AR): Personas que tienen interés en las nuevas tecnologías de realidad aumentada y disfrutan de experiencias de juego inmersivas que integran elementos del mundo real con el virtual.
Amantes de los juegos clásicos de arcade: Entusiastas de los juegos retro que aprecian los títulos clásicos de la era de los arcades y que buscan experiencias modernas que capturen la esencia y la nostalgia de esos juegos.
Usuarios de dispositivos móviles Android de gama media a alta: Propietarios de dispositivos Android con especificaciones técnicas que admitan la ejecución fluida de juegos de realidad aumentada y que estén interesados en explorar nuevas experiencias de juego en sus dispositivos móviles.
Edad y demografía: La audiencia objetivo principal abarca a jugadores de entre 18 y 40 años, aunque el juego puede atraer a un rango más amplio de edades. Se espera que la audiencia está compuesta principalmente por jugadores casuales y entusiastas de la tecnología.
Release date: 03/2024
Publisher: SinPC Entertainment
En este juego de realidad aumentada habrá que proteger tu nave de androides los cuales quieren destruir tus barricadas para matarte.
Objetivo del juego

El objetivo del juego se basa en eliminar una cantidad indeterminada de androides antes de  que logren acercarse a tu barricada en un tiempo límite, si se acaba el tiempo límite es que ganaste, la puntuación dependerá de cuantos androides hayas destruido. Si varios androides logran alcanzar tu barricada, la salud de esta se reducirá a 0 y habrá pantalla de game over. El usuario podrá ver a su alrededor para ir eliminado los androides en todas las direcciones y así poder defender su base. 
Tema, ambiente y estilo visual
El juego será ambientado en un apocalipsis tecnológico, con vibras de post apocalípsis tecnológico usando audios, VFX y más modelos 3D para generar ese tipo de sensación de Fin del mundo.
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.giantbomb.com%2Fon-rails%2F3015-169%2F&psig=AOvVaw2gpyyDjs1oH4HZvBiWUSse&ust=1708128289970000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMiumfXHroQDFQAAAAAdAAAAABAEhttps://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.roadtovr.com%2Ftower-defense-vr-game-home-a-drone-release-date%2F&psig=AOvVaw1d594ko2O1h3m_KZnyUa9x&ust=1708128390401000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPihhaXIroQDFQAAAAAdAAAAABAJ

Gameplay
Puntuación
Los androides que destruyas te darán recompensas aleatorias, lo que puede ser: Balas, tiempo extra, mejoras al jugador o tablas de reparación. .
Mecánicas del jugador
Tap al celular para disparar
Tap a bolas de mejoras para equiparlas
Deslizar hacia abajo para recargar balas.
Agarrar tablas para reparar barricadas.

Mecánicas de los objetos
Enemigos movimiento contínuo hacia el jugador.
Atacar al jugador.
Soltar objetos al morir y dar una cantidad de puntos.
Tablas: Recolectarse y usarse para mejorar barricadas.
Barricada: Representa la vida del jugador, al destruirse se acaba el juego. se repara con tablas.
Munición: Se recolecta por el jugador, para poder utilizar el arma.
Mejoras: Velocidad de disparo, se pueden disparar más balas por tap, y Daño, cada disparo hace más daño a los enemigos.
Tiempo extra: Los enemigos soltaran objetos de tiempo extra, que alargan el tiempo de la partida.
 
Diseño de interacciones

El juego inicia en el momento que la cámara detecta el suelo y crea un ground plane.
Aparecerá una barricada alrededor del jugador.
Los androides van a estar apareciendo desde una distancia definida, en lugares aleatorios, es decir pueden aparecer en la espalda al lateral o al frente pero siempre a una distancia definida.
Los androides al acercarse quitan vida a la barricada, esto es para controlar la distancia a la que ellos se acercan.
El Jugador podrá tener mejoras para hacer más daño o disparar más rápido, además de poder agarrar tablas y reparar la barricada.
El jugador usará las tablas que dejan los enemigos para reparar la barricada y poder durar más en la partida.
Al acabarse el tiempo habrá pantalla de game over con tu puntaje, también se acaba el juego se destruyen por completo tu barricada.

Interfaz de usuarios y retroalimentación


Barra de vida que indica cuanto más se puede resistir.
Cuando se recibe daño la pantalla titila rojo.
Balas enumeradas para que el jugador sepa cuando debe recargar.
Cuando muere un androide este explota dejando loot para tomar.
Un temporizador que indica el tiempo límite para culminar.
El loot brillará de colores según que sea, munición, tablas, mejoras o tiempo extra.

Técnicas 
Motor 
Unity 2022.3.6f1 ha sido seleccionado como el motor de desarrollo para Zungax debido a su facilidad de uso en la creación de experiencias de realidad aumentada (AR), su amplia gama de características y su sólida capacidad de implementación en las plataformas objetivo. Al utilizar Unity, podemos aprovechar al máximo las herramientas y recursos disponibles para ofrecer una experiencia de juego envolvente y de alta calidad.
 
Plataformas de destino 
 
Para Zungax, las plataformas de destino incluirán dispositivos Android de gama media a alta. Al focalizarnos en la plataforma Android, nos aseguramos de alcanzar una amplia base de usuarios, ya que es el sistema operativo móvil más utilizado a nivel mundial. Esto nos permite maximizar la accesibilidad y la participación del público objetivo del juego. Además, al enfocarnos en Android, podemos aprovechar al máximo las características específicas de esta plataforma para optimizar la experiencia de juego y garantizar un rendimiento óptimo en una amplia variedad de dispositivos. Aun	que no nos limitamos a adapatarlo a IOS en un futuro.
