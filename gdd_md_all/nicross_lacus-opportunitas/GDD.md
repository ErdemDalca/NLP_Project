# Lacus Opportunitas: Lunar lake trading simulator
Venture the lake, build a trading empire, and perform tricks in this submission to Games for Blind Gamers 4.

## Key features
- A scenic lake to explore
- Cargo to buy and sell
- Unique ports with supply and demand
- Perform tricks to earn extra points
- Purchase properties for bonuses?

## Game loop
- Start game docked at an agricultural port with 10 credits and 4 empty cargo slots
- Dock at port
  - Buy/sell materials
  - Purchase/upgrade properties
  - Leave
- Explore the lake
  - Jump waves?
  - Do tricks?
  - Navigate to ports

## Development phases
1. Basics (interface / water graphics and sounds / controls / movement and sounds)
2. Ports (world generation / port types / navigation / docking and undocking)
3. Economy (buy and sell goods / supply and demand / rare goods / gold)
4. Polish

#### Stretch phases
1. Tricks (go airborne / button sequences / sound design / earn bonus credits)
2. Building upgrades
3. Dolphins?
4. Quests?

## Mechanics
### Procedural generation
- World seed
- Time moves forward when undocked (to freeze prices in place)

### Lake
- 5 km diameter circle (max 5 minute travel time)
- Dynamic surface with big waves in the center
- 3D simplex, 8 layers (different octave/frequency per layer), multiplied by distance from center

### Ports
- 1-2 ports of each economy randomly placed around the lake
- Random name generator that combines unique prefixes and suffixes into location names
- Ports are undiscovered until visited, named Unknown Port
- Ports can be upgraded in various ways by spending gold

### Trading
- Player can buy goods from any port that supplies them, as long as their inventory is not full
- Player can sell goods at any port that demands them, as long as they have them
- Each good has a base price influences by port supply, demand, and upgrades
- Supply
  - A value from 0 to 1 which scales from 1x base price (low supply) to 0.75x base price (high supply)
  - With upgrades this value can reach 2 (0.5x base price)
  - Fluctuates over time for each good per port (e.g. 1d noise, 8 octaves, t/60/60)
- Demand
  - A value from 0 to 1 which scales from 1x base price (low demand) to 1.5x base price (high demand)
  - With upgrades this value can reach 2 (2x base price)
  - Fluctuates over time for each good per port (e.g. 1d noise, 8 octaves, t/60/60)

#### Economies
A list of all economy types, and the goods they buy and sell:

- Agricultural
  - Buy
    - Agricultural Equipment
    - Waste
  - Sell
    - Essentials
- Extraction
  - Buy
    - Extraction Equipment
    - Essentials
  - Sell
    - Copper / Iron / Gold / Platinum Ore
    - Waste
- Refinement
  - Buy
    - Copper / Iron / Gold / Platinum Ore
    - Refinery Equipment
    - Essentials
  - Sell
    - Copper / Iron / Gold / Platinum Bars
    - Waste
- Manufacturing
  - Buy
    - Copper / Iron / Gold / Platinum Bars
    - Essentials
  - Sell
    - Agricultural Equipment
    - Extraction Equipment
    - Refinement Equipment
    - Consumer Goods
    - Waste
- Luxury
  - Buy
    - Consumer Goods
    - Essentials
  - Sell
    - (Unique Rare Good)
    - Waste

#### Special goods
- Unique goods from cosmopolitan ports
- Bought by any port for (1 + distance from origin)x base price
- Names are the origin port name combined with a random noun (e.g. Brineport Dust, Watercastle Zest)
  - Dust
  - Elixir
  - Sauce
  - Spice
  - Zest

### Pricing ideas (multiply by 8?)
- Essentials - 1
- Waste - 1
- Ores
  - Copper - 2
  - Iron - 8
  - Gold - 32
  - Platinum - 128
- Metals - 8x base ore price
- Manufactured
  - Agricultural Equipment - 1024
  - Extraction Equipment - 512
  - Refinement Equipment - 256
  - Consumer Goods - 2048
- Rare goods - 512

#### Upgrades
- Players can purchase various upgrades for each port
- Port upgrades vary by economy type
- Upgrades can provide supply and demand bonuses (e.g. buy a factory)
- Upgrades can add supply or demand for stuff the economy doesn't normally produce or consume

##### Upgrade types
- Agricultural
  - Hydroponics +1-5 (increased supply of essentials)
  - Waste Treatment +1-5 (increased demand of waste)
- Extraction
  - +1-5 supply for each ore (also increases waste)
