# E.X.O.
Exoskeletal exomoon explorer

## Goals
To expand on S.E.A. thematically and mechanically:
- Present an alternate perspective to its narrative universe
- Explore new terrain generation techniques
- Provide new freedoms of movement

## Controls
### Keyboard
W/S - Accelerate forward/backward
A/D - Strafe left/right (on-foot only)
Q/E - Turn left/right
F - Scan
R - Vehicle mode switch
Space - Jump (double-jump to engage jetpack)
Shift - Sprint / Turbo
Esc - Menu

### Gamepad
Left Stick - Forward/backward/strafe
Right Stick - Turning
Press Left Stick - Turbo
Press Right Stick - Vehicle mode switch
Triggers - Accelerate forward/backward
Right bumper - Jump (double-jump to engage jetpack)
Left bumper - Scan
Haptic feedback?

## Menus
White screen with black, blocky elements.

- Splash
- Main menu
  - Continue
  - New Game
  - Miscellaneoys
  - Quit to Desktop
- Miscellaneous
  - Settings
  - Statistics
- Settings
  - Main volume slider
  - Push to toggle turbo
  - Controller vibration?
- Statistics
  - Time played
  - Distance traveled
  - Scans
  - Materials collected
  - Parts synthesized
- Game screen
- Game paused
  - Status
  - Synthesis
  - Resume game
  - Miscellaneous
  - Exit to Main Menu
  - Quit to Desktop
- Status
  - Coordinates
  - Heading
  - Altitude
  - Time

## Setting
An icy exomoon, similar in size to Triton, tidally locked in its orbit around the gas giant that fills its sky.
A secretive military expedition to the peripheries of alien space.
Barren, low gravity, high albedo.

### Landscape
Vast plains, rolling hills, mountains, cliffs, hoodoos, canyons, and craters.
Layers of noise are grouped and mixed into a heightmap.

### Atmosphere
It's tenuous.
The low density makes it nearly invisible and inaudible.
A faint blue glow hugs the horizon, producing a subsonic breeze.

## Mechanics
### Movement
#### Walking
#### Driving
### Scanning
Scanning allows pilots to interrogate the terrain within a semicircle ahead of them.
It casts rays in every direction and turns their distances into a series of tones.
Tones are emitted in groups from left-to-right, sequenced top-to-bottom.

### Materials
Materials spawn and persist in unexplored areas.
Each biome and depth has different compositions.
They're indicated by tones in the environment.
They're collected automatically on collision, displaying a notification, and leaving behind a breadcrumb.

#### Material types
- Common
  - Hydrogen
  - Nitrogen
  - Carbon
  - Oxygen
  - Silicon
- Metals
  - Aluminum
  - Iron
  - Copper
  - Silver
  - Gold
- Exotic
  - Neodymium
  - Uranium
  - Plutonium
- Xenotechnology
  - Artifact
  - Black Box

### Synthesis
Crafting mechanic which spends collected materials against a technology tree.
Each upgrade improves an aspect of the exosuit.
For simplicity, the synthesis screen only shows available upgrades.

##### Technology tree
- Actuators (increase on-foot sprint speed)
- Cargo Racks (carrying capacity - need to upgrade once per level to have storage capacity for other upgrades)
- Heatsinks (increase jetpack duration)
- Pistons (increase on-foot jump height)
- RCS (turning mid-air)
- Sensors (increase scanner or material detection radius?)
- Traction (increase vehicle acceleration)
- Vectoring (forward thrust when using jetpack)

## Sound design
### Player character
The player's breathing and heartbeat are always audible, oscillating in frequency and harshness with their stress level.

### Walking
Each stride is panned, pistons quietly moving, ending in a crunchy footstep.
The terrain varies from soft to hard with a noise field to produce various sounds.

### Driving
The engine produces a whine that responds to its thrust and resistance against the ground.
The ice cracks and crumbles like gravel as the player moves.
When drifting the cracking is loudest in the direction of movement.

### Environment
The wind produces a low rumble from west to east, responding quietly to your movements.
Occasionally the ice creaks, producing tonal pings and pongs.

### Materials
Materials produce periodic percussive pings.
Pitches are a random index, which accesses a frequency from the current soundtrack chord.
When collected a pleasant sound is emitted.

### Soundtrack
Each leap off the ground fades in an atmospheric soundtrack.
Three channels with four synths each, positioned binaurally in static directions.
The four synths allow seamless crossfading between time and Z-dimensions.
Over time the synths glide between chords.
As the player ascends higher above the surface, they pass through zones of random harmonics.
