# Tiny Tank Survival Game Design Document
## Game Concept
The game is arcade style Player vs Enemy top down 3D shooter. It is a single player game, but could later be extended to multiplayer as well - by replacing NPCs with other players. While the game doesn't have set age requiremenets, its target audience ranges mainly from 10-25 year olds, because of its simple/cartoony artstyle and fast-paced action.

## Gameplay
- The main objective for the player is to survive as long as possible and destroy as many enemy tanks as possible.
- Every destroyed tank gives points, the points are given based off how hard it is to kill the given enemy, in other words - slow, weak enemies give less points than fast and strong enemies. When the player dies, they can put their score on the leaderboard.
- Game has a simple progression system - it is divided into rounds, at start of which, a new wave of enemy tanks spawn. Each subsequent round adds more and more enemies into each wave, as well as different types of enemy tanks or with upgraded stats (speed, reloading, ammo).
- After each round, the player is given time to choose a single upgrade that they can add onto themselves, they can also save up upgrade points for more valuable upgrades.

## Mechanics
- Every tank (both enemies and player) can have between 1 and 10 bullets in stock.
- The reload speed for a bullet in stock can be between 0.1 and 3 seconds.
- The bullets can bounce off of walls at least one time, special bullets or upgrades can upgrade this to more.
- To destroy a target, all the bullet needs to do is hit it. Applies to both player and enemies.
- All tanks can collide with each other and, of course, the map. They can't collide with destroyed tanks (neither can bullets).

## Game elements
The player can choose a map on which to play. Every map includes the player's "safe area", which is supposed to be the furthest away from enemy spawn locations. The maps are with simple design - no heavy visibility obstruction or complex collisions. 

### Characters (Tanks)
1. Regular tank - basic movement and can shoot straight where the player is aiming. Bullets bounce against the walls.
2. Artillery tank - basic movement, but the bullets go directly to the spot where the player aimed. Bullets ignore walls, because they fly over them, but do show a red spot FOR ALL PLAYERS, where it will land.

### Upgrades
- Tank speed - ability to go forward/backward faster
- Tank rotation - ability to turn left/rigt faster
- Ammo reload speed - ammo reloads faster (each bullet)
- Ammo capacity - add 1 more bullet in stock
- Bullet bouncyness - improve all bullet bouncyness (off walls) by 1

## Milestones
1. Implement basic movement for the player. The player needs to have a simple test tank, that could later be used as a reference for other tank models in the future. Create a test map, where the main gameplay loop will be tested. Implement simple spawning of enemies.
2. Implement core bullet mechanics - bouncing off walls and destroying player/enemies. Add shooting mechanic to player. Add movement & shooting AI to enemies. Implement round progression & score HUD.
3. Implement upgrade system (after rounds, reload, speed, etc. limitations). Add other types of tanks. Create more maps. Add UI for leaderboard and other necessary menu elements.