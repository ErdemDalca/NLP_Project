## Genre

Action-adventure, Puzzle
**References:** Undertale, OneShot, Deltarune.

## Synopsis: 

>[!info]- What it is?
>This part of GDD provides a concise overview of the setting, allowing any reader to understand what to imagine while specific terms are mentioned in the text. For example, if we specify that the game setting is a medieval fantasy world, the reader will understand that when "weapons" is mentioned, it means swords or crossbows, and not futuristic laser weapons.

The setting of the EG6 game is a bleak world of a landfill on an arctic island, filled with pollution and leftover technologies. The player and his companion, a robotic penguin, explore this devastated landscape, collecting pieces and solving puzzles to find a route to salvation. Time on this island seems frozen, and nature has almost completely disappeared due to the terrible impact of pollution.

## Controls

>[!info]- For what?
>In later sections of the document, to associate a specific action with a button, you must specify the name of that button in triangle brackets.
>**Example:** To destroy an obstacle, the player must press button *`<Interact>`* while near the obstacle so that the character is facing in its direction.
>
>If we need to change a button that will be responsible for some action, it will be enough to change it in the table and not touch all the other places where it is mentioned.

### Keyboard

| Button          | Name             |
| --------------- | ---------------- |
| W / Arrow Up    | Up               |
| A / Arrow Left  | Left             |
| S / Arrow Down  | Down             |
| D / Arrow Right | Right            |
| E / Space       | Interact         |
| Esc             | Pause Menu       |
| Q               | Change character |

### Gamepad
| Button                      | Name             |
| --------------------------- | ---------------- |
| D-pad Up / L-stick Up       | Up               |
| D-pad Left / L-stick Left   | Left             |
| D-pad Down / L-stick Down   | Down             |
| D-pad Right / L-stick Right | Right            |
| Button South                | Interact         |
| Start                       | Pause Menu       |
| Button North                | Change character |

## Style

>[!info]- What is it?
>Style is understood in the broadest sense. Here we can add any concept art and references. Write down the details of how the game should feel, what emotions it should evoke in the player.
>
>From a gameplay point of view, in this section you should describe how the game works without touching on details. For example, how the game world is structured, whether it is divided into levels or an "open world", how movement between locations occurs. Can the character only walk? Or fly? Or drive a vehicle? Will you be able to pick up something in his inventory? Move things? Struggle? Use magic?, etc...
>
>This section is like a trailer for the game in text form, where we describe the player's capabilities. After reading the entire section, the reader should understand what the game will be about, but without going into details.

The game is made in 2D pixel art, with a Top-Down camera position.
The game world is divided into levels, each level has a specific set of screens, each screen is made of tiles. 
There is a "hub" in the form of a character's room, which you arrive at after completing a level (by collecting new piece).

The game should feel primarily like a puzzle, the environment should motivate the player to leave the island and should cause rejection by the appearance of an environment full of garbage. At the same time, the appearance of the character's room should motivate him to return there, create a feeling of security (like bonefire in the Dark Souls game series or the elevator at the end of the level in the Portal series).

