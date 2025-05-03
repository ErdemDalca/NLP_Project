# Hieretic: Game Design Document

> [!IMPORTANT]
> This document serves as the authoritative reference for Hieretic's game mechanics and systems. All game features must align with these specifications.

## Core Game Systems

### Resource System

| Resource | Symbol | Generation | Max Pool | Primary Use           |
| -------- | ------ | ---------- | -------- | --------------------- |
| Material | 🜔      | +1/turn    | 10       | Physical entities     |
| Mind     | 🜕      | +1/turn    | 10       | Psychological effects |

> [!NOTE]
> Most cards require mixed resources, creating natural strategic tension in resource allocation.

### Player Stats

| Stat            | Value | Notes                   |
| --------------- | ----- | ----------------------- |
| Starting Health | 30    | Damage is NOT mitigated |
| Hand Size       | 5     | +1 card per turn        |
| Field Slots     | 3     | Per layer               |
| Max Resources   | 10    | Per type                |

### Card Stats

| Stat    | Symbol | Range | Notes               |
| ------- | ------ | ----- | ------------------- |
| Attack  | 🜂      | 1-3   | Base value          |
| Defense | 🜄      | 1-4   | Damage reduces this |

## Cost Structure

### Single Resource Cards

| Cost     | Power Level | Typical Stats  | Frequency |
| -------- | ----------- | -------------- | --------- |
| 1🜔 or 1🜕 | Basic       | 1🜂/2🜄 or 2🜂/1🜄 | 20%       |
| 2🜔 or 2🜕 | Moderate    | 2🜂/2🜄          | 15%       |
| 3🜔 or 3🜕 | Strong      | 2🜂/3🜄 or 3🜂/2🜄 | 10%       |

### Mixed Resource Cards

| Cost         | Power Level | Typical Stats  | Frequency |
| ------------ | ----------- | -------------- | --------- |
| 1🜔1🜕         | Enhanced    | 2🜂/2🜄 + Effect | 25%       |
| 2🜔1🜕 or 1🜔2🜕 | Strong      | 2🜂/3🜄 + Effect | 20%       |
| 2🜔2🜕         | Powerful    | 3🜂/3🜄 + Effect | 10%       |

> [!TIP]
> Mixed resource cards should have effects that justify their more demanding costs.

## Game Flow

### Turn Structure

1. **Start Phase**

   - Gain 1🜔 and 1🜕
   - Draw 1 card

2. **Main Phase**

   - Play cards
   - Activate effects
   - Switch layers

3. **Combat Phase**

   - Declare attacks
   - Resolve combat

4. **End Phase**
   - Resolve end effects
   - Check win conditions

> [!IMPORTANT]
> Players must explicitly end each phase, ensuring intentional play patterns.

### Combat Resolution

1. Attacker declares target
2. Defender may activate responses
3. Compare 🜂 vs 🜄
4. Apply damage
5. Trigger post-combat effects

## Layer System

### Material Layer (🜔)

- Physical entities and effects
- Direct damage focus
- Unit-to-unit combat

### Mind Layer (🜕)

- Psychological effects
- Control mechanics
- Indirect damage

> [!NOTE]
> Units can only attack within their layer unless modified by effects.

## Card Types

### Units

```
┌────────────────┐
│ Name        1🜔 │
│ ═══════════════│
│     Art        │
│                │
│ ───────────────│
│ Effect text    │
│                │
│         2🜂/2🜄 │
└────────────────┘
```

### Effects

```
┌────────────────┐
│ Name      1🜔1🜕│
│ ═══════════════│
│     Art        │
│                │
│ ───────────────│
│ Effect text    │
│                │
└────────────────┘
```

### Rituals

```
┌────────────────┐
│ Name      2🜔2🜕│
│ ═══════════════│
│     Art        │
│                │
│ ───────────────│
│ Effect text    │
│ Duration: X    │
└────────────────┘
```

## Win Conditions

1. **Primary**

   - Reduce opponent health to 0
   - Opponent cannot draw cards

2. **Special**
   - Specific ritual completions
   - Card-defined conditions

## Game Phases

### Early Game (Turns 1-4)

- Resource building
- Board establishment
- Layer control

### Mid Game (Turns 5-9)

- Strategic pressure
- Resource manipulation
- Cross-layer threats

### Late Game (Turns 10+)

- Win condition execution
- Resource maximization
- Combination plays

> [!TIP]
> Games should typically conclude between turns 12-15, with clear strategic progression through each phase.

## Effect Categories

| Type       | Primary Layer | Description           |
| ---------- | ------------- | --------------------- |
| Damage     | 🜔             | Reduce health/defense |
| Control    | 🜕             | Affect unit behavior  |
| Buff       | Both          | Enhance stats         |
| Debuff     | Both          | Reduce stats          |
| Transform  | 🜔             | Change unit type      |
| Manipulate | 🜕             | Affect card locations |

## Balance Guidelines

### Unit Stats by Cost

| Cost | 🜂 Range | 🜄 Range | Effect Power |
| ---- | ------- | ------- | ------------ |
| 1    | 1-2     | 1-2     | Minor        |
| 2    | 2-3     | 2-3     | Moderate     |
| 3    | 2-3     | 2-4     | Strong       |
| 4+   | 3-4     | 3-4     | Powerful     |

### Effect Power by Cost

| Cost | Direct Damage | Control Duration | Buff Amount |
| ---- | ------------- | ---------------- | ----------- |
| 1    | 1             | 1 turn           | +1          |
| 2    | 2             | 2 turns          | +2          |
| 3    | 3             | 2 turns          | +2/+2       |
| 4+   | 4             | 3 turns          | +3/+3       |

> [!IMPORTANT]
> All effects must be clearly resolvable with minimal rules interpretation required.

## Deck Construction

### Requirements

- Minimum 30 cards
- Maximum 3 copies per card
- At least 10 units

### Recommendations

- 40-50% units
- 30-40% effects
- 10-20% rituals
- Balance between 🜔 and 🜕 costs
