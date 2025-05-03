# Game Design Document (GDD) - Top-Down Zombie Game 

  

## 1. Game Overview 

  

**Game Title:**   

ZombieLand 

  

**Genre:**   

Top-down, action, survival. 

  

**Platform:**   

PC, Console (expand based on your choice). 

  

**Target Audience:**   

Players who enjoy intense survival games, strategy, and adaptive AI challenges.   

Target age: 16+. 

  

--- 

  

## 2. Gameplay Overview 

  

The player is faced with waves of zombies in this top-down zombie survival game, which spawn at random in response to their actions and surroundings. The aim is to survive for as long as possible, using weapons, environmental challenges, and strategically positioning to ward off masses of enemies (zombies). 

 

### Core Gameplay Loop: 

1. **Explore:** The player moves through the environment, searching for resources and avoiding traps. 

2. **Combat:** Engage zombies with various weapons, deciding when to attack or evade. 

3. **Survive:** Endure waves of dynamically spawning zombies based on player actions, environmental triggers and adaptive difficulty systems. 

4. **Progress:** Upgrade weapons, unlock new areas and adapt to increasingly challenging enemy spawns. 

 

## 3. Game Objectives 

  

### Primary Objective:   

Survive as long as possible against waves of zombies, managing resources, positioning, and timing to fend off increasingly difficult enemies (zombies). 

![3x zombie Spawn](https://7daystodiemods.com/wp-content/uploads/2021/09/7-days-to-die-3x-zombie-spawn.jpg)
   

--- 

  

## 4. Player Objectives (Prototype Focus) 

  

The prototype will aim to answer the following question:   

**"How does dynamically wave spawning AI enemies impact player engagement and challenge?"** 

  

  

--- 

 ## 5. Wave Spawning System 

  

### Types of Waves: 

- **Constant Wave Spawning:** Zombies spawn at a steady rate, giving players constant pressure. 

![Contant Waves](https://github.com/Varsha-vk05/forpics/blob/main/Screenshot%202024-09-25%20130125.png?raw=true)

- **Burst Wave Spawning:** Large groups of zombies spawn in short bursts after longer breaks, creating intense moments followed by quieter intervals.
  
![Burst Waves](https://github.com/Varsha-vk05/forpics/blob/main/Screenshot%202024-09-25%20131402.png?raw=true)

- **Mixed Wave Spawning:** A combination of both constant and burst waves, keeping players on their toes.
  
![Mixed Waves](https://github.com/Varsha-vk05/forpics/blob/main/Screenshot%202024-09-25%20131812.png?raw=true)
  

### Adaptivity of Waves: 

The system adjusts difficulty based on: 

- **Player Skill Level:** If the player is moving through levels too quickly, tougher zombies spawn. If the player is struggling, fewer zombies spawn. 

- **Player Behavior:** React to player actions like triggering spawns with noise or by spending too long in one area. 

  

--- 

 

## 6. AI Spawning System 

  

### Spawning Types: 

- **Environmental Triggers:** Zombies spawn when the player enters specific zones or crosses boundaries. 

- **Player-Triggered Spawns:** Defeating a boss, collecting items, or interacting with objects (e.g., breaking doors or making noise) will trigger nearby zombie spawns. 

- **Random Intervals:** Unpredictable zombie spawns that happen periodically to keep the player alert. 

- **Adaptive Spawning:** AI spawning adjusts based on the player's performance. For example, more zombies spawn if the player is doing well, and fewer appear if the player is struggling. 

  

### How AI Spawning Affects Gameplay: 

- The unpredictable nature of spawning increases tension and challenge as players must constantly adapt to new threats. 

- Players must balance offensive and defensive strategies, utilizing the environment (e.g., barricades, traps) to survive. 

- Enemies spawn from various locations, requiring the player to stay mobile and avoid being overwhelmed. 

  

--- 

  

## 7. Combat Mechanics 

  

- **Weapons:** The player will have access to melee weapons (e.g., bats, knives) and ranged weapons like stones, slingshots and guns. Each weapon has limited durability or ammo, requiring resource management. 

- **Health:** The player’s health will deplete with each zombie attack. Health can be restored by finding and using healing items. 

- **Environmental Interactions:** Players can interact with the environment to slow down or trap zombies like barricading doors, triggering traps. 

  

--- 

  

## 8. AI Behavior 

  

- **Basic Zombies:** Slow-moving, weak enemies that rely on overwhelming the player with numbers. 

- **Special Zombies:** Faster, more durable, or possessing unique abilities like summoning additional zombies or spitting acid. 

- **Boss Enemies:** Larger, more dangerous enemies that appear after completing specific objectives (e.g., a mini-boss after unlocking a new area). 

  

--- 

  

## 9. Progression System 

  

- **Upgrade System:** Players earn resources for surviving waves and can use them to upgrade weapons, health, and movement speed. 

- **Unlockable Areas:** As players progress, they unlock new zones, each with its own difficulty level and AI spawning triggers. 

  

--- 

  

## 10. Conclusion 

  

The main goals and mechanics of the top-down zombie game are described in this GDD. The main mechanic that will be looked at to figure out its effect on player engagement, challenge, and strategic thinking will be the AI wave spawning system. Our goal is to create a dynamic and exciting survival experience by adjusting the spawning system and balancing difficulty. 



---


### External Resources for Prototype

- **Enemy Spawner**:  
  [Spawner YouTube Video](https://www.youtube.com/watch?v=cecD66fZ_4c&list=PLx7AKmQhxJFajrXez-0GJgDlKELabQQHT&index=14)

- **Enemy Tracking**:  
  [Tracking YouTube Video](https://www.youtube.com/watch?v=cecD66fZ_4c&list=PLx7AKmQhxJFajrXez-0GJgDlKELabQQHT&index=14)
