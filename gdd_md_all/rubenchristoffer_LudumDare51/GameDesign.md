# Game Design Document


A game design document is living document which describes the intent of the game design. 
It has two goals, first to document the decisions that have been made about the game and communicate those concepts to the entire team. 
Thus, it needs to be detailed enough for programmers to refer to when they need clarification about an aspect of the game. 
It must be able to be updated as the game is to be built. 
The need to have a game design document increases with the size of the team and length of the project. 

For a student project the intent is to capture as much as possible of your design. 
The game design will be larger than what you can achieve in a semester, but you must then decide what you need to do first. 
This document should be in version control so that you can see it changing and growing. 
Given we are using git you could also use @name to assign parts of the design to individual members of the team.


## Overview
*Name* , *Team*

### Game Concept
What the game is about?

Procedurally generated tiles. Don't die (roguelike). Use money to expand an area. Gather clues to find your way to the exit. 

Ideas regarding theme:
1. Spawn enemies every 10 seconds
2. Gain money every 10 seconds (you don't gain currentcy by killing enemies)
3. Lose money every 10 seconds (gotta go fast)
4. Switch gravity every 10 seconds
5. Can only go through passage/tile on the 10's second mark (you have to time it)

Ideas regarding clues:
1. Clue that points to another clue
  - Randomized "max" clues until the final destination is revealed

2. Pre-defined path of nodes to exit. All other nodes point to closest node on the pre-defined path. 

### Genre
What other games is it like?

Procedural escape-room "kinda" roguelike dungeon crawler

### Target Audience
Who will play it?

Indie nerds. 

### Game Flow Summary
How does the player move through the game?

Move through tiled areas until exit is found. 

### Look and Feel
What is the basic look and feel of the game?  What is the visual style?

Pixel art.

## Gameplay and Mechanics
What does the player do?

Move
Attack
Buy tiles
Interact with clues

### Gameplay
What is the core of the players interaction with the game?

Expand tiles and survive to reach the exit. Make sure the player stays alive!

#### Game progression
How does the player progress through the experience and how do they know they are making progress?

Finding clues that indicate a step towards the exit. 

#### Mission/challenge Structure
Is there a heirachy to the challenges in the game?

Every level is more difficult than the last. 
Good and bad modifiers that amplifies every 10 seconds. 

#### Puzzle Structure
Are there puzzles, ie challenges that have a correct answer?

Nope. 

#### Objectives
What is the player trying to achieve?

FREEDOM. 

### Mechanics
What are the rules to the game, both implicit and explicit?  
This is the model of the universe that the game works under.  
Think of it as a simulation of a world. How do all the pieces interact?

#### Physics
How does the physical universe work?

Everything is darkness except the tiles you own. 
Enemies have hitboxes (colliders)

#### Movement
How the player interacts with the game?

WASD - Move up, left, down, right. 
E - Interact / Buy spaces
Space - Attack

#### Objects
What are the objects in the game?
How does the player interact with them?

Red spinning arrow? Interact to stop arrow that will point towards next clue (it will turn green). 
Compass. 

#### Actions
What are the other interactions the player has with the game world?

Go to next level.

Select modifiers?

#### Combat
If there is combat or conflict, how is this specifically modeled?

Melee only (for now) 

#### Economy
What is the economy of the game? How does it work?

Cash money.

Mana?

#### Screne Flow
A graphical description of how each screne is related to every other and a description of the purpose of each screen.

Very simple main menu that overlays a new game. 

### Game Options
What are the options and how do they affect gameplay and mechanics?

### Replay and Saving

No?

### Cheats and Easter Eggs

Egg tile?

## The Story, Setting, and Character

### Story and Narrative
If there is a story component includes back story, plot elements, game progression, and cut scenes. 
Cut scenes descriptions include the actors, the setting, and the storyboard or script.

No. 

### Game World
The setting of the game

#### General look and feel of the World
Aesthetics

Minimalistic pixel art.

#### Areas
including the general description and physical characteristics as well as how it relates to the rest of the world 
(what levels use it, how it connects to other areas).

Unlocks as you go. 

### Characters
Each character should include the back story, personality, appearance, animations, abilities, relevance to the story and relationship to other characters.

## Levels

Infinite. Procedurally generated. 

### Playing Levels
Each level should include a synopsis, the required introductory material (and how it is provided), the objectives, 
and the details of what happens in the level.  
Depending on the game, this may include the physical description of the map, the critical path that the player needs to take, 
and what encounters are important or incidental.

### Training level
How is onboarding managed?

No

## Interface

### Visual System
If you have a HUD, what is on it?  What menus are you displaying? What is the camera model?

Health bar
Cash with symbol
Current 10-second cycle/tick

Modifier?

### Control System
How does the game player control the game?   What are the specific commands?

### Audio, Music, Sound Effects

Enemy attack
Player attack
Player move
Sound every cycle / tick - not in the way, subtle
Unlock area sound?
Yay woo sound, you've done good :)

### Help System

No.

## Artificial Intelligence

Normal AI: Very simple. Attack when possible. Move towards player when attacking, move away when recharging attack. 

### Opponent and Enemy AI
The active opponent that plays against the player and therefore requires strategic decision making.

### Non-combat and Friendly Characters

No. 

### Support AI

No. 

### Player and Collision Detection, Path-finding.

Hitboxes, but nothing other than that. Stop player from going outside level boundaries. 

## Technical

### Target Hardware

From potato to NASA space rocket (depending on how far you have come :)). 

### Development Hardware and Software (including game engine)

Unity 2020.3.40f1.

### Network requirements

None. 

## Game Art

### Key assets 
How are they being developed.  Intended style.

Johannes fikser. 

This is an extension of parts of [cs.unc.edu](http://wwwx.cs.unc.edu/Courses/comp585-s11/585GameDesignDocumentTemplate.docx)


