# Game Design Document: AI Bot Arena

**Version:** 1.0
**Date:** 2025-04-06

## Project Goal

Create a browser-based **2D top-down** game using **HTML5 Canvas** where users can code the AI of triangular robot ships (tanks) in **JavaScript** and watch them battle in a fixed arena. Each ship will have an independently rotating turret, a scanner with visual indication, a weapon firing **projectiles**, heat, armor, and the ability to use "overburn." Users will define **JavaScript AI code** for each ship in a setup stage, add or remove bots, and can also manually control one ship via the keyboard. Movement and collisions will be handled **kinematically without a physics engine**.

## Core Technologies

* **Frontend:** HTML, CSS, JavaScript
* **Rendering:** **HTML5 Canvas 2D API**
* **AI Scripting:** **JavaScript** (User-provided code executed in a sandboxed environment)
* **Optional: Syntax Highlighting:** Ace Editor, Monaco Editor, or CodeMirror (Configured for JavaScript).

## Key Decisions Made

* **Rendering Engine:** HTML5 Canvas 2D
* **Physics Engine:** None (Kinematic movement, manual collision detection)
* **AI Scripting Language:** JavaScript
* **Weapon Type:** Projectiles
* **Overheating Consequence:** Temporary Shutdown
* **Coordinate System:** 2D Cartesian (X horizontal, Y vertical), Origin Top-Left recommended.

## General Principles

* **Coordinate System:** 2D Cartesian. **Recommendation:** Origin (0,0) at the top-left corner of the canvas. X increases to the right, Y increases downwards. Angles measured in **radians** (standard for `Math.sin`/`cos` and Canvas rotation), potentially 0 radians pointing right (East), increasing counter-clockwise, or 0 radians pointing up (North) increasing clockwise (choose one and be consistent). Degrees can be used for API input/output but converted internally.
* **Units:**
    * Distance: Pixels.
    * Angles: Radians (internally), Degrees (optionally for user API).
    * Time: **Seconds**. Use delta time (`dt` - time since last frame in seconds).
* **Frame Rate Independence:** All time-based actions (movement, rotation, heat changes, cooldowns, projectile movement) **must** use `dt`.

## 1. Project Setup and Core Structure

* Create a basic HTML file with a `<canvas>` element. Include CSS for basic layout. Link necessary libraries (Syntax Highlighter).
* Establish a clear JavaScript module structure (e.g., `main.js`, `game.js`, `renderer.js`, `bot.js`, `projectile.js`, `collision.js`, `ai_interface.js`, `ai_manager.js`, `ui.js`). `collision.js` will handle manual collision detection logic.
* Implement a core game loop (`requestAnimationFrame`) handling initialization, state updates (AI, movement, collisions), and rendering.
* Implement robust delta time (`dt`) calculation.

## 2. Game World and Arena

* **Canvas Element:** The `<canvas>` element defines the viewable game area.
* **Dimensions:** Define `ARENA_WIDTH` and `ARENA_HEIGHT` in pixels (matching canvas size). These define the boundaries for movement and collisions.
* **Background:** Draw a simple background color or texture on the canvas each frame.
* **Initial Bot Placement:** Place bots at random `(x, y)` coordinates within the arena boundaries, ensuring minimum separation distance (based on `ship_radius`).

## 3. Ship (Bot) Design

