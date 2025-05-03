# PSGJ-July-2024

Game Design Document(GDD) for the July 2024 Pirate software Game Jam with the theme _Shadow Alchemy_.

Authors: iFire, Yolodude, Ryan, Lagmaister, Profilename14

# Introduction

## Requirements

### Theme requirements

Shadows and Alchemy

The community decided on combining the two winning themes of Shadows and Alchemy. Shadows can relate to a number of different subjects outside of light levels. Think about shadow governments, secret societies, or elemental effects. Alchemy can also be used for much more than mixing potions. Alchemy is about transformation, synthesis, combination, and hidden knowledge.

Themes are meant to be a restriction that you need to solve your way out of. Don't despair if this is a theme you dislike, instead try to find a creative solution where you can have fun and try something you otherwise wouldn't have.

### Delivery requirements

July 30th 2024

- A planning document that details what your game will be.
- A limited working copy of your game.
  - Focus on playability over anything else.
  - If it doesn't run, it won't win.
  - If you don't submit a valid link your submission will not be accepted.

## Jam Objectives

- [ ] Have fun
- [ ] Finish something for once

## Game Summary Pitch

You were going about your day eating cereal and watching cartoons, when you have to go outside.
OH NO! Your shadow is gone! I must gather the combined power of other shadows so I can capture my shadow back.

- Top-Down adventure, sneak through shadows, collect alchemy ingredients, turn-based battle

- Card battler that involves collecting "aspects" (mana of different types ala thaumcraft) from background objects

- A game in the vein of Echoes of Wisdom focused on creating "shadows" of objects in the world

- possibly tied to the above, a pokemon esque game where you capture shadow versions of monsters you find. Pokemon types can be based off metals! "Stealing shadows" involves alchemy "ingredients." Shadows can be more like Pokemon cards in that they have a few select attacks/abilities, and you switch between them constantly.

- Card battler sim where you make cards from potions and the cards get played onto the board to create some shadow-fied miniatures.

- Two Abilities (any combination of Attack and Defense)

## Inspiration

- Slay the Spire
- Pokemon

## Player Experience

## Platform

The game is developed to be released as a web game on [Itch.io]().

## Development Software

- Engine: Godot 4.2
- Art Software: Aesprite
- Audio Software:

## Genre

- Turn-based card battler with simple overworld adventure

## Target Audience

# Concept

## Gameplay Overview

## Combat

During a normal encounter, the player battles a single enemy that has HP, a list of 1-2 moves, and possible passives (think about as complex as a pokemon card). The player's "Pokemon" is a set of multiple shadows that they've captured from previous foes. During their turn, the player can select first one of their shadows for their "fake shadow" to take form this turn. Then, the player can select one of that shadow's attacks. After this, the opposing shadow goes, damaging the player's own hp (respecting the type of their currently selected shadow)

A monster has a type, amount of hp (only wild monsters), and set of attacks or passives (usually 1-2 attacks and 0-1 passives). Attacks have an element assigned to them with damage bonuses to certain other types, a base damage, and sometimes special effects. They also have associated costs: In order to use most attacks the player has to sacrifice reagents that the player prepares at checkpoints and regenerate at the start of combat. The player's resources and the opposing monster's type, as well as possible special effects the player has available, push the player to use different shadow forms on different turns.

Reagents are the main mechanic influencing combat. The player at a checkpoint can allot their total balance of reagents, which is double the number of reagent types they have unlocked. For example if the have the earth and water reagents, the player has 4 total slots they can alot between earth and water (3 earth + 1 water is possible).

There are 4 total reagents in the demo, being water, earth, fire, and air, but the player starts with none and has their starting shadow form use no reagents at all. There's a metroidvania-esque progression in collecting all 4. Attacks with multiple reagents are super effective vs all types.

Enemies have reagents as well. Enemies have a list of reagents they are capable of using for any of their attacks, starting with 1 of each and having a maximum of 2. At the start of every player turn (including their first), enemies have a 50% chance of gaining each reagent and then decide randomly their next attack, showing the player which one they'll select similar to slay the spire. We can customize this later if we find it stifles late game enemies.

Likewise, the player regenerates reagents according to the chart below.

## Combat Test

The combat test will have the player immediately start in a battle against a single opponent with 2 debug monsters, every reagent in equal amounts (2 each), and a strong debug enemy.

The player has a base attack (as a formless blob) that's free and deals 20 damage (in case the player runs out of reagents).

Example player shadow 1: Living tree (earth type, 280 hp)

