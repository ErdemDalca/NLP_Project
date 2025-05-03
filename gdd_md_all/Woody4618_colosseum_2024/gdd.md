Blobs and on chain game 

## Blobs Game Design Document

The game works is inspired by dark forest which is an on chain game on eth. 
It is a real time strategy game. 

## The Game 

The game is played on a grid. Each player needs to buy into the game. When buying in the player gets a home blob and also spawns 4 random blobs of different sizes on the map. 

Each blob has a color meter that slowly fills over time when a player owns the blob. The color is used to convert other blobs. 

So the main interaction is to convert other blobs. 

### Winning

The game ends when there is only 1 player left.
Or maybe when a certain main blob in the middle is converted. 

## Resources

There is 1 resources in the game:

1. Color 

### Color

Each blob that is owned by a player generates color. The color is used to convert other blobs.
The color generation follows a curve where the most color is generated at around 50%.  

## Converting Blobs

At any time a player can take any amount of color of his blob and use it to attack another blob. 
The attack amount falls off over distance. 
Then the color of the current player falls to 0 the blob in converted and produces color for the new player.

## Upgrading Blobs

Blobs can be upgraded to hold more color, generate color faster and have a higher range.

### Earning 

If a player want to extract the sol from a blob back to his wallet he can do so but during that time he will be very vunerable to attacks and may loose his blob. 

# Implementation

Either one big grid account or multiple PDAs for each player. 
TODO: Discuss the pros and cons of each.

TODO Game preset: 
- Add use session to player data init
- Add check for session to session popup
- Rename test ts file to how the project is called or smth default 
- Switch to main thread on game data message 
- Check if seeds in unity client and program are the same 
- Rename gameData from level seed so that they are the same in unity and the program

TODO Client: 
- Add Spawn blobs call to unity 
- Draw blobs in a grid in unity 


TODO Program: 
- Random blobs position 
- Blob position check (increase blob level on duplicate)
- Attack async 
- Attack test 
- Attach finish battle 


