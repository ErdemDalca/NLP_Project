# Dome Gardener or Guardiens of Gua

*Inhaltsverzeichnis aus dem Mass Flux Design Document von der Pirate Software develop.games Seite*
[Mass Flux GDD](https://docs.google.com/document/d/1Vl7BMvzUOhbunJrI_X1gUc6x-LAp3aaBiPwHUf27B70/edit?tab=t.0#heading=h.lr899156xjnx)

## Introduction

### Game Summary

Guardiens of Gua is a game only controlled with one button. You protect your plants from hungry bugs with a vicious force field.

### Inspiration

Our game is inspired by tower defense games such as Dome Keeper.

### Player Experience

It will be a challenge, but with a light-hearted tone.

### Platform

Web-based, any pc

### Development Software

raylib, maybe more?

### Genre

tower defense

### Target Audience

Casual gamers


## Concept

### Gameplay Overview

You can shrink and grow your force field to kill the bugs. With time more bugs will spawn and you will have to defend more plants.

### Theme Interpretation (Dome, Agreement, Bug)

We chose to focus on the keywords Dome and Bug. That can be seen by the force field dome and the bug enemies.

### Primary Mechanics

1. The Force Field kills bugs, and can change it's size
2. Bugs can destroy your plants, which leads to game over

### Secondary Mechanics

1. Over time more plants will grow
2. There will be different kinds of bugs


## Art

### Theme Interpretation

We will have bugs and a dome.

### Design

Lots of

Rectangles Rectangles
Rectangles Rectangles

and minimalistic


## Audio

### Music

8-Bit Sound, very few voices -> minimalistic

### Sound Effects

Similar to the above.


## Game Experience

### UI

Tbd.

### Controls

Just one button.


## Development Timeline

### Minimum Viable Product

| What to do?                      | When to be done? | Whoms work?     |
|----------------------------------|------------------|-----------------|
| Enemy Spawning                   | 30.11.           |       |
| Enemy Behaviour                  | 30.12.           |         |
| Visual Assets (Dome, Plant, Bug) | 01.12.           |  |
| Start Menu                       | 01.12.           |  |
| Main Theme (Music)               | 01.12.           |           |
| One Background Music Track       | 01.12.           |          |
| Sound effects                    | 30.11.           |          |

### Beyond (if ahead of schedule / extra time)

day night cicle
advanced input handling -> tapping
hard mode -> smaller dome, more tapping, STEPS as a var
enemy animations

### Notes

To plants spawning: The plants are constructed out of hollow Rectangles. The first plant has the power of reproduction, by filling itself out (with color). When she is full a new offspring will be spawned and there small chance that it too can reproduce.
