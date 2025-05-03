Game Design Document (GDD) for Maze Game🧑‍💻:
________________________________________
1. Game Overview
Game Title: Maze Challenge
Genre: Puzzle / Survival
Platform: PC (Unity-based)
Target Audience: Casual gamers, AI enthusiasts, and players interested in experimental AI-generated content.
Game Objective:
•	Navigate a 3D maze.
•	Collect treasures while avoiding the enemy.
•	The game ends when the player is caught by the enemy or collects the treasure.
________________________________________
2. Gameplay Mechanics
Player Character:
•	Camera Player (PlayerFollowCamera):
The player controls the game from a dynamic camera perspective. Movement is tracked as the camera navigates the maze.
Game Actions:
•	Move: Explore the maze using WASD or arrow keys.
•	Collect Treasures: Touch a treasure object to win.
•	Avoid Enemy: Navigate around the maze to avoid contact with the enemy.
Win/Loss Conditions:
•	Win: Collect the treasure before being caught by the enemy.
•	Loss: The game ends if the enemy catches the player.
________________________________________
3. Features
Maze Design:
•	The maze consists of wooden-textured walls arranged in a grid-like format. The layout was manually designed in Unity (as shown ).
Enemies:
•	Enemy Sprite: Created using Hugging Face's Muse Sprite.
•	Behaves as a 2D sprite that patrols sections of the maze.
Treasures:
•	Simple treasure objects scattered in the maze.
•	The game ends upon interaction.
Sound and Music:
1.	Background Music:
o	Created using Udio, a generative AI model. The music loops during gameplay, creating an immersive atmosphere.
2.	Intro Sound Effect:
o	Generated using MusicGen on Hugging Face Spaces. A 15-second audio file with a textual prompt describing the game (“player in the maze moves, collects treasures while avoiding enemy”). The sound plays once at the start of the game.
________________________________________
4. AI Integration
AI Tools Used:
1.	Muse Chat: Assisted in generating the maze structure and logic.
2.	Muse Sprite: Generated the 2D enemy character.
3.	Udio: Generated dynamic background music.
4.	MusicGen: Produced the 15-second introductory sound cue.
________________________________________
5. Art Style
•	Maze: 3D wooden textures applied to Unity cubes.
•	Enemy: 2D sprite integrated into the 3D world, providing a unique aesthetic.
•	Treasures: Basic 3D models with shiny textures.
________________________________________
6. Technical Specifications
•	Engine: Unity 2022.3
•	Assets:
o	Maze: Cubes arranged in Unity.
o	Enemy: Generated using Muse Sprite.
o	Music: Created via Udio and MusicGen.
________________________________________
7. User Interface (UI)
Game Screen:
•	Displays the maze from the PlayerFollowCamera’s perspective.
•	Basic HUD showing the player’s status (e.g., "Collect the treasure!" or "Avoid the enemy!").
________________________________________
8. Development Plan
1.	Prototype:
o	Complete the maze design and implement basic player movement.
2.	AI Assets:
o	Integrate assets from Muse Sprite, Udio, and MusicGen.
3.	Game Logic:
o	Program win/loss conditions based on treasure collection and enemy collision.
4.	Polish:
o	Add sound effects and adjust the difficulty of the enemy’s patrol pattern.
________________________________________
9. Future Enhancements
•	Add multiple levels with increasing difficulty.
•	Introduce more treasures and varying enemy behaviors.
•	Implement a leaderboard to encourage competition among players.
________________________________________
10. Credits
•	Developer: MAHDI ABUNEMER 
•	AI Assistance: Hugging Face Spaces (Muse Chat, Muse Sprite, Udio, MusicGen)
•	Engine: Unity



https://github.com/user-attachments/assets/e607f9ba-5866-4e7e-8ff3-31bafb1963f6

