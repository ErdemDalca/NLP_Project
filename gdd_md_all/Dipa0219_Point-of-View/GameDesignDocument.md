# Point of view #

## Overview and vision statement ##

“Point of View” is a level-based puzzle game in which two small robots must find a way to exit the 
room by position on the two white platforms in the room simultaneously. Simple, right? Sure, if it weren’t for a 
malfunction preventing the two robots from changing their view, making everything outside their field of 
vision unknown. Therefore, the only way for them to escape is to rely on each other, and cooperation will be 
the key to their escape

## Gameplay ##

The gameplay is simple yet engaging: the player will simultaneously control two distinct robots. For one, only a first-person view is available, while for the other, the player can control its movements, with the option to swap roles at any time. The objective of the game is to have the two robots collaborate to reach the end of the level, marked by postioning simultaneously over two different platforms.

To move the robots, players can use either the arrow keys or the WASD keys, while the C key allows them to switch between robots. As the levels progress, new mechanics are introduced, such as movable boxes and intermediate buttons to press, gradually increasing the game’s difficulty and making the experience progressively more challenging and engaging.

## Characters ##

We have only two distinct characters in our game, that are the two robots that you control during the gameplay. 


## Story ##

We evaluated add a story in the game but in the end we understood that there wasn't enough time to add also that
In any case this were the idea we found:
- One evil robot that makes a joke to the main characters and that's the reason why they are blocked and they have to press the buttons to free themselves. In the last level we make a sort of boss fight in which by completing the puzzles you reduce the life of the evil bot.
- An hacker attacked the laboratory where the robot are and they have to escape that place in order to reach a engineer that can adjust their problem. The button are used to access the following rooms.
In the end, our final decision was that the storyline wouldn't fit with the kind of game that we proposed, so we cut it off.

## World ##

The game is set in a laboratory warehouse divided into different zones that the robots must navigate to reach their objectives. We’ve designed the game to include three distinct worlds, each introducing a new core mechanic:

World 1: A tutorial world where players learn the basics of the game, understanding how to make the robots work together to achieve their goal.

World 2: A world that introduces new elements, including buttons that alter the environment and boxes that assist the player. These boxes can be used to reach different areas or to hold down buttons that need to stay pressed.

World 3: The final world introduces moving platforms that add new challenges. These platforms can transport the player (even while in the robot’s first-person view, as the platform moves beneath them) and can rotate the robot, which is otherwise impossible.

Each world progressively builds on the collaboration mechanics, making the gameplay increasingly complex and engaging.

## Media list ##

