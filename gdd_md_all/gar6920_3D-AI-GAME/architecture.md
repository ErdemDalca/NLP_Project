# 3D AI Game Platform - Architecture

## Overview
3D AI Game is a modular 3D web-based game platform built with Three.js and Colyseus, utilizing a client-server architecture for multiplayer functionality. Players control customizable characters and interact with a colorful 3D environment. The platform is designed to support various game implementations.

## Core Components

### 1. Server (server/core/server.js)
**Technology:** Built with Node.js and Colyseus.

**Responsibilities:**
- Manages game rooms and player connections/disconnections
- Maintains the authoritative game state (including position, rotation, and current animation)
- Processes player inputs (e.g., movement keys, mouse look for rotation)
- Broadcasts state updates to all connected clients
- Handles entity spawning and lifecycle management
- Statically loads the 'default' implementation.
- Validates and manages structure placement in the building system
- Handles RTS movement commands by setting target positions
- Determines appropriate animation state based on player input/status

**Key Features:**
- Room-based multiplayer with session persistence
- State synchronization using Colyseus schema
- Server-authoritative position and rotation tracking
- Server-determined animation state synchronization
- Dynamic entity spawning system
- Statically loads the 'default' implementation.
- Server-validated building placement system

### 2. Client Core Platform (/client/js/core)
The core platform provides foundational functionality that all game implementations can leverage.

**Key components:**
- **main.js:**
  - Entry point for client-side code
  - Loads core modules and initializes the game engine
  - Sets up default player factory and loads the 'default' implementation.

- **controls.js:**
  - Handles player input (keyboard/mouse), manages different camera control schemes (PointerLock, Orbit, FreeCam, RTS panning/zoom).
  - Supports first-person, third person, free roam, and RTS view modes
  - Manages input handling for keyboard and mouse
  - Sends calculated rotation values to the server for player rotation.
  - Implements quaternion-based rotation for smooth local camera movement.
  - Applies direct rotation to player mesh for immediate visual feedback.
  - Distinguishes between rotation controls through mouse movement and keyboard (Q/E keys).
  - Run is default movement, Shift activates walking.

- **game-engine.js:**
  - Initializes the Three.js scene, renderer, and camera
  - Sets up player controls and world objects
  - Manages the animation loop for continuous rendering
  - Implements four distinct camera systems:
    - First-person view: Camera attached to player's head position, local rotation responds immediately to mouse.
    - Third-person view: Camera follows behind player with orbiting controls.
    - Free camera mode: Independent camera with WASD/QE movement and mouse look functionality.
    - RTS view mode: Top-down strategic view with panning, zoom, selection, and move commands.
  - Handles smooth camera transitions between view modes
  - Applies server-authoritative position to player meshes.
  - Provides proper orientation for the camera without affecting model rotation.
  - Calls player animation update logic.
  - Suppresses player movement/animation logic when in Free Camera or RTS modes.

- **network-core.js:**
  - Establishes and maintains WebSocket connection to the server via Colyseus
  - Sends player input state (keys, rotation, viewMode) to the server
  - Processes state updates from the server
  - Creates/updates/removes visual representations of remote players based on server state.
  - Applies server-sent animation state (`currentAnimation`) to remote player models.
  - Handles player joining/leaving events
  - Manages Colyseus connection, state synchronization, player join/leave, entity creation/updates based on server state. Handles remote player interpolation.

- **Entity.js:**
  - Base class for all game entities
  - Provides core entity functionality (position, rotation, scale)
  - Defines interface for entity behaviors
  - Handles common entity lifecycle events

- **Player.js:**
  - Extends Entity for player-specific functionality
  - Manages player state and input handling (primarily for remote players, local player uses controls.js)
  - Provides interface for implementation-specific player behaviors (e.g., DefaultPlayer loading GLB model)

- **NPC.js:**
  - Extends Entity for non-player characters
  - Implements basic AI behaviors
  - Provides interface for implementation-specific NPC behaviors

- **EntityFactory.js:**
  - Factory pattern for creating entities
  - Registers entity types and their constructors
  - Used by both core platform and game implementations

- **collision.js:**
  - Handles collision detection and resolution
  - Provides interfaces for implementation-specific collision behaviors
  - Basic AABB collision detection system (primarily client-side checks for immediate feedback, server is authoritative).

- **player-ui.js:**
  - Manages common UI elements for player information
  - Provides hooks for implementation-specific UI components

### 3. Game Implementations (/client/js/implementations and /server/implementations)
Each game implementation extends the core platform with specific gameplay mechanics and visuals.

**Implementation Structure:**
- Client-side implementation code in /client/js/implementations/default/ (currently only 'default' exists)
- Server-side implementation code in /server/implementations/default/ (currently only 'default' exists)
- The 'default' implementation uses a GLB model for the player character (`DefaultPlayer.js`) and includes functionality for RTS and Building modes.

