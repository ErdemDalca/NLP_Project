# Game Basic Information

## Summary

Space Chase is a two player racing game with platforming elements. This game takes inspiration from
[Celeste](https://store.steampowered.com/app/504230/Celeste/),
[SpeedRunners](https://store.steampowered.com/app/207140/SpeedRunners/), and [Super Smash Bros](https://www.smashbros.com/en_US/). Players have to race against each other to reach their ship first, however they would need to collect energy on the way to full charge their ship to win. A unique aspect is that the player can sabotage their opponent such as throwing them off the platforms or into spikes. Players can also dash, which can be utilized both for movement and offensive ability (stunning the player).

## Gameplay Explanation

The main goal of the game is to reach your ship while collecting as much energy as possible to refuel it.
However you will be competeing against an opposing player. Mechanics such as grabbing, throwing, and dashing are at
your disposal to gain the upperhand against your opponent. Movement is also a huge part of this game and
serves are a core gameplay mechnaic. Borrowing the omnidirectional dash from Celeste it servers as an
extra tool for the player to traverse the deadly level and out run their opponent. There are also power
ups to level the playing field such as a speed boost or shrinking.

We suggest bringing a friend to play the game with. Two controllers are recommended. Start off by going to the controls menu to get familiar with the player's abilities. Players have the following abilities:
- Grab (press key to grab, hold key to hold, release key to thow): Different throw directions if holding up/down/horizontal/diagonal. You can move/jump while holding. You can input mash out if you're being held.
- Dash: 8-way directional dash. Dashes can stun players.
- Jump: Can short hop or hold jump
- Fast fall: Hold down while in the air

Once both players are ready, go back to the main menu and play the main game!

If you want to test the game's mechanics or experiment, feel free to do so in the playground level. You can find it in the extras menu.

Press the escape key if you want to restart/exit the main game or playground.

# Main Roles

- Producer: [Carlos Huang](https://github.com/cahuang10)
- Movement and Physics: [Karim Shami](https://github.com/BoiPlex)
- Game Logic: [Jason Zhou](https://github.com/khromeengine), [itch.io page](https://khromeengine.itch.io)
- User interface and input: [Patrick Le](https://github.com/patple)
- Animation and Visuals: [Raghav Bajoria](https://github.com/RaghavsScarletSplendour)

## Producer (Carlos Huang)

### Organization Work

- To help brainstorm ideas for a game, I hosted a couple of meetings during the first week. During the meetings, I suggested ideas such as implementing a point system and power-ups. After the first week, there was no longer a need to meet online, but I would occasionally check in with my groupmates.
- I also created a GitHub repository. This allowed everyone to push their work from their own branch to the main branch. Ensuring that everyone worked on their own branch was helpful, as it allowed them to focus on their respective parts.
- It was important to make sure everyone followed the deadlines based on the schedule I helped create at the beginning of this project. The schedule was effective because people started working on different tasks, and it was mostly followed by everyone.

### Implementing power-ups

There were two aspects of the game that people were not working on: the power-ups and the enemies. Due to the limited amount of time given for this project, I decided to implement the power-ups. I created a base class for all the power-ups.

- The first class I created was `base_powerup.gd`. The class had an enum that assigned the six types of power-ups we have. This class also handled the player entering and picking up the power-ups. With the help of Karim Shami, we made the power-ups float up and down, which gave them a better game feel.
- I also created the `powerup_manager.gd` class. This class essentially applies and removes the effects of power-ups. I wanted to make a centralized class to handle the complexity of the power-up system. Additionally, I ensured that when the same power-up is picked up again before it runs out, the game increases the duration of the power-up's effect.
- Lastly, I made the `randomizer_powerup.gd` class. This class was more challenging for me because I was not familiar with animations and the preload function. For the animation, I combined all the sprites we had for the different types of power-ups and created an animation that cycles through the sprites. This is similar to Mario Kart's power-ups, where the power-up shuffles until the player picks it up.

### Poweru-ps:

#### GetBig:

![Recording2024-12-13224827-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c3902754-2400-4d69-8a32-32ff9f131fc0)

This power-up grants the player the ability to double in size while gaining a strength boost that allows the player to throw opponents further.

#### GetSmall:

![Recording2024-12-13222122-ezgif com-video-to-gif-converter (2)](https://github.com/user-attachments/assets/00eaf34c-960f-4e2c-88ba-a3afcd3ec77a)

This power-up grants the player the ability to shrink in size while gaining the ability to double dash, which can be useful for escaping enemy grabs and traps.

#### Speed:

![image](https://github.com/user-attachments/assets/306dc0cf-f420-4978-8aa1-20b22b2e6983)

This power-up increases the player's movement speed.

#### Jump:

![image](https://github.com/user-attachments/assets/8cf3edcd-ae67-4046-9783-fea9da55a06d)

This power-up boosts jump height and distance.

#### Shield:

![Recording2024-12-13223635-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c2787735-cf8f-48c6-b4c0-538ea5dee2bd)

This power-up prevents the opponent from grabbing the player. It is a one-time-use power-up. Finally, it creates an vortex-like aura around the player. This was made using CUPparticles2d with a texture `effect_4.png`.

#### Energy:

![image](https://github.com/user-attachments/assets/330b7131-d44a-4ab1-a95d-8957c44c638d)

Although not exactly a power-up, it behaves like one. When players collect this, they gain energy points to charge the ship at the end of the game.

## Movement and Physics (Karim Shami)

### Collision Masks & Layers

Before implementing the game's physics I started by outlining the collision layers that will govern what collides with what. It's imperative the collision layers are distinct and useful:

- Layer 1 (Solid ground): All solid ground tiles exist in this layer, which enable players to collide with the level's solid ground/walls. This collision is also used to kill the player if they're found inside solid ground.
- Layer 2 (Platforms): Platforms exist on their own layer to allow players to conditionally stand on them
- Layer 3 (Hurtbox): Allows hurtboxes to be detected by hitboxes (killing the player) and grabboxes (grabbing the player)
- Layer 4 (Hitbox): For hitboxes such as trap tiles, death pits in the level, and the walls of aliens.
- Layer 5 (Grabbox): Allows grabboxes to be detected by other grabboxes for grab collisions (grab teching)
- Layer 6 (Impassable by ghosts): Used by the world border to prevent ghost players from exiting the autoscroll camera's frame
- Layer 7 (Traps): Trap tiles exist in this layer to be detected by hurtboxes to kill the player.

### Player Controller/Physics

Given our game is both a platformer and versus game, we couldn't rely on standard physics conventions. While platformers typically involve acceleration/friction, I made the design choice of not using acceleration/friction. The main benefit of constant velocity is that the movement feels very tight and responsive. Our fast-paced versus platformer needed to have movement that feels responsive but also chaotic. This is achieved by using instantaneous velocity for all movement. It makes for a tense but fun experience for both players to have instant control over movement while having to react to the other player's instant movement, contributing to the chaos. The no acceleration rule doesn't apply to gravity.

I outline each of the player's major movement/physics mechanics, all of which are implemented in [player.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/player.gd). Due to the scope of our game I wanted to keep all the movement mechanics in 1 script for easy lookup (using comments as documentation). The only exceptions are [grabbox.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/grab_box.gd), [hurtbox.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/hurt_box.gd), and [hitbox.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/hit_box.gd), which are scripts attached to Area2Ds, similar to exercise 1.

A playground scene that's ouside the main level is used for testing purposes.

**Horizontal movement**

Players can instantaneously move left or right by simply setting their x velocity to their speed times horizontal direction.

![run](https://github.com/user-attachments/assets/a328a550-3799-432a-b97c-1bc71011800b)

**Jumping**

I wanted to give players more control with jumping, where players can either short hop, hold jump, or anything in-between. Holding jump reduces the player's gravity, which increases jump height and also enables the player to fall slower if jump is continued to be held. Short hops can be even shorter if combined with the fast falling mechanic.

![jump](https://github.com/user-attachments/assets/48c2a1ae-4af9-4dfa-bf8e-74a9422b4c21)

**Fast Falling & Going Down Platforms**

Holding down enables the player to fast fall, which increases the player's gravity, giving the player even more movement options. This could help the player regenerate their dash, jump sooner, avoid obstacles, and even lead to some combos.

Fast falling leaves a white trail behind the player.

![fast_fall](https://github.com/user-attachments/assets/250e1ea0-f21a-4cd2-9ce3-9283281fb01c)

![platform](https://github.com/user-attachments/assets/ac908bb2-78d3-4d61-b918-cda02836d9d9)

**Grabbing**

Each player can try to grab the other player be temporarily enabling the grabbox. If a grabbox detectes the other player's hurtbbox, then the player holds the other player. However, if a grabbox detets another grabbox, then a grab tech occurs, stunning both players in their opposite directions.

![grab](https://github.com/user-attachments/assets/18c2ed30-6135-42ea-8d6f-7f8950497e1a)

![grab_tech](https://github.com/user-attachments/assets/2209b80a-960c-4fb4-85cd-522424b56b07)

**Holding a Player**

While the grab button is held, a player can hold the other player for `HOLD_TIME`. During this time the player can move and jump around freely, enabling for devious throw setups. The only restriction is that the player can't dash while holding another player.

![hold](https://github.com/user-attachments/assets/9e89413a-efc7-499f-ab00-223c3ea06837)

**Throwing a Player**

Releasing the grab button throws the held player. If the grab button is tapped (quickly pressed and released), then the throw is done instantly out of grab. After gameplay testing, I figured it would be better to give the player more throw options. Holding up throws the player up, holding down drops the player in front (grab release), holding diagonally up throws the player in that same direction, and holding horizontally throws the player in that direction with less height. Each type of throw is configured based on direction and x and y velocities. If no direction is pressed then the throw defaults to horizontal. 

![throwing](https://github.com/user-attachments/assets/82f2890e-50a4-4df2-bdd3-5468778c027d)

**Being Held by a Player**

After testing, I found it to be unfair to have no control while being held, so I added input mashing, enabling the held player to escape faster. This is achieved by reducing the hold timer for every input the held player presses. Once the hold timer ends, the held player is released just like a throw where down is being held.

Being held makes the player sprite flash yellow, while input mashing makes the player flash purple.

![mashing](https://github.com/user-attachments/assets/f6dd097c-e2f9-456d-bc3d-403ab27044aa)

**Dashing**

Given our game is a platformer I had to make sure the dashing felt good but also useful for versus.

In terms of movement I took inspiration from Celeste, one of my most favorite platformers. Dashes last for `dash_time`, where they apply a constant `dash_speed` velocity. Dashes are 8-way, enabling for discrete D-pad-like movement. At the end of the dash, just like Celeste (at least while in the air), the player's velocity is taken away with a damping effect of 0.4. Jason helped with this as I originally planned to set velocity to 0 rather than multiplying it by a damping effect, which feels much nicer, giving the player more air time. The dash recharges when touching the ground.

I incorporated versus into the dash by making it so players can stun the other player by dashing into them. If players dash into each other at the same time then both players are stunned.

Dashes leave a dash trail behind the player.

![dashing](https://github.com/user-attachments/assets/45fc2ae4-8dbc-4ece-87a8-0fe7ce4619df)

![dash_stun](https://github.com/user-attachments/assets/227fa02d-ab83-43ac-a579-65ef8fc373ca)

![dash_collision](https://github.com/user-attachments/assets/976b59f4-c864-4ddb-a60b-80891409b708)

**Death**

As discussed with Jason and the rest of the team, our game felt best with no health system. So the player is instakilled by any hitbox (as detected by hurtbox). I implemented the death mechanic since it's a prerequisite for the player's ghost movement. The player is dead for `RESPAWN_TIME` before spawning in as a ghost.

![death](https://github.com/user-attachments/assets/b72104c5-ccdd-4e58-838c-dbcfaa1e704b)

**Ghost Movement**

As a ghost, players don't have gravity. Ghosts have 8-way movement, similar to the heart in Undertale. Ghosts don't have collision since the `_disable_interactions` function is called, meaning they can phase through solid ground and can't be killed. The only collision ghosts have is for the world borders (layer 6), as to not let ghosts escape the auto scroll camera's frame. During `GHOST_TIME`, ghosts can freely pick where they want to respawn, giving the players more control and making it more fair. We came to the decision to allow ghosts to dash with no cooldown, allowing ghost players to have faster movement for picking their respawn location. One issue I noticed was that if you try to spawn inside solid ground then you get stuck (since normal players collide with solid ground), so I made it so that the player dies if this occurs.

The ghost sprite blinks to indicate that the player will soon respawn as normal.

![ghost](https://github.com/user-attachments/assets/4c0f139a-da5c-4093-85a8-bd557527f64d)

**Stunned**

Players can be in a stunned state from the various interactions (grab teching, dash stunning, throws, etc). This stunned state is initiated by the `_start_knockback` function, which takes in a force (Vector2) and the duration of the stun (float). The force is a Vector2, which decides the stun's direction and magnitudes. It's called force, but in actuality it's a constant velocity applied for the stun duration.

**Other**

I wanted to make sure the player has a variety of movement options, including combos. Here are a few combos:
- Up throw into jump and dash up
- Diagonal down dash into grab
- Side throw into side dash
- Grab release (release grab while holding down) into grab

Given I was in-charge of the players' movement/physics, I wanted to make sure that everyone had the proper tools to implement their parts, so I added a bunch of conditional variables that are updated based on player state. For example, these conditional variables played an essential role in updating the player's animation state tree.

![image](https://github.com/user-attachments/assets/fe61feff-3457-485d-8b24-0e029c6f19b9)

### Level Terrain & Other Collisions

The other part of the game's physics is the level terrain itself. I managed this using various tilemap layers:

Tilemap Layers

- Background: No collision layer. Exists the furthest back and is purely visual.
- Midground: No collision layer. Exists ontop of the background and is also visual.
- Solid ground: In the solid ground collision layer (layer 1). Players collide with solid ground tiles. In addition to basic square tiles, I added slope tiles, which have a triangular collision shape, allowing players to run up/down them.
- Platform tiles: In the platforms collision layer (layer 2). Just like standalone platforms but with tiles. These are used for the bridge tiles so that players can fall down them.
- Trap tiles: In the traps collision layer (layer 7). Players are instakilled when colliding with trap tiles. A script is used to define it as a `TrapTileMapLayer` type for detection by hurtboxes. This tilemap layer acts as a hitbox but with tiles. 
- Foreground: No collision layer. Exists on top of everything else and is visual.

![image](https://github.com/user-attachments/assets/b5cc5319-ce7d-46cf-9569-da3dcf8c9cba)

## Game Logic (Jason Zhou)

![The core game design document from the initial plan.](ExampleImages/core_gameplay_design.png)

As the head of Game Logic, I was in charge of implementing various systems overseeing game states and data and other
backend parts that are required for the game to function. To this end, I designed and implemented the [GameStateManager](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/game_state_manager.gd)
singleton / global script, the [charging stations](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/charging_station.gd),
and the [camera](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/autoscroll_camera_controller.gd).

Since Game Logic is important to get working sooner rather than later, most of my code on Game Logic was written
in our first week of work, including most of the GameStateManager and most of the camera. The charging station and
related logic for charging in the game state were worked on but incomplete until the last week when our game was near completion.

While I wrote most of the code in the first week, I continued to update and fix my code according to my team's needs over the span of the project.
Details for this will be provided in the following sections. I also continued to consult for my team to make sure they can fulfill their roles
when working on systems related to game state, particularly with Patrick, our UI lead. Occasionally, I redesigned game objects to be better
integrated with the rest of the game.

In this project, I followed no particular design pattern, but tried my best to keep code free from dependencies that might break the game.
This is especially important, as the game state is very often accessed by many different objects.

I originally planned to also implement menus, cutscene, powerup, and enemy managers as per our initial plan, but:

- Menus and level management were implemented by Karim with an add-on with the first build of our project. Most of the menus were made by Patrick and Karim.
- Cutscenes were designed and implemented by Karim as the narrative designer.
- Carlos, our producer, implemented the powerup manager.
- We ran out of time to work on enemies and integrate them into our level.

### Game State Manager

The GameStateManager is primarily responsible for handling game data for player energy and camera position (and by extension level progress).
For player energy, it stores each player's energy separated into a Vector2 and has many functions to manage energy like set, get, and add functions.
For level progress, the game state manager is updated with new values related to level progress when the camera moves forward and contains
a get function for our progress bar in the HUD.


The GameStateManager also contains constants that are used for many of the game's objects, such as the player ID enumeration, player energy capacity,
and the charging threshold for winning. To allow game objects to easily influence the game state, the manager contains many global signals related to
energy, players, and level state.


This script was gradually updated throughout our project, with new additions whenever our team needed more access to certain parts of the game state. Originally, 
we didn't have signals in the manager, but I added them to more easily coordinate the rest of the game.

### Charging Station

The ChargingStation class and object is the win condition for the game. We developed the game fairly linearly, so we didn't get to the ending sequence
until around the last week of work. Because of this, I developed but never tested the code for the charging station in the beginning. There was a decent
core idea, and as it turns out, most of the code was functional as it is. As we got to making the ending sequence, I finished the code for the charging station
by fixing some bugs, changing the charging algorithm from being proportional to constant, and integrating overcharged player energy into the algorithm.


A charging station is assigned to a player through an export variable and stores its own charged energy. In hindsight, the role of storing the charged energy
could have been left to the GameStateManager, but by the time I realized, it was a bit too late to refactor. The charging station is unlocked when the game is in the final zone,
and gains charge through proximity to its assigned player if the player has energy. To do this, it emits a request_charge signal, which is caught by the GameStateManager.
The proximity is indicated by a circle of particles that I designed in the players' colors.

### Camera

The camera design that we landed on initially was an autoscrolling pushbox camera. Essentially, we have a camera that moves forward automatically and moves
forward if a player pushes on the boundary. This is done by getting a push line position as a ratio of the viewport width (x) and running checks on an array
of exported players in process, and obviously, it autoscrolls by moving forward every frame.


There were a few simple but important changes to the camera during development. While designing the camera, I noted that we needed consistency for the GameStateManager's
position variables, so I standardized each position to consider the right border of the viewport. During gameplay testing, I noticed that the screen was too disorienting when platforming back and forth along the push line, so I added a linearly interpolated speedup zone to the camera. This is done similarly to the push line, by getting another line by adding a constant x to the push line. The actual mechanism of the speedup zone is that the autoscroll speed is increased by a linear interpolation between 0 and any far enough player's speed, where the weight is a the player's distance between the speedup and push line. In effect, as the player gets closer to the push line, the camera will speed up
gradually until they reach the push line.


A weakness with our camera design is that it really only works to the right. Significant changes would need to be made for it to function in any other direction. To get around
this, we designed our entire level where we only go right. It's a solution that's employed in many games, but I think we could introduce a much bigger variety of gameplay
if we could change camera directions, assuming we designed levels around it as well.


The camera signals to the GameStateManager whenever it moves, to update game state for our progress bar. After the camera reaches the end zone, it similarly signals
to the game state to intitialize the end sequence.

## User interface and input (Patrick Le)

### Main Menu

![main menu](ExampleImages/mainmenu.png)

Karim Shami (Movement and Physics) and I implemented the `menu_manager.gd` script which
organized and manages the whole menu system for our game. In there every menu state is declared as a enum and handles key features such as changing and entering between menus. Futhermore an addon was used to manage the multiple menu scenes. Helpful functions such as `change_scene` allowed us to move between menu states while also adding animated transitions. Most of the menus used are children of the menu manager. So `@onready var menu_manager: MenuManager = $".."` was very usful accessing functions within menu manager when changing menus. The structure of each menu scene has similar formatting with each other. Being some form of vbox container with a set of buttons, each withtheir own signal controlled by a script for that scene. Within each menu, besides the start and quit,
there is a "back" button which takes the player to last previous menu. Also each menu has an animated background, this was done by using a TextureRect and creating a shader to automatically scroll the texture, giving it an animated look.

### Controls Menu

![volume/setting menu](ExampleImages/controlsmenu.png)

For the controls menu it has all the keybinds for each player as well as the controller inputs. All the spirtes were contained in a Hbox conainter for easier editing and formatting. The only button that was in the controls menu was back which allowed the player to go to the main menu. The addition of having the players test the movement in the controls menu was both implemented by Jason Zho(Game Logic) and Karim. This was done by adding the two players to the scene and adding invisible barriers.

### Settings Menu

![volume/setting menu](ExampleImages/volumemenu.png)

This menu would lead to the sound setting menu where the player could adjust the master, music and sfx of the game. Jason implemented the sliders which was built into godot. The script would adjust the sound accordingly, such as updating the bus volume to the current slider value or muting sound when the
slider is at zero.

### Pause Menu

![pause menu](ExampleImages/pausemenu.png)

For the pause menu it was similarity built like the main menu, however it is not managed by the
`menu_manager.gd` thus not it's child. The 3 buttons that make up the pause menu are resume, restart, and quit. Using
`paused` boolen that is already in godot a function was made that pauses the current
scene. The pause menu is binded to the escape key so upon pressing it the current screne will be
paused and the [menu will be made visible](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/e1394f4026841682ba1f7e9b6818259c7c52892e/space-chase/scripts/Menu%20scripts/pause_menu.gd#L27). If the player chooses to resume the scene will be unpaused
and the game will continue. For the restart button the game is unpaused and the current scene is
reloaded thus resetting any progress done. As for the quit, it will take the player back to main
menu. For the blured background of the pause menu a ColorRect was used with a shader to give the
blured effect. The whole pause menu scene was added to the autoscrolling camera since it allowed the pause menu to be in
view of the camera at all times when the player pressed pause. Also the z of this scene was placed at 11 to make it appear in front of all the objects in the camera.

### Ending Scene

![ending scene](ExampleImages/endmenu.png)
The ending scene was created with the help of Karim who created the cutscene. Once the cutscene ends the name of the player will appear as well as a quit button to return the player back to the main menu.

### In-Game UI

![energy player bar](ExampleImages/energybar.png) ![level progression bar](ExampleImages/progressbar.png)

There are two main aspects of the in-game UI. The level progress bar and the player energy bar. Both used functions from the gamestate manager
to get the current level progression and the player's energy. The game state manager was implemented by Jason. Using the [`get_level_progress`](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/cf6b6518055fa3b0b0419af4be64a5942517d500/space-chase/scripts/game_state_manager.gd#L129)
function I was able to display the current's level progress on the bar at the top of the camera. While the energy bar of the player used a similar format of using [`get_player_energy`](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/cf6b6518055fa3b0b0419af4be64a5942517d500/space-chase/scripts/game_state_manager.gd#L110)
from the game state manager to display the current energy of each player. The function simply returns the energy of the player ID passed through. Futhermore
the player would lose a fixed amout of energy upon death and that lost amount would be given to the other player. To implemente this the [instakill](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/cb12d3fa9054d308f30a1e9c84a88861d3687b77/space-chase/scripts/player.gd#L261)
function inside the `player.gd` was modified so that players who died would have lost energy and the oposing player would have gained some. The scene created for both the player energy and progress bar was made in a similar format. Where a TextureRect was used with the progress bar placed inside of it. The TextureRect would be loaded with a
specific sprite to give the bar more detail.

### Input Devices

This was implemented with the assistance of Karim. He created a player [controls script](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/7572aeca99ce3adfedc336fae82fce82ea16661b/space-chase/scripts/player_controls.gd#L1) where each player
had their own dedicated control list and inputs. Also in the input map settings you could add different devices. This allowed it the game
differentiate between two controllers. As for keyboard the player 1 was WASD was used while having F as grab and G being the dash. While player 2
used the arrow keys or IJKL if they didn't have arrow keys Comma was used for the grab, period was the dash and slash was for space

### UI Resources

- [How to make a Scrolling Background in Godot 4](https://www.youtube.com/watch?v=TMeT541OLPA&t=78s)
- [Make a Pause Menu in Godot in 5 Minutes!](https://www.youtube.com/watch?v=e9-WQg1yMCY)
- [Godot 4 Main Menu Beginner Tutorial](https://www.youtube.com/watch?v=vsKxB66_ngw)

### Assets used

- [Menu background](https://space-spheremaps.itch.io/pixelart-starfields)
- [Pevel progression bar and player banner icons](https://mattwalkden.itch.io/free-space-runner-pack)
- [Player energy bar](https://adwitr.itch.io/pixel-health-bar-asset-pack-2?download)
- [Parts of the player banner](https://bdragon1727.itch.io/basic-pixel-health-bar-and-scroll-bar)

## Animation and Visuals (Raghav Bajoria)

### Player Animations

The player character has a wide variety of animations designed to enhance gameplay and create a dynamic experience. These animations include:

- Idle: A static yet engaging pose to signal inactivity.
- Running: Basic running
- Jumping: Basic jump
- Dashing: A streak of orange behind the playe
- Grabbing: Player tilts to the right or left when pressed
- Held/Holding: Player holds the other player on top of their head
- Fast Falling: dash animation downwards
- Ghosting/Respawning (as Ghost/Normal): Player becomes opaque and washed with white
- Stunned: Displays the player's vulnerability when hit or sabotaged.
- Death (Die): Player shrinks when dead

These animations, though simple in implementation, contribute to the competitive and high-energy tone of the game. The animations were implemented using a state machine to seamlessly transition between different player actions. Player feedback reported that the animations felt very satisfying.

![Animation_tree](ExampleImages/animation_tree)

![image](https://github.com/user-attachments/assets/226d39f0-882c-4753-8223-d046b0372e14)

### Cutscene Animations

Cutscenes enhance the game's storytelling and immersion with animations such as:

Explosions: Spaceship and world explosions
Spaceship Movement: Spaceship movement to demonstrate entering, fighting and leaving the scene

Karim Shami played a major role in creating these animations, ensuring consistency and visual flair. Raghav helped with adjusting certain animations to provide a better visual experience.

### Sprites and Tilesheet

The sprites and tilesheets used in Space Chase were primarily sourced from pre-downloaded assets, ensuring high-quality visuals while saving development time.

These included:

- Character Sprites: Used for player animations like running, dashing, grabbing, and more.
- Environmental Tilesheets: Created the dynamic and visually distinct environments, such as platforms, traps, and backgrounds.

Karim Shami played a key role in helping find and implement assets, ensuring they aligned with the game's fast-paced and competitive aesthetic. Minor modifications were made to some sprites (e.g., grab animation) to better fit the gameplay mechanics.

All assets under [License.md](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/License.md)

### Challenges

The most challenging part of the process was setting up and fine-tuning the animation state machine, ensuring smooth and logical transitions between different states.

### Feedback and Iterations

Adjustments were made to the grab animation for smoother transitions based on playtesting feedback.
Overall, animations remained consistent with their initial designs.

### Audience Reception

The dash animation stood out as the most impressive feature, garnering praise for its visual impact and gameplay utility.

# Sub-Roles

- Press Kit and Trailer: [Carlos Huang](https://github.com/cahuang10)
- Narrative Design: [Karim Shami](https://github.com/BoiPlex)
- Audio: [Raghav Bajoria](https://github.com/RaghavsScarletSplendour)
- Gameplay testing / Level Design: [Patrick Le](https://github.com/patple)
- Game Feel & Polish: [Jason Zhou](https://github.com/khromeengine)

## Press Kit and Trailer (Carlos Huang)

## Trailer

I made a trailer using DaVinci Resolve. I came up with interesting text to describe what was happening during the trailer.
I recorded many trial gameplays with a friend so the audience could get a sense of what the game is about.
I looked for interesting audio I could use as background music and ensured that we had the rights to use it.

Here is the link to our [trailer](https://youtu.be/sAVLEPqOCx0)

## Press Kit

For the press kit, I decided to create it using Notion. I like its easy-to-use interface. I created a logo for our game along with a slogan. I added some important details about our game. I also took screenshots of parts of our map that I felt were important to include in the press kit.

Here is the link to our [press kit](https://deep-spleen-40e.notion.site/Space-Chase-156a4264007680478aeacbd30d0a2188?pvs=4)

## Narrative Design (Karim Shami)

We decided on the theme of our game before writing our game's initial plan. We wanted our game to be space-themed, where players fight to escape a planet.

### Intro Cutscene

Intro Narrative: Themed in space, 2 astronauts in spaceships encounter a planet. There is disagreement on who found it first, so they argue about it. The argument escalates into both spaceships ramming into each other, causing an explosion. The spaceships get damaged, causing them to both fall and crash into the aforementioned planet.

I implemented this intro into the game through the intro cutscene. I thought about using a similar scheme to exercise 1's cutscene commands, but I decided against it since it wasn't worth the added complexity, especially since our game's intro isn't directly linked to the main game scene. In a separate scene, I used a single animation player to play the intro cutscene by moving around the necessary sprites and animations, heavily relying on rotation, scale, and transparency. I made sure there was no text in the cutscene, which makes the cutscene's story accessible and up to interpretation. The menu can enter the intro cutscene. At the end of the cutscene animation, the game leaves the scene and enters the main game scene. The cutscene can be skipped by pressing the escape key or the start button on controllers. The cutscene logic is implemented in [intro_cutscene.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/intro_cutscene.gd)

![intro_cutscene](https://github.com/user-attachments/assets/c776e247-a603-4b5b-b64b-d4984e960f45)

### In-Game Narrative Elements

In-Game Narrative: The planet is infested with a swarm of hungry alien monsters, so the players must run away from the wall of aliens as they navigate the mysterious planet’s platforming challenges and battle it out to see who can collect enough energy and stay above the curve. The goal is to charge their respective spaceship in the final zone of the level.

I incorporated the in-game narrative by collaborating with Raghav to use space-themed assets and to give the planet an alien feel. We had trouble finding free use space-themed assets, so we had to mix and match assets from various sources.

Parallax Scrolling: Given the players are traveling the planet through the use of an auto scroll camera, I replaced the static background with 3 layers parallax background scrolling. This increases the immersion of players as it gives more depth as the backgrounds scroll at different speeds.

![parallax](https://github.com/user-attachments/assets/6094eade-a4eb-4090-912c-8eb89800c60f)

Wall of Alien Monsters: Using 3 different aliens (ghost, bat creature, flying eye thing), I created a giant wall that is a hitbox with a vertical world border hitbox. We initially had a static wall of drills chasing the players, but it felt too bland, so I replaced it with a giant swarm of individual monsters. The `wall_of_death.gd` script loops through every monster, allowing each monster to randomly extend outwards to reach the players. Given the randomness element of reaching out, this mechanic makes the wall of death lifelike, almost like a hivemind. Each enemy has an individual hitbox that's able to kill players. To better incorporate the in-game story, when the auto scroll camera stops at the final zone of the level, there's a second wall of alien monsters to the right of the screen. This adds to the narrative as the players now find themselves trapped between 2 walls of alien monsters, leaving them no choice but to gather energy and battle it out as they try to be the first one to charge their ship and escape the planet. To make the aliens more life-like, I used an animation player to move the parent node of all the monsters in a circular pattern, making them appear like they're actually hovering/flying. The reaching mechanic is implemented in [wall_of_death.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/wall_of_death.gd)

![wall_of_death](https://github.com/user-attachments/assets/72049ccf-d437-4cc7-8ee0-0ae238531fa2)

To make the level feel like a mysterious planet, I used vegetation of unnatural colors (orange), rock formations, and pillar structures. These background assets add to the immersion of the planet while also adding mystery. Life exists on the planet (such as alien monsters and orange plants), but what about the abandoned pillars and entrances? The level's terrain is rocky, with pockets of life throughout.

![image](https://github.com/user-attachments/assets/88ae0152-8f62-4fab-8073-6768c779d33e)

Given the importance of the final zone, I put extra effort into making it feel ominous. I did this by utilizing symmetry, which serves as constrast to the disorderly nature of the planet. The platform is made up of unique tiles never previously seen in the level, which adds to the intrigue. Overall, the final zone feels like a fitting battle ground.

![image](https://github.com/user-attachments/assets/c6f82e46-40a2-4101-ad7b-75fdb19176d0)

### End Cutscene

End Narrative: The winning player fixes their spaceship and escapes the planet, leaving the other player to die on the planet as it gets internally consumed by the swarm of monsters, exploding and being crushed into nothingness. With a stroke of luck, the losing player is thrown off the planet and its sent into the depths of space with a broken spaceship.

Just like the intro cutscene, the end cutscene is in its own scene. The key difference is that I had to make sure there were two different animations, 1 for each player winning. I decided to implement 3 animation players. 1 animation player plays regardless, which is the planet exploding and being crushed into nothingness. One of the other 2 animation players are specifically chosen based on which player won. The winning player's spaceship quickly escapes the planet and gracefully glides through space as the losing player is knocked off the planet and falls into the depths of space. At the end of the cutscene's animation, a menu appears, displaying the player who won and a back button to return to the main menu (I worked with Patrick to integrate the UI). The end cutscene is triggered once a player wins (fully charging their spaceship). The cutscene logic is implemented in [end_cutscene.gd](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/end_cutscene.gd).

![end_cutscene](https://github.com/user-attachments/assets/12a24117-3e42-448f-9397-d1b1d0dceb26)

## Audio (Raghav Bajoria)

### Audio Collection and Implementation

- Sourced high-quality audio tracks and sound effects to match the project's tone and theme.
- Edited and trimmed audio to fit specific scenes and timing requirements.
- Converted audio files into the appropriate formats for seamless integration into the project.

### Animation Integration

- Synchronized animations with collected audio for a cohesive storytelling experience.
- Ensured smooth transitions between scenes with aligned audio and animations.

### Challenges and Solutions

- Challenge: Trimming and aligning audio to fit precise scene timings. Solution: Carefully reviewed and adjusted soundtracks using Quicktime Player to match visual cues and transitions.
- Challenge: Finding the correct audio to fit the game whilst also complying with the copyright and legal agreements. Solution: itch.io and opengamemart.org was a great resource to find the right fit.

### Assets used

All under [License.md](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/License.md)

## Gameplay testing / Level Design (Patrick Le)

[Full report can be seen here](SpaceChasegameplaytestingnotes.pdf)

### Gameplay feedback

- Most of the complaints seem to be the keybinds and the controls of the player. Most players did not like how the up movement was also the jump. It made it harder for them to jump diagonally. Furthermore other players had certain preferences for different controls. For example some people were fine with the grab being the right bumper while some would have preferred the right trigger. Furthermore from the testing people noted keybinds for when playing two players on a single keyboard was unplayable.

- Another suggestion we had was the difficulty of the level design. Although I intentionally designed the level to be hard with near impossible jumps I agree some trap and platform placement was unfair. So some map tweaks were made to make the level more enjoyable while also not being too hard. We also got some feedback of how the push box aspect of the camera was high risk high reward since the players would have less time to react to traps. This was intended and it was nice to see the play testers noticing.

- A number of players also commented about players and visibility. Such as indicators for when the player respawn is going to happen, when the ships are fully charged, and a change of one of the player's colors.
  respawn is going to happen, when the ships are fully charged, and a change of one of the player's color.

- Players also felt that the ghosting mechanic was confusing and difficult to move around when ghosting, causing them to respawn in the wall and dying again.

### Adjustments after feedback

- The controls were changed for both controller and keyboard. For both devices the jump and up movement were separated into two different inputs. This allowed the players to have more freedom when jumping to the left or right. It also made it easier to jump and dash midair. Another thing we changed for the controller was the dashing, instead of having it on the bumpers it was changed to square and triangle, while the jump was changed to X and circle. The grabbing was also changed to both triggers and both bumpers.

- As for gameplay clarity we have changed player 2's color from blue to green to improve player visibility. I also increased the contrast of the background of the cave sections of the level since some complaints were that the background blended into the solid ground too much making it hard to see.

- To fix some issue with the ghosting we added an indicator such as the player blinking to show that the ghosting was ending and that the
  the player was going to respawn. We also made it so that the player could dash in when they are a ghost. This allows the player to recover more quickly from a bad spawn.

### Level Design

- The level design was very straight forward with Raghav's(Animation and Visuals) implementation of the different stylesheets. I wanted to make the level hard yet not frustrating. Furthermore I wanted to add an emphasis on the tradeoff of using the push box to speed up the camera. So spike traps are randomly placed so that if a player is constantly using the push box why will run into since there is a very short window to react. Also to add more variation throughout the map there are hidden tunnels that led provide strong power-ups or lead you directly into a trap. Karim also helped with level design by providing more detail and decorations throughout the level.

## Game Feel & Polish (Jason Zhou)

My work on game feel and polish is very varied and range from visuals to physics to audio.

### Visual Polish

   To improve game feel on the visual end:
   - I implemented [particle effects](https://github.com/ECS-179-Game-Project/Space-Chase-Game/tree/main/space-chase/scenes/particles) in a few parts of the game. These include when players die, when a powerup is picked up, when players are charging their stations,
   and when the charging stations are activated to indicate charging zones. For energy charging particles, I edited the [particle shader](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scenes/particles/3_energy_particles.tscn) to be able to target
   a specific point in space to go to, since standard Godot particle effects weren't capable of doing that.
   - Intertwined with charging particles, I added the progress bar for the charging stations in the end zone to clarify when players will win.
   - I wrote [shaders](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/shaders/player.gdshader) for and designed most of the player-specific objects to be differentiable by color, like the player energy bars, charge bars, and player characters.
   - I remade our [player spritesheet](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/assets/sprites/player/Astronaut/Astronaut_Spritesheet.png) to be more easily integrated into our animations. Previously, all of our player animations were split into multiple spritesheets, which made it much harder to animate the player. In the process, I also redid animations for player actions, adding animations to actions that had previously not had any, and overall making animations slightly smoother. This was especially noticeable for the grab, which used to have no animation and only a skew effect on the player.
   - I reorganized some of the menus to be more even and, in the future, more modifiable, using Godot's control node system.
   
### Gameplay Polish

   To improve game feel on the gameplay side, I mostly changed the player script:
   - I implemented [coyote time](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/db485cb862817148040876708b118bfd3fba2749/space-chase/scripts/player.gd#L209) for player jumping. Really, universally needed for platformers. I'm not playing a platformer without coyote time.
   - I changed the player dash so that the player retains some vertical momentum, to keep a sense of speed. I shamelessly ripped off Celeste's dash mechanics to make the dash feel better.
   - I added terminal velocity to the player, so the player doesn't fall extremely fast when platforming.
   - Karim did a great job, so I didn't really need to tweak anything else. I did not change player movement to be acceleration based since I want to keep the twitchy, fast-paced game feel. Also I wanted to avoid shenanigans with wavedashing.
   
### Audio Polish

To improve game feel on the audio side:

- I adjusted the volume of most sound effects and music in the game to overall be more balanced. Previously, many of the sound effects were too loud while some others were fine.
- I adjusted the speed of some sound effects like the player jump to fit more with the action. The player jump sound effect used to be much longer and lower-pitched, which I thought did not feel good for a fast-paced platformer.
- I properly positioned audio streams so they would be mixed better in stereo. Since most of our audio streams are 2D objects, we used to have issues with audio mixing with improperly placed audio.
- I changed the music to loop. Previously, if you stayed in the menu or the game levels for too long, the music would stop playing.
- I implemented the [audio sliders](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/main/space-chase/scripts/Menu%20scripts/volume_slider.gd) in the volume settings.
- I created audio buses and categorized sound effects and music for Godot's audio server, so they can be adjusted manually by the player in audio settings.
- I [sped up](https://github.com/ECS-179-Game-Project/Space-Chase-Game/blob/370cffc64f5a3e9fb428805a2edaaad745f5f31d/space-chase/scripts/world_audio.gd#L15) the music in the final area to give more of a sense of urgency.

# Areas to improve

## UI and Input

- The controller support still needs more work. The main issue is that the if there is only one controller
  then that controller is assigned to player 1. This could lead to accessibility issues if player 1 wants to play on
  keyboard and player 2 wants to play on controller.
- Another thing we could have done was having customizable player inputs since in the current build the player controls
  are fixed and the only way to change them is through the project settings in godot
- Also adding network multiplayer would have been a nice thing to add as well since godot does
  have some support with online multiplayer.

## Visual Improvements

- We could definitely have more visual effects in our game like distortions when dashing, dying, etc.
- An idea that might not be too hard to implement is color selection for players. Most of the player differentiated objects are already colored automatically. This could also help with accessibility, considering we chose red and green for our players which is a common type of colorblindness.
- Adding lighting could help with visuals.

## Gameplay Improvements

- Increasing variety by adding more planets (levels), perhaps with different color palettes and environments. This would have to come with a planet/level selection screen, which would look pretty cool.
- Adding an additional game mode in the "extras" menu that is just 1v1 Final Destination (some items) in the end zone.
- Adding more verticaliy, allowing the auto scroll camera to go up/down.
