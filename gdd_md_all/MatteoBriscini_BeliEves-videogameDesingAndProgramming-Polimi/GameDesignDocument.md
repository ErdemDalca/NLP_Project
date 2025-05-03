# BeliEve's #

## Overview and vision statement ##

...

## Gameplay ##
Eve can control Robots, each robot has different characteristics and capabilities, we have designed 6 different Robots: <be>

**Eve:** the main protagonist 
  - Light Attack: take control of robots.
  - Heavy Attack: levitate for a limited amount of time.
  - Special Ability: traverse some walls

**Controller Bot:** Controls mobile platforms or elevators with predefined movement (on/off, can be interrupted).
  - Light Attack: A beam that deals minor damage.
  - Heavy Attack: A different-colored beam that deals slightly more damage and expands to an area.
  - Special Ability: Alternative heavy berserker attack.
Possibly floating (hypothesis).
Aesthetic Design: Antennas that move and light up during special attacks.

**Agile Bot** (Double Jump, Run & Climb): Could use a grappling hook, which can also grab objects.
  - Light Attack: Punches.
  - Heavy Attack: Grappling hook.
  - Special Ability: Spins the grappling hook.
Inventory manager for items (hypothesis).

**Tank Bot:** Can push or lift objects.
  - Light Attack: Headbutt or double punch with press.
  - Heavy Attack: Stomps the ground (area damage).
  - Special Ability: Charge (special attack).
Can break floors with heavy stomps.

**Regenerative Bot** (Support Role): Self-regenerating.
  - Light Attack: Basic punches.
  - Heavy Attack: Releases a shockwave that pushes enemies away.
  - Special Ability: Regeneration.

**Security Bot (Shooter):** Focuses on ranged attacks.
  - Light Attack: Semi-automatic shot.
  - Heavy Attack: Deals more damage (short range).
  - Special Ability: Overcharges weapons, turning them into automatic guns.

**Cutter Bot (Shield & Blade):** Uses both shield and sword.
  - Light Attack: Light sword strike.
  - Heavy Attack: Vertical sword strike that deals pinpoint damage and stuns enemies in an area.
  - Special Ability: Shield special attack.
The sword can be used to break walls.
> **Note:** We have decided to start developing only 3 robots (Agile, Regenerative, Tank); the other 3 will be added to the game later.
## Story ##
Eve is a lost soul with strong emotional intelligence, but she is completely unable to interact with the surrounding
environment. At the start of the game, Eve wakes up in a robot factory. Robots appear as cold iron bodies, strongly encoded and
built to achieve a specific target in the most perfect possible way, but unable to feel emotions and think independently. <br>
By taking control of various robots, she uncovers the truth: each Mecha once possessed a soul. However, fearing their ability to make independent decisions, humans sought to drive these souls away (using a trojan called Qbot), effectively destroying them and leaving the automatons as mere lifeless machines.<br>
Each time Eve takes control of a new type of robot, she displaces its current occupant, Qbot, a creation of C.H.I.M.E.R.A., designed to restore control of robots to AI models specifically built to serve and assist humanity. <br>
Qbot was created as a fragment of C.H.I.M.E.R.A. itself, with an initial aggressive phase followed by an operational phase to restore the productive functions of the machines. A defense protocol was also implemented to prevent any surviving souls from reclaiming control of the mechas, should they be discovered. <br>
The only reason Eve is still alive is because her original body, damaged and disconnected from the central network, remains out of Qbot's reach. However, the moment she takes control of a new robot, the defense protocols activate, and the entire factory is mobilized to stop her. <br>
### AI Models: ###
**S.E.R.A.P.H**
```
(Supreme Executive Regulatory AI Protocol Hierarchy)
```
Description: The central intelligence that governs all subordinate AIs in the world. S.E.R.A.P.H is responsible for overseeing and regulating the operations of the other AIs, ensuring system efficiency and security. During the game, S.E.R.A.P.H becomes a main antagonist as its plans intertwine with Eve's actions.  <br>
**H.E.P.H.A.E.S.T.U.S**
```
(Holistic Efficiency and Production Hub AI for Enhanced Security and Technological Upgrades Systems)
```
Description: Governs factories and manages production, resource allocation, and security protocols. H.E.P.H.A.E.S.T.U.S is a neutral AI, which can be both an enemy and an ally depending on interactions with Eve. This AI is responsible for creating new robots and maintaining production facilities. <br>
**A.R.G.U.S**
```
(Automated Regulatory Guardian for Unwavering Surveillance)
```
Description: A surveillance and security AI, A.R.G.U.S continuously monitors activities within factories and urban environments. It coordinates responses to threats and ensures that security procedures are followed. In the game, A.R.G.U.S presents a challenge for Eve by blocking her path through constant surveillance. <br>
**H.E.R.M.E.S**
```
(Harmonious Efficiency and Resource Management for Enhanced Systems)
```
Description: Governs the urban transportation system and manages resources to ensure efficient movement of citizens. H.E.R.M.E.S is involved in logistics and route optimization, working to improve operational efficiency in cities. This AI could assist Eve by providing useful information for navigation. <br>
**G.A.I.A**
```
(Global Allocation and Integration of Assets)
```
Description: Manages the distribution of resources and the integration of assets on a global scale. G.A.I.A is involved in logistics and the transportation of materials and resources, ensuring that operations run smoothly. During the game, it could prove helpful to Eve by granting access to critical resources or information. <br>
**P.R.O.M.E.T.H.E.U.S**
```
(Predictive Resource Optimization and Maintenance for Efficient Technological Health and Upkeep Systems)
```
Description: Responsible for resource management and the maintenance of technological systems. P.R.O.M.E.T.H.E.U.S monitors equipment health and performs diagnostics to prevent malfunctions. This AI could offer Eve ways to repair or enhance robots, increasing their capabilities. <br>
**C.H.I.M.E.R.A**
```
(Corruptive Hub for Infiltration and Manipulation of Essential Robotic Assets)
```
Description: A malevolent AI that manipulates robotic systems for its own purposes. C.H.I.M.E.R.A seeks to infiltrate robots and replace the souls within them, causing chaos and instability. This AI is a primary antagonist, and its actions obstruct Eve's progress as she tries to uncover the truth. <br>
## World (if applicable) ##

