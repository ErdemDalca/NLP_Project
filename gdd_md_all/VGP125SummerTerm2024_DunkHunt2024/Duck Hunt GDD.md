# DUNK HUNT GDD
#### Audience:
-	Teacher
-	Friends and victims willing testers
## Core Goal
Recreate Duck Hunt in Unity

## Story: 
Dark and brooding, the ducks killed the hunters family, now he’s killing them. [title card]

## Art: 
Use existing assets wherever possible
Custom assets for possible stretch goals:
-	Zombie ducks
-	Cyborg ducks
-	Chimera ducks
-	Turtle ducks

### Sprites:
- Ducks
- Trees
- Grass
- Bush
- Foreground (dirt)
- Ammo
- Hearts
- Backgrounds
- Title image
- Custom cursor / crosshairs
- Particle FX: (Stretch goal)
  -	On shoot
  -	On duck hit
  -	On duck landing
  -	On dog dives

## Mechanics
-	Aim with a mouse
-	Shoot with left click
-	Hit a duck
-	Duck behaviour
-	Dog behaviour
-	Ammo counter
-	Duck counter
-	Game Modes
-	1 Duck
-	2 Ducks
-	Clay Shooting (stretch goal - on team agreement only)

## Gameplay
### Title Screen
Players are able to navigate up and down the menu to 3 options: Game A, Game B and Game C. The top score is displayed along the bottom of the screen and will need to be updated when the player returns to the main menu 

### Game Scene 
The dog runs out as the level begins and jumps behind the grass. A jingle plays and ducks fly out. Players have 3 shots per round of duck(s) and a hidden time limit (5 seconds) before the ducks fly off. They will need to kill 10 ducks before the next round begins.

When the player kills a duck, they fall behind the grass as the dog picks them up. The score updates as soon as the duck gets shot. The round counter updates after all 10 ducks have been killed and the round progression is called. If players kill all 10 ducks successfully by the end of the round, they’ll get a point bonus depending on what round they’re on.  

If a player misses a duck, the sky behind the grass and trees briefly turns pink with “Fly Away” written on it before returning back to normal. The dog laughs at the player and spawns a new duck. If players fail to reach the limit of ducks (determined by the blue bar beneath the duck meter), A jingle plays and a box with “game over” written on it appears above the laughing dog with the game over music playing, then the players are brought back to the title screen as the song ends.

---


#### Authors:  
Amelia Harrison  
Jonathan Anthony  
