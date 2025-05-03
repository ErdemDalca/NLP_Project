# **Game Design Document: Zig Zag Zog**

**1\. Game Concept**

Zig Zag Zog is a fast-paced, round-based game where each player simultaneously chooses one of three shapes: triangle, circle, or square. In every round, after either all players have made a selection or N (e.g., 10\) seconds have elapsed, the shape chosen by the majority eliminates all players who picked it. The game concludes when all remaining players choose the same shape or two or more shapes are tied for the most votes, at which point they equally share a pool of rewards.

## **2\. Core Mechanics**

* **Shape Selection:** At the start of each round, players choose from three shapes: triangle, circle, or square.  
* **Timer:** Each round features a N second timer. If a player fails to select within this period a default action is triggered (e.g., player is eliminated or auto-selects).  
* **Elimination Rule:** After the round ends, the shape that received the most selections is determined. Every player who chose that shape is eliminated.  
* **Victory Condition:** The game ends when either:  
1. Every player selects the same shape in a round OR   
2. Two or more shapes are tied for the majority of selections.

## **3\. Game Flow**

1. **Lobby Phase:** Players join a game lobby and wait for a sufficient number to start the match. Could start when X players join or start based on a time trigger (e.g. noon).  
2. **Round Start:** Each round begins with a clear display of the shapes available and a visible countdown.  
3. **Selection Phase:** Players make their selection by tapping or clicking on their preferred shape.  
4. **Round End & Elimination:** Once all players have selected or the timer expires, the system tallies the choices, and players who picked the majority shape are eliminated.  
5. **Continuation:** Remaining players proceed to the next round. If a victory condition is met then the game ends.  
6. **Game Conclusion:** All users in the shape with the most or tied for the most selections users to share the reward pool equally (or pro-rata to stake size).

## 

## **Additional Rules and Considerations**

* **Default Actions for Inactivity:** If a player does not select a shape within 10 seconds, a predefined default action (such as random selection or a penalty) is applied.  
* **Tie Scenarios:** Detailed tie-breaking rules must be defined to maintain fairness; for instance, if two shapes tie as the majority, either no elimination occurs or a random elimination among those tied may be enforced.  
* **Balancing:** Regular analytics will help ensure no particular shape becomes overly dominant, with adjustments made to tie-breaking or timing rules as necessary.

## **Future Development & Scalability**

* **Game Variants:** Future updates might include power-ups or modifiers that affect the elimination rules (e.g., “shield” that protects one player per round).  
* **Customization:** Allow players to customize the timer or shapes or default rules for inactivity or the victory condition.