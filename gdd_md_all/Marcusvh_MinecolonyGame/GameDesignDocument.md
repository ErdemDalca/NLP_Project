// note: CTRL + p => "markdown"
# Game Design Document

## Table of contents
- [Game Design Document](#game-design-document)
  - [Table of contents](#table-of-contents)
  - [Building](#building)
    - [All Buildings Descriptions](#all-buildings-descriptions)
      - [Townhall](#townhall)
      - [Farm](#farm)
      - [Builder's Hub](#builders-hub)
      - [Barracks](#barracks)
      - [Bakery](#bakery)
      - [Fishing Dock](#fishing-dock)
      - [Healing Center](#healing-center)
      - [Logistics Hub](#logistics-hub)
      - [Fabric Artisan](#fabric-artisan)
      - [Forester's Hub](#foresters-hub)
      - [Miner’s Hub](#miners-hub)
      - [Warehouse](#warehouse)
      - [Blacksmith's Forge](#blacksmiths-forge)
      - [Tavern](#tavern)
      - [School](#school)
      - [Market](#market)
      - [Watchtower](#watchtower)
    - [Table of Buildings and their tier upgrades](#table-of-buildings-and-their-tier-upgrades)
    - [Requirements for building tier upgrades](#requirements-for-building-tier-upgrades)
      - [Townhall Tier 2 Requirements:](#townhall-tier-2-requirements)
      - [Farm Tier 2 Requirements:](#farm-tier-2-requirements)
      - [Builder's Hub Tier 2 Requirements:](#builders-hub-tier-2-requirements)
      - [Barracks Tier 2 Requirements:](#barracks-tier-2-requirements)
      - [Bakery Tier 2 Requirements:](#bakery-tier-2-requirements)
      - [Fishing Dock Tier 2 Requirements:](#fishing-dock-tier-2-requirements)
      - [Healing Center Tier 2 Requirements:](#healing-center-tier-2-requirements)
      - [Logistics Hub Tier 2 Requirements:](#logistics-hub-tier-2-requirements)
      - [Fabric Artisan Tier 2 Requirements:](#fabric-artisan-tier-2-requirements)
      - [Forester's Hub Tier 2 Requirements:](#foresters-hub-tier-2-requirements)
      - [Miner's Hub Tier 2 Requirements:](#miners-hub-tier-2-requirements)
      - [Warehouse Tier 2 Requirements:](#warehouse-tier-2-requirements)
      - [Blacksmith's Forge Tier 2 Requirements:](#blacksmiths-forge-tier-2-requirements)
      - [Tavern Tier 2 Requirements:](#tavern-tier-2-requirements)
      - [School Tier 2 Requirements:](#school-tier-2-requirements)
      - [Market Tier 2 Requirements:](#market-tier-2-requirements)
      - [Watchtower Tier 2 Requirements:](#watchtower-tier-2-requirements)
      - [House Tier 2 Requirements:](#house-tier-2-requirements)
      - [Townhall tier 3 Requirements:](#townhall-tier-3-requirements)
  - [NPC](#npc)
    - [Table of NPCs](#table-of-npcs)
    - [NPC traits](#npc-traits)

## Building

### All Buildings Descriptions

#### Townhall
The **Townhall** serves as the central hub for managing the colony. It is where the player can oversee colony activities, assign tasks, and monitor the overall progress of their settlement.

#### Farm
The **Farm** is essential for food production, allowing colonists to cultivate crops. It ensures a steady supply of food, which is vital for maintaining the health and happiness of the colony.

#### Builder's Hub
The **Builder's Hub** is where builders work on constructing and upgrading various buildings. It plays a crucial role in expanding the colony's infrastructure and capabilities.

#### Barracks
The **Barracks** provide housing for guards and soldiers, allowing them to rest and store their equipment. This building is vital for maintaining security and defense in the colony.

#### Bakery
The **Bakery** transforms raw ingredients into delicious baked goods. It provides colonists with food that boosts their happiness and productivity.

#### Fishing Dock
The **Fishing Dock** is where colonists catch fish and process them for food. This building offers an alternative food source and supports the colony's nutritional needs.

#### Healing Center
The **Healing Center** provides medical care and treatment for injured colonists. It is essential for maintaining the health of the population and ensuring quick recovery from ailments.

#### Logistics Hub
The **Logistics Hub** manages resource transportation and logistics within the colony. It helps streamline the movement of goods, ensuring that supplies are delivered where needed efficiently.

#### Fabric Artisan
The **Fabric Artisan** specializes in creating clothing and armor from various materials. This building contributes to the overall well-being of colonists by providing necessary attire.

#### Forester's Hub
The **Forester's Hub** is focused on tree cultivation and harvesting. Foresters work here to maintain the forest, providing a sustainable source of wood for construction and crafting.

#### Miner’s Hub
The **Miner’s Hub** is dedicated to mining and gathering underground resources. Miners extract valuable materials such as ores and stone, which are crucial for various building projects.

#### Warehouse
The **Warehouse** acts as the central storage facility for the colony. It securely stores various items and resources collected by colonists, ensuring that supplies are well-organized and easily accessible.

#### Blacksmith's Forge
The **Blacksmith's Forge** is where tools, weapons, and armor are crafted from metal. This building is vital for equipping colonists and ensuring they are prepared for various tasks and challenges.

#### Tavern
The **Tavern** provides a social space for colonists to relax and socialize. It increases overall happiness and morale, contributing to a thriving community atmosphere.

#### School
The **School** is responsible for educating the children of the colony, enhancing their skills for future roles. It plays a crucial role in preparing the next generation of colonists.

#### Market
The **Market** serves as a trading hub where colonists can buy and sell goods. It facilitates resource exchange and helps maintain a balanced economy within the colony.

#### Watchtower
The **Watchtower** provides surveillance over the colony, enhancing security. It allows guards to monitor the surrounding area, ensuring that potential threats are detected early.


### Table of Buildings and their tier upgrades

| Name      | Description                                                | Cost                                                           | Size (Length, Width, Height) | Tier | Requirements                                            | More Info              |
|-----------|------------------------------------------------------------|----------------------------------------------------------------|------------------------------|------|-------------------------------------------------------|------------------------|
| Townhall  | The center of the colony. General management will be here.  | FREE                                                           | 16x8x14                      | 1    | FREE                                                  | [About Townhall](#townhall) |
| Townhall  | The center of the colony. General management will be here.  | 100 Wood, 250 Stone, 50 Coins, 20 Iron                         | 22x12x18                     | 2    | [Townhall Tier 2 Requirements](#townhall-tier-2-requirements) | [About Townhall](#townhall) |
| Townhall  | The center of the colony. General management will be here.  | 350 Wood, 1000 Stone, 200 Coins, 200 Iron, 200 Fabric, 50 Gold | 28x16x22                     | 3    | [Townhall Tier 3 Requirements](#townhall-tier-3-requirements) | [About Townhall](#townhall) |


### Requirements for building tier upgrades 

#### Townhall Tier 2 Requirements:
- Tier 1 Townhall
- Population of 20
- Explored 1 dungeon
- Completed 1 NPC quest
- Reached chapter 2 in main questline
- At least tier 1 of the following buildings: 
  - Warehouse
  - Builder's Hub
  - Miner's Hub
  - Forester's Hub
  - Fishing Dock or Bakery and Farm
  - Houses for all of the population

#### Farm Tier 2 Requirements:
- Tier 1 Farm
- Planted at least 3 different crop types
- Population of 15
- 2 Builders available
- At least tier 1 of:
  - Forester's Hub
  - Warehouse
  - House for the farmer

#### Builder's Hub Tier 2 Requirements:
- Tier 1 Builder's Hub
- Constructed at least 3 buildings
- Population of 15
- 100 wood in the Warehouse
- At least tier 1 of:
  - Warehouse
  - Townhall

#### Barracks Tier 2 Requirements:
- Tier 1 Barracks
- Hired 5 guards
- Completed a defense quest
- Population of 25
- At least tier 1 of:
  - Watchtower
  - Warehouse
  - Blacksmith's Forge

#### Bakery Tier 2 Requirements:
- Tier 1 Bakery
- Produced 100 bread
- Population of 15
- At least tier 1 of:
  - Farm
  - Warehouse
  - Houses for workers

#### Fishing Dock Tier 2 Requirements:
- Tier 1 Fishing Dock
- Caught 50 fish
- Population of 10
- Completed a fishing-related quest
- At least tier 1 of:
  - Warehouse
  - Forester's Hub

#### Healing Center Tier 2 Requirements:
- Tier 1 Healing Center
- Healed 10 injured colonists
- Population of 20
- At least tier 1 of:
  - Warehouse
  - Bakery or Farm

#### Logistics Hub Tier 2 Requirements:
- Tier 1 Logistics Hub
- Transported resources 50 times
- Population of 15
- At least tier 1 of:
  - Warehouse
  - Townhall

#### Fabric Artisan Tier 2 Requirements:
- Tier 1 Fabric Artisan
- Produced 100 fabric items
- Population of 15
- At least tier 1 of:
  - Forester's Hub
  - Warehouse
  - Farm

#### Forester's Hub Tier 2 Requirements:
- Tier 1 Forester's Hub
- Harvested 100 wood
- Population of 10
- At least tier 1 of:
  - Warehouse
  - Builder's Hub

#### Miner's Hub Tier 2 Requirements:
- Tier 1 Miner's Hub
- Mined 100 stone or ore
- Population of 10
- At least tier 1 of:
  - Warehouse
  - Blacksmith's Forge

#### Warehouse Tier 2 Requirements:
- Tier 1 Warehouse
- Stored 500 resources
- Population of 15
- At least tier 1 of:
  - Builder's Hub
  - Logistics Hub

#### Blacksmith's Forge Tier 2 Requirements:
- Tier 1 Blacksmith's Forge
- Produced 50 tools or weapons
- Population of 15
- At least tier 1 of:
  - Miner's Hub
  - Warehouse
  - Barracks

#### Tavern Tier 2 Requirements:
- Tier 1 Tavern
- Population of 25
- Served 50 drinks to colonists
- Completed a social quest
- At least tier 1 of:
  - Warehouse
  - Houses for the population

#### School Tier 2 Requirements:
- Tier 1 School
- Educated 5 children
- Population of 20
- Completed a knowledge-related quest
- At least tier 1 of:
  - Townhall
  - Warehouse

#### Market Tier 2 Requirements:
- Tier 1 Market
- Conducted 20 trade transactions
- Population of 25
- Reached chapter 2 in the main questline
- At least tier 1 of:
  - Warehouse
  - Townhall

#### Watchtower Tier 2 Requirements:
- Tier 1 Watchtower
- Successfully defended the colony from 2 attacks
- Population of 15
- At least tier 1 of:
  - Barracks
  - Blacksmith's Forge

#### House Tier 2 Requirements:
- Tier 1 House
- Population of 10
- Upgraded the Townhall to tier 2
- At least tier 1 of:
  - Warehouse
  - Builder's Hub

#### Townhall tier 3 Requirements:
something about the upgrade requirements of townhall tier 3
- Tier 2 Townhall
- Population of 50
- Explored 10 dungeon
- Drink 2 glass of "holy water"

## NPC

### Table of NPCs


### NPC traits 