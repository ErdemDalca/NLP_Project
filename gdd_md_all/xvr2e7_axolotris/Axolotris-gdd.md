# Axolotris (A Submission to Studio Jam 2024)

## Core Concept

A strategic block manipulation game where a clever axolotl must engineer its own escape by transforming surrounding blocks into tetriminoes. By inverting the traditional Tetris formula, players actively create their pieces before using them to break free from their blocky prison.

## Core Mechanics

### Grid Specifications

- Size: 12(width) x 21(height)
- Buffer Zone: Top 7 rows for Tetris piece manipulation
- Exit: Two blocks wide, centered at top of grid
- Minimum path width: 2 blocks

Example Grid Layout:

```
Row 21 [ ][ ][ ][ ][ ][E][E][ ][ ][ ][ ][ ]   E = Exit
Row 20 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]   Buffer Zone
Row 19 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]   (7 rows for
Row 18 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]    Tetris play)
Row 17 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
Row 16 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
Row 15 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
Row 14 [PH][ ][WV][ ][PH][ ][ ][ ][ ][ ][ ][ ]
Row 13 [ ][ ][≈][ ][ ][ ][ ][ ][ ][ ][ ][ ]
...
Row 1  [S][A][S][S][S][S][ ][ ][ ][ ][ ][ ]
```

### Game States

**Navigation Mode (Primary)**

- Move axolotl through grid
- Select blocks to create tetriminoes
- Store created pieces for later use
- Cannot pass through barrier fields
- Cannot select blocks in barrier fields

**Tetris Mode (Activated by TAB)**

- Traditional Tetris controls
- Use previously created pieces
- Clear lines to break barriers
- Auto-return to Navigation when pieces depleted

### Player Character (The Axolotl)

- Grid-based movement (up/down/left/right)
- Fixed selection range (3 adjacent blocks)
- Four-direction rotation
- Selection directions tied to orientation (like rami extending from sides)

### Barrier System

**Barrier Strength Types**

```
Primary Barrier [P]:
- Requires either:
  * Double line clear
  * Two separate single line clears

Weakened Barrier [W]:
- Requires:
  * Single line clear
```

**Field Projection Types**

```
Horizontal Lock [→]:
- Projects barrier field left/right
- Blocks horizontal movement/selection

Vertical Lock [↑]:
- Projects barrier field up/down
- Blocks vertical movement/selection

Cross Lock [+]:
- Projects in all directions
- Maximum field coverage
```

**Combined Notation**

```
[PH] = Primary Horizontal Barrier
[WH] = Weakened Horizontal Barrier
[PV] = Primary Vertical Barrier
[WV] = Weakened Vertical Barrier
[P+] = Primary Cross Barrier
[W+] = Weakened Cross Barrier
```

### Safe Block System

**Static Safe Blocks [S]**

- Immune to barrier fields
- Permanently accessible for selection
- Strategically placed in level design
- Creates reliable navigation points
- Essential near starting position

**Power-up Runes** (Optional Feature)

- Collectible items that grant temporary immunity
- Remove (shovel away) unwanted Tetrimino
- Add more available moves

### Breaking Mechanics

**Line Clears**

- Single line clear:
  - Destroys weakened barriers
  - Damages primary barriers
- Double line clear:
  - Destroys primary barriers
  - Affects all barriers in cleared rows

**Special Combinations** (Optional Feature)

```
T-Shape Clear:
[■][■][■]    Instant primary barrier break
[_][■][_]    (Must clear simultaneously)
[_][■][_]

Square Clear:
[■][■]       Weakens all adjacent barriers
[■][■]       (Must clear simultaneously)
```

### Essential Assets

- Axolotl (4 rotations)
- Basic blocks
- Barrier blocks (6 types)
- Safe blocks
- Exit blocks
- Field effect indicators