**Key implementation components:**
- **DefaultPlayer.js:**
  - Uses a container/model relationship for proper rotation handling
  - Creates a container Group that serves as the mesh for rotation
  - Contains the actual model (human_man.glb) within this container
  - Applies a 180° rotation to the model to align its forward direction with the camera
  - Handles mesh visibility based on camera mode
  - Implements animation state updates based on player inputs
  - Distinguishes between local and remote player rotation handling

**Future Implementations:**
- Would follow similar patterns, extending the core components
- Each implementation will be contained in its own directory
- Will register custom entity factories and behaviors

### 4. Main Engine (game-engine.js)
- Initializes the Three.js scene, renderer, and camera
- Sets up player controls and world objects
- Loads the 'default' game implementation.
- Manages view modes (first-person, third-person, free roam, RTS view)
- Updates visual components based on server state
- Handles synchronization between player rotation and camera orientation

### 5. Networking Architecture
**Technology:** Colyseus for WebSocket-based real-time multiplayer.

**Implementation:**
- Server maintains authoritative game state using Colyseus Schema
- Player state includes position, velocity, pitch, rotationY, input state, currentAnimation.
- Client sends input state (including current rotation values) via `updateInput` message.
- Server calculates movement, rotation, and animation state based on input.
- Server applies direct rotation from client when provided.
- Server broadcasts delta updates.
- Client interpolates remote player positions and applies server rotation/animation state.

**Key Features:**
- Session persistence with reconnection support
- Room-based multiplayer with shared state
- Message-based communication for game events
- Schema-based state synchronization with type annotations
- Player list UI showing all connected players
- Automatic remote player creation and cleanup
- Smooth remote player movement interpolation
- Proper handling of player value updates and mesh recreation
- Resilient error handling for network disconnections
- Automatic cleanup of stale player instances

**Schema Implementation:**
- `GameState`: Holds maps for `players`, `entities`, `structures`.
- `Player`: Extends `BaseEntity`, includes `input` (InputState), `currentAnimation`, `pitch`, `rotationY`, `velocityY` etc.
- `InputState`: Holds `keys`, `mouseDelta.y`, `clientRotation`, `viewMode`.

**Player Synchronization:**
- Automatic creation of remote player instances with proper sessionId tracking
- Smooth position interpolation using Three.js lerping
- Proper cleanup of disconnected player instances
- Value-based mesh updates
- Efficient player collection management using Set data structure
- Proper separation of local and remote player handling
- Resilient error handling for edge cases
- Different rotation handling for local vs remote players

### 6. Building System
**Technology:** Three.js for rendering, Colyseus for server-side validation and synchronization.

**Implementation:**
- Server-authoritative structure placement system 
- Client-side preview with real-time validation feedback
- Built on Colyseus Schema for synchronized structure collections
- Toggle between game and building modes with keystroke (B key)
- Grid-based placement with 15° rotation increments (Q/E keys)
- Seamless operation across all camera modes

**Client Components:**
- Building mode UI overlay with structure selection menu
- Structure preview mesh with valid/invalid placement indicators
- Click-to-place functionality with server authorization
- Structure rotation controls (Q/E for 15° increments)
- Cross-camera mode compatibility (first-person, third-person, RTS)
- Interactive grid system for structure placement

**Server Components:**
- Structure schema extending BaseEntity
- Structure collection in GameState
- Server-side collision detection and validation
- Server broadcasting of structure changes to all clients
- Authoritative structure placement confirmation

**Structure Types:**
- Buildings: Base structures with customizable dimensions
- Walls: Thin structures with height/width customization
- Additional types can be added by extending the Structure schema

**Networking Flow:**
1. Client enters building mode and selects structure type
2. Client shows preview mesh at mouse pointer location
3. Client validates placement and shows green/red indicator
4. Client sends placement request to server on valid click
5. Server validates placement and checks for collisions
6. Server creates structure and broadcasts to all clients
7. All clients render the confirmed structure

**Key Features:**
- Complete cross-client synchronization of structures
- Real-time placement validation with visual feedback
- Seamless integration with all camera modes
- Full server authority for all structure placement
- Interactive preview system with structural rotation
- Grid-based placement with customizable sizing

## Project Structure (Simplified View)

```
/
├── client/                 # Client-side code
│   ├── css/
│   ├── js/
│   │   ├── core/           # Core client platform components (game-engine, controls, network, etc.)
│   │   ├── implementations/
│   │   │   └── default/    # Default game implementation (e.g., DefaultPlayer.js)
│   │   └── lib/            # Additional JavaScript utilities
│   ├── assets/             # Game assets (textures, etc.)
│   │   └── models/         # 3D model assets (GLB files)
│   │       └── human_man.glb # Player character model
│   ├── models/             # Additional model assets
│   └── index.html          # Main game HTML
├── server/                 # Server-side code
│   ├── core/               # Core server platform components (BaseRoom, schemas, etc.)
│   │   ├── index.js        # Server setup and Colyseus integration
│   │   ├── BaseRoom.js     # Base room implementation with player movement logic
│   │   └── schemas/        # Colyseus schemas (GameState, Player, etc.)
│   └── implementations/
│       └── default/        # Default server implementation (DefaultRoom.js)
├── public/                 # Public assets
├── memory bank/            # Documentation (like this file)
├── node_modules/           # npm dependencies
├── package.json            # Project dependencies
├── package-lock.json       # Lock file for dependencies
├── start_game.bat          # Windows startup script with dependency check
├── start_server.bat        # Server startup script
├── update_compiled_code.bat # Utility script
└── README.md               # Project readme
```

