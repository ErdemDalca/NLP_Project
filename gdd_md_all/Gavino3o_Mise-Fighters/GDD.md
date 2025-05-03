---
layout: page
title: Mise Fighters Game Development Document
---


**Mise Fighters is a Local Multiplayer Co-op Hack & Slash RPG.**<br>
The game lets you play as a chef, a butcher, a bartender or a pattisier on a mission to withstand the fury of vengeful food ingredients that have mysteriously come to life to seek revenge for their cooked brethren.<br>
While Hack & Slash games often exhibit a gory and intense atmosphere, Mise Fighters is infused with humour and light-heartedness while maintaining a thrilling action-packed gameplay.

<br>

## Problem Motivation

Drawing inspiration from beloved hack and slash titles like Hades and Hyper Light Drifter, we set out to create a whimsical online multiplayer cooperative hack and slash experience. Our game introduces a team of a chef, a butcher, a bartender and a pâtissier on a mission to withstand the fury of vengeful food ingredients that have mysteriously come to life. While hack and slash games often exhibit a gory and intense atmosphere, we wanted to infuse our game with humour and light-heartedness while maintaining a thrilling action-packed gameplay.

In our unique culinary adventure, players are not only encouraged but also rewarded for synergizing their skills to unleash mesmerizing combos and amusing effects against the culinary adversaries. By seamlessly combining their culinary prowess, the 4 friends can overcome the challenges and obstacles thrown their way.

<br>

## Overview

### Game Flow

In the main menu, players can customise their controls/keybinds before choosing to either host a game or join a game. They can also access a character guide menu to read about the playable characters’ skills.

Upon connecting as a host or a client, both players can choose their characters in a character selection lobby, after which loading into the first stage. There are 3 stages in total, each stage increasing in difficulty and culminating in a boss challenge at the end. Enemies will spawn in waves and target the players, and they have to work together to defeat the horde. Once all waves of enemies are defeated the players can proceed to the next stage.

For combat, every character firstly has a unique auto-attack that fires automatically, their primary method of doing damage to enemies. Each character also has an arsenal of skills/spells that can be cast, each with unique effects and cooldowns. Enemies on the other hand deal damage either by firing projectiles of their own or directly colliding with the player. Further depth is added to combat through a status effect system, where players and enemy units alike can be afflicted with buffs or debuffs, providing additional options for dealing with enemies.

At the end of the final stage, there will be a boss fight with a tanky, hard-hitting enemy that has access to multiple moves and attack patterns. Defeating the boss would result in a victory for the players.

Upon victory or defeat, players will be brought back to the main menu, where they can play again with different characters.

### Units

Units in the game have 4 core stats: Health Points(HP), Attack Power(ATK), Attacks Per Second, and Movement Speed. Both Characters and Enemies are considered units.

They can also be afflicted with status effects. When afflicted by status effects, there will be simple sprite animations so that it is obvious to the player.

| Name | Effect |
|------|--------|
| Taunt | Enemies change targets to the object |
| Slow (CYAN) | Movement speed is by 50% |
| Freeze (BLUE) | Enemies are unable to move |
| Flattened (INVERTED SPRITE) | Movement speed is decreased by 50%, Attack Power is reduced by 50% |
| Douse/Burn (GREY/RED) | Douse: Attack on the unit is increased by 50% <br> Burn: Damage over time debuff is inflicted. If target is doused, an additional 7 Ignition Damage is inflicted |
| Buff (GREEN) | Attack Power is increased by +50% (affects all scaling) |

### Playable Characters

![PlayableCharacters](images/PlayableCharacters.png)

4 characters with varying play styles and multiple cooperative options to deal with enemy waves. (See Appendix A for the detailed rundown on the characters’ stats and movesets)

Each character will have original hand-drawn sprites and animations for their various skills and movement.

### Enemy variety

The game has various enemy types that will spawn in waves. The enemies target the players and use AStar pathfinding algorithms to advance on the players. Different enemies have different attacks and behaviours to provide some strategic depth to how players want to deal with them. (See Appendix B for the detailed rundown on the enemies’ stats, move sets and behaviours)

Enemy waves have different enemy amounts and enemy variety, and are designed to provide a scaling difficulty curve as the game progresses. Enemies are spawned from various spawn points around the arena and will path find towards and attack the characters.

### Environments

The game will have different stages for the players to fend off the horde in. The environment can pose an added challenge to the players by virtue of both restricting the space available to kite enemies around the arena as well as obstacles that can hinder/slow movement.

#### Stages

1. **The Restaurant**
   - In this stage there should not be any stage hazards. This stage is designed to have large area for ease of movement.
   - Some tables and chairs are present to obstruct movement of both players and enemies. It also includes an accessible kitchen and toilet area for players to explore.
