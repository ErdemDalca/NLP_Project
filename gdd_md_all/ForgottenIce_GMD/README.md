# Slime Forest: Arcade Adventure - Game Design Document
This is my GDD (Game Design Document). The content of this document has changed over time. Check the [Git history](https://github.com/ForgottenIce/GMD/commits/main/Blogs/Game%20Design%20Document/README.md) of this file if you are curious.

## The General Ideas for My Game
- It's a 2D platformer
- Focus on tight controls (with inspiration from games like Celeste, SMW kaizo ROM hacks, IWBTG-fangames & Hollow Knight).
- Unlockable movement abilites that makes it possible to progress in new areas as well as previous areas.
- Maybe metroidvania (as in, one big explorable level)? If that isn't feasible it will be level-based progression instead.

## Milestone 1: A Test Level With a Playable Character
For the first milestone, my aim is to have a playable character with most of the moveset completed. The main focus is to experiment and find a control set that feels satistfying. There will also be a focus on creating the unlockable movement abilities, as well as other game object that the player can interact with (such as jump pads, dash orbs, etc.). A testing area will be built to test these things.

## Milestone 2: Player Sprites, Gameplay Elements & Level Building
This milestone will focus on implementing sprites for the different states the player can be in (idle, run, jump, dashing, etc.). There will also be a focus on implementing gameplay elements (like jump orbs, trampolines, etc.). And lastly, I will try and create the first level of the game.

## Milestone 3: State Machine, Enemies & UI Elements 
In this milestone, I would like to implement a state machine system. The player's movement script should be refactored to use this system. There will also be a focus on creating at least one enemy for the game, which could also be built using the state machine. Lastly, there will be a focus on implementing some UI elements.

## Game Ideas / Features to Implement
- Abilities
  - Dashing
  - Double jump
  - Speed boost
  - ~~Ceiling grab (stick to the ceiling)~~
  - ~~Gravity flip~~
- Trampolines / Bouncy objects
- ~~Pickup objects (such as trampolines, boxes or other stuff)~~

The above list is incomplete, and was created at the start of the course. Check out the [Game Showoff Blog Post](../Game%20Showoff/README.md) to see the final list of features in the game