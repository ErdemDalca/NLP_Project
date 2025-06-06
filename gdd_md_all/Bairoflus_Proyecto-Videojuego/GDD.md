![][image1]  
**4.2.1 Actividad Diseño de Juego**  
\- \- \-  
Construcción de software y toma de decisiones (Gpo 501\)

**Sergio Jiawei Xuan							A01784695**

**Erick Alonso Morales Diéguez					A01029293**

**Fausto Izquierdo Véjar							A01785221**

Código de clase:

TC2005B.501

**Profesor@:** 

Octavio Navarro Hinojosa

Esteban Castillo Juarez

Gilberto Echeverría Furió

Fecha de entrega:  
22 de marzo de 2025

# **Shattered Timeline**

## ***Game Design Document***

All rights reserved. Developed by the Shattered Timeline team.

## ***Index***

1. Index

2. Game Design

   1. Summary

   2. Gameplay

   3. Mindset

3. Technical

   1. Screens

   2. Controls

   3. Mechanics

4. Level Design

   1. Themes

      1. Ambience

      2. Objects

         1. Ambient

         2. Interactive

      3. Challenges

   2. Game Flow

5. Development

   1. Abstract Classes

   2. Derived Classes

6. Graphics

   1. Style Attributes

   2. Graphics Needed

7. Sounds/Music

   1. Style Attributes

   2. Sounds Needed

   3. Music Needed

8. Schedule

## ***Game Design***

### **Summary**

*Shattered Timeline* is an action-adventure roguelite where you travel through a broken timeline, from a primitive world to an industrial dystopia and finally to a futuristic realm. Fight through waves of enemies and bosses across three dynamic floors while restoring balance to your universe.

### **Gameplay**

Players navigate through randomly selected rooms filled with enemies, using a variety of weapons, items, and food to survive. Tactical decisions are crucial: manage your stamina and food levels, craft and upgrade gear in the base, and defeat bosses to progress to the next era.

### **Mindset**

The game encourages a sense of progression and triumph throughout the different floors. Players will feel tension during enemy encounters and relief upon returning to the base to upgrade. We aim to evoke feelings of determination, strategy, and reward.

## ***Technical***

### **Screens**

1. Title Screen

   * Start

   * Options

   * Credits

   * Exit

2. Save Slot Selection

   * New Game

   * Continue Game

3. Game

   * Inventory

   * HUD (Health, Map, Weapons, Gold, Items, Stamina, Food, Mana)

   * Evaluation / Next Level

4. End Credits

### **Controls**

* Diagonal movement enabled using vector input

* Dash / Roll to dodge

* Action buttons to interact with objects and use abilities

* Possible remapping in Options

### **Mechanics**

* Food impacts stamina regeneration rate

* Stamina governs attacks and dodging

* Rooms are randomly selected from a designed pool

* Weapon upgrades, gear crafting, and cooking in base

* Enemy difficulty increases per floor

## ***Level Design***

### **Themes**

1. Swamp / Forest / Caves (Floor 1\)

   * Mood: Mysterious, primal, moody

   * Ambient: Mist, glowing plants, ruins

   * Interactive: Basic goblins, wolves, …

2. Destroyed City / Factory / School (Floor 2\)

   * Mood: Chaotic, broken, abandoned

   * Ambient: Cracked roads, rubble, flickering lights

   * Interactive: Trolls, ogres, …

3. Spaceship / Futuristic Zones (Floor 3\)

   * Mood: High-tech, futuristic, dangerous

   * Ambient: Electric panels, robotic parts, neon lighting

   * Interactive: Golems, laser barriers, …

### **Challenges**

* Wave-based battles per room

* Bosses with unique patterns and phases

### 

### **Game Flow**

1. Start at the base

2. Enter portal to Floor 1

3. Clear 5 rooms, face boss

4. Portal to Floor 2, repeat process

5. Portal to Floor 3, repeat process

6. Return to base between runs for crafting and upgrades

## ***Development***

### **Abstract Classes / Components**

1. BaseEntity

2. BasePlayer

3. BaseEnemy

4. BaseObject

5. BaseWeapon

6. BaseItem

### **Derived Classes / Component Compositions**

* Enemies:

  * Goblin (Bow, wizard, sword), Wolves

  * Dark Elves, Trolls, Ogres

  * Cyclops, Bears, Golems

* Objects:

  * Armor, Boots, Potions, Scrolls

* Weapons:

  * Katana, Bow, Shield, …

  * Pistol, Assault Rifle, Lightsaber, …

## ***Graphics***

### **Style Attributes**

* Pixel-art with rich dark backgrounds and glowing highlights

* Vibrant effects for hits, dashes, item use

* Strong contrast between enemy/projectile vs background

* Visual feedback for damage, status effects, …

### **Graphics Needed**

1. Characters

   * Player (idle, attack, dash)

   * Enemies by type and difficulty

2. Environment Tiles

   * Forest, city, factory, ship, …

3. Objects

   * portal, cooking station, …

4. UI Elements

   * HUD indicators for each stat and item

## ***Sounds/Music***

### **Style Attributes**

* Futuristic synths mixed with ambient environmental tones

* Battle music with heavy drums and rhythm

### **Sounds Needed**

1. Effects:

   * Footsteps (dirt/metal), dash, hits, object usage, chest open

2. Feedback:

   * Hurt, heal...

### **Music Needed**

1. Base theme

2. Floor 1 theme (swamp/forest)

3. Floor 2 theme (ruins/factory)

4. Floor 3 theme (spaceship)

5. Boss theme

6. Ending theme

## ***Schedule***

[image1]: <data:image/png;base64,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>