2. **Market Area**
   - A colourful market area with various obstacles to obstruct movement or allow for kiting. This stage includes new enemy variants that will keep the players on their toes.
3. **Basement**
   - Final face off against the boss monster, in an arena stage. This stage includes a large open space for players to move around and dodge the bosses attacks.


### User Interface (UI)

The in game overlay will provide key information to the player while also being as unobtrusive as possible.

### Music/SFX

The game will consist of captivating audio throughout. Players are able to enjoy background music in menus and in game accompanied by fun sound effects for characters, enemies and environments. The audio of this game aims to enhance the player experience.

<br>

## User Stories

1. As a player, I want to access the main menu to start or join a multiplayer game, adjust settings, and navigate the game options easily.
2. As a player, I want to host a multiplayer game so that I can invite friends or other players to join and play together.
3. As a player, I want to enter the character select scene after joining or hosting a multiplayer game, where I can choose a unique character to play.
4. As a player, I want to see information about each character, including their abilities, strengths, and weaknesses, to make an informed decision during character selection.
5. As a player, I want to face waves of enemies, challenging my skills and teamwork with other players.
6. As a player, I want to survive against increasingly difficult waves of enemies by utilising my character's skills and discovering powerful skill combinations.
7. As a player, I want the option to restart the game if all players die, allowing us to make a fresh attempt to overcome the challenges.
8. As a player, I want to be able to exit the game midway, ensuring that I can easily return to the main menu or exit the game entirely.

<br>

## Design

### Technologies Used

- Unity: Engine used to develop the game.
- FishNet: Networking solution for Unity that we used to implement multiplayer functionality.
- C#: Main scripting language used for development.
- Aseprite: Used for sprites and animations for Units, Environments and VFX.
- Clip Studio Paint: Used for splash art and concept art for the game.
- GitHub: Version control and collaboration.

### Overall Design

![OverallDesign](images/Overall_Design.png)

### Characters

![CharacterScripts](images/CharacterScriptDiagram.png)

- Unit - contains information (Stats, StatusEffects) about units in the game and implements methods for units to interact via the combat system. (Taking damage, being afflicted by Statuses)
- Player - contains information about the player and a reference to their controlled character.
- Character - contains references to all components, as well as basic information about the character.
- InputCharacter - wrapper class around player inputs calculating and containing information used by other character components.
- MoveCharacter - movement script for character.
- AttackCharacter - character automatically attacks at intervals determined by their AttackSpeed.
- CastCharacter - abstract class outlining universal spellcasting behaviour. (spell cool-downs, spell information etc.)
- CastCharacter - concrete classes containing the specific implementation for each character’s unique skill set.
- AnimatorCharacter - controls what animations are playing for each character.

### Managers/UI

![ManagerUI](images/ManagerScriptDiagram.png)

- GameManager - singleton in charge of scene changes and keeping references to all connected players. Handles the lives total as well.
- UIManager - singleton with functionality to change UI screens that can be used from other classes.
- MainMenu - Main Menu screen with host, join and quit buttons.
- CharacterSelect - Character select lobby.
- GameInfo - UI overlay when in game with information like health and skill cooldowns.
- ReadyScreen - Screen overlay when the current stage is clear and awaiting transition to the next level.
- AwaitingRespawn - Screen overlay when downed and awaiting help from an ally.

### Combat Scripts implementing Combat System above

- SpellData - contains information like spell name, description, cool-down, damage to be used by CastCharacter classes.
- StatusEffectData - contains information about the buffs and de buffs associated with a status effect to be used by Unit classes when being afflicted.
- Damager - inflicts damage on collision with a Character or Enemy.
- Lifetime - server side coroutine to despawn objects after a set time.

### Enemy System

![EnemySystemDiagram](images/EnemyScriptDiagram.png)

- EnemyMovement - A controller to decide which enemy movement algorithms to use
- EnemyAI - Contains information about enemy max health, enemy death event and controls enemy movement and player targetter
- PlayerTargetter - Stores information on the current player targeted for movement and attack.
- Projectiles - Scripts regarding behaviour of projectiles spawned by enemies to be attached to projectile prefabs.

![EnemyWaveDiagram](images/EnemyWaveDiagram.png)

- EnemySpawner - Spawns enemies type according to EnemySpawnerData injected.
- EnemySpawnerData - Contains information such as enemy prefabs, max enemy to spawn and spawn locations
- EnemyManager - Singleton managing and storing references and counts of active enemies currently in the wave
- WaveManager - Singleton managing wave information, enemy spawners and enemy boss information that are injected using WaveData.
- WaveData - Scriptable Object containing information regarding waves such as wave delays, spawners involved.

### Audio System

![AudioScriptDiagram](images/AudioScriptDiagram.png)