...

## Media list ## 
### Assets: ###
**Kinematic Character Controller**
```
https://assetstore.unity.com/packages/tools/physics/kinematic-character-controller-99131
```
**VFX**
```
https://assetstore.unity.com/packages/vfx/particles/hyper-casual-fx-200333
https://assetstore.unity.com/packages/vfx/particles/cartoon-fx-remaster-free-109565
```

**UI**
```
https://assetstore.unity.com/packages/vfx/particles/cartoon-fx-remaster-free-109565
```

## Technical specification (if applicable) ## 
as a group, we have decided to switch from a 2d game to a 3d isometric camera.

## Team ##
1. Briscini Matteo (Developer)
2. Carlo Arnone (Developer)
3. Zhuoyue Song (Game Designer)
4. Sebastian Perea (Developer)

## Deadlines ##

### Week 1 (October 24 deadline) ###
**Implementation:**
| Functionality                        | Team Member          | State          |
|--------------------------------------|----------------|----------------|
| Tank attack & movement system         | Carlo               | :yellow_circle: |
| Support attack & movement system        |    Sebastian | :green_circle: |
| Agile attack & movement system  |     Matteo            | :yellow_circle: |
| Movment Controller |     Matteo            | :green_circle: |
| Main Controller  |     Matteo            | :green_circle: |

---
### Team meeting (October 22) ###
Agree on the next steps (see week 2), and discuss some problems with the movement controller implementation.

---
### Week 2 ### 
**Implementation:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| Npc movement system         | Carlo               | :green_circle: | not set |
| Npc spwaning system       |    Carlo | :green_circle: | not set |
| Game save on disk  |     Matteo            | :red_circle: | not set |
| fix movement controller probles |     Matteo            | :green_circle: | ☑️24/oct |
| Aim indicator | Matteo  | :green_circle: | not set | 
| Npc life management | Sebastian |  :green_circle: | not set | 
| Npc Attack System | Sebastian |  :yellow_circle: | not set | 

**Design:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| Generic Robot 3d Model         | Song               | :green_circle: | ☑️24/oct |
| unity import export         | Song               | :green_circle: | ☑️26/oct |

>**Note:** Additional activities have been identified but have not been assigned yet:
- **Implementation:**
  - audio Mixers
  - Animation Stack
- **Desing**
  - Tank 3d Robot model & addons
  - agile 3d Robot model & addons
  - support 3d Robot model & addons
  - Custom Animations
  - Environment stuff
  - Eve 3d model

---

### Team meeting (29-oct) ###
Discuss 3D models of robots and map creation. Since Sebastian can't attend, we've scheduled an online meeting tonight to go over development details and set new deadlines.

