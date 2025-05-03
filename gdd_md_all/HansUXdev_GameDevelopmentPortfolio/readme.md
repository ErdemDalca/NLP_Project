# Ouroboros



# Game Design Document (GDD)

## Game Title: Ouroboros

### Overview
Ouroboros is a multiplayer snake game where players control their snakes to outmaneuver opponents in a strategic arena. The objective is to block enemies from reaching their base, circle around the enemy, or attack from behind to consume their segments. The game combines classic snake mechanics with competitive multiplayer features, encouraging tactical gameplay and cooperation.

### Game Mechanics

- **Movement**: Players control their snakes using the W, A, S, D keys.
- **Actions**: The Space button allows players to disconnect one unit of their snake, creating a block that can hinder enemy movement.
- **Win Conditions**:
  - Block the opponent from crossing to their base.
  - Successfully encircle the opponent’s base.
  - Attack the opponent’s rear and consume their snake segments.

### Multiplayer Features

- Players can connect to a server via IP address or host locally.
- Real-time updates ensure low latency gameplay.
- Players can interact by blocking each other’s paths or using strategic maneuvers to outplay opponents.
- Spectator mode allows players to watch ongoing matches.

### Characters and Power-ups

- **Characters**: Each player’s snake is visually distinct with customizable colors.
- **Power-ups**:
  - **Speed Boost**: Temporarily increases snake speed.
  - **Shield**: Protects the snake from being eaten for a short duration.
  - **Obstacle Spawn**: Create temporary walls that block movement.

### Unique Features

- **Dynamic Arena**: Randomly generated obstacles and environments in each match.
- **Night Mode**: Different visual theme with glowing snakes and luminescent power-ups.

---

# Technical Design Document (TDD)

## Architecture

- **Client-Server Model**: The game uses a lightweight server to handle connections, game state updates, and player interactions.
  - **Client**: Each player connects via a web browser or a dedicated application.
  - **Server**: Handles game logic, synchronizes state across clients, and manages player connections.

## Technology Stack

- **Frontend**:
  - **Framework**: Pygame for local development, with potential integration into a web-based platform using WebSockets for multiplayer.
  - **Languages**: Python for server-side logic; HTML/CSS/JavaScript for web interface.
  
- **Backend**:
  - **Server**: Flask or FastAPI for handling connections and game logic.
  - **Database**: SQLite for storing player statistics and game history.

## Data Structure

- **Game State**:
  - `players`: List of player objects with attributes (position, length, direction, and active status).
  - `powerups`: List of active power-ups with coordinates and type.
  - `arena`: Grid-based representation of the game field, including obstacles.

- **Player Information**:
  - `player_id`: Unique identifier for each player.
  - `snake_length`: Number of segments in the snake.
  - `score`: Current score based on actions and achievements.

---

# User Experience (UX) Document

## Wireframes

- **Main Menu**: Options for "Start Game," "Instructions," and "Settings."
- **Gameplay Screen**: Displays the arena, player snakes, score, and available power-ups.
- **Scoreboard**: Shows player rankings and current scores post-game.

## User Flow

1. Player starts the game from the main menu.
2. Joins a match or hosts a new game.
3. In-game, player controls the snake, using visual cues for movement and action.
4. Post-game, players return to the scoreboard to view results.

## Accessibility Considerations

- High-contrast colors for better visibility.
- Audio cues for important game events (e.g., power-up pickups).
- Key remapping options for player controls to accommodate different preferences.

## Design Principles

- Intuitive navigation with clear labels and buttons.
- Feedback mechanisms (visual and auditory) for player actions to enhance engagement.
- Responsive design to ensure functionality on various devices.




```plaintext
Ouroboros/
│
├── README.md                  # Project overview and instructions
├── game/
│   ├── __init__.py            # Package initialization
│   ├── main.py                # Main game loop and entry point
│   ├── snake.py               # Snake class and logic
│   ├── server.py              # Server setup and game state management
│   ├── client.py              # Client connection and rendering logic
│   ├── powerups.py            # Power-up definitions and behavior
│   └── arena.py               # Arena setup and obstacle generation
│
├── assets/
│   ├── sprites/               # 8-bit sprites and SVGs
│   │   ├── snake.svg          # Snake sprite
│   │   ├── food.svg           # Food sprite
│   │   ├── block.svg          # Block sprite (disconnected unit)
│   │   └── powerups/          # Power-up sprites
│   │       ├── speed_boost.svg # Speed Boost sprite
│   │       └── shield.svg      # Shield sprite
│   └── sounds/                # Sound effects and music
│       ├── pickup.wav         # Power-up pickup sound
│       └── background.mp3      # Background music
│
├── docs/
│   ├── GDD.md                 # Game Design Document
│   ├── TDD.md                 # Technical Design Document
│   └── UX.md                  # User Experience Document
│
├── tests/
│   ├── test_snake.py          # Unit tests for snake logic
│   ├── test_server.py         # Unit tests for server interactions
│   └── test_powerups.py       # Unit tests for power-ups
│
└── requirements.txt           # Dependencies and libraries



