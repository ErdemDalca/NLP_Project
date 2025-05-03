# Game Design Document
=============================
## Título
   1. Laser Dodge
   2. Subtítulo   
   3. Coletilla
   4. Información adicional
       1. Gestor de Proyecto: Santiago
       2. Developer: Ricardo
       3. QA y testing: Antía
2. Información general del juego
   1.  Concepto del juego
       1. Concepto General
       Juego de naves que consiste en esquivar balas para pasar de pantalla o morir.
       3. Características principales
           1. Un jugador
           2. Estilo retro
       4. Diseño
           1. Objetivo del juego y filosofía: Entretener y oportunidad de entrenar reflejos
           3. Qué es diferente: No hay patrones a la hora de generar las balas
   2.  Género: Arcade
   3.  Audiencia objetivo: Gente adulta que le guste tener nostalgia
   4.  Experiencia de juego
        1. Flujo de juego: Según avanzas de pantalla se va complicando ya que hay que esquivar más balas
4. Gameplay
   1.  Gameplay
       1. Progresión del juego: Avanzas de pantalla cuando esquives todas las balas necesarias por nivel
       2. Objectivos: Esquivar balas
       4. Desafío y estructura del puzle: Las balas se disparan en diferentes spawns que se randomizan
       6. Flujo de juego: Según avanzas de pantalla se va complicando ya que hay que esquivar más balas
5. Mecánicas
   1. Físicas y movimiento: Físicas las propias de unity y movimientos direccionales
   2. Acciones, interacción y comunicación: Si recibes daño tienes un feedback tanto visual como auditivo (Visual: corazones; Auditivo: sonidos de impacto y de disparo)
6. Opciones de juego
   1.  Opciones generales: En cada pantalla de "Game Over" o del Menú principal puedes salir del juego o darle al inicio
   2.  Replaying: Cada vez que se juega el spawn cambia
7. Escenario y personajes   
   1.  Mundo del juego
      El espacio
   2.  Personajes 
      La nave del jugador
8. Niveles 
    Se disponen de diversas pantallas (de momento 3) en las que varía el fondo y la cantidad de balas generadas   
9. Interfaz
   1.  GUI (Graphic User Interface): 
    -Nave del jugador en el centro de la pantalla
    -Vidas en la esquina superior izquierda
    -Balas que pueden aparecer en cualquier sitio de la pantalla
   2.  Sistema de control
   -Con las flechas direccionales o WASD
   3.  Audio
       1. SFX (Sound Effects): Disparos, golpes, victoria y derrota   
10. Técnicos
    1. Hardware objetivo
      PC de perfil bajo
    2. Hardware y software de desarrollo
       1. Motor de juego: Unity
       2. Software principal: Unity, Visual Code, Git, GitHub y Audacity
11. Arte del juego 


    ![Player](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Galaxia%20Sprite%20Pack%20%231/Player/idle_player_basic.png)
    ![Laser](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Galaxia%20Sprite%20Pack%20%231/Effects/BulletsSpriteSheetRed.png)
    ![3 Hearts](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Health%20Sprites/6.png)
    ![2 Heaths](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Health%20Sprites/4.png)
    ![1 Heart](https://user-images.githubusercontent.com/94117604/148687298-7130cdac-d576-4669-8360-7598b779b511.png)
    ![Background1](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Background/Dynamic%20Space%20Background/Sprites/Nebula%20Blue.png)
    ![Background2](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Background/Dynamic%20Space%20Background/Sprites/Nebula%20Aqua-Pink.png)
    ![Background3](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Background/Dynamic%20Space%20Background/Sprites/Nebula%20Red.png)
    ![YouDied](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Background/YouDiead.jpg)
    ![YouWin](https://media.githubusercontent.com/media/SolidSLR/Laser-Dodge/main/Assets/Background/YouWin.jpg)
