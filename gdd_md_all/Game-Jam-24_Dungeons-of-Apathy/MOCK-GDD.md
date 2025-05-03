# MOCK Game Design Document
This is a compiled resource of all mock GDD that we have made to be properly formatted. Ideas can be added to and expanded in here.


## GDD Mock from Spoons

# Theme
It's Spreading...
# Premise
The game is defined as a 2D dungeon crawler, with procedural elements. The player will be tasked with retrieving an objective, in which the either the dungeon itself spreads and changes, or some entity within does, introducing the game's challenge.
### The Player
Player is a simple entity. No menu or equipment to manage. Player has a reasonable movement speed for pacing, and the ability to "clear" a space of an enemy or spreading material. Perhaps a flamethrower, or a torch that burns things when swinging. The core resource a player will maintain is their health.
### The Entity
The Entity is the thing infesting the dungeon. It spreads using some modified cellular automata algorithm, and has 4 states: Passive, Aggressive, Locked, and Dead. The entity acts as the primary enemy, and the effective 'timer' mechanic of the game.
##### Passive
Passive state simply spreads. When conditions for spreading are viable, the cell occupied is non-hostile. maybe it slows the player down.
##### Aggressive
Aggressive state is a hardier fixed state. When spreading is no longer feasible, it "hardens" and becomes a damaging entity. Perhaps there are variations that shoot projectiles, but most of it should be a non-traversable damage tile that takes twice as long to clear.
##### Locked
Locked state is a set of cells that need a sub-objective completed, before they become destroyable. This could be anything from clearing an adjacent room, to solving a small puzzle.
##### Dead
Dead state occupies a cell for a short period of time before decaying away. it's non-blocking, and counts as a non-spreadable tile.
### The Dungeon
The dungeon should procedurally generate from a selection of prebuilt rooms, or what would effectively be blueprints. Corridors between rooms can be calculated by shortest path, and rooms should have some margin of space around them to prevent overlapping. There should aways be a clear path between the entrance and the objective. Side rooms should be provided, with blocking material. When the objective is collected, the side rooms become unblocked, and to exit, the player must solve some series of puzzles or additional objectives to clear the path back.
### The Objective
The objective will be some McGuffin that gives the spreading entity its "power". Leaving with the objective will effectively kill it by depriving it of it's power source.

## GDD Mock from Makerizms

Finalizing (prototype 1):
Procedurally generated rooms (like binding of Isacc)
Hub room disconnected from the dungeons
Shopkeeper has weapon options (like Hades)
Saving souls from the dungeon (souls are connected to lives and give you buffs/debuffs)
Final boss (?)
Spreading entity (spawns monsters, potential name: apathy)
Abilities learned from notes (iteration 2)
Folk hero vs gods
Theme: heroes throughout the ages
Notes left by fallen heroes
Art style: 2D pixel art 32x32, character- modern times, dungeon- the deeper you go the order the architecture


## GDD Mock from Bark

placeholder
