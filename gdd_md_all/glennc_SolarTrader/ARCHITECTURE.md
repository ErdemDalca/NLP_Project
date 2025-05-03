# Proposed Project Architecture for Solar Clipper

## Goal

To create a modular and extensible architecture for the Solar Clipper game, aligning with the Game Design Document (GDD) and allowing for future expansion to include multiple locations (e.g., ships, stations).

## Core Concepts

1.  **Location Abstraction:** Introduce a base `Location` concept to represent any navigable space (ship, station, etc.). Specific locations like `Ship` will inherit from or implement this base.
2.  **Compartments:** Define `Compartment` (or `Room`) generically as an area *within* any `Location`.
3.  **World Management:** A dedicated `WorldManager` will track all active `Location` instances and the player's current position among them.
4.  **Modular Systems & Interfaces:** Keep game systems (power, life support) and UI interfaces (bridge terminal, datapad) separate and potentially tied to specific `Location` types where appropriate.
5.  **Dynamic CSS Loading:** A system to load and unload CSS stylesheets per interface, ensuring CSS is modular and interface-specific styles are only loaded when needed.

## Proposed Directory Structure (`src/`)

*   **`core/`**: Fundamental game objects and concepts.
    *   `location.ts`: Base class/interface for navigable locations.
    *   `ship.ts`: Implementation of `Location` for the player's ship, **including ship-wide inventory (supplies, parts).**
    *   `compartment.ts`: Represents areas within a location, **containing `Entity` instances and potentially fixed interactable objects/tools.**
    *   `player.ts`: Player state (needs, **skills**, personal inventory, current location/compartment).
    *   `game-state.ts`: Overall game state tracking.
    *   `entity.ts`: **Foundational base class/interface for all objects existing within the game world (terminals, items, equipment, NPCs).**
    *   `interactable-object.ts`: Base class for game objects that can be interacted with (examined, used, etc.).
*   **`systems/`**: Individual game mechanics.
    *   `power.ts`, `life-support.ts`, `propulsion.ts` (Ship-specific)
    *   `needs.ts` (Player-specific)
    *   `system.ts` (Optional): Base class/interface for systems.
    *   `base-system.ts`: Foundation for all ship systems with common functionality.
*   **`managers/`**: Handles overarching game logic and state transitions.
    *   `world-manager.ts`: Manages locations, player movement between them.
    *   `time-manager.ts`: Tracks game time, updates systems.
    *   `event-manager.ts`: Triggers random events.
    *   `interface-manager.ts`: **Switches between different UI views based on interaction events triggered on world entities.**
    *   `command-parser.ts`: Handles user input parsing, **interpreting general commands, and triggering entity interactions or system actions.**
*   **`interfaces/`**: Defines the different UI views and rendering logic. **Views handle UI-specific input (clicks, menu keys) directly.**
    *   `base-interface.ts`: Abstract base for UI modes.
    *   `first-person-view.ts`: Text-based navigation display.
    *   `bridge-terminal-view.ts`: Renders the bridge UI (Ship-specific).
    *   `datapad-view.ts`: Renders the datapad UI.
    *   `engineering-view.ts`: Renders the engineering UI (Ship-specific).
    *   `dom-renderer.ts`: Handles updating the HTML DOM.
    *   `dom-css-loader.ts`: Manages dynamic loading and unloading of CSS.
    *   `base-system-interfaces.ts`: Base class for all system interfaces with shared functionality.
    *   `systems/`: System-specific interface implementations.
    *   `terminals/`: Terminal-specific interface implementations.
*   **`data/`**: Static game data definitions.
    *   `location-definitions.ts`: Data for ships, stations, etc.
    *   `compartment-definitions.ts`: Data for rooms/areas within locations.
    *   `item-definitions.ts`: Data for items, tools, etc. (potentially portable).
    *   **`entity-definitions.ts`: Data for fixed entities within locations (terminals, stations).**
*   **`narrative/`**: **Handles text generation, templates, and procedural rules.**
    *   **`text-generator.ts`: Core text generation logic.**
    *   **`templates/`: Directory for text templates.**
    *   **`rules/`: Directory for procedural generation rules.**
*   **`utils/`**: Helper functions.
*   **`main.ts`**: Application entry point, initializes managers, starts game loop.

## CSS Organization

*   **`styles.css`**: Core application styles (base layout, typography, variables).
*   **`css/`**: Directory for modular CSS files:
    *   `system-interfaces.css`: Shared styles for system interfaces.
    *   `coolant-system.css`: Specific styles for the coolant system interface.
    *   `components/`: Reusable UI component styles:
        *   `action-controls.css`: Button and action element styles.
        *   `alert-indicators.css`: Alert and status indicator styles.
        *   `datapad.css`: Datapad-specific styles.
        *   `resource-displays.css`: Resource meter and gauge styles.