- Refinement
  - +1-5 demand/supply for each ore/metal (also increases waste)
- Manufacturing
  - +1-5 supply each equipment/goods (increase demand for metals and waste supply)
- Cosmopolitan
  - +1-5 consumer goods demand (more waste supply)
  - +1-5 rare good supply

### Boating
- 25 m/s max velocity
- Similar physics to Fishyphus, but can go airborne
- 2 m/s gravity when jumping
- Simply stop when hitting the shore with a collision sound?

#### Docking
- Each port has a dock zone around its tower
- Automatic docking within a certain radius, just get there and the menu opens
- Placed outside the radius, facing away, when undocking (click the menu undock button)

#### Tricks
- Performed in the air.
- Fail when landing if still in progress.
- Earn +floor(1/10 points) credits when docked.
- Toast when

0. Spin. +5 points for every 180 degrees
1. Short press button 1, release after 1/4 s. +10 points per trick
2. Long press button 2, release after 1/2 s. +25 points per trick
3. Hold button 3. +10(2s + log(2s+1)) points per trick

#### Controls
- Accelerate: W, arrow up, numpad 8, stick up, right trigger
- Brake: S, arrow down, numpad 5, stick down, left trigger
- Right: D, E, arrow right, numpad 9/6, stick right
- Left: A, Q, left arrow, numpad 7/4, stick left
- Target: F, Enter, Numpad Enter, gamepad A, d-pad down
- Trick 1: 1, numpad /, gamepad x, d-pad left
- Trick 2: 2, numpad *, gamepad y, d-pad up
- Trick 3: 3, numpad -, gamepad y, d-pad up
- Menu: Escape, Tab, Numpad 0, Start, Select

## Graphics
Minimal graphics represented by colorful circular moving dots, like pointillism.

- Sky
- Stars
- Sun
- Earth
- Terrain particles
  - Sample the terrain height over the life of the particle
  - Particles wrap as the player moves
  - Particles are colored based on whether water, structure, or landing zone
  - Water is in motion but land is stationary
- Lighthouse particles
  - Emitted when facing a lighthouse or targeted
  - Sort of like the destination guide in PSEP but in reverse

## Audio
- Water ambient
  - Brown noise
  - Granular like Fishyphus
- Water directional
  - Pink noise
  - 7-point audio like PSEP
- Wind ambient
  - White noise
  - Very soft
- Wind directional
  - Brown noise
  - Based on movement velocity
- Engine sound (like Fishyphus)
- Sound when target is engaged and disengaged (a simple on/off melody would work)
- Sun (sub bass, centered, with parameters, brighter when airborne)
- What if every port is a directional AM+FM sawtooth synth?
  - Distance and dot product control their main parameters
  - Each synth has a root frequency (2 octaves of pentatonic scale) and prime number (5,7,11,13,17 twice) picked randomly
  - Parameters
    - AM depth: -18 dB edge of lake -> -6 dB middle of lake
    - AM frequency: 1/prime facing away -> prime facing (lerpExp)
    - Color: 1 facing away -> 8 facing (lerpExp)
    - FM depth: 0 when not targeted, -600 cents facing away -> 0 cents facing
    - FM frequency: 0 when not targeted, -1200 cents far away -> 0 cents nearby
    - Gain: -24 dB far away -> -12 dB nearby
    - Slight detune based on relative velocity? +/- 10 cents
  - When docked, music fades out into port music (a three-note music system + sun)
- Blip when facing a port?
- Sounds when navigating menus
  - Focus
  - Click
  - Click disabled
  - Specific sounds for buying/selling?
- Trick audio cues?
  - Unique sequence cues per trick
  - Success / fail
  - Ca-ching when landing after a trick?

While docked, fade out the SFX volume all the way, music to half volume, remove current target

## User interface
- Game screen
  - Name of city currently facing, if any (top center)
  - Target information, if any (top left)
    - Name of port
    - Distance that updates visually in real-time, screen reader every 250m?
  - +N gold from tricks (bottom toast)
- Docking screen
  - title / focusable information about the system
    - Welcome to Port name
    - Economy type
  - Buttons
    - Buy
    - Sell
    - Properties
    - Leave Port
    - System (Main menu)
- Buy screen
  - Table of buttons, every good that the
  - Name, (very low, low, medium, high, very high) supply, cost
  - Click to buy
  - Disabled when inventory is full /
  - Toast when inventory is full?
- Sell screen
  - Table of buttons, every good that this port demands, buttons disabled if none in cargo
  - Name, (very low, low, medium, high, very high) demand, sell price
  - Click to sell
- Properties screen
  - A list of upgradable buildings
