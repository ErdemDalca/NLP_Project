# Space-Explorer

# Game Design Document: Space Explorer
# 1. Overview:
  Space Explorer is a 2D arcade-style game where the player pilots a spaceship through space, avoiding asteroids, collecting stars, and earning points by shooting down asteroids. The game aims to provide an engaging experience while reinforcing key Unity concepts such as object manipulation, physics, collisions, and scene management.
# 2. Game Elements
# 2.1. Spaceship (Player Object)
Description: A 2D spaceship that the player controls.
Functionality:
Moves in all directions using the arrow keys.
Key D and Next : Helps the spaceship move to the right
Key A and Pre : Helps the spaceship move to the left
Key W and Top: Helps the spaceship move to the top
Key S and Bottom: Helps the spaceship move to the bottom
Shoots missiles to destroy asteroids.
Has a health system represented by three hearts.
# 2.2. Asteroids
Description: Floating 2D asteroids that move randomly across the space environment.
Functionality:
Move randomly within the scene.
The longer the time, the faster asteroids appear.
If the spaceship collides with an asteroid, the player loses one heart.
Can be destroyed by the spaceship’s missiles , earning the player 1 point per asteroid.
# 2.3. Stars
Description: Scattered 2D stars in the game space.
Functionality:
When collected, they add 10 points to the player's score.
# 2.4. Health System (Hearts)
The player starts with three hearts.
Each collision with an asteroid removes one heart.
The game ends when all three hearts are lost.
# 4. Game Flow
# 3.1. Main Menu Scene
Contains the following UI elements:
"Play" Button: Starts the gameplay scene.
"Instructions" Button: Displays a panel with game instructions.
“Quit” Button: You can turn off the game
# 3.2. Gameplay Scene
Features:
The spaceship navigates space while avoiding and destroying asteroids.
Stars appear randomly and can be collected for points.
Score is updated in real-time.
Health is displayed using heart icons.
# Objective:
Survive by avoiding asteroids while collecting stars and shooting asteroids to gain points.
Losing all three hearts results in game over.
# 3.3. End Game Scene
Displays the final score.
Includes options to:
Return to the main menu.
Quit the game.
# 5. Implementation Details
# 4.1. Player Controls
Movement: Arrow keys.
Shooting: Spacebar or left mouse click.
# 4.2. Collision Logic & Scoring
# Asteroids:
Colliding with an asteroid reduces health by one heart.
Destroying an asteroid grants 1 point.
Stars:
Collecting a star grants 10 points.
# 4.3. Scene Transitions
Smooth transitions implemented between the main menu, gameplay, and end game scenes.

