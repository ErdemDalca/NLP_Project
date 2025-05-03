# DOT4 Gravity

![image](https://github.com/ajuna-network/game-dot4-unity/assets/17710198/e9a88a3d-9632-4e86-8947-1d7fe1c8d1ba)

DOT4 Gravity is a science fiction-based interpretation of Connect Four that is fully playable on the chain. It operates on a substrate-based main chain, and the game logic runs on a trusted, execution-based, substrate-based sidechain. The game engine is located [here](https://github.com/ajuna-network/ajuna-games).

"The Three Towers" is a simplified mode of DOT4 Gravity, where the objective is to create 3 square patterns to win. At the beginning of the game, each player can place three bombs on the field. These bombs will explode, causing all stones in a 3x3 square around the bomb to vanish.

## DG-5: Principal Game Logic

Short Description, 

<p float="left">
  <img src="https://github.com/ajuna-network/game-dot4-unity/assets/17710198/5ab3f5b4-c2bb-486d-a79a-038f53f58652" width="200" />
  <img src="https://github.com/ajuna-network/game-dot4-unity/assets/17710198/e45b772d-e1f4-49de-8bf1-a6b1ec0f3778" width="200" /> 
  <img src="https://github.com/ajuna-network/game-dot4-unity/assets/17710198/47cbc958-beb6-4a9a-8ce1-09fd51fc5a7f" width="200" /> 
  <img src="https://github.com/ajuna-network/game-dot4-unity/assets/17710198/98bac77f-467e-4a8f-b15b-663d03a5e8af" width="200" />
</p>

At the beginning of the game, 10 random blocks are set on the field.

In the Bomb Phase, each player can place 3 bombs. Only the bombs placed by a player are visible to that player. This phase ends automatically after 30 ticks or when both players have placed their 3 bombs. Note that this phase is not turn-based.

In the Play Phase, each player can drop one stone per round. This phase is turn-based, with each turn lasting a maximum of 30 ticks.

Players can trigger bombs - either their own or their opponents'. A position can hold multiple bombs from different players, but a maximum of one bomb from each player. A bomb detonation removes everything except fixed blocks, including other bombs. Bombs are triggered when a stone attempts to pass through.

For more detailed game logic, please refer to the [Game Design Document (GDD)].

https://www.youtube.com/watch?v=VXwb8YSnjRQ
