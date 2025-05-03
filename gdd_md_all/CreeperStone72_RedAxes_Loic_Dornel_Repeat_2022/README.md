
# Red Axes REPEAT 2022 - Loïc DORNEL

This project contains my work for the Summer 2022 repeat of PROJI8006. The folders contain the following :

* _resources : Non-code files
  * Portfolio : Images, audio files and videos used in the portfolio
  * Voicelines : New voicelines recorded by Erik's voice actor
* LevelGeneration : Technical work on a Procedural Level Generator
  * Assets/Features : Each folder corresponds to an element from the generator
* Norsevar/Project : Original game, and canvas for my Narrative work
  * FMOD/FMOD.fspro : FMOD file associated with the game, all voicelines are held in SFX/REPEAT/Voicelines.
  * NorseVar/Red Axes
    * Common
      * Generated/GeneratedEventEnum.cs : Events were altered, generating a new file
    * Features
      * _REPEAT : New scene, scriptable objects and scripts, all of which I created during this repeat
      * Levels/BeginningBehaviour.cs : Altered the script to feature the new voiceline
    * Releases/Test 1.1/Scenes/Level 1.unity : Altered the scene to feature new bounding areas and rebalanced the first and third fights
    * Resources
      * Data/Events
        * Dialogues : Altered all events to feature the new dialogues and voicelines
        * Generic/Player/TakeEquipmentFirstSay.asset : Altered to feature the new dialogue and voiceline
        * Level/Level1 : Altered all events to feature the new dialogues and voicelines

___

# Norsevar

## What is the game about?

Norsevar is a Norse mythology-themed roguelite dungeon crawler game with a Hack n’ Slash combat system, in which the player plays as a Viking with a one-handed axe, fighting his way through randomly generated rooms filled with enemies. Each room has to be cleared before being able to proceed to the next.  

After clearing a room, the player receives a random upgrade, which either increases his character stats (ex.: Attack damage, Health points, Armor, ...) or changes/enhances one of the abilities of the character (ex.: Dashing spawns an axe that spins around on the spot, dealing damage to enemies in its reach.). When the player dies, he respawns in his base, where he can buy permanent upgrades for his character and start the game again. After a set amount of rooms are cleared, a boss appears, which has to be defeated to move to the next layer. The game ends after the boss on the last layer is defeated.

___

## Where can you find more information?

- [Version control information](https://github.com/dmar98/GD4_RedAxes_Collaborative_Project/wiki)
- [Game Design Document](https://docs.google.com/document/d/1cZSOyrd5LRHa5OsAITo3Q8_iuw6jrqSYKlKNHs19Ixg/edit#)
- [Daily Scrum](https://docs.google.com/spreadsheets/d/1wNdlBaOaOkeRh4qAp8Xy7eyniYXfBVPm1PL31J4ReYk/edit?usp=sharing)
