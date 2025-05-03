# Stellar Onslaught: One-Week Task List

## 1. Project Setup & Core Features

### Unity & Repository Setup
- Create a new Unity project (build target: WebGL).
- Initialize a GitHub repository; ensure all members can commit/pull.
- Create an itch.io project page for web builds.

### Main Menu & Basic Flow
- Implement a simple main menu (Play / How to Play / Quit).
- Ensure clear start/exit flow for user convenience.

### Core Shooting Mechanics
- **Player movement** (left/right).
- **Player shooting** (bullet spawning, speed, fire rate).
- **Basic enemy spawns/movement** (expand waves/patterns later).
- **Collision detection** (bullet vs. enemy, enemy vs. player, debris vs. player).
- **Player lives** (3-life system) & Game Over handling.

### Basic Scoring System
- Award points for destroying enemies/obstacles.
- Display the running score in the HUD.

---

## 2. Tutorial / Onboarding

### “How to Play” Screen or Brief Tutorial
- Explain controls (A/D for movement, Space for shooting, etc.).
- Clarify objectives (avoid dying, destroy enemies, etc.).

### UI Tips if Needed
- Show short in-game hints at the start.

---

## 3. Upgrades & Skill Points

### Skill Point Acquisition & Management
- Grant skill points after finishing each wave/level.
- Maintain a running total of skill points.

### Upgrade/Shop UI
- Spend skill points in a menu or between stages.
- Upgrade categories (e.g. movement speed, bullet damage, bullet speed, defense).

### Implementing Upgrade Effects
- Ensure upgrade choices affect gameplay (e.g. bullet damage increases, etc.).

---

## 4. Wave Structure & Difficulty Tuning

### Wave/Level Progression
- Move to the next wave once enemies are cleared.
- Show a results screen with score + skill point rewards → go to upgrade menu.

### Balancing Enemies
- Adjust enemy count, HP, firing rate, and speed to match player upgrades.
- Avoid making the game too easy after upgrades.

### Mid-Week Internal Playtest
- Run a full-flow test (start → wave clearance → skill upgrade → next wave).
- Identify major bugs or balance issues early.

---

## 5. Visual & Audio Feedback / UI Polish

### Effects
- Small explosion or hit effect when enemies are destroyed.
- Player hit flashes or sounds.
- Visual differentiation for upgraded bullets.

### Audio
- Background music (loop if possible).
- SFX for shooting, explosions, UI interactions.
- Consider audio toggles (mute on/off) if time permits.

### UI/UX Fine-Tuning
- HUD elements (lives, score, skill points).
- Upgrade screen layout & main menu flow.

---

## [If We Have Time] 6. Boss Battle & Final Win/Loss Conditions

### Implement Boss (If Time Permits)
- Add a final wave with a tougher boss.
- Unique projectile patterns or higher HP.

### Victory & Game Over
- “Victory” screen upon beating the final wave/boss.
- “Game Over” screen when lives reach zero.
- Local high score save if time allows.

---

## 7. Final Polish & Submission Prep

### Bug Fixes & Performance Tuning
- Address collision issues, spawn timing, or other frequent problem areas.
- Ensure stable framerate and no major crashes.

### WebGL Build & itch.io
- Export a WebGL build and upload to itch.io.
- Test in a browser to confirm everything runs correctly.

### Individual Video Recordings & GDD Updates
- Record short clips of each feature you implemented (for grading).
- Update the Game Design Document with any final changes.

### Final Daily Check & Git Confirmation
- Verify all commits are pushed to GitHub.
- Confirm each task’s status → finalize submission.

---

## Additional Reminders
- **Daily Stand-Ups**: Spend a few minutes each day sharing progress and blockers.
- **Focus on a Playable Version First**: Prioritize bug-free core gameplay over fancy effects if time is tight.
- **Proof of Implementation**: Keep short recordings of your implemented features for final evaluation.
