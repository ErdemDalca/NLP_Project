# **Raccoon Runcasters**

![Racoon Runcasters Logo](https://www.bing.com/images/create/raccoon-runecasters-logo2c-2d-pixel-art-style-from-/1-6619b092ae554b62ae139291fd48a5db?id=%2bFgM14aupL%2bJEXM7%2bYhehw%3d%3d&view=detailv2&idpp=genimg&idpclose=1&thId=OIG3._2kDxjbN7ZkHQGftlGfX&FORM=SYDBIC)
## _Game Design Document_

---

##### **© 2024 . All rights reserved.

##### Title: Raccoon Runcasters

The content of this game, including all text, graphics, images, and other material are protected by copyright laws and international treaties. Unauthorized reproduction or distribution of this game, or any portion of it, may result in severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.

No part of this game may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the copyright owner, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

For permission requests, write to the copyright owner at the following email: (Scrum Master actual)

#### Autors:

##### Ellioth Romero 
A01781724

###### Natalia Rodriguez 
A01663909

##### Bruno Avendaño 
A01784613


##
## _Index_

---

1. [Index](#index)
2. [Game Design](#game-design)
    1. [Summary](#summary)
    2. [Gameplay](#gameplay)
    3. [Mindset](#mindset)
3. [Technical](#technical)
    1. [Screens](#screens)
    2. [Controls](#controls)
    3. [Mechanics](#mechanics)
4. [Level Design](#level-design)
    1. [Themes](#themes)
        1. Ambience
        2. Objects
            1. Ambient
            2. Interactive
        3. Challenges
    2. [Game Flow](#game-flow)
5. [Development](#development)
    1. [Abstract Classes](#abstract-classes--components)
    2. [Derived Classes](#derived-classes--component-compositions)
6. [Graphics](#graphics)
    1. [Style Attributes](#style-attributes)
    2. [Graphics Needed](#graphics-needed)
7. [Sounds/Music](#soundsmusic)
    1. [Style Attributes](#style-attributes-1)
    2. [Sounds Needed](#sounds-needed)
    3. [Music Needed](#music-needed)
8. [Schedule](#schedule)

## _Game Design_

---

### **Summary**

It's a game that resembles the Pokemon style, where instead of a moveset there are cards that allow you to attack your enemy in many ways depending on your class.

The visual style is pixel art, aiming to resemble turn-based RPG games of pokemon from the 2000's.

Es un juego estilo Pokémon, donde en vez de un moveset hay cartas que te permiten atacar a tu enemigo de múltiples formas dependiendo de tu clase.

El estilo visual es pixel art, se busca dar un aire a los juegos RPG de turnos de Pokémon de los 2000's

### **Gameplay**

ENGLISH:
Two players (PvE), face eachother in a turn-based attack game, each one has a pool of cards but they can only have 4 in their hand at a time, the cards will cycle according to the use they give them, like in Tetris or Clash Royale, where the cards in your deck work in a queue system, waiting to be utilized and cycled. These cards can harm, increase/decrease statistics, prevent attacks or even invoke duels. The game ends when the life of one of the players reaches zero. In addition to these cards, you will have the opportunity to choose one of three classes (Cowboy, Magician or Fighter), each class will have some special cards that will help to add dynamism to the game.  

ESPANOL:
Dos jugadores (PvE), se enfrentan en un juego de ataque de turnos, cada uno tiene un pool de cartas, pero solo podrá tener 4 en mano, e irán ciclando de acuerdo a su uso, estilo tetris/clash royale. Estas cartas podrán hacer daño, aumentar/disminuir estadísticas, evitar ataques, o inculso invocar duelos. El juego acaba cuando la vida de alguno de los dos participantes llegue a cero.

### **Mindset**

ENGLISH:
It's oriented to be a TCG, your deck depends on your class and progess, though you will be able to unlock cards to use in your deck and attack in more intersting ways. 

ESPANOL:
Está orientado hacia un TCG, tu deck depende de tu clase y tu progreso, pues podrás ir desbloqueando cartas para utilizar en tu mazo y atacar de maneras más interesantes.

QUESTION:
What kind of mindset do you want to provoke in the player? Do you want them to feel powerful, or weak? Adventurous, or nervous? Hurried, or calm? How do you intend to provoke those emotions?

ANSWER:
We want the player to feel a sense of strategy and skill in the game, we want them to plan out micro strategies despite the randomness of the card cycles
in order to win. We want each class to have a different feeling when it comes to strategies, and with that, a different approach to winning. For example
one can pick the cowboy class, which could have a certain advantage in minigames, one could take advantage of that and shoot their way towards the win instead of just sticking to the main game and dealing damage. The game should feel even, not too easy, not extremely hard, it should be hard enough to actually feel you deserved to win.

With the minigames we want to provide a rich but connected environment where the player does not feel stranded in one place, which is kind of what happens
in traditional RPG Pokemon games, they eventually get repetitive and you can get away with spamming one strong move, we would like to scrap that completely.

We want the game to have two sides, the cards will encourage the players to think and use their tactical skills to winn the game, while the minigames will test their ability and distress to be able to overcome the oponent. 

## _Technical_

---

### **Screens**

1. Title Screen
    1. Options
2. Level Select
3. Game
    1. Inventory
    2. Assessment / Next Level
4. End Credits

_(example)_

### **Controls**

How will the player interact with the game? Will they be able to choose the controls? What kind of in-game events are they going to be able to trigger, and how? (e.g. pressing buttons, opening doors, etc.)

### **Mechanics**

Are there any interesting mechanics? If so, how are you going to accomplish them? Physics, algorithms, etc.

## _Level Design_

---

_(Note : These sections can safely be skipped if they&#39;re not relevant, or you&#39;d rather go about it another way. For most games, at least one of them should be useful. But I&#39;ll understand if you don&#39;t want to use them. It&#39;ll only hurt my feelings a little bit.)_

### **Themes**

1. Forest
    1. Mood
        1. Dark, calm, foreboding
    2. Objects
        1. _Ambient_
            1. Fireflies
            2. Beams of moonlight
            3. Tall grass
        2. _Interactive_
            1. Wolves
            2. Goblins
            3. Rocks
2. Castle
    1. Mood
        1. Dangerous, tense, active
    2. Objects
        1. _Ambient_
            1. Rodents
            2. Torches
            3. Suits of armor
        2. _Interactive_
            1. Guards
            2. Giant rats
            3. Chests

_(example)_

### **Game Flow**

1. Player starts in forest
2. Pond to the left, must move right
3. To the right is a hill, player jumps to traverse it (&quot;jump&quot; taught)
4. Player encounters castle - door&#39;s shut and locked
5. There&#39;s a window within jump height, and a rock on the ground
6. Player picks up rock and throws at glass (&quot;throw&quot; taught)
7. … etc.

_(example)_

## _Development_

---

### **Abstract Classes / Components**

1. BasePhysics
    1. BasePlayer
    2. BaseEnemy
    3. BaseObject
2. BaseObstacle
3. BaseInteractable

_(example)_

### **Derived Classes / Component Compositions**

1. BasePlayer
    1. PlayerMain
    2. PlayerUnlockable
2. BaseEnemy
    1. EnemyWolf
    2. EnemyGoblin
    3. EnemyGuard (may drop key)
    4. EnemyGiantRat
    5. EnemyPrisoner
3. BaseObject
    1. ObjectRock (pick-up-able, throwable)
    2. ObjectChest (pick-up-able, throwable, spits gold coins with key)
    3. ObjectGoldCoin (cha-ching!)
    4. ObjectKey (pick-up-able, throwable)
4. BaseObstacle
    1. ObstacleWindow (destroyed with rock)
    2. ObstacleWall
    3. ObstacleGate (watches to see if certain buttons are pressed)
5. BaseInteractable
    1. InteractableButton

_(example)_

## _Graphics_

---

### **Style Attributes**

What kinds of colors will you be using? Do you have a limited palette to work with? A post-processed HSV map/image? Consistency is key for immersion.

What kind of graphic style are you going for? Cartoony? Pixel-y? Cute? How, specifically? Solid, thick outlines with flat hues? Non-black outlines with limited tints/shades? Emphasize smooth curvatures over sharp angles? Describe a set of general rules depicting your style here.

Well-designed feedback, both good (e.g. leveling up) and bad (e.g. being hit), are great for teaching the player how to play through trial and error, instead of scripting a lengthy tutorial. What kind of visual feedback are you going to use to let the player know they&#39;re interacting with something? That they \*can\* interact with something?

### **Graphics Needed**

1. Characters
    1. Human-like
        1. Goblin (idle, walking, throwing)
        2. Guard (idle, walking, stabbing)
        3. Prisoner (walking, running)
    2. Other
        1. Wolf (idle, walking, running)
        2. Giant Rat (idle, scurrying)
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

### **Sounds Needed**

1. Effects
    1. Soft Footsteps (dirt floor)
    2. Sharper Footsteps (stone floor)
    3. Soft Landing (low vertical velocity)
    4. Hard Landing (high vertical velocity)
    5. Glass Breaking
    6. Chest Opening
    7. Door Opening
2. Feedback
    1. Relieved &quot;Ahhhh!&quot; (health)
    2. Shocked &quot;Ooomph!&quot; (attacked)
    3. Happy chime (extra life)
    4. Sad chime (died)

_(example)_

### **Music Needed**

1. Slow-paced, nerve-racking &quot;forest&quot; track
2. Exciting &quot;castle&quot; track
3. Creepy, slow &quot;dungeon&quot; track
4. Happy ending credits track
5. Rick Astley&#39;s hit #1 single &quot;Never Gonna Give You Up&quot;

_(example)_


## _Schedule_

---

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
