# Game Design Document

Outline taken from here: https://docs.google.com/document/d/1Vl7BMvzUOhbunJrI_X1gUc6x-LAp3aaBiPwHUf27B70/edit

- [Game Design Document](#game-design-document)
  - [Introduction](#introduction)
    - [Game Summary](#game-summary)
    - [Inspiration](#inspiration)
    - [Player Experience](#player-experience)
    - [Platform](#platform)
    - [Development Software](#development-software)
    - [Genre](#genre)
    - [Target Audience](#target-audience)
  - [Concept](#concept)
    - [Gameplay overview](#gameplay-overview)
    - [Theme Interpretation](#theme-interpretation)
    - [Primary Mechanics](#primary-mechanics)
    - [Secondary Mechanics](#secondary-mechanics)
  - [Art](#art)
    - [Theme](#theme)
    - [Design](#design)
  - [Audio](#audio)
    - [Music](#music)
    - [Sound Effects](#sound-effects)
  - [Game Experience](#game-experience)
    - [UI](#ui)
    - [Controls](#controls)
  - [Development Timeline](#development-timeline)


## Introduction

### Game Summary

"You are responsible for setting an exeperimental bacteria colony free. Unfortunately, said colony replicates at an unprecedented speed. Double unfortunately, its favorite food is meat! You better make use of that energy core and get out of there!"

The game revolves around a rapidly spreading bacteria colony which the player character is responsible for. They then have to escape the premises by going through fast-paced platforming challenges. The movement tries to be as fluid as possible to encourage going fast.

### Inspiration

- *Downwell* is the primary source of the artstyle and simple gameplay. It only uses a few colors uses those to indicate dangers and pickups.
- *Pizza Tower* has easily mastered the art of designing controls for 2D platformers that allow you to go *really fast*.

### Player Experience

The player should feel a sense of anxiety or pressure when playing for the first time as the bacteria grows and fills up rooms behind them. Later on as they master the movement, they should feel in control while blazing through the levels.

### Platform

Windows, Linux

### Development Software

- Engine: Godot
- Editor: VS Code
- Pixel-art: Aseprite
- Audio editor: Audacity

### Genre

Platformer, rogue-lite

### Target Audience

General audiences familiar with some platformers.

## Concept

### Gameplay overview

The player's main objective is to escape the bacteria while overcoming various obstacles such as spikes, traps and enemies. There is a distinct focus on speed. The level design and movement directly support that. On the topic of levels, they are a collection of rooms that can be assembled in any order. (with some restrictions) This allows for randomly generated levels of any length.

During gameplay, the player is able to find collectables that may then be spent on upgrades. There are also secret paths that contain power-ups and/or lots of currency.

The game is "won" if the player reaches the final exit.

### Theme Interpretation

Bacteria are well known for their ability to rapidly reproduce. The "natural" next step is to come up with a bacteria reproduces at a comical scale. To make it extra dangerous, it really likes to eat other creatures.

### Primary Mechanics

![](img/mockup.png)

### Secondary Mechanics

...

## Art

### Theme

The game plays out in an abandoned reasearch complex. Since the bacteria is ever-growing, it will quickly fill up the current room and spill out to the next. This fuels the impending feeling of claustrophobia, putting some pressure on the player.

### Design

Since we don't have a lot of time on our hands, the visual style is mostly monochrome with specific colors for negative and positive elements. In the default case, red signifies danger and blue corresponds to the player character and collectibles.

Objects are created using simple pixel-art with a focus on readability. There will be some background decoration but not too much. The player is simple, gender-ambiguous stick figure with a blue core. While said core doesn't have clear function right now, it may be useful to convey the player state at some point.

## Audio

### Music

TBD. Probably some sort of chiptune or tracker music. Will probably have to grab some free assets.

### Sound Effects

Sound effects should be punchy and clearly bitcrushed. Fortunately, reducing the quality of sound effects is a lot quicker than enhancing them.

## Game Experience

### UI

...

### Controls

- Controller (xbox)
  - A/Y: Jump
  - B/X: Dash
  - LStick/DPad: Movement
- Keyboard (QWERTZ)
  - Y: Jump
  - X: Dash
  - Arrows/NumPad: Movement

## Development Timeline

...