# GDD
## Harmony Falls
An arcade shooter against endlessly falling notes.

### Controls
**Move left and right:** A, D, arrow keys, numpad 4 5, gamepad any stick
**Shoot:** W, up arrow, numpad up, space, gamepad triggers, gamepad face buttons
**Exit:** escape, backspace, start, select

### Mechanics
- World wraps like a cylinder
- 64 vertical progress bars along x-axis
- Game starts with random falls
- Falls spawn randomly at the top, weighted near existing ones
- Falls advance continuously toward bottom at a rate which accelerates over time
- Falls are random heights between 1-3 (screen heights) before they fall under the screen and can spawn again
- Player can move discretely on x-axis as fast as they can press, or half-speed by holding button
- Player can shoot at a rate as fast as they can press, or half-speed by holding button
- Projectiles move continuously upward until they hit a fall or top of screen
- Falls struck by projectiles are pushed back to the top
- Falls pushed beyond top are destroyed
- Colliding with falls ends the game
- Score accumulates per second, successful shots, and when destroying falls

### Graphics
- Canvas API, simple colorful rectangles
- 16 falls visible at once (90-degree FOV)
- Background and foreground color generators
  - 1D noise controls the background brightness / foreground saturation (pastels on slate, rainbows on black)
  - Background is a neutral slate to black
  - Foreground (bar colors) hue is controlled by 2D noise (x, time) along x-axis
  - Falls flash briefly when hit by projectiles
- Projectiles
- Particle effects when projectiles hit falls or player dies
- Player sprite, zooms when player spawns, jiggles when player moves, shrinks when player dies

### Sound design
- Falls
  - Tone for every fall visible on the screen, panned and attenuated
  - Tone selection is from a pentatonic scale spread over many octaves, from highest to lowest
  - Fall tone synths retrigger when player moves or when changing frequency
  - Buzz when impassable and will cause death, modulation controlled by height of fall remaining
- Shoot
- Projectile hit
- Fall destroy
- Player destroy

## Melody Heights
A colorful midnight stroll through Melody Heights, Montana.

### Controls
**Walk:** W/S/A/D, up/down arrows, numpad 8/5/4/6, click, right stick
**Turn:** Q/E, left/right arrows, numpad 7/8, mouse, left stick
**Look:** Page up/down, mouse, right stick
**Exit:** escape, backspace, start, select

### Mechanics
- Procedural terrain generation
  - Flatter plains and rolling hills from x < 0 (direction of moon)
  - Constantly growing mountains from x > 0
- Footsteps inserted into a quad tree

### Graphics
- WebGL with 3D graphics and camera with vertical look
- Background fades from dark pink at feet to black straight up
- Black triangles sample terrain ephemerally within 500m
- Rainbow triangles at footstep locations that glow white when emitting sound
- Large crescent moon above horizon
- Stars

### Sound design
- Footsteps
  - A soft binaural sound
  - Sample 2D noise fields (x,y) for parameters (color, duration, etc.)
- Wind
  - Sample 1D noise field (time) for parameters (color, gain, etc.)
- Footstep trail
  - Select all nearby footsteps
  - Arrange them into a timed sequence
  - Assign musical frequencies to each
  - Play sequenced sounds in world space
  - Trigger a sound on step?

## Secret Bread
A strange object that vibrates upon inspection.

### Controls
😅

### Keyboard controls
All letters and numbers are mapped to points on the surface of a sphere.
From left to right, the keys map to longitudes.
From top to bottom, the keys map to latitudes.
Hold one shift to press deeper, hold both to press even deeper.
Arrow keys control the frequency interpreter.

### Gamepad controls
Sticks control position of two pointers on opposite halves of the sphere.
Click stick or press bumper to touch.
Triggers control depth.
Directional pad controls the frequency interpreter.

### Mechanics
- Keep track of touch points (key or gamepad presses)
- Touches are 3D normal vectors with an extra depth component
- Depth is the time dimension of a 4D simplex noise field
- Time is always moving forward, but going deeper looks back in time by a maximum amount
- Frequency interpreter modes: chromatic, diatonic, major pentatonic, minor pentatonic
- Polyphony up to a certain number of ongoing notes, cancels oldest note
- Haptic / film grain noise field, summed from touches

### Graphics
- Circle oscilloscope in center of screen
- Notes represented by glowing triangles on the surface of an invisible sphere circumscribed by the oscilloscope
- Particle effects around notes?

### Sound design
- Notes are panned to 3D position of sphere
- Notes around back of sphere are filtered
- Notes are complex PWM synths with parameters controlled by 4D simplex noise fields
  - Root frequency based on interpreter, possibly with some glide
  - Detune, oscillator type, pulse width
  - AM depth, frequency, oscillator type
  - FM depth, frequency, oscillator type
  - Shaper mix
  - Attack qualities
