**Game Design Document: Space Base Under Siege (Tower Defense Game)**

---

## **Overview**
**Space Base Under Siege** is a sci-fi tower defense game where players defend their base from waves of attacking alien forces. The game features three core tower types, each with specializations, and an upgradeable home base that provides strategic benefits between waves.

---

## **Gameplay Mechanics**
### **Enemies**
Enemies come in three categories, each with different attributes that scale over time:

| **Enemy Type**   | **Base HP** | **Speed** | **Armor** | **Resistances** | **Currency Drop** |
|-----------------|------------|---------|--------|-----------------|----------------|
| **Swarmers** (Small) | 50 HP | 🚀 Very Fast | ❌ None (0% DR) | ❌ No resistance to slows | 5 credits |
| **Brutes** (Medium)  | 150 HP | 🏃 Average | 🛡 Light (10% DR) | Moderate resistance | 15 credits |
| **Juggernauts** (Large) | 300 HP | 🐢 Slow | 🏰 Heavy (25% DR) | 🛑 High resistance | 30 credits |

**Scaling Rules:**
- Swarmers scale at **1.15x HP per level**
- Brutes scale at **1.2x HP per level**
- Juggernauts scale at **1.3x HP per level**
- Armor and resistances **remain fixed** at their base values
- Currency drop scales as `(Base HP / 10) + (Level * 2)`

---

### **Towers**
Each tower starts as one of three core types and can specialize into different variants.

#### **Tower Types**
| **Tower** | **Type** | **Base Damage** | **Range** | **Rate of Fire** |
|----------|-------------|------------|--------|--------------|
| **Plasma Cannon** | Direct Damage | 25 | 200 | 1.5 sec |
| **Tesla Disruptor** | AOE | 10 | 150 | 1.0 sec |
| **Graviton Manipulator** | Debuff | 0 | 175 | 2.0 sec |

#### **Tower Specializations**
Each tower can specialize into **one of three paths**, allowing it to mimic aspects of the other tower types.

| **Tower** | **Specialization** | **Effect** |
|----------|----------------|--------------------------------------------|
| **Plasma Cannon** | Plasma Overload | **Massive single-target damage increase** (x2 damage, slower ROF) |
|  | Explosive Shot | **Adds splash damage** (small AOE radius) |
|  | Graviton Rounds | **Shots now slow enemies** (30% movement reduction) |
| **Tesla Disruptor** | High Voltage | **Increased AOE damage and chain range** |
|  | Focused Lightning | **Converts into a high burst, single-target tower** |
|  | Electro-Gravitic Pulse | **Adds a slow effect to electrocution** (20% reduction) |
| **Graviton Manipulator** | Event Horizon | **Doubles slow duration and effect** (50% slow for 4s) |
|  | Singularity Collapse | **Deals AOE damage over time** (5 damage/sec, 3s) |
|  | Kinetic Railgun | **Becomes a direct-damage railgun** (40 damage, faster ROF) |

---

### **Home Base Mechanics**
The base is **not** just a static objective. It provides strategic advantages between waves.

#### **Base Attributes & Effects**
| **Attribute** | **Effect on Base** | **Effect on Towers** |
|--------------|--------------------|----------------------|
| **Shields** ⚡ | Determines how much repair power is available after each wave. | The more shields, the more towers can be repaired. |
| **Energy/Power** 🔋 | Boosts base’s energy output. | **Increases tower rate of fire** (stacks with tower upgrades). |
| **Hit Points (HP)** 🏰 | Increases total base HP, making it harder to destroy. | **Increases tower resistances**, reducing incoming damage. |

#### **Upgrade Scaling**
Each base attribute can be upgraded at an increasing cost:

| **Upgrade Type** | **Level 1** | **Level 5** | **Level 10** |
|-----------------|------------|------------|-------------|
| **Shields** | 100 Repair Points | 250 Repair Points | 600 Repair Points |
| **Energy (Fire Rate Boost)** | +5% Rate of Fire | +15% Rate of Fire | +30% Rate of Fire |
| **HP (Tower Resistance Bonus)** | 2% DR | 6% DR | 12% DR |

Upgrade costs follow **an exponential formula**: `Base Cost * (1.3 ^ Upgrade Level)`

---

## **Game Economy & Progression**
- Enemies drop **currency** that is used to upgrade **towers and the home base**.
- Each wave increases **enemy health and rewards**.
- Towers become stronger **through RPG-style specialization**.
- The home base **buffers player weaknesses** and enhances **tower effectiveness**.

---

## **Final Thoughts**
This game design allows for **strategic depth while keeping mechanics streamlined**. The **specialization system** ensures **tower builds feel unique**, while **the home base provides global upgrades** to support different playstyles.

🚀🔥 This is going to be an **epic tower defense experience!**


