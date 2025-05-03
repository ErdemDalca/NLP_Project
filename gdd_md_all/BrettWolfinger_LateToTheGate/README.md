# Late To My Gate Game Design Document


## Game Summary
Late To My Gate is a runner arcade game designed to capture the frantic adrenaline of arriving to the airport late and having to rush to catch your plane. 

## Genre
Mobile runner/arcade

## Inspiration
### Temple Run
Temple Run is the inspiration behind the player perspective and gameplay. In Temple Run, players endlessly run down a lane, dodging obstacles and collecting coins until they hit an obstacle and must start over. Late to My Gate differs from Temple Run in that it is not endless, there are more nuanced environmental hazards, and that players will need to plan their route to navigate the airport.
[
](https://www.google.com/url?sa=i&url=https%3A%2F%2Fthebinarymessiah.com%2F2012%2F04%2F04%2Ftemple-run-810%2F&psig=AOvVaw1DuRDVS8FngJtbrYO8zhxa&ust=1726077721749000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLDq6N_6uIgDFQAAAAAdAAAAABAE)![image](https://github.com/user-attachments/assets/360c282d-3018-426c-b698-e3eca3ecaaae)

### Real Life Experiences at the Airport
Unlike Temple Run’s fictional setting, Late To My Gate is set in a realistically designed airport. This is intended to draw on player’s real-life experiences navigating airports to generate a more authentic feeling of anxiety. 
[
](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hksinc.com%2Fwhat-we-do%2Fprojects%2Fdfw-international-airport-terminal-d%2F&psig=AOvVaw1sXk_9erOYb9-41LBkNNrd&ust=1726077821990000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCe5477uIgDFQAAAAAdAAAAABAE)![image](https://github.com/user-attachments/assets/20f4b7ed-8ca6-466a-9a1c-ece635936bbf)

## Player Experience/Gameplay
The player navigates using a typical WASD/arrow keys to move and the camera is fixed behind the player. The player spawns in front of a map of the airport and is given a destination gate and a time to reach it. If the player reaches the gate in time the win, but if they don’t the plane takes off without them and they lose. The player must avoid AI controlled pedestrians, other obstacles, and utilize speed-up sections to get through the map quickly.

I’m currently in between two control schemes – using a single modifier such as shift to switch between sprint/walk, or having W and S act as accelerate and decelerate keys so there is a transition time between speeds. This would require players to plan out slowing down more in advance rather than letting go of the shift key as soon as they are close to an obstacle. Further, I think I might make A and D be lateral “lane shift” keys while using something like Q and E to rotate the player if they need to turn around.


## Additional Mechanics
-	Foot traffic/pedestrian simulation
    - Other traveler NPCs navigate their way through the airport and serve as the primary obstacle for the player to avoid
    - Possible Behaviors:
      - Walking straight,
      - Define groups of pedestrians that walk multiple people wide
      -	Stop and start semi randomly
      -	Turn into and out of side gate areas
  o	Colliding with another pedestrian will cause the player to lose all speed and be stunned for a few moments
-	Moving walkway speedup/slowdown
-	Slippery/wet patches
    -	Moving through these areas at too high of a speed will cause the player to slip and fall, losing all their speed
-	Hitching a ride on Electric Cart
    -	The player can jump on the back of passing by electric carts to potentially move through the airport faster. 
    -	They don’t actually have control over the cart however so it might take wrong turns or stop unexpectedly
-	Having to take a tram between terminals

## Minimum for Vertical Slice
-	A very simple and short airport environment to demonstrate the core concept
    -	Can be just a straight hallway without any major turns or traps
-	Full player controls
-	Basic pedestrian movement, even if it’s just moving in a straight line without stopping
-	Core Game Loop
    -	Ending the game when the player reaches the goal OR time runs out
    -	Restarting the player

## Stretch Goals
-	Hand design a more complex airport environment
    -	Level 1: Branching dead-end terminals
    -	Level 2: Terminals that require you to take a tram between them
-	Procedural Generation of airport environments
    -	Including traffic generation
    -	Makes it so that the player has a different experience each time
-	More advanced pedestrian AI control

## Project Checkpoint Submission Goals
-	Sep 25 - Part 2: 3D scenes and user interaction (Ch 2, 3)
    -	Layout the hand designed environment with basic polygons
    -	Implement player movement
    -	Implement game loop for finishing/restarting
-	Oct 16 - Part 3: Polygon meshes (including characters) and materials (Ch 4, 5)
    -	Add meshes and more details to environment
    -	Implement AI pedestrians
-	Dec 2  - Part 4: Physics, special effects, terrains, and sound (Ch 6-9)
    -	Implement speed-ups, wet patches, and pedestrian collisions
    -	Add music and sound effects for slips/crashes/speeding up
    -	Expand the design of the airport
    - Give the pedestrians more advanced control

