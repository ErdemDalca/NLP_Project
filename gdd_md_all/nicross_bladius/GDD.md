# Bladius
A roguelike game of gladiatorial combat with deckbuilding elements.

## Overview
TK

## Storyboard
1. Splash
  - Game title / version / author
  - Interact to begin
2. New game
3. Game over
  - Final score / stats
  - New game

## Game Loop
### Booster pack
- Earn new cards at the start of select rounds
- Randomly generated with rarities
- On new game, open the Starter Pack of 8 random cards:
  - 4 weapons
  - 1 shield
  - 1 armor piece
  - 1 boon
  - 1 bane
- On every 10 matches, open a Booster Pack of 3 random cards
- Forces deck reshuffle

### Draw Cards
- Deck of cards
- Draw 3 cards at the beginning of each match
- If 3 weapons draw, discard weakest, redraw indefinitely
- If 2 shields drawn, discard weakest, redraw indefinitely
- Randomly assigned to right/left hands
- Hands can be unarmed
- Can spend 1 gold to discard and redraw

### Combat
- Fight a wave of enemies scaled according to experience
- Independent control of both hands
- Sprint and dodge with stamina
- Use potions to recover health
- Can use dynamic targeting controls to locate enemies

#### Stamina
- Stamina is used when performing movement actions
- Sprinting drains it slowly
- Dodging uses 1/3 stamina
- Movement actions cannot be performed when stamina is too low
- Stamina recharges over time
- More points in the Endurance attribute increase the rate of recharge

#### Health
- Game is over when all health is lost
- Potions can be used during combat to restore health
- Potions can be purchased in the shop
- Healing mechanic
  - Healing is applied over time
  - When a potion is used, a counter is set equal to the amount needed to reach full health
  - The player health increases as the counter ticks to zero
  - More points in the Healing attribute increase the rate of healing

### Winnings screen
- Currency
  - Earn 1 per kill
- Experience
  - Earn 1 per match
- Time elapsed
- Damage dealt vs damage taken

### Level Up
- Shown when enough experience is gained to earn a level
- List of all attributes with one point to spend
- Ability to skip? Can you get higher rewards for being underleveled?

#### Experience curve
See: https://oeis.org/A000217
Sequence: 1, 3, 6, 10, 15, 21...
Or, f(L) = L + f(L - 1)
Use a generator?

### Store
- Purchase items with gold earned
- Health potion
  - Offered if below max number of health potions
  - Always 1 gold
- Cards
  - Three random cards are generated
  - Cost depends on strength of card
  - Card strengths scale with matches won
  - Can reroll for 1 gold

## Controls
### Gamepad
Move - Left Stick
Turn - Right Stick
Right Hand - Right Trigger
Left Hand - Left Trigger
Dodge - A
Heal - B
Sprint - Press Left Stick
Target Next - Right Bumper
Target Previous - Left Bumper
Haptic feedback on damage dealt and taken

### Keyboard
Move - WASD / Arrows / Numpad
Turn - QE / Arrows / Numpad
Right Hand - Left Alt / Right Ctrl
Left Hand - Left Ctrl / Right Alt
Dodge - Space
Heal - F / Z / /
Sprint - Shift
Target Next - R / X / .
Target Previous - T / C / ,

### Mouse
Turn - Mouse X
Right Hand - Right Click
Left Hand - Left Click
Dodge - Mouse 5
Heal - Mouse 4
Target Next - Mouse Wheel Up
Target Previous - Mouse Wheel Down

## Progression
### Stats
- Strength (base damage dealt)
- Defense (base damage absorption)
- Health (total health)
- Stamina (total stamina)

#### Shadow stats
- Stamina regen rate
- Potion healing rate
- Movement speed
- Attack speed
- Reflexes (enemies only)

### Cards
#### Weapons
- Stat bonuses for strength
- Types
  - Axes
    - High damage
    - Low attack speed
  - Daggers
    - Normal damage
    - High attack speed
    - Low range
  - Maces
    - High damage
    - Normal attack speed
    - Low range
  - Swords
    - Normal damage
    - Normal attack speed
  - Unarmed
    - Normal attack speed
    - No stat bonuses
    - Low range

#### Shields
- Active defense bonuses
- Absorbs damage when used successfully against attacks
- Made from increasingly rare materials
- Materials, in order of stat bonuses
  - Wooden
  - Leather
  - Bronze
  - Iron
  - Steel
  - Diamond

#### Armor
- Passive defense bonuses
- Made from increasingly rare materials
- Materials, in order of stat bonuses
  - Leather
  - Bronze
  - Iron
  - Steel
  - Diamond
- Types, in order of stat bonuses
  - Gauntlets
  - Pauldrons
  - Vambraces
  - Greaves
  - Helmet
  - Cuirass

#### Boons
- Passive effects during combat
- Boons have increasingly rare levels (e.g. Regeneration IV is stronger than Regeneration I)
- Types
  - Every stat (+1..4 points)
    - Vitality (health)
    - Endurance (stamina)
    - Might (strength)
    - Protection (defense)
    - Shadow stats?
      - Healing (potion healing rate)
      - Quickness (attack speed)
      - Swiftness (movement speed)
      - Vigor (stamina regen rate)

#### Banes
- Negative effects during combat that grant increased rewards at end of round
- Banes have increasingly rare levels (e.g. Poison IV is stronger than Poison I)
- Reward multipliers increase with level (e.g. x2, x3, x4)
- Types
  - Every stat (-1..4 points)
    - Wounded (health)
    - Fatigued (stamina)
    - Vulnerable (defense)
    - Weakened (attack)
    - Shadow stats?
      - Exhausted (move speed)
      - Dazed (attack speed)

## Expansion deck
- Environments
  - Generate unique soundscapes
  - Have effects that apply to player and all opponents
  - TBD
- Boons (that don't involve stat boosts)
  - Regeneration (gain health over time)
  - Restoration (gain stamina over time)
  - Vampirism (gain health on successful attack)
- Banes (that don't involve stat reductions)
  - Poisoned (lose health over time)
  - Encumbered (stamina does not recharge)

## Enemies
TK

## Sound design
- Breathing
  - Represents stamina system
  - Long deep to short harsh
- Heartbeat
  - Represents health system
  - Slow to quick
- Targeting system
  - Hard panning
  - Tracks target relative position
  - Filtered FM synth
  - Loudest when centered
  - Filtered when decentered
  - Heartbeat pattern, increasing as enemy health is low
- Footsteps
- Enemy sounds
- Attack sounds
  - Signifiers
  - Swings (panned brown noise which goes from hard left/right to center and back)
  - Hits
  - Blocks (muted hits + shield sound)
- Between rounds the game loop is always running
  - breathing/heartbeat filtered out but still audible, returning to resting rate
  - enemies are spawned in when new rounds begin
