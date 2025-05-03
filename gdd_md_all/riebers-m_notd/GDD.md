# Game Design Document for **Night of the Dead**

## Table of Contents
1. [Game Overview](#1-game-overview)
2. [Game Mechanics](#2-game-mechanics)
3. [Game World](#3-game-world)
4. [Game Progression](#4-game-progression)
5. [User Interface (UI)](#5-user-interface-ui)
6. [Audio](#6-audio)
7. [Art Style](#7-art-style)
8. [Technical Specifications](#8-technical-specifications)
9. [Future Development & DLC Ideas](#9-future-development--dlc-ideas)

---

## 1. Game Overview

### Game Concept
**Night of the Dead** is a survival-action game where the player controls a soldier who wakes up in a city overrun by undead and zombies. With limited starting equipment, players must explore the procedurally generated environment, gather resources, defeat enemies, and improve their combat skills to escape the city. The game features an isometric view and random events that challenge players as they try to survive.

### Genre
- Survival Action
- Roguelike Elements
- Procedurally Generated

### Platform
- PC (Windows/Linux) using SFML

### Target Audience
- Players aged 16+
- Fans of survival-action and roguelike games
- Players who enjoy games with procedurally generated environments and replayability

---

## 2. Game Mechanics

### Core Gameplay
- **Survival**: The player must gather items, defeat undead enemies, and survive long enough to escape the city.
- **Combat**: The player uses a combination of firearms, melee weapons, and explosives. Enemies get progressively more dangerous.
- **Procedural Generation**: Each time the game starts, the layout of the city is different. Loot, enemies, and events are randomized.
- **Resource Management**: Players manage weapons, ammo, health, and items they gather from the environment or fallen enemies.

### Player Controls
- **Movement**: Controlled via keyboard (WASD or arrow keys) with mouse aiming for combat.
- **Combat Actions**: Left-click to shoot, right-click to aim, other keys for melee, throw grenades, etc.
- **Inventory Management**: Accessible via a quick-access key or menu, where players can equip items, use consumables, and check stats.

### Combat System
- **Weapons**: Ranged (guns, crossbows), melee (knives, bats), and throwable items (grenades, Molotov cocktails).
- **Enemy Types**: Standard zombies, fast-moving undead, boss-like enemies, and swarms of weaker enemies.
- **Health and Armor**: Players have a health and armor system; armor reduces damage, while health must be restored with items.

### Procedural Generation
- **City Layout**: Procedurally generated maps with varying streets, buildings, and hidden areas. Every game feels different.
- **Random Events**: Quest events and encounters are generated dynamically, offering the player side-objectives and rewards.

### Inventory and Equipment
- **Inventory**: Players can hold multiple items, manage their loadout, and equip weapons or armor.
- **Looting System**: Items can be scavenged from the environment, looted from enemies, or found in hidden areas.
- **Upgrading**: Players can find attachments or upgrades for weapons and equipment to improve performance.

---

## 3. Game World

### Setting and Atmosphere
- **City Environment**: A desolate urban landscape overrun by zombies. The atmosphere is dark, oppressive, with a strong survival-horror feel.
- **Day/Night Cycle**: A dynamic day/night cycle where enemies become more aggressive at night.
- **Interactive Objects**: Players can interact with doors, windows, and environmental traps (explosive barrels, etc.).

### Environment Design
- **Isometric View**: The game uses an isometric view, providing tactical awareness of surroundings.
- **City Features**: Players can explore abandoned buildings, streets, and sewers, with occasional safehouses scattered throughout.

### Procedural World Generation
- **Layout**: Each playthrough generates a new city map, with randomized streets, buildings, loot placements, and enemies.
- **Special Areas**: Rare locations (like military bunkers or labs) provide higher-tier loot and tougher challenges.

### NPCs and Enemies
- **Enemies**: Various types of undead, ranging from slow-moving zombies to aggressive, fast-moving creatures.
- **AI Behavior**: Enemies patrol areas, react to noise, and become more dangerous in larger groups or at night.

---

## 4. Game Progression

### Objectives and Quests
- **Main Goal**: Escape the city by locating key areas (exits, safe zones) and completing objectives to unlock pathways.
- **Side Quests**: Randomized quests that reward the player with rare items or weapons (e.g., rescue survivors, secure resources).

### Difficulty Levels
- **Dynamic Difficulty**: The game gets harder as players progress, with more challenging enemies and fewer resources.
- **Difficulty Options**: Players can select from easy, normal, and hard modes, affecting enemy strength and resource availability.

### Player Progression
- **Experience and Skills**: Players gain experience by defeating enemies and completing quests, unlocking new skills or abilities.
- **Equipment Upgrades**: Weapons and armor can be upgraded through attachments or by finding higher-tier equipment.

---

## 5. User Interface (UI)

### HUD (Heads-Up Display)
- **Health and Armor**: Displayed in the corner, showing the player's current status.
- **Ammo and Inventory**: A quick-access display of ammo count and current weapons.
- **Quest Log**: A minimal quest log showing active objectives and progress.

### Menus
- **Main Menu**: New Game, Load Game, Settings, Exit.
- **Inventory Menu**: Allows players to equip, use, or drop items.
- **Pause Menu**: Allows players to save the game, adjust settings, or quit.

---

## 6. Audio

### Sound Effects (SFX)
- **Combat Sounds**: Gunshots, melee impacts, enemy growls, and explosions.
- **Environmental Sounds**: Footsteps, distant moans, wind, and other city-related ambient noises.

### Music
- **Dynamic Music**: Music that changes based on the player's situation (calm during exploration, intense during combat).
- **Theme**: Dark, atmospheric music to enhance the horror and survival feel.

---

## 7. Art Style

### Visual Design
- **Isometric Pixel Art**: A mix of 2D pixel art with 3D lighting and effects to create a unique atmosphere.
- **Dark Tones**: A focus on dark, moody color palettes to enhance the feeling of danger and isolation.

### Animation
- **Character Animations**: Smooth, fluid animations for movement, combat, and interactions.
- **Enemy Animations**: Each enemy type has distinct movement and attack animations to differentiate them in gameplay.

---

## 8. Technical Specifications

### Tools and Technologies
- **Game Engine**: Built using SFML (Simple and Fast Multimedia Library) for 2D graphics.
- **ECS (Entity Component System)**: A custom-built ECS for handling game entities and components efficiently.

### Performance Requirements
- **Minimum Specs**: Mid-tier CPU, GPU with basic 3D rendering support, 4GB RAM.
- **Recommended Specs**: Higher CPU and GPU for smoother procedural generation and rendering.

---

## 9. Future Development & DLC Ideas

- **Co-op Mode**: Add a multiplayer mode where players can team up to survive together.
- **New Enemy Types**: Introduce more complex enemies like zombie bosses, intelligent undead, or military squads.
- **Map Expansions**: Add new city districts or unique biomes like forests or underground tunnels.
- **Survival Mode**: A timed mode where players see how long they can last against waves of enemies.

---