- AudioManager - Contains a list of all sound clips and audio sources to control the playing/synchronisation of game sounds.
- AudioMixers - Allows playing of multiple clips simultaneously.

<br>

## Testing

### Unit Testing

Unit testing was conducted with a focus on whether individual scripts and methods within those scripts worked as intended.

### Player-Character related systems

Note: All tests in this section were conducted in multiplayer context. (one game instance in the Unity Editor as the host and another built instance as the client). The tests are  considered successes only if it is performed and satisfactory result is achieved across both client and host in synchronisation. Double checking of synchronised values was done via the Unity Editor’s hierarchy.

#### Character Input

| Test | Expected Result |
|------|--------|
| WASD movement keys pressed | Character moves along cardinal and diagonal directions properly according to keys pressed |
| Mouse moved around the character | Direction faced in input script updates correctly to match the character’s faced direction. |
| Mouse moved around the character | Character turns left and right properly to face the mouse cursor |
| Skill key pressed | Character attempts to cast a skill correctly |
| Dash key pressed | Character attempts to cast a dash correctly |
| Ultimate key pressed | Character attempts to cast an ultimate correctly |
| Wait for character to auto attack | Character attempts to attack at the intervals specified  |

#### Character HP/Death Behaviour

| Test | Expected Result |
|------|--------|
| Character collides with a character damager | Character takes damage |
| Character with 35 HP collides with a 10 HP damager | Character takes 10 damage; remaining HP 25 |
| Character with 5 HP collides with a 10 HP damager | Character takes 5 damage, remaining HP at 0 |
| Character with 20/35 HP collides with a -10HP damager  | Character heals 10 HP, remaining HP 30 |
| Character with 30/35 HP collides with a -10HP damager | Character heals 5 HP, remaining HP 35 |
| Character HP is reduced to 0 | Respawn screen shows correctly |
| Character HP is reduced to 0 | Respawn screen shows correct amount of revives available for both players |
| Character attempts inputs while dead (in respawn screen) | Character does not respond to inputs |
| Character attempts to attack while dead | Character no longer automatically attacks while dead |
| Character is revived | Character HP set to maximum as defined in baseStats |
| Characters run out of revives | Respawn button greys out and is not interactable. Quit Game Button becomes interactable |

#### Character Status Effect

| Test | Expected Result |
|------|--------|
| Character is afflicted with a slow effect | Character movement speed is reduced by the set multiplier|
| Character is afflicted with a slow while already slowed | Character movement remains at the lowered value, only restoring once the latest slow expires |
| Character is afflicted with a freeze effect | Character movement is stopped |
| Character is afflicted with the douse status | Character attack is lowered and isDoused flag is set |
| Character is afflicted with burn status while undoused | Character is burned and their attack is lowered while taking a Damage over Time (DoT) effect |
| Character is afflicted with burn status while doused | Character takes the 7 ignition damage while still receiving effects of burn, isDoused flag is unset |

#### Character Spell System

| Test | Expected Result |
|------|--------|
|Skill/Dash pressed when off cooldown | Spell casts correctly and is put on cooldown|
|Skill/Dash pressed when on cooldown | Spell does not cast|
|Character deals damage| Ultimate meter charges|
|Character takes damage| Ultimate meter charges|
|Character charges ultimate meter when it is already full| Ultimate meter does not exceed the maximum stipulated charge amount|
|Ultimate pressed when not enough ultimate charge| Ultimate does not cast|
|Ultimate pressed when at full ultimate charge| Ultimate casts and expends all ultimate charge|

#### Butcher Spells/Attacks

| Test | Expected Result |
|------|--------|
|Butcher auto attacks| Attack prefab spawned correctly in the direction faced|
|Taunt spell is successfully casted|Taunt spell effect is spawned at the butcher’s position|
|Dash spell is successfully casted|Butcher’s movement inputs are interrupted while dash is casting|
|Dash spell is successfully casted|Butcher moves rapidly in direction faced|
|Dash spell ends|Butcher’s movement inputs are restored and player regains control|
|Ultimate spell is successfully casted|Ultimate coroutine starts and spawns the circular damage prefab at the correct predefined intervals and the correct predefined number of times.|
|Ultimate spell is successfully casted|The ultimate spell prefab is spawned at the butcher’s position|
|Dash casted successfully while Ultimate is channelling|The ultimate spell cast follows the butcher correctly|

#### Bartender Spells/Attacks

