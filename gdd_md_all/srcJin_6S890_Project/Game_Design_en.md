## **MVP Game Design Document**

### **Goals**
1. Players (agents) need to take actions in a resource-constrained and dynamic environment by constructing different types of buildings to optimize their rewards.
2. Each player pursues personal interests (such as money and reputation) while considering the global environment score to avoid the negative impact of environmental collapse.
3. The game is designed to teach agents that cooperation can improve total scores in the long term while preserving enough competition to maintain complexity and strategic diversity.

---

### **Board**
- **Map Size:** 4x4 grid.
- **Initial State:** Empty, where each grid cell can accommodate different types of buildings.

Each grid cell is associated with the following three core indices, all represented as relative values in the range [0, 100], with an initial value of 30. These indices are dynamically updated each round based on interactions between cells:

1. **Greenery Index ($G$):**

2. **Vitality Index ($V$):**

3. **Density Index ($D$):**

---

### **Imperfect Information**
1. **Hidden Resources:**
   - Each player's money and reputation are not visible to other players.

---

### **Resource Constraints**
- Each player starts with 20 money and 20 reputation.
- When a player's resources are depleted, they must skip their turn.

---

### **Building Types**

Building are designed to affect both current cells and their surrounding cells.x

### **Park**
- **Cost**
  - Consumes 1 money
  - Consumes 3 reputation
- **Utility**
  - Reduces the builder's money by 1 per turn
  - Increases the builder's reputation by 3 per turn
- **Benefits**
  - Increases greenery index: $G +30$ for itself, $G +10$ for adjacent cells.
- **Drawbacks**
  - Suppresses vitality: $V -30$ for itself, $V -10$ for adjacent cells.

### **House**
- **Cost**
  - Consumes 2 money
  - Consumes 2 reputation
- **Utility**
  - Increases the builder's money by 2 per turn
- **Benefits**
  - Increases density index: $D +30$ for itself, $D +10$ for adjacent cells.
- **Drawbacks**
  - Decreases greenery index: $G -30$ for itself, $G -10$ for adjacent cells.

### **Shop**
- **Cost**
  - Consumes 3 money
  - Consumes 1 reputation
- **Utility**
  - Increases the builder's money by 3 per turn
  - Reduces the builder's reputation by 1 per turn
- **Benefits**
  - Increases vitality index: $V +30$ for itself, $V +10$ for adjacent cells.
- **Drawbacks**
  - Reduces residential comfort: $D -30$ for itself, $D -10$ for adjacent cells.

---

### **Players**
- **Number of Players:** 3 (can be extended to more players).
- **Player Characteristics:**
  - **Resources:** Each player has independent money and reputation.
  - **Reward Function:** Each player earns rewards based on their actions, consisting of **personal rewards** and **environment score contributions**:
    $$
    u_i = \alpha \cdot \text{self\_score}_i + \beta \cdot \text{environment\_score}
    $$
    where $\alpha$ and $\beta$ are preference weights assigned to each player at the start of the game, introducing strategic differentiation.
  - Each player tracks their **spend** and **earned** for subsequent scoring.

---



### **Player Actions**
Players take turns, and during their turn, they can perform the following actions:
1. **Construct:** Spend money and reputation to place a building on an empty grid cell.

---

## **Player Strategies**

### **Player A: Economic Player**
- **Traits:** Focuses on monetary rewards, pursuing short-term benefits through shop construction and high-vitality areas.
- **Reward Function:**
  $$
  \text{self\_score}_A = 0.8 \cdot \text{money\_earned} + 0.2 \cdot \text{reputation\_earned}
  $$

---

### **Player B: Reputation Player**
- **Traits:** Focuses on reputation by building houses and collaborating with parks to create high-reputation neighborhoods.
- **Reward Function:**
  $$
  \text{self\_score}_B = 0.2 \cdot \text{money\_earned} + 0.8 \cdot \text{reputation\_earned}
  $$

---

### **Player C: Balanced Player**
- **Traits:** Balances between monetary and reputation rewards, aiming to optimize both economic and environmental outcomes.
- **Reward Function:**
  $$
  \text{self\_score}_C = 0.5 \cdot \text{money\_earned} + 0.5 \cdot \text{reputation\_earned}
  $$

---

## **Scoring Mechanism**

The environment score ($\text{Global Environment Score}$) is calculated based on the weighted averages of all grid cells:
$$
\text{Global Environment Score} = w_G \cdot \bar{G} + w_V \cdot \bar{V} + w_D \cdot \bar{D}
$$

- $\bar{G}, \bar{V}, \bar{D}$: Average indices of greenery, vitality, and density across the board.
- $w_G, w_V, w_D$: Weights, initially set to $w_G = 1/3, w_V = 1/3, w_D = 1/3$.

The final score for each player is:
$$
\text{Final Score}_i = \alpha \cdot \text{self\_score}_i + \beta \cdot \text{environment\_score}
$$
Where $\alpha = 0.5$, $\beta = 0.5$.

---

### **Game End Condition**
The game ends when the board is filled or a maximum turn reached.

---

### **Evaluation**
After the game ends, each player’s contribution to their objectives and the overall goals is evaluated. There is no defined "winner" in this game.

---

## **Multi-Agent Learning Objectives**

1. **Cooperation:**
   - Agents need to balance environmental scores and personal scores to learn cooperation in specific scenarios.
2. **Competition or Blocking:**
   - Agents can choose competitive strategies to reduce other players’ rewards and gain advantages.

---

## **Game Dynamics and Experimental Directions**
We aim to calculate each player’s optimal strategy and find the Course Correlated Equilibrium.

### **Evaluation Metrics**
1. **Cumulative Score for each player**
2. **Cooperation Degree:** Proportion of actions that benefit the environment.

---

## **Game Visualization**
   - Display the global environment score in each step.
   - Show each player's current resources, earnings, selected action, self\_score, and final\_score in a structured format.
   - Display the game board in text