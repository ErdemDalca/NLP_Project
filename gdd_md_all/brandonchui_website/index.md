---
title: "My Experience Making An Autobattler"
description: "Making an autobattler game"
date: "2024-09-29"
tags: ["game-development", "unity", "c-sharp", "design"]
---

A game design student at USC and I collaborated on this project. I translated the game design document into code, and the student also contributed by adding some of the art and visuals to this small game in collaboration with a game design student at USC. I was responsible for translating the game design document into code, and they also contributed to adding some of the art and visuals of this small game.
![Description of the image](/AutoGame-1.jpg)
## Features
**Level-Up System**: The leveling-up system was a linearly implemented system that, in the end, could have scaled better and made the game somewhat tricky as you reached higher levels. On the other hand, the game was thus too easy in the beginning. You could also upgrade various craftable equipment. The leveling up raised your character's stats.

**Crafting**: This mechanic uses an inventory system to track all the random loot each monster gives. A randomly generated number determines the crafting item dropped based on the color tile where the player killed the beast.

**Autoplay and Pause**: The game supports autoplay as it is an auto battler in which you watch your character defeat creatures by themselves, and you control the various equipment and levels from a high level. The movement worked by having a spline on which the main character travels - a closed loop line in which they will cycle endlessly. The play and pause buttons will stop the character's movement. There was also a fast-forward button, in which we just doubled the character's movement speed.

**Issues**: The game was tricky at times, as the balancing was a big issue that we needed more time to address before the deadline. There are instances where the monsters became so hard that they could defeat the character in just a couple of hits, leaving a rather unfun experience.


![Description of the image](/AutoGame-2.jpg)
