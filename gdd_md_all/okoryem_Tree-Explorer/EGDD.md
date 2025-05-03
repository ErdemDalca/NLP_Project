# Cave Explorer

## Elevator Pitch

You are mining in a deep cavern with monsters closing in \- choose the most efficient route to the center to survive and collect the most minerals\!

## Influences (Brief)

- Influence \#1: Stardew Valley and Omori  
  - Medium: Game  
  - Explanation: The view of the game would mirror the pixelated aesthetics of Stardew and Omori. There would be a slight 3D aspect to the map but overall the map should be 2D.  
- Influence \#2: Binding of Isaac  
  - Medium: Game  
  - Explanation: To traverse the tree we want to do a room system, where the player walks through different doors. This type of system is used in the Binding of Isaac and we would like to implement a system similar to it, for traversal. This will give players the ability to explore each room and pick which room they want to go to next freely.  
- Influence \#3: Solo Leveling   
  - Medium: Television  
  - Explanation: The aesthetic of the anime inspired the color scheme and mood of the game. The exploration of a cave was inspired by the dungeon exploration in the show.

## Core Gameplay Mechanics (Brief)

- Traversing the Cave  
- Mining  
- Danger  
- Time Constraint

# 

# Learning Aspects

## Learning Domains

Introduction to Data Structures

## Target Audiences

College Level Computer Science Students

## Target Contexts

Data Science college level courses

## Learning Objectives

- By playing this game students will be able to differentiate between both Breadth-First-Search (BFS) and Depth-First-Search (DFS).  
- By playing this game students will be able to traverse graphs and correctly choose which algorithm (BFS or DFS) to implement based on the given problem.  
- By playing this game students will be able to identify why visiting certain nodes is more or less efficient based on the search algorithm used.

## Prerequisite Knowledge

- Prior to playing this game, players should be able to identify what trees and graphs are  in the context of Computer Science.  
- Prior to playing this game, players should be able to define what an algorithm is and why it is necessary for searching a tree in Computer Science.  
- Prior to playing this game, players should be able to differentiate between a stack and a queue.

## Assessment Measures

Given a random tree and a map, be able to correctly list the nodes that need to be traversed by depth according to the right algorithm.

# What sets this project apart?

- This game has a unique learning objective. Very few games, if any, aim to teach students about BFS and DFS algorithms both of which are important concepts for CS students  
- The aesthetics of the game are unique, combining elements of 2D and 3D while also using a vibrant color scheme that accentuates the minerals in the map.

# Player Interaction Patterns and Modes

## Player Interaction Pattern

One person plays the game using WASD to move. The player can walk to the direction of the next node they want to move to and confirm their choice on the screen.

## Player Modes

- Player mode \#1: Main Menu (title screen, rules, and any game settings, click keys to navigate to the main game)  
- Player mode \#2: The Caves (Click a button on screen to Start Game or Restart Game if you lost)  
- Player mode \#3: The Map (Click a key to get to the map. Select a node/cave with the mouse)

# Gameplay Objectives

- Primary Objective \#1:  
  - Description: Go to the correct node to mine crystals  
  - Alignment: Choosing the right notes for the BFS or DFS algorithm would result in better crystals to mine at the node.  
- Primary Objective \#2:  
  - Description: Escape the cave as fast as possible in order to avoid being eaten  
  - Alignment: Following the path you took into the cave is similar to returning a path after doing a BFS or DFS on tree

# Procedures/Actions

The player can use WASD to move around and click to select things. The player can move to a different node, check their map, and check their items.

# Rules

- The player has a pickaxe and a flashlight. The pickaxe is used to mine minerals, and the flashlight is used to illuminate the area more. Both of these resources are currently infinite.  
- The player is limited to choosing certain doors in the direction of a new node. If the player does not advance to the right node in an efficient way and amount of time, they will be penalized or eaten by monsters.  
- Different minerals have different scores. Better minerals increase your score. There are also different levels of pickaxes that can be unlocked with progress that are needed to mine higher level minerals.

# Objects/Entities

- Minerals  
- Miner  
- Cave  
- Map (with tree)

## Core Gameplay Mechanics (Detailed)

