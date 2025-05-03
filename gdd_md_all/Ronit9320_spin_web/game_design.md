# Game Design Document: Boss Fight Game

## Game Overview
A multiplayer boss fight web game where players control two modifiable characters: a hunter and a boss. At the start of each match, one player is randomly selected to play as the boss while others play as hunters. Matches are time-based with 5 players per match.

## Core Mechanics

### Character System
- **Hunters**: Player-controlled characters with unique abilities
- **Bosses**: Powerful entities with special abilities and weaknesses
- Both hunters and bosses are considered "weapons" that can be modified and upgraded

### Match Structure
- 5 players per match
- One player randomly selected to be the boss
- Time-based matches (suggested duration: 5-10 minutes)
- Victory conditions:
  - Hunters win by defeating the boss within the time limit
  - Boss wins by surviving until time runs out or defeating all hunters

### Progression System
- In-game currency earned through matches
- Shop system for purchasing upgrades and modifications
- No permanent progression (no signup required)
- Session-based temporary progression

## Detailed Game Elements

### Hunter Characters
1. **Ranger**
   - Long-range attacks
   - Lower health
   - Abilities: Snipe Shot, Trap Placement, Evasive Roll

2. **Warrior**
   - Close-range attacks
   - Higher health
   - Abilities: Heavy Strike, Shield Block, Charge

3. **Mage**
   - Area-of-effect attacks
   - Medium health
   - Abilities: Fireball, Frost Nova, Teleport

4. **Rogue**
   - Fast attacks
   - Medium health
   - Abilities: Backstab, Smoke Bomb, Shadow Step

5. **Support**
   - Healing and buffs
   - Lower health
   - Abilities: Heal Pulse, Speed Boost, Protective Barrier

### Boss Characters
1. **Behemoth**
   - High health
   - Slow but powerful attacks
   - Abilities: Ground Slam, Rock Throw, Enrage
   - Weakness: Slow movement speed

2. **Shadow Fiend**
   - Medium health
   - Fast attacks
   - Abilities: Shadow Strike, Teleport, Summon Minions
   - Weakness: Vulnerable to area attacks

3. **Dragon Lord**
   - High health
   - Ranged attacks
   - Abilities: Fire Breath, Wing Gust, Tail Swipe
   - Weakness: Vulnerable underbelly

### Upgrade System
- **Weapon Modifications**: Change attack patterns, damage types, or effects
- **Ability Enhancements**: Reduce cooldowns, increase damage, add effects
- **Stat Boosts**: Increase health, damage, speed, or defense
- **Consumables**: One-time use items for healing or temporary buffs

### Shop System
- Currency: "Essence" earned from matches
- Categories:
  - Hunter Upgrades
  - Boss Upgrades
  - Consumables
  - Cosmetics (optional)

### Game Flow
1. Player enters the game (no signup required)
2. Joins matchmaking queue
3. Match found with 5 players
4. Random selection of boss player
5. Character selection phase
6. Match begins
7. Players fight until victory condition met
8. Results screen shows rewards
9. Players can spend currency in shop
10. Return to matchmaking or exit

## User Interface

### Main Menu
- Play Button (enters matchmaking)
- Shop Button
- How to Play Button
- Settings Button

### In-Game UI
- Health bars for all players
- Ability cooldown indicators
- Match timer
- Score/kill counter
- Mini-map (optional)

### Shop UI
- Currency display
- Categories for different item types
- Item cards with descriptions and costs
- Purchase confirmation

## Technical Considerations

### Multiplayer Implementation
- Room-based matchmaking
- Server authority for game state
- Client prediction for smooth gameplay
- Synchronization of player positions and actions

### Game State Management
- Match state (lobby, in-progress, ended)
- Player states (health, position, abilities)
- Boss selection and role assignment
- Shop inventory and player currency

## Art Style and Visual Direction
- Stylized 2D graphics
- Top-down or isometric perspective
- Distinct visual design for hunters vs bosses
- Clear visual effects for abilities and attacks

## Sound Design
- Background music for menu and matches
- Sound effects for abilities and attacks
- Victory/defeat sounds
- Shop and UI interaction sounds
