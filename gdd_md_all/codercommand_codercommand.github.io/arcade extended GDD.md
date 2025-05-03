+++
title = 'Arcade: Extended GDD'
date = 2024-04-30
draft = false
+++

Copyright, Rian Rutherford, 2024, All rights reserved.

_This is a live document and continues to have edits._

![Image](../arcade-gdd/gavin-rothery-concept-piece-8-colour-schemes-black-v006.jpg)
> ^ Concept art by Gavin Rothery [source](https://www.artstation.com/artwork/bKXE2G).

# GDD Extended

This document originated as an extended section in the GDD. From 30th April 2024 it has been separated into its own document. While this has already been published, it is a live document and will continue to receive edits.



# Scale & Pacing

Make the player's spaceship the size of a house or office. This has the benefit of making the environment more compact because relative to other objects in the world the player is large. It also means even if the player is moving slow, because of the scale difference they'll feel like they're moving very fast.

Having spaceships large in scale relative to real world objects also means instead of a fight taking place at a city junction or above a river, it now takes place over an entire town.

Large doesn't mean UNSC from Halo large, it means taking a spaceship with the design of a fighter, and scaling it up so by ratio it's large, for example x4 larger than a house (4:1).



# Weapons Ideas

All most projectiles should be slow enough that a player has enough time to react, turn 180 degrees, and shoot it down with another projectile.


##### Standard Missile

Scans for a target and chases the closest target. This includes other missiles, not just spaceships. The missile does medium damage to the target it hits. This missile does not have AOE damage.


##### Micro Nuke Missile

Scans for a target and chases the closest target. This includes other missiles, not just spaceships. The missile explodes in an AOE when destroyed by another missile, reaches the end of its life, or hits a target. The missile does huge damage to everything in an AOE. The missile is slower than most others.


##### Triple Missile

You shoot a missile that breaks into 3 smaller missiles, each doing 1/3 the damage of a standard missile. The missile and smaller missiles have the same behavior as the _Standard Missile_.


##### Cloud Rocket

A missile that shoots in a straight line, if it detects a missile in it’s range it will explode creating a smokescreen This smoke screen stops missiles from tracking their target while inside the smoke. Missiles in the smoke tranvel straight till they leave.


##### Rocket Barrage

The player can shoot lots of small rockets like a machine gun or rocket pod. These rockets have poor turning making them bad at hitting targets suddenly changing directions. 

{{< youtube N4JhkjtCnVQ >}}


##### Gravity Void Missile

A missile that creates a gravity void sphere (like a black hole) when it’s near an enemy spaceship or missile. It lingers in the area for a long period of time, and pulls stuff towards it. It does not cause damage to anything it pulls in. The gravity void is intended as a type of crowd control ability and large AOE map control ability.



# Level & Environment Design Ideas

##### Moving City/Moving Ground

When close to the ground as you move above it, structures will appear out from the ground in front of you and disappear again behind you.

Specifically the structures will achieve this by moving up and staying out fully extended a second or two before the player moves past them, then will move back down into the ground.

One variant idea of who this moving ground could be as you fly over a desert, the sand jumps to form pillars or other shapes when you’re near the ground. The plot/logical reasoning is because the sound bounces from the acoustic sound of the spaceship, example:

{{< youtube Q3oItpVa9fs >}}


##### Multi Atmosphere

Levels can have multiple atmospheres with different amounts of air friction/air density.

1. Space no friction
2. High altitude low friction
3. Low altitude high friction
4. Water/Other extreme friction

The friction in the air could also scale with a gradient or use a curve graph to have a wide array of frictions at different altitudes scaling differently.


##### Fog Level

Foggy level where fights look like lots of small dots flashing in a cloud.



# Market Research

Arcade's competitors are games that feature multiplayer spaceship combat targeting audiences that are looking for action gameplay instead of a 1:1 space simulator.

Our tags include: Multiplayer, PvP, Sci-fi, Action, Space, 3D, Spaceships. Using all these tags doesn't reveal all our competitors, you must use different combinations to get a feel for what's out there. [SteamDB](https://steamdb.info/instantsearch/) was used to search for competition.

Found competitior games:
1. [In The Black](https://steamdb.info/app/380110/) The game is in development by [Impeller Studios](https://impellerstudios.com/). Its target audience are people looking for hardcore PvP spaceship combat. While we share a similar audience, our combat and movement are fundamentally different. Because of this we share some of the target audience, but are not in direct competiton tying to provide the same game.
2. [Star Age: Space Combat](https://steamdb.info/app/1726690/) is an already release game with no playerbase. It's a dead game, quick google search and the only YouTube video available is a trailer. While they're arcade like with simple controls and thirdperson camera, they do not share our design pillars or target game qaulity on release.
3. [Lost Fleet](https://steamdb.info/app/1911780/) is a competitor of Arcade. They have 3rd person flight controls, homing projects & lock-on weapons, and PvP. Many players gave feedback saying it had potential but still needed polishing and adjusting. Some comments included floaty movement making it hard to aim when shooting, to many lock-on based weapons they want some weapons with skill expression. The feedback given to this game should be used to help inform Arcade. Arcade shouldn't suffer from two of the complaints I read because our movement is very fast, and while most weapons are homing there is skill expression in your loadout, shooting down other projectiles, etc...
4. [BattleGroupVR](https://steamdb.info/app/1178780/) VR based space battleship simulation game. We are not competition and don't have anything in common.
5. [Fly Dangerous](https://steamdb.info/app/1781750/) could be a good inspiration for some things, but they're not competition. They don't share anything in common with Arcade except spaceships and fast movement.
6. [STAR WARS™: Squadrons](https://steamdb.info/app/1222730/) is a direct competitor of Arcade. There is a lot of comments and feedback we can take from this game and use for arcade. Fortunately while the game is our competitor according to the feedback EA killed the game and there is no one playing multiplayer, only solo. Something to consider that was mentioned by one reviewer is that when there are people playing PvP, it's hardcore vetrans which stop everyone to the point of being unable to play. Arcade will need to be very careful to not to have such a huge disadvantage between vets and noobs, or will need some balance match making.
7. [Project Genesis](https://steamdb.info/app/700240/) is a competitor of Arcade, but don't appear to successful. They don't appear to be able to keep the game enjoyable enough for people, based on read feedback this appears to have to do with not enough players, some people having laggy servers, gameplay getting boring quickly, and missing polish.
8. [STAR WARS™ Battlefront™](https://steamdb.info/app/1237980/) has a spaceship flying mechanic which means we share some competiton with it, but the game doesn't share the same mechanics or gameplay. The game has great reviews and people loved it, but the game is pretty dead now with it being very hard for anyone to get into multiplayer games.
9. [Phantom Galaxies](https://steamdb.info/app/1272550/) mecha+spaceship game. While they should be competition, the game is dead and the reviews are very mixed.

There is room for a multiplayer spaceship shooter with no direct competition because most games that would control that market are either dead from age or have other problems causing them to die off.

Most of the dead or dying games do not appear to be dying from a lack of content, but instead from a lack of polish and qaulity for what's already there. And for the older games they would have players if there were given care and attention to entice older players back and bring in new ones.

Arcade's goal should be to provide an extremely polished experience on release even if it means it has less content than other games, because insufficient qaulity of what was already there is what lead to the decline of most spaceship games.
