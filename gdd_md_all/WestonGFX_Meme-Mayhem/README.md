# Pepe's Meme Mayhem

**Pepe's Meme Mayhem** is a roguelite, top–down shooter inspired by *The Binding of Isaac* but with a unique twist: a Twitch meme/Pepe the Frog theme with deep item synergy, dynamic resource management, and a chaotic gameplay experience. Every run is unpredictable—items interact in cascading ways, creating explosive chain–reaction effects that change your playstyle every time you play.

---

## Table of Contents

- [Game Overview](#game-overview)
- [Features](#features)
- [Gameplay Mechanics](#gameplay-mechanics)
- [Tech Stack Options](#tech-stack-options)

---

## Game Overview

**Pepe's Meme Mayhem** is a fast–paced roguelite shooter where every run is a unique, meme-filled adventure. Inspired by the gameplay of *The Binding of Isaac*, it features procedurally generated dungeons, randomized enemy spawns, deep resource management, and, most importantly, a robust synergy system. Every item—from coins to power-ups—interacts in unpredictable ways, leading to explosive, chain–reacting effects that can clear entire rooms if you manage your build correctly.

Set in a world where Twitch memes, rare Pepe imagery, and internet culture collide, the game offers a tongue-in-cheek experience that is both challenging and entertaining. Whether you're battling bosses that adapt to your synergy build or exploring rooms filled with hidden secrets, every playthrough is different, ensuring endless replayability.

---

## Features

- **Procedurally Generated Dungeons:** 
  - Randomized rooms with obstacles, enemies, loot, and secret areas.
  
- **Deep Synergy System:** 
  - Items interact in unexpected ways. For example, combining "Heat Rocket" with "Attack Speed" can spawn additional projectiles leading to explosive chain reactions.
  
- **Resource Management:**
  - Manage coins, bombs, keys, hearts, tarot cards, and rerolls to optimize your build and survive longer runs.
  
- **Dynamic Boss Battles:**
  - Boss enemies that transform based on your synergy build, with multiple phases and evolving attack patterns.
  
- **Interactive Environments:**
  - Bombable walls, donation machines, and beggars add an extra layer of strategy.
  
- **Unique Shop System:**
  - In–game shop offers upgrades and “meme packs” that temporarily alter synergy rules.
  
- **Time–Shift Effects:**
  - Trigger temporary slow-motion effects to emphasize cascading synergy interactions.
  
- **Robust Audio & Visual Effects:**
  - Particle effects, screen shakes, and a dynamic soundtrack enhance the chaotic gameplay experience.
  
- **Modding API:**
  - Easily extend the game with custom items, synergy rules, and enemy behaviors.
  
- **Multiple Tech Stack Options:**
  - The project is designed to be implemented using various technologies (C++ with SDL2, C# with Unity, Godot, JavaScript with Phaser, etc.).

---

## Gameplay Mechanics

- **Movement & Shooting:**  
  Move using WASD or arrow keys and shoot with the left mouse button. The player rotates to face the mouse cursor.

- **Synergy Overload:**  
  When specific items (e.g., "Heat Rocket" and "Attack Speed") are in your inventory, a synergy overload effect is triggered, amplifying your damage or spawning additional projectiles.

- **Procedural Generation:**  
  Each floor is generated randomly, including room layouts, enemy placements, loot, and environmental hazards.

- **Resource Decisions:**  
  Spend coins at shops, use bombs to destroy walls for hidden rewards, and manage other resources to keep progressing.

- **Boss Battles:**  
  Bosses are not only challenging but adapt based on your synergy builds, providing a fresh challenge every run.

---

## Tech Stack Options

This project can be built using various languages and engines. Here are 6 different approaches along with their pros, cons, and best use cases:

1. **C++ with SDL2/OpenGL:**  
   _Pros:_ High performance, full control, cross-platform.  
   _Cons:_ Steep learning curve, slower development.  
   _Best Use Case:_ When maximum optimization and engine customization are required.

2. **C# with Unity:**  
   _Pros:_ Rapid prototyping, built-in tools, large community.  
   _Cons:_ Requires learning Unity’s workflow, potential asset costs.  
   _Best Use Case:_ For polished, professional 2D games with rich toolsets.

3. **Godot with GDScript:**  
   _Pros:_ Lightweight, Python–like scripting, open source.  
   _Cons:_ Smaller ecosystem, less professional support.  
   _Best Use Case:_ Indie 2D roguelites with rapid iteration.

4. **Java with libGDX:**  
   _Pros:_ Cross-platform, robust framework, good performance.  
   _Cons:_ Verbose, steeper setup.  
   _Best Use Case:_ When you need balance between control and rapid development.

5. **JavaScript with Phaser:**  
   _Pros:_ Web-based, easy to deploy, lots of tutorials.  
   _Cons:_ Performance limitations for very complex games.  
   _Best Use Case:_ For browser-based games with rapid prototyping.

6. **Python with Pygame:**  
   _Pros:_ Beginner-friendly, rapid prototyping.  
   _Cons:_ Performance may suffer, requires Python on target machines.  
   _Best Use Case:_ For initial prototypes and indie projects.

---

## DEVELOPMENT NOTES

This is a prototype version of Pepe's Rogue Emote Adventure. The current build includes:

- Basic gameplay mechanics (movement, shooting, dodging)
- Procedural dungeon generation
- Enemy AI and boss battles
- Item and weapon system
- Meme Fusion system
- Basic UI elements

Future development will focus on:
- Additional content (enemies, items, weapons, rooms)
- Enhanced visual effects and animations
- Full controller support
- Sound design and music
- Additional game modes
- Meta-progression system
- Achievements

---

## KNOWN ISSUES

- Some weapon synergies may not function properly
- Occasional glitches in room generation
- Performance may decrease with large numbers of projectiles
- Controller mapping might require adjustment on certain devices

---

## CREDITS

Developed by: WestonGFX

Art assets and sound design: [Placeholder for full release]

Special thanks to the roguelike community for inspiration.

---

## How to Install and Run the Prototype

1. **Requirements**:
   - Unity 2021.3 LTS or newer
   - Basic knowledge of Unity editor

2. **Setting Up the Project**:
   - Create a new 2D project in Unity
   - Create the following folders in your Assets directory:
     - Scripts
     - Prefabs
     - Scenes
     - Sprites
     - Audio
   - Copy all the scripts provided above into the Scripts folder
   - Create a new scene called "Main"

3. **Creating Basic GameObjects**:
   - Create an empty GameObject named "GameInitializer" and attach the GameInitializer script
   - Create an empty GameObject named "GameManager" and attach the GameManager script
   - Create an empty GameObject named "DungeonGenerator" and attach the DungeonGenerator script
   - Create an empty GameObject named "RoomGenerator" and attach the RoomGenerator script
   - Create an empty GameObject named "EmoteFusionSystem" and attach the EmoteFusionSystem script
   - Create an empty GameObject named "WeaponSynergyManager" and attach the WeaponSynergyManager script

4. **Creating Basic Prefabs**:
   - Create a simple player character sprite and attach the PlayerController script
   - Create basic enemy sprites and attach the EnemyController script
   - Create simple weapon sprites and attach the appropriate weapon scripts
   - Create basic item sprites and attach the ItemBase derivatives
   - Create basic tile sprites for floor, walls, and doors

5. **Setting Up References**:
   - In the GameInitializer object, assign the prefab references
   - In the GameManager object, assign UI references and the player prefab
   - In the DungeonGenerator object, assign the RoomGenerator reference
   - In the RoomGenerator object, assign the tile, enemy, boss, and item prefabs

6. **Running the Game**:
   - Save the scene
   - Press Play in the Unity Editor
   - The game should initialize with a main menu
   - Press "Start Game" to begin a new run

This prototype implementation provides the basic framework for Pepe's Rogue Emote Adventure. The core systems are in place, but would need additional content and polish for a full release. This prototype demonstrates the key mechanics described in the game design document:

1. Player movement and combat
2. Procedural dungeon generation
3. Enemy AI with different behaviors
4. Boss battles with phases
5. Item and weapon systems with synergies
6. Meme Fusion system for combining abilities

For a complete game, you would need to expand content in all areas (more enemies, items, rooms, etc.), add visual and audio assets, and refine the gameplay balance.
