# Game Design Document for "Vertex"

## 1. Introduction and Overview

**Game Idea:**  
"Vertex" is a turn-based strategy game where two players take turns placing markers on an expanding game board. The objective is to be the first player to align five markers in a row, either horizontally, vertically, or diagonally.

**Vision:**  
Create a simple yet visually appealing game with a minimalist design and smooth animations. The game should be easy to understand and play while offering strategic depth.

---

## 2. Gameplay Mechanics

**Basic Rules:**

- Two players take turns placing markers on the game board.
- There are placement nodes where the player can place markers.
- Starting, there is a single placement node.
- Whenever a marker is placed, any surrounding spot, not containing a placement node or player marker, will have one created.
- A player can place their marker on any placement node.
- The game continues until one player aligns five markers in a row (horizontally, vertically, or diagonally).

**Game Board and Markers:**

- **Game Board:** Starts with a central marker on a placement node and expands with more available nodes as players place their markers.
- **Nodes:** Marks positions where players can place their markers next.
- **Markers:** Two different types of markers are used, one for each player, with contrasting colors for clarity.

**Win Condition:**

- The game automatically detects when a player has placed five markers in a row and declares that player the winner.
- When a player wins, the winning row is animated to highlight the victory.

---

## 3. Graphics and Animation

**Visual Style:**

- **Background:** A darker background that creates contrast against the markers and highlights the game board.
- **Markers:** Contrasting colors distinguish the two players' markers. The markers have a subtle reflective effect that gives them depth and enhances the minimalist design.
- **Hover:** When hovering over placement nodes, an opacity color is applied to the node, helping indicate which player will get the marker at this position if placed.
- ~~**Mouse cursor:** The mouse cursor is represented by an animated particle system that reflects the current player's color. This particle system emits a soft light that casts around the surrounding area, providing a subtle visual cue of the player’s active turn.~~

**Animations:**

- **Placement:** When a marker is placed, it is animated where the placement node is animated in color to the player's color, while the size is increased. It is increased to slightly larger before reaching its final permanent size.
- **Winning Sequence:** When a player wins, the winning markers pulse and light up to signify the victory.

---

## 4. Camera Handling

- **Automatic Camera Management:** The camera automatically zooms out as the game board expands. The camera always keeps the center of the game board in focus, providing the player with a good overview of the entire board. When the center changes, it will smoothly adjust its position.

---

## 5. User Interface (UI)

**Start Menu:**

- **Layout:** A simple menu with a "Start Game" button centered, covering the screen.
- **Functionality:** The start menu allows the player to begin a new game.

**Restart Game:**

- **After Winning:** After a player wins, a button appears that allows players to restart the game from the beginning. This doesn’t prevent the player from seeing the game board.

---

## 6. Development Plan for Version 1.0

**Milestones:**

1. **Basic Structure:**
   - Implement the game board and markers.
   - Implement basic game rules and turn-taking.

2. **Gameplay Mechanics:**
   - Implement the logic to detect five in a row and trigger a win.

3. **Graphic Polishing:**
   - Implement basic graphics and animations for markers and winning sequences.

4. **Camera Handling:**
   - Implement automatic camera management that zooms out as the game board expands.

5. **User Interface:**
   - Create the start menu and implement the game restart functionality.

6. **Mouse Cursor Experimentation:**
   - ~~Develop and implement the particle-based mouse cursor that reflects the current player's color and emits light.~~