| Test | Expected Result |
|------|--------|
|Bartender auto attacks| Attack prefab spawned correctly and travels in the direction faced|
|Bartender auto attacks|Attacks continue flying at the predefined speed| while having random rotations as visual effect|
|Bomb spell successfully casted|Bomb spell spawned at the cursor location and lasts for the set duration|
|Backstep spell successfully casted|Lure spell spawned at the current location and lasts for the set duration| bartender’s movement inputs are briefly interrupted|
|Backstep spell successfully casted|Bartender swiftly moves in direction opposite to the current one faced|
|Ultimate spell successfully casted|Ultimate spell spawns correctly as current location|

#### Patissier Spells/Attacks

| Test | Expected Result |
|------|--------|
|Patissier auto attacks| Attack prefab spawned correctly and travels in the cardinal directions|
|Patissier auto attacks|Attacks continue flying at the predefined speed|
|Torch spell successfully casted|Torch Spell Prefab follows the players on either the left or right side depending on player target position|
|Dash spell is successfully casted|Patissier movement inputs are interrupted while dash is casting|
|Dash spell is successfully casted|Patissier’s moves rapidly in direction faced|
|Dash spell ends|Patissier’s movement inputs are restored and player regains control|
|Ultimate spell successfully casted|Ultimate spell spawns correctly as player current location|
|Ultimate spell successfully casted|Rolling Pin Spell Prefab spawns and travels in direction faced|
|Ultimate spell successfully casted|Rolling Pin Spell Prefab despawns once lifetime is exceeded|

#### Chef Spells/Attacks

| Test | Expected Result |
|------|--------|
|Head Chef auto attacks|Chef Auto Attack Prefab spawned correctly in direction faced with correct orientation|
|Slice spell successfully casted|Two Slice Prefabs are spawned simultaneously in correct rotations in direction faced of the chef|
|Blink spell successfully casted|If no obstacles are in front of the direction faced| the player is successfully teleported in the direction faced at a predetermined distance|
|Blink spell successfully casted|If there is an obstacle in front of the direction faced| the player is successfully teleported in the direction faced| but stopping right before the obstacle|
|Blink spell successfully casted|When player teleports to set distance| a stun prefab is spawned at player new location.|
|Ultimate spell successfully casted|Player movement imputed is interrupted at the start of the spell and regained once the spell finishes|
|Ultimate spell successfully casted|Ultimate Prefab is spawned correct in direction faced| with correct rotation and despawns after lifetime is exceeded|

### Enemy Spawning and Enemy Behaviour

#### Enemy Pathfinding/Targetting

| Test | Expected Result |
|------|--------|
|Target and Enemy pathfinder are in the same scene|Enemy sets target and starts following it|
|Target moves position while being targeted by enemy|Enemy pathfinding updates to follow the target|
|Target moves behind an obstacle|Enemy pathfinding updates to move around the obstacle|
|Target stops|Enemy pathfinding stops when attack range is reached|
|Enemies with CanMove flag set as false|Enemy will not move when spawned|

#### Enemy Attacking/Behaviour

| Test | Expected Result |
|------|--------|
|Melee enemy collides with the target|Melee enemy deals damage to the target|
|Target moves while being chased by melee enemy|Melee enemy continues chasing target until colliding with it again|
|Ranged enemy is outside its attack range to target|Ranged enemy pathfinds towards target|
|Ranged enemy enters attack range|Ranged enemy stops movement and attempts to start attacking|
|Ranged enemy attacks| Projectile spawns and moves towards target fired at regular intervals
|Arc Projectile Ranged enemy attacks|Projectile moves towards target location in an arc
|Target is moved out of attack range again|Ranged enemy stops attacking and continues to chase the target|
|Spaghetti Boss Enemy Spawns|All boss skills occur after indicated time delay|
|Spaghetti Boss Enemy Shoots Tomato Projectile|Tomato projectile is fired at random player character|
|Spaghetti Boss Summons Tomato Bomb Enemies|Tomato Bomb enemies are spawned in specified radius and are activated|
|Spaghetti Boss Summons Meatball Comets|Meatball comets are spawned in the edges of the map| and move horizontally or vertically across the arena based on spawn location.|
|Meatball Comet or Tomato Projectile hits player|Player character takes indicated damage|


#### Enemy Spawning

| Test | Expected Result |
|------|--------|
|Injected enemy prefabs are spawnedEnemy Spawner spawned enemy|Enemy prefabs spawned has working attack and behaviour|
|Enemy Spawner spawned enemy|Enemy prefabs spawned in correct spawn location|
|Enemy Spawner spawning enemy|Enemy Spawner spawns the correct predetermined number of enemies|
|Enemy spawner spawned all enemies|Enemy spawner deactivates and no enemies are spawned|
|Boss Spawner spawns enemies|Boss is spawned and activated|

#### Wave System