## Established Conventions

1. **Dynamic CSS Loading**: CSS is loaded on-demand when entering an interface and unloaded when exiting, using the `dom-css-loader.ts` utility.
   ```typescript
   // Loading CSS in a system interface
   this.loadInterfaceCSS('/css/system-name.css', 'system-name');
   
   // Unloading when exiting the interface
   this.unloadInterfaceCSS();
   ```

2. **Interface Structure**: System interfaces follow a standard pattern:
   * Extend `BaseSystemInterface`
   * Implement `renderInterface()` method that returns a cleanup function
   * Use `loadInterfaceCSS()` for interface-specific styles
   * Use DOM manipulation via `DOMRenderer` for interface rendering

3. **CSS Namespacing**: Interface-specific styles use prefixed class names to avoid conflicts:
   * `.system-diagnostics` for diagnostics interface
   * `.coolant-system` for coolant system interface

4. **Status Indicators**: Standardized classes for status indicators:
   * `.status-normal`, `.status-warning`, `.status-danger` for system status
   * `.status-good`, `.status-warning`, `.status-danger` for component states

5. **Animation & Effects**: Common animation conventions:
   * `@keyframes progress-scan` for diagnostic scanning effects
   * `@keyframes pulse` for alerting elements
   * `.diagnostic-running` for active diagnostic displays

## Visualization

```mermaid
graph TD
    subgraph src
        main.ts --> managers
        managers --> core
        managers --> systems
        managers --> interfaces
        managers --> narrative // Added
        core --> data
        core --> narrative // Narrative might need core concepts
        systems --> core(ship.ts)
        interfaces --> core
        interfaces --> narrative // Interfaces consume generated text
        interfaces --> dom-renderer.ts
        interfaces --> dom-css-loader.ts // Added CSS loader connection
        managers --> command-parser.ts
        command-parser.ts --> interfaces
        command-parser.ts --> core // For interacting with entities

        subgraph core
            direction TB
            entity.ts      // Now foundational
            game-state.ts
            location.ts
            ship.ts        // Implements Location, holds ship inventory
            station.ts     // Example future Location
            player.ts      // Holds personal inventory, needs, skills
            compartment.ts // Contains Entities
            interactable-object.ts // Base for interactable objects
        end

        subgraph systems
            direction TB
            base-system.ts // Base system class
            power.ts
            life-support.ts
            needs.ts
            // ... Ship-specific systems ...
        end

        subgraph managers
            direction TB
            world-manager.ts
            time-manager.ts
            event-manager.ts
            interface-manager.ts // Switches views based on entity interactions
            // Potentially InteractionManager if CommandParser doesn't handle it
        end

        subgraph interfaces
            direction TB
            base-interface.ts
            first-person-view.ts
            bridge-terminal-view.ts
            datapad-view.ts
            engineering-view.ts
            base-system-interfaces.ts // Added base for system interfaces
            systems/  // Added system interfaces
            terminals/ // Added terminal interfaces
            // Views render data, handle UI-specific input
        end

        subgraph data
            direction TB
            location-definitions.ts
            compartment-definitions.ts
            item-definitions.ts
            entity-definitions.ts // Added for fixed entities
        end

        subgraph narrative // Added
            direction TB
            text-generator.ts
            templates/
            rules/
        end
    end

    index.html --> main.ts
    styles.css --> index.html
    css/system-interfaces.css --> dom-css-loader.ts // Added CSS file connections
    css/coolant-system.css --> dom-css-loader.ts
    css/components/ --> dom-css-loader.ts
```

## CSS Loading System Flow

```mermaid
sequenceDiagram
    participant UI as User Interaction
    participant IM as InterfaceManager
    participant SI as SystemInterface
    participant CL as DOM CSS Loader
    participant DOM as Browser DOM
    
    UI->>IM: interact with system
    IM->>SI: renderInterface()
    SI->>CL: loadInterfaceCSS()
    CL->>DOM: create <link> element
    CL->>DOM: append to <head>
    SI->>DOM: render interface HTML
    
    Note over UI,DOM: User uses interface
    
    UI->>IM: exit interface
    IM->>SI: call cleanup function
    SI->>CL: unloadInterfaceCSS()
    CL->>DOM: remove <link> element
    SI->>DOM: restore previous view
```

## Future Expansion (Example: Adding a Station)

1.  Create `src/core/station.ts` implementing `Location`.
2.  Add station compartment data to `src/data/compartment-definitions.ts`.
3.  Update `WorldManager` to handle station instances and docking logic.
4.  Add station-specific systems (e.g., `src/systems/trading.ts`) or interfaces (e.g., `src/interfaces/station-market-view.ts`) if needed.