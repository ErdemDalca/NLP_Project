# Game Design Document (GDD)

## 1. Game Overview
- **Title (working):** _Echoing Fates_
- **Genre:** Text Adventure / Interactive Fiction / RPG
- **Platform:** PC Terminal
- **Target Audience:** Old-School RPG fans
- **Game Summary:**
  > This game is a call-back to old-school adventure games player entirely in the terminal. You are the heroic adventurer off on a quest to save the realm. Explore the world, fight monsters, collect treasure. Inspired by TTRPGS like Dungeons & Dragons.

---

## 2. Gameplay
### Core Gameplay Loop
- Read narrative text
- Make choices or input commands
- Receive feedback and consequences
- Repeat

### Player Input
- Parser-based (e.g., `take torch`) or choice-based (e.g., `1. Go north`)

### Combat System (if applicable)
- Turn-based?
- Dice rolls or stat comparisons?

### Inventory & Item Management
- Text list or structured inventory
- Equipables, weight limits?

### Character Stats and Progression
- Stats: Strength, Intelligence, etc.
- Leveling or skill-based system

### Quests and Objectives
- Main story arc
- Optional side quests

---

## 3. Narrative Design
### Setting
- TODO

### Plot Summary
- TODO

### Characters
- Player Character

### Dialogue & Choices
- TODO

---

## 4. World Design
### Locations & Areas
- To be added later

### Exploration Mechanics
- Puzzles
- Passwords
- Maybe 'fast travel'

---

## 5. User Interface
### Input Method
- Typed commands

---

## 6. Systems & Mechanics
### Parser System (if applicable)
- Programmed commands
- always available help function (with context specific actions, ie. attack only available when the player has something to attack)
- Planned arrow key interaction to allow the player to scroll through the commands and select one with the enter key

### Save/Load System
- Plan on both auto-save and manual

### Randomness & RNG
- Dice simulation
- random enemies and world

---

## 7. Art & Audio (Optional)
### Visual Style
- Maybe ASCII Art
- Maybe add color

### Music & SFX
- Plan on using the Windows terminal capability of playing WAV files to add some music
- Add Sound Effects (again using WAV files) for increased immersive experience

---

## 8. Technical Details
### Programming Language
- C#, JSON

### Framework or Engine
- Custom

### File Structure
- Data-driven vs logic-heavy scripting

---

## 9. Content Plan
### Game Length
- TBD

### Replayability
- Procedurally generated world
- Proceedurally generated BBEGs and Factions for a dynamic world

### Modularity
- Code released under CC BY-SA 4.0

---

## 10. Development Timeline
### Milestones
- [ ] Core engine prototype
- [ ] Basic input/output system
- [ ] First playable chapter
- [ ] Full narrative content
- [ ] Final polish and release

### Tools
- Git
- Visual Studio 2022 Community

---

## 11. Testing & QA
- Internal playtesting
- External feedback cycle
- Bug tracking process
- Balancing (combat/stat system)

---

## 12. Distribution & Monetization
### Release Format
- Downloadable executable
- Source Code on Github

### Platforms
- GitHub
- Itch.io

---

## 13. Future Features / Stretch Goals
- Voice acting or narration
- Procedural story elements
- Dynamic NPC interactions
- Community-created modules

---
