---
id: godotsharp-dungeon-doom-souls-gdd
aliases:
  - godotsharp-dungeon-doom-souls-game-design-document
  - GodotSharp Dungeon Doom Souls Game Design Document
tags: []
---

# GodotSharp Dungeon Doom Souls Game Design Document
Game Title: GodotSharp Dungeon Doom Souls
Version: 0.0.1
Date: 2024-08-14 - 2024-??-??

Logo:

This could eventually be published as a website

Maybe incorporate chatgpt intergration to help with creating custom terrain generation and different bigginer loot depending on the player's custom story. Could be done by modyging different weights related to frost, lava, water, dungeons, etc... and by simply increases some a lot, some a little, and some not we could get kinda custom terrain generation maybe a lore accurate item???

I want to incorporate general attack1, attack2, dodge, etc... in code but with potentially completely different effect and animations depending on the weapon and armor the player is wearing. This will allow for a lot of customization and replayability. for example one players dodge may be a dark souls type dodge while for another it might be a full on dash or even tracer style tp-dash.

https://www.youtube.com/watch?v=drCnFueS4og&pp=ygUNcHJpbWFnZW4gZ2FtZQ%3D%3D

## Introduction
### Game Summary Pitch
### Inspiration
### Player Experience
*How will the player feel when playing the game?*
This will depend completely on the role you want to play, Currently there are 4 main roles but you can completely redefine your initial role depending on the weapons/armor/skills you find and the way you spend you level up points. For example you may play as a Swordsman and you may spec into having a big ass sword or you can spec into parrying with daggers. You may even level in arcane as a swordsman and be able to use mage spells (for example basic fire and healing spells).
You're initial class does however play a major role in shaping your build, especially early game.
- Shooter
- Swordsman
- Mage
- Tank
### Platform
### Development Software
### Genre
### Target Audience
- People who are into fps shooter games, people who like dungeon crawlers, and DS/Elden Ring player (include steam analytics for pc numbers)

## Table of Contents
- [Concept](dds-concept.md)
  - [Gameplay Overview](dds-concept-gameplay-overview.md)
  - [Theme Interpretation](dds-concept-theme-interpretation.md)
  - [Techincal Overview](dds-concept-technical-overview.md)
  - [Primary Mechanics](dds-concept-primary-mechanics.md)
  - [Secondary Mechanics](dds-concept-secondary-mechanics.md)
- [Gameplay](dds-gameplay.md) // Note: For this game, we will have a similar approach to dark souls were we will have a vague story
  - [Combat](dds-combat.md)
  - [Movement](dds-movement.md)
  - [World](dds-world.md)
    - [Exploration](dds-exploration.md) // How it should feel to explore the world and what the player would typically see depending on the scene - When you're not in a puzzle room or boss fight what are you seeing?
      - [Dungeons](dds-dungeons.md)
        - [Atmosphere](dds-atmosphere.md) - What the player should feel when they're in a dungeon and less what it will look like - refer to art section for that
        - [Layout](dds-layout.md)
        - [Traps](dds-traps.md)
        - [Enemies](dds-enemies.md)
      - [Lava Areas](dds-lava-areas.md)
      - [Ice Areas](dds-ice-areas.md)
      - [Cave Areas](dds-cave-areas.md)
      - [Forest Areas](dds-forest-areas.md)
      - [Castle Areas](dds-castle-areas.md)
      - [Desert Areas](dds-desert-areas.md)
      - [Interdimensional Areas](dds-interdimensional-areas.md)
        - [Time Travel](dds-time-travel.md)
        - [Interdimensional Doors](dds-interdimensional-doors.md) // A form of interdimensional travel
          - Grace room: https://www.youtube.com/watch?v=F02iMCEEQWs
    - [Puzzles](dds-puzzles.md)
    - [Boss Fights](dds-boss-fights.md)
    - [NPCs](dds-npcs.md)
    - [Loot](dds-loot.md)
      - [Weapons](dds-weapons.md)
      - [Armor](dds-armor.md)
      - [Consumables](dds-consumables.md)
  - [Character Progression](dds-character-progression.md)
  - [Multiplayer/Co-op](dds-multiplayer.md) // Note: This will be a stretch goal - This covers the gameplay aspect of multiplayer not the technical details; please refer to the tech. details section
- [Story](dds-story.md) // Maybe be unnecessary for this game as I can attach ##Story or ##Lore to individual items/bosses/locations
  - [Lore](dds-lore.md)
  - [Characters](dds-characters.md)
  - [World](dds-world.md)
- [Art](dds-art.md)
  - [Art Style](dds-art-style.md)
  - [Effects](dds-effects.md)
    - Have a Post Processing section with specific effects I want and link to them in the Graphics section for a more technical view on what they're actually doing and how they're doing it
  - [Character Design](dds-character-design.md)
  - [Environment Design](dds-environment-design.md)
  - [UI Design](dds-ui-design.md)
- [Audio](dds-audio.md)
  - [Music](dds-music.md)
  - [Sound Effects](dds-sound-effects.md)
- [Game Experience](dds-game-experience.md)
  - [Ui/UX](dds-ui-ux.md)
    - [Accessibility](dds-ui-ux-accessibility.md)
      - [Colorblind Mode](dds-colorblind-mode.md)
      - [Subtitles](dds-subtitles.md)
      - [Language Support](dds-language-support.md) // Localization
  - [Controls](dds-controls.md)
  - [Game Flow](dds-game-flow.md)
  - [Game Progression](dds-game-progression.md)
