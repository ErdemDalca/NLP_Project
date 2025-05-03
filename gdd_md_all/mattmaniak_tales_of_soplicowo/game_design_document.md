# Tales of Soplicowo

Adventure RPG video game

## Game Design Document

by mattmaniak

## Table of Contents

- [Overview](#overview)  
  1. [Motto](#motto)  
  2. [Logline](#logline)  
  3. [Genre](#genre)  
  4. [Objective](#objective)  
  5. [Setting](#setting)  
  6. [Plot](#plot)  
  7. [Inspirations](#inspirations)  
  8. [Unique Selling Point](#unique-selling-point)  
  9. [Sources](#sources)
- [Development](#development)
  1. [Technologies](#technologies)  
  2. [Assets Budget Summary](#assets-budget-summary)  
- [Gameplay](#gameplay)  
  1. [Key Mechanics](#key-mechanics)
  2. [Core (Low-level) Loop](#core-low-level-loop)
  3. [High-level Loop](#high-level-loop)
  4. [Core Number](#core-number)
  5. [Approach](#approach)
  6. [Modularity](#modularity)
  7. [MoSCoW analysis of mechanics](#moscow-analysis-of-mechanics)
  8. [Winning and Losing](#winning-and-losing)
  9. [Prizes](#prizes)
  10. [Statistics of the Player](#statistics-of-the-player)
  11. [Progression](#progression)
- [Characters](#characters)  
  1. [Player](#player)  
  2. [NPCs](#npcs)  
- [World](#world)
  1. [Environment](#environment)  
  2. [Map](#map)  
  3. [Levels](#levels)  
- [Story](#Story)
  1. [Timeline](#timeline)  
  2. [Events/Books](#events-books)  
  3. [Quests](#quests)  
  4. [Endings](#endings)  
- [Graphics](#graphics)  
  1. [Art Direction](art-direction)  
- [Controls](#controls)  
- [Sound](#sound)  
  1. [Music](#music)  
  2. [Effects](#effects)  
- [Accessibility](#accessibility)  
- [Miscellaneous](#miscellaneous)  

## <a id='description'></a>Description

1. ### <a id='motto'></a>Motto

   Fight with word like a sword/Unite with word, not a sword.

2. ### <a id='logline'></a>Logline

   Play as a 19th-century priest whose goal is to reunite Polish noble-class in order to prepare uprising against Russian. Use word as a sword and try to persuade them. Will you succeed?

3. ### <a id='genre'></a>Genre

   Adventure with RPG elements.

4. ### <a id='objective'></a>Objective

   Do some open-source in game development. Create game for the people.

5. ### <a id='setting'></a>Setting

   Occupied Lithuanian areas of 1811.

6. ### <a id='plot'></a>Plot

   Taduesz backs to Soplocowo from Vilnus. This causes the castle conflict again. His father - Priest Robak has to help Soplicas get the castle. However, some things go wrong during his journey and Horeszkos' are preparing some big too.

7. ### <a id='inspirations'></a>Inspirations

   "Don't be told what games must be. Instead find new and different types of games."  
   ~Hideo Kojima

   As the title suggests, those are only inspirations and won't be copied directly. It's just a list of key elements those seem to be fitting to our idea.
   - *AER Memories of Old* - minimalistic graphical design with faceless characters.
   - *Disco Elysium* - engaging dialogue trees instead as a combat.
   - *Hellblade: Senua's Sacrifice* - environmental puzzles and personal narration.
   - *Horizon Zero Dawn* - specific save points only.

8. ### <a id='unique-selling-point'></a>Unique Selling Point

9. ### <a id='sources'></a>Sources

   - [PDF version of *Pan Tadeusz* uploaded by Leonard Kress](https://leonardkress.com/Pan%20Tadeusz.pdf).

## <a id='development'></a>Development

1. ### <a id='technologies'></a>Technologies

   The newest Python 3.12, Panda3D engine with it's Render Pipeline.

2. ### <a id='assets-budget-summary'></a>Asset Budget Summary

   The less the better.

## <a id='gameplay'></a>Gameplay

The player acts as a priest whose goals is to go through the quests which are strictly related with Polish noble-class and *Sir Thaddeus* events. The goal is to persuade them to reunion. It will be done via helping them during various tasks from the Mickiewicz's book and deep talks about the Commonwealth. Optionally, the player will have to find and repair chapels.

To solve those problems, player will have to explore levels those will be labirynths with various paths to go through. They will be somehow connected with a camera's fixed pitch and base on the problem of getting into some kind of relatively complex place.

1. ### <a id='key-mechanics'></a>Key Mechanics

   - Constantly jump between Robak's life and Jacek's interactive memories those dialogue choices will affect Priest's behaviour.
   - Explore invisible level labirynths to find your path as the Priest or as Jacek.

   Both Jacek's and Robak's world will be dualistic, however there will be only one predominant style for each. Jacek's memories will include dark fantasy elements. Also there will be subtle positive stuff as he was a young vagrant. Robak's real world will be wonderfully colorful and inspired by high fantasy. On the other side, it will be still an occupied motherland.

2. ### <a id='#core-low-level-loop'></a>Core (Low-level) Loop

   1. Walk.
   2. Go Back.
   3. Repeat.


3. ### <a id='high-level-loop'></a>High-level Loop
   1. Let the level guide you via labirynth.
   2. Enter one of the memories.
   3. Choose your path via dialogues and exploration.
   4. Enter next level as a Robak or Jacek and continue your internal journey.

4. ### <a id='approach'></a>Approach

   It will be somehow mix of systemic and directed approach: on the one hand, it will allow player to use mechanics on their own, like various exploration possibilities and dialogue choices, on the other hand, the game won't have much mechanics (above two only) so the directed approach will be present too.

5. ### <a id='modularity'></a>Modularity

   The gameplay will be a little modular only, as there will be labirynth and NPCs conversations as the cores. These mechanics modules will overlap.

6. ### <a id='core-number'></a>Core Number

   Core number of the game should be 2 multiplications to symbolise a dualism everywhere, eg. there should be two ways to get into an area, two dialogue answers...

7. ### <a id='moscow-analysis-of-mechanics'></a>MoSCoW analysis of mechanics:

   - **Must have**:
     - High third-person perspective camera with a fixed pitch angle.
     - Comperhensive dialogue trees with short option and truly story-changing lines to reduce translations costs.
     - Mandatory but various time limit for dialogues with a possibility to skip an answer in order to **favour human connection**.
     - Reputation system.
     - Detailed and dense world.
     - Auto save during specific story moments.
     - *Press any button to continue* after loading screens.
   - **Sould have**:
     - Day-night cycle that changes gameplay and mostly negative night consequences.
     - In-door visibility - transparent portal on player or buildings half-transparency.
     - Basic in-game menu with: map, reputation graph, skills and current quest description.
     - Symbolic hints: icons, GIFs, sounds to represent settings differences and visualise invisible.
     - Compass.
   - **Could have**:
     - Basic economy for repair stuff trade.
     - Time skip only near repaired chapels.
     - Chapels repair and manual save possibility near them.
     - Courier's backpack when carrying repair tools.
   - **Won't have**:
     - Shoulder third-person perspective camera.
     - Minimap.
     - Combat.
     - Stealth.
     - Random encounters.
     - All unique *Sir Thaddeus* characters.

8. ### <a id='winning-and-losing'></a>Winning and Losing

   It's inevitable that a player could get lost, however this particular scenario will be quite similar to the deep exploration. Quite similar scenario will appear when a player will explore levels enough, there will be the same chance to gain a prize.

9. ### <a id='prizes'></a>Prizes

   There will be a chance to find something that will enhance the historical lore and/or add additional dialogue.

10. ### <a id='statistics-of-the-player'></a>Statistics of the Player

    The game shouldn't be explicit with stats displaying them by numbers. Instead, it should use some graphs and mainly storytelling to show characters' parameters. Here comes the *show, don't tell* rule.

    Optionally, there will be a reversed triangle that symbolises main character's attitude. Center will be the initial neutrals state. Left corner will symbolise Horeszko family, while right one - Soplicas. Collaboration with Russians will be placed at the bottom. As the protagonist is one of the Soplicas, player's attitude may be prejudiced, however to reconceal noblemen and thus succeed, neutrality will be necessary. Those attitudes will be the essence of the RPG loyality system, however it may judge player's morality so it should be considered deeply before optional implementation. This would trick player as working with Soplicas will be suggested at first sight, even if they won't be too familiar. Because of that, player probably will try to become neutral, and tho will probably achieve a relative success.

11. ### <a id='progression'></a>Progression 

    Note that each further labirynth and dialogue should be harder to provide a customizable progression system with a progressive difficulty.

    **Game's content and progression chart here.**

## <a id='characters'></a>Characters

There should be 12 characters, excluding the players. Each of them should be connected with exactly of the 12 Jungian archetypes. One of them will by same as the player's archetype as opposition.

1. ### <a id='player'></a>Player

   - **Father Robak** a.k.a. **Jacek Soplica** - a catholic priest, ex-vagrant.

2. ### <a id='npcs'></a>NPCs

   Every of them will be at least neutral on unfriendly. There will be a possibility to gain some friendship relations according to player's decisions.

   - #### Soplicas

      - **Protazy Brzechalski**.
      - **Tadeusz Soplica** - title character
      - **Judge Soplica** - mentor archetype - conservative Pole stereotype.

   - #### Horeszkos

      - **Count Horeszko** - Dandelion from *The Witcher*.
      - **Zosia Horeszkówna** - maiden archetype - Tadeusz's crush.
      - **Gerwazy Rębajło**.

   - #### Russians

      - **Major Płut** - Russian officer of Polish descent.
      - **Captain Nikita Rykow**.

   - #### Dobrzyńscy

      - **Maćko Dobrzyński**.
      - **Bartek Brzytewka**.

   - #### Neutral

      - **Jankiel** - local Jew.
      - **Telimena** - seductress archetype - *femme fatale*.

## <a id='world'></a>World

Closed but with various options to achieve a destination. Internal legacy prototype `mapa_w_skali_v2.jpg` is a good initial reference for a level design. It should be full of symbols to communicate effectively.

1. ### <a id='environment'></a>Environment

   ...should not only perform as a static world component, but also as a dynamic narrative tool. Using various intense and distinctive weather types will according to the present events willprovide additional background and experence.

2. ### <a id='map'></a>Map

   Contains some levels on the single map. It will be important storytelling and reputation system component too - some places will be unavailable, while other will be available according to the player choices. This will provide gameplay nonlinearity. Each level will be symbolic and will be uniqely different. Walking speed and placement of objects should provide a possibility to reach every building or place in two seconds.

3. ### <a id='levels'></a>Levels

   1. Chapel.
   2. Soplicowo - starting point, hub world, maybe.
   3. Horeszko's Castle.
   4. Forest.
   5. Jankiel's Inn.
   6. Bear's Forest.
   7. Horeszko's Castle.
   8. Soplicowo.
   9. Count's Palace.
   10. Dobrzyn.
   11. Sopliciwo.
   12. Dobrzyn.
   13. Soplicowo - ending point.

## <a id='Story'></a>Story

There is no distiction between and side jobs to simplify implementation. There will be nonlinear main quests only whose will have optional tasks sometimes to provide more diverse choices and consequences.

1. ### <a id='timeline'></a>Timeline

   A distinctive element will be that the game will use the Monomyth in the case of Priest Robak and an inverted Monomyth in Jackes's story. Initially, the player will start from the same moment in 1811, and then will go through the Robak's events traditionally and Jacek's events from this point to the past. Robak's past world will be introduced softly by his mentions about memories, which will be revealed step-by-step.

2. ### <a id='events-books'></a>Events/Books

   1. Tadeusz arrives to Soplicowo, and Priest Robak later on from a Chapel.
   2. Count Horeszko arrives to a Castle and stalks Zosia, Robak comes in-between.
   3. Mushrooming with Soplicas.
   4. Robak encourages noblemen in Jankiel's Inn to reconceal, then helps with a  Bear hunting.
   5. Robak gifted with the Bear meat, serious argument in the Castle.
   6. Priest arrives to Soplicowo once again, then to the Count's Palace tracking Protazy.
   7. Robak tries to track Gerwazy to Dobrzyn (not included in the source).
   8. Priest Robak arrives back to Soplicowo and makes a coming out to Judge.
   9. Dobrzyn noblemen captive Soplicas, Robak goes to there and back with Maćko Dobrzyński is wounded nearly after in a Battle with Russians.
   10. Public coming out and death of Robak, talks about emigration.
   11. Public rehabilitation of Jacek Soplica in 1812 by Podkomorzy, during Napoleon's raid on Russia.
   12. Junket with Polish generals in Sopliciwo, Tadeusz and Zosia wedding, a hope.

3. ### <a id='quests'></a>Quests

   1. Some kind of intuitive and immersive tutorial to provide an **intro**.
   2. A little harder quest to create an **exposition** and speed-up **pacing**.
   3. Harder quest with a **rising action**.
   4. Final hard quest that becomes a **climax**.
   5. A slowdown and player's Catharsis.
   6. A short cutscene/gameplay event as a final conclusion. 

4. ### <a id='endings'></a>Endings

   - The Blind One - Soplicas.
   - The Lawful Harsh - Horeszkos.
   - The Collaborant - Russians.
   - The Reconciler - active neutrality.
   - The Vagrant - live as Jacek before.

## <a id='sound'></a>Sound

1. ### <a id='music'></a>Music

   Some tracks. Must be interactive and adaptive as games are interactive medium.

2. ### <a id='effects'></a>Effects

   Simple free assets.

## <a id='graphics'></a>Graphics

3D low poly pixel art, where pixels are used only for details. Meshes and the textures' context are classicaly flat. Rich post-processing can be easily achieved due the Render Pipeline.
1. ### <a id='art-direction'></a>Art Direction
   Beautiful.

## <a id='controls'></a>Controls

Easy.

## <a id='accessibility'></a>Accessibility

Each in-game feedback is expressed via at least two sensitive events, eg. dialogues use subtitles and narrator, enemies distraction - some character outline and a proper sound. Visual effects change it's shape, not color only to provide meaningful experience also for color-blind people. Most of the information is shown using mix of various visual and sound effects. Also the game should support at least custom mappings for: keyboard + mouse and Xbox, PlayStation pads. Game controls should be as much analogue as possible, eg. triggers on pads. The game should contain full colorblind-friendly only visuals optionally.

Context subtitles, eg. [jazz music in backround].

## <a id='miscellaneous'></a>Miscellaneous

- Easter eggs?
- Some kind of metagame?
- Negative emotions per contrast?
- Gameplay aided by Jacek/Robak.
- The game should contain verisimilitude.
- Convert this doc to a future tense!
- [To monomyth or not](https://www.steveseager.com/heros-journey-four-innovative-narrative-models-digital-story-design/).