1. Earth Attack: 40 damage (costs 1 earth)
2. Water Attack: 40 damage + take 40 less damage this turn (costs 2 water)

Example player shadow 2: Luminous Moth (air type, 200 hp)

1. Air Attack: 30 damage + clear debuffs (costs 1 air)
2. Fire Attack: 40 damage + the opponent takes 20 damage per turn for 3 turns (costs 1 air and 1 fire)

Example monster: Volcanic Snail (sulphur type, 300 hp)

1. Water Attack: 20 damage + remove 1 fire reagent (costs 1 water)
2. Fire Attack: 70 damage + 50% chance opponent is stunned (costs 1 earth, 1 fire, and 1 water)

The base damage, excluding special effects, of any attack is doubled when there's type effectiveness and halved when there's type ineffectiveness. The player starts with 200 hp in any random encounter by default (we may add health upgrades later on though).

This test will just have a tree / moth back sprite, a shadow blob back sprite, and an eel front sprite, as well as the ui for every reagent.

## Reagents

## Alchemy Points

- lv1: 3AP - 1 Regen
- lv2: 3AP - 2 Regen
- lv3: 5AP - 2 Regen
- lv4: 5AP - 3 Regen
- lv5: 7AP - 3 Regen

### Type Chart

![image](https://hackmd.io/_uploads/rJrs5FBuC.png)

**How Type effectivness works:**

An element can be a fundamental element (Earth, Water, Air or Fire), a second level element (Salt, Mercury, or Sulphur), A higher element (Celestial or Niter), or the Prima Materia: Metal.

Any element beats all elements in layers under it, and is beaten by all elements in layers above it. Niter is beaten by metal, neutral towards Celestial, and beats all other elements both defensively and offensively.

However, when a monster of an element performs an attack with a combination of energies, if those energies combine into the target element, then that attack becomes that element and is super effective. For example, an attack that costs 1 air and 1 fire used against a sulphur enemy deals double damage. This same attack is also neutral to Salt and mercury types, but ineffective against metal, celestial, and niter.

An attack may have at most two elements. In addition to considering the elements of the attack, any damage over time debuffs will add to the element of that attack. For example, a water debuff will cause the air and fire attack above to not only hit sulphur super effectively, but all 3 in that layer as well as niter. Likewise, adding an earth debuff to that even allows beating metal.

## Theme Interpretation

- Objects contain a shadow that can be captured and shadows fight with the power of alchemy reagents

## Mechanics

- Turn based battle using shadow creatures
- Alchemy for items
- Alchemy for capturing shadows

# Art

## Design

### Overworld

An isometric view of a small town.

### Battles

As the battles have two fases:

Preparation phase: the screen is dominated by an alchemy table, with an open tome with the colection of captured shadows, and some vials...

further in the backgroud a bit of the enemy and up close our shadow blob

Attack Phase: The table slides down and our blob slides left, the enemy slides right, taking a more clasic RPG layout
two vials from the table are still visible, one full(and emtying) for out vitality, and one empty that fills for our AP

Upgrades will change the vials for bigger vials.

### Menus

## Assets

Organized in [Asset Task Board](https://github.com/orgs/PSJamTeam/projects/1/views/8).

|          |           | Extra <br>views | Anim | Node | Scene | Done | Notes            |
| -------- | --------- | --------------- | ---- | ---- | ----- | ---- | ---------------- |
| 1.1.1.0  | Door      |                 | no   |      |       |      | Tiles Outdoor    |
| 1.1.2.0  | Window    |                 | no   |      |       |      |                  |
| 1.1.3.0  | Wall      |                 | no   |      |       |      |                  |
| 1.1.4.0  | Roof      |                 | no   |      |       |      |                  |
| 1.1.5.0  | Chimney   |                 | no   |      |       |      |                  |
| 1.1.6.0  | Tree 1    |                 | yes  |      |       |      |                  |
| 1.1.7.0  | Tree2     |                 | yes  |      |       |      |                  |
| 1.1.8.0  | Mail Box  |                 | no   |      |       |      |                  |
| 1.1.9.0  | road      |                 | no   |      |       |      |                  |
| 1.1.10.0 | grass     |                 | no   |      |       |      |                  |
| 1.2.1.0  | chicken   | X3              | yes  |      |       |      | Tiles Characters |
| 1.2.1.1  | chicken   | front           | yes  |      |       |      |                  |
| 1.2.1.2  | chicken   | side            | yes  |      |       |      |                  |
| 1.2.1.3  | chicken   | back            | yes  |      |       |      |                  |
| 1.2.2.0  | squirrel  | X3              | yes  |      |       |      |                  |
| 1.2.3.0  | cat       | X3              | yes  |      |       |      |                  |
| 1.2.4.0  | dog       | X3              | yes  |      |       |      |                  |
| 1.2.5.0  | Person 1  | X3              | yes  |      |       |      |                  |
| 1.2.6.0  | Person 2  | X3              | yes  |      |       |      |                  |
| 1.2.7.0  | Player    | X3              | yes  |      |       |      |                  |
| 1.3.1.0  | wall      |                 | no   |      |       |      | Tiles Indoors    |
| 1.3.2.0  | window    |                 | no   |      |       |      |                  |
| 1.3.3.0  | fridge    |                 | yes  |      |       |      |                  |
| 1.3.4.0  | sink      |                 | no   |      |       |      |                  |
| 1.3.5.0  | bed       |                 | no   |      |       |      |                  |
| 1.3.6.0  | coutch    |                 | no   |      |       |      |                  |
| 1.3.7.0  | TV        |                 | yes  |      |       |      |                  |
| 1.3.8.0  | table     |                 | no   |      |       |      |                  |
| 1.3.9.0  | chairs    |                 | no   |      |       |      |                  |
| 1.3.10.0 | floor     |                 | no   |      |       |      |                  |
| 2.1.1.0  | Tree 1    |                 | no   |      |       |      | Combat Cards     |
| 2.1.2.0  | Tree2     |                 | no   |      |       |      |                  |
| 2.1.3.0  | Mail Box  |                 | no   |      |       |      |                  |
| 2.1.4.0  | house     |                 | no   |      |       |      |                  |
| 2.1.5.0  | chicken   |                 | no   |      |       |      |                  |
| 2.1.6.0  | squirrel  |                 | no   |      |       |      |                  |
| 2.1.7.0  | cat       |                 | no   |      |       |      |                  |
| 2.1.8.0  | dog       |                 | no   |      |       |      |                  |
| 2.1.9.0  | Person 1  |                 | no   |      |       |      |                  |
| 2.2.1.0  | Tree 1    |                 | yes  |      |       |      | Combat Enemies   |
| 2.2.2.0  | Tree2     |                 | yes  |      |       |      |                  |
| 2.2.3.0  | Mail Box  |                 | yes  |      |       |      |                  |
| 2.2.4.0  | house     |                 | yes  |      |       |      |                  |
| 2.2.5.0  | chicken   |                 | yes  |      |       |      |                  |
| 2.2.6.0  | squirrel  |                 | yes  |      |       |      |                  |
| 2.2.7.0  | cat       |                 | yes  |      |       |      |                  |
| 2.2.8.0  | dog       |                 | yes  |      |       |      |                  |
| 2.2.9.0  | Person 1  |                 | yes  |      |       |      |                  |
| 2.2.10.0 | Person 2  |                 | yes  |      |       |      |                  |
| 2.2.11.0 | Player    |                 | yes  |      |       |      |                  |
| 2.3.1.0  | Tree 1    |                 | yes  |      |       |      | Player Units     |
| 2.3.2.0  | Tree2     |                 | yes  |      |       |      |                  |
| 2.3.3.0  | Mail Box  |                 | yes  |      |       |      |                  |
| 2.3.4.0  | house     |                 | yes  |      |       |      |                  |
| 2.3.5.0  | chicken   |                 | yes  |      |       |      |                  |
| 2.3.6.0  | squirrel  |                 | yes  |      |       |      |                  |
| 2.3.7.0  | cat       |                 | yes  |      |       |      |                  |
| 2.3.8.0  | dog       |                 | yes  |      |       |      |                  |
| 2.3.9.0  | Person 1  |                 | yes  |      |       |      |                  |
| 2.4.1.0  | Table     |                 | no   |      |       |      | Combat UI        |
| 2.4.2.0  | Tome      |                 | yes  |      |       |      |                  |
| 2.4.3.0  | HP Beeker | X4              | yes  |      |       |      |                  |
| 2.4.4.0  | AP Beeker | X4              | yes  |      |       |      |                  |
| 2.4.4.0  | Enemy HP  | X4              | no   |      |       |      |                  |
| 2.4.4.0  | Enemy Inf | X4              | no   |      |       |      |                  |

# Audio

Organized in [Asset Task Board](https://github.com/orgs/PSJamTeam/projects/1/views/8).

# Game Experience

## UI

## Learning the game

## Controls

# Development Tasks

Organized in [Github Task Board](https://github.com/orgs/PSJamTeam/projects/1/views/1).
