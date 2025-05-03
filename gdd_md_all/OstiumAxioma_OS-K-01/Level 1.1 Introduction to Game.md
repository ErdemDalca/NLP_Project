---
date: 2024-05-06
tags:
  - 游戏开发
  - 游戏开发/引擎
toolSet:
  - "[[现代C++基础]]"
knowledgeLink: 
status: true
---
# Foundations of Game Development
## Plan Ahead
### High Concept Document

To flush out your vision for the game

Define the scope of the game and basic game logic

Intentionally brief

### Game Design Document

To flesh out your game with all the details

e.g. world, story, characters, core mechanics etc.

Intentionally detailed

## Game Development Life Cycle

![[02-Game_Developing/CS5540_GameProgramming/CS5540_System.excalidraw.md#^area=UahuL5Gdrbic-sTtXLSPP|GameProductionFlow|center|800]]

### Development Stages

**<font color="#ffc000">Game Concept</font>**: Ideation and brainstorming

**<font color="#ffff00">Game Design Documentation</font>**: The core plan for features and game scope

**<font color="#92d050">Prototyping</font>**: Initial implementations such as sketches, grayboxing, etc.

**<font color="#00b050">Initial Production</font>**: Main cycle of development and Content creation + Implementation of core game play features

<font color="#548dd4"><font color="#57a6ff">Production Stages</font></font>: 
	1. Alpha Release: Core gameplay features are implemented
	2. Beta Release: Complete version of the game with fully functioning core game play features
	3. Gold Release: Quality check and ready to be launched for the public release

### Iteration Process

![[02-Game_Developing/CS5540_GameProgramming/CS5540_System.excalidraw.md#^area=4XTcU5Oi9lotspppoXH92|IterationProcess|center|500]]
# Introduction to Unity
## Basic Environment: Scene

> [!tip]
> Scene is the basic environment structure  of Unity.  

- Scene contains the environments and menus of the game. 
- A scene is essentially a level of your game. 
- A project can contain multiple scenes.

> [!important]
> It is encouraged to store scene inside a parent folder through out the project

## Basic Unit: GameObject

Every object in a unity game is a GameObject. Players, collectibles, cameras, lights, and so on.

> [!tip]
> GameObjects are more like containers or placeholders. They can't do anything on their own. 

<mark class="hltr-green">Components</mark> are properties of the GameObject. 

## Basic Rendering: Material

Material defines how a surface should be rendered. 

> [!tip]
> The **Albedo** parameter controls the base color of the surface

