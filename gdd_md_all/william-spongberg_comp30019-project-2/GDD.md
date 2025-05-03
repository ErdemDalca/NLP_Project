
# Game Design Document (GDD) #

## Game Overview ##

### Core Concept ###

Our game’s core concept is a movement based FPS Shmup(shoot em’ up) that takes place in an eerie and surreal environment that pits the player and the main character(Aidan) against an otherworldly, ominous, eldritch being known as The Admin. In order to save his wife, Aidan must venture into The Admin’s domain, destroying the entity’s forces through a series of increasingly abnormal environments and delving deeper level by level until he can confront The Admin. Because the game is about willingly entering the lair of a dangerous monster in order to accomplish the player's goal, we have named our game, "Into The Abyss".

Games that are similar, and from which we drew inspiration from include ULTRAKILL and Doom Slayer, which are both Shoot Em’ Ups, ULTRAKILL specifically is also a movement based FPS. 

<img title="Ultrakill, a game by New Blood Interactive" alt="Alt text" src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1229490/header.jpg?t=1704406135">

*Figure 1: Ultrakill, a game by New Blood Interactive*

For the level design, one inspiration we drew from was the Backrooms, an ordinary environment that is eerie in context(in the case of the Backrooms, the infinite size and monsters). Similar to the Backrooms, the environments in our game will primarily be normal environments that have become unsettling or uncomfortable due to contextual factors.

Our game is focused on telling a story and giving players a memorable experience through the medium of the game’s mechanics, atmosphere, and narrative. 

### Target Audience ###

Our game is aimed at people aged 16 and above and who want a sharp detour from reality. It is designed for those who love to be immersed in a fantastical yet eerie and confusing environment. Due to the nature of the graphic details and uncomfortable atmosphere, this game should not be played by children.

Thanks to a timer and excellent movement design, it is also perfect for speedrunners or those who generally love movement and action-based games. However, it contains a rich and emotional story, so it can also be enjoyed more generally by those who like to embrace a new and exciting world.

### Unique Selling Points (USPs) ###

Into The Abyss will give players a different experience every time they play thanks to the procedurally generated world and environment, added depth is found in the out-of-this-world, shadowy, and surreal design. Which, combined with an emotional storyline and action-packed gameplay, keeps Into The Abyss unique, whether to new or returning player.

## Story and Narrative ##

### Backstory ###

Into The Abyss takes place in the lair of a being named the Admin, an otherworldly entity beyond human comprehension that enjoys toying with living beings and consuming their memories. Outside of the Admin’s lair is a modern world setting similar to our own. The lair of the Admin is an office tower with floors/levels with a theme of being familiar locations with some abnormal twist.

### Plot ###

The main character Aidan’s wife will be forcibly taken from him by the Admin, causing him to willingly delve into Their lair in a bid to save her.

To progress and go deeper into the tower, the main character must kill the pawns of the Admin, who are victims that have had their memories devoured in the past and ride elevators that take him to higher floors. Throughout his journey, the Admin will taunt and antagonise the protagonist so that his presence will have a greater impact and be a larger motivator for a player.

The player will eventually learn that the floors of this tower are actually modelled after his own memories, and the process of climbing it(to save his wife) allows the Admin to see and consume more of his memories. Which is why the Admin allows the main character to keep climbing the tower.

In the end, the protagonist determines that the only hope he has of defeating the Admin is to find a memory strong enough to kill or wound it. He takes an elevator into the next floor(memory) to search for his strongest memory.

Upon finding his strongest memory, the Admin will show its face, eager to consume the main character’s memory the moment it is revealed, commencing the final boss fight.

Upon defeating the Admin, the player will get one of two endings depending on how well they did/if they completed the requisite additional objectives.

One in which the main character stands before the grave of his wife, and one in which he successfully rescues his wife.

### Characters ###

There will be 4 major characters in the story of the game:

**Aidan**, the protagonist, and husband to Sherry. They are an average salaryman that has recently left his job in order to start a business with his wife(cafe/bakery/restaurant). They are the point of view character and have entered the Admin’s lair in order to save his wife.

**Sherry**, wife of Aidan. Bright and cheery, a big dreamer. Is currently still working as an office worker. Was dragged into the lair of the Admin to have her memories consumed.

