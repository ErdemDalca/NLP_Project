# Hunt for Magic 
## Game Design Document Shape 
All work Copyright ©2021 by Pelipojut  
Written by Tomi Asikainen, Eetu Pitkänen, Niko Hokkanen, Ville-Veikko Taskinen & Arttu Rintamäki 

* Game Design Document
  * Game Design
    * Summary
    * Gameplay
  * Story
    * Plot Summary
    * Narrative
  * Technical
    * Development Details
    * Controls
    * Mechanics
    * Spells & Weapons
    * Spell synergies/comninations
  * Level Design
    * Key Locations
    * Objects
    * Game Flow
  * Character Design
    * Protagonist Design
    * Enemy Design
    * Boss Design
  * Graphics
    * Style Attributes
  * Audio
    * Style Attributes
    * Music
    * Sound Effects

## Game Design
### Summary 
You are a novice mage on a quest to stop a necromancer that is trying to summon the great evil. In the demo, you will be journeying through the forest in search for new spells and unrest. 

### Gameplay 
The game will have a roguelike gameplay style, where the player will have to start an attempt to beat the game, these attempts are called “runs”. In a run the player will have to go through three areas that are split into two stages, so six stages in total. The goal of the game is to defeat the final boss that is found at the end of the last stage, without dying on the way. If the player dies at any point during a run, they will be sent back to the hub world, where they need to then start a new attempt to beat the game. The player will find various upgrades during a run that make them stronger and allow for more creative use of the mechanics offered by the game, these upgrades will only last for the current run.  

In this game you will be a wizard, so instead of attacking using swords and bows, you will be using various elemental spells to deal with your enemies. Most of these spells can also combine when used together, in order to do special effects that are more useful than just the basic spell. All of the spells will have cooldowns, so you will not be able to just use them repeatedly. You will need to use your resources wisely to get the most out of your spells. 

In order to defeat the enemies in this game the players need to be able to observe and use their environment to their advantage. Most of the time it will be wiser to try and push enemies to spikes instead of trying to defeat the enemies using only damaging attacks. 

## Story 
### Plot summary 
Up to the year 1304 the kingdom of Rothmar was ruled by the righteous king Rhojorn, until his former advisor and an arch mage, Eimird, decided to betray his kingdom by killing Rhojorn and start conjuring monsters. Ever since then the kingdom has fallen under the reign of this evil necromancer. 

For almost a decade now the king’s rightful heir, prince Avalnir, has been in a war against the necromancer’s army of monsters to finally redeem back his father’s old kingdom. However, Avalnir’s attempts in the cause have been futile and have been criticized by some. Over the course of years he has send thousands of soldiers into the battle and with every fallen Rothmarian soldier the necromancer resurrects them back to be part of his undead army. 

The Necromancer’s plan is to perform an ancient ritual in order to summon Asmodeus, the king of demons. He believes that he could control the demon overlord and take over the rest of the world. This however has not been successful because the ritual can only be performed once all the conditions are right, which becomes more imminent with each passing day. 

All hope was lost until seemingly out of nowhere a novice mage appeared to begin fighting necromancer’s army all by himself. 

### Narrative 
The Forest area has journal entries from a fallen Rothmarian soldier dated to the year 1310. These will tell the player about the history of the ongoing war, victories and losses, the soldier’s personal life and his experience in the horrors of war. Some of this information is a fact (i.e. history) and some of it is this soldier’s personal view on the events.  
## Technical 
### Development Details 
The game could be developed on the Unity engine and it will be made for the PC. Porting it to other consoles could be possible, but will not be our priority. 

### Controls 
Moving in game will work with WASD controls. Player can jump, dodge dash, do a weak melee attack, attack with equipped spell, select a spell with the scroll wheel or numbers. There is an “interact” button, that can be used to open doors, open chests and talk to NPCs. Esc-key will open the pause menu where you can save and exit, if you are in a safe zone, exit the run or open the options. The volume, graphics settings and key-bindings can be changed from the options menu. 

### Mechanics 
The game’s mechanics are heavily based on combining elements and environmental hazards to defeat enemies and unlocking pathways. For example, if water spell is aimed at the ground it leaves a "puddle". An ice spell can then be used to freeze the puddle and by that, temporarily freezing the enemies standing on it. However, some of these combos work only if the puddle is large enough. The spells can also be used together with level design to gain an advantage. For example, a (bottomless)pit can be frozen, where enemies and players can stand on top of, until the ice melts. 

Spells won’t use any resource such as mana, instead there is a certain amount of charges. All charges will refill after a cool-down time. For example, there could be five charges that the player has. Some spells can be constantly casted by holding down the "cast" button (uses 1 charge per 5 seconds) and others work as a single shot (1 charge per shot).  

There is a dodge dash move with a slight cool-down. It is used to evade enemy attacks and if timed correctly, it grants the player a few invincibility frames. 

### Spells & weapons 
The player starts with a basic staff, which has two spell slots. Before a run player can choose from the following spells: 

* Fire  
* Water 
* Electricity  
* Air  

These are the basic elements of the spells, but there are different elements which can only be found in a run (i.e. earth). There are also stronger versions of the basic elemental spells. For example fire element has an stronger spell called fireball, which is single shot, but deals more damage. Taking this spell however, does not discard the basic version of the spell, as it is just a different spell of the same element. This meaning you can still have both basic fire and fireball spells equipped on your staff. Other upgraded versions of elements are: 

