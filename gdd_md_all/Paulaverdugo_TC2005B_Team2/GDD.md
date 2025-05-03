# **Shadow Collective**

## _Game Design Document_
## Created by Andrés Tarazona Solloa A01023332, Dulce García Ruiz A01748013, Mariel Gómez Gutiérrez A01275607, Paula Verdugo Marquez A01026218, Santiago Rodríguez Palomo A01025232


---

##### **Copyright notice / author information / boring legal stuff nobody likes**

##

## _Index_

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

In the year 2047, Nexus - an evil corporation led by a hyper-smart AI - conquered the world. The shadow collective, a group of rebels, has been hiding in the shadows trying to overthrow Nexus' rule of surveillance and injustice, but to no avail. The world's last hope rests in the hands of our hero, a cyborg who wishes to use technology for the greater good.

### **Gameplay**

Shadow Collective will be a rogue-lite top-down RPG. The player will choose at the beginning one of three cyborg classes: Cybergladiator, Codebreaker, and Ghostwalker. The Cybergladiator class will give the player super-human strength and fighting skill. The Codebreaker class will give the player the ability to control some of the technology remotely. And finally, the Ghostwalker will have technology that allows them to go undetected.

The gameplay will focus on the player inflitrating the Nexus building, a tall tower with the final boss on the top floor. Each floor will be a level with different objectives and mechanics. As the level progresses, or climbs the building, they will be given rewards like gadgets or upgrades from which they can choose and build their own character, simulating leveling-up. The boss will have different stages, with different mechanics, and the goal is to disconnect the power supply that keeps Nexus alive. (This gives a window for a sequel, since maybe before being disconnected, Nexus transfered itself into another computer). If the player dies, they will be allowed to keep their gadgets but they will have to start again from the first level.

### **Mindset**

Shadow Collective wants to make the player feel like there is a lot at stake. This is done through the rogue-lite mechanic and the story, however, we don't want to make the game too punishing and that's why the player will be able to keep their gadgets. Also, we want the player to feel how they become increasingly powerful as they progress through the levels and climbs the tower. Finally, in the boss stage, we want to make the player feel a sense of urgency, which will be done through the music and visual cues of the game.

## _Technical_

---

### **Screens**

1. Title Screen
   1. Welcome Screen
2. Character Select
   1. Choose your class
3. Game
   1. Level 1-2
   2. Boss Level
   3. Death - Game over screen
4. End Credits
   1. Credits roll

