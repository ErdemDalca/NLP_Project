---
layout: articlealt
title: "Revised Game Design Document"
date: 2024-11-21
tags: [videogame]
pdf:
---

# CERNUS Game Design Document

---

## 1. Game Overview

- **Game Title**: 
  - *CERNUS*
- **Genre**: 
  - Sci-Fi Movement based First-Person Shooter
- **Platform(s)**: 
  - Primary: PC  
- **Target Audience**: 
  - CERNUS is designed for players who enjoy strategic shooters with slower time-to-kill mechanics, such as fans of Halo's deliberate pacing, Valorant's tactical depth, or Apex Legends' movement-based gameplay. It also appeals to sci-fi enthusiasts who enjoy exploring rich, narrative-driven universes like Mass Effect or Destiny.

### Game Summary

*CERNUS is a movement-focused first-person shooter that emphasizes strategic play over raw mechanical skill. Players will balance movement, aim, and ability use, leveraging their chosen faction's unique strengths. The game also immerses players in a richly detailed universe, uncovering the history of the WPC and the CERNUS Initiative through in-game exploration, hidden messages, and collectible logs. Whether you're a tactical shooter, an explorer of alien worlds, or a seeker of deep lore, CERNUS offers an experience for everyone.*

---

## 2. Core Gameplay Mechanics

### Combat
- **Key Combat Features**:  
- Each distinct faction in CERNUS has different abilities and weapons, which drive how the game is played. 
- Player health is separated into two segments, a Casing and a Core. Casings are regeneratable health that protect the player core, with the player core being an incredibly vulnerable spot that when destroyed kills the player. 
- Player Cores act as central processing for player characters, controlling energy usage, regeneration, and other factors that effect gameplay.
- All modifications, abilities, and weapons players can choose from change core and casing health in some way, with players who want more abilities having to sacrifice maximum health, regeneration, or other stats.
- Time to kill in CERNUS is much longer than usual, with players needing focus and control rather than speed and reaction time.
- All factions will have Movement, Combat, and Defense based abilities along with miscellaneous faction specialty abilities that can range from information to support.
- Factions will all share a "united pool" with abilities that players of all factions can choose from, but are the less powerful and specialized versions of abilities and weapons.
### Faction-Based Gameplay
- **Faction System**:  
  - Factions are a core aspect of CERNUS that make in unique from other games
  - Factions have different main focuses, with each faction having a unique playstyle that has strengths and weaknesses
  - Factions have unique coloring and iconography, making players easily identifiable to each other, allowing for strategic counterplay and changing strategies as games progress
  - Players are incentivized to bring teams composed of multiple different factions to maximize team adaptability and diversify skillsets
  - **Faction Summaries**:  
    - **Kronenbuerger Division**: Industrial heavy machinery faction, focused on survivability and damage over time  
    - **Galiedon**:  Growth and Terraforming faction, focused on regeneration and support
    - **Applied and Relative Sciences Agency (ARSA)**:  Science and Technology faction, focused on focused and instantaneous damage and movement
    - **Forefront**:  Peace and Unity faction, all rounded and a good starting point for players. Minor focus on defense and damage

### Customization and Upgrades
- **Customization Options**:  
  - Players can choose from different combat, defense, and movement upgrades as well as faction specific upgrades.
  - Cosmetics that give players the ability to express themselves and show identity will be available, with players being able to find or collect cosmetics through challenges.
  - **Examples**: 
	  - Dash ability
	  - Ground pound
	  - Blink(teleport forwards)
	  - Deployable shield wall
	  - Healing bubble
- **Upgrade System**:  
  - CERNUS' upgrade system is fully unlocked at the start of the game
  - Players have the option of choosing from branching paths at the start of abilities, such as being able to choose between a shield with higher health or one which you can shoot through
  - Players can earn badges that show their skill with a certain ability, such as badges for getting 50 kills after dashing, or blocking a certain amount of damage with the shield wall.

---

## 3. Narrative and Worldbuilding

### Backstory
- **Setting**:  
  - In the mid-21st century, World War III ravaged the Earth, depleting its resources and rendering parts of Australia and South Asia uninhabitable. The accidental discovery of the Trifolium particle, a result of a failed weapon, led to the creation of the World Peace Commission (WPC) and the reorganization of the UN Peacemaking Force. The WPC established the CERNUS initiative to "save the goddamn world" and expedited scientific and technological development through General Intelligences (GIs).
  - By 2060, humanity had developed the first CERNUS fleet, and in 2061, CEF-1 departed for Alpha Centauri. The fleet's 2064 discovery of alien life set the stage for humanity's interstellar future. By 2080, Earth had stabilized under WPC governance, achieving Type 1 Civilization status and entering the CERNUS era.