During the game, the main character can interact with objects, but he will have disadvantages in the form of movement restrictions. He can break some tiles that prevent him from passing (like wooden trash), but this does not apply to all obstacles.
The penguin, on the other hand, has fewer options for interacting with the environment, but more movement options (it can swim where the player can't, light the way in a dark place, break tiles of ice, etc.)

The player's objective is to solve tasks by switching between characters and using their unique set of skills (almost like the levels in [It Takes Two](https://www.youtube.com/watch?v=GAWHzGNcTEw&ab_channel=ElectronicArts), but under control of a single player).

## Dynamics

>[!info]- What is it?
> Within the MDA framework, "dynamics" refers to the way players interact with game mechanics while playing. Dynamics are defined as how game mechanics lead to changes and evolution of the game experience over time. In other words, dynamics are the result of the player's interaction with the mechanics and subsequent changes in the game.
> 
> In the context of the MDA framework, we can say that dynamics is a higher level of abstraction compared to mechanics. Mechanics determine what actions are available to the player, and dynamics describe how these actions affect the course of the game, what consequences they have, how the game experience unfolds, and what emotional reactions are evoked in the player.
> 
> Thus, we can say that the dynamics are not simply a system of mechanics, but the result of their interaction during the course of the game.

The game cycle consist of the following actions: player needs to leave the character's room in search of a part to upgrade the penguin robot, goes through increasingly difficult levels using new mechanics, returns to the room to upgrade his companion in order to overcome more difficult obstacles and escape from the island .

If the player completes the optional activity of collecting pickable trash, both characters' power increases (they can break obstacles in fewer hits), and at the end of the game, the player can get a different ending in case of collecting all the trash in all levels.

## Systems and Mechanics

>[!info]- What is it?
> In this section we must write everything related to the logic of the game. There is no need to delve into the parameters of how long it lasts in seconds or how much damage it causes. Here we must describe the working principle of EVERYTHING that happens within the game.
>
> In terms of building the structure of the document, it is worth starting with the systems and then moving on to the mechanics.


>[!note]- Consejo
>
>Estoy seguro de que en España, como en muchos otros países, en el colegio/escuela te enseñan a escribir composiciones o ensayos, intentando cometer un mínimo de errores léxicos y estilísticos (por ejemplo, tautologías).
>
>Pero la documentación no es una obra de arte, aquí se fomenta romper las reglas de redacción de composiciones para evitar la grafomanía
>
>**Ejemplo:** 
>*`Cuando un personaje activa la habilidad de "Curación", el personaje recibe el buff de "Curación", que cura al personaje y restaura N unidades de salud.`*
>
>Esto puede sonar terrible desde un punto de vista estilístico, pero para fines de documentación, este es un párrafo muy bueno que se puede traducir fácilmente a [codigo](code_example.png).

### Systems

>[!info]- What is it?
>
>**El sistema** es una regla global que siempre funciona. Por ejemplo, un sistema de movimiento, un sistema para interactuar con objetos (el personaje SIEMPRE debe acercarse al objeto y hacer clic en el botón de interacción), un sistema de selección de nivel (el jugador hace clic en el ícono de nivel, se resalta en color, después de lo cual el botón "Confirmar" vuelve a estar disponible y el jugador se transfiere a una escena con el nivel apropiado), etc.

#### Companion System
This system affects two main sets of game mechanics: movement and interaction. It also indirectly affects other mechanics (for example, the behavior of the camera). That's why it is first on the list.

The game has two characters - a child and a penguin. Both differ in their ability to interact with objects and move. Switching between characters occurs by pressing a button.
Switching is possible only after  picking up a mechanical egg and collecting the first piece.

**Related mechanics**:
- [[#Switching Character]]

| Class             | Responsibility                                                                          |
| ----------------- | --------------------------------------------------------------------------------------- |
| CharacterSwitcher | Switches between characters by enabling/disabling the corresponding components in them. |

#### Movement System
The game has movable objects, these include moving obstacles, some pickable objects, and both main characters (a child and a penguin).

Movement occurs by pressing the buttons: *`<Up>`*, *`<Left>`*, *`<Down>`*, *`<Right>`*.

Moving objects use kinematic rigidbody type and custom collision detection. Also, each object has an additional vector in order to apply external movement to it (for example, when it is on a conveyor belt).

Both character controllers (child and penguin) are inherited from the moving object class.
The penguin controller uses two movement modes (this is not a State pattern!). 
When the penguin is not under the player's control, navmash is used to make the penguin follow the child, avoiding obstacles.

The system also includes conveyor belts.
A conveyor belt is an object with a collider isTrigger that applies an additional motion vector to all moving objects that enter it.
Conveyor belts can be controlled using buttons (change direction and stop their operation).

**Related mechanics:**
- [[#Walking Mode]]
- [[#Swimming Mode]]
- [[#Conveyor Belts]]
- [[#Penguin AI Movement]]

| Class             | Responsibility                                                                                                                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MovableObject     | Base class for the movable objects in the game.                                                                                                                                                            |
| ChildMovement     | Class for the child movement, inherits from MovableObject, but sets the input direction to the movement direction.                                                                                         |
| PenguinMovement   | Сlass for the penguin movement, uses NavMeshPlus for the AI movement and the MovableObject functions for the player controlled movement.<br>Uses enum Movement Mode to switch between Walking and Swimming |
| Collision Handler | Handle the collisions of every movable objects in the game.<br>Uses Raycast and Layer Mask.                                                                                                                |
| Conveyor Belts    | Class is used to move objects that are inside the trigger area of the conveyor belt.                                                                                                                       |

#### Interaction System
Characters can interact with the environment: press buttons, open doors, pick up objects, break obstacles. For each of these type of items, we have basic classes (button, pickable object, destroyable object).
Detailed information about each type of interaction is described in the corresponding section of each specific mechanic.

**Related mechanics:**
- [[#Destroy obstacles]]
- [[#Picking up items]]
- [[#Pressing buttons]]
- [[#Candies with hints]]


| Class                                           | Responsibility                                                                                                                |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| DestroyableObject, <br>+ByChild, <br>+ByPenguin | Contains the logic of objects that can be destroyed (changing the sprite, destroying the object according to the durability). |
| Character Damage                                | Determines the damage the character inflicts on destroyable objects. Increases it as trash is collected.                      |
| Character Interaction                           | Responsible for the logic of selecting items for interaction (using raycast). And contains a method to call the interaction.  |
| FloatingSelectArrow                             | A small script for the arrow prefab that points to the currently selected object.                                             |
| Button                                          | Base class for button                                                                                                         |
| Button Command                                  | Class to implement command pattern for combination of buttons.                                                                |
| Door Button                                     | Button child that calls function to open door (connected to it by SerializeField)                                             |
| Combination Door Button                         | Button child that uses a command pattern to enter a combination                                                               |
| Sequence Checker                                | Script that checks combination of Button Commands and opens the door if it is correct (match with pre-configured sequence)    |
| ClueTrigger                                     | Shows hint when we stand on object with this components                                                                       |

#### Save System
This system performs 3 main functions:
- Save information about collected, destroyed objects, open doors and pressed buttons.
- Change the state of these items when loading the level so that it is not possible to interact with them again.
- Store this information in the game folder when the game itself is disabled.

**To do this, the system uses 3 main scripts:**

| Class                  | Responsibility                                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local Object Handler   | Uses a structure with information about interacting objects in the level, updating this information as the game progresses for the currently active scene. When player changes scene, it saves information about scene progress to the global register. |
| Global Object Registry | Stores global information about the game in the form of variables (whether the penguin is unlocked, how much trash the player has collected, etc.), as well as a list of all level states for each scene.                                               |
| Saves Manager          | Saves information to the game directory, converting the level state structure into a JSON file. Also makes deserialization to load level from JSON.                                                                                                     |

#### Camera System
[Unity Cinemachine](https://unity.com/unity/features/editor/art-and-design/cinemachine) is responsible for the behavior of the camera in the game
Camera movement is limited within one level or part of a level; when the character reaches the edge, the camera rests on the border of an invisible area.

In moments when it is necessary to show the player a part of the level that is distant from the character, a script is used that moves the camera according to a pre-prepared scenario.

### Mechanics

>[!info]- What is it?
> 
> **La mecánica** es una acción separada, una pieza a partir de la cual se forman los sistemas. Por ejemplo, el sistema de movimiento tiene una mecánica "correr" y una mecánica "nadar". Nuestra tarea es describir la mecánica para que podamos imaginar su código.

#### Walking Mode
We move the current character by giving him input using a [New Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/index.html). 
Movement is carried out in 8 directions (2 axes and diagonals) sin acceleration.
This type of movement applies to the child and the penguin when they are on solid surface tiles (not liquid).
#### Swimming Mode
Movement occurs by changing the velocity parameter, using linear interpolation (to create smooth acceleration and deceleration).
This type of movement only applies to the penguin, and only when it is on a water tile.
#### Conveyor Belts
Conveyor belts are objects without a rigid body component, just collider isTrigger. They have two main parameters - the direction of “pushing” and speed.
When a moving object enters their zone, it applies a vector (direction * speed) as an additional to the moving object's movement vector.
Uses animator for movement animation in the form of arrows on belt surface that indicate the direction of the conveyor belt.
#### Penguin AI Movement
To make the penguin follow the child automatically, we used [NavMeshPlus](https://github.com/h8man/NavMeshPlus).
When implementing this mechanic, we used several tricks. To prevent the penguin from passing through destructible obstacles, we bake a map with a “walkable” zone at the beginning of the level, taking into account the previously destroyed obstacles. We also clear the navmesh map and bake it again every time we destroy another obstacle to update possible paths.
#### Switching Character
After collecting the first part, the player can change the character by pressing the button:
 *`<Change Character>`*.
When a child is under the player's control, the penguin follows him automatically. When the player controls the penguin, the child does not move.
Switching characters is accompanied by a small arrow that appears above the currently selected character.
#### Destroy obstacles 
Both characters can destroy objects by pressing *`<Interact>`*. To select objects we use raycast. If a character looks at an object in front of him that is close enough, the object is marked as "Selected" and a corresponding prefab appears above it, indicating the possibility of interacting with it.
Destroyable obstacles are divided into two types:
- Destroyable by a child (wooden trash)
- Destructible by penguin (ice shards)
If a character tries to destroy an object that he cannot destroy, it makes a corresponding sound and shakes a little.
Destruction occurs by removing a hidden durability parameter.
In this case, the sprite of the object changes and cracks appear on it.
The player can increase the damage that characters deal to destructible objects by collecting trash in levels.
#### Picking up items 
Collecting items occurs through a collision with the collider of the player and the item.
There are two types of items in the game that the player can pick up: trash and pieces.
By picking up trash, characters become stronger and can destroy obstacles with fewer hits.
By picking up pieces, the player marks the level as completed and unlocks a new ability for the penguin robot. 
#### Pressing buttons
Pressing buttons occurs in the same way as trash collection - at the intersection of the character collider and the button.
The basic logic of the buttons is to change the sprite and play a sound file. The specific implementation depends on what object these buttons can be associated with.
The button can be connected to the door. There are two types of connection:
- Single button that opens the door with one press.
- Button combination. Here the player is required to enter the correct combination. We use the command pattern to implement these buttons, which allows us to remember the sequence in which they were pressed, in case of an incorrect combination, the buttons return to their original position one by one with a slight delay, giving the player a reminder of which combination was incorrect.
The player can read hints for combinations using candies (see [[#Candies with hints]]).

Buttons can also be connected to [[#Conveyor Belts]] (they can change their direction or turn them on and off).

#### Candies with hints
While on an object with candy, the player can read a veiled hint about the order in which to press the buttons. In case he forgot it, he can always go back and read it again. This is not a pickable object.

## Parameters

>[!info]- What is it?
>
>These are all (often) numerical indicators, sometimes colors and other attributes of objects or their behavior, which we will change hundreds of times during development. This includes all dynamic data, from the character's movement speed to the smoothness of the camera transition from one screen to another and the time it takes to break an ice tile.
>
>They should be separated from the mechanics section, because this will make script design easier (knowing in advance which parameters should be highlighted in SerializeField). This will also allow us to create parameter sets already prepared for testing (presets) and quickly switch between them.
>
>The value of the parameters should not be written before the prototype, as it is better to test them in practice and point them here.

## Design

### Narrative:


### Art:

**Main Menu background**

![[MainMenuBackground.png]]




### Animations:

**Main character animation**

![[ChildAnimations.png]]


### Sound:
  
  

### Music:
  

### Levels:

  
## Progression

>[!info]- What is it?
>A very small section that indicates the sequence of opening levels, unlocking new mechanics and story events.
  
## Interface




  
  