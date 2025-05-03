# 3D Pacman Game Design Document

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)

# Introduction
The project aims to create a new version of the classical - retro videogame Pacman, in a 3d world. This is part of the final exam of the Computer Graphics course held at Politecnico of Milan by professor Gribaudo Marco;

Overview: as said before the idea is to reimagine Pacman in a 3d environment. This is done using cpp as main language, taking advantage of the Vulkan APIs for the graphics implementation;

This document will be used as Game Design Document in order to annotate what has been done in the project, what must be done now and what could be future ideas to implement;

## Concept
In our 3d adaptation, we'll try to preserve the original feeling of playing Pacman, the gameplay will be both old and new, taking the classical experience of playing the original game while however be as if inside it ourselves. Some details:

- 3D Environment: the game features the classical maze shape we all know, but there will be the possibility of generating new mazes each time we play a new game;

- Player Perspective: the idea is to have the player feel like he/she is Pacman itself, so the game will have a first-person view of the world. The walls of the maze will be higher of the player view, so that he doesn't know where he is or where the ghosts are. This, however, could reveal to be very hard for the player to complete the game, so in the future a map of the maze will be put as interface for the player to always have under control (maybe without the ghosts to preserve a little of the challenge the 3D world contains);

- Ghosts AI: classiical enemies where 4 little ghosts, each with different behaviours. This will be ported to our game in the most similar way possible, in order to have the same feeling as playing the real Pacman;

- Power Ups: in the game there will be only one "power up" that is the one that lets Pacman eats the ghosts upon contact with them. This will also be imported in our game as unchanged as possible. Ghosts eaten will return for a brief time in their lobby and then will be released again;

- Interface: as said there will be an interface for the player to read informations from, things like the lives, the points the player gets throughout the round, maybe tha map, and so on;

- Goal: the game goal will be to gather all the coins there are in the maze, without being hit by any of the ghosts. The player will also have a fixed number of lives that he will lose if it hits ghosts. The game ends if there are no more lives and a ghosts hits again the player. If possible (not because it is hartd to do, but just because is something more than needed and so wil have last priority), a second level, and then maybe more, will be added for the players which manage to complete the first one. The rules will be the same but the maze will change to increase the difficulty;

## Gameplay Overview
Provide a detailed overview of how the game is played, including objectives and challenges.

## Technical Overview
Explain the technology stack, including graphics engine, libraries, and programming languages.

## Art Style
Describe the visual style, including art direction, character design, and environment aesthetics.

## Sound Design
Discuss the audio elements of the game, including music, sound effects, and voice acting.

## Controls
List and explain the controls for playing the game.

## Levels
Detail the different levels, including maze layouts, obstacles, and enemy placements.

## Characters
Introduce the main characters, their roles, and behaviors.

## Power-Ups
Describe the power-ups available in the game and their effects.

## Scoring
Explain how scoring works and the factors that contribute to it.

## User Interface
Describe the UI elements, menus, and HUD components.

## Platforms
List the platforms the game will be available on, including PC, consoles, and mobile devices.


___

# Project Structure

The project main structure is this one:

![Project Structure](Images/ProjectStructure.png)

Many folders got taken as they are from the Assignments given to us by the prof throughout the course. Other folders are:

- Documentation: contains this document, the relative images and everything that is considered documents that explain the project;

- Core: contains all files created as new to handle the project functionalities, like the ControlHandler.hpp or the GhostsBehaviour.hpp;