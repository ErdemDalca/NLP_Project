# **Quimera**

## _Game Design Document_

---

### Authors

- Alejandro Fernández del Valle Herrera **A01024998**

- Oswaldo Ilhuicatzi Mendizábal **A01781988**

- Andrea Alexandra Barrón Córdova **A01783126**

- Alan Anthony Hernández Pérez **A01783347**

- Mario Ignacio Frías Pina **A01782559**

> Copyright $\copyright$  2023 Ig-Drasil

>    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
>
>    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
>
>    You should have received a copy of the GNU General Public License along with this program.  If not, see https://www.gnu.org/licenses/.    

##
## _Index_

---

- [**Quimera**](#quimera)
  - [_Game Design Document_](#game-design-document)
  - [_Index_](#index)
  - [_Game Design_](#game-design)
    - [**Summary**](#summary)
    - [**Gameplay**](#gameplay)
    - [**Mindset**](#mindset)
  - [_Technical_](#technical)
    - [**Screens**](#screens)
    - [**Controls**](#controls)
    - [**Mechanics**](#mechanics)
      - [Mecánicas activas](#mecánicas-activas)
        - [Movement](#movement)
          - [Side to side movement](#side-to-side-movement)
          - [Air movement](#air-movement)
          - [Jumps](#jumps)
          - [Dodge](#dodge)
        - [Combat](#combat)
          - [Short distance attack](#short-distance-attack)
          - [Mid distance attack](#mid-distance-attack)
          - [Long distance attack.](#long-distance-attack)
        - [Defense Mechanics](#defense-mechanics)
          - [Cloth doll (shield)](#cloth-doll-shield)
          - [Dodge](#dodge-1)
        - [Mecánicas de buffs](#mecánicas-de-buffs)
          - [Candy (temporary buffs)](#candy-temporary-buffs)
          - [Food (health regen)](#food-health-regen)
          - [Muñecas quitapenas (permanent buffs)](#muñecas-quitapenas-permanent-buffs)
        - [Mecánicas de inventario y contadores](#mecánicas-de-inventario-y-contadores)
          - [Cambio de armas](#cambio-de-armas)
          - [Life meter](#life-meter)
          - [Coin system](#coin-system)
          - [Doll counter](#doll-counter)
          - [Mecánicas de comercio](#mecánicas-de-comercio)
        - [Item shop](#item-shop)
          - [Items the shopkeeper can give](#items-the-shopkeeper-can-give)
      - [Mecánicas pasivas](#mecánicas-pasivas)
        - [Item drops](#item-drops)
          - [Bicitaxi (save / fast travel)](#bicitaxi-save--fast-travel)
          - [NPC](#npc)
      - [Cam movement](#cam-movement)
      - [Enemies](#enemies)
        - [Beginners](#beginners)
        - [Mid tier](#mid-tier)
          - [Bosses](#bosses)
      - [Environment](#environment)
        - [Traps](#traps)
        - [Pressure plates](#pressure-plates)
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
    - [**Music Needed**](#music-needed)
  - [_Schedule_](#schedule)

## _Game Design_

---

### **Summary**

Quimera is a metroidvania-rpg where you play as Alex looking for their mom in a rapid-fire  adventure inside a fantastic mexican folklore dream. You will have to make friends and defeat enemies to survive, but be carefull, people are not always what they seem. 

### **Gameplay**

The gameplay is a side-scrolling action adventure game with RPG elements, where you have to move and fight in a 2D world using different types of weapons and items with a Mexican cultural theme.


The goal of the game is to progress through the different levels and find out the truth about the dreams that Alex has been having. In each of these levels there are both platforming and combat challenges, where there are some normal enemies throughout the level and a final boss at the end.


In terms of tactics the player should be resourceful and know how to use the tools and weapons provided, at what time and in what way, depending the situation.


### **Mindset**

The player should feel the fear that Alex feels at the beginning of the adventure, and as the game progresses both Alex and the player get stronger. At the same time the player should want to adventure through the world and see all the things that it contains, but without hurry. We want to provoke these emotions through the mechanics of movement and combat of our game.


It is important that the player feels constantly challenged, and that the game adapts its difficulty to maintain a challenging environment.


The play should be having a similar experience to what a child would feel when getting into a mystical world. having lots of awe at the beginning, but then realizing that “I’m in trouble”.


## _Technical_

---

### **Screens**

1. Title Screen
    1. Play game
    2. General Options
    3. Exit game
2. Game
    1. Assessment / Next Level
    2. Death screen
3. End Credits

### **Controls**

- Movement
    - Lateral Movement
        - Using A and D with keyboard, or the left stick for a gamepad
    - Jumping
        - Using space with keyboard, or the a button on a gamepad: hold
	    to jump higher. 
    - Dash
        - Using shift with keyboard, or the x key on a gamepad
- Weapons
    - Using Weapons
        - Left click with keyboard, or tight trigger with a gamepad
    - Aiming Weapons
        - Aiming with the mouse in the screen with keyboard, or aiming with right stick with gamepad
    - Changing Weapons
        - Right click with keyboard, or left trigger with gamepad

### **Mechanics**

To assure a better experience for the player the game relies on various mechanics. In this section we will start with the active mechanics, the ones that the player does directly, then we will follow with the passive ones, elements of the game where the player does not have to do anything).


#### Mecánicas activas


##### Movement


###### Side to side movement


The player will be able to move left and right with the keys "a" and "d" respectively. 


To be able to move more realistically this movement will consider momentum, that is, it will take a while to stop, and the faster the player goes, the longer it will take to stop.


![Alt text](img/move1.png)


###### Air movement


While the player is in the air, they will have a more limited movement, they will be able to make small corrections, but the movement will not be as fluid as when they are touching the ground.


While in the air the player will not be able to recharge movements. If they jump and then hit, they will not be able to hit again until they touch the floor again.




###### Jumps
To jump the player will have to press "Space".
The player will have a simple jump. Every time they touch the ground, it will only be regained by touching the ground once again.
Thanks to the limited air mobility, the player will have to be very careful when jumping. 
By realizing the space bar early the jump will be shorter, cutting the momentum and increasing the level of relative gravity. By holding it the jump will be higher.


![Alt text](img/jump1.png)


###### Dodge
To doge, the player will click the “CTRL” key.
To help the player navigate, and provide them with an advantage, the player will get a doge action. This action will throw the player slightly backwards and upwards in the opposite direction to the one they are facing. This action can also allow the player to gain speed in order to evade an attacking enemy.




![Alt text](img/doge.png)


##### Combat


### Close ranged attack
This weapon will be able to make area attacks. To activate it the player will use the right click.
In order to attack in close proximity the player can use a wooden snake as a whip. 
The statistics are the following:
- Knockback
- Velocity
- Damage
- Recharge time
- Range distance


###### Mid ranged attack
To activate it the player will use the left click.
To attack at medium distance the user will be able to use a balero to hit someone. The balero is going to be thrown, yet it will stay attached to the player. It has a limit of enemies that it is able to hit at a time. It will be very similar to the way you would throw a chain in other games. 
The statistics are the following:
1. Knockback
1. Velocity
1. Weight
1. Damage
1. Recharge time
1. Range distance
1. Maximum of enemies attacked


Once thrown, the balero will return to the player to allow him to throw it again. 


![Alt text](img/att2.png)


###### Long distance attack.
To activate it the player will use "central mouse".
To allow the player to have a defense from a distance, they will be granted a top that will serve as a projectile.
The top is going to stay rolling, and it will damage the enemies as long as it has speed to roll. 
The top will be thrown, and it will function as an independent object. The only way to get it back is to grab it again by getting closer to it. 
The statistics are the following:
1. Knockback
1. Personal knockback
1. Velocity
1. Weight
1. Damage
1. Recharge time
1. Range distance
1. Maximum of enemies attacked
1. Speed when throwing


![Alt text](img/att3.png)


##### Defense Mechanics


###### Cloth doll (shield)
To activate it the player will hold the "Z" key.
The cloth doll is a typical doll that will fill the role of protecting Alex during dreams. 
It can be used at any moment, and it will completely nullify any damage, but it will break in the process. This means that the doll will be a one use item, so the player will have to be careful when they use it, specially because they will have a maximum capacity of 5. They also aren’t cheap, either by being rare items on the field or by being expensive.


###### Dodge
To doge, the player will click the “CTRL” key.
In order to avoid enemies the player will be able to use the dodge mechanic.


To help the player navigate, and provide them with an advantage, the player will get a doge action. This action will throw the player slightly backwards and upwards in the opposite direction to the one they are facing. This action can also allow the player to gain speed in order to evade an attacking enemy.


##### Mecánicas de buffs


###### Candy (temporary buffs)
Enemies will drop random loot such as candy and coins. The candy will give a temporary buff to the player. This buff will be applied based on the type of candy, adding a temporary damage multiplier. 
There will be the following types:
- Speed
- Attack
- Damage


This will make swarms easier to clear and make players feel more in the zone, clearing hoards, and giving the player a rush and a rewarding feeling when they do so.


![Alt text](img/candy.png)


###### Food (health regeneration)
The player can consume one food item by pressing “E”.
The only way you will be able to regain health is through consuming food items. 
The food can be bought at the ropavejero. Allowing a maximum of 10 items to be bought. After buying food the player will be able to eat it, gaining 20 HP per food item (2 full heals).


![Alt text](img/food.png)


###### Muñecas quitapenas (permanent buffs)


Once you get a doll it gets added as skill points. When pressing “I”, you open an inventory that allows you to click on what you want to upgrade. Once upgraded, there is no going back.


![Alt text](img/doll1.png)


##### Mecánicas de inventario y contadores


###### Cambio de armas


When upgrading a weapon one of them can be chosen to be improved. Depending on what gets chosen, the color of the weapon will change.


###### Life meter
The player will always have a visible life meter. This will display the percentage of life remaining (from 0 to 100). 
To make the character feel like they have progressed, armor stats will increase.


###### Coin system
Chocolate coins will be used as currency. 
When an enemy gets defeated a counter will go up, and an animation will show the coins going into the player.


###### Doll counter
Cloth dolls get used only when being activated while using shields. This will get displayed as a counter.


###### Mecánicas de comercio


Once you find a ropavejero, acknowledged because the Cri Cri song by the same name plays. You can use the in-game currency to buy certain items. Items will be picked at random and will only refresh once the ropavejero decides to move location. 
The ropavejero changes location at random on certain chosen points, and will not appear for a certain amount of time. The point of the ropavejero is that once you find him the amount of time he will stay is random, he needs to get going to pay the bills.


##### Item shop
When interacting with the ropavejero a UI will open. This will let the player choose between different items. The player can buy them there, or leave them. Once they are bought they will get added to the player’s inventory.


###### Items the shopkeeper can give


- Life
- Dolls
- Weapon upgrades


#### Mecánicas pasivas


##### Item drops


Item drops will use an SQL table where there is a random amount of drops based on how the player interacts. This means that monsters will get a category, and it will drop a random amount of items based on the progression and loot table.


The player will then be able to get any amount.


![Alt text](img/random.png)


###### Bicitaxi (save / fast travel)


The bicitaxi will be the only place where you can save the game. After saving it can be used for fast travel. Any unlocked bicitaxi will allow so. They will be placed along the map at specific locations.


![Alt text](img/vicitaxi.png)


###### NPC


NPC’s will be used only as worldbuilding, making the world feel more alive.


They will take lines from a database, looping through the chat options.


![Alt text](img/npc1.png)
![Alt text](img/npc2.png)


#### Camera movement


To move the camera, we will use cinemachine. This will allow the player to look forward when running around so they can see what will come next. The camera will also have a smooth dampening to help users with diverse eye problems feel more comfortable.


![Alt text](img/cinemachine.png)


#### Enemies


There will be 3 types of enemies:


- The common
- The mid tier
- The boss


##### Common


These enemies are easy to kill. Their AI will be focused on just walking to the player and their main objective is to give the player a challenge based on swarms.


##### Mid tier


These enemies will have the ability to try to get close and make better combat. The enemies that are considered mid tier will have better base stats and will be considered as a challenge by themselves.


###### Bosses


Each boss will have their own mechanics. The mechanics are described on how the boss will move.


#### Environment


The environment will have various traps and tricks that serve as passable obstacles.


##### Traps


There will be places where you can fall through the ground. The ground will be a slightly different color, but other than that, it will be the same.


##### Pressure plates


Some places will be reachable by using pressure plates. They can be activated by using enemies, the player themselves, or toys.


Pressure plates will have the ability to move objects in game, spawn new objects or set actions.


## _Level Design_

### **Themes**

1. Forest
    1. Mood
        1. Dark, calm, foreboding
    2. Objects
        1. _Ambient_
            1. Tall Trees
            2. Falling Leaves
            3. Flowers
            4. Bushes
        2. _Interactive_
            1. False floor
2. Town
    1. Mood
        1. Secure, light up, night
    2. Objects
        1. _Ambient_
            1. Houses
            2. Tavern
            3. StreetLights
            4. Street
		    5. Trash cans
        2. _Interactive_
            1. BiciTaxi
            2. Townsfolk
                1. Mariachi
                2. Catrinas
3. Underground Sewer
    1. Mood
        1. Dark, gross, scary
    2. Objects
        1. _Ambient_
            1. Dirt
            2. Dripstone
            3. Rats
            4. Fumes
  		    5. Water
        2. _Interactive_
            1. Nahuales
		    2. Mummies of Guanajuato
            3. Toxic water
            4. Boss

### **Game Flow**

1. The player starts in the forest
2. Starts walking to his right to fall into a trap.  
3. When they fall into the trap they enter the tutorial
4. At the end of the tutorial gets the doge 
5. Go back to the forest to jump over the trap and get to the city.
6. The NPC gives the player a start on how to progress.
7. Goes to the sewers
8. Pass the sewers after defeating the enemies and mini-bosses.
9. Arrives with the weeping woman to defeat the enemies.
10. Unlock the Charro Negro zone.
11. Confronts the Charro
12. End

#### Map examples

<img src="img\Boceto_Mapa1.jpg" width="50%">
<img src="img\Boceto_Mapa2.jpg" width="50%">
<img src="img\Boceto_Mapa3.jpg" width="50%">
<img src="img\Boceto_OpenWorld.jpg" width="50%">

## _Development_

---

### **Abstract Classes / Components**

1. BasePlayer
    1. PlayerController
    2. GroundDetection
2. SaveAndLoad
    1. saveload
3. Teleport
    1. TPsystem
4. Weapon
    1. Hurtbox
    2. Balero
    3. ControladorTrompo
    4. Espada
    5. Trompo
    6. TrompoDetect
5. UI
    1. HealthManager
6. BaseEnemy

### **Derived Classes / Component Compositions**

1. BaseEnemy
    1. BeginnerEnemy
    2. MediumEnemy
    3. BossEnemy

## _Graphics_

---

### **Style Attributes**

The graphic style of the game is cartoony, the colors used are from a vibrant color palette, the game uses mainly raster graphics from open graphics libraries and some custom-made graphics assets.

The textures will feature solid, thick outlines and smooth curvatures that complete a more hand-drawn style. We opted out of a pixelated style in favor of this one, this will change the process of animating the models to using the unity animating studio.

The inspiration for the games style is mainly hollow knight, this cartoony style lends itself to detailed backgrounds and fluid animations.

For our interactive elements we strive to have a simple and clear UI, where the player can feel that their actions are being represented in game, and that they know how to use their tools to progress through the game.

#### Assets Examples

<img src="img\quitapenas_gris.png" width="200" height="200">
<img src="img\Calaverita.png" width="200" height="200">
<img src="img\alexFront.png" width="200" height="300">
<img src="img\alexSide.png" width="200" height="300">

#### Backgrounds Examples

<img src="img\Background.png" width="400" height="200">
<img src="img\Cartoon_Forest_BG_04.png" width="400" height="200">
<img src="img\City1.png" width="400" height="200">
<img src="img\City2_pale.png" width="400" height="200">
<img src="img\City4_pale.png" width="400" height="200">

### **Graphics Needed**

1. Characters
    1. Human/player
        1. Mariachis
        2. Catrinas
        3. Player / Alex
        4. Cholo
        5. Bartender
        6. Horse
        7. Axolotl
    2. Other
        1. Xoloitzcuintle
        2. Rats
        3. Ropavejero
        4. Bicitaxi
2. Blocks
    1. Dirt
    2. Dirt / Grass
    3. Stone Block
    4. Stone Bricks
    5. Tiled Floor
    6. Weathered Stone Block
    7. Weathered Stone Bricks
3. Ambient
    1. Tall Grass
    2. Trash Cans
    3. Torch
    4. Armored Suit
    5. Chains (matching Weathered Stone Bricks)
4. Other
    3. Tramps
    4. Pressure plates

## _Sounds/Music_

---

### **Style Attributes**

Our music will have two different styles between the two worlds that Alex travels through.

First, in the human world there will be some Mexican music and a lively mood throughout, Then, once Alex goes to a level where there is danger the music will reflect this change and become instrumental and serious.

### **Sounds Needed**

1. Effects
    1. Walking
    2. Doge
    3. Kill (take damage)
    4. Monsters Noises (mummies, mystical and else)
    5. Swing
    6. Random people murmuring
    7. A hmmm sound
    8. Talaches moving
    9. Boss noises
2. Feedback
    1. candy eaten
    2. healed
    3. low health
    4. open inventory
    5. picked up top
    6. coin up sound
    7. protected by doll (something getting broken)

### **Music Needed**

1. Intro song for the forest
1. Ambient sound that makes you feel anxious
3. Ambient sound for the city
4. Cri cri’s “la gran ciudad” for the ropa viajeros
5. Intense boss music
6. Really badly sang “Matalas” by Alex
7. Cumbias for the bicitaxi
8. “El mariachi loco” for the mariachi NPC

## _Schedule_

---

1. Documentation
    1. User Stories
    2. Product Backlog
    3. UML Diagrams
        1. ER Diagram
        2. Use Case Diagram
2. Development of Base Classes
    1. Entities
        1. Player
        2. Enemy
        3. Interactive Objects
    2. States
        1. World
        2. UI
3. Development of basic mechanics
    1. Movement
    2. Weapons
    3. UI
    4. Enemies
4. Level Design
    1. Sketch making
    2. Tileset selection
    3. Tile palette making
    4. Map making
    5. Backgrounds
5. Development of Derived Classes
    1. Enemies
        1. Basic
        2. Medium
        3. Boss
    2. Interactive
        1. Traps
        2. Pressure plates
6. Sound and music design