**Admin**, an incomprehensible entity with no clear origin, the victims who They have devoured memories from act as Their physical vessels. Their voice will be made up of multiple people speaking at once. They will be referred to with They/Them/Their, all capitalised to represent their status as a collective being and as a godlike entity.They are whimsical and cruel, like a tyrant. They are entertained by the torment and suffering of people and by extension Aidan. The Admin appears to hunger and feast on the memories of living beings, which serves as their primary motivation.


## Gameplay and Mechanics ##

### Player Perspective ###

Into The Abyss is a first-person game with a camera that is moved by the mouse. This allows for specific and smooth movement + combat which aims to give more freedom to speedrunners and better immerse the player into the world of our game. Only the character’s hands and office-shirt sleeves, as well any equipped weapons/tools, will be visible on screen at any point in time.


## Controls ##

Our game is a movement based FPS. The player will be able to fire weapons using the mouse, as well as move using the arrow keys. In addition to moving and shooting, the player will be able to jump using the spacebar.

<img title="a title" alt="Alt text" src="https://steamuserimages-a.akamaihd.net/ugc/2042989031190792657/F73A45A40AF841EF254E2E2E83A232CA26EEB18A/">
(Figure 2: Jumping from counterstrike)

The game’s controls are meant to have a high skill ceiling, so that players who are more experienced and more skillful will be able to navigate and combat enemies more easily.

### Player Progression ###

Progression in our game is designed to reward players with a sense of satisfaction in their in-game abilities. As players delve deeper into the lair of the Admin, they will unlock new weapons that greatly expand their combat options. Each new weapon caters to a distinct playstyle, whether that be melee or long-range. Weapons are introduced at key points in the story. The first weapon unlockable is a simple gun.

A pistol and shotgun will be the primary weapons for the player, with a pencil as a melee sidearm. Providing a variety that a player can experiment and play around with.

<img title="First level" alt="Alt text" src="https://github.com/feit-comp30019/2024s2-project-2-alphabeta/blob/main/Images/Weapons.png?raw=true">
(Figure 4: Weapon Model Examples)

There will also be an element of skill progression, as the player gets more familiar with the game, they will find it easier to evade enemies as they grow accustomed to the movement controls, and learn what weapons are most effective against certain enemies.

### Gameplay Mechanics ###


## Levels and World Design ##

### Game World ###
The world of Into The Abyss will be expressed as a 3D environment, viewed from the main character’s perspective. There will be two levels, the player will find themselves in the first after entering the Admin's tower, and the second level will be reached by a mysterious elevator that will spawn at the end of the first level. The player navigates for the most part blindly through a dark, jumbled and confusing world, only reaching their destination when a new elevator is found. These elevators spawn near the player when all enemies for that level are defeated. There is no map for the player to use, and the only guidance that is given comes from small blinking lights that guide the player to the next elevator.

The first level will be procedurally and infinitely generated using Perlin noise to allow for a sensibly structured yet random and confusing environment, and infinite chaos within the infinite world.

1. The first level is an office space that portrays familiarity and order which allows the player to be deceived into a sense of comfort before realising something feels off.

 <img title="First level" alt="Alt text" src="https://github.com/feit-comp30019/2024s2-project-1-alphabeta/blob/main/Images/image_2024-08-25_230238124.png?raw=true">
(Figure 5: Example of what the first level will look like)

2. The second level is a church with objects "glitched" into solid surfaces, an ordinary environment that has been corrupted into something abstract and bizarre. This level will represent the happiest time of the main characters life, twisted into something almost unrecognizeable.

### Objects ###

The game world is populated by low-poly objects such as desks, chairs, etc; to be changed depending on the current level. These serve as mainly decorative objects that also act as obstacles for both the player and other characters such as enemies. The player can also interact with certain doors, weapons and tools by clicking on them to trigger an animation and change the state of the interacted object.

### Physics ###

The game uses Unity’s rigidbodies system to simulate real-world physics and collisions in order to allow objects, characters and the player to react naturally to the environment around them. All objects (except for structural ones such as walls, ceilings and floors) and characters can be pushed and can push each other. If equipped, weapons and tools can be used to hit other objects and apply great force to them, especially guns which can send objects flying with the great force excluded by their bullets. Additionally, when a character dies they will fall into a ragdoll-like state that allows them to be moved around freely by other objects.

## Art and Audio ##

### Art Style ###