* **2D Visuals:** Bots drawn as 2D shapes (e.g., filled triangles) using Canvas API. Turret drawn as another shape (e.g., rectangle or line) on top.
* **Visual Distinction:** Use `color` property for `fillStyle` or `strokeStyle` when drawing.
* **Bot Object Properties:**
    * `id`: Unique identifier.
    * `name`: User-defined string.
    * `color`: String (CSS color value).
    * **`x`**: Current X position (pixels).
    * **`y`**: Current Y position (pixels).
    * **`angle`**: Current ship body orientation (radians).
    * **`turret_angle`**: Current turret orientation (radians, potentially relative to ship `angle` or absolute world angle - define this).
    * **`velocityX`**: Current velocity component along X axis (pixels/sec).
    * **`velocityY`**: Current velocity component along Y axis (pixels/sec).
    * **`target_speed`**: The speed the bot is trying to reach (pixels/sec).
    * **`current_speed`**: Magnitude of current velocity (calculated from `velocityX`, `velocityY`).
    * **`target_angle`**: The absolute angle the ship body is trying to face (radians).
    * **`target_turret_angle`**: The absolute angle the turret is trying to face (radians).
    * `armor`, `max_armor` (float)
    * `heat`, `max_heat` (float)
    * `max_ship_rotation_speed`: Max rotational speed (radians per **second**).
    * `max_turret_rotation_speed`: Max rotational speed (radians per **second**).
    * `max_speed`: Max linear speed (pixels per **second**).
    * `acceleration`: Rate of speed increase (pixels per second²).
    * `braking_power`: Rate of speed decrease when braking (pixels per second²). Also need passive deceleration/friction.
    * `heat_generation_fire`, `heat_generation_overburn`, `heat_dissipation_rate` (floats)
    * `ship_radius`: Radius for collision detection (pixels).
    * `fire_power`: Damage per projectile hit (float).
    * `fire_cooldown`: Min time between shots (seconds).
    * `overburn_speed_multiplier`, `overburn_fire_power_multiplier`, `overburn_heat_generation_multiplier` (floats)
    * `scan_range`: Max scan distance (pixels).
    * `scan_arc_degrees`: Scan cone width (degrees - convert to radians for drawing/checks).
    * `scan_cooldown`: Scan recharge time (seconds).
    * `projectile_speed`: Speed of projectiles (pixels per **second**).
    * `projectile_lifetime`: Max projectile duration (seconds).
    * `projectile_radius`: Radius for projectile collision (pixels).
    * `explosion_radius`, `explosion_damage` (pixels, float). Define falloff.
    * `aiScript`: String containing user JavaScript code.
    * `isShutdown`: Boolean flag.
    * `memory`: Persistent object for AI state.

## 4. Kinematic Movement and Manual Collisions

* **Movement Update (per frame, using `dt`):**
    * **Rotation:** Gradually adjust `bot.angle` towards `bot.target_angle` at `max_ship_rotation_speed * dt`. Implement shortest angle logic. Do similarly for `bot.turret_angle`.
    * **Acceleration/Deceleration:** Calculate the difference between `target_speed` and `current_speed`. Apply `acceleration` or `braking_power` (using `dt`) to adjust `current_speed`, clamping at 0 and `max_speed` (adjusted by overburn). Introduce passive friction (slight speed decrease over time if not thrusting).
    * **Velocity:** Update `velocityX = Math.cos(bot.angle) * current_speed` and `velocityY = Math.sin(bot.angle) * current_speed`.
    * **Position:** Update `x += velocityX * dt` and `y += velocityY * dt`.
* **Boundary Checks:** After updating position, check if `x` or `y` (plus/minus `ship_radius`) are outside `ARENA_WIDTH`/`ARENA_HEIGHT`.
    * **Response:** Simplest: Stop movement at boundary. Better: Clamp position to boundary and potentially zero out the velocity component towards the wall. Optional: Apply damage on high-speed wall collision.
* **Collision Detection (`collision.js`, per frame):**
    * **Bot-Bot:** Iterate through all pairs of bots. Calculate distance between centers (`Math.sqrt((x1-x2)^2 + (y1-y2)^2)`). If `distance < bot1.radius + bot2.radius`, a collision occurred.
    * **Bot-Projectile:** Iterate through bots and projectiles. Calculate distance. If `distance < bot.radius + projectile.radius` (and projectile owner !== bot), a collision occurred.
* **Collision Response:**
    * **Bot-Bot:** Simplest: Prevent overlap by slightly moving bots apart along the collision axis. Optional: Apply damage based on relative velocity at impact. Optional: More complex response like conserving momentum (requires mass property).
    * **Bot-Projectile:** Apply damage to bot, destroy projectile.

