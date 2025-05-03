# Terminal Hacker

## Elevator Pitch

You’re stuck in a dead-end CS job and decide to take on a hacking course. Your goal: find important data hidden in a secure system and escape. But the system’s firewall is chasing you, and you’ll need to leave a fake trail to throw it off while you hack your way to escape.

## Influences (Brief)

- Deadeye Deepfake Simulacrum
  - Medium: Game
  - Explanation: This game features a decently in-depth hacking system that focuses on the aspects of programming we want to focus on: directory traversal on a command line.
- The Matrix
  - Medium: Movie
  - Explanation: Our game is Terminal Hacker, meaning the player is someone who is hacking into a system to escape people and do hacker things. When I first heard the concept of the game, the movie The Matrix came to mind, as it is about a person being transported into a cyber world, where the main character is essentially a hacker of that world.
- Anonymous
  - Medium: Hacker Group 
  - Explanation: Anonymous is known for using hacking to expose corruption and injustice. This inspired Terminal Hacker, where players must outsmart security systems to achieve their goals.

## Core Gameplay Mechanics (Brief)

You write commands to traverse directories, trying to find a specific piece of data. You are being pursued by the firewall, which you have to try and trick to throw them off your trail. Each level gets progressively harder as the player must race against the clock to retrieve the desired data.

-  traversing through directories
-  Chased by the Firewall 
-  Creating fake trails(directories, files) 
-  Rising difficulty


# Learning Aspects

## Learning Domains

Introduction to directory and file traversal and management

## Target Audiences

- Early learners of computer science who have little experience with directory and file traversal and management.

## Target Contexts

- This would be played when you are learning basic directory and file management

## Learning Objectives

*Remember, Learning Objectives are NOT simply topics. They are statements of observable behavior that a learner can do after the learning experience. You cannot observe someone "understanding" or "knowing" something.*

- *Executing Files*: *By the end of the game, players will know how to run files located inside directories.*
- *Creating Files*: *By the end of the game, learners demonstrate the ability to create new files in specified directories.*
- *Traversing Directories*: *By the end of the game, players can navigate through different bash directories.*

## Prerequisite Knowledge

- *Before the game, players need to be able to differentiate between files and directories*
- *Before the game, players need to be able to understand how files and directories work*

## Assessment Measures

*We will assess the learner with a pre/post-test, allowing them to demonstrate their understanding of the learning objectives. We will compare their scores in each test to measure their understanding.*

# What sets this project apart?

- The gameplay of having to “dungeon crawl” through a terminal style world
- the game focuses on teaching player how cmd/terminal works, with a fun gameplay mechanics 
- the game will have a unique enemies preventing player from succeeding
- this game will have fun and unique endings that the players can achieve

# Player Interaction Patterns and Modes

## Player Interaction Pattern

*Terminal Hacker is a single-player game. You traverse through the world using the WASD movement. You interact with objects/prompts with, that will pop up a keyboard allowing you to type in bash commands. You will repeatedly go through harder and harder levels until you reach the end.*

## Player Modes

- *Singleplayer*: *The only mode of the game will be available from the main menu with a simple start option. In this mode, the player will be met with a few difficulty levels where they have to try and traverse the directory and find a specific file.*

# Gameplay Objectives

- *Steal data*:
    - Description: *The player must find and collect secure data hidden throughout the level.*
    - Alignment: *This teaches players how to navigate directories and manage files.*
- *Don’t get caught*:
    - Description: *There will be a firewall (progress bar) that will be hunting you down. You have to write in bash commands to throw them off.*
    - Alignment: *This aligns with teachthe player to create new files/directories*
- *Advance to the next level*:
    - Description: *Once the player reaches the end of the level, you will progress to the next level* 
    - Alignment: *This will help them advance their knowledge of directory traversal and file management*

# Procedures/Actions

*You can traverse the overworld with the WASD keys and interact with terminals by moving to them and pressing E. From there, you will have access to various bash commands, which can be freely typed into the terminal.*

# Rules

- Players move their character with WASD
- LS command will open the map and show you the layout of the dungeon
- LS -a will reveal hidden files within a room, this will have limited uses
- LS -l shows the timestamps of files on the map
- CD can be used in elevators to navigate to different floors (directories)
- RM will allow you to delete files to remove debuffs or to slow down the firewall, this will have limited uses
- VIM? Will allow you to edit files to change the code to either buff/debuff your character
- TOUCH will allow you to create new files and update the timestamp on files to slow down the firewall, this will have limited uses
- MV will allow you to change the position of files in the room (maybe even bring them to another room)
- PWD will show you the current path of the directories you are in
- The goal of the game is to find the file with the secret data to expose the person you are hacking

