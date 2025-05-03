# AoT: Utopia

# Attack on Titan: Utopia

## Game Design Document

This document provides a detailed description of the game elements and gameplay. It does not contain any implementation or coding details.

---

## Outline

- [Intro](#intro)
- [Space Setting](#space-battle-setting)
- [Enemy Characters](#enemy-characters-titans)
- [Friendly Pieces](#friendly-pieces-weapons)
- [Game Rules](#game-rules)
- [Game Flow](#game-flow)

---

## Intro

**Attack on Titan: Utopia** is a one-player, endless tower defense game inspired by the hit anime *Attack on Titan*. The story of the anime revolves around how titans, gigantic humanoid creatures, emerged one day and wiped out most of humanity. The few surviving humans fled and hid behind three great walls that provided safe haven from the titan threats: Wall Maria (outer wall), Wall Rose (middle wall), and Wall Sina (inner wall).

This game takes place in an imaginary scenario where the titans breached their way through Wall Maria and reached the northern border of Wall Rose at the **Utopia District**. The human forces stationed in Utopia engage the titans in battle for one last hope of preventing the titans from breaching Wall Rose. The humans fight by deploying different types of **Anti-Titan weapons** to stop the onslaught and keep Utopia’s (and Wall Rose’s) walls safe.

> **Tower Defense Games**: A type of game where the player controls a base, defending it from incoming enemies by deploying weapons/tools.
>
> **Endless Mode**: The game has no winning condition; the player continues playing to defeat as many enemies as possible.

---

## Space (Battle) Setting

The battlefield is divided into multiple **lanes**, each with:

1. **A part of the wall** to be defended, with HP that decreases when attacked. If destroyed, the lane becomes a **lost lane**.
2. **Weapons** deployed by the player.
3. **Titans** marching toward the wall. Each titan has HP and moves closer every turn.

Each lane has a **danger level** based on the number and types of titans inside it.

In the player’s base, the player can:
- View available weapons and purchase/deploy them.
- Monitor gathered resources, score, remaining wall HP, titan HP, and distances.
- See the order of approaching titans, which will spawn in upcoming turns.

The battle progresses through **three phases**:
1. **Early**
2. **Intense**
3. **Grumbling**

---

## Enemy Characters (Titans)

All titans share the following stats:

| Type | HP  | Damage | Height | Speed | Resources | Danger Level | Special Trait |
|:----:|:---:|:------:|:------:|:-----:|:---------:|:------------:|:-------------:|
| Pure Titan  | 100 | 15 | 15 | 10 | 10 | 1 | None |
| Abnormal Titan | 100 | 20 | 10 | 15 | 15 | 2 | Attacks twice per turn |
| Armored Titan | 200 | 85 | 15 | 10 | 30 | 3 | Takes only 25% of damage received |
| Colossal Titan | 1000 | 100 | 60 | 5 | 60 | 4 | Gains +1 Speed per movement |

> **Distance Unit**: A fictional unit used in this game.

---

## Friendly Pieces (Weapons)

All weapons share the following stats:

- **Damage**: Attack power.
- **Price**: Cost to purchase and deploy.

Some weapons, like the **Volley Spread Cannon**, have additional stats:
- **Min Range**: Minimum attack range.
- **Max Range**: Maximum attack range.

### Weapon Types

| Weapon Name | Price | Damage | Min Range | Max Range |
|:-----------:|:-----:|:------:|:---------:|:---------:|
| Piercing Cannon | 25 | 10 | - | - |
| Sniper Cannon | 25 | 35 | - | - |
| Volley Spread Cannon | 100 | 5 | 20 | 50 |
| Wall Trap | 75 | 100 | Proximity Trap | - |

### Attack Actions

| Weapon Type | Attack Behavior |
|:-----------:|:---------------:|
| Piercing Cannon | Attacks the closest 5 titans in the lane. |
| Sniper Cannon | Attacks the closest titan in the lane. |
| Volley Spread Cannon | Attacks all titans within min-max range. |
| Wall Trap | Attacks one titan that reaches the walls. |

---

## Game Rules

### Winning & Losing Conditions

- **No winning condition** – the player plays until all lanes are lost.
- **Losing condition** – all wall parts are destroyed.
- **Final score** – determined by the player’s accumulated resources.

### Titan Movement

- Each turn, **titans move** forward based on their **speed**.
- Colossal titans **gain +1 Speed** per movement action.

### Attack Actions

| Action Type | Description |
|:----------:|:-----------:|
| **Titans Attack** | Titans attack walls if distance = 0. |
| **Weapons Attack** | Weapons attack titans according to their attack patterns. |

### Turn Actions

| Step | Action |
|:----:|:------:|
| 1 | Player buys/deploys weapon or passes. |
| 2 | Titans move. |
| 3 | Weapons attack. |
| 4 | Titans attack. |
| 5 | New titans spawn. |
| 6 | Battle phase updates. |

---

## Game Flow

The game follows a continuous loop where the player must strategically defend against increasingly difficult waves of titans.

![Flow Chart](https://github.com/user-attachments/assets/8db32f3e-bd87-4366-820f-dfe445df0a90)

---
