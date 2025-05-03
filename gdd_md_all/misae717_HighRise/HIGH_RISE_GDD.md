# HIGH RISE - Game Design Document
## Version: Unity 2022.3 LTS
## Implementation Status Legend
- **CANCELLED** - Feature has been cancelled
- **MIGHT CANCEL** - Feature might be cancelled
- **NO NEED TO READ** - Information not relevant for implementation

*Note: Most base ideas in this document may not be implemented*

---

## Core Concept
A gravity-based action platformer with sword combat against robotic enemies and an AI boss. The game draws inspiration from Celeste in its platforming and camera style, and from titles like Cuphead and Nine Sols for its combat and movement feel.

---

## Controls & Camera
- **Camera:** Stable, does not follow the player directly (Celeste-style)
- **Movement:** WASD - Left Analog Stick
- **Jump:** Space - X
- **Attack:** Left Mouse Button (swipe, bottom slash, upper slash) - Square
- **Gravity Activation:** E (connects player to gravity points) - Circle + Right Analog to choose which gravity direction to activate
- **Look Direction:** Character faces mouse cursor - Right analog
- **Dash:** Shift button.

# Keyboard Mouse - DualShock controller

---

## Player Character Mechanics
- **Gravity Mechanic:** Player can connect to specific points in the level, altering movement and combat options
- **Attacks:**
  - Swipe attack (deals 100 damage)
  - Bottom slash (single attack)
  - Upper slash (single attack)
- **CANCELLED:** Three-attack sword pattern (combo)
- **Special Moves (Time Permitting):**
  - Double jump
  - 1.5x attack speed
  - 1.5x faster grapple, including grappling to enemy faces
- **Movement Feel:**
  - Cuphead-like responsiveness
  - Null cancelling for tight control
  - Air time: 0.2–0.5 seconds (to be tested)

---

## Combat & Enemies
- **Eyeball AI Boss:**
  - Inspired by Wheatley (Portal 2)
  - Multi-phase fight with shield and vulnerability mechanics
- **Crab Robots:**
  - 100 health
  - Rush player, die in one hit (invisible health bars)
- **Flying Robots:**
  - Detect player and shoot rockets
- **Porcupine Obstacle:**
  - Unkillable, slow-moving, prevents player from idling

---

## Environment
- **Outdoors:**
  - Features flying enemies and crab robots
- **Indoors:**
  - Boss encounters and narrative moments

---

## Boss Design
- **MIGHT CANCEL:** Octopus-like attack pattern (disrupts player rhythm)
- **Attacks:** Rockets, tentacles, possible parry/slice mechanics
- **Boss Fight Structure (Plan B - Likely):**
  - No strict outdoor/indoor split
  - Certain rooms trigger boss attacks
  - Two phases, with dialogue at 50% health
  - **Stats:** 5 hearts (500 HP)
    - Phase 1: Shielded, unattackable while attacking
    - Phase 2: Shield drops, boss vulnerable
    - After taking damage, shield returns
  - Gravity pods in arena for player movement and attack opportunities
  - After damage, boss may:
    - Move to a new room (player chases)
    - Destroy and respawn platforms

---

## Special Mechanics (Time Permitting)
- **Special Meter System:**
  - Builds up for temporary buffs (e.g., attack speed)
- **Advanced Grapple:**
  - Grapple to enemy faces for unique attacks

---

## References & Inspirations
- Octopus kid (NieR)
- Nine Sols (slicing mechanics)
- Portal 2 (Wheatley)
- Celeste (camera, platforming feel)
- Cuphead (movement responsiveness)

---

## Additional Features
- **NO NEED TO READ:** AI boss speech (humanity theme)
- **CANCELLED:** Nine Sols-style slicing without movement
- **Health System:** 5 hearts (player and boss)
- **Slice Animations:** Two types
- **Damage:** Each hit deals one heart

---

## To Do / Open Questions
- Test and tune air time and movement responsiveness
- Finalize boss attack patterns and vulnerability windows
- Decide on inclusion of special meter and advanced grapple
- Playtest for level and enemy balance 