- [Technical](dds-technical.md) // Include global variables sush as gravity, or time_scale
  - Programming Style
    - Will use "TODO:", "FIXME:", "NOTE:", "HACK:", "BUG:"
      - NOTE: for important or useful information about the code, function, or system that should be known especially if you're working on it (That may not initially be obvious, such as weird quirks or things that are done in a certain way for a specific reason)
      - TODO: for things that need/should be done but aren't critical (at least not yet...)
      - FIXME: for things that are broken and need to be urgently fixed asap
      - BUG: for things that are broken but not urgent to fix (yet...)
      - HACK: for things that are done in a way that is not optimal or ideal but works (at least for now)
  - [Tools](dds-tools.md)
    - [Game Engine](dds-game-engine.md) // Godot
    - Programming Language: C#
    - Version Control: Git & GitHub
    - Development Environment: NeoVim
    - Modeling: Blender, Blockbench (NOTE: Blockbench has a Gif recording functionality under View > Record Gif and they have on option to use a pixilate shader which i should copy for my game, maybe look for an acerola video?)
    - Texturing: Photopea
    - Audio: Audacity
    - Music: Ableton Live
    - Video Editing (Dev Logs and Trailers): Shotcut
  - [Mobs](dds-mobs.md)
    - [Damage System](dds-damage-system.md)
      - There is a Damage struct that contains a dictionary of damage types and their corresponding damage values (e.g. Physical : 10, Fire : 5, etc...) called a DamageTable and a damage type. The weapon passes a copy of that damage object to the owner mob's Attack() in which any effects the owner mob has active such as temporarily doubling physical attack damage for example with be applied on the Damages.m_DamageTable and whatever else needs to be applied, then the Damage object with the potentially modified values is passed to the targetMobs TakeDamage() by reference in order to save memory and finally, any of the mob's effects are applied and the damage is finnally taken.
    - [Physics](dds-physics.md)
    - [Attribute_System](dds-attribute-system.md)
    - [Stats_System](dds-stats-system.md)
    - [Player](dds-player.md)
      - [State Machine](dds-state-machine.md)
        - [Player States](dds-player-states.md)
      - [Leveling System](dds-leveling-system.md)
    - [NPC](dds-npc.md)  // Npc and enemy might be able to be combined into one section - with the only difference being that NPC default to friendly and have text dialogue or different special events such as trading, talking, buying, selling, etc...
      - [State Machine](dds-state-machine.md)
        - [NPC States](dds-npc-states.md)
      - [AI](dds-npc-ai.md)
        - [Pathfinding](dds-pathfinding.md)
        - [Behavior Trees](dds-behavior-trees.md)
        - [Decision Trees](dds-decision-trees.md)
    - [Enemy](dds-enemy.md)
      - [State Machine](dds-state-machine.md)
        - [Enemy States](dds-enemy-states.md)
      - [AI](dds-enemy-ai.md)
        - [Pathfinding](dds-pathfinding.md)
        - [Behavior Trees](dds-behavior-trees.md)
        - [Decision Trees](dds-decision-trees.md)
    - [Boss](dds-boss.md)
      - [State Machine](dds-state-machine.md)
        - [Boss States](dds-boss-states.md)
      - [AI](dds-boss-ai.md)
        - [Pathfinding](dds-pathfinding.md)
        - [Behavior Trees](dds-behavior-trees.md)
        - [Decision Trees](dds-decision-trees.md)
  - [Items](dds-items.md)
    - [Weapons](dds-weapons.md)
    - [Armor](dds-armor.md)
    - [Consumables](dds-consumables.md)
  - [Input System](dds-input-system.md)
  - [Game Engine](dds-game-engine.md)
  - [Programming Language](dds-programming-language.md)
  - [Multiplayer Networking](dds-multiplayer-networking.md)
  - [Graphics](dds-art-style-graphics.md)
    - [Post Processing](dds-art-style-post-processing.md)
      - [Dithering]() // TODO: add as a link to ##Dithering in post-processing.md (lookup Acerola YT video)
  - [Random Generation](dds-random-generation.md)
  - [Performance](dds-performance.md)
  - [Optimization](dds-optimization.md)
  - [Testing](dds-testing.md)
  - [Save System](dds-save-system.md)
  - [Loading System](dds-loading-system.md)
  - [Version Control](dds-version-control.md)
- [Development Timeline](dds-dev-timeline.md)
- [Marketing](dds-marketing.md)
  - [Social Media](dds-social-media.md)
    - [YouTube](dds-youtube.md)
      - [Dev Logs](dds-dev-logs.md)
  - [Community Engagement](dds-community-engagement.md)
  - [Press Kit](dds-press-kit.md)
  - [Game Trailer](dds-game-trailer.md)
    - Have cinematic and bombastic exciting gameplay in the first trailer
    - Have a seperate Mechanics overview trailer we we show off movement, combat, the world, and the different areas, etc... in a longer slower paced video.
  - [Game Demo](dds-game-demo.md) // First demo will have no multiplayer prob
  - [Monetization](dds-monetization.md)
