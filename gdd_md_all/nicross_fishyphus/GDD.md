# GDD
Sail the waves, catch every fish, and avoid the reaper.

Traverse an impressionistic sea, listening for predator and prey.
Cast a lure and feel their cues to reel them in.
The reaper slowly tracks your movements, who you must outmaneuver to survive.

## Objective
To create a fast-paced horror experience with a fishing minigame.

### Goals
- Prioritize universal design.
- Intuitive fishing minigame that's impossible to lose but hard to master.
- Reactive music which signals a creeping dread.
- Responsive controls and movement.
- Supported with tasteful haptics.
- Impressionistic yet informative graphics.

### Strategy
- v0.1.0: Basic playable prototype
- Prioritize interface, gameplay, audio, video, haptics, documentation.

## Systems
### World generation
- Flat for all gameplay purposes.
- Simplex noise generators drive the environmental audio and graphics.

### Movement
- Tank controls which apply force in the facing direction.
- Drifting with heavy acceleration and deceleration.
- Movement speed is no greater than 10 m/s.
- Tweak to the perfect feel.

### Fishing
- Musical fish spawn and move in circles around points in the world.
- The radius of the circle shortens as you near its center.
- This determines the difficulty of the minigame.
- Pressing the action button initiates the minigame by casting a lure.
- During the minigame the movement controls are ignored.
- A cue will indicate the best time stop casting the lure.
- The fish approaches the lure at a speed based on the timing.
- A cue will indicate when to start reeling in.
- Mashing the button decreases the time slightly but not significantly.
- Once the fish is caught, the score increases and movement controls are active again.

### Death
- The reaper spawns below and moves at a constant rate equal to the player speed.
- Starting depth of reaper defaults to 60 seconds away.
- During the fishing minigame, it moves twice as fast.
- After the fishing game, it's stunned for a short time.
- While stunned it cannot move.
- The game ends if it reaches the player.

### Persistent rewards
- After certain highscores the player receieves bonuses.
- **MVP:** the reaper receives a small depth bonus per point of highscore.
- Post-jam this could be expanded with an end-of-game screen and several bonus types:
  - Reaper depth bonus
  - Movement speed bonus
  - Reaper stun bonus

## Interface
### Controls
- WASD, arrow keys, or numpad to accelerate, reverse, and turn.
- Spacebar or enter to perform actions.
- Gamepad should accept input from either stick and respond to any button press.
- Mouse to turn and click to perform actions.
- Escape or Start/Select pause the game.

### Screens
- The traditional splash screen.
- Main menu with Continue, New Game, or Quit buttons.
- Game screen where the action happens, with an `aria-live` region for the score.
- Pressing a menu button will autosave and go back to main menu.
- Game over screen with score, highscore, and back button.

### Audio
- Basic movement sound based on current velocity.
- Sample the ocean surface to emit quiet, staccato, musical sounds.
- Parameterized music which reacts to reaper position and stun status effect.
- Fish emit tones from their positions.
- Sound effects to support the fishing minigame.
- Heavy reverb except for sound effects.

### Video
- First-person camera.
- Sky shader provides a subtle background color which changes over time.
- Water shader samples the surface and paint dots in a secondary color.
- Particle effect shader responds to fish audio.
- Film grain shader responds to monster position.
- Analogous pastel colors which rotate around the color wheel.

### Haptics
- Rumbles when near a fishing location.
- Rumbles during important fishing minigame cues.
- Rumbles in pulses as the reaper nears.