# Objects/Entities

- There will be a player model that looks like a hacker
- There will be a firewall progress bar (maybe an npc model)
- There will be dungeon-like rooms acting as the directories
- There will be rooms acting as files
- There will be a terminal displayed with a keyboard on screen that you can type into

## Core Gameplay Mechanics (Detailed)

- *Editing Files and Directories*: *The player will be able to perform commands at terminals that allow them to edit and create files, including moving them between directories or eve removing them entirely.*
- *Hazards*: *At the top of the screen, players can monitor the alert meter—once it fills up, it will expose their location to the FIREwall, forcing them to evade detection. On certain floors, players may encounter trap files that weaken their abilities and accelerate the meter’s increase, raising the stakes even further.*
- *Searching for Core Data*: *The player will have to manage their more limited commands to find the core data they are looking for.*

    
## Feedback

- There will be a walking noise for when your character is moving around
- There will be a command line prompt on screen with a keyboard visually, when typing there will be keyboard noises as audio feedback as well as the keyboard typing on screen
- If you input a wrong command it will increase the firewall’s progress bar and give you a visual feedback and audio feedback like a strike/red
- Advancing to a new level will play a noise and visually transition
- When you win there will be a winning audio and a you won screen
- If you get caught by the firewall there will be a game over screen and there will be defeat audio 


# Story and Gameplay

## Presentation of Rules

*The player will learn each of their possible actions at terminals one at a time. The pressure of trap files and firewalls will be added slowly and only ramped up as the player learns better ways to deal with them. We will allow them a few calm levels to figure out the basics before the difficulty increases.*

## Presentation of Content

*The player will learn new commands as they complete levels, learning bit by bit instead of all at once. For instance, they’ll learn how to use ls and cd first, since those are very bare bones ways to get around in directories. Then they will be taught things like mv, rm, or touch as they have to deal with the firewall more. Each command will be taught one at a time, and assigned a mechanical purpose in the context of the game to make memorizing the command and how it works more engaging.*

## Story (Brief)

*You’ve been trapped in the digital realm and have to find the key pieces of data to code a way out of here before the firewall burns you to a crisp!*

## Storyboarding

![image1](https://github.com/user-attachments/assets/d3674fe0-7d8e-4085-8d1e-33acfbc06f06)
![image2](https://github.com/user-attachments/assets/edf6b0d1-e2e0-4270-b997-8690e9040a01)


# Assets Needed

## Aesthetics

*The aesthetics should be sort of electronic or mechanical, with a sort of digital look to everything. This plays into the game's theme of terminal hacking in a sort of computer world and will hopefully immerse the player in the game and make them feel more invested.*

## Graphical

- Characters List
  - Hacker -  This is the player-controlled character. The player will be able to customize their hair
  - Fire Wall  -  Chases the player/hacker, and tries to catch them. A very mad mini computer head that's on fire.

- Textures:
  -  1s and 0s - classic binary matrix rain 

- Environment Art/Textures:
  - Background -  The background will be similar to the insides of the computer(lots of wire, sensors, etc)
  - doors - vault style door, hallway door, and semi-circle elevator 
  - Mini Terminal - next to the vaulted door there will be a “security terminal”(keyboard, and screen), where the player can interact with


## Audio

- Music List (Ambient sound)
  - *Title Screen*: *https://freesound.org/people/RICHERlandTV/sounds/351920/ (OPening the Game/Loading into a Level)*, *https://freesound.org/people/orginaljun/sounds/396960/ (Title Music)*
  - *General Gameplay*: *https://freesound.org/people/Timbre/sounds/406915/ (Background Music)*, *https://freesound.org/people/B_Lamerichs/sounds/262834/ (general)*

- Sound List (SFX)
  - *Opening a terminal*: https://freesound.org/people/Debsound/sounds/256543/ (Opening the terminal),       
    https://freesound.org/people/unfa/sounds/543968/ (Running a Command), https://freesound.org/people/FoolBoyMedia/sounds/352661/ (extra)
  - *Entering a Room*: https://freesound.org/people/tim.kahn/sounds/91926/ (Elevator),   
    https://freesound.org/people/Pixeliota/sounds/678254/ (File Door Opening/Enterning)
  - *Death*: https://freesound.org/people/AceOfSpadesProduc100/sounds/360871/


# Metadata

* Template created by Austin Cory Bart <acbart@udel.edu>, Mark Sheriff, Alec Markarian, and Benjamin Stanley.
* Version 0.0.3


