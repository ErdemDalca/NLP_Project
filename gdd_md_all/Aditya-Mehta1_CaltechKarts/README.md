# Game Design Document

## Section 0: Summary
Working Title: CaltechKart
Team Members: Dhruv Verma, Aditya Mehta, Jacobo de Juan Millon
Concept Statement: A 2D arcade racer on Caltech campus


## Section 1: Gameplay
Players must complete 5 laps around a track on Caltech’s campus in a time trial or against an AI racer. A player wins if they beat the AI racer or set a new time trial record (lowest time).

The game will use WASD/Arrow keys to control the car with the spacebar triggering a power-up. We will also use a mouse handler for buttons in the menu.

We incorporate the physics engine by having collisions with other racers/obstacles/barriers. We will also heavily utilize the physics engine while regulating the movement of the car through its acceleration, velocity and turning radius using friction.

The player will open a menu where they can select their game mode and toggle the settings (AI difficulty and no music). Then they will be prompted to choose their vehicle, which will all have different speed, handling and acceleration parameters. They will then start the race where the starting lights will count down. When the lights turn green the players start the race until they cross the finish line 5 times. Then we will display a podium and game summary taking the player back to the menu.

We will draw sprites for the cars and create a scrollable background for the Caltech track.


## Section 2: Feature Set
Priority 1:

Scrollable background - Jacobo
The track will be implemented as a scrollable background

Key Handler - Aditya
We will use the key handler to control the movement of the car
We will also use for toggling menu options and using power ups

Movement - Dhruv
We will use the physics engine to update the cars position
We need to implement friction to calculate the turning radius

Collisions - Dhruv
We will implement collisions with other racers, obstacles and barriers
We need to implement a collision handler with power-ups

Priority 2:

Sprites and Map - Aditya
Sprites for background and different surfaces, the karts, and items (power-ups).

Checkpoints - Aditya
Ensure that player is not moving backwards by checking if checkpoints are crossed in order and in the right direction

Times / Text - Jacobo
Keep track of time passed to get best scores.
Timer to indicate the start of race

Friction / Surfaces - Dhruv
Make some karts’ surfaces more slippery (lower friction) to make it harder to turn
Create surfaces where karts have lower maximum speed

Menu - Dhruv
Buttons to race against AI or Ghost (Time trial)
Settings Menu to toggle AI speed, music and available items
Car selector page varying different parameters for movement

Priority 3: 

Powerups - Jacobo
Controls powerup abilities (speed-up, slow-down etc)

Obstacles and Barriers - Dhruv
Adds obstacles and track limits to the track

Ghosts - Dhruv
Remembers best path
Turns racer collision with ghost off

Wrong way detector - Aditya
Check at all times that the user is going in the correct way along the track
If the user starts going in the wrong way, have a warning pop up on the screen informing them 

Priority 4:

Improve integration - Aditya
Use Simpson’s rule for velocity and position update

Music - Jacobo
Background music
Sound effects for powerups and crashes

AI Opponent racer for the user - Dhruv
Follows an optimal path (racing line)
Can change difficulty (of speed of the car)


## Section 3: Timeline
Aditya:
- May 27, 2024: Key Handler + Sprites and Map
- June 4th. 2024: Checkpoint + Wrong way detector
- June 11th, 2024: Improve Integration  

Dhruv:
- May 27, 2024: Movement, Collision Handler, Friction
- June 4th, 2024: Make menu
- June 11th, 2024: AI opponent

Jacobo:
- May 27, 2024: Scrollable background
- June 4th, 2024: Powerups
- June 11th, 2024: Times/text, music

## Section 4: Disaster Recovery
If any team member falls behind, we will try and redistribute the work equally by assigning them more work for the next week but picking up their slack on the late work. If there is not enough time to recover, we might decide to not implement certain non-essential features like music, specific power-ups, or the time trial game-mode.