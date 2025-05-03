# Road of Heroes

## Table of Contents

1. [Overview](#overview)
2. [Characters](#characters)
3. [Gameplay](#gameplay)
4. [Game Experience](#game-experience)
5. [Items](#items)
6. [Art & Music](#art--music)

## Overview

### Story

An apocalyptic catastrophe known as *the Eternal Night* has consumed the continent. In the ever-lasting darkness which has covered the sun and blocked all the light, a profound, contagious curse has spread across the world, bringing abominations from an evil dimension.

4 heroes, each from a different background, have come together to embark on an epic journey to seek out the sources of *the Divine FIre* in hope of fending off the terror of the Night. In their way, with determination, our heroes will meet new comrades, anihilate evil beings, save the people and help reclaim their homeland. Moreover, there is more to the mysteries behind the catastrophe and the world to be discovered in this great expedition.

### Gameplay

Road of Heroes is a **2D roguelike turn-based tactical role-play game**. In the game, the player plays as a group of heroes to set out for a journey to seek *the Divine Fire* in order to save the world from an apocalyptic catastrophe known as *the Eternal Night*. In this journey, the player will unravel the mysteries of the world, collect powerful relics to gear up the heroes, and fend off enemies and complete quests to claim rewards. The world is divided into regions with each region controlled by a powerful demon. The player needs to defeat the demon in order to proceed to the next part of the journey, until the heroes finally arrive at the Divine Fire.

## Characters

The player recruits **heroes** to venture into expeditions.

Each hero has 5 base stats:

- **Speed**: characters with higher speed takes actions before those with lower speed in a battle turn.
  
- **Agility**: increases the chance of dodging off attacks and the distance the character can move through in a battle turn.
  
- **Strength**: increases the damage dealed from physical attacks.
  
- **Perception**: increases the chance of dealing critical attacks.
  
- **Precision**: increases the hit chance of skills during combat.
  

Each hero's physical conditions are reflected as the following 4 values:

- **Health (HP)**: character dies when the HP reaches 0.
  
- **Magicka**: character consumes Magicka to cast spells.
  
- **Sanity**: character receives heavy penalties and de-buffs when sanity is low.
  
- **Fatigue**: lowers the damage dealed by attacks.
  

At the start of the game, the player has 4 randomly generated heroes. The initial limit for the number of heroes recruited is 8, but it can be increased via upgrades.

### Races

Each hero also has a **race**. A hero's race affects his starting base stats and gives him 3 **gifts**, which are race-specific skills that can only be used for a limited number of times per battle. The races include **human**, **elf**, **dwarf** and **orc**. Each of the 4 initial heroes at game start is of a different race.

### Traits & Disease

Each hero also has up to 5 **traits**. A trait may have various effects, such as offseting the hero's fighting abilities, banning the hero from doing certain actions or enabling special actions for the hero. Every hero comes with 1 to 3 traits at start and may gain or lose traits during the game play.

**Diseases** are similar to traits but they are temporary. Each disease has a **base recovery rate**.

### Skills & Hero Classes

Heroes use **skills** to fight the enemies in battles. All skills can be learnt by all heroes, but a hero can learn a maximum of 8 skills. The player can pick any 5 of the 8 skills as **active skills** which the hero can use during battles.

Each skill has some **affinity** towards certain **hero classes**, which has 3 levels:

1. **High affinity**: $+20\\%$ effectiveness when used by the matching class.
  
2. **Medium affinity**: $+10\\%$ effectiveness when used by the matching class.
  
3. **Low affinity**: $+5\\%$ effectiveness when used by the matching class.
  

A hero will be categorised to the class to which his skill set has the highest total affinity, with ties broken randomly. Class affects the equipment a hero can use and enables certain unique interactions with other game objects. The hero classes are:

- Alchemist
  
- Archer
  
- Assassin
  
- Bard
  
- Enchanter
  
- Mage
  
- Mercenary
  
- Necromancer
  
- Occultist
  
- Ranger
  
- Spellsword
  
- Warrior
  

To raise a powerful hero, the player needs to pay close attention to the hero's base stats and traits in order to determine the most suitable class for the hero, and thus let the hero to learn the right skills to optimise his abilities.

## Gameplay

The game is set in a fictional fantasy world and the player starts with four default characters in their expedition team. In order to reach *the Divine Fire*, the player needs to pass through several **regions**. Each region is guarded by a powerful **boss** which the player must defeat in order to proceed to the next region. However, the player can freely choose the right timing to challenge the boss. Prior to the boss fight, the player can complete **expeditions** to upgrade the heroes.

### Cities

The **city** is the headquarter in each region. In the city, the player perform the following actions to prepare for the next expedition:

- **Training**: the player can choose one hero to spend money upgrading the heroes' skills.
  
- **Rest**: the player can let an hero take a rest. Resting will remove all permanent de-buffs from the hero, fill up the hero's HP, magicka and sanity, and clear all fatigue of the hero. However, resting heroes cannot join the next expedition.
  
- **Trade**: the player can sell or purchase relics and other useful **consumable items** or purchase upgrades for the expedition team.
  
- **Recruitment**: the player can recruit new heroes or fire current heroes from the team.
  
- **Treatment**: the player can spend money on:
  
  - **Short-term treatment**: increases the recovery rate of a disease for a hero.
    
  - **Long-term treatment**: completely cures a disease for a hero. However, heroes under long-term treatment cannot join the next expedition and will not regenerate HP, magicka and sanity.
    
  - **Spiritual Reconstruction**: removes one negative trait and fill up the hero's sanity. However, the hero cannot join the next expedition.
    

Heroes that return to the city from an expedition will immediately restore $20\\%$ of HP, magicka and sanity. When the player is ready, he can set out for a new expedition. When doing so, the player is given 3 **contracts**. Each contract is a main quest which needs to be completed in the next expedition. The player must choose 1 of them to start the expedition.

### Expedition

Each **expedition** emulates a **turn-based board game** with a **procedurally generated grid-based world map**. At the start of each turn, the player rolls the dice to determine how many moves can be taken in the turn. **Encounters** are randomly spawned in the map, which may include:

- **Enemies**: a battle will start.
  
- **Survivor settlement**: one or more from below may be available:
  
  - **1 to 3** heroes are available for recruitment;
    
  - a **merchant** is present in the settlement, with whom the player can trade items;
    
  - **settlers** may offer **side quests** which the player can accept, and receive award from if the player completes the side quest during the expedition;
    
  - the settlement has an **inn** where the player can spend money letting heroes rest. A rested hero will restore $20\\%$ HP and sanity.
    
- **Lair of darkness**: the player will face a battle with enemies that are more powerful than the expedition's average battle difficulty. However, the reward from such battles is *usually* higher.
  
- **Place of mystery**: a game event will be triggered. Based on the player's choice, he might either gain a reward or a buff for the heroes, or face some penalties.
  
- **Campfire**: the player can choose one of the two actions below:
  
  - **Search for salvage**: the player collect some **items** from the previous ones who used this campfire.
    
  - **Encamp**: the player will get **12 hours** which can be used to perform the following **camping activities**, each activity can be performed at most once:
    
    - Spend 1 hour to **have a meal**: restore $15\\%$ HP for every hero. The player needs to have sufficient **food** in the inventory.
      
    - Spend 2 hours to **have a feast**: restore $25\\%$ HP and $20$ sanity for every hero. A feast costs twice the amount of food needed for a meal.
      
    - Spend 2 hours to **perform group prayer**: restore $10$ sanity for every hero. If a hero has the **fervent** trait, he restores $25$ sanity instead. If a hero has the **atheist** trait, he restores only $5$ sanity.
      
    - Spend 4 hours to **arrange night duties**: select 4 heroes to guard the camp site to prevent **ambush** battles. However, these 4 heroes will not be able to rest.
      
    - Spend 3 hours to **perform dark rituals**: *if the player has an occultist in the expedition team*, select 4 heroes to undergo a dark ritual. At the cost of $10$ sanity, each of them has $75\\%$ chance of gaining a buff in subsequent battles.
      
    - Spend 2 hours to **cure a disease**: *if the player has an alchemist in the expedition team*, select one hero to remove one of his diseases.
      
    - Spend 2 hours to **enchant weapons**: *if the player has an enchanter in the expedition team*, select one hero to give a buff for sebsequent battles.
      
    - Spend 4 hours to **give a performance**: *if the player as a bard in the expedition team*, every hero except one selected bard restore $30$ sanity.
      
    - Spend all remaining hours to **rest**: all heroes except those on night duties lose some fatigue. The amount is proportional to the number of hours left. The camping ends once the team goes to rest.
      
- **Occultist's avatar**: the player can summon a dead hero back to life (see [Reincarnation](#reincarnation)).
  

The player can choose to end the expedition at any point of time to teleport back to the city. However, if the player does this before completing the main quest, no reward will be given and each hero in the expedition suffers $+20$ fatigue and $-20$ sanity.

### Battles

A battle is initiated when the player's expedition party encounters enemies in the map. The difficulty of the battles is determined based on the **average level** of the heroes in the team. In each battle, the player chooses up to four heroes to fight the enemies. The battle uses a **turn-based** system, emulating the battle system of *Darkest Dungeon*. The basic flow of a battle is as follows:

1. At the start of the turn, each actor (the player's heroes and the enemies) in the battle will be assigned a **speed**. This speed is determined by each actor's base speed plus a randomised offset ranging from $-4$ to $4$.
  
2. The actors will be ranked in non-decreasing order by this speed. If a hero and an enemy has the same speed, the hero is ranked before the enemy. In other situations, ties are broken randomly.
  
3. The actors will take moves in this order.
  
4. At each actor's turn, he can perform one of the following actions:
  
  1. Use a skill.
    
  2. Swap his position with one of the two neighbouring actors.
    
  3. A hero can skip the current turn, at the cost of a small reduction in sanity.
    
5. When all actors have taken their moves, the current turn ends.
  
6. The battle ends if one side has lost all actors, or if the player chose to retreat.
  

If the player has lost all heroes, the current expedition will be forced to terminate and 4 random heroes will become available for recruitment so that the player can continue the game.

During battles, if a hero has 0 HP, the hero will enter the **dying state**. For every damage the hero receives during the dying state, the hero has a $50\\%$ chance of dying. If a dying hero is hit with a **critical attack**, the hero will die immediately. At the dying state, the hero deals $50\\%$ less damage.

The dying state can be dispelled if the player manages to restore the hero's HP back to a positive value. However, the hero will then receive a **critically injured** de-buff which will cause the hero to receive $20\\%$ more damage and deal $20\\%$ less damage until the player finishes the current expedition.

**Relics** may be collected either as rewards from battle or through random encounters. The player can equip heroes with these relics to upgrade their combat abilities.

### Reincarnation

Reincarnation is a core element of player progression in the game. At an **occultist's avatar**, if the player has lost any hero during combat before, the player can attempt to summon the dead hero back to life by one of the following means:

1. The player can perform a **ritual to the dark lord** by spending a large sum of gold and sacrificing one living hero in the team. The ritual has a probability of failure. If the ritual succeeds, the dead hero will possess the body of the sacrificed hero and be brought back to life. The reborn hero will have the same stats as before, but the hero can choose to take the sacrifice's skills to add to the skill set or replace his original ones. This means that the ritual is a relatively low-cost low-risk method to resurrect a hero, with the benefit of possibly acquiring better skills for the resurrected hero.
  
2. The player can also choose to **reclaim the soul from the abyss** by sending a party of heroes to fight the devillish beings in the underworld. Heroes who die in this combat will not be able to reincarnate, but if the combat is victorious, the reclaimed hero will be brought back to life with higher base stats. For every hero who has died in this combat, the reborn hero can freely take their skills to add to his own skill set or replace his original ones. This means that the reclamation is a high-risk but high-reward way to resurrect a hero.
  

## Game Experience

The game will have a **mysterious and dark** base tone to symbolise a sense of the unknown and peril in the expeditions. However, it is important to note that **no explicit horror element** should be used to create a sense of scare in the gameplay. Overall, the player should feel **tension and distress** but the story will turn to **hopefulness** in the end as the player approaches the Divine Fire.

We aim to make the game playable with only mouse clicks, so as to simulate the experience of a **board game**.

## Items

There are 3 types of items which can be collected and used in the game.

**Relics** are powerful weapons, armours or trinkets which can improve the combat abilities of heroes. They may be spawned in game expeditions at random, or appear as rewards after battles, or be purchase from **merchants**.

**Consumables** are single-use items which aid in combat or expedition. They are usually purchased from merchants, but the player might also be able to find them scattered across game expeditions. Some consumables include:

- **Bandage**: cancel **bleeding** effect and restore a small amount of HP.
  
- **Herbs**: cancel **poisoned** effect and restore a small amount of HP.
  
- **Mage's Brew**: restore a medium amount of Magicka.
  
- **Alcohol**: restore a small amount of sanity and reduce sanity loss.
  
- **Stimulant**: reduce s medium amount of fatigue, but increase fatigue generation.
  

**Gold** is the currency in the game. The player can spend gold purchasing other items, or selling other items for gold at merchants. Merchants can be found in settlements, cities. There is also a very small chance of a merchant appearing in the wild at random.

## Art & Music

The art of the game will be dedecated to creating a grim and eerie atmosphere, and therefore a vision of a world at the verge of breaking apart amid an apocalypse. One important point to note is that **this is not meant to be a horror game**. The focus of the art and music is to convey a sense of **decay, darkness, despair and unholiness**. The player should be able to feel **tension and distress** from their immersion in the game, but **not direct horror** (however, fright might be *implicitly* felt from certain elements used in the art). The art should fit to the setting of a medieval fantasy world. For music, though, we are receptive to any genre and style.

We are receptive to all styles of art, including hand-drawn realistic art, doodling style sketches, pixel art etc. The specific detail and choice of art is largely dependent on the artist, as long as the art produced matches with the game's base tone.

For music, instrumental (i.e. lyrics-free) style is preferred. However, both classical style and modern/electronic music are possible for the game's purpose.
