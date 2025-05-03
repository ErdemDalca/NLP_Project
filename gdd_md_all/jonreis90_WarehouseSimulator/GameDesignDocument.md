

# Warehouse Simulator 
# Game Design Document

Unreal engine version 4.19.2
Version 1.0












Jon Reis
jonreis90@hotmail.com


________________





## Design History 
This is a change listing quickly describing each major version and changes.
________________
## Section I - Game Overview
### Game Concept
Warehouse Sim is a game were you manage a warehouse with you and your friends and try and run a successful business, growing in size 
or becoming bankrupt in the process. 
### Feature Set
Game consists of realistic warehouse components, such as firstperson players, forklifts, shipping/receiving ports, pallets/shipping materials
shelving/storage systems, purchasing, job recieving system.  

### Genre
Sim 
### Target Audience
Young children, older males( young children want to know what its like, older males want to relate)
### Game Flow Summary
Players start by purchasing a small affordable warehouse with the limited funds they start with, taking on jobs they think they can handle using the computer system, 
slowly building a business making more money to buy better equipment such as different forklifts and racking systems. Players eventually can buy bigger warehouses and 
really push the limit to managing a massive warehouse 
### Look and Feel 
The game will be as realistic as reasonable to fit into the simulation catagories and sell to are target audience  
### Project Scope 
Start with all the core concepts, should look for a monthly timeframe to complete core game  
________________
## Section II - Gameplay and  Mechanics
### Gameplay
The game play will consist of getting jobs through the computer, a truck will deliver goods, players must store goods for a time based on the contract,
goods will need to be shipped out at the later date by putting them back in another truck. 
### Game Progression
The player can use their money to buy more equipment and bigger warehouse to aquire more difficult jobs 
### Mission/challenge Structure
The challenge of the game is managing the finances and using/buying equipment and utilitizing storage space effiencetly.
(possibilty of adding special challenges later on if deemed fit)
### Objectives
Is to build a warehouse empire from the ground up. 
### Mechanics
The game will contain the following mechanics


* Firstperson characters with the ability for coop/multiplayer play
* A basic warehouse 
* Ability for players to pickup and drop smaller boxes/items 
* Ability for players to drive forklifts 
* Pallets/boxes and other commonly shipped goods all containing real physics simulation 
* A adjustable damage(hp) system for the package when they are hit or dropped to violently, (fragile packages are weaker)  
* A Garagedoor opening and closing simulating a truck is docked to the warehouse 
* A computer system in the warehouse were players can get work, order new forklifts, order racking or other 
warehouse storage equipment
* Ability for players to build the racking or other storage equipment that they ordered  
* A labeling system for players to organize their shipping goods 

Less important mechanics that could be added later 
* Bidding system for getting new jobs
* automated equipment such a conveyer belts and scanners 
* Hiring workers to do automatic organizing 
* robot arms 
(watch an amazon warehouse video for inspiration)
 
### Physics 
All packages/shipping goods and pallets with have full physics with a impact detection for damage 
### Movement
Players will be first person with a generic movement abilities 
### Objects
* Boxes small and large
* Pallets
* Forklifts different kinds
* Large awkward items 
* Racking systems 
* Computer desk with computer 
* Garage door with inside of truck docked to warehouse 

### Picking Up Objects
Players can pickup smaller items and place them  
### Moving Objects
Players can pick up objects and move with them, or use a forklift or other equipment 
### Switches and Buttons
An action button for entering or operating equipment like forklifts and the computer, a pickup button   
### Reading
The computer will contain information for the game  
### Economy
There may be economy type systems in future releases 
### Screen Flow 
Game will have a mainmenu to select game modes, players will spawn in warehouse and interacting with the computer will create a gui 
### Screen Descriptions
* mainmenu contains all the elements to select 
* main game which also contains a computer gui 
* might contain a pause menu 
### Main Menu Screen
* Careermode/ new game - the main game  
* Tutorial- game will have a tutorial either built in the careermode start or possible a seperate mainmenu item  
* Other game modes- possibly adding challenges or online play or other in the future 
* Settings- settings  
### Settings Screen
Will contain settings of game if needed 
### Game Settings
How the settings will affect the game, settings not determined yet.
### Replaying and Saving 
The player will be able to save/load a saved career 
________________
## Section lll – Warehouse/Levels
## Warehouse #1
### Synopsis
A introductory warehouse were you can barely do anything or afford any equipment. Player will take on simple small package organization 
jobs and carry them around. Players will buy small racks for organizing small packages. Player could buy pallet jacks for simple large
item storage. Warehouse becomes crowded very quickly 
### Objectives
Make money and buy a bigger warehouse when appropriate 
### Physical Description
Small almost 2 car garage size(size to be adjusted with playtesting) containing computer desk and garage door for truck docking, 
low ceiling height to limit equipment thats usable(no forklifts or multiheight storage)   
## Level #2
The warehouse levels will get larger in size and support additional equipment

## Section IV - Interface
### HUD
No hud, packages will have a damage meter when selected, packages will have some kind of number or identification when selected 
### Menus
Computer system will contain all menus and guis for the most part 
### Rendering System
The game will auto render elements as placed in build area 
### Camera
The camera will be player controlled 
### Lighting Models
The game will contain generic lighting
### Control System
The player controllers use standard mouse wasd movement/ or gamepad input 
### Music
Generic background music possibly 
### Sound Effects
Sound effects for package movement/dropped and equipment(forklifts), walking possibly as well, interacting with objects  
### Help System
A tutorial will be required 
________________
## Section V – Technical
### Target Hardware
PC
### Development hardware and software
Unreal engine, possible other 3d modeling software 
### Development procedures and standards
Using github to organize procedures and standards 
### Game Engine
Unreal engine 
### Network
No network at the moment 
### Scripting Language
Blueprint Scripting 
________________
## Section V – Game Art
### Concept Art
None
### Style Guides
Realistic 
### Environments
Will be a super basic- no outside, just dark warehouses with lighting   
### Game Asset
Will be realistic 


______________________
## Gameplay Programming/Blueprints Documentation and Guides 
This section goes into details about how all the files and the gameplay programming works 
### Blueprints List
todo
### Level Creating Guide 
todo 

______________________

## Appendices
### Asset List
todo
### Model and Texture List
todo
### Interface Art List 
todo
### Sound
todo
### Environmental Sounds
todo
### Interface Sounds
todo
### Music
todo
