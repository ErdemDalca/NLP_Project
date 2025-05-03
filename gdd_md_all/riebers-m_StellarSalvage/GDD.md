# Game Design Document

## Game Title

**Stellar Salvage**

## Game Overview

**Stellar Salvage** is a 2D action-adventure game where players control a small spaceship from a top-down perspective.
The main objective is to navigate through space, collect valuable items, move obstacles like asteroids, and destroy
enemies to progress through levels.

## Table of Contents

1. [Game Concept](#game-concept)
2. [Gameplay Mechanics](#gameplay-mechanics)
3. [Game World](#game-world)
4. [Characters and Entities](#characters-and-entities)
5. [User Interface](#user-interface)
6. [Controls](#controls)
7. [Art and Sound](#art-and-sound)
8. [Technical Requirements](#technical-requirements)
9. [Development Timeline](#development-timeline)
10. [Architecture](#architecture)

## Game Concept

### Genre

- Action
- Adventure

### Platform

- PC (Windows, macOS, Linux)

### Target Audience

- Ages 10 and up
- Fans of space-themed games and action-adventure games

## Gameplay Mechanics

### Core Mechanics

- **Spaceship Control**: Players can move the spaceship in all directions using keyboard inputs.
- **Item Collection**: Players collect items scattered throughout the levels for points or power-ups.
- **Obstacle Interaction**: Players can move asteroids and other objects to clear paths or solve puzzles.
- **Combat**: Players can shoot projectiles to destroy enemies and obstacles.

### Objectives

- **Primary Objective**: Collect all valuable items in a level to advance to the next.
- **Secondary Objectives**: Destroy enemies, avoid or move obstacles, and achieve high scores.

### Progression

- Levels become progressively more difficult with more enemies, complex obstacles, and intricate layouts.

## Game World

### Setting

- The game is set in various sectors of space, each with unique backgrounds, obstacles, and enemy types.

### Levels

- **Sector 1**: Introduction to basic mechanics with few enemies and simple obstacles.
- **Sector 2**: Increased number of enemies and introduction of moving asteroids.
- **Sector 3**: Complex layouts requiring strategic movement and item collection.
- **Sector 4**: Advanced enemies with unique behaviors and more challenging item locations.
- **Sector 5**: Boss level with a powerful enemy guarding the final item collection.

## Characters and Entities

### Player Character

- **Spaceship**: The player's avatar with capabilities to move, shoot, and interact with the game world.

### Non-Player Characters

- **Enemies**: Various types of hostile entities with different behaviors and attack patterns.
- **Asteroids**: Moveable obstacles that can be used strategically to block enemy paths or create safe zones.
- **Items**: Collectible objects that provide points or power-ups.

## User Interface

### Main Menu

- Start Game
- Options (Settings for audio, controls, etc.)
- Exit

### In-Game HUD

- **Score**: Displays the current score based on collected items and defeated enemies.
- **Health**: Shows the spaceship's current health status.
- **Mini-Map**: Provides an overview of the current level layout.

### Pause Menu

- Resume Game
- Options
- Main Menu

## Controls

- **Movement**: The spaceship moves towards the direction of the mouse pointer when the movement key is held down. The movement key could be one of the following:
  - **W Key** (default) or any custom key set by the player. While the movement key is held down, the spaceship continuously accelerates towards the mouse pointer, allowing precise control over direction and speed.
  - **Shift Key** can be used to activate a temporary speed boost while moving.

- **Shooting**:
  - **Main Weapon (Primary Fire)**: Press and hold the **Left Mouse Button** to continuously fire the spaceship's main weapon in the direction the spaceship is facing (towards the mouse pointer). This weapon is designed for regular combat and has a steady rate of fire.
  - **Secondary Weapon (Secondary Fire)**: Press and hold the **Right Mouse Button** to fire the spaceship's secondary weapon. This weapon might have different properties, such as a slower fire rate, higher damage, or area-of-effect impact. The secondary weapon could also be a chargeable weapon that becomes more powerful the longer the right mouse button is held.

- **Interaction**:
  - **E Key** or **Middle Mouse Button**: Use this to interact with objects in the game world, such as moving asteroids or activating switches.

- **Pause**:
  - **Escape Key**: Press to pause the game and bring up the pause menu, where you can resume, adjust settings, or return to the main menu.

### Additional Considerations

- **Mouse Sensitivity**: Allow players to adjust mouse sensitivity in the settings to ensure smooth control over the spaceship's movement and targeting.
- **Customizable Controls**: Include an option in the settings menu for players to remap the controls according to their preferences. This is particularly important for accessibility.
- **Visual Indicators**: When the movement key is held, a visual indicator (such as a small arrow or a trail) could show the direction of movement towards the mouse pointer, helping players align their movement with their intended trajectory.
- **Aim Assist (Optional)**: Consider implementing a light aim assist for players to help with precision when targeting fast-moving enemies. This could be especially useful for less experienced players.

## Art and Sound

### Art Style

- 2D pixel art with a vibrant color palette to depict various space environments and entities.

### Sound Effects

- **Spaceship Movement**: Subtle thruster sounds.
- **Item Collection**: A pleasant chime or beep.
- **Shooting**: Laser or projectile sound effects.
- **Enemy Destruction**: Explosion or destruction sound.

### Music

- Ambient space-themed background music with increasing intensity for higher levels.

## Technical Requirements

### Software

- C++ with SDL or SFML for rendering.
- CMake for build configuration.
- Any text editor or IDE for coding (e.g., Visual Studio, CLion, or VS Code).

### Hardware

- Minimum:
  - CPU: Dual-core processor
  - RAM: 2 GB
  - Graphics: Integrated graphics
  - Storage: 100 MB available space

## Development Timeline

### Milestones

1. **Week 1-2**: Project setup, basic game loop, and rendering backend abstraction.
2. **Week 3-4**: Implement spaceship movement, basic item collection, and simple obstacles.
3. **Week 5-6**: Add enemy entities and basic combat mechanics.
4. **Week 7-8**: Level design and progression mechanics.
5. **Week 9-10**: User interface and HUD implementation.
6. **Week 11-12**: Art and sound integration.
7. **Week 13-14**: Testing, bug fixing, and polish.
8. **Week 15**: Final testing and release preparation.

## Architecture

### Design Pattern: Functional Core, Imperative Shell

**Stellar Salvage** is designed using the **Functional Core, Imperative Shell** architecture pattern. This approach ensures that the core logic of the game is highly testable, isolated from external dependencies, and maintains a clear separation of concerns between the game logic and the system-specific operations.

### Core Logic

The core logic is built around an **Entity Component System (ECS)**, which is responsible for managing game entities and their interactions. The core components include:

- **Entities**: Represent individual game objects (e.g., spaceship, enemies, asteroids).
- **Components**: Define specific attributes or behaviors (e.g., position, health, movement).
- **Systems**: Implement the logic that operates on entities and their components (e.g., collision detection, movement, rendering).

### Imperative Shell

The **Imperative Shell** abstracts the platform-specific and rendering backend details. It interfaces with the core logic to handle tasks such as:

- **Rendering**: Drawing the game world and entities on the screen.
- **Input Handling**: Processing player inputs (e.g., keyboard, mouse).
- **Audio**: Managing sound effects and background music.
- **Resource Management**: Loading and managing game assets like textures, sounds, and levels.

This separation allows the core game logic to be developed and tested independently of the rendering engine or platform, promoting cleaner code and easier maintenance.

## Conclusion

**Stellar Salvage** aims to provide an engaging and challenging space adventure for players of all ages. With its core mechanics, progressively challenging levels, vibrant art style, and a robust architecture, it promises to be an exciting addition to the action-adventure genre.
