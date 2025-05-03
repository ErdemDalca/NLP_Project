# Global Games Jam 2014: Game Design Document

## Technicals: 
- Alex Haak (thedevtank), Keiran Lovett(keiranlovett), Sam Wong, Mandy Liang, Sathya Naidu, Mark Calugay

- Date: January 24, 2014

- Team Name: Super Awesome Possum Mean Team 

- Game Title: Romera vs Julia 

- Theme: Bi-polar lovers 

## Vision:
An experimental game that focuses on the theme: “We don’t see things as they are, we see things as we are.” A game that receives an emotional response from playing a modified version of tag with a twist. 
 
## Genre 
Social Game (not to be confused with social networking game), Multi player, adventure, maze game

## Concept
### Bi-polar lovers 
Players control a character with limited vision. The objective of the game is to find each and chase each other. The winning condition is one of the two players is caught. The stalker and the prey will be chosen at random times and roles switch at random times during game play. 
Each player sees differently than the other. Picture in picture game play where players use opposing players sight against them. 
Landmarks in the game trigger the power ups. The landmarks light up when the player approaches it. It will automatically activate. Power ups increase the field of view, decrease opponents field of view, mobility, and disrupt stalker.

## Story 
A great species of monsters was split into two by angry gods, resulting in two clans of Monsters who can’t decide whether to love or be loved. Romera and Julia find themselves in a peculiar predicament when they become trapped in a city with no exit. They must either confront or avoid each other in this endless cycle of love and hate, and determine the fate of their clan.

The mother tree gives vision (increase field of view for player, decreases for opposing player). The Fountain gives mobility (both player speed is increased). The Statue gives bravery (player gains permanent role of stalker for 10 seconds). The Horn gives music (both players decrease speed). They realise that in other to find out the truth, they must work together or destroy each other. 

## Players & Target Audience
### Demographic: 20-45+ 
### Competitive game: 
Both players are trying to chase each other or not get caught. The first player that becomes red is the stalker and the player that becomes blue is the prey. Roles switch at random times.

## Game structure
### Splash Screen
After the splash screen appears, there will be three buttons. The play button is tucked in the corner of the screen while play demo is surrounding it. Settings is on the opposite corner with audio, graphics and general settings. During gameplay, if the player decides to pause game, the settings screen will appear with the added option of “quit game”.

### Developer Rules
Developers should keep in mind that this will be a 3D game with fog of war and it is top down view. The picture in picture game play is taken in consideration. 

There will be landmarks throughout the level. These landmarks are of two things. Power ups and an indication of player (refer to Content section). Whenever any player approaches a landmark, the landmark glows with the players color code and an ability gets activated. There will be a cool down of 30 seconds for each landmark after its activation. 

A timer appears temporarily on the center top part of the screen, indicating that the roles of each player is about to change. That is the only purpose of the timer. It will not permanently appear on the screen. 
During fog of war, the revealed area dissipates after a short period of time. A small radius surrounds the player giving them limited view. Exploration of the level will reveal areas.
Both players move in the same speed. Both have the same field of view around them and can activate landmarks. 
Awarding points: Award the stalker one point after each successful catch. Award the prey one point after a successful evasion. These points will tally up to five, and the first player that gets that wins the game.
The game follows the cycle of search, follow, avoid and caught. 

## Player Rules
Players navigate around the play space with arrow keys or the W, A, S, D keys. The objective of the game is to either evade or stalk opposing players. Once the stalker catches the prey, the roles switch. The roles randomly change and this is indicated by a small timer that will appear and disappear after a few seconds.

You gain points by catching the prey or evading the stalker. Gain five points and win the game and the soul of your enemy. 
Implicit Rules

Players have to explore the play space in order to find out the main objectives. Once the objectives are set, the game of capture the prey begins. Players also have the ability of finding landmarks

## Content and Structure
### 3D Unique Assets
Our unique assets consists of the main characters Romera and Julia. Other such assets are related to the storyline, and these are the Big Horn, a Statue, and Mother Tree. These three unique assets are also landmarks (Big Horn, Statue and Mother Tree).
### 3D Modular Assets
Modular assets that are going to be created/outsourced are walls, pavements, fountains, rivers, and bridges. These will populate the game space and will bring the player to explore the game space. The bridges and the fountains are landmarks.
### 2D Assets
2D assets are going to be used mainly for texturing 3D assets or populating the splash screen and menu backgrounds. These are the textures for the main characters, modular and unique assets. 
Cartoon shading is the art style (refer to references at the end of this document). Cartoon brick walls, and shrub textures. Some cartoon pavement and grass areas. These assets are essential to setting the mood of the game. 
### User Interface
Scores are displayed at the top left hand side of the screen. This will always stay transparent unless the scores change. Then the opacity will change to visible and will slowly dim down to transparency again.
The timer will indicate the random role switch. Like the score interface, this will appear on screen and will slowly disappear.
In the Menu. The players have the option of changing sound, graphics and general settings. 
### Unity scene
The unity scene file will be in this folder format. Animations, Animators, Audio, Materials, Meshes, Prefabs, Scenes, Shaders, Scripts, Styles, Textures.
### Level Design
The level is created with modular assets. It will be designed around a 150 x 150 unit grid. Each 50 unit space will have a city block, sparse houses, and parks. They will all have different looks to them. 

### Game situations
### Situation 1
Two players begin at opposite ends of the level. 
Limited with a small view, the players must explore the play space and find the opponent. 
Variations

### Moving
Players navigate around the play space with arrow keys or the W, A, S, D keys. 
Representing the Player
Visuals
The player is represented by a 3D character model of monsters. They have limited view.
Data management
Score tally up to five, and we have a winner. 

## Conclusion
### About the Game and Players
This game is centered around the theme that was announced in the beginning of the Global Games Jam. This game will make the players think that they are not really who they think they are. Are you trying to stalk the prey or are you being chased?

1. Fits Well With Platform
This fits well with the chosen platform for the sole purpose of multiplayer over a network. This game will work better with two players because they will not know who will be the stalker and who will be the prey. An AI will not work as well because it will be unfair to the players. 

2. Pace 
The overall pace of the game will be slow explorations followed by quick bursts of cat and mouse. Once the player is caught or evaded, the loop begins. 

3. Rewards
- **Informed Choice**: Players gain a powerup and temporarily boost his chances of winning a point. 

- **Meaningful Choice**: Players 

- **Irreversible Choice**: