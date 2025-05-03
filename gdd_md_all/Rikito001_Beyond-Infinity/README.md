# **Beyond Infinity - Game Design Document - EN**

The repository contains a prototype implementation of a game in Pygame, which was implemented during an exercise for the Object Technologies course. The created game presented essential game functions and the repository serves as a example for the development of a game intended for the course project.

**Author**: Simon Kováčik

**Chosen theme**: One level, but constantly changing

---
## **1. Introduction**
The proposed game serves as a demonstration for the subject Object Technologies, with the aim of creating a functional prototype of the game as a project for the exam. The created game meets the requirements of the assigned topic (One level, but constantly changing). The game has a player trying to avoid obstacles in an infinite level with 3 possible difficulties.

### **1.1 Inspiration**
<ins>**Geometrydash**</ins>

Geometrydash is a "side-scrolling platforming" multiplatform game which has the player jump over obstacles in multiple levels often created by the fan-base and not just original game developer. The levels are often, if not always, based off fast-paced songs and the obstacles are placed exactly in a way that makes the player jump over them in the beat of given song. The faster the song, the harder and faster is the level, which also requires more skill.

<p align="center">
  <img src="https://github.com/Rikito001/Beyond-Infinity/blob/main/Images/geometrydash.jpg" alt="Geometrydash">
  <br>
  <em>Figure 1 Preview of Geometrydash</em>
</p>

<ins>**Fancade - Gold Rush**</ins>

Gold Rush is one of many minigames in a mobile game called Fancade. Its a fan-made game (Fancade is an app for simple game making and publishing) which includes one level that changes constantly. The player takes control of a ball-like character that jumps between two static walls and with each touch of a wall, spikes appear or change their position on the given wall. The game continues till the player touches one of the spikes or either top or bottom of the vertical tunnel (the two static walls). The player can also collect coins with which upgrades can be bought, such as an extra life or slower speed, giving the player more time to decide his moves. 

<p align="center">
  <img src="https://github.com/Rikito001/Beyond-Infinity/blob/main/Images/GoldRush.jpg" alt="Gold Rush">
  <br>
  <em>Figure 2 Preview of Gold Rush</em>
</p>

### **1.2 Player Experience**
The goal of the game is to gain the highest score in an infinite tunnel with spikes on both top and bottom, while the speed keeps going up by 5% with each 100 points reached. The player can choose from 3 difficulties - easy, medium and hard, with each difficulty having a multiplier on both the player speed and gained score (the higher the difficulty, the higher the reward).

### **1.3 Development Software**
- **Pygame-CE**: chosen programming language.
- **PyCharm 2024.1**: chosen IDE.
- **Photopea**: graphical tool for creating background.
- **Pixabay**: source sounds for the game.

---
## **2. Concept**

### **2.1 Gameplay Overview**
The players character moves up and down, and the goal is not to hit a spike obstacle or the ground. As the player progresses through the infinite level, each 100 points reached adds 5% to the current speed, making it more challenging. Aside from the level becoming harder, the player can choose from 3 difficulties with multiplier on the player speed and gained score - easy (1.0 on speed and 1.0 on score), medium (1.5 on both), hard (1.75 on both). Once a player dies, his highest score will be saved (for each difficulty separately) and it will be displayed in the level itself, allowing the player to compete against themselves.

### **2.2 Theme Interpretation (One level, but constantly changing)**
**"One level, but constantly changing"** - 

### **2.3 Primary Mechanics**
- **Spikes**: there are objects on the map that create an active obstacle for the player.
- **Multiplier**: the difficulty can be chosen directly but also gets higher as the player progresses through the level.
- **High Score**: the player can compete against themselves as they get more skilled over time.

### **2.4 Class design**
- **Game**: class that will contain the main game logic (menu, game loop, game ending, ...).
- **Player**: class representing the player, player control and character rendering.
- **Sprites**: class of enemies (spikes), their game logic and character rendering.
- **Settings**: class that contains basic settings of the game (window size, tunnel (map) size, ...).
- **High Score**: class handling saving and updating highest achieved score.

---
## **3. Art**

### **3.1 Theme Interpretation (One level, but constantly changing)**
Game is focused on a 2D map and objects with simple pixel design. Spikes are simply generated using a function, while the player's character, a spaceship, and it's engines are pixel sprites with simple animations.

<p align="center">
  <img src="https://github.com/Rikito001/Beyond-Infinity/blob/main/Images/PlayerPreview.png" alt="Player">
  <br>
  <em>Figure 3 Preview of player character</em>
</p>

### **3.2 Design**
The game tries to keep a simplistic, slightly retro look. The interface is minimalistic, and while the player is in the game there are stats carefully placed in a way that they still can be checked while avoiding spikes. No assets were used for the spikes and both player and engine effects are from itch.io (https://foozlecc.itch.io/void-main-ship).
<p align="center">
  <img src="https://github.com/Rikito001/Beyond-Infinity/blob/main/Images/LevelPreview.png" alt="Level design">
  <br>
  <em>Figure 4 Level design concept</em>
</p>

---
## **4. Audio**

### **4.1 Music**
The selection of background music was focused on a fast paced pixel-like theme as the game has a retro feel to itself (https://pixabay.com/music/drum-n-bass-pixel-run-206007/). The menu music is a slower and calmer soundtrack that makes sure the player experience starts already in the menu while not being too loud or fast (https://pixabay.com/music/pulses-coffee-with-sugar-background-music-by-alienightmare-237715/)

### **4.2 Sound Efects**
The sounds effects in this game maintain a pixel/8-bit feel and were made using sxfr sound effect maker.

---
## **5. Game Experience**

### **5.1 UI**
The user interface will be oriented towards the overall graphic style and the start screen will include the option to start and exit the game or view the highscore or developer credits.

### **5.2 Controls**
<ins>**Keyboard**</ins>
- **Arrows UP and DOWN**: selection in menu.
- **Space**: player movement up and down.
- **Escape**: return to menu/game exit
