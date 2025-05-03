# Game Design Document (GDD)

This is based on the **One-page Design Document**.  
This file will continue to evolve during the development process.

## Title and People

- Title: Game Design Document for Iskrambol Game by Nittee
- Author(s): jiroblea, servin
- Team:
- Reviewer(s):
- Created on: 2024 July 8
- Last Updated: 2024 July 23
- GitHub Issue: #5

## Table of Contents

- [Game Design Document (GDD)](#game-design-document-gdd)
  - [Title and People](#title-and-people)
  - [Table of Contents](#table-of-contents)
  - [Game Identity / Mantra](#game-identity--mantra)
  - [Design Pillars](#design-pillars)
  - [Mechanics](#mechanics)
  - [Features](#features)
  - [Interface](#interface)
  - [Art Style](#art-style)
  - [Music / Sound](#music--sound)
  - [Target Platform and Audience](#target-platform-and-audience)
  - [Development Roadmap](#development-roadmap)
  - [References](#references)

## Game Identity / Mantra

*A single sentence description of the game that you will use to guide design decisions.*

A wireless local PvP multiplayer word game designed to gauge the players' vocabulary knowledge while racing against other players or against time (single-player mode).

## Design Pillars

*Three words or phrases that convey the feeling or emotion you want the players to experience.*

Confusion (?). AHA-moment.
[suggestions] Fast-paced. Brain-racking. Stimulating.

## Mechanics

*List what the game is from a gameplay perspective.*

- The host can input a parent word with at least 6 letters or choose at random.
    - [suggestion] parent word can be generated randomly
- Under a specified time limit, the players will jumble the letters of the parent word to distinguish an existing word from the dictionary (English or Tagalog).
    - [suggestion] time limit may be specified by player or automatically computed based on number of letters of parent word and number of players
- will consists of the following game modes:
  - campaign (single-player, point-based)
  - multiplayer (wireless, local PvP, point-based)
  - daily puzzle (single-player, random word, time-strict)
  - challenge (a player can post a word that other players can reshuffle to obtain new words)
- Points will be given based on the complexity of the word distinguished.
    - complexity may be equal to: number of letters, rarity of the word, scrabble score, combination of some of the previos ones

## Features

*List the cool features or unique elements that you want to include in your game.*

- wireless local PvP
- multiplayer (or single-player)
- with built-in dictionary (?)

## Interface

*List the player input method, the controls, and how the player interacts with your game.*

- touch-based
- letters are clicked ("scooped") as if in keyboard, building the word to be included
    - enter and delete letter buttons included
- options are given

## Art Style

*Include references to lots of images and games that have a similar aesthetic to what you're trying to achive.*

- iskrambol themed: inspired b Filipino street dessert ice scramble
- [unsure] "cutesy" themed with pink-based color scheme (pink being the most common ice scramble color)
    - this may imply that the target audience is primarily Filipino children
    - the color may be light purple instead. It's prettier anyway lol, but it's less common and therefore less appropriate
- [suggestions] artstyle themes (ranked from most favorite to least)
    - lofi aesthetic (pastel colors, simple artstyles, cozy atmosphere); the studying aspect can be highlighted; this also means that the music will be lofi too; cats, don't forget the cats, and much better if they're puspin lol
    - 8 bit theme (pixel art, simple colors, "Press Start 2P" font); artstyle and music inspirations from games like Mario or Undertale
    - chalk on blackboard
    - roblox inspired

## Music / Sound

*Include links to music and sound design similar to what you're tring to achieve. You can also list the emotional responses that the sound should invoke in the players.*

- calming
- Chopin's Nocturnes, Op. 9 No. 2 in E-Flat Major Andante
- [suggestions] see [Art Style](##Art-Style)

## Target Platform and Audience

*Describes who the game is for. Bullets can often be clearer than paragraphs. Full sentences sometimes use too many words.*

- Platform: Android 9.0 Pie (for **83.8%** can download the game [[Android Distribution](https://9to5google.com/2023/06/02/android-13-june-distribution/)])
- Audience: Students with friends
- Storage: **TODO**

## Development Roadmap

*Contain project's development milestones and phases of work.*

1. [ ] Planning
    - [ ] Research
    - [ ] Documents

2. [ ] Design
    - [ ] Wireframe
    - [ ] User flow

3. [ ] Development
    - [ ] Setup
    - [ ] Configuration
    - [ ] Main Page

## References

- [GameDev Underground](https://imgv2-2-f.scribdassets.com/img/document/470888352/original/5b3a0b6b63/1683989803?v=1)
- [gamedevbeginner](https://gamedevbeginner.com/wp-content/uploads/GDD-example-2.png)

Back to [Table of Contents](#table-of-contents)