| Test | Expected Result |
|------|--------|
|Game begins| Wave system loads first wave and instantiates initial spawners|
|An enemy is killed|Wave system successfully records down enemy death and update enemy death counter accordingly|
|All enemies in current wave are killed|Wave system successfully detected wave is over|
|All enemies in current wave are killed|Wave system loads next wave successfully|
|Loading next wave|Wave system loads next wave and instantiates spawners correctly|
|Loading next wave|Wave system resets enemy death count correctly|
|All waves loaded|Wave system successfully detects all waves has been loaded| signals end of level|
|Boss is killed by player|Wave system successfully detects boss on death status and signals end of game|

### Scene Transitions and Basic Player Connectivity

#### Main Menu

| Test | Expected Result |
|------|--------|
|Build and Run game|Offline Main Menu scene loads correctly|
|Host button is pressed when no active connections|Starts game and hosts a lobby|
|Join button is pressed when no active host|Nothing happens as no host is active|
|Join button is pressed when active host present|Client loads into the same lobby|
|Player connects to game correctly either as host or client|Character Select lobby loads|
|Guide Button is pressed when no active connections|Menu with Interactable character sprites of the 4 playable characters are shown|
|A character sprite is pressed in the guide menu|Character splash art is shown along with the names and descriptions of character kit/skills|
|Close button is pressed in the character kit/skill screen|Menu with Interactable character sprites of the 4 playable characters are shown|
|Main menu button is pressed in the 4 Character Info Screen|Main Menu loads|

#### Character Select

| Test | Expected Result |
|------|--------|
|Loading into Character Select as host|UI loads for host with the start button active but greyed out|
|Loading into Character Select as client|UI loads for client with the start button inactive|
|Cycling through characters as host and client|Character splash arts cycle correctly and display the currently hovered character; at the end of the character list it loops back to the first|
|One player locks in|Host is still unable to start the game as not all players are locked in|
|All connected players lock in|Host is able to start the game| start button is no longer greyed out|
|Host leaves the lobby|Lobby disbands automatically and all connected players are returned to the offline Main Menu scene|
|Client leaves the lobby|Host still remains in the lobby and the lobby can still accept new players|

#### Game Scene

| Test | Expected Result |
|------|--------|
|Load into game scene|Characters load successfully into new game scene and can see each other in the game world|
|Load into game scene|Camera centres on characters correctly|
|Load into game scene with scene objects|Scene objects are loaded and are visible to both players|
|Host disconnects from game scene|Both players are forced to disconnect and game session ends|

<br> 

### Integration Testing

Testing done to ensure individual components/scripts work together as intended.

#### Combat Interactions

| Test | Expected Result |
|------|--------|
|Character and Enemy in the same scene|Enemy targets the player automatically|
|Character hits an Enemy with a damaging attack|Enemy takes damage successfully|
|Enemy hits Character with a damaging attack|Character takes damage successfully|
|Character kills an Enemy|Enemy dies and is despawned|

#### Character Animations/Sprite Visuals

| Test | Expected Result |
|------|--------|
|Character does not input anything|Idle animation plays and loops|
|Character starts moving|Walk animation starts playing|
|Character turns to face the opposite direction|Sprite is flipped on both host and client|
|Character casts spell successfully|Spell animations play uninterrupted by movement/idle animations|
|Character is afflicted by status effect with sprite alterations|Character sprite changes colour correctly to match the status effect changing back to the default colour once the effect expires|

#### Character Scripts/GameView UI

| Test | Expected Result |
|------|--------|
|Character takes damage/HP is changed|GameView updates to show the most recent HP value|
|Character spell is available to cast|GameView shows that the spell is ready to be cast|
|Character casts spell and goes on cooldown|GameView updates to show the spell is on cooldown|
|Character has X ultimate charge|GameView correctly shows that character has X ultimate charge|
|Character gains ultimate charge|GameView correctly updates to show new ultimate charge level|

#### Audio/SFX Responses to Game Events

| Test | Expected Result |
|------|--------|
|Game loads offline Main Menu scene|Background music plays|
|Game loads online CharacterSelect scene|AudioManager plays lobby BGM for both host and client|
|Player clicks UI buttons|Appropriate SFX plays only for the player in question
|Characters perform actions with SFX attached (attacking, casting etc.)|AudioManager plays SFX for both host and client|
|Enemies perform actions with SFX attached (attacking etc)|AudioManager plays SFX for both host and client|

#### EnemyManager/WaveManager/GameManager Scene Transitions

| Test | Expected Result |
|------|--------|
|EnemyManager quota met|EnemyManager signals quota met to WaveManager, Enemy Death Count Resets for next wave|
|Boss Wave conditions met|WaveManager calls GameManager to show VictoryScreen|
|Waves have all finished spawning|WaveManager calls GameManager to show ReadyScreen|
|Host clicks continue when all players are ready|Scene transitions successfully to next scene and waves spawn if in the scene|