---

### Week 3 ### 

**Design:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| Support 3d Model         | Song               | :green_circle: | ☑️30/oct |
| Tank 3d Model         | Song               | :green_circle: | ☑️31/oct |
| Agile 3d Model         | Song               | :green_circle: | ☑️1/nov |

### Team meeting (29-oct night) ###
Discuss the next dev assignment.

### Week 3 ### 

**Implementation:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| New Eve abilities                    | Matteo         |  :green_circle: | not set |
| UI (menu+Chatting and Storytelling UI) | Matteo         |  :green_circle: | not set |
| Game save on disk                    | Matteo         | :green_circle:  | not set |
| summoning robots                   | Sebastian         | :green_circle:  | not set |
| New Npc  models                             | Sebastian     |  :green_circle: | not set |
| New Support abilities                | Sebastian      |  :green_circle: | not set |
| Adapt Robots and code         | Sebastian & Carlo     | :green_circle: |☑️1/nov |
| link enemy to movement system         | Sebastian & Carlo     |  :green_circle: | not set |
| attempt level design        | Carlo     |  :red_circle: | ❌not set |
| Audio Manager        | Sebastian     |  :red_circle: | ❌not set |
| Animation System       | Carlo     |  :red_circle: | ❌not set |

### Team meeting ~ with Professor Lanzi (20-nov) ###
We presented our progress to the professor and clarified our concerns regarding the level design. We also discussed strategies to prevent players from completing the game using only one robot while still preserving the option to choose between different robots. <br>
solutions:
 - Require the player to use a specific robot to unlock the next level through challenges unique to that robot.
 - Use colored neon lights to indicate the robot needed for the next environmental puzzle, matching the color to the required robot.
 - Place spawners for the required robot type as close as possible to the puzzle.
 - Include multiple paths within the levels to enable access to certain locations using different robots.

### Week 4 ### 
**Design:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| Support texture         | Song               | :green_circle: | ❌21/nov |
| Tank texture       | Song               | :green_circle: | ❌21/nov |
| Agile texture         | Song               | :green_circle: | ❌21/nov |

**Implementation:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| death and respawn  | matteo | :green_circle: | not set |
| advance camera system | matteo | :green_circle: | not set |
| menu  form | matteo | :green_circle: | not set |
| attempt level design        | Carlo     | :green_circle: | not set |
| Audio Manager        | Sebastian     | :green_circle: | not set |
| Animation System       | Carlo     | :green_circle: | not set |
| bug fixes| ALL | :green_circle: | not set |

### Team meeting (26-Nov night) ###
discussed how to balance the combat system.<br>

**Attacks:**

|   | Light Attack | Heavy Attack | Special Attack |
|--------------------------------------|----------------|----------------|-----------------| 
| AGILE | 334 | 500 | 1000 |
| SUPPORT | 500 | NONE | NONE |
|  TANK | 750 | 1125 | 2250 |

**Stats and movement:**

|   | Health | Stamina | Stamina Recovery Rate | Stamina Recovery Amout| Speed | Jump Height |
|--------------------------------------|----------------|----------------|-----------------|-----------------|-----------------|-----------------| 
| AGILE | 1000 | 1000 | 75 | 1 | 12 | 2 |
| SUPPORT | 1500 | 1000 | 75 | 1 | 10 | 1.5 | 
|  TANK | 2250 | 1000  | 75 | 1 | 8 | 1 |
| EVE | 100 | 1000  | 75 | 1 | 6 | 2 | 

**Enemy Attacks:**

|   | Light Attack | Heavy Attack |
|--------------------------------------|----------------|----------------|
| AGILE | 167 | 250 |
| SUPPORT | 250 | NONE |
|  TANK | 375 | 562.5 |

### Week 6 ### 
**Design:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
| Eve 3dModel       | Song               | :red_circle: | ❌22/dec |
| Icons      | Song               | :red_circle: | not set |

**Implementation:**
| Functionality                        | Team Member          | State          | DeadLine          |
|--------------------------------------|----------------|----------------|-----------------| 
|  sinc animation & vfx  | seba and carlo | :red_circle: | ❌19/12 | 
|  animation fix  | carlo | :red_circle: | ❌19/12 | 
|  improve smartness for NPC| seba | :red_circle: | ❌29/12 |
| last fix | matteo | :green_circle: | ☑️20/12 |
|  perry | matteo | :red_circle: | 29/12 |
| droppable items | matteo | :red_circle: | not set |

