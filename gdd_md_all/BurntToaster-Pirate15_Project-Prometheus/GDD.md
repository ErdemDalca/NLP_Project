# Introduction
## Game Summary
Prometheus is a top-down metroidvania turn-based tactics game about an alchemist attempting to restore the sun.

## Inspirations
* Turnip Boy Commits Tax Evasion (and other Zelda-like games)
* Transister ("go to a new room, fight, explore" loop)
* Hoplite (mobile game, how it blends combat with puzzle)
* Into the Breach (seeing enemy intention, environmental interactions as part of core combat mechanic)

## Player Experience

## Platform
This runs on Windows, Linux, and in Web.

## Development Software
Programming: Godot Engine

Art: 

Music: 

## Genre
Singleplayer Metroidvania Turn-based Tactics Adventure

## Target Audience


# Concept
## Gameplay Overview
Navigate the overworld, armed with the Potion Launcher.
The overworld is made up of multiple rooms. When player enters a new room, the room is shrouded in SHADOW (room is grayscale), and filled with SHADOW creatures.
The ALCHEMIST must purify the room without hurting the SHADOW CREATURES, by getting to the SUNflowers (colored).
Upon reaching enough SUNflowers, the ALCHEMIST's SUNSPARK activates, purifying the room and every SHADOW creatures within it.

## Theme Interpretations
ALCHEMY brought prosperity to humankind, but at the cost of gradually corrupting our surroundings.
First, it was the AIR. Air was filled with alchemical fumes, and soon, people couldn't breathe the air without protection, also made through ALCHEMY.
Next, it was the WATER. Not even the cleansing nature of WATER could wash away all the corruptive fumes. ALCHEMISTS made distilleries to try to purify the WATER.
Then, it was the EARTH. The WATER carried its corruption into the EARTH, and soon the soil grew sour. ALCHEMISTS still tried to fix the EARTH with more ALCHEMY.
And finally, it was the FIRE. The SUN itself was swallowed by the SHADOWS and shattered. The SUNSPARKS scattered around the world, carrying what little strength remains of the SUN.
It wasn't just you who made this happen, but you were one of the ALCHEMISTS. With a shard of SUNSPARK in protected by ALCHEMY, you venture out to collect the SUNSPARKS and restore the SUN...

## Primary Mechanics
* Turn cycle: Player makes 1 action, all the NPCs make 1 action each
* Player is armed with potion gun, with a bunch of different options depending on what they unlocked so far
* Each shadow has a small moveset, and they tell you in advance what they will do (i.e. Into the Breach)
* Players must get to 3 out of 5 SUNflowers to extract the latent energy of the SUN and purify the room. This restores color to the room and you can now safely explore.
* (There should be some sort of turn timer. Refer to Issue 16 for discussion.)

### Potion Launcher
Shoot potions to interact with the world.
* Alchemist's Fire: ranged attack in a line, knocks back and Stun 1 first enemy hit. (Stun X: prevent next X turns of the hit enemy)
* Watercharm Potion: makes a 3x3 pond in target area. Knockback 1 characters caught in it outward. Non-flying characters can't walk on water. (Knockback X: move character by X away from the point of origin)
* Tailwind Potion: makes a 2x2 area of wind that Shift 1. Shift 2 flying characters. (Shift X: move in a predetermined direction by X when they first enter the area)
* Ice Potion: can freeze all water in 5x5 area, turning it to Ice.

### Enemies:
* Shadow squirrel: can come out of trees, and are territorial (5x5 area around the originating tree). Can move by 1 each turn, and attacks instead if adjacent.
* Shadow bird: Can move 1 or 2 in a line each turn, attempting to line up with . Flying. Can swoop, moving 1 and attacking if in the next space.

### Environment:
* Tree: impassable terrain. Can spawn squirrels.
* Water: impassable terrain for non-flying characters. can be frozen
* Ice: characters who walk on it will slide until collision. can be melt

# Art

## Theme Interpretation

## Design

# Audio

## Music

## Sound Effects

# Game Experience

## UI

## Controls

# Development Timeline
See [Task Board](https://github.com/orgs/BurntToaster-Pirate15/projects/1)
