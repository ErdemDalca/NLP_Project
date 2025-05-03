# FRESHALIENS

# Game Design Document

## 1 Introduction

Freshaliens is a 2D platform game where the main characters are two little aliens.
The game is designed in order to be played both by a single player or by two player
in cooperative mode.
The two aliens are not the same: one is a simple ground player, able to move, jump and shoot; the other one
is able to fly everywhere. The two of them must collaborate to overcome every obstacle and succeed their mission!
### 1.1 Plot

In a remote galaxy there is an ancient alien race that use to conquer as many planets as they can.
Their children are trained since their birth to conquer planets and when they turn 10 are sent to conquer their first planets.
Two cute aliens, Mike and George, are the main character of our adventure.  
Mike has been trained to kill, he has no fear and has learnt to use all kind of alien weapons but he always use his favorite one.
George has been trained to overcome every obstacle he can face. He can fly and can reach even the most unreachable spot.
Mike and George have also learnt to collaborate together as a couple of partners should ever do.
Will they be able to conquer all their assigned planets?

## 2 Description of the game
### 2.1 Technical specifics

Freshaliens is a PC offline game where the player(s) plays using the keyboard as input or a controller input that will be provided and suggested.  
It is developed using Unity as graphic engine and C# scripts.  
The game has a 2D graphic with an horizontal scrolling view (like Super Mario Bros for instance).

## 3 Gameplay design

### 3.1 Basic Mechanics

|                      "Main"                      |                            "Fairy"                             |
|:------------------------------------------------:|:--------------------------------------------------------------:|
| Can move forward and back on the ground and jump |                  Flies in all the directions                   |
|        Can shoot to enemies with his gun         |            Can only stun enemies with melee attacks            |
|                        /                         | Is able to interact with the environment to overcome obstacles |


### 3.2 Cooperative Mechanics

- The two aliens have 3 shared lives: each time one of them is hit, one of the lives is lost, once all the lives are lost the level restart from above.
  When someone is hit he will blink for some seconds and there will be no respawn, if Mike falls he will respawn in a chosen point.
- George can allow Mike to jump on itself, making him reaching higher points: when they are near they have to press JUMP in the same moment and George will make Mike jump higher.
- George has to control the environment in order to unlock passages and make Mike go on.

### 3.3 Cooperative situations

- Some enemies need to be first stunned by George in order to be then killed by Mike. (Stun can be required to be one single shot or multiple shot)
- While George search a way to go on, enemies attack Mike.
- Mike could must shoot to the environment in order to allow George to proceed, the whole mechanic could be required to be executed in a synchronous way.
- In situation with several enemies George can use the environment to harm them.


### 3.4 Levels Organization

Each planet to conquer represent a level. The planets will be distributed in solar systems.

### 3.5 Level Design

In order to give the idea of conquering a planet, each level of the game is shaped as a round world: the two aliens must round it all, killing all enemies and overcoming all the obstacles. 
They land on a point on the planet with their ship and, rounding it, they will return to the starting point and plant their flag.
Same planets of the same solar system will be characterized by the same design: rocky, desert, iced.

### 3.6 Controls

KEYBOARD: George will use W-A-D to move and jump and Q to shoot, Mike will use I-J-K-L or the arrows to move.
Mike will shoot on the horizontal axis: its shoots will proceed right forward toward the direction where Mike is looking at when shoots.
Some other keys could be used for special actions.  

### 3.7 Enemies

On the planets there are different kind of enemies (each one with its own attack style). Flying and not flying enemies.

### 3.8 Menu
Once the game starts it is shown the main menu. From it is possible to start a new game, load a previous one or change the settings.  
When the game starts it will show the actual solar system and the player have to choose the level to play.  