Examples:
![](https://i.imgur.com/1v3AbP1.jpeg)
![](https://i.imgur.com/2Yo0DFx.jpeg)
![](https://i.imgur.com/Ka1K3Mg.jpeg)

### **Controls**

The player will control their character using the WASD keys. As it is a top-down game, they will be able to go in all four directions. To attack, the player will aim using their mouse, and when they click, a projectile will shoot from the player in the direction of the mouse position, until it hits a wall or an enemy. Some gadgets will require player input, so they will be assigned in order a number key.

### **Mechanics**

There are a number of interesting mechanics, and this is how they will be achieved:

- When a player is seen by a camera or a guard, the rest of the guards will be notified and they will go towards the player. The path the enemies will use will be calculated using the A\* algorithm. This will trigger a state of alarm for the guards. If after a certain time the guards haven't seen the player, the state of alert will drop and the guards will again pathfind their way to their original outpost.
- There is a cone of vision for cameras and guards, where if the player is inside they can be seen. This will be implemented with a Polygon 2d Collider, where if the player goes in, a ray will be thrown towards it. If the ray does not hit an obstacle before, the camera or enemy will call a public function from the player if it can be seen (since there are gadgets and ability that could manipulate this), which will return if the player was seen or not.
- The passive gadgets will modify the player class when instantiated, while the active gadgets will have a method called each frame in order to check for input in order to perform an action if necessary.
- The different playable classes will be defined by derived classes from a base abstract class.

Each class has passive abilities and unique gadgets that modify their behaviour and abilities. Here are brief descriptions for each:

Cybergladiator: Has more HP and does more damage.

- Cyber Rush: A dash ability.
- Plasma Shield: A shield that blocks all damage briefly.
- Overcharge: Briefly doubles all damage.

Codebreaker: Can hack (disable for 5 seconds) nearby enemies.

- Shadow Veil: A cloak that when seen hacks the enemy that saw you.
- Circuit Breaker: An EMP surge that hacks enemies inside a range for 5 seconds.
- Phantom Signal: A fake decoy that sends an alarm with the wrong coordinates.

Ghostwalker: Can go invisible for 5 seconds.

- Ghost Vision: The player can see vision cones.
- Phantom Step: Dash when stealthing.
- Ghost Blade: One-hit takedown while stealthing. One use only.

## _Level Design_

---

### **Themes**

1. Tutorial Level

   1. Mood
      1. Easy, interactive, intuitive
   2. Objects
      1. _Ambient_
         1. Small space
         2. Tech trash (obstacle)
      2. _Interactive_
         1. Cameras
         2. Guards
         3. NPC 

2. First Level

   1. Mood
      1. Active, easy, tense, surprising
   2. Objects
      1. _Ambient_
         1. Office cubicles
         2. Dark aisles
         3. Abandoned computers (obstacles)
         4. Tech trash (obstacles)
         5. Desks and chairs (obstacles)
      2. _Interactive_
         1. Cameras
         2. Guards

3. Second level

   1. Mood
      1. Challenging, tense, curious
   2. Objects
      1. _Ambient_
         1. Dark spots
         2. Dark aisles
         3. Office cubicles
         4. Small offices
         5. Abandoned computers (obstacles)
         6. Tech trash (obstacles)
         7. Desk and chairs (obstacles)
      2. _Interactive_
         1. Guards
         2. Cameras
         3. Damaging tiles

4. Final Level
   1. Mood
      1. Tense, tricky, dangerous, hard
   2. Objects
      1. _Ambient_
         1. Narrow and dark aisles
         2. Office cubicles
         3. Small offices
         4. Obstacles arranged as a maze
         5. Desks and chairs (obstacles)
         6. Tech trash (obstacles)
         7. Abandoned computers
         8. Boss room 
      2. _Interactive_
         1. Guards
         2. Cameras
         3. Damaging tiles
         3. Damaging tiles

### **Game Flow**

TUTORIAL LEVEL:

1. Player starts the tutorial level, where he learns how to move forward, back, left, and right.
2. Player gets seen by a camera, so he knows how it works.
3. Player passes along a guard and kills it to understand the dynamic.

ALL LEVELS:

1. Player starts at the entrance.
2. PLayer explores the level map.
3. Enters office cubicles, gets seen by cameras, and followed by guards.
4. Player finds the exit door hidden in the map.
5. Player exits the level and gets to the next one.

FINAL LEVEL:

1. Player starts at the entrance.
2. Player gets to explore the map which divides into two sections.
3. If the player chooses the first section, it will go through a path full of cameras.
4. If the player chooses the second path they will have to fight teh Boss guard.
5. The player needs to find the winner's room.
6. The player needs to enter the winner's room.

### **Examples**

![](https://hackmd.io/_uploads/rycanftw2.jpg)
![](https://hackmd.io/_uploads/H1To2ztD3.jpg)
![](https://hackmd.io/_uploads/BkO23zKv2.jpg)
![](https://hackmd.io/_uploads/HJBC2GKPn.jpg)



## _Development_

---

### **Abstract Classes / Components**

1. BasePlayer
2. BaseEnemy
3. BaseGadget
4. BaseTile

### **Derived Classes / Component Compositions**

1. BasePlayer
   1. Cybergladiator
   2. Codebreaker
   3. GhostWalker
2. BaseEnemy
   1. Guard
   2. Camera
3. BaseGadget
   1. CyberRush
   2. PlasmaShield
   3. Overcharge
   4. ShadowVeil
   5. CircuitBreaker
   6. PhantomSignal
   7. GhostVision
   8. PhantomStep
   9. GhostBlade
4. BaseTile
   1. GroundTile
   2. WallTile
   3. DamagingTile

## _Graphics_

---

### **Style Attributes**

For this game, we will be choosing a neon color pallet. We are including some grays and blacks to give a tech ambient. Because the theme is cyberpunk, colors such as purple, green, and blue are popular between the tiles and the characters.

We are implementing a pixel-y aesthetic, choosing 32 x 32-bit tiles. Because of this selection, the visual may include sharp angles and solid and thick outlines. Because we need obstacles, we include sprites such as tech trash or computers, that will give the ambient a sense of a tech abandoned company.

We are going to implement a tutorial level for the player to learn how different dynamics work. This level will show how he can move and interact with the enemies. We are also providing visual feedback every time a player gets seen by the cameras or shot by the guards. This will give the game a more interactive sense.

### **Graphics Needed**

1. Characters
   1. Human-like, same graphic
      1. Cybergladiator (idle, attack, death)
      2. Codebreaker
      3. Ghostwalker
   2. Other
      1. Camera (surveilance animation)
      2. Guard (idle, attack)
      3. Boss (idle, attack, death)
2. Blocks
   1. Tile floor
   2. Detailed tile
   3. Vent
   4. Vent to grass
   5. Grass
   6. Walls
3. Ambient
   1. Projectiles
   2. Tanks
   3. Wet floor
   4. Computer
4. Gadgets
   1. CyberRush
   2. PlasmaShield
   3. Overcharge
   4. ShadowVeil
   5. CircuitBreaker
   6. PhantomSignal
   7. GhostVision
   8. PhantomStep
   9. GhostBlade

## Examples:

![](https://i.imgur.com/BHKwhv6.jpeg)
![](https://i.imgur.com/YxLgwwG.jpeg)
![](https://i.imgur.com/VmzLfIV.jpeg)
![](https://i.imgur.com/ra03weW.jpeg)
![](https://i.imgur.com/OK3N6W7.jpeg)

## Sounds/Music

---

### **Style Attributes**

Futuristic, somewhat sci-fi sounds. However, it is important to keep everything relatively grounded, given that out theme isn't a space opera, it most likely resembles cyberpunk, which tends to be mostly grounded in a reality slightly ahead of its time.

A perfect example of the grounded nature of the genre we are exploring is the book Neuromancer, where every technological aspect of the world that William Gibson builds, is based off of his contemporary reality in the 80s.

The production of our music should closely resemble production from the 80s, where drums had immense reverbs, and synthesizer were used above all else to convey a futuristic, yet nostalgic sound. This is the basis of the genres of synthwave and cyberpunk. Synthesizers such as the Juno-6 are great synthesizers for lead sounds within less intense tracks. A Prophet synthesizer might be close to what we need for more intense versions, such as higher levels.

### **Sounds Needed**

1. Effects
   1. Steps (Only one type of step is needed in our case, for the main character).
   2. Steps of enemies.
   3. Gunshot with the pulse gun.
   4. Alarm.
   5. Camera sounds when one is nearby.
   6. Hacking sounds (R2D2-like, can be made with an ARP 2600).
2. Feedback
   1. Hacking success.
   2. Level success.
   3. Low Health or hits.
   4. No more MP.
   5. Disabled enemies / cameras.

### **Music Needed**

1. Intro track, main menu screen music.
2. Intro sound for every level, short 10 second track for loading.
3. One track for every level:
   1. Tutorial level: More relaxed track, mostly ambient.
   2. Level 1: Track with lead synth/guitar a bit more intense.
   3. Level 2: Dubstep inspired bass might enter. Higher pace.
   4. Level 3: Intense music. Heavy saw basses, maybe heavy distorted guitars.
4. Boss music: Most intense one yet, phrygian dominant mode could be used to give it a sinister feeling.

_Inspirations_
[Perturbator - Future Club](https://youtu.be/RY66fdMt4vc)
[Carpenter Brut - Roller Mobster](https://youtu.be/qFfybn_W8Ak)
[Kavinsky - Nightcall](https://youtu.be/MV_3Dpw-BRY)
**Boss Music**
[Caprenter Brut - Turbo Killer](https://youtu.be/wy9r2qeouiQ)

## _Schedule_

---

_(define the main activities and the expected dates when they should be finished. This is only a reference, and can change as the project is developed)_

1. WEEK ONE
   1. Create script for moving and shooting.
   2. Create abstract classes for each player type.
   3. Craete abstract classes and prefabs for enemies.
   4. Create player animations.

2. WEEK TWO
   1. Create healthpoints.
   2. Create pathfinding algorithm.
   3. Create scripts for gadgets.

3. WEEK THREE
   1. Create cut scenes.
   2. Create NPC.
   3. Create first level.
   4. Create second level.
   5. Make the enemies follow the character. 

4. WEEK FOUR
   1. Create tutorial level.
   2. Create boss level
   3. Create music controller. 

5. WEEK FIVE
   1. Presentation
   2. Final configurations.
