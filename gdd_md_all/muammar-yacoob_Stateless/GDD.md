# Game Design Document (GDD)

## Game Title
Halloween Candy Hunt

## Game Concept
Halloween Candy Hunt is a cooperative local multiplayer game where players must work together to collect 100 candies from 20 houses while fending off zombies with candy attacks.

## Game Mechanics
- **Players:** 2-4 players.
- **Collecting Candies:**
  - Players collect candies by approaching houses and interacting with them.
  - Different houses contain varying amounts of candies.
- **Zombies:**
  - Zombies appear after the first 3 houses are visited.
  - Zombies chase players, causing damage to their health.
  - Players can fight back by throwing candy at zombies, reducing the candy inventory but repelling the zombies.
- **Health:**
  - Each player has individual health.
  - Taking damage from zombies reduces health.
  - Running out of health results in a game over.
- **Win Condition:**
  - Players win if they collect 100 candies from the houses.
  - They lose if all players run out of health.

## Visual Design
- Halloween-themed environment with spooky houses and decorations.
- Cartoonish characters and zombies.
- Candy-themed UI elements.

## Game Flow
1. Players start at a central point.
2. They visit houses one by one, collecting candies.
3. Zombies appear after the 3rd house.
4. Players must defend against zombies while collecting candies.
5. Winning or losing conditions are checked after visiting all 20 houses.