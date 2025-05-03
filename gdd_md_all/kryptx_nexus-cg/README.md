# NEXUS: The Convergence - LÖVE Implementation

**Version:** 0.2 (Rendering & Styling Setup)

This README provides information for developers working on the LÖVE (Love2D) implementation of the strategic card game NEXUS: The Convergence.

**Note:** This README should be kept up-to-date with the current state of the project, including setup instructions, key architectural decisions, and build status.

## 1. Overview

NEXUS: The Convergence is a strategic card game focused on network building and player interaction via a "convergence" mechanic. This project aims to create a 2D digital version suitable for prototyping, playtesting, and potentially wider release.

For detailed gameplay rules, mechanics, theme, and design goals, please refer to the **[Game Design Document (GDD.md)](GDD.md)**.

## 2. Technology

*   **Engine:** LÖVE (Love2D) framework ([https://love2d.org/](https://love2d.org/))
*   **Language:** Lua
*   **Target Platforms:** Windows, macOS, Linux
*   **Fonts:** Requires Roboto Regular and Roboto SemiBold fonts (included in `assets/fonts/`).

## 3. Setup & Running

1.  **Install LÖVE:** Ensure you have the latest stable version of LÖVE installed for your operating system from the official website.
2.  **Clone Repository:** Clone this project repository to your local machine.
3.  **Run:**
    *   Navigate to the **root directory (`nexus/`)** of the cloned repository in your terminal.
    *   Run the command: `love .`
    *   **Important:** The game uses a root `main.lua` file to bootstrap the application from the `src/` directory. Running `love src/` directly will cause errors, especially with asset loading.
    *   Alternatively, on Windows/macOS, you can often drag the **project folder (`nexus/`)** onto the LÖVE application executable (ensure it targets the root folder, not the `src` folder).

## 4. Directory Structure

The project follows this structure to maintain organization:

```
nexus/
├── main.lua           # Root LÖVE entry point (bootstrapper for src/main.lua)
├── conf.lua           # LÖVE configuration file (window size, title, modules)
├── GDD.md             # Game Design Document (READ THIS FIRST)
├── NEXUS_rules_draft.md # Original rules concept draft
├── README.md          # This file
├── src/               # Source code directory
│   ├── main.lua       # Actual game entry point (loads game state, handles core loop)
│   ├── core/          # Core engine systems (state management, event handling)
│   │   └── state_manager.lua # Manages game states (menu, play, etc.)
│   ├── game/          # Gameplay logic and state representation
│   │   ├── card.lua     # Card definitions and logic for all card types (including Reactor)
│   │   ├── player.lua   # Player state, hand, resources
│   │   ├── network.lua  # Network representation, placement logic
│   │   ├── rules.lua    # Core game rules validation, turn structure
│   │   ├── game_service.lua # Orchestrates game flow and actions
│   │   └── states/      # Specific game states
│   │       ├── menu_state.lua
│   │       └── play_state.lua
│   │   └── data/        # Game data definitions
│   │       └── card_definitions.lua
│   ├── rendering/     # Graphics rendering logic
│   │   ├── renderer.lua # Handles drawing game state, cards, UI
│   │   └── styles.lua   # Centralized UI style definitions (fonts, colors)
│   ├── audio/         # Sound and music management
│   │   └── audio_manager.lua # Handles loading/playing audio assets
│   ├── ui/            # User interface components
│   │   └── button.lua   # Example UI element
│   └── utils/         # General utility functions (math, tables, etc.)
│       └── vector.lua   # Example utility
├── assets/            # Game assets (art, sound, music, fonts)
│   ├── fonts/         # Font files (e.g., Roboto-Regular.ttf)
│   ├── images/        # Sprites, icons, card art placeholders (PNG)
│   ├── sounds/        # Sound effects (WAV)
│   └── music/         # Music tracks (OGG)
├── tests/             # Unit and integration tests (using a Lua testing framework like Busted - TBD)
│   ├── core/
│   ├── game/
│   └── utils/
└── lib/               # External Lua libraries (if needed)
```

## 5. Development Philosophy

*   **Modularity:** Keep components (Lua files/modules) small, focused, and responsible for a specific piece of functionality.
*   **Testability:** Design components with testing in mind. Use pure functions where possible and minimize complex dependencies.
*   **Test Coverage:** **Write tests!** Aim for good test coverage, especially for core game logic (`src/core/`, `src/game/`, `src/utils/`). Use a suitable Lua testing framework (e.g., Busted, to be added to `lib/` or managed externally). Tests should verify component behavior in isolation and potentially integration between components.
*   **Clarity:** Write clear, readable code with appropriate comments for complex sections. Follow consistent naming conventions.
*   **GDD Alignment:** Ensure implementation aligns with the design specified in `GDD.md`. If changes are needed, update the GDD first or alongside the code changes.
*   **README Maintenance:** Keep this `README.md` updated with any significant changes to setup, architecture, or dependencies. 

## Lua Development Notes

### Colon (`:`) Syntax for Methods

When defining and calling methods on Lua tables (objects), be mindful of the colon (`:`) syntax:

*   **Definition:** Use `function TableName:methodName(arg1, arg2, ...)`.
    *   The colon `:` after `TableName` implicitly makes the first argument passed to the function `self` (the instance the method is called on).
    *   **Important:** Do *not* explicitly list `self` as a parameter in the definition (e.g., `function TableName:methodName(self, arg1, ...)`). While Lua allows this, it breaks the argument mapping when called with the colon syntax, as the explicitly listed parameters will be matched against the arguments *after* the implicitly passed `self`.
*   **Call:** Use `instance:methodName(val1, val2, ...)`. 
    *   The colon `:` after `instance` implicitly passes `instance` as the first argument (`self`) to the method.

**Example:**

```lua
local MyObject = {}
MyObject.__index = MyObject

-- CORRECT Definition (self is implicit)
function MyObject:greet(message)
  print(string.format("Instance %s says: %s", self.name, message))
end

-- INCORRECT Definition (explicit self with colon definition)
-- function MyObject:bad_greet(self, message) 
--   print(string.format("Instance %s says: %s", self.name, message))
-- end

local obj = setmetatable({ name = "Obj1" }, MyObject)

-- CORRECT Call
obj:greet("Hello!") -- Implicitly passes 'obj' as self, "Hello!" as message

-- Calling bad_greet would lead to errors or incorrect behavior:
-- obj:bad_greet("Hi!") -- 'self' inside bad_greet would receive "Hi!", message would be nil
```

Consistent use of `function T:m(...)` for definition and `instance:m(...)` for calls ensures `self` is handled correctly.