### Sounds 
- [Soundsnap.com](https://www.soundsnap.com/)

### Assets
- [Unity Asset Store](https://assetstore.unity.com/packages/3d/environments/sci-fi/sci-fi-construction-kit-modular-159280)

## Mechanics ##

As we anticipated during the section "Worlds" during our gameplay we will focus in particularly on two different mechanics: buttons and boxes, moving platforms.

### Possible uses ###

Boxes
- Boxes used to fill an hole to create a pathway for the players
- Boxes used to keep activated a button
- Boxes used to block a moving object
- Boxes can be an obstacle for the view and, because you can't remove it, you have to deal with problem

Buttons
- Buttons used to open a door
- Buttons that can control if an object moves
- Buttons that may create a box
- Buttons that creates a new pathway

Moving platforms
- Can be used to give the possibility to go over a certain obstacle
- Can be used to reduce the time to complete the level with the correct speed
- Can be used to create an obstacle if they move in a opposite direction
- Can be also an obstacle if they ends in a hole and so the player has to pay attention during his movement
- Can be used to create a moving view for the player on the moving platform
- Can add verticality to the level by moving up and down

## Team ##
1. Antonio Di Paola (Developer)
2. Simone Frazzei (Developer) 
3. Francesco Benelle (Developer)
4. Giacomo Ballabio (Developer)

## Deadlines ##

### Week 1 (October 15 deadline) ###
- Prepare 4 different examples of level (1 for each world) to discuss together

### Team meeting (October 15) ###
- All prepared the required levels
- We discussed about our ideas and unterstood that the dark mechanic wasn't has interesting as expected so we decided to focus more on platforms 

### Week 2 (October 22 deadline) ###
- Mobile platform implementation (Horizontal, vertical, treadmill, rotating) (Francesco Benelle, Giacomo Ballabio)
- Button mechanic and organization of package to move (Antonio Di Paola, Simone Frazzei)

### Team meeting (October 24) ###
- Discussion and brainstorming about GDD
- First graphic representation of the most part of the levels
- Coding together regarding physics interaction, user interfaces and menus

### Week 3 (October 29 deadline) ###
- Conclusion of GDD in order to revise that in the following days (Antonio Di Paola)
- Implementation of main menu (Francesco Benelle, Antonio Di Paola)
- In game physics and right interaction between boxes and player (Giacomo Ballabio)
- Construction of the first levels and testing tools to make them (Simone Frazzei)
- User interface during level and completion of levels (Francesco Benelle)

### Team meeting (October 29)
- Conclusion and last check on GDD
- Discussed programs regarding the following week
- Fixed menus and prepared first two levels

### <ins> GDD deadline (November 4 deadline) 

### Week 4 (November 5 deadline)

- Fixing collision between robot and environment (Antonio Di Paola)
- Code cleaning and better organization (Antonio Di Paola)
- Fixing physics after modification made during previous week (Giacomo Ballabio)
- Construction of all remaining levels (Simone Frazzei)
- Starting reasoning about textures for level building (Simone Frazzei)
- Conclusion of all UIs (Francesco Benelle)
- Preparation of local saves (Francesco Benelle)

### Team meeting (November 5)

- Reasoning about adding music to the game
- Prepared the local save for the game
- Discussed about possible texture for the two player

### Week 5 (November 12 deadline)

- Conclusion of physic management (Giacomo Ballabio)
- Start working on music (Giacomo Ballabio)
- Saving statement (Francesco Benelle)
- Texture of the two player (Simone Frazzei)
- Bug fixing and code cleaning (Antonio Di Paola)
- Reasoning about light in dark level (Antonio Di Paola)

### Team meeting (November 13)

- Reasoning about level design
- Discussing about music
- Reasoning about physics

### Week 6 (November 19 deadline)

- Graphic upgrade in menu (Francesco Benelle)
- Texture for levels (Simone Frazzei)
- Level building (Simone Frazzei)
- Soundtrack in levels (Antonio Di Paola)
- Level design (Antonio Di Paola)
- Physics (Trying new models and fixing the one we were using) (Giacomo Ballabio)

### Team meeting
- Preparing the meeting with professors
- Reasoning about difficulty on levels
- Building of a good scene to show to teachers

### Week 7 (November 26 deadline)
- Physics bug fixing (Giacomo Ballabio)
- Level design and fixing level difficulty (Antonio Di Paola)
- Message to show in level and info menu (Francesco Benelle)
- Fixing end level platforms (Simone Frazzei)

### Team meeting
- Discussed last elements for the Alpha
- Concluded selection of the level to for Alpha
- Generated executable for windows, Mac and web

### <ins> Alpha submission deadline (December 8 deadline) 

### Team meeting
- Discussion about comments received on alpha

### Post Christmas deadline (December 28 deadline)
- Level design (Giacomo Ballabio, Francesco Benelle)
- Fixing textures and lights (Simome Frazzei)
- Fixing initial camera (Antonio Di Paola)

### Team meeting
- Discussion about last missing problems
- Reasoning about levels
- Last feature to add

### Session startin deadline (January 7 deadline)
- Added arrow that follows robot (Francesco Benelle)
- Fixing UI (Giacomo Ballabio)
- Level design (Simone Frazzei)
- Finishing GDD and bug checking (Antonio Di Paola)
 
### <ins> Prototype submission deadline (January 12 deadline)

