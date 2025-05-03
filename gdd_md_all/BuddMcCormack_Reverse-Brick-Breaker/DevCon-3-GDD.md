# Game Design Document: *Reverse Brick-Breaker*

## **1. Overview**

**What are we making?**  
We are creating *Reverse Brick-Breaker*, a game where players drop balls, based on realistic physics simulation, through a pachinko-style board to break layers of bricks at the bottom.

**Point Values**:  

- **Layer 1**: 1000 Points  
- **Layer 2**: 2000 Points  
- **Layer 3**: 3000 Points  
- **Layer 4**: 1000 Points  
- **Ground**: 1000 Points if the ball collides with the ground before the bounce limit is expended.

**Gameplay Objective**:  

- **GET POINTS**: Break all the brick layers before running out of balls.  
- **GET A HIGHSCORE**: If you run out of balls, you've reached your high score.  

---

## **2. Objective Statement**

- **What question are you trying to answer with your prototype? Why?**  
  Is it possible to take the physics of pachinko and the gameplay of brick breaker and merge them into one?
By having pegs that cause complex geometry, and a drop with good placement, one can create an interesting gameplay loop by breaking bricks that give points. This rewards the player while also creating suspense through the complex movement of the various balls.

---

## **3. Design Rationale**

- **What do you envision?**  
  We envision a feasible fusion between Pachinko and Brick breaker. Where, the gameplay of Brick breaker is now upside down, and you are now dropping the balls, through pegs, onto the bricks in hopes of breaking them and getting a high score. The idea is to have the main gameplay loop revolve around the simulation aspect but be nearly disguised to feel as if it's part of the arcade aspect. A true simulation-arcade experience!

- **How is the game experience informed by metrics?**  
  All of the balls in the game are based off of physical objects, and have their object scale, weight, friction, and bounce adjusted as a result. This provides a facade of realism in the way they perform when bounced off pegs and bricks.

- **How is it engaging beyond a simulation?**  
  Beyond the simulation aspect of our game, the engagement players will feel trying to obtain a high score from breaking bricks, or the puzzle of attempting to destroy all the bricks in the level by leveraging physics to your advantage.

---

## **4. Metric Research and References**

  **Naval Cannon Ball = Cannon Ball**
  - Size = 5.5in
  - Mass = 24lbs
  
  **Professional Tennis Ball = Tennis Ball**
  - Size = 2.6in
  - Mass = 0.126lbs ( converted from grams )
  
  **Gymnasium Grade Dodge Ball = Dodge Ball**
  - Size = 8.5in
  - Mass = 0.90lbs ( converted from grams )
  
  **Full Hollow Steel Ball = Metal Ball** 
  - Size = 12in
  - Mass = 8.81lbs
  
  **Feng Shui Crystal Ball = Glass Ball**
  - Size = 1.5in
  - Mass = 0.299lbs ( converted from grams ) 

---

## **5. Citations**

- Brick Breaker: [Wikipedia](https://en.wikipedia.org/wiki/Brick_Breaker)  
- Pachinko: [Wikipedia](https://en.wikipedia.org/wiki/Pachinko?variant=zh-cn)  
- Cannon Ball Metrics: [Wikipedia](https://en.wikipedia.org/wiki/Naval_artillery_in_the_Age_of_Sail)  
- Tennis Ball Metrics: [Wikipedia](https://en.wikipedia.org/wiki/Tennis_ball)  
- Dodge Ball Metrics: [Wikipedia](https://en.wikipedia.org/wiki/Dodgeball)  
- Metal Ball Metrics: [Custom Iron Works](https://customironworks.com/metal-balls-c-1/aluminum-hollow-balls-c-1_142/aluminum-hollow-balls-30815-p-1716.html)  
- Glass Ball Metrics: [Wikipedia](https://en.wikipedia.org/wiki/Crystal_ball)  

- In planning we looked a lot at games like Pachinko and Brick breaker and decided that it was feasible to incorporate the two into our project. So shout out to those games.

---

## **6. Additional Sections**

### **Ball Types and Properties**

Each ball has unique gameplay properties:  

- **Tennis Ball**: Medium weight and bounce.  
- **Cannonball**: Very heavy; drops almost vertically.  
- **Glass Ball**: Limited durability; precise targeting.  
- **Rubber Ball**: High bounce; unpredictable movement.  
- **Metal Ball**: Heavy with minimal bounce.

### **Setup**

- **Movement Controls**:  
  - (A) or (Left Arrow): Move Left  
  - (D) or (Right Arrow): Move Right  

- **Ball Selection**:  
  - (Q): Cannon Balls = 5  
  - (W): Tennis Balls = 10  
  - (E): Dodge Balls = 15  
  - (R): Metal Balls = 8  
  - (T): Glass Balls = 8  
  - (H): Last Resort = ∞ (after all balls are used)  
  - (C): Secret Chicken Button = ∞  

---

### **Playtesting Feedback and Design Response**

**FB = Feedback | DR = Design Response**

**FB** - Balls were too small  
**DR** - _(The balls were fixed by being scaled up each by the same increment, and the board was also rearranged for better player experience.)_

**FB** - It felt really good, the physics were accurate to the objects they were representing  
**DR** - _(Continued to use the same physical metrics going into final build.)_

**FB** - Reverse brick breaker is an interesting idea and potentially entertaining idea  
**DR** - _(Designed the game to be more exciting, playing off of the physics simulation aspect of the game.)_

**FB** - Randomness undermines character agency, so having different categories of balls with different amounts of each ball would be a good way to add back the agency.  
**DR** - _(Made a set amount of each ball instead of random balls.)_

---

### **Additional Questions**

#### 1. How does the choice of ball physics affect gameplay in terms of player control and strategy?

- **Metal Ball**: Heavy and fast, with minimal bounce—ideal for tough layers.  
- **Tennis Ball**: Balanced weight and bounce for flexible play.  
- **Cannonball**: Extremely heavy; excellent for smashing through layers but hard to aim.  
- **Glass Ball**: Precise targeting with limited durability.  
- **Rubber Ball**: Unpredictable but can create exciting plays with skilled use.

#### 2. What strategies can players use to achieve the highest scores?

Careful ball selection and understanding their unique properties allow players to plan drops strategically, targeting high-value layers like Layer 3 or Layer 2 for maximum points.

#### 3. How does the arrangement of pegs influence the player’s decisions and gameplay strategy?

The placement of pegs creates a challenge. Players must analyze how the pegs guide the ball's path and plan their drops accordingly to hit high-value targets and break layers effectively.