<br>

### System Testing/Regression Testing
Throughout the software development process, measures were taken to ensure code changes on the commit would not jeopardise the existing product. Before any commits/after every work session  a simple runthrough of the game was conducted to lookout for new bugs/console errors that might arise.

This was especially important when working on the character/enemy related scripts, as they all had to interact with one another; sometimes improving a system would require changing how these scripts interact.

1. Game starts up and loads the offline scene successfully.
2. One instance hosts and another joins, ready system working as intended and background music is playing for both instances. Character select panel displays the hovered character.
3. In game, both characters’ movement, animations, attacks and sound effects can be seen/heard on each others’ screens. Notably, movement abilities that drastically change the player position still gets networked without error.
4. Players take turns attacking enemies with both skills and auto attacks. Once the enemies die, they despawn properly on both instances. 
5. Upon completing the waves of enemies, no more enemies spawn and the ready screen is displayed.
6. Upon completion of the boss level, the ready screen’s continue button brings both players to an empty scene where a victory popup is displayed. Players can then return to the main menu.

### User Acceptance Testing

Testing procedure: Game was given to the participants without any explanation, testers gameplay was observed and noted down.

Afterwards an interview is conducted with the tester to explain anything unclear about the game and ask for their feedback.

#### SESSION 1: Date: 24/6/2023

**Playtester #1 description:** <br>
Limited experience with this genre of 2D hack and slash
Experience with top down MOBAs

**Playtester #2 description:**<br>
Little/No experience with action games.

**Observations:**<br>

- Hosting and joining was not immediately clear, more explanation probably needed or better naming of buttons.
- Controls were unknown, tutorial screen or controls shown in main menu would have been helpful. We ended up having to break silence and at least tell them the controls, especially for the less experienced playtester.
- Movement was smooth as well as camera follow.
- Desired more feedback on enemy hit/defeat.
- Playtester #2 suggested a “puff of smoke” when enemies were defeated.
- Playtester #1 felt the game was too easy.
- Both playtesters communicated while playing.
- Sometimes one would ask another for help with a swarm of enemies.
- However, no communication about specific skill combinations actually took place. This could come with more experience with the game, but unknown for now.

#### SESSION 2: Date: 22/7/2023

Playtester hosted the lobby and played together with a dev. The dev gave minimal insight regarding HOW to play the characters,  but would still communicate stuff happening in game.
 
**Playtester #3 description:**<br>
Avid watcher of game playthroughs, familiar with many genres of games.
Experience with top down MOBAs.
Experience with co-op games like Overcooked.

**Observations:**<br>

- Felt the game was way too hard
- Game dragged on for a really long time and enemies piled up fast.
- Increased intervals and decreased wave counts for earliest waves.
- Preemptively reduced enemy counts across the board.
- Swarmer enemies being introduced in the first stage is quite jarring for new players.
- Removed all “fast” enemies from the first stage.
- Boss was too easy and dies too quickly, felt the stages were harder than the boss.
- Increased boss health, attack count, attack frequency.
- Lack of healing felt quite unforgiving.
- Changed heal on revive to be 75%.
- Added healing to Butcher’s taunt.

**Patissier clunky to play, difficult to hit enemies**

- Originally meant to be a character with a unique DoT and run play pattern, but not as obvious to the player.
- I think it’s good for some characters to be stronger when learnt.
- Buffed hitboxes of the normal attack at least, as the visuals need to be more forgiving for multiplayer

**Bartender feels strong**

- Good beginner friendly character
- We want the butcher to feel this way as well, so we buffed his invincibility duration on the taunt and his overall tankiness.

We improved the feedback on buffing and status effect application in general, and the playtester actively tried to buff their ally when playing bartender/butcher.
Buffing is direct and obvious enough to be actively considered.
Less direct combos like taunting and AoEs seem to be subconsciously used as well (although this could be a result of playtesters experience with MOBAs)

Appreciated the control mapping.
Felt the unit guide was ‘cute’.

#### SESSION 3: Date: 23/7/2023

**Playtester #4 description:**<br>
Experience with games like Vampire Survivors and Hades, well-versed with this genre of games.

**Playtester #5 description:**<br>
Experience with some FPS games.

**Observations:**<br>
In general playtester #4 was more comfortable with the controls owing to their experience.

Both playtesters made exclamations about gameplay (sufficiently engaged) and would ask for help dealing with enemies (especially the faster ones in stage 2)