## 5. Ship AI (JavaScript Integration)

* **AI Code Format:** User provides JS string defining `runBotAI(botInfo, api, memory)`.
* **AI Interface (`api` object):** Pass functions to the AI:
    * `api.thrust(amount)`: Sets `target_speed` (0 to 1.0 scale of `max_speed`).
    * `api.brake()`: Sets `target_speed` to 0.
    * `api.turn(target_angle_degrees)`: Sets `target_angle` (convert degrees to radians).
    * `api.turn_turret(target_angle_degrees)`: Sets `target_turret_angle` (convert degrees to radians).
    * `api.scan(relative_angle_degrees, arc_degrees) -> scanId | null`: Initiates scan. Angle relative to turret? Check enemies within range/arc manually. Store results associated with `scanId`.
    * `api.fire() -> bool`: Attempts to fire projectile. Checks cooldown/shutdown.
    * `api.overburn(enable)`
    * `api.getScanResults(scanId) -> Array<EnemyInfo> | null`: Retrieve results of finished scan. Need manual implementation to find bots within scan cone at time of scan completion.
* **`botInfo` Object:** Passed to `runBotAI`. Contains read-only state: `x`, `y`, `angle`, `turret_angle`, `current_speed`, `armor`, `heat`, `max_armor`, `max_heat`, cooldowns, `isShutdown`, etc.
* **AI Execution Model (`ai_manager.js`):**
    * **Sandboxing (Web Workers Recommended):** Execute user `runBotAI` function safely. Main thread sends `botInfo`/`memory`, worker executes AI, worker sends API calls back via `postMessage`. Main thread applies API call effects (setting targets, initiating fire/scan). Update `memory`.
    * **Frequency:** Execute AI per bot each game tick or fixed interval.
    * **Time Limits & Error Handling:** Enforce execution time limits within worker. Catch errors. Log issues, display "AI Error" status, stop AI execution for faulty bots.

## 6. User Interface (UI) - Two-Stage Process

* **Stage 1: Setup Screen:** Add/Remove bots. List bots with editable Name, Color Picker, **JavaScript code Text Area** (JS syntax highlighting), Load/Save **JS Script**. Optional: Customize properties. "**Start Game**".
* **Stage 2: Game Screen:**
    * **Main View:** The `<canvas>` element where the game is drawn.
    * **Side Panel / Status Display:** (Separate HTML overlay) List bots. For each: Name, ID, Color, Armor Bar, Heat Bar, Status Indicators (**"Shutdown"**, "Overburn", "AI Error", "Destroyed").
    * **Game Controls:** Pause/Resume, Reset, Optional: Speed Slider.
    * **Manual Control Section:** Select bot, Enable checkbox, Key mapping info.
    * **Game Over Display:** Show winner/draw message.

## 7. Manual Keyboard Control

* Implement listeners (`keydown`, `keyup`).
* Map keys to **directly set target values** for the controlled bot (e.g., `W` sets `target_speed` towards `max_speed`, `A`/`D` modify `target_angle`, `Q`/`E` modify `target_turret_angle`, `Space` calls `fire()`). Respect game rules (cooldowns, **shutdown state**).
* Disable `ai_manager` execution for the manually controlled bot's AI function.

## 8. Rendering (Canvas 2D API)