### Lore and Worldbuilding Details
- **Core Themes**:  
  - What moral or philosophical questions does the game explore?  
  - How do the factions reflect these themes?  
  - There are no good guys
	  - Everyone just wants something, and their is no definitive right or wrong
  - Factional philosophies
	  - Each faction embodies contrasting philosophies about survival and progress. Kronenbuerger sees suffering as the cost of achievement. Galiedon champions structure and order to create growth. ARSA embraces the pursuit of unyielding technological advancement. Forefront seeks unity, believing in the potential of cooperation over division. These perspectives reflect humanity's fractured but relentless pursuit of survival.
  - Humanities will to go on
	  - Despite the countless setbacks, atrocities, and tragedies we have faced, humanity will continue to soldier on. The Exploritors in CERNUS have human emotions and reactions, and despite that do everything for the mutual benefit of humanity
- **Unique spaces**:  
  - Describe the variety of alien ecosystems.  
  - What unique opportunities and threats do these environments provide?  
  - CERNUS will give players the ability to explore many diverse environments, and game spaces, each with unique gameplay implications.
  - **Examples**:
	  - Kronenbuerger space station
		  - Areas of different gravity
		  - Industrial machinery
		  - Deep space backdrop
	  - Alien jungle world
		  - Dense cover and vision obstruction
		  - Mud and other obstructions that limit speed
		  - Dangerous flora and fauna
	  - Alien ruins world
		  - Destroyed ruins
		  - Alien lore
		  - Mission content or special event(later in development cycle)

---

## 4. Technical and Art Direction

### Visual Style
- **Artistic Goals**:  
  - Weathered but bright, contrasting colors.
  - Sleek sci-fi with inspirations from several different sources, such as star wars, mass effect, and Warhammer(Mainly the tau).
  - Sense of wonder that is associated with space and the unknown.
  - Optimism despite the indifference of the universe.
  - Contrast human technology vs. alien environments.

### UI Design
- **Core Features**:  
  - Casing health
  - Core status
	  - Damaged, Regeneration compromised, tracked by enemies
  - Velocity
  - Mini map
  - Weapon charge/ammo
  - Color/marker or UI color scheme change for each faction
  - **Faction Specific**:
	  - Ability health 
	  - Ability Recharge time
	  - Faction specific resource (if applicable)
  - Will create UI mockup(WIP)

### Audio
- **Soundtrack and Ambiance**:  
  - upbeat, high tempo music and slow, orchestic music to contrast from each other
  - Sci-fi sound effects that inform players of environment and character changes, such as low health or approaching danger

---

## 5. Prototype Goals

### What to Focus On:
- **Exploration Mechanics**:  
  - Playable game space with cover
  - Space station to avoid complicated textures
- **Faction Gameplay**:  
  - All four main factions, but limited to one or two abilities at first
- **Basic Combat Mechanics**:  
  - Casing and Core health
  - Two to Three different guns

---

## 6. Long-Term Features

### Expansions and New Features
- **Multiple Planets and Levels**:  
  - What new challenges will different maps bring?  
- **Additional Gameplay Modes**:  
  - 5v5 PVP game mode
  - FFA game mode
  - PVE objective game mode
  - Parallel but asymmetric game mode
	  - Player goals are not necessarily against each other, but mutual success is not an option
	  - Players can sabotage enemy goals, but that takes players away from their main goal
	  - Whoever has the higher score wins at the end
  - event/story game mode
- **Post-Launch Content**:  
  - Other factions
	  - Other factions may explore stealth, espionage, and other cultures and themes
  - Expanded lore
  - New maps
  - Balancing
  - Animations and stories

---

## 7. Iceboxed Features

*(Features that are not critical for launch but could add depth or variety later.)*  

- **Resource Management**:  
  - Players would be able to collect resources from planets to customize and build up their own base
  - Resources could be used for crafting cosmetics
- **Decision-Making Mechanics**:  
  - Players will be able to formally join certain factions, and fight against other factions 
  - Diplomacy with other species
- **Advanced Exploration Tools**:  
  - In game vehicles and space ships
  - exploration entire star systems, piloting ships to discover alien worlds, hidden dangers, and new opportunities.
- **Damage Types**:
  - Different Damage types that effect players differently
  - Weapons that deal different types of damage
  - Environments having different damage types

---

## Final Thoughts and Next Steps

*Making a videogame has been a childhood dream of mine. CERNUS is an unexpected way that I have started achieving the dream. The majority of the work I have done on CERNUS has been design and worldbuilding, but now that I have a revised game design document I will start focusing on a prototype, as well as finishing up each faction page for you to see. I hope you are as excited as me about the launch of CERNUS, and I hope you'll stick around for the ride.*  