* Water → Ice  
* Electricity → Thunderbolt (instant strike on a selected enemy) 
* Air → Tornado (conjured tornado that can be commanded) 

The basic spells of fire, water and electricity can be casted continuously causing a stream of sorts, but the basic spell of air works as a single shot. It has kind of shotgun logic where a single “shot” deals a lot of damage close-range, but very little from far away, and the push-back works with the same logic.  

The player can also find upgraded staffs which allow increased spell slots and damage values. The staff has a melee strike for close-quarters. 

### Spell synergies/combinations 
Different elements combined can create synergies. For example casting fire on a puddle of water on the ground creates a temporary fog wall, which grants invisibility from enemies on the other side of the fog. Water (or ice) casted on fire will stop the burning effect. Other synergies include: 

* Fire + electricity (on enemy) = stronger electric hit + spreads fire 
* Water (on ground) + electricity (on enemy) = +damage to wet enemies, spreads to all wet enemies in room 
* Electricity + air = strong stun + knock-back 
* Tornado + fire = +damage + burning effect 
## Level Design 
### Key Locations 
The demo will have 1 major area, the forest stage. The player will prepare and choose to start a new run from the menu. The forest stage will be split into two randomly generated stages. The first stage will end with a room that gives a reward and the second stage will end with a boss fight. 

### Objects 
There are multiple upgrades and spells that the player can find in a run. These upgrades can be found from chests that can be found in special “reward” rooms, after boss fights or from puzzle rooms that require the use of a specific element in order to be accessed.  

All the items in the game are not immediately available to the player and need to be unlocked through certain achievements before they can be found from chests. These achievements will be specific to their unlockable items. For example, the player would need to kill 40 enemies using fire damage to unlock the spell “fireball” and after doing this once, they may find this spell in any future run. 

Upgrades that a player may find from chests can either increase the maximum health, health regeneration. There are also could be perks, such as, cooldown reduction from killed enemies with a scavenger perk. They may find new staffs that would have more damage and give the player a different amount of spell slots that could allow them to carry more spells. These upgrades are only active for the duration of the current run. The later area that the player is in the stronger the upgrades from chests will be.  

### Game Flow 
1. Player will explore the area, by going to different rooms. 
2. After defeating all the enemies in a room, the doors open, and the player can explore again. 
3. Player will find reward rooms with chests that give useful upgrades. 
4. Player find a room that has a bigger reward and sends them to the next level. 
5. After exploring enough of the next level, the player find a big menacing boss door. 
6. Player will find the boss room and enter when ready. 
7. Player will learn the boss’s patterns, and eventually defeat it. 
8. Player will be given a new upgrade and sent to the next stage. 

## Character design 
### Protagonist design 
The game will be in first person so the only visible design of the protagonist will be the right hand holding the staff.  

### Enemy design 
The game will need interesting enemy encounters that discourage the player from fighting them head-on. Instead, the enemies should encourage the players to study the enemy’s actions and find their weaknesses. Forest area has three different kinds of enemies: small and fast slime; bigger, stronger but slower enemy; ranged enemy with elemental projectiles. 

### Boss design 
End of demo boss- Plantie. It will be mostly immobile and stay at the middle of the arena, being an easy target. It will attack using its vines and uses them to create walls that need to be removed by the player. If the player does not stay moving while dealing with this boss, it can easily trap the player from moving and deal a large amount of damage and end the run. Plantie will create pools of poison that can be removed by some spells, but will deal a lot of damage when stood on. 

## Graphics 
### Style Attributes  
We will be going for a cel-shaded slightly cartoony graphics style. Everything interactable or relevant to the player, like the enemies, will have slightly saturated color schemes, so they will always be clearly recognizable.  

When the player is looking at something that can be interacted with, there will be text near the object that shows the interact button and says briefly what interacting will do. For example, when looking at a chest, the text would read “Open [e]”. 

When an enemy takes damage, there will be some particle effects relevant to the source of damage. For example, spikes would show small blood splatter, electricity would show static and so on. When the player receives damage, the screen will shake a little and the corner of the screen that the hit came from will have a slight red hue.  

## Audio 
### Style Attributes 
The game has a medieval fantasy theme so the music and sound effects are trying to express that genre and enhance the atmosphere. Instruments such as lute, harp and flute could be used to create fitting compositions for the “time-period”. The different areas will have a great variety of musical elements between them while still maintaining the core themes of the game. Because the game is fast-paced, the music’s tempo and pompousness will increase according to the intensity of the gameplay. 

### Music 

Track list: 

1. Main theme/menu music 
2. Forest (neutral) 
3. Forest (combat)  

From these tracks, adaptive music is created by fading out the first cue, while the second cue fades in. There are similarities in the area’s neutral and combat themes (combat is more menacing and has a higher tempo). Menu area will have a calm and simple melody which is supposed to make the player feel safe and relaxed. Forest will have more of a mystic and adventurous theme.   

### Sound effects 
Sound effects will be made mostly by foley. Audacity can be used to record and alter the sounds to match the desired result. Sound effects needed are for these examples: 

 

#### Characters: 
* Taking damage 
* Hitting  
* Jumping 
* Dying 
#### Interactive: 
* Footsteps 
* Weapons/casting spells 
* Door open/close 
* Chest open/close 
#### Ambient: 
* Weather (wind, rain, thunder etc.) 
* Nature (birds, a water stream, water drippling from the caste ceiling, Inferno’s fire etc.) 
* Drones 