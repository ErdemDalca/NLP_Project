# Game Design Document: Hero Race 2

## Table of Contents

1. [Game Overview](#game-overview)
2. [Core Fun](#core-fun-and-selling-points)
3. [Core Features](#3-core-features-selling-points)
4. [Gameplay Mechanics](#4-core-mechanics-that-provide-core-fun)
5. [Map Design](#map-design)
6. [Heroes](#heroes)
7. [Items](#items)
8. [Game Modes](#game-modes)
9. [Victory Conditions](#victory-conditions)
10. [Art and Sound](#art-and-sound)
11. [Development Plan](#development-plan)
12. [Marketing](#marketing)
13. [Difficulty Flow](#difficulty-flow)

---

## 1. Game Overview

**Title:** Hero Race 2  
**Genre:** Racing / Action  
**Platform:** Dota 2 Custom Map  
**Player Count:**

-   10 (5v5 or 2v2v2v2v2 or FFA)
-   9 (3v3v3)
-   8 (4v4 or 2v2v2v2)
-   6 (2v2v2)
-   20 (10v10 or 5v5v5v5 or 2v2v2v2v2v2v2v2v2v2)
-   18 (3v3v3v3v3v3v3 or FFA)

**Target Audience:** Dota 2 players familiar with heroes and seeking a new gameplay experience that blends Dota's mechanics with fast-paced racing.

Dota Player Count: (2024 still peak 600k player)

-   [Steam DB: Dota2](https://steamdb.info/app/570/charts/#12y)
-   [Custom Game Stat](https://shimo.im/outlink/gray?url=https%3A%2F%2Fwww.customgamestats.com%2F%3FaccessToken%3DeyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MzA5NDU0NDQsImZpbGVHVUlEIjoicnAzT1Z5QmR4anRuQm1BbSIsImlhdCI6MTczMDk0NTE0NCwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjotODk1Mjg2Mzg0M30.ZslUldgjmq5kafqTTfQGZMtOO6rk7n90XzQlek1B10I)

**Summary:** Hero Race 2 is a competitive, action-packed racing game where teams race to the finish while using hero abilities to hinder opponents and gain advantages, blending Dota 2’s mechanics with Mario Kart’s chaos.

---

## 2. Core Fun / Experience

The core fun of _Hero Race 2_ is built around thrilling, team-based racing with dynamic hero abilities that make every race unpredictable. Players experience high-stakes choices, explore dynamic tracks, and improve team coordination.

**Core Fun Highlights:**

-   **Thrill and Excitement**: Fast-paced racing combined with hero abilities creates adrenaline-pumping action, especially in competitive moments.
-   **Unpredictable Outcomes and Replayability**: Every race feels unique due to random items, hero interactions, and dynamic maps, keeping players on their toes.
-   **Risk-Reward Decisions**: Making choices about when to use abilities or items adds depth and excitement, especially when it pays off.
-   **Team Synergy & Strategy**: Players experience satisfaction from collaborating with teammates to execute strategies, blending racing with tactical gameplay.
-   **Skill Progression:** Mastering racing and combat mechanics offers long-term achievement.
-   **Exploration and Discovery**: Dynamic maps encourage players to find shortcuts and adapt to changing obstacles, enhancing engagement.

---

## 3. Core Features (Selling Points)

**Core Features Overview:**

-   **Racing + MOBA Hybrid**: Integrates racing speed with ability-based gameplay, allowing players to support teammates and hinder opponents with tactical skill.
-   **Diverse Hero Abilities**: Each hero has a unique set of abilities that cater to various playstyles, encouraging experimentation and strategic decision-making.
-   **Dynamic, Evolving Tracks**: Maps feature procedural elements and shifting obstacles, creating fresh challenges in every race and ensuring replayability.
-   **Risk-Reward Abilities**: Many abilities and items require players to weigh risks and rewards, adding layers of tactical depth to gameplay.
-   **Variety of Items**: A wide range of randomly generated items provides boosts, defensive options, and offensive tools, keeping races unpredictable and exciting.
-   **Progression and Achievement Tracking**: Track individual and team performance stats, offering long-term engagement through progression and leaderboard ranking.

---

## 4. Gameplay Mechanics (that provide core fun)

-   **Racing + MOBA Hybrid:** Racing mixed with ability-based combat, allowing players to support teammates and disrupt enemies.

    -   **Core Fun Provided:** Thrill and Excitement, Unpredictable Outcomes and Replayability, Team Synergy & Strategy, Risk-Reward Decisions.

-   **Hero Abilities & Track Interactions**: Heroes have abilities that interact with the track, such as creating shortcuts or removing obstacles (e.g., trees), allowing players to influence the race environment.

    -   **Core Fun Provided**: Exploration and Discovery, Skill Progression.

-   **Coordinated Team Play**: Success relies on team coordination, with powerful ability combos and synchronized tactics rewarding teamwork and strategic planning.

    -   **Core Fun Provided**: Team Synergy & Strategy, Skill Progression.

-   **Dynamic and Adaptive Maps**: Procedural elements and track-specific obstacles change each race, requiring players to stay alert, adapt quickly, and find creative solutions in real time.

    -   **Core Fun Provided**: Unpredictable Outcomes and Replayability, Exploration and Discovery.

-   **Item Variety and Drop Mechanics**: Items acquired during the race offer boosts, defenses, or disruptive abilities, adding surprise elements. Dropping items upon defeat introduces strategic choice and risk in item handling.

    -   **Core Fun Provided**: Unpredictable Outcomes, Thrill and Excitement.

-   **High-Stakes Ability Timing**: Some abilities and items carry inherent risk, challenging players to make critical decisions about when to activate them for maximum impact, balancing potential rewards with possible drawbacks.

    -   **Core Fun Provided**: Skill Progression, Thrill and Excitement, Unpredictable Outcomes.

---

## 5. Map Design

-   **Track Layout:** Winding paths with varied terrains (grass, desert, ice).
-   **Obstacles:** Static and dynamic (trees, rocks, enemies, mazes, spider webs).
-   **Power-up Locations:** Specific spots with random items to collect.

---

## 6. Heroes

-   **Hero Selection:**

    -   Choose from unique heroes with racing and combat abilities.
    -   Modes:
        -   20-pick 1 mode
        -   All-random
        -   3-pick 1 mode
        -   Team leader BAN/PICK mode

-   **Example Heroes:**

    -   **Speedster:** High speed, phases through obstacles.
    -   **Tank:** High health
    -   **Support:** Heals teammates during the race.
    -   **Dragger** Hinder opponent.

-   **Hero Balance:** Adjust hero win rates close to 50% while retaining unique features. Base on win rate data collected for each version.

---

## 7. Items

-   **Power-ups item:**

    -   **Speed Boost:** Increases speed temporarily.
    -   **Traps:** Hinder Opponent.
    -   **Shield:** Provides short-term invulnerability.
    -   **Additional items...**

-   **Random Item Drops:** Earned by defeating enemies or environmental objects (consumables or equipment).

---

## 8. Game Modes

-   Player Counts:

    -   10 (5v5, 2v2v2v2v2, FFA), 9 (3v3v3), 8 (4v4, 2v2v2v2), 6 (2v2v2)
    -   20 (10v10, 5v5v5v5, 2v2v2v2v2v2v2v2v2v2)
    -   18 (3v3v3v3v3v3)

-   Mode Variants:
    -   **Ranked & Casual 5v5**
    -   **Repeat Hero Mode:** Allow choosing the same hero.
    -   **Mirror Hero Mode:** Both teams have the same heroes.
    -   **Clone Hero Mode:** Teams use identical heroes.
    -   **Die-to-Change Mode:** Players switch heroes upon death.
    -   **Item Shop Mode:** Players can purchase items.
    -   **Spring Festival Mode:** Super-powerful random items every 10s.
    -   **Player Place Obstacle Mode:** Player can place obstacle before the race start for each team.

---

## 9. Victory Conditions

-   **Team Score Mode:**

    -   Points based on finishing position (1st = 105 pts, 2nd = 90 pts, etc.).
    -   When any player reach the goal, timer start.
    -   -90 points for team if time runs out and the goal isn’t reached for each player.

-   **N-1 mode**

    -   N-1 player of the team reach goal win immediately
    -   N: team player count

-   **Alternate Modes:**
    -   **Transport Mode:** Protect an NPC racer.
    -   **Flag Mode:** Deliver a flag to the goal; flag drops upon death.
    -   **Relay Race Mode**

---

## 10. Art and Sound

-   **Visual Style:** Bright, colorful graphics matching the racing theme.
-   **Sound Effects:** Unique sounds for abilities, power-ups, and racing.
-   **Music:** Upbeat, Future Bass style, fitting the track themes.

---

## 11. Development Plan

### Phase 1: Prototype (MVP)

-   **Goal:** Build a Minimum Viable Product (MVP) or vertical slice to validate the core fun elements of gameplay.
-   **Focus Areas:**
    -   **Core Mechanics:** Establish racing and ability-based combat system.
    -   **Game Modes:** Implement a core game modes (e.g., Casual 5v5).
    -   **Hero Abilities:** Implement initial hero abilities to test gameplay balance and strategic options.
    -   **Playtesting:** Gather feedback on core fun, especially the thrill and replayability.
-   **Expected Outcome:** A playable MVP with a functional gameplay loop, capturing the main fun elements and setting the foundation for more complex features.

### Phase 2: Alpha

-   **Goal:** Expand the game’s content, polish gameplay, and begin balancing.
-   **Focus Areas:**
    -   **Hero Expansion:** Introduce additional heroes with unique abilities for varied playstyles.
    -   **Item System:** Integrate a range of items, including boosts and defensive items, to enhance tactical choices.
    -   **Procedural Maps:** Create simple map prototypes with basic dynamic elements (obstacles, shortcuts).
    -   **Map Complexity:** Enhance procedural elements, adding new obstacles and random event mechanics.
    -   **Game Modes:** Implement a few core game modes (e.g., Ranked 5v5, Repeat Hero Mode).
    -   **Initial AI Bots:** Introduce beginner-level bots for testing and player practice.
    -   **Playtesting & Iteration:** Test extensively, gathering feedback to fine-tune ability effects, item functionality, and game pacing.
-   **Expected Outcome:** A feature-rich alpha build with expanded heroes, modes, and maps that supports initial multiplayer testing and refinement.

### Phase 3: Beta

-   **Goal:** Polish the game, focusing on performance, stability, and deeper gameplay balance.
-   **Focus Areas:**
    -   **Advanced Balancing:** Adjust hero abilities, item drop rates, and map obstacles based on playtesting data.
    -   **Matchmaking & Difficulty Tuning:** Refine skill-based matchmaking and introduce difficulty progression, including AI with machine learning for advanced practice.
    -   **UI/UX Improvements:** Update HUD, scoreboards, and user flow to enhance player experience.
    -   **Additional Game Modes:** Finalize and test alternate modes (e.g., Transport Mode, Flag Mode).
    -   **Victory Conditions Testing:** Ensure that victory conditions work well across all game modes, adjusting rules for balanced outcomes.
    -   **Bug Fixing & Stability:** Prioritize performance optimization and fix bugs, preparing for the final launch.
-   **Expected Outcome:** A stable beta version that reflects the full game experience, with refined mechanics, complete modes, and optimized performance.

### Phase 4: Launch

-   **Goal:** Release the fully polished game with a solid content foundation and stability.
-   **Focus Areas:**
    -   **Final Balancing and Polish:** Conduct last adjustments based on beta feedback.
    -   **Marketing & Community Engagement:** Kick off marketing campaigns, set up social media channels (Discord / Twitter), and begin building a community.
    -   **Ongoing Post-Launch Support:** Prepare for post-launch updates, including new heroes, seasonal modes, and player-requested features.
-   **Expected Outcome:** A fully released version of _Hero Race 2_, with a strong initial player base and plans for continued content updates.

---

## 12. Marketing

-   **Business Model:**
    -   Sell hero skins (non-pay-to-win), offer "Buy Me a Coffee" donations, and consider a custom map game pass.
-   **Revenue Flow:**

    -   **Attract Custom Map Players:**
        -   Utilize seasonal events, leaderboards, and challenges to draw in new players.
    -   **Retain Players with Core Fun:**
        -   Keep players engaged through ongoing events, team-based challenges, and personalized progress rewards.
    -   **Encourage Small Purchases or Donations:**
        -   Offer tiered donation levels (Bronze, Silver, Gold) with exclusive perks like custom profile badges and leaderboard recognition.
        -   Highlight specific funding goals (e.g., “Support to unlock a new map!”) to make donations feel impactful.

-   **Continuous Updates:**
    -   **Regular Content Drops:**
        -   Add new heroes, tracks, items, and balance changes regularly to keep the gameplay fresh and exciting.
    -   **Player-Engagement Features:**
        -   Implement personal and collaborative goals (e.g., Hero Mastery, community unlocks) to incentivize frequent play and retention.

---

## 13. Difficulty Flow

-   **Progressive Difficulty:** Start with easy heroes for new players (0-30 rounds), granting extra HP or faster respawns. Remove bonuses after 75 rounds.
-   **Matchmaking:** Skill-based matchmaking to improve player retention.
-   **Balanced Teams:** Team shuffle based on player skill and win rates.
-   **Practice Bots:** AI bots (easy, normal, hard, and machine learning) for players to practice based on their skill.
-   **Assistance System:** Random assist items for low-position players, with temporary speed boosts buff awarded for kills when in lower positions (similar to Mario Kart).

### Player Journey and Difficulty Flow

| **Stage**                 | **Player Rounds** | **Difficulty Adjustments**                                        | **Features for Player Support and Engagement**                                                                                                                                                                                                                                                                          |
| ------------------------- | ----------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Beginner Phase**     | 0-30 rounds       | Easy heroes, extra HP, faster respawns                            | **Balanced Teams:** Team shuffle based on player skill and win rates. <br> **Matchmaking:** Skill-based matchmaking prioritizes balanced teams. <br> **Assistance System:** Random assist items and speed boosts for lower-position players. <br> **Practice Bots:** Easy and normal bots available for skill-building. |
| **2. Intermediate Phase** | 30-75 rounds      | Gradual removal of bonuses, introduction to regular respawn rates | **Balanced Teams:** Team shuffle based on player skill and win rates. <br> **Matchmaking:** Continues to adapt to increasing skill levels. <br> **Practice Bots:** Normal and hard bots available for improved competition.                                                                                             |
| **3. Advanced Phase**     | 75+ rounds        | No bonuses, high-skill matches                                    | **Skill-Based Matchmaking:** Places players in advanced pools. <br> **Assistance System:** Still provides situational boosts to players falling behind, ensuring a dynamic experience. <br> **Practice Bots:** Hard and machine learning-based bots to simulate advanced scenarios.                                     |

---

This document serves as the foundation for developing Hero Race 2, providing clear direction for gameplay, mechanics, and design. Updates may occur as development progresses.

```

```
