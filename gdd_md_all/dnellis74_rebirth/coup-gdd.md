# 🎮 Game Title (Working Title): *Coup*

## 🎯 Core Game Loop (V1)

1. **Start**: Player escapes the coup and returns to their home state.
2. **Deploy**: Player sends lieutenants to other regions from a central map.
3. **Move**: Each turn, both player and despot move units across a map (turn-based or real-time with pausing).
4. **Recruit**: When a lieutenant enters a town, if the town matches their “recruit condition” (e.g., origin, culture, or item carried), it flips to your side.
5. **Compete**: The despot spreads influence via their own forces at the same time.
6. **Win/Loss Conditions**:
   - **Victory**: Control a majority of states or key cities.
   - **Defeat**: Despot controls too much territory or captures your lieutenants.

---

## 🗺️ Map Design

- Abstract or stylized national map divided into:
  - **States/Provinces**: Larger areas for regional control.
  - **Towns/Cities**: Individual nodes that can be flipped.
  - **Roads & Terrain**: Optional terrain modifiers (e.g., mountains = slow, airports = fast travel).

---

## 🧑‍🤝‍🧑 Units & Characters

### Player Units

- **You (the escaped governor)**:
  - Can’t be lost.
  - Acts as central command unit from home state.

- **Lieutenants**:
  - Unique traits (e.g., charisma, shared hometown with certain cities, item-carrying ability).
  - Limited movement per turn.
  - Some can “carry” items that help recruit specific towns.

### Despot Units

- AI-controlled.
- March outward from the capital.
- Flip towns using brute force, propaganda, or loyalty.

---

## ⚙️ Recruitment Mechanic (Discrete Flip)

- Each town has a **"key"** requirement:
  - Specific lieutenant.
  - Item (e.g., old flag, local heirloom).
  - Trait (e.g., same faction, race, class).

- When a matching unit enters the town:
  - **Instant Flip** to your side.
  - Triggers a small recruitment bonus (e.g., gain new lieutenants, resources).

---

## 🧠 AI & Strategy

- Despot chooses between:
  - Strategic choke points (roads, capitals).
  - Rapid expansion (blitz towns).
- Adaptive AI optional in later builds (responds to your actions).

---

## ⏱️ Turn & Time System

- **Turn-Based** (initially): Each turn is one day or week.
- Optional real-time or hybrid in future versions.

---

## 🧪 Tech Demo MVP Requirements

- [ ] Static map with 10–15 towns.
- [ ] 2–3 lieutenants with distinct recruitment conditions.
- [ ] Turn-based movement and basic fog-of-war.
- [ ] Towns flip when conditions met.
- [ ] Despot AI spreads in a predictable or semi-random pattern.
- [ ] Simple UI showing territory control.

---

## 🌱 V2 Ideas (Narrative Layer)

- Dialogues when entering towns.
- Branching choices with consequences.
- Dynamic relationships with other lieutenants.
- Town loyalty affected by decisions or events.
