# Game Design document

## Introduction
Don't go outside is a 2D platformer. The game will employ sprite-based animation, tiled foreground, collision detection, physics and gravity.


## Technology
The game will use the following libraries: 
* SFML
* nlohmann json
* Box2D
* Engine
* ECM 
* Tile loader
* maths.h 


## Objective
The objective of the game is for the player to make their way to the exit door by jumping from platform to platform. The player will be able to collect coins to score points and will have to avoid enemies.


## Levels
The levels were made using [Tiled](https://www.mapeditor.org/), this is a tile editor. It allows users to paint tile maps and then export them as a file. The file format that will be used is JSON. 
|
## Controls
The controls of the game will be:

| Control             |     Key    |
|---------------------|------------| 
|Move Left            | Left Arrow |
|Move Right           | Right Arrow|
|Jump                 | Up Arrow   |
|Interact with objects| E          |

## GUI/In-game menu
The game will will have a splash menu and a score menu. The GUI will display the players score and health.


## Artwork
In the engine library there is a system resource manger will be used to improve memory managment. 

| Art    | Link     |
|--------|----------|
|Tileset | [here](https://opengameart.org/contentplatformer-art-complete-pack-often-updated) |
| Backgrounds | [here](https://opengameart.org/content/backgrounds-for-2d-platformers) |


## Sound (sound effects)
In the engine library there is a system resource manger will be used to improve memory managment.

| Sound Effect    | Link |
|-----------------|------|
| Coin collecting | [here](https://opengameart.org/content/gold-coin-6) |
| Pulling lever   | [here](https://opengameart.org/content/mechanical-sounds) |
| Button press    | [here](https://opengameart.org/content/menu-selection-click) |

## Music
In the engine library there is a system resource manger will be used to improve memory managment.

| Music       | Link     |
|-------------|----------|
| Main Menu   | [here](https://opengameart.org/content/crystal-cave-song18) |
| Score Menu  | [here](https://opengameart.org/content/crystal-cave-song18) |
| Level One   | [here](https://opengameart.org/content/chill-loopable) |
| Level Two   | [here](https://opengameart.org/content/calm-ambient-2-synthwave-15k) |
| Level Three | [here](https://opengameart.org/content/a-chill-fever-loopable) |