**Overall Aesthetic**: The game features a minimalistic yet unsettling low-poly art style, adding to the eerie, dreamlike atmosphere. The simplicity of the low-poly assets creates a sense of detachment and unease, reinforcing the game's uncomfortable tone.

<img title="Isolated elevator" alt="Alt text" src="https://media.istockphoto.com/id/1088914534/photo/an-old-elevator.jpg?s=1024x1024&w=is&k=20&c=qOkH0L2ZjmtG5BvIZjsZMk-n6X6Si0BPI-0ECANltFk=">
(Figure 6: Example of an elevator to the next level)

**Environment and Colors**: The game starts in an infinite office space, shrouded in perpetual fog that obscures the player's vision. This office is vast, empty, and repetitive, with long, monotonous hallways, and cubicles. The dark colour palette consists mainly of muted greys, blacks, and deep blues. Bright blue light will appear near elevators, standing in stark contrast to the darker surroundings. This is to guide the player toward the next objective while evoking a sense of coldness and detachment.


<img title="Eerie Atmosphere/lighting" alt="Alt text" src="https://cdn.mos.cms.futurecdn.net/uNEwCDpYeSshXdNUYnqpvM-1200-80.jpg">
(Figure 7: Example of blue light highlighting an objective)

Low, eerie lighting is a key visual feature. Like flickering lights scattered in the office space create unsettling shadows and abrupt changes in visibility, adding to the tension.

**Enemy Design**:

Variety of Enemy Types: We will introduce different classes of enemies with distinct behaviors and appearances that align with the surreal environment. =

Echoes: Enemies that are distorted reflections of Aidan, representing his fragmented memories. They mimic his movement pattern but have their own delayed rhythm.

Hollows: Victims whose memories were devoured by The Admin. With hollow and empty eyes, they move erratically and randomly pause to clutch their heads, as if trying to bring out their true selves. Implode upon death.

Phantoms: They feature red glowing eyes, which will appear as an unnatural glow amidst the dark fog. They appear and disappear in and out of the fog, only every now and then attempting to attack the player when they have their backs turned. Inspiring a primal fear to get the player more immersed in the world. 

Possible enemy interactions with the environment, since the procedural landscape is built on tiles, enemies (The Admin) could have the ability to modify it during combat.


### Sound and Music ###

1. **Initial Silence and Subtle Ambience**:  We begin with near silence, creating a false sense of calm. Minimal background noise, like faint wind or distant dripping water, will establish an eerie tension. This will make the sudden change in audio and visuals (like the flickering lights) more impactful.
2. **Flickering Lights**:  As the lights begin to flicker (inspired by this video) , subtle electrical buzzing and crackling sounds will accompany the flicker. These sounds will increase in intensity to build discomfort for the player.
3. **Approaching enemies**: To signal the player that the enemies are approaching, we will have distant footsteps sounds ( running sounds ).
4. **Gradual Sound Build-up**: As the player navigates the environment and starts facing the enemies, an eerie ambient track (selected from assets like Horror Elements) will slowly fade in, with volume gradually increasing as danger feels more imminent.
5. **Dynamic Audio Based on Proximity**: To guide the player and increase immersion, we’ll implement dynamic audio. Different soundscapes will be present in various areas of the environment: for example: silencing of the eerie ambient track when the player is closer to finishing the particular level. When the level is almost done, the player will go to the next level using an elevator so when player is:
   - **Close to the Elevator**: The sound of distant ‘elevator dings’ and metallic clanks will grow louder as the player approaches the elevator, providing an auditory cue. (inspired from elevator sound effects) This will be synced with a brighter blue light, subtly signalling the player's direction.

Thus, we aim to utilise 3D audio to create the illusion of sounds originating from specific directions that will enhance the player's immersion. For example, footsteps behind the player, eerie whispers from the side, or random distant noises can increase the sense of being watched or pursued.

### User Interface (UI) ###

1. **Main Screen**: Player can start or quit the game

    <img title="First level" alt="Alt text" src="https://github.com/feit-comp30019/2024s2-project-1-alphabeta/blob/main/Images/image_2024-08-25_231833229.png?raw=true">
  (Figure 8: Example of a possible main screen)
2. **Basic UI of gameplay screen**:
   - Total Timer (10 Minutes):
     - Purpose: The game has a fixed playtime of 10 minutes
     - Visibility: This timer is visible to the player in a discreet spot (top left screen), with a countdown animation.
     - Health Bar:
     - Purpose: The player will die if the health bar reaches 0.
     - Visibility: Positioned at the top right corner of the screen
   - Score:
     - Purpose: It shows the score that the player has gained while going through his memories.
     - Visibility: Positioned at the top right corner of the screen