- Players were surprised by the tomatoes and swarmers in stage 2
- Good difficulty mixup
- The fast enemies only wave caused a lot of chaos
- Difficulty curve from stage 1 to 2 is evident
- Spaghetti monster is sufficiently tanky; the bullet hell attacks force the players to move around
- Felt it was a bit challenging for melee characters
- Playtester #4 complained about hitboxes a lot, especially when combined with the multiplayer delay.
- Altered hitboxes/hurt boxes for more precise dodging and hitreg.
- Key takeaway is that the player’s spells/attacks should have larger hitboxes than their sprites to give some leeway for multiplayer, and the enemies’ attack hit boxes can be smaller than their sprite suggests to allow for more outplay potential/narrow precise dodging.

Playtester #4 enjoyed the chef the most due to the high damage output and mobility.

Playtester #5 enjoyed the bartender the most due to the ranged attacks.

Character identities seemed sufficiently defined, different playstyles are available to match different player preferences.

**Example questions:**

- Do you have any general thoughts about the game?
- Which character was your favourite?
- Which character was your least favourite?
- Which enemy gave you the most trouble?
- Did you find the game challenging enough?

<br>

## Build

Link: [Mise-Fighters Download](https://drive.google.com/file/d/1TGjD3pHHSMJFhYWlhF8fZCtCaoKDS3S_/view?usp=drive_linkhttps://drive.google.com/drive/u/0/folders/1Cx69BKabV8r-LCioAJPXIR8c9OckY4Fi)

(Extract the contents before proceeding.)

![BuildExampleImg1](images/BuildExampleImg1.png)

We are using this Network Discovery package for LAN play (as recommended by FishNet official documentation) : Abdelfattah-Radwan/Fish-Networking-Discovery

In order to facilitate testing both over LAN and on a single machine (two instances), we have left both FishNet’s NetworkHUD and the package NetworkDiscovery HUD active.

**LAN Testing instructions:**<br>
You will require two machines connected to the same WiFi network. One will be the host and the other the client.
The host machine runs the application, and selects host. They will be loaded into the lobby. Click Start under the Advertising tab if not automatically advertising.
The client machine runs the application. Click Start under the Searching tab if not automatically searching.
Once the server has been found, the IP will be displayed under the servers tab in the same section.
Click the button with your IP to connect to the same lobby as the host machine.

![HostingExample1](images/HostingExample1.png)

**Single Machine testing instructions:**<br>
Open two instances of the game on one machine. One will be the host and the other the client.
The host instance selects host. They will be loaded into the lobby.
The client instance clicks the “Start Client” button at the top left of the screen to connect to the same lobby as the host machine.

<br>

## Problems Faced

Managing the multiple aspects of the game 
With such a complex design and multiple interconnected parts, there was a constant need for us to update each other on the changes we made and do peer code reviews to understand the design of all the game systems, at least at a basic level.

Us having to affect multiple scripts/systems when making changes also led to the occasional merge conflicts.

Managing the difficulty curve (solved with playtesting)
As developers we are very familiar with the game and its mechanics, so we would naturally underestimate the difficulty of the game. Even with this in mind, we somehow still managed to make the game too difficult on the first playtest. Through player feedback we have brought the difficulty back to an acceptable level, but definitely could be refined more.

### Bugs Squashed:

#### Synchronisation bugs

Faced many challenges involving syncing of values across clients. Especially with so many moving parts, we had to make sure values were synchronised properly.

To fix this bug, we used SyncVar and ServerRPC calls to alter values that are meant to be synced (notably, health) this not only reduced desync but made health bars more responsive and stop jittering, which was a problem before.

#### Client side errors and dealing with RPC calls

Often when implementing features they would work on the host instance/in singleplayer but break in multiplayer on the client instance.

To fix these bugs, we had to correctly implement RPC calls and chain the correct function calls together. For instance, UI displays were bugged and inconsistent for the client instance. Our solution was to chain a TargetRPC function so that only the targeted connection shows the new UI, while other clients remain unaffected (this was useful for Respawn screen and Pause menu screen)

#### Spellcasting related bugs

Spell casting was challenging to implement as animations and damagers had to be synchronised across both clients. We often encountered issues where the client could not cast spells in the desired input direction.

We found out the bug was caused by us calculating/accessing values from our InputCharacter class within RPC functions. To fix it we passed the data as arguments instead.

#### Enemy spawning

Initially, our enemy system uses multiple spawners per wave with set number of enemies per wave and pre-determined enemy variants. The wave system also utilised a buffer mechanism to determine the number of enemy deaths before signalling a wave transition. This system has caused some performance issues and logic error when the wave sized has been increased and boss waves were implemented.

After some brainstorming, we decided we had to overhaul the whole enemy system entirely. The new system would utilise one spawner per wave with set number of enemies, and the enemy variants spawned are determined by set probability. Wave transition conditions were also revised to be more in depth with multiple checks instead of just checking for enemy death counts. These changes have made the wave transition more stable and made enemy waves more diverse and unpredictable, resulting in overall better player experience.

## Appendix A: Character Details

| Character | Butcher | Bartender | Pâtissier | Chef |
|-|-|-|-|-|
|HP|High|Medium|Medium|Low|
|ATK|Medium|Low|Low|High|
|AS|Medium|Fast|Slow|Fast|
|MS|Slow|Medium|Medium|Fast|
|Normal Attack/Basic attack. Automatically fired with delay.|Swings his cleaver in an arc in front of him damaging all enemies in range.|Flings an ice cube at the faced direction damaging all enemies it passes through.|Scatters 4 pastries cardinally damaging enemies hit.|Stabs quickly at the closest enemy damaging all enemies in range.|
|SP1<br>Signature skill|[A Butcher’s Bravado]<br>Stomps the ground while TAUNTING all enemies within a medium range and dealing damage in an AOE.|[Cocktail Bomb]<br>Lobs a freshly shaken Margarita at the closest enemy that explodes in a large AOE dealing damage DOUSING them. Allies caught in the range receive an ATK BOOST.|[Toasted Meringue]<br>Activates his blowtorch and continuously ignites enemies (in the horizontal direction faced) applying a strong BURNING effect to all enemies hit.|[Slice and Dice]<br>Performs two quick slashes in an arc in front of him| doing damage to all enemies hit.|
|SP2<br>Movement ability|[Reckless Charge]<br>Charges forward dealing damage to all enemies hit.|[On the House]<br>Nimbly backsteps leaving behind a sweet concoction at her previous location which TAUNTS enemies.|[Gotta Run]<br>Frantically scrambles in the direction they are facing.|[Nothing Personal]<br>Blinks behind the closest enemy in the direction faced| STUNNING enemies in a small AOE for 1s.|
|ULT Can only be used when the ULT meter is full (Build meter by attacking OR taking damage)|[Gutsy Pirouette]<br>With surprising dexterity, the Butcher performs a glorious spin, heavily damaging enemies caught in the area. (1 tick/s)|[Just the Rocks]<br>The Bartender flash freezes everything around her in a large radius dealing massive damage and FREEZING enemies.|[You’re Dough-ne for]<br> The Patissier sends out a comically large rolling pin in the direction they are facing, dealing massive     damage and FLATTENING all enemies hit.|[Julienne]<br>Using his trusty (and meticulously sharpened) chef’s knife| the Head Chef decimates everything in a rectangular area in front of him| dealing massive damage.|

<br>

## Appendix B: Enemy Details

|Enemy Type| HP | ATK | AS | MS | Description |
|-|-|-|-|-|-|
|(Normal/Elite) Carrot | Medium/High | Medium | Medium | Medium | Basic Melee Enemy |
|Tomato | Low | High | NA | Fast | Self-Exploding enemies. It will charge the player and detonate itself when in range |
| Corn | Low | Medium | Medium | Low | Basic ranged enemy. Chucks kernels of itself at the player |
| Meat | Low | Medium | Medium | Low | Elite ranged enemy. Lobs drumsticks in an arc towards the player|
| Corn Kernels | Very Low | Very Low | Medium | Very Fast | Fastest swarm enemies. They tend to pop out of nowhere. |
| Spagetthi Monster | Very High | Medium | Medium | Does not move | Boss Enemy.<br>SP1: Spawns Tomato Enemies to attack the players.<br>SP2: Flings tomato projectiles at the player.<br>SP3: Summons meatball comets horizontally or vertically accross the arena. |

<br>

## Appendix C: Credits/Assets Used

### Packages:
- Network Discovery package: Abdelfattah-Radwan/Fish-Networking-Discovery
- Astar Pathfinding package: Pathfinding in 2D
- Fishnet package: https://github.com/FirstGearGames/FishNet

### Sprites: 
- Fire effect/ Ice effect: https://codemanu.itch.io/pixelart-effect-pack 
- Interior Design Tileset: https://rcpstd.itch.io/interior-tileset-asset-pack-16x16
- Kitchen Tileset: https://limezu.itch.io/kitchen
- Market Tileset: https://gif-superretroworld.itch.io/marketplace

### Music:
- Main Menu BGM: https://www.youtube.com/watch?v=o9_Gu3TI4IY&ab_channel=Chillpeach
- Character Select BGM: https://www.youtube.com/watch?v=c9aDCHM73Ro&list=PLMf0q6-pSDdsWY4LWYncx25qvonLA520c&index=12&ab_channel=yourmoodishere.
- Action BGM1: https://soundcloud.com/spatemusic/fuccatatogue-alteredidk3
- Action BGM2: https://soundcloud.com/spatemusic/idkwhatbiibthisis2
- Action BGM3: https://soundcloud.com/spatemusic/sets/prologue-ep
