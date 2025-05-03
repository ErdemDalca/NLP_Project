# Game Overview - TumbleToad

## Description:

In TumbleToad, You play as a Pumpkin Toadlet (A frog that can’t properly land). Your goal is to reach the end of the pond by leaping from one obstacle to another whilst avoiding the alligator infested waters; Though be careful, your toadlet is bad at landing, you might tumble off Lily pads and fall off, so take your time and estimate your leaps.
(click and pull to charge your frog’s leaps)

(Pumpkin toadlets are very bad at jumping, often losing balance mid-air and crash landing awkwardly. This is due to the small size of their inner ear canals, the area of the body that regulates balance and orientation).

---

## Objective Statement

For this Prototype, we want to accomplish a comedic feel to our game while trying to keep the thrill from falling off obstacles. 

We want to test if the “Ragdoll” frog aspect adds a comedic feel, where the frog would just tumble around. We also want to test our prototype’s difficulty based off our mechanics and adjust it accordingly to balance the funny and fun aspect with challenge.

---

## Design Rational

Our overall vision for our game as mentioned in our game overview description will be about a Pumpkin Toadlet attempting to cross an alligator infested pond, where players would control the little frog’s leaps between obstacles. The challenge is that the little frog can’t land properly, which would add difficulty mixed with the funny tumbling frog. The players must successfully reach the “finish line” without falling into the water.
Our game experience is informed by metrics with gravity, spring force, scale, and weight. Gravity and weight is what controls our little frog’s fall, while the weight and the strength of the spring force is used for the leap.

---

## TumbleToad - Mood Board

![TumbleToad - Mood Board](https://imgur.com/a/OD620A6)

### Games included in Mood Board
- **Game:** Angry Bird | **Reason for Including:** Drag and Pull controls
- **Game:** Roblox (Obby) | **Reason for Including:** Perspective, Gameplay

---

## Metric Resources & References

#### Forces and Physics 

1. **Gravity**: Earth's gravitational force is set to `9.8 m/s²`, used to simulate the frog's natural fall and jump trajectory. 
-	Formula: `F = m * g`, where: 
-	`m = 0.01215 kg` (frog's mass). 
-	`g = 9.8 m/s²` (gravitational acceleration). 
-	`F = 0.01215 * 9.8 ≈ 0.119 N` (force acting downward on the frog).    - Reference: google 
  
2. **Launch Force**:  
-	Spring force calculation `F = -kx` (Hooke’s Law), where: 
-	`k = 20 N/m` (spring constant; we can also adjust for balance). 
-	`x` is the drag distance in Unity units. 
  
#### Object Scale and Weight 
1. **Frog Size**: 
-	Pumpkin Toadlet frogs are tiny: 
-	Approximate dimensions: `0.01 m x 0.015 m x 0.005 m` (10mm x 15mm x 5mm). 
-	In-game representation scaled up slightly for visibility . 
-	Reference: Research on frog species. 
  
2. **Frog Weight**: 
-	Weight: `12.15 g` or `0.01215 kg`. 
-	Used to calculate realistic movement and jumping forces. 
-	Reference: [Pumpkin Toadlet Research Papers](https://worldspecies.org/ntaxa/960910). 
  
#### Materials and Friction 
1. **Surface Interaction**: 
-	Friction coefficient: 
-	Grass: `0.35`. 
-	Wet surfaces: `0.1` (slippery after rain). 
-	Reference: [Engineering Toolbox - Friction Coefficients](https://www.engineeringtoolbox.com). 
  
2. **Bounciness**: 
-	Frog’s body elasticity : `0.3`. 
-	Used for slight bounce when landing on obstacles. 

#### Surface Interaction

**Friction Coefficients**: 

- Grass: 0.35, Moderate friction slows down rolling movement slightly. 

- Wet Grass: 0.1 , Low friction makes the frog slide further especially after rain. 

- Sticky Surfaces (Mud): 0.5 , High friction significantly reduces sliding. 

- Hard Surfaces (Rocks): 0.2 , Moderate friction with little resistance to sliding. 

- Sand: 0.4 , Slightly higher friction slows the frog, with reduced rolling momentum. 

**Bounciness**

Elasticity of the frog's body: 0.3

Adds a slight bounce when the frog lands on obstacles or hard surfaces. 

--- 

#### Environmental Effects

**Wind Resistance**: 

- The frog experiences a drag force based on its size, shape, and speed during jumps or slides. This is calculated using the formula:

- F_drag = 0.5 × ρ × v² × Cd × A 

- ρ (Air Density): 1.225 kg/m³ (standard atmospheric conditions).

- v (Velocity): The frog's speed.

- Cd (Drag Coefficient): 1.0 Assuming a blunt shape for simplicity.

- A (Cross-sectional Area): Based on the frog's scaled size in the game .

- Wind resistance slightly reduces jump distance and slide speed. This effect is minor but noticeable at higher launch velocities.

---

## Link Dump (Resources)

- [Real Pumpkin Toadlet Jumping](https://www.youtube.com/watch?v=HoY1_QIS8k8)
- [Movement References](https://www.youtube.com/watch?v=xZ0pPnm3tDI)
- [Another Movement Reference](https://www.youtube.com/watch?v=99yIg-A5eCw&list=PLGXzgnKhu_mCTmg_AS66j8U7duSzcsub7)
- [Obstacle Track](https://assetstore.unity.com/packages/templates/packs/obstacle-course-pack-178169)
- [Toadlet Asset](https://assetstore.unity.com/packages/3d/characters/animals/toxic-frogs-132963)
- [Friction Coefficient Resource](https://www.engineeringtoolbox.com/friction-coefficients-d_778.html)

## Game Dev. Video

[Here's our commentary on our prototype!](https://youtu.be/tqP74rTFdwY)