3. Pause Menu:
    - This screen appears when the player clicks on the setting icon.
    - The player can pause the game ( the timer stops ), and can choose to restart or quit the game. The player can also adjust the sound levels of the game from here.

4. Game End Screen:
5. - As described earlier, the game has two endings:
   - The player loses and cannot save his wife
   - The player beats the game and is returned to the home screen

## Technology and Tools ##

The game will be created using Unity and tracked and managed using Github. Blender will also be used to create and modify any extra low poly models. For audio, Audacity will be used to mix in dialogue and music into the game. Anything further such as animation, scene design, etc will be done using Unity.

The game will be developed using the following software and tools:

1. **Unity**: The primary game engine used to create the game. While it is mandatory to use for this project, the team recognises its versatility, powerful features and wide support for 3D game development.
2. **Github**: Used for version control and collaboration over multiple different systems. While also mandatory, the team recognises its usefulness in rolling back to previously working updates, safety features and general project management.
3. **Blender**: Used for creating and modifying 3D assets in the game. It is open-source, robust and its easy tools are ideal for low-poly design.
4. Audacity: Used for audio editing, dialogue mixing and music. It is also open-source, and is known for its ease of use and broad range of tools in audio processing.

All software described above is free, with a notable amount being open-source.

## Team Communication, Timelines and Task Assignment ##

Provide a detailed plan of how you'll distribute the work amongst your team, and what communication channels will be utilised to facilitate discussions. You may wish to use a project management tool such as Monday.com or Trello to help you delegate tasks and track your team's overall progress.

The game has been split up into distinct workable sections between the 4 team members:

| **Will**         | **David** | **Ananya**      | **Alistair** |
|------------------|---------- |-----------------|--------------|
| World Generation | Story     | User Evaluation | Movement     |
| Shaders          | Boss      | Assets          | AI/Enemies   |
| Lighting         | Movement  | UI              | Audio        |
| Post Processing  |           |                 | Weapons      |
| Particle Systems |           |                 | Boss         |

Communication will be through Discord, and progress will be tracked through both Trello and Github. Each member will have a separate Github branch to work on.

## Possible Challenges ##

We as a team recognise the future possible challenges of this large project. First of all, the most obvious challenge lies in the time constraints for this project. With each of our own other classes, work and lives outside of this, there is going to be a lot of work put into reducing the scope of this game to a feasible amount alone. We cannot have any ideas that are too massive nor too complex as we need to be able to finish them alongside all our other work within the deadlines. This is why we are using tools such as Trello to track our progress and keep us up to date.

Secondly, there is the concern of using WebGL to run the game. Compiling this game into something that can be run purely over a feeble web browser on virtually any device means there is also a large constraint on the amount of computational resources we can use. This means reducing the size of the game world for better memory performance, using low-poly assets for better CPU and GPU performance and in general reducing the game down to a usable product.

Finally, there is justified fear surrounding making the game actually fun and interesting to play. If we lose sight of the bigger picture of this game and only focus on the individual parts, it could genuinely not be a good product in the end and we would have worked for nought. To prevent this, regular reviews of the game and its current progress will be had as a team to reflect on the current product, what we initially had in mind and what we ultimately are happy submitting.

## References ##

1. Image of Ultrakill's cover image, taken from the Steam page of the game ULTRAKILL: https://store.steampowered.com/app/1229490/ULTRAKILL/
2. Art taken from a steam guide on Counterstrike movement: https://steamcommunity.com/sharedfiles/filedetails/?id=2972053090
3. Taken from the article "Titanfall 2's Mobility Revolutionized Shooters - Or At Least It Should Have" by Cian Maher, published by The Gamer: https://www.thegamer.com/titanfall-2-mobility/
4. Image taken from our game
5. Image taken from prototype of our game
6. Stock photo of an elevator from the website Istock, credited to user "chainatp": https://www.istockphoto.com/photo/an-old-elevator-gm1088914534-292093369
7. Image taken from the article "Little Nightmares 2 Review" written by Stacey Henley and published on PCGamer: https://www.pcgamer.com/little-nightmares-2-review/
8. Image taken from prototype of our game



  