- Traversing the Cave: Players will have to decide which door to go through next throughout the cave to follow a BFS or DFS. They can move using WASD, and are free to choose which way they go. Players will be incentivized to follow the search algorithms in order to teach them about tree traversal, as well as win the game.  
- Mining: In each node of the cave there will be crystals to mine. The player will need to have the correct level of pickaxe to mine specific crystals in each cave. The player will click or press an interact button to mine the crystals. Crystals will be used to upgrade the level of their pickaxe.  
- Danger: The player will have to run away from monsters while traversing the caves. These monsters should start off easier and increase in difficulty as the player progresses through the game. They must take the shortest way out to survive the monster attacks.  
- Time Constraint: There is a limited amount of time to complete each map. The player must keep moving before their timer runs out. Otherwise, the player would either be attacked by a monster or miss out on better loot in the new node.

## 

## Feedback

The score on the screen will notify the player of how much loot they have collected. There would be audio feedback as well that notifies the player of their progress; going in the right direction would trigger positive sounds and making a mistake or approaching danger would trigger a negative sound. Any rare item that the player encounters would have a unique sound.

The player should receive a congratulations screen when they reach the last node using the search algorithm. The screen will show the route that they took as well as the most efficient route (showing where they made errors).

# Story and Gameplay

## Presentation of Rules

Players will be presented with a tutorial walking them through how to traverse a cave (graph/tree). It will be a simple cave.

## Presentation of Content

The tutorial will guide the player through DFS and BFS and give them the correct options to traverse. If the player is in the main game and makes a mistake more than twice, the player would be prompted with the best node to visit next instead of continuing to fail. The quality of the loot is also an indicator of making the right decision for the next node.

## Story (Brief)

You play as a miner who is seeking to become rich so he explores caves looking to mine expensive minerals to sell. Getting these minerals is no easy task though, since these caves are infested with monsters who are eager to dine on our curious explorers. Fortunately, our miner has an ace up his sleeve, he has inherited maps which can guide him through the caves safely past the monsters and to the rarest of minerals. The miner must do this quickly or risk having his scent picked up by the monsters, ending up on the menu for them. 

## 

## Storyboarding


<img width="425" alt="Game Over Screen" src="https://github.com/user-attachments/assets/463c84db-52d7-40ed-96e2-9646bc3c089a" />

<img width="229" alt="Map" src="https://github.com/user-attachments/assets/743d5123-1fa8-4766-85fc-b9b23ca27946" />

<img width="307" alt="Cave" src="https://github.com/user-attachments/assets/39abe815-58f4-46e0-8037-68ce25bfa0e2" />

<img width="302" alt="Miner" src="https://github.com/user-attachments/assets/a0448824-4c35-42b7-b26b-da86c0ef239e" />

<img width="304" alt="Monster" src="https://github.com/user-attachments/assets/682552ab-b9ae-4bfb-9baf-daa0bea85e5c" />







# Assets Needed

## Aesthetics

The game starts out with a calmer atmosphere when the timer is full with calmer music. As the game progresses and the clock runs down or the player starts to make mistakes, the music would become more tense and the player would start to feel more pressure. The player may feel some sense of fear when the monsters start attacking them. The visuals are also mysterious, with low lighting in areas not illuminated with the flashlight. You should feel some sense of curiosity not knowing what or who is in the room with you until you explore.

## Graphical

- Characters List  
  - Main Character (Miner)  
    - Miner hat  
    - Tool Belt  
    - Backpack with Crystals in it  
  - Monsters  
    - Green or Red  
    - Horns and Fangs  
    - Possibly have weapons with them  
- Textures:  
  - Sparkles  
  - Dust from mining  
  - Dust cloud when walking  
- Environment Art/Textures:  
  - Stone (cave texture)  
  - Minerals  
  - Dungeon/cavern

## Audio

- Music List (Ambient sound)  
  - Calm, mysterious music for peaceful aspects  
  - Suspenseful, tense music for harder aspects  
- Sound List (SFX)  
  - Mining crystals  
  - Walking noise  
  - Hissing from monsters  
  - Noise when the player takes damage

# Metadata

* Template created by Austin Cory Bart [acbart@udel.edu](mailto:acbart@udel.edu), Mark Sheriff, Alec Markarian, and Benjamin Stanley.  
* Version 0.0.3

