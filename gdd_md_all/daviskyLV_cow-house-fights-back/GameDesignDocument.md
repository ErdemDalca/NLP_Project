# Cow House Fights Back!
Foxes, wolves, bears and even tigers would love to just snatch up your delicious farm animals! But these ones fight back, and it's up to you to lead them!
### Genres
- Tower Defense
- Strategy
- Low-poly style
- Side-scroller
### Selling Points
The game is aimed to be kid friendly and doesn't teach to kill animals (the carnivorous wildlife), but to scare it off. It also teaches fun facts about every animal while playing the arcade tower defense game. The game also feels 2D, but with 3D low-poly graphics, making it stand out from the rest of the texture based games.

## Product Design
### Player Experience & Game POV
The player is the farmer keeping an eye over the livestock. Day after day, wildlife from the forest comes and tries to sneak into the barn to steal some food. The player has to breed/buy animals that help protect the farm and manage crops to feed the livestock.
### Visual and Audio Style
Game is centered around simple 3D graphics with a cartoony feel for 2D UI and audio effects.
### Monetization
One time game purchase
### Platforms
- PC (Windows & Linux)
- VIA Arcade Machine

## Game System Design
### Core Loops
Main gameplay loop is having more and more enemies attack the farm after each passing day. After certain amount of days new enemies get introduced, as well as night time attacks.
### Objectives & Progression
The player's objective is to not let all farm animals die from the constant wildlife attacks. The player progresses through the game by surviving as long as possible and purchasing new types of farm animals with the money they got. Player makes money by selling animals (can be bred) or food (can be grown).
### Systems
- Procedural AI (NavMeshes)
- Animations (Both premade and procedural for eg. aiming)
- Controller support (VIA Arcade Machine)
### Interactivity
The player can move the camera left & right with arrow keys/A&D/Joystick. When on PC, the player can do most of the actions (planting, placing down objects, etc.) via mouse, but on VIA's machine a separate button needs to be pressed first and the Joystick will act as a mouse.

## Milestones
### 1. Basic skeleton & base assets
- Find base assets to use for UI and 3D models to get a feel of the game's style.
- Create a small test map
- Implement camera movement controls
- Day/night cycle
- Spawn enemies based on current day/night
- Implement ability to place chickens on the field (only for PC)
- Implement basic game UI
### 2. AI, Breeding, farming, animations
- Implement ability to breed animals behind the barn
- Implement food farming behind the barn
- Implement animal animations
- Implement animal AI (both enemy and farm animals')
- Add a small shop to buy other kinds of animals/food
### 3. Sound, visual effects, polishing
- Add missing audio to game assets/scenes/events
- Add some shaders (eg. grass)
- Add controls for VIA Arcade Machine
- Polish bugs and last minute fixes
