# Game design document

# Farming Valley - Game Design Document

## 1. Introduction

*Farming Valley is a Cozy Roguelike VR Farming Game that combines relaxing farm management with procedurally generated environments and roguelike survival elements.*

## 2. Game Overview

### 2.1 Concept

We can use the previous version of Farming Valley as a base for the game, but since it’s too old it’s better to start a new project. 

As a start and to make some progress fast, we can reuse as much as possible from [[Meta Quest 2 - VR] Life at Pixel Farm by Sorskoot (itch.io)](https://sorskoot.itch.io/life-at-pixel-farm)

### 2.2 Player Experience Goals

*Players should feel a sense of relaxation and accomplishment from farming and resource management, alongside the thrill of exploring new and unpredictable environments.*

## 3. Gameplay

### 3.1 Mechanics

- Daylight cycle is used as the turns of the roguelike.
    - It'll not be happening automatically, but when the player ends their turn it becomes night.
    - The next day starts with a rooster announcing the new morning. 

### 3.2 Roguelike Elements

*Details on procedurally generated fields, permadeath, and how it affects gameplay.*

- The World is procedurally generated. By using a seed the world should be endless. You start with a basic set of tiles you can walk around in and work with. The rest is up to RNG
- When you’re out of money the game ends, and the world is gone.
- 

### 3.3 Farming and Resource Management

Resources: crops, animals

Tools: Hoe, watering can, etc

Building materials: to create pens. 

Cards with different items and levels.

- Corn
- Watering can
    - Leaky
    - Small
- Well
- Carrots
- Wees

Crows and wolves will come at some point to eat crops and animals. You need to keep those away (scarecrow, traps).

### 3.4 Progression and Rewards

*Outline of player progression, skill upgrades, and in-game rewards.*

### 3.5 Game Loop

This is the rough idea for the game loop. 

**Initialize the Game World**

- Procedurally generate the game world (fields, weather, seasons)

- World will be generated using wave form collapse algorithm to make sure there’s always a certain amount of specific ‘tiles’ available at the start.

- Place initial resources and obstacles like water, trees, rocks.

1. **Character Creation**
    - Player chooses a character or randomly generates one with unique traits/skills
2. **Game Loop Start**
    - Hoe ground: player moves in a grid, turn-based fashion to till the land
    - Plant seeds/seedlings: introduce random seed types with unique grow times and benefits
    - Water plants: manage water resources which can vary depending on weather conditions
3. **Player Interaction**
    - Sleep is ending the turn.
    - Remove overgrowth: RNG-based events cause overgrowth that must be cleared
    - Combat pests/diseases or birds/preditors: introduce enemies in the form of pests
    - Repeat steps 3-5: incorporating RNG for weather, plant growth success, pest attacks
4. **Harvest and Profit**
    - Harvest: success based on player's actions throughout the loop
    - Sell crops: fluctuating market prices affect profit
5. **Roguelike Progression**
    - Permanent upgrades or knowledge that can be used in the next run
    - Death or failure: permadeath leads to game over, but with the potential for new starting bonuses
6. **End of Loop**
    - Evaluate performance, provide score or resources for next run
    - Loop back to start but with increased difficulty or variation
7. **Meta Progression**
    - Unlock new seeds, tools, or character traits for future runs
    - Achieve specific milestones that carry over to new games

Repeat this loop, each iteration offering a new challenge or twist to keep the gameplay fresh and engaging.

## 4. Virtual Reality Integration

### 4.1 Immersion

*How VR contributes to the sense of presence within Farming Valley.*

### 4.2 VR Mechanics

*Specific interactions that are unique to VR, such as planting, harvesting, and tool use.*

## 5. Art and Audio

### 5.1 Visual Style

Pixel Art, Low poly

### 5.2 Audio

*Approach to sound design that enhances the immersive experience.*

## 6. Technical

### 6.1 Engine

- Wonderland Engine.

### 6.2 Platforms

Focus on Quest 3, but it should run everywhere WebXR works. 

No support for desktop.

### 6.3 Frameworks

- @sorskoot/wonderland-components (github:sorskoot/SorskootWonderlandComponents)
- rxjs
- @tweenjs/tween.js 

Optional:

- tsyringe


## 7. Marketing and Monetization

### 7.1 Target Audience

*Definition of the primary market for Farming Valley.*

### 7.2 Monetization Strategy

*Plan for generating revenue, including potential DLCs, in-app purchases, etc.*

---

## Live streams

**2024-03-18**
- Add a few libraries we will need
- Start working on the basics of the world generation

---


*This document is a first draft and subject to change as the development of Farming Valley progresses.*