* **Game Loop:**
    1. Clear the entire canvas (`ctx.clearRect(0, 0, canvas.width, canvas.height)`).
    2. Draw arena background (e.g., `ctx.fillStyle`, `ctx.fillRect`).
    3. Iterate through bots:
        * `ctx.save()`
        * `ctx.translate(bot.x, bot.y)`
        * `ctx.rotate(bot.angle)`
        * Draw bot body shape (triangle: `ctx.beginPath`, `moveTo`, `lineTo`, `closePath`, `fill`, `stroke`). Use bot's `color`.
        * `ctx.rotate(bot.turret_angle - bot.angle)` (If turret angle is absolute; adjust if relative). Or perform separate translate/rotate for turret.
        * Draw turret shape (rectangle/line).
        * `ctx.restore()`
        * Optional: Draw health/heat bars directly above/below bot (requires inverse transforms or drawing after restoring).
    4. Iterate through active projectiles: Draw shape (e.g., small circle `ctx.arc`, `fill`).
    5. Draw Scan Effects: If a scan is active, draw a semi-transparent arc (`ctx.arc`) originating from the bot/turret.
    6. Draw Explosion Effects: If an explosion is active, draw expanding circles or particle-like effects.
* **Coordinate System:** Ensure all drawing commands use the chosen coordinate system (e.g., Y downwards, angles in radians).

## 9. Weapons and Combat (Projectiles)

* **Firing Logic:** On successful `api.fire()` (not cooldown/shutdown): Generate heat, start `fire_cooldown`. Create projectile **JavaScript object**:
    * `ownerId`, `x`, `y` (spawn at turret muzzle point).
    * Calculate initial `vx`, `vy` based on `projectile_speed` and current turret angle (`vx = Math.cos(turret_angle) * speed`, `vy = Math.sin(turret_angle) * speed`).
    * `damage` (based on `fire_power`, adjusted by overburn).
    * `creationTime = performance.now()`.
    * Add projectile object to an active projectiles list.
* **Projectile Movement:** In game loop update phase, iterate active projectiles:
    * `proj.x += proj.vx * dt`
    * `proj.y += proj.vy * dt`
* **Projectile Lifetime:** Check `performance.now() - proj.creationTime`. Remove projectile object if it exceeds `projectile_lifetime`.
* **Projectile Collision/Damage:** Performed in manual collision detection phase (Section 4). On hit: apply damage to bot, remove projectile object. Check target destruction.
* **Destruction:** If bot `armor <= 0`: Trigger destruction sequence (mark bot inactive), create explosion effect object (position, current radius, max radius, duration). Remove bot object. Check win condition.
* **Explosion Effect:** Update explosion object each frame (increase radius, decrease opacity). Check for nearby bots within current radius, apply damage based on distance (falloff) and `explosion_damage`. Remove effect object when done.

## 10. Overburn Logic

* **Activation:** `api.overburn(True)` sets flag (if not shutdown).
* **Effects:** Multiplies effective `max_speed` and `fire_power`. Increases `heat`. Check `max_heat`.
* **Deactivation:** `api.overburn(False)` clears flag. Modifiers revert. Overburn heat generation stops.
* **Passive Heat Dissipation:** `heat` decreases by `heat_dissipation_rate * dt`, clamped at 0.

## 11. Overheating State (Temporary Shutdown)

* **Trigger:** Set `bot.isShutdown = true` when `heat >= max_heat`.
* **Consequence:** While `isShutdown` is true: Bot ignores movement/action commands from AI/Manual Control. `target_speed` might be forced to 0. `fire()`, `overburn()` etc. fail.
* **Reactivation:** Set `isShutdown = false` when `heat` drops below threshold (e.g., `0.9 * max_heat`).
* **Indication:** Visual (Section 8), UI status (Section 6).

## 12. Game State Management & Win Condition

* **States:** `Setup`, `Running`, `Paused`, `GameOver`.
* **Transitions:** Manage state changes.
* **Win Condition:** Last bot remaining active (`armor > 0`).
* **Game End Logic:** On bot destruction, check remaining active bots. If <= 1, transition to `GameOver`, display result.

## 13. Future Considerations / Phase 2

* 2D Arena obstacles (drawn shapes, add to collision checks).
* Different 2D weapon effects (e.g., beam using `lineTo`, area effect).
* Power-ups (drawn items, collision checks).
* Team modes.
* Simple particle effects using Canvas.
* Sound effects.
* Persistence (Save/Load JS AI code via LocalStorage or files).
* Tilemap backgrounds or simple sprites instead of basic shapes.