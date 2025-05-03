# Game Design Document (GDD) 



## 1. Game Concept
- **Title**: Accelither
- **Concept**: slither controlled through a DE10 lite fpga with possible extra functionality enabled through this

## 2. Gameplay
- **Objective**:
  - Grow as large as possible
  - Achieve the highscore on the leaderboard
  - Eliminate as many players as possible
- **Mechanics**:
  - Snake moving in 2d game plane
  - Snake can accelerate
  - If a snake hits another snakes body it dies
  - Snakes picks up food and grows
- **Controls**:
  - x,y coordinates recieved from accelerometer for control in the 2d game plane
  - Hold down button to accelerate/decelerate
  - switches control HUD
- **Level**:
  -  Single level with defined game arena 

## 3. Story and Setting
- **Narrative**:
  - Snakes want to grow big.
- **World**:
  - Sci-fi 
 

## 4. Art and Aesthetics
- **Visual Style**:
  - Sci-fi aesthetic
- **Characters**:
  - Simple 2d art of snakes
  - randomly start with one
  - snakes scales are the complement colour of their body which is calculated from the majority colour of their head
- **UI/UX Design**:
  - Very minimal and small
  - Current score
  - Current position in the size leaderboard
  - Number of enimies killed

## 5. Sound and Music
- **Sound Effects**:
  - Sound played through laptop when you die 
  - Sound for eating food
  - sound for gameover screen
- **Music**:
  - intro music and ingame playlist that is randomly shuffled

## 6. Multiplayer
- **Network Play**:
  - Competitive survival, can eliminate other players
- **Server Architecture**:
  - fpga->client->server->client where most processing and game logic is done on the server
  - Connecting over tcp from server to multiple client concurrently
- **Matchmaking and Lobbies**:
  - One server hosts a game instance

## 7. Technology
- **Engine**:
  - pygame :)
- **Platforms**:
  - Strictly downloadable executable linked to via webpage / download from github
- **FPGA Integration**: 
  -  FPGA data streams accelerometer data through client straight to the server for processing

## 8. Development and Production
- **Timeline**:
  - Major milestones [Timeline](./Timeline.md)
- **Task Tracker**:
  - List of roles/responsibilities, emptied as tasks were taken. [Role Allocation](./RoleAllocation.md)
