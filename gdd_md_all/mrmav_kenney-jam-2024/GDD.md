# GDD - Magnum Opus The Quest.

THIS IS A WIP document

**A Game By:**
* mrmav @ https://mrmav.itch.io/
* serrot @  https://luistorres.itch.io/

# Introduction 
////

## Game Summary Pitch
////

## Inspiration
* Potion Craft (beta)
* Path of Exile skill tree game
* Dark Souls messages
* Journey the interaction with strangers

## Player Experience
Between a maze of options players can choose the alchemy path to their concoction, hopefully the highly regarded [[philosophers stone]].

After felling lucky with their choices players can Transmutate and try to create the stone. After, mostly likely failing, the player will get a result of how close he was to the concoction, percent based, and where in the path it went awry. Now the player is given the option to color their path in:
* nigredo (blackening), for bad paths
* albedo (whitening),  for better ones
* citrinitas (yellowing), almost there
* and rubedo (reddening), to hopefully mark the successful attempts in acquiring the concoction.

Score is based on how efficient the path is.

## Platform
WebGL & Mobile

## Development Software
* Godot 3.6rc1
* Kenney Assets
* Audacity
* Paint.net
* VSCode
* Github

## Genre
Multiplayer Player, puzzle, casual, clicker, social

## Target Audience
Casual players who are looking for a social challenge where they in will cooperative (or not) with strangers looking for a common but competitive objective eternal youth or something.

# Concept
## Gameplay overview
Player interacts with a node interface with a multitude of elements, and by trial and error they will look for the final solution.

## Theme Interpretations
This game was made for **two** game jams, for a more challenging experience
Bellow follows the themes Interpretations & the correspondent jam

### Connection
* [KenneyJam2024 https://itch.io/jam/kenney-jam-2024]
  
The player must navigate a maze of connections between elements, natural or not. This navigation is a overwhelming web of interface nodes.

### Alchemy
* [Pirate Software - Game Jam 15 https://itch.io/jam/pirate]
  
Players are challenged into discovering the recipe to the [[philosophers stone]].

### Shadows
* [Pirate Software - Game Jam 15 https://itch.io/jam/pirate]
  
Each run leaves it's shadow that can be seen by other players, (this shadow can have a custom color chosen by its maker). 

### Other Limitations
* Kenney Assets for the Kenney jam
* Single Button (this one was easy)
* Co-op (or maybe not)

## Primary Mechanics
Click!

## Secondary Mechanics
Hold?
# Art
The art will consist of modified ui elements and 2d sprites from Kenney. (Thanks Kenney)
Below follow how and which sprites and assets are used for what:

| Asset                       | Solution                                  |
| --------------------------- | ----------------------------------------- |
| Philosophers Stone          | 3D/TowerDefenseKit/detail_crystal         |
| Philosophers Stone Particle | 2D/JumperPack/particle_pink               |
| Background                  | 2D/CartographyPack/Papers                 |
| Base Elements               | 2d/Planets                                |
| Outer Elements              | 2D/InterfacePack/minimapMap_blank         |
| The Squared Circle          | 2D/PatternPack2/Thin Edited merged shapes |
| Selection Particles         | 2D/VoxelPack/Particles/swirl_white        |
| Ribbitonious                | 2D/Animal                                 |
| Hat                         | 2D/ScribblePlatformer                     |
| Banner                      | 2D/InterfacePack/bannerScroll             |



# Audio

# UX
The overall player UX should be streamlined and quick. Given the limited mechanics present the visuals and animation will do most of the heavy lifting, when it comes to exploration and novelty.

## User Interface 
Player sees a basic popup style menu where they have Transmute(Play), settings, leader board, exit options

After Concoction is made player can chose between on the color and are incentivize to use them according ot the following description:
**Nigredo**: Facing and purging inner darkness.
**Albedo**: Achieving purification and spiritual clarity.
**Citrinitas**: Gaining wisdom and deeper understanding.
**Rubedo**: Reaching unity and enlightenment.

## Controls

* Mouse
	* Right Click - Primary Action
	* Left Click -- Secondary Action
* Touch Screen
	* Tap --------- Primary Action
	* Hold -------- Secondary Action
* 
# Development
Below follows the rough dev plan.

## MVP

| Feature                   | Importance 1-5 | Budget (hh) | Status |
| ------------------------- | :------------: | :---------: | :----: |
| Node interface            |       5        |      4      |   -    |
| Previous attempt Paths    |       5        |      4      |   -    |
| Colored Path              |       3        |      2      |   -    |
| Win Condition             |       5        |      2      |   -    |
| Lose Condition            |       5        |      2      |   -    |
| Multiplayer Previous Runs |       5        |      8      |   -    |
| Multiplayer LeaderBoard   |       3        |      2      |   -    |

  
## Goodies & Extras
| Feature                                  | Importance 1-5 | Budget (hh) | Status |
| ---------------------------------------- | :------------: | :---------: | :----: |
| Settings Menu                            |       1        |      4      |   -    |
| Colorblind support                       |       2        |      2      |   -    |
| Daily recipe (A* Pathfinding generated?) |       2        |      2      |   -    |
| Daily Leader Board                       |       2        |      2      |   -    |
| All Time Leader Board                    |       2        |      2      |   -    |
