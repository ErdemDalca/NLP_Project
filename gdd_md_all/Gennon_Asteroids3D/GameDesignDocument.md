# Game Design Document

## Asteroids 3D

### Concept

This game is a 3D version of the classic Asteroids game. The player controls a spaceship and has to destroy asteroids and enemy spaceships. The player can collect power-ups to upgrade the spaceship.

### Genre

Single-player, action, arcade.

### Target Audience

The target audience is anyone who enjoys playing arcade games. Especially people who played the original Asteroids game and want to try a 3D version of it.

## Gameplay

### Mechanics

The player controls a spaceship and has to destroy asteroids and enemy spaceships. The player can collect power-ups to upgrade the spaceship. The view is from a top-down perspective. The player can move the spaceship in all directions and rotate it. The player can shoot bullets and missiles.

### Controls

The player can move the spaceship forward and backward and rotate it. The player can shoot bullets and missiles. The player can pause the game, restart and quit.
The player can use the keyboard or a gamepad (need to verify using web export) to control the spaceship.

- Forward: W, Up Arrow, Left Stick Up
- Backward: S, Down Arrow, Left Stick Down
- Rotate Left: A, Left Arrow, Left Stick Left
- Rotate Right: D, Right Arrow, Left Stick Right
- Shoot Bullets: Space, Right Trigger

### Progression

There should be 3-5 levels depending on the time available. Each level should be more difficult than the previous one. The difficulty should increase by increasing the number of asteroids and enemy spaceships. The player should be able to upgrade the spaceship by collecting power-ups. The power-ups should increase the speed of the spaceship, the number of bullets and missiles, and the damage of the bullets and missiles.

Level 1: The player has to destroy X amount of asteroids.
Level 2: The player has to destroy X amount of asteroids and Y amount of enemy spaceships. Spaceships should shoot bullets and has a chance to drop power-ups.
Level 3: The player has to destroy X amount of asteroids and Y amount of enemy spaceships. Spaceships should shoot bullets, has a shield and has a chance to drop power-ups.

Levels beyond level 3 should be similar to level 3 but with more asteroids and enemy spaceships if there is time to implement them.

### Win condition

Each level should have two different modes.

- The first mode is a time limit mode where the player has to destroy all asteroids and enemy spaceships before the time runs out. The best time should be saved and displayed on the main menu.
- The second mode is an endless mode where the player has to survive as long as possible and get the highest score. The player can get a higher score by destroying asteroids and enemy spaceships.

If time permits then there should be a global leaderboard for both modes on all levels. That will be created in a different repository but communicated with the game using a REST API.

## Art

### Art Style

The game will make use of Low Poly art style. The game will use a top-down perspective and all models will be far from the camera. All the models will be created in Blender using [Imhenzia PixPal Texture](https://imphenzia-free.nyc3.cdn.digitaloceanspaces.com/imphenzia-pixpal-1.1.zip).

### Characters

#### Spaceship

The spaceship will be a simple low poly model based on inspiration from the following image.

![Spaceship](low_poly_spaceships.png)

It will have a thruster particle effect and a shield particle effect.

#### Missiles

There should be three or more missiles, depending on available time. The missiles should be simple low poly models with a particle effect for the thruster. Changing missiles should be a power-up.

#### Asteroids

The asteroids should be simple low poly models. The asteroids should be able to break into smaller asteroids when destroyed and also have an explosion effect. The color and size should be random. They should travel in a straight line and rotate. They should not collide with each other only with the spaceship.

#### Enemy Spaceships

The enemy spaceships should be simple low poly models. They should be able to shoot missiles and have a chance to drop power-ups. Some should have a shield. The different types should be distinguishable using colors and/or different models. They should move in a pattern that the player can recognize and use to their benefit. They should not collide with each other only with the spaceship and asteroids.
They should have a particle effect for the thruster and a shield.

### Environments

The game will take place in space. There should be different backgrounds for each level. The background should be some kind of effect that is moving. There could be elements like:

- Stars
- Nebula
- Planets
- Comets

## Sound

All sounds will be credited to other people and under the CC0 or CC-BY licenses. Mainly from [Freesound](https://freesound.org/) and [OpenGameArt](https://opengameart.org/).

### Music

We need to find music that fits the game. It should be something that is not too distracting but still fits the theme of the game. It should be something that can be looped and more modern than the original Asteroids music, but still have a retro feel to it.

- [Space Shooter Music](https://opengameart.org/content/space-shooter-music)

We need the following tracks:

- Menu
- Level 1
- Level 2
- Level 3

### Sound Effects

- [16-bit SFX](https://opengameart.org/content/sfx-the-ultimate-2017-16-bit-mini-pack)

We need the following sound effects:

- Spaceship Thruster
- Spaceship Shooting (multiple)
- Spaceship Explosion
- Asteroid Explosion
- Enemy Spaceship Explosion
- Enemy Spaceship Shooting
- Power-up Pickup
- Game Over
- Level Complete
- Level Start
- Menu Select
- Menu Back
- Menu Screen Change

## Technical

### Platforms

This game will be released on Itch.io and will be playable in the browser and on Windows, Linux, and Mac.

### Programming Language and Tools

The game will be made using GDScript and the Godot Engine. The game will be developed in Godot 4.2.2 or later.

### System Requirements

Basically a computer with modern browser like Chrome, Firefox, Edge, or Safari. The game will be playable on Windows, Linux, and Mac. I will look into mobile support but it is not a priority.

## Schedule

### Development Milestones

#### Level 1:

- Main Menu
- Level Select Menu
- Level 1 with asteroids
- Spaceship
- Local leaderboard (best score and time)
- The player has to destroy X amount of asteroids before the time runs out
- Music and sound effects for menu and level 1

#### Level 2:

- Level 2 with asteroids and enemy spaceships
- Enemy spaceships can shoot bullets
- The player has to destroy X amount of asteroids and Y amount of enemy spaceships before the time runs out
- Music and sound effects for level 2

#### Level 3:

- Level 3 with asteroids and enemy spaceships
- Enemy spaceships can shoot bullets and has a shield
- The player has to destroy X amount of asteroids and Y amount of enemy spaceships before the time runs out
- Music and sound effects for level 3

#### Leaderboard:

This might be scipped if the projects takes too long.

- Global leaderboard for all levels and modes
- Leaderboard Menu
- Leaderboard API
- Leaderboard UI
- Music and sound effects for leaderboard

#### Polish:

- Polish the game
- Publish the game on Itch.io using Godot CD Action

### Launch Date

The game will be released when it is done. Whenever time permits me to finish it. The goal is to have a playable version on Itch.io by the end of the year 2024.
