# MOWER MAYHEM Game Design Document

[Google Docs](https://docs.google.com/document/d/17fQRRZAxU0p46rq8_0EtXGiUOwAG26MZjd8QWxwoxSk/edit?usp=sharing)

## Introduction
### Overview
Mower Mayhem is an immersive, action-packed game where players take on the role of a skilled landscaper battling against time, enemies, and obstacles to transform ordinary lawns into legendary masterpieces.

### Description of Concept
In the bustling world of [Game Title], players step into the shoes of a skilled landscaper with a mission to transform ordinary lawns into legendary masterpieces. The game introduces a dynamic blend of hyper-casual and action-packed gameplay, where the art of lawn mowing becomes a thrilling adventure.

Embark on a journey across thematic worlds and real-world farms, each presenting unique challenges and obstacles. The core concept revolves around the player's ability to cut all the grass within a designated time frame while navigating through a variety of static obstacles and encountering mischievous enemies like moles, tractors (in later development), bees, and crows (also in later development).

The gameplay loop involves selecting a level, attempting to complete it successfully, and earning coins that can be utilized to upgrade the lawnmower. As players progress through levels, they unlock new challenges and encounter escalating difficulty, ensuring a satisfying and competitive experience.

The game's central objectives include mastering the art of precision lawn mowing, avoiding obstacles and enemy attacks, and strategically upgrading the lawnmower for enhanced performance. Collectables such as badges, coins, and health add an extra layer of engagement to the gameplay.

[Game Title] sets itself apart with its unique selling points, delivering a perfect balance of competitiveness, visually stunning landscapes, and opportunities for character personalization. Drawing inspiration from iconic titles like Minecraft, Hill Climb Racing, and Breath of the Wild, the game promises not only a satisfying gameplay experience but also a visually immersive journey through diverse environments.

Get ready to dive into the world of [Game Title], where every mow counts, and the race against time transforms mundane lawns into legendary turf triumphs.

### Objective and Goals
Cut all grass within the time frame.
Avoid obstacles/enemies attacks.
Upgrade vehicle features.
Collectables
Badges (Leaderboards Token) - position on leaderboard based on total.
Coins
Health

## Game Concept

### High-Level Overview
[Game Title] offers a unique blend of hyper-casual and action gameplay, challenging players to become the ultimate landscaper. With a focus on satisfying gameplay and competitive elements, the game combines amazing visuals with character personalization for an engaging experience. Inspired by titles like Minecraft, Hill Climb Racing, and Breath of the Wild, [Game Title] promises an exciting journey through thematic worlds and real-world farms.

### Target Audience
Plus Twelve. ( 12+ )
Unique Selling Points
Satisfying gameplay.
Perfect amount of competitiveness.
Amazing Visuals.
Character personalization.

### Inspirations and Influence
Minecraft - Sound design.
Hill climb Racing - Upgrade system.
Breath of the wild - Visual style.

## Genre And Setting
Game Genre
Hyper casual / Action 

### Setting and World
Farms that compete in mowing competitions. Modern setting plus extra thematic worlds.

Environment Settings:
Real world farm.

## Gameplay Mechanics
### Core Gameplay Loop
Select a level
Try to complete the level
Upgrade the lawnmower

### Player Objectives
After entering a level, the player needs to cut all the grass from the level while trying to dodge obstacles and enemies. The level ends successfully when all grass is cut, or it fails if the player is hit by an obstacle or enemy. Grab Collectables. Upgrade vehicle.

### Controls
To control the main character, the player will use a touch analog.

Vertical Screen

### Progression System
After completing a level successfully, the next level is unlocked.
With the coins earned from the levels the player can upgrade their vehicle.

### Levels and Challenges
Every level will be unique and will have its set of challenges. The main challenge will be cutting all grass under a time limit while dodging enemy attack’s and obstacles.
Static Obstacles:
Rocks
Tree
Enemies:
Mole
Tractor [Later Development]
Bees [Later Development]
Crow [Later Development]

## Characters
### Playable Characters
[Add main character description here]
### Non-Playable Characters
Enemies:
Mole


## User Interface
Main Menu
Start
Garage/Store
Settings
Music
Sound
Unlock Ads
Start>Level Select
Back Button
Levels
Brief level description
Time to complete
Highscores
Loading
Fisip Group Logo
In game
Countdown to start
Joystick
Vehicle Health
Currency
Time to Complete
Pause
Settings
Quit
Restart
Win/Lose
Time Finished/Game Over
Currency Gained, unless lost
Highscore Check?
Extra Time, with Ads/Revive, with Ads
Redo/Try again


## Art and Visuals
Mix farming and racing elements, and have a UI to match.
Audio and Music
Music:
Main menu
Gameplay
Audio:
Menu button clicks
Race begin.
Race countdown
Race end
Grass cut



## Level Design
Overview of Levels
For the creation of the levels, a procedural level creation system will be created to help with development. 
This system will be responsible in generating:
Map layouts
Obstacles
Enemies
Coins
Decoration
Grass
Background
Completion Time
Save Level into file
Load file into Level
The system will also have certain parameters to set how a level should be generated:
Size 
Obstacles Frequency
Enemies Frequency
Coins Frequency
Grass Frequency
Level Progression
Upon successfully completing a level within the designated time frame, players unlock the opportunity to progress to the next stage. Additionally, they have the option to re-do completed levels, either to amass additional in-game currency or to vie for top positions on the leaderboards.
The accessibility of levels is facilitated through a user-friendly level select panel, enabling players to seamlessly navigate and choose their desired challenges.
As players advance through the game, they will encounter escalating difficulty levels characterized by longer gameplay durations and more intricate obstacles, providing a progressively challenging and engaging experience.

## Monetization
For monetization, we will use Unity’s In-App Purchasing Service, since It supports both the Apple App Store and Google Play Store.

### In-App Purchases
Coins
No advertising subscription.
Limited time offer.

### Ads Strategy
Advertisement video at end of level.
Watch video to get bonus coins.
Watch video to earn 2x, 3X, 5X Coins

### Premium Features
Subscription to remove advertising.

## Technical Specifications
### Target Platforms
iOS
Android
### Target Devices
Phone
Tablet