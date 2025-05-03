# Game Design Document

This document was created at the beginning of the project to outline the game concept, design, and development plan. It
served as an early reference board and idea collection for the project. This entails that there might be inaccuracies in
the document, as the project progressed and the game design evolved.

## Concept

### Working title

Cold Case

### Concept Statement

A 2.5D adventure game in which two players have to solve a mystery together by solving various puzzles. An investigator
and a ghost cooperate with their different abilities across their different worlds.

### Genre

puzzle, isometric 2D, Adventure
→ Adventure Coop Puzzle Game

## Product Design

### Player Experience and Game POV

<!-- Who is the player? What is the setting? What is the fantasy the game grants the player? What emotions do
you want the player to feel? What keeps the player engaged for the duration of their play? -->

- 2 Players: 1 “living”, and 1 “ghost”
- end of 20th century detective in an overgrown ruin / ghost world mirroring the real word to an extent
- mystery solving
- engagement through curiosity and social interaction

### Visual and Audio Style

<!-- What is the “look and feel” of the game? How does this support the desired player’s experience? What
concept art or reference art can you show to give the feel of the game? -->

- 3D block Visuals:

| ![first visual design showcase](showcase.png) |
 |:---------------------------------------------:|
|             first design proposal             |

- old ruins/overgrown ruins and ghost realm
- calming music

#### Inspiration

- visual: [monogon-isometricdungeon asset pack](https://maxparata.itch.io/monogon-isometricdungeon)
- Gameplay:
    - [Keep talking and nobody explodes](https://keeptalkinggame.com/)
    - [We were here](https://store.steampowered.com/app/582500/We_Were_Here/) and following titles of the same series
    - [BOKURA](https://store.steampowered.com/app/1801110/BOKURA/)

### Game World Fiction

<!-- Briefly describe the game world and any narrative in player-relevant terms (as presented to the player). -->

- Detective solving Puzzles together with a/his ghost in a different realm
- the Detective (living) Player wants to solve a Murder Mystery by exploring the ruin in which the murder happened
- in the end it is revealed that the ghost is the dead detective, who dies in the end and travels back in time to help
  his living self out -> both players can switch places and replay

### Platform(s), Technologie, and Scope

<!-- PC or mobile? Table or phone? 2D or 3D? Unity or Javascript? How long to make, and how big a team?
How long to first-playable? How long to complete the game? Major risks? -->

- libGdx
- Deno
- 2D isometric gameworld
- Multiplayer over a gameserver (WebSockets for Communication)
- MVP in 1 Months
- Release in Jan.2025

#### Major Risk

- achieving a multiplayer connection through a server
- Interactions in the game world without a overarching game engine like Unity

## Game System Design

### Core Loops

<!-- How do game objects and the player’s actions form loops? Why is this engaging? How does this support
player goals? What emergent results do you expect/hope to see? If F2P, where are the monetization points? -->

→ Players solve puzzles in their own world, but also ones spanning between both game worlds, requiring teamwork and
tight communication between both players

Each level is split into two worlds, one for both players. In itself each player can individually solve parts of the
puzzle in his world, but to reach the goal there has to be a need for communication and correct interaction with parts
of the game world concerning both players. This in turn means, that both players need to have meaningful interactions
and communication to be able to reach their individual goal.

If both player reach their goals the next level starts.

### Objectives and Progression

<!-- How does the player move through the game, literally and figuratively, from tutorial to end? What are their
short-term and long-term goals (explicit or implicit)? How do these support the game concept, style, and
player-fantasy? -->

- each game level consists of a starting location, a puzzle and an end/finish location
- the puzzle hinders the player/s to get to the end
- both players have to get to the end of the level to progress to the next

#### Short-Term

- manage to get to the next room

#### Long-Term

- get to the last room completing the game and having the chance to replay as the other role (living/ghost)

### Game Systems

<!-- What systems are needed to make this game? Which ones are internal (simulation, etc.) and which does the
player interact with? -->

#### Core

- Solid Player Movement based on an isometric Grid System
- Player Inventory
- Portals to transfer Items between the gameworlds of both players
- 2 States an Object can have:
    - normal - the object is only in the world it appears in
    - transcended - the object exsits and acts in both worlds the same
- Asynchronous (Multiplayer) Gameplay

#### Level Specific

(living/ghostly)

##### mvp:

- gloves to push blocks and to toggle levers
- spikes that block the path of the player and get toggled by a lever

##### later:

- miasma/fog unpassable for the player + torch to detect or remove miasma/fog

## Interactivity

<!-- How are different kinds of interactivity used? (Action/Feedback, ST Cog, LT Cog, Emotional, Social, Cultural)
What is the player doing moment-by-moment? How does the player move through the world? How does
physics/combat/etc. work? A clear, professional-looking sketch of the primary game UX is helpful. -->

- wasd grid based movement
- e to interact/pickup/drop items