## Data Flow

1.  **Initial Connection**: Client browser navigates to the root URL (`/`).
2.  **Redirect**: Server receives request for `/`, executes `res.redirect('/select')`.
3.  **Selection Page**: Client browser requests `/select`. Server serves `public/player_select.html`.
4.  **Player Choice**: User clicks a button on the selection page.
    *   **1 Player**: Browser navigates to `/game`.
    *   **2-4 Players**: Browser navigates to `/setup?players=N`.
5.  **Game Page Load**: 
    *   If `/game` was requested, server serves `client/index.html`.
    *   If `/setup` was requested, server serves `four_player_setup.html`, which then loads `/game` in iframes.
6.  **Client Initialization**: `client/index.html` loads necessary JS (`main.js`).
7.  **Server Connection**: Client connects to Server via WebSocket (Colyseus `network-core.js`).
8.  **Join Room**: Client joins the 'active' room (`DefaultRoom.js`).
9.  **State Sync**: Server sends initial `GameState` to Client. Player entities are created client-side (`network-core.js` using `EntityFactory`).
10. **Input**: Client sends input state (keys pressed, mouse movement, rotation) to Server (`controls.js` -> `network-core.js` -> `BaseRoom.js`).
11. **Server Processing**: Server updates player state based on input, performs physics/collision checks (`BaseRoom.js` or `DefaultRoom.js`).
12. **State Broadcast**: Server broadcasts delta updates of the `GameState` to all clients.
13. **Client Update**: Client receives state updates, interpolates remote player positions, updates local visuals (`network-core.js`).
14. **Building**:
    *   Client enters build mode, sends placement request (`game-engine.js` -> `network-core.js`).
    *   Server validates, updates `GameState.structures`, broadcasts change (`BaseRoom.js`).
    *   Clients render the new structure (`network-core.js`).
15. **RTS Commands**:
    *   Client selects units, issues move command (`game-engine.js`/`rts-view.js` -> `network-core.js`).
    *   Server receives command, updates target position for player entities (`BaseRoom.js`).
    *   Server state updates cause units to move on all clients.

## Player Model & Rotation System

The player model system uses several key architecture components working together:

1. **Model Structure:**
   - `DefaultPlayer.js` creates a hierarchical structure:
     - A THREE.Group container (`this.mesh`) handles overall rotation
     - The actual model (`human_man.glb`) is a child of this container
     - The model itself is rotated 180° to align its forward direction with the camera

2. **Rotation Handling:**
   - For local player:
     - Mouse movement and Q/E keys directly update `playerRotationY` and mesh rotation
     - Camera views are properly aligned with mesh rotation
     - Rotation values are sent to server via `clientRotation` in input updates
   - For remote players:
     - Server state `rotationY` is used to determine target rotation
     - Smooth interpolation is applied for natural movement
     - Distinct handling prevents rotation conflicts

3. **Camera View Coordination:**
   - First-person: Camera uses player rotation without additional Math.PI offset
   - Third-person: Camera orbits player position based on player rotation
   - Both camera systems respect the proper model orientation

4. **Dual Control Mechanisms:**
   - Mouse movement directly updates rotation for precise control
   - Q/E keyboard controls provide incremental rotation with visual feedback

## Notes & Discrepancies from Code Review (Commit abdc192)

- The actual default player implementation uses a GLB model (`human_man.glb`), not simple cubes as described in the Game Design Document.
- The RTS view mode and Building system are implemented (`game-engine.js`, `BaseRoom.js`, schemas) but might not be fully documented outside this architecture file.
- Dynamic server-side implementation loading (based on arguments/env vars) is mentioned in previous versions of this doc but is *not* currently implemented in `server/core/index.js`. It statically loads the 'default' implementation.
- The specific "Numberblocks" game features described in project memories are *not* part of this codebase version; this version contains the core platform and a generic 'default' implementation.

## Notes & Current State

- Player model (`human_man.glb`) loading and basic movement animations (Idle, Walk, Run, Jump, Strafe) are functional.
- Animation state is synchronized between server and clients.
- Run/Walk inversion (Run default, Shift=Walk) is implemented.
- View modes (FPS, TPS, FreeCam, RTS) function, and player input/animations are correctly suppressed in non-player-control modes.
- Startup script (`start_game.bat`) includes dependency checking (`npm ci`).
- Player rotation system now correctly handles both local and remote player rotations with proper model orientation.
- Model directionality aligns with camera views through a container/model hierarchy system.