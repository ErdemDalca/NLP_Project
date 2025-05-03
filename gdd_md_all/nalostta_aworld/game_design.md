# 3D Multiplayer Game Design Document (Refactored)

## 1. Game Overview
A 3D multiplayer game where players can interact in a shared virtual environment. The game focuses on player interaction, exploration, and dynamic object manipulation.

## 2. Core Mechanics

### 2.1 Player Mechanics

#### 2.1.1 Player Texture
- Player-mesh is a rectangle with randomly assigned color and name label.
- Each browser session spawns a unique player-mesh.
- Users enter a name at session start via a text input. This name floats above the player and follows its position.

#### 2.1.2 Player Movement
- WASD keys for movement
- Q and E keys for camera rotation (anti-clockwise and clockwise)
- Space for jumping, Shift for sprinting, C for crouching
- Physics-based movement: gravity, smooth acceleration/deceleration
- Movement direction dynamically updates with camera rotation
- Prevent overlapping via capsule-to-capsule collision detection

#### 2.1.3 Player-Player Interaction
- Players can view each other in real-time
- Unique colors and identifiers for each player
- Server-authoritative model: movement and state validated server-side
- Latency handling via interpolation and client-side prediction

#### 2.1.4 Player Customization
- Players can customize their avatar appearance (e.g., select from preset models, accessories, or colors).
- Customization options are stored per session and broadcast to all clients.

### 2.2 Object Interaction
- Players can interact with objects in the world (pick up, move, place, or delete objects).
- Raycasting is used for object selection; actions are validated and synchronized via the server.
- Object ownership and manipulation rules are enforced to prevent conflicts.

### 2.3 Game Objectives & Progression
- The game supports objectives such as collecting items, reaching zones, or completing cooperative tasks.
- A scoring or achievement system tracks player progress.
- Win/lose conditions or open-ended sandbox modes can be configured.

### 2.4 User Interface (UI)
- HUD elements display player info, score, chat, and notifications.
- In-game chat and player list are accessible at all times.
- Optional minimap and objective tracker for navigation.

### 2.5 Audio/Visual Feedback
- Sound effects for actions (movement, interaction, events).
- Background music and ambient sounds enhance immersion.
- Visual feedback (particle effects, highlights) for important events.

### 2.6 Networking/Session Management
- Handles player disconnects/reconnects gracefully.
- Prevents duplicate player names; basic authentication for persistent identity.
- Session persistence for returning players.

### 2.7 Security/Anti-Cheat
- All game actions are validated server-side.
- Anti-cheat checks and rate limiting are enforced.
- Regular audits for suspicious behavior.

### 2.8 Performance/Scalability
- Optimized for large player counts using spatial partitioning.
- State updates are sent only to relevant clients to reduce bandwidth.

### 2.9 Accessibility & Platform Support
- Colorblind modes, key remapping, and readable fonts are available.
- UI is responsive and supports both desktop and mobile/touch controls.
- Accessibility settings can be adjusted in-game.

### 2.10 Environment
- 3D world with ground plane
  - Green color ground with semi-transparent square grid
- Grid system aids navigation
- Collision detection with ground and objects
- Object physics managed via bounding boxes or Cannon.js (future extension)

### 2.11 Camera Dynamics
- Camera follows player, attached per browser session
- Controlled using Q/E keys
- Maintains smooth relative position during rotation
- Camera affects forward direction vector for movement

### 2.12 Keyboard Dynamics
- Controls activated only after name entry and start button click
- WASD movement relative to camera
- Q/E for camera rotation
- Session-level keyboard control for multi-tab safety
- Debounced input events to prevent rapid fire issues
- The keyboard controls are bound to the active broswer session and thus the player-mesh of the active broswer session is controlled.

### 2.13 Game Start
- Initial screen includes name input field and "Start Game" button
- Pressing enter or clicking the button transitions to the game view

## 3. Technical Specifications

### 3.1 Frontend
- Three.js for 3D rendering
- Socket.IO for real-time bi-directional communication
- ES6+ JavaScript
- Responsive design for varied screen sizes
- `requestAnimationFrame` used for all animation/game loops

### 3.2 Backend
- Python Flask server (optionally upgrade to FastAPI for async handling)
- WebSocket support via Socket.IO
- JSON-based communication
- Modular code with separation for auth, game logic, object handling

### 3.3 Data Structure

```javascript
// Player Object
{
    id: string,             // Server-assigned UUID
    position: { x, y, z },  // 3D position
    color: string,
    mesh: THREE.Mesh
}

// Custom Object
{
    id: string,             // Server-assigned UUID
    type: string,           // box | cylinder | sphere
    position: { x, y, z },
    dimensions: { width, height, depth },
    texture: string
}
