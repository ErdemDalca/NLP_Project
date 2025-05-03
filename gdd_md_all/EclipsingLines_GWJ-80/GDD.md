# Game Design Document: gwj_80

## 1. Game Overview

### 1.1 Game Title

gwj_80 (Working Title)

### 1.2 Genre

Puzzle

### 1.3 Target Audience

All ages

### 1.4 Platform

Web (HTML5)

### 1.5 Game Summary

gwj_80 is a grid based card color puzzle game. You use cards with different shapes (o and +) and one of the basic colors each turn to color a portion of the board. The round ends after a set number of turns, and the player is scored based on how closely the resulting image matches a target grid.

---
*This document is a living document and will be updated throughout development.*

## 2. Gameplay Mechanics

### 2.1 Core Mechanics

- **Grid-based Coloring:** Players apply colors to a grid using cards.
- **Card System:** Players draw and use cards with specific shapes and colors.
- **Turn-based Gameplay:** Players take turns playing cards.
- **Scoring System:** Player's final grid is compared to a target grid for scoring.
- [Add more core mechanics as defined]

### 2.2 Player Actions

- **Draw Card:** Automatically draw 1 card per turn.
- **Select Card:** Choose a card from the hand.
- **Place Card:** Apply the selected card's shape and color to a chosen location on the grid.
- **End Turn:** (Potentially implicit after placing a card or if turn limit exists).
- [Add more player actions as defined]

### 2.3 Game Rules

- **Grid Size:** 16x9 cells.
- **Card Shapes:**
  - 'o': Applies color to a 3x3 block centered on the target cell.
  - '+': Applies color to a 3x3 cross (center cell + 4 cardinal neighbors).
  - '-': Applies color to a 3-cell horizontal line centered on the target cell.
  - '|': Applies color to a 3-cell vertical line centered on the target cell.
  - '.': Applies color to a single target cell.
- **Card Colors:** Red (R), Green (G), Blue (B).
- **Hand Size:** 5 cards.
- **Turn Limit:** 15 turns per round.
- **Color Application:** Grid cells start white. Applying a card blends its color with the cell's current color. Applying a 5th blend/card to the same cell turns it black. (Specific blending logic TBD).
- **Scoring Calculation:** Percentage (%) match between the player's final grid and the target grid.
- [Add more game rules as defined]

### 2.4 Objectives

- **Primary Objective:** Replicate the target grid as accurately as possible within the turn limit.
- **Secondary Objectives:** [e.g., Achieve a minimum score, use specific card combinations, complete bonus challenges].

## 3. Game World

### 3.1 Setting

- **Visual Style:** Pixel Art.
- **Atmosphere:** Retro Psychedelic.
- **Lore/Theme (Optional):** Finishing your art piece as fast as possible.

### 3.2 Level Design

- **Structure:** Each level consists of a target grid image to replicate.
- **Progression:** Difficulty increases through:
  - Less time allowed per turn (if timed turns are implemented).
  - Target images starting with some pre-filled (potentially incorrect) colors.
  - After completing a set number of 16x9 rounds, the completed images are combined into a single larger target image for a "boss" round.
- **Level Grouping (Optional):** Levels are grouped into sets corresponding to larger pixel art images. Each 16x9 grid represents a block of the larger image.
- **Development Strategy Note:** The initial development focus will be on creating a sandbox mode where players can freely use cards to color the grid. The target image replication and scoring mechanics will be implemented *after* the core sandbox is functional. This allows for easier testing and iteration of the core coloring mechanics.

### 3.3 Map Layouts (Target Grids)

- Target grids will be pre-designed images using the available colors on the 16x9 grid.
- Examples will be created during development.
- [Consider how target grids are stored/loaded].

## 4. Characters

*(This section may be minimal for an abstract puzzle game)*

### 4.1 Protagonist

- N/A (Player is represented by their actions on the grid/cards).

### 4.2 Antagonists

- N/A (The challenge comes from the puzzle itself and the turn limit).

### 4.3 Non-Player Characters (NPCs)

- N/A

## 5. Story and Narrative

*(This section may be minimal for an abstract puzzle game)*

### 5.1 Plot Summary

- N/A (Focus is on puzzle-solving).

### 5.2 Story Arcs

- N/A

### 5.3 Dialogue

- N/A

## 6. User Interface (UI) and User Experience (UX)

### 6.1 UI Elements

- **Game Grid:** The main 16x9 play area.
- **Target Grid Display:** Shows the image the player needs to replicate.
- **Player Hand:** Displays the 5 cards the player currently holds.
- **Card Selection Indicator:** Highlights the currently selected card.
- **Turn Counter:** Shows remaining turns (out of 15).
- **Score Display:** Shows the current match percentage (updates potentially at end of round).
- **Color Palette Indicator (Optional):** Shows the available R, G, B colors.
- **Shape Indicator (Optional):** Shows the available card shapes.
- **Menus:** Main Menu, Pause Menu, Level Select (if applicable), Options, End-of-Round Screen (showing score, target vs actual).
- [Add more UI elements as needed]

### 6.2 UX Flow

- **Main Menu:** Start Game, Options, Quit.
- **Gameplay Loop:**
    1. Level starts, target grid displayed.
    2. Player hand is dealt/drawn.
    3. Player selects a card from hand.
    4. Player clicks a cell on the grid to place the card shape/color.
    5. Grid updates based on color blending rules.
    6. Card is consumed from hand.
    7. Player draws a new card.
    8. Turn counter decreases.
    9. Repeat steps 3-8 until turn limit reached.
- **End of Round:** Display player's grid vs target grid, show score (%), offer options (Next Level, Retry, Main Menu).
- [Refine UX flow based on specific interactions]

### 6.3 Accessibility

- **Color Blindness:** Consider alternative ways to differentiate colors (patterns, symbols?) or offer colorblind modes if blending is complex.
- **Input:** Ensure clear visual feedback for card selection and placement. Mouse-driven primarily for web.
- [Add other accessibility considerations]

## 7. Audio and Visuals

### 7.1 Art Style

- Pixel Art.

### 7.2 Sound Design

- **Music:** Retro psychedelic background track(s). Different tracks for menu vs gameplay?
- **Sound Effects (SFX):**
  - Card Draw
  - Card Select
  - Card Place (different sound per color/shape?)
  - Color Blend
  - Cell turns Black (5th blend)
  - Turn End/Counter Tick
  - Level Start
  - Level Complete (Success fanfare based on score?)
  - UI Button Clicks/Hover
- [Add more sound design elements]

## 8. Monetization Strategy (if applicable)

- N/A (Likely not applicable for a game jam web game).
