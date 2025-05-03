# Game Design Document (GDD) for "Blockchainia: CardBrawl"

## 1. Game Overview

### Title
Blockchainia: CardBrawl

### Concept
Blockchainia: CardBrawl is a fully on chain game in which Cards are minted for a complex Collect, Craft, and Compete Card game. Each card features a different Monster, Boss, NPC or Playable Character from the Blockchainia Lore. Blockchainia: CardBrawl is a mini-game to our wider gaming ecosystem. The game mixes and adapts from the mechanics of many well known games, from simple capturing based on value (Dominoes, Triple Triad, Final Fantasy 8), to complex battles (Magic the Gathering, Tetra Master, Final Fantasy 9). We implement a combination of Rank, Genetics, Battle Arrows, and Battle Classes to create a strategic hybrid-deterministic battle system. CardBrawl players compete with their genetically unique Cards to collect Resources and earn Experience. Resources allow players to alter their Card's attributes, as well as Forge new Equipment to each card. Experience allows players to level their cards, potentially increasing certain attributes along the way. Legendary and Mythical Weapons and Armor will grant specific Perks in the battle mathematics.
The winner of each match may "Clone" one perishable copy of a card they have captured from their opponents hand. This Clone will be automatically burned after the completion of the first match it participates in. The game's returns are the following Resources: Ingredients, Materials, and Essence, which must be obtained through winning matches. Crafting together Formulas of these Resources results in more powerful equipment and spells which can be Forged to cards to increase its "Face Values" and genetic attributes.  

### Platform
PC/Mobile

### Genre
Card Game

## 2. Gameplay

### Game Overview
EterraCards combines resource collection and crafting with a complex battle system. Players compete against AI NPCs to mine Resources to enhance their genetically unique cards, driving players to level up to enable higher stakes games. Players Ante-up a small fee to play against AI NPCs who drop valuable Resources upon losing. These resources are needed to engage with the crafting system. Cards can be acquired through minting Card Packs, while Resources in the form of Ingredients, Materials, and Essence must be won through playing Card games through the Ante-up system. 

CardBrawl is played on a four-by-four (4x4) four grid of blank squares where cards will be placed as the game progresses. At the start of each game, up to six squares may be blocked from play, referred to as Grid Lock. Each card has four numbers, one in each Cardinal Direction, referred to as "Face Values". Each individual number is referred to as a Rank, representing its strength in that direction. These numbers range from one to ten, ten being represented by the letter 'A'. Cards can have elemental alignments that affect the game play if there are elemental icons on the game board. 

Before a match, each player selects five Cards from their Deck. A coin-flip decides who begins. The player who wins the coin toss may choose a card to play anywhere on the grid. After the first card is played, the opposing player may play a card on any unoccupied square on the board. The game continues with players' turns alternating.

To win, a majority of the total ten cards played (including up to one card that is not placed on the board if 6 blocks are Grid Locked) must be of the player's card color. To do this, the player must capture cards by placing a card (referred to as the "Active" card) adjacent to an opponent's card (referred to as the "Resting" card) whereupon the the player placing the active card can choose whether to "Face Off" with one of the opponents cards using their "Face Value" Ranks in a cardinal direction, or challenge a card in any of the ordinal directions to a Card Brawl.

During a Face Off the Ranks of the Active and Resting card(s) are compared. If the Resting Card's Rank is resolved to be higher than the Active card's, the Active card will be captured and turned into the opponent's color. If the Active card's Face Value is higher, the Resting card will be captured and changed into the player's color instead. Capturing a Card via Face Off can only occur during that player's turn, and no other opponent card can capture a card during said turn. That is to say, there is only one Face Off per turn. If a grid square contains an elemental marker, the card placed on it may rise or lower in Rank by 1. 

When a player places a card adjacent to an opponents card in a ordinal direction, and the Active card contains a Brawl Arrow in that direction, the player may choose to challenge the Resting card in a Card Brawl. The Brawl Direction is selected by the player placing the Active card. If the Active card contains Brawl Arrows facing the Resting cards in multiple directions, and the player chooses to Card Brawl, multiple Card Brawls will take place towards the final outcome, until all potential cards have been captured. The player placing the Active card chooses the initial direction to take, and continues until all Brawls have completed. In this scenario, cards may be captured and lost multiple times before the final outcome of the turn is reached. 

Cards have different levels. Common level cards have low Face Values, like 1's and 2's and 3's, while Epic and Legendary level cards have 8's, 9's, and A's. Some cards are considered "Mythical". Mythical cards have unique perks derived from their Forged Weapon and Armor. 

### Game Setup
1. **Face Values:** Each card has four numbers, one in each Cardinal Direction, representing its strength in that direction. Each number is referred to as a Rank, evaluated as a Value from one to ten, ten being represented by the letter 'A'. A cards Ranks are permanent, set when the card is minted. 

1. **Genetics:** Each card contains unique Genetics that derive it's initial Face Values, Brawl Arrows, Attributes, and Elemental compatibility. These genetics play a crucial role in the Brawl Mathematics through each Genetic attribute's value, such as setting the Card's Brawl Class and Power attribute. 

1. **Adeptness:** Each card contains a genetic elemental compatibility. The adeptness attribute for each element can be increased through placing the card on an grid square containing an elemental symbol during a match. Greater adeptness increases the base compatibility for each element.

1. **Card Ranks:** Cards have four Ranks which comprise it's Face Values, one in each Cardinal direction. 

     **Rank Distribution for Season 1**
     
     Each percentage is the chance, when minted, of each of the four Ranks falling into one of the ranges. Ranks do not change during a rarity change. 
     
     | Rank Range | Common | Uncommon| Rare | Epic | Legendary |
     |------------|--------|---------|------|------|-----------|
     | 0-2        | 40%    | 30%     | 20%  | 10%  | 10%       |
     | 3-5        | 35%    | 30%     | 35%  | 35%  | 30%       |
     | 6-8        | 25%    | 40%     | 35%  | 40%  | 35%       |
     | 9-A        | 0%     | 0%      | 10%  | 15%  | 25%       |

1. **Brawl Arrows:** Each Card contains up to four arrows, one possible in each of the four ordinal directions. Cards may start a Card Brawl when one of the Brawl Arrows faces an adjacent opponents card. 

1. **Levelling and Forging:** A card can be leveled up to level 100 through gaining experience when used in game. As a card levels, it will change in rarity on a unique schedule set by its DNA. Epic cards may have one piece of equipment Forged to them. Legendary cards may have two pieces of equipment Forged to them. When forging, the genetics of a card change according to the table below. 

     **Genetic Distribution for Season 1**

     When minted, there is a 1% chance of minting a card with an A Brawl class and 4% chance for a D Brawl Class. There is a 50% chance of minting an P Brawl Class, and 45% chance for an S Brawl Class. While Leveling, a cards genetic attributes will change according to its Level Graph. When changing rarity, the Card's genetics change to closer fit the following population distribution: 

     | Hex Range | Common | Uncommon | Rare | Epic | Legendary |
     |-----------|--------|----------|------|------|-----------|
     | 0-3       | 35%    | 25%      | 15%  | 12%  | 12%       |
     | 4-7       | 45%    | 40%      | 40%  | 28%  | 18%       |
     | 8-B       | 15%    | 30%      | 40%  | 50%  | 35%       |
     | C-F       | 5%     | 5%       | 5%   | 20%  | 35%       |

1. **Level Graph:** A Graph that shows genetic and rarity changes possible as a card progresses through various Levels.

1. **Card Levels:** As are used in Brawls, they earn experience towards its Level. Levels range from 1-100. As a card levels, its Brawl Class may change . 

1. **Deck Construction:** Players construct a deck of cards from cards they own, or may borrow up to 5 cards, Common through Rare, from a pool of cards made available for each game. The cost of borrowing cards is included in the "ante-up" fee. Players are unable to keep their borrowed cards, although their Opponent may Clone any of the captured borrowed Cards upon winning a match. 

1. **Deck Limits:** Players may only hold 10 instances of a Card for each unique monster, pet, character, or boss per Wallet. This total includes Cloned cards. If there is no room left in a player's wallet for a Cloned card, they must first burn one card of that instance in their deck to collect it. A Wallet Manager will allow the storing of multiple Wallets, akin to a "save file". Players are free to trade their cards to other Wallets through over-the-counter transactions.
  
1. **Game Board:** Blockchainia: Cards is played on a 4x4 grid board. Each square on the grid can hold one card. 

1. **Grid Lock:** As a game starts, up to six squares may be blocked off, which prevents either player from placing a card on that board square.  

1. **Face Off:** When two cards are placed adjacent to each other and challenge each other in a cardinal direction, a Face Off ensues. When Cards Face Off, their adjacent Ranks are compared. The Card with the lower Rank will be captured. 

1. **Genetics** Each card has a genetic value that influence which card will win a Card Brawl. The Brawl Class, Power, Physical Defense, and Magical Defense are shown on the face of each card. These values can be increased through properly forging weapons, armor, and accessories to each card. Genetics give each card a unique base attributes and elemental compatibility. 

1. **Card Brawls** When two cards are placed adjacent to each other and challenge each other in an ordinal direction a Card Brawl ensues. The Card Brawl mathematics are described below. A single card placement may result in multiple card brawls. The player who places the card decides which brawl occurs first. 

1. **Equipment and Spells** The primary objective of the card game is to craft Legendary Equipment. Card types are uncommon, common, rare, epic, and legendary. Only Legendary Equipment can be used to upgrade a Card to Mythical status. Mythical cards can be obtained by Forging Legendary Spells and Equipment to a card. 

1.  **Collection and Crafting:** The basic resources of the game are ingredients, materials, and elemental essence of magic.  Players create spells and Equipment via the Resources gathered by winning games against AI NPCs. 
    - **Alchemy, Synthesis, and Forging:** Visit the NPC-owned Alchemy and Synthesis shops to craft resources into Spells and Equipment. Equipment can be Forged to a card to alter the cards Face Values and Genetics to upgrade cards to Legendary and Mythical status. 
    - **Card Brawls:** It is possible to increase a cards Brawl Class from P or M to D or A through engaging the card in Card Brawls. 
    - **Vending:** Visit the Vending Machine to mint new card packs and view special deals. 
    - **Elemental Advantage:** Adds strategic depth with elemental bonuses during a Card Brawl.
    - **Perks:** Introduce conditional skill activation for dynamic gameplay. Perks are derived from Legendary and Mythical Weapons

1. **Resource Types:**
    - **Ingredients:** Used to craft and upgrade Equipment and Spells. 
    - **Materials:** Used to craft and upgrade Equipment and Spells.  
    - **Essence:** Used to craft and upgrade Equipment and Spells. 

1. **Starting Hands:** Players draw a starting hand of cards from their deck. If the player does not own enough cards to fill a hand, they can choose up to five basic cards through the "Ante-Up" system, essentially renting the remaining cards needed to start the game.

1. **Coin Flip:** Each player has five cards, neither knowing the other player's hand. A coin-flip decides which of the two players shall begin.
 
1. **Cloning Cards** The winner of each match is allowed to Clone one perishable copy of a card of their opponents selected from the pool of cards they captured throughout the match. This card is burned after it participates in a match as an Active card. 

### A card is played

Once the game is set up, the starting player may play their first card at any unoccupied grid square on the board. After the first card is played, the opposition may play a card, and the game continues with player turns alternating in this fashion.

### Neutral card play

If a card is placed next to another card in a cardinal or ordinal direction, they may interact. Should a placement happen where none of the cards are adjacently in the cardinal or ordinal directions there is no interaction. This is a neutral card play.

### Card capture

An Active card may be used to engage in a Face Off or Card Battle, but not both. The card that loses the Face Off, or any card that loses a Card Battle is Captured. 

#### Card Brawls

##### Genetic Attributes: 

Every card has eight genetic attributes. Four are comprised of the face values, which are also the cards elemental strength attributes. Printed on each card are also four Genetic Attributes. The first is a Brawl Class followed by is power, physical defense, and magical defense. An example card may have the Attribute values: P-3-A-0. Each Genetic Attribute relates to the card's competitive strength. The first value (P in the example) is always an alphabetical value from the set [P,S,D,A], while the next three genetics increase on a hexadecimal range, meaning they can range from 0-9, then through letters A-F.

   - The first value is the Brawl Class of the card. (P above)
   - The second value is for the power genetic of the card. (3 above)
   - The third value is for the physical defense genetic of the card. (A above)
   - The fourth value is for the magical defense genetic of the card. (0 above)

The power and defense genetics represents a range of possible attack or defense points. 0 will take values from 0-15, while F will take values from 240-255. 

The card genetics are used in the following situations:

The first two values are used for the Active card.
The last two values are used for the Resting card.

#### Power genetic

The first value on the card is the power attribute. This is the card's offensive value. How this value is used is described in the Battle Mathematics. 

**Brawl Class genetic:**
The second value on the card is the brawl class attribute. This value is not based on the hexadecimal scale like its other genetics, but instead is one of four classes. This genetic is represented by the letters P, S, D, and A. The card's brawl class determines how the values are assessed in card brawls.

- P is a Physical brawl class
- S is a Spell brawl class
- D is a Defensive brawl class
- A is an Ace brawl class

The brawl class affects which attribute the Active card attacks. P will attack the Physical Defense attribute, while S will attack the Magical Defense attribute. The other two are genetically rarer, but can be earned by Leveling a card. D attacks the lower of the two defenses and A attacks the lowest value on the card. It is possible to increase a Card's Brawl Class at certain levels to D or A, but only if it contains certain genetics and was leveled at the appropriate time.  

#### Physical Brawl
If the challenging card has a brawl class genetic of P (Physical), the power value of this card challenges the physical defense of the Resting card. 

#### Spell Brawl

If the challenging card has a brawl class genetic of S (Spell), the power value of this card challenges the magical defense of the Resting card. 

#### Defensive Struggle

If the challenging card has a brawl class genetic of D (Defense), the power value of this card challenges the weaker of the two defense genetics of the Resting card.

#### Ace Brawl

If the challenging card has a brawl class genetic of A (Ace), the strongest of all three values on this card challenges the weakest of all three values of the Resting card.

#### Battle Statistics 
Stat ranges are determined by right shifting the the binary representation of the hex value by three bits and randomly assigning a value for the additional three bits. The range for the hexadecimal values are shown below. 
| Hexadecimal   | Range   |
|:--------------|:--------|
| 0             | 0-7     |
| 1             | 8-15    |
| 2             | 16-23   |
| 3             | 24-31   |
| 4             | 32-39   |
| 5             | 40-47   |
| 6             | 48-55   |
| 7             | 56-63   |
| 8             | 64-71   |
| 9             | 72-79   |
| A             | 80-87   |
| B             | 88-95   |
| C             | 96-103  |
| D             | 104-111 |
| E             | 112-119 |
| F             | 120-127 |


#### Brawl Mathematics
     Relevant Card Attributes:
     
     Element: Each card has an elemental attribute (e.g., Fire, Water, Earth, Air, or Void). This is determined by its strongest elemental genetic, but also considers the card adeptness with each element. 
     Perk: Each card may have a special skill that can be activated under certain conditions.
     Brawl Class: The Brawl Class of the Active card determines which defense stat of the Resting card is attacked during a brawl. In the following example, the Brawl Class of the Active card is Physical, and the Physical Defense stat is being attacked. 

     Battle Phases

     Phase 1: Attribute and Range Determination
     
     Power and Defense Values:

     The challenging card's power value is randomly chosen within its stat range.
     The defending card's defense value is randomly chosen within its stat range, based on the battle class of the Active card(physical or magical). 

     Example:
     Card A: Power = 41 (stat 5 = range 40-47, final Power: 41)
     Card B: Defense = 21 (stat 2 = range 16-23, final Defense: 21)
     Elemental Advantage:

     If the challenging card's element has an advantage over the defending card's element, add a bonus to the challenging card's power. If the challenging card's element is weak to the defending cards element, reduce the challenging cards power. 
     Example:
     Card A (Earth) vs. Card B (Fire): Earth has an "Strong" effect on Fire.
     Card A: Power = 41 + 10 (bonus) = 51

     Phase 2: Perk Activation 

     Perk Activation:

     Each card can activate its weapon and armor [Perk] if a specific condition is met.
     Example Perks:
     "Weapon": Increase power by 20 if the random attack score is above 50.
     "Armor": Increase magical defense by 10 and physical defense by 15 if defense score is below 25.
     Score Calculation:

     Apply perks if conditions are met:
     If Card A's [Perk] activates (since 51 > 50), new attack score = 51 + 20 = 71
     If Card B's [Perk] activates (since 3 < 10), new defense score = 3 + 15 = 18 
     
     Phase 3: Final Score and Outcome Determination

     Randomly select additional attack and defense scores within the Phase 2 power and defense values.
     Example:
     Card A: Attack score = Random(0, 71) = 31
     Card B: Defense score = Random(0, 18) = 10

     Score Adjustment:

     Subtract the scores from Phase 2 from the initial stat values in Phase 1.
     Example:
     Card A: 
     71 − 31 = 40
     Card B: 
     23 − 0 = 23
     Outcome Determination:

     Compare the final scores to determine the winner.
     The card with the highest difference wins the battle.
     Example:
     Card A: 40
     Card B: 23
     Card A wins the battle.

     Final Scores: Final scores reflect the impact of skills and elemental bonuses, determining the battle outcome.

## Design Considerations
- **Strategic Placement:** Players must consider directional coverage for card placement on multiple fronts, equipped items, and elemental effects.
  
- **Balance:** Ensure cards contain a balance of Face Values in each direction. With a breadth of considerations needed to create the optimal deck for success, finding the proper balance to work up the Leaderboard and receive a tournament invite.

- **Seasonal Tournaments:** At the end of each season, the top 64 players of the Leaderboard will be invited to play through a Tournament Bracket. 
  
- **Variety:** Include a wide range of cards to encourage diverse strategies. Each card contains a wide range of attributes that make it unique. 
  
- **Customization:** Allow players to customize their decks of cards through crafting to suit their play style.

## Elemental Effectiveness Table
Lore Note: The Void type is derived from subtypes: Light, Dark, Moon, and Nature. 

| **Element \ Target** | Earth  | Water | Fire  | Wind  | Void    |
|----------------------|--------|-------|-------|-------|---------|
| **Earth**            | Normal | Weak  | Strong| Weak  | Normal  |
| **Water**            | Strong | Normal| Weak  | Strong| Weak    |
| **Fire**             | Normal | Strong| Normal| Weak  | Weak    |
| **Wind**             | Strong | Weak  | Strong| Normal| Weak    |
| **Void**             | Strong | Strong| Normal| Strong| Normal  |

## Resource list

### Ingredients
Lore note: The most common materials, like Leather, are frequently dropped by NPCs when a player loses. 

Strategy Note: Some ingredients are purposefully unused in the first version of the Crafting implementation. This is intended to drive engagement from Early Access Users on future Formulas for Spells, Materials, and Equipment. It is also inherent to the lore, storyline, and marketing strategy, as the Alchemists are aware of artifacts containing Symbols for Ingredients that they have no known Formulas for. They compete to rediscover these "Lost Spells". 

| **Ingredient**        | **Description**                                      |
|-----------------------|------------------------------------------------------|
| Wax                   | Used for sealing and waterproofing                   |
| Water                 | Essential liquid, often used as a solvent            |
| Vinegar               | Acidic liquid used in various concoctions            |
| Root                  | Plant-based ingredient                               |
| Oil                   | Used for lubrication and combustion                  |
| Mushroom              | Fungal ingredient with various effects               |
| Limestone             | Calcium-rich mineral used in various mixtures        |
| Iron                  | Metal used for strengthening concoctions             |
| Gunpowder             | Explosive mixture used for powerful effects          |
| Ethanol               | Alcohol used as a solvent and for combustion         |
| Dry Ice               | Solid carbon dioxide used for freezing effects       |
| Clay                  | Earthy material used for crafting and grounding      |
| Bone                  | Used for necromancy and strengthening spells         |
| Ash                   | Remnants of combustion, used in various spells       |
| Mythril               | Rare metal used for crafting powerful items          |
| Phoenix Dust          | Revives the fallen, symbolizes rebirth               |
| Dragon Fang           | Rare and powerful, used for high-level concoctions   |
| Ether                 | Restores magical energy                              |
| Dreamstone            | Rare stone, used for crafting powerful artifacts     |
| Luminite              | Luminescent material, used for light-based items     |

### Essences

| **Essence**           | **Description**                                   |
|-----------------------|---------------------------------------------------|
| Aquanix               | Water spirit, grants water-based magic            |
| Terralon              | Earth spirit, grants earth-based magic            |
| Aerion                | Wind spirit, grants wind-based magic              |
| Pyron                 | Fire spirit, grants fire-based magic              |
| Nocturne              | Void-Darkness spirit, grants dark-based magic     |
| Radiance              | Void-Light spirit, grants light-based magic       |
| Selene                | Void-Moon spirit, grants lunar-based magic        |
| Verdant               | Void-Nature spirit, grants nature-based magic     |

### Materials

| **Material**          | **Description**                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------|
| Leather               | Durable hides, heirlooms symbolizing ancestral resilience and victories         |
| Iron                  | A sturdy metal used for basic weaponry and armor                                              |
| Adamantine            | A rare and nearly indestructible metal |
| Obsidian              | A brittle volcanic glass that can be sharpened to a razor edge      |
| Dragonbone            | Incredibly strong bones from ancient dragons imbued with magical energy                             |
| Crystal               | Mystical crystals that can channel magical energies                   |
| Darkwood              | A rare and sturdy wood with dark coloration                           |
| Orichalcum            | A mythical metal with a golden hue, known for its durability and enchantment capabilities               |
| Moonstone             | A pale, luminescent stone with magical properties   |
| Dwarven Steel         | Superior steel known for its exceptional quality and strength                 |
| Elven Silver          | A light and strong metal with magical properties                        |
| Froststeel            | Steel imbued with the essence of ice                         |
| Bloodstone            | A dark, crimson stone that can enhance the power of blood magic                              |
| Star Metal            | Metal forged from meteorite fragments, possessing unique otherworldly properties                        |
| Voidsteel             | A dark, shadowy metal that absorbs light              |
| Living Wood           | Enchanted wood that retains the essence of life |
| Thunderstone          | A rare stone that can store electrical energy |
| Phoenix Feather       | Feathers from the mythical Phoenix |
| Shadowglass           | A dark reflective glass that can absorb and manipulate shadows |

## Crafting through Synthesis and Alchemy to Create Legendary Weapons

### Synthesis Formulas for Equipment
These items may be Forged to a card to add Perks to the card. These Perks activate in the Battle Mathematics.  

### Common Weapons

| **Item**            | **Formula**           | **Description**                                                 |
|---------------------|-----------------------|-----------------------------------------------------------------|
| Iron Sword          | Iron + Darkwood        | A simple yet reliable sword.                                    |
| Iron Dagger         | Iron + Root          | A sturdy dagger with enhanced sharpness.                        |
| Wooden Bow          | Darkwood + Oil     | A basic bow crafted from darkwood.                              |
| Iron Hammer         | Iron + Clay            | A heavy hammer made from iron.                                  |
| Iron Spear          | Iron + Root          | A spear with a strong steel tip.                                |

### Common Armor

| **Item**            | **Formula**           | **Description**                                                 |
|---------------------|-----------------------|-----------------------------------------------------------------|
| Steel Armor         | Iron + Leather        | Basic armor made from iron and leather.                         |
| Steel Helmet        | Dwarven Steel + Leather      | A helmet made from durable steel.                               |
| Leather Boots       | Leather + Oil      | Simple boots made from treated leather.                         |
| Wooden Shield       | Darkwood + Iron       | A basic shield made from darkwood reinforced with iron.         |
| Iron Gauntlets      | Iron + Leather        | Protective gauntlets made from iron and leather.                |

### Uncommon Weapons

| **Item**            | **Formula**           | **Description**                                                 |
|---------------------|-----------------------|-----------------------------------------------------------------|
| Bronze Sword        | Bronze + Darkwood      | A sword made from bronze, lighter than iron.                    |
| Silver Dagger       | Silver + Root         | A sharp dagger made from silver, effective against certain creatures. |
| Composite Bow       | Darkwood + Dwarven Steel      | A stronger bow made with darkwood and steel.                    |
| Warhammer           | Dwarven Steel + Clay           | A heavy warhammer for devastating blows.                        |
| Iron Pike           | Iron + Root           | A long pike for keeping enemies at a distance.                  |

### Uncommon Armor

| **Item**            | **Formula**           | **Description**                                                 |
|---------------------|-----------------------|-----------------------------------------------------------------|
| Bronze Armor        | Bronze + Leather      | Armor made from bronze and leather.                             |
| Silver Helmet       | Silver + Oil       | A helmet made from shiny silver.                                |
| Sturdy Boots        | Leather + Dwarven Steel       | Boots reinforced with steel for extra protection.               |
| Bronze Shield       | Bronze + Iron         | A shield made from bronze and iron.                             |
| Silver Gauntlets    | Silver + Leather      | Gauntlets made from silver and leather.                         |

### Rare Weapons

| **Item**            | **Formula**                           | **Description**                                                 |
|---------------------|---------------------------------------|-----------------------------------------------------------------|
| Fire Sword          | Pyron + Iron + Darkwood                | A sword imbued with the power of fire, dealing extra fire damage. |
| Ice Dagger          | Aquanix + Mithril + Dry Ice           | A dagger that freezes enemies upon contact.                     |
| Lightning Axe       | Aerion + Dwarven Steel + Thunderstone         | An axe that crackles with electricity, stunning enemies.        |
| Earth Hammer        | Terralon + Iron + Clay                 | A hammer that causes small earthquakes on impact.               |
| Shadow Blade        | Nocturne + Voidsteel + Shadowglass    | A blade that deals additional darkness damage.                  |
| Light Mace          | Radiance + Mithril + Luminite         | A mace that emits a blinding light, damaging and blinding enemies. |
| Moon Spear          | Selene + Orichalcum + Moonstone       | A spear that glows with lunar energy, increasing precision and power. |
| Nature Bow          | Verdant + Darkwood + Root             | A bow that enhances arrows with nature's power, causing additional damage. |

### Rare Armor

| **Item**            | **Formula**                           | **Description**                                                 |
|---------------------|---------------------------------------|-----------------------------------------------------------------|
| Elemental Shield    | Aquanix + Pyron + Iron                | A shield that provides resistance to elemental damage.          |
| Stealth Suit        | Oil + Clay + Nocturne              | Armor that enhances the wearer's stealth abilities.             |
| Frost Gauntlets     | Froststeel + Silver + Ether           | Gauntlets that grant the wearer control over ice and cold.      |
| Nature Boots        | Verdant + Living Wood + Leather       | Boots that enhance the wearer's connection to nature, boosting speed and agility. |

### Epic Weapons

| **Item**            | **Formula**                           | **Description**

### Epic Weapons

| **Item**            | **Formula**                           | **Description**                                                 |
|---------------------|---------------------------------------|-----------------------------------------------------------------|
| Firearm (Pistol)    | Iron + Oil + Gunpowder             | A basic firearm that is reliable and effective at short range.  |
| Firearm (Rifle)     | Dwarven Steel + Luminite + Gunpowder          | A rifle with enhanced aiming capabilities for long-range attacks. |
| Crossbow            | Darkwood + Iron + Oil              | A crossbow that fires bolts with precision and power.           |
| Elemental Crossbow  | Crystal + Darkwood + Ether            | A crossbow that can fire elemental bolts.                       |
| Aqua Trident        | Aquanix + Dwarven Steel + Crystal             | A trident that controls water and deals heavy water damage.     |
| Lightning Blade     | Aerion + Silver + Thunderstone        | A blade that strikes with the power of lightning.               |
| Earth Axe           | Terralon + Iron + Dragonbone          | An axe that can split the earth and create tremors.             |
| Flame Sword         | Pyron + Star Metal + Phoenix Feather  | A sword that deals immense fire damage and burns enemies.       |

### Epic Armor

| **Item**            | **Formula**                           | **Description**                                                 |
|---------------------|---------------------------------------|-----------------------------------------------------------------|
| Regenerative Armor  | Phoenix Feather + Mithril + Bone      | Armor that grants the wearer regenerative abilities.            |
| Scale Armor         | Dragonbone + Dwarven Steel + Crystal  | Armor made from dragon scales, offering unmatched protection.   |
| Invisibility Cloak  | Ether + Moonstone + Elven Silver      | A cloak that provides invisibility and enhances magical abilities. |
| Earth Gauntlets     | Terralon + Iron + Stone               | Gauntlets that grant the wearer increased strength and control over earth. |
| Flame Armor         | Pyron + Dwarven Steel + Luminite              | Armor that protects the wearer from fire and increases fire magic potency. |
| Ice Bow             | Aquanix + Mithril + Froststeel        | A bow that shoots arrows of ice, freezing targets on impact.    |
| Nature Cloak        | Verdant + Living Wood + Root          | A cloak that allows the wearer to blend seamlessly with nature. |

### Legendary Weapons

| **Item**            | **Formula**                                                    | **Description**                                                 |
|---------------------|----------------------------------------------------------------|-----------------------------------------------------------------|
| Thunder Hammer      | Aerion + Dwarven Steel + Thunderstone + Sapphire + Lightning Axe| A hammer that can summon thunderstorms on impact.               |
| Shadow Dagger       | Nocturne + Voidsteel + Shadowglass + Onyx + Shadow Blade       | A dagger that deals critical damage from the shadows.           |
| Lunar Staff         | Selene + Crystal + Moonstone + Opal + Moon Spear               | A staff that channels lunar energy for powerful spells.         |
| Phoenix Blade       | Radiance + Star Metal + Phoenix Feather + Ruby + Fire Sword    | A blade that can resurrect the wielder and deal immense fire damage. |
| Void Sword          | Nocturne + Voidsteel + Ether + Amethyst + Shadow Blade         | A sword that drains the life from enemies.                      |
| Frost Bow           | Aquanix + Star Metal + Froststeel + Diamond + Ice Dagger       | A bow that unleashes freezing arrows with every shot.           |
| Nature Staff        | Verdant + Crystal + Living Wood + Emerald + Nature Bow         | A staff that channels the power of nature, enhancing healing and growth. |
| Light Sword         | Radiance + Mithril + Luminite + Topaz + Light Mace             | A sword that emits blinding light, dealing significant damage to dark creatures. |
| Blazing Sword       | Pyron + Iron + Mithril + Ruby + Fire Sword                     | A sword imbued with the power of fire, dealing extra fire damage. |
| Sniper Rifle        | Iron + Oil + Luminite + Sapphire + Firearm (Rifle)          | A high-precision firearm with enhanced aiming capabilities.     |
| Energy Sword        | Luminite + Mithril + Oil + Diamond + Fire Sword             | A melee weapon with a blade made of pure energy.                |
| Grenade Launcher    | Gunpowder + Iron + Oil + Topaz + Firearm (Pistol)           | A firearm that launches explosive grenades.                     |
| Plasma Rifle        | Luminite + Iron + Ethanol + Emerald + Firearm (Rifle)          | A futuristic rifle that shoots plasma bolts.                    |
| Thunder Blade       | Thunderstone + Iron + Etherstone + Sapphire + Lightning Axe    | A sword that crackles with electricity, stunning foes.          |
| Mystic Staff        | Crystal + Elven Silver + Moonstone + Opal + Elemental Crossbow | A staff that enhances magical abilities, channeling powerful spells. |
| Celestial Mace      | Star Metal + Adamantine + Bloodstone + Ruby + Light Mace       | A mace that glows with celestial light, smiting enemies.        |

### Legendary Armor

| **Item**            | **Formula**                                                    | **Description**                                                 |
|---------------------|----------------------------------------------------------------|-----------------------------------------------------------------|
| Cosmic Helm         | Star Metal + Orichalcum + Mithril + Diamond + Invisibility Cloak| A helmet that grants the wearer cosmic awareness and protection. |
| Phoenix Armor       | Phoenix Feather + Star Metal + Mithril + Ruby + Regenerative Armor| Armor that grants the wearer the power of resurrection.         |
| Light Shield        | Radiance + Orichalcum + Luminite + Topaz + Elemental Shield    | A shield that emits blinding light, repelling enemies.          |
| Moon Gauntlets      | Selene + Silver + Moonstone + Opal + Frost Gauntlets           | Gauntlets that increase the wearer's strength during the night. |
| Frost Gauntlets     | Froststeel + Silver + Ether + Sapphire + Frost Gauntlets       | Gauntlets that grant the wearer control over ice and cold.      |
| Earth Armor         | Terralon + Dragonbone + Dwarven Steel + Emerald + Scale Armor  | Armor that provides unparalleled defense and strength.          |
| Shadow Cloak        | Nocturne + Voidsteel + Ether + Onyx + Stealth Suit             | A cloak that makes the wearer invisible in the shadows.         |
| Nature Boots        | Verdant + Living Wood + Leather + Emerald + Nature Boots       | Boots that enhance the wearer's connection to nature, boosting speed and agility. |
| Star Metal Helm     | Star Metal + Orichalcum + Mithril + Diamond + Cosmic Helm      | A helmet that grants the wearer cosmic awareness and protection. |
| Ethereal Cloak      | Etherstone + Moonstone + Elven Silver + Opal + Invisibility Cloak| A cloak that provides invisibility and enhances magical abilities. |
| Phoenix Cape| Phoenix Feather + Living Wood + Bloodstone + Ruby + Regenerative Armor| A cape that provides regeneration and fiery protection.          |
| Moonlight Robe      | Selene + Silk + Moonstone + Opal + Stealth Suit                | A robe that grants the wearer enhanced magical abilities and stealth. |
| Flame Cloak         | Pyron + Silk + Gold + Ruby + Flame Armor                       | A cloak that grants immunity to fire and increases fire magic potency. |
| Storm Helm          | Thunderstone + Iron + Luminite + Sapphire + Lightning Blade    | A helmet that channels the power of storms, protecting the wearer. |

### Synthesizing Precious Stones
Precious stones can be used to craft Legendary Weapons to Forge to cards . They can also be used for the summoning of powerful allies in the Blockchainia: OpenWorlds and Blockchainia: CryptoBrawl. 

| **Precious Stone**    | **Formula**                         | **Name**       | **Description**                                                       |
|-----------------------|-------------------------------------|----------------|-----------------------------------------------------------------------|
| Aqua Gem              | Aquanix + Crystal + Moonstone       | Poseidon       | Summons Poseidon, god of the sea, to command water and marine creatures. |
| Earth Crystal           | Terralon + Dragonbone + Orichalcum  | Gaia           | Summons Gaia, the Earth Mother, to protect and nurture the land.       |
| Flame Ruby            | Pyron + Obsidian + Bloodstone       | Hephaestus     | Summons Hephaestus, god of fire and forge, to wield flames and craft.  |
| Shadow Onyx           | Nocturne + Voidsteel + Shadowglass Shard | Hades       | Summons Hades, lord of the underworld, to command darkness and the dead. |
| Light Diamond         | Radiance + Luminite + Elven Silver  | Apollo         | Summons Apollo, god of light and music, to heal and inspire.           |
| Lunar Pearl           | Selene + Moonstone + Froststeel     | Artemis        | Summons Artemis, goddess of the moon and hunt, to guide and protect.   |
| Nature Emerald        | Verdant + Living Wood Heart + Dwarven Steel | Cernunnos | Summons Cernunnos, the horned god, to oversee nature and wildlife.     |
| Volcanic Garnet       | Pyron + Terralon + Adamantine       | Surtr          | Summons Surtr, the fire giant, to unleash volcanic fury.               |
| Storm Topaz           | Aerion + Thunderstone + Dwarven Steel       | Thor           | Summons Thor, god of thunder, to wield his mighty hammer and storm.    |
| Mystic Amethyst       | Radiance + Etherstone + Crystal     | Amaterasu      | Summons Amaterasu, goddess of the sun, to illuminate and purify.       |
| Warrior's Bloodstone  | Pyron + Dragonbone + Bloodstone     | Ares           | Summons Ares, god of war, to lead in battle and inspire warriors.      |
| Ocean's Heart         | Aquanix + Sapphire + Luminite       | Ryujin         | Summons Ryujin, the dragon god of the sea, to control tides and marine life. |
| Frost Crystal         | Aquanix + Froststeel + Mithril      | Yuki-Onna      | Summons Yuki-Onna, the snow woman, to command ice and cold.            |
| Chaos Ruby            | Nocturne + Bloodstone + Voidsteel   | Loki           | Summons Loki, the trickster god, to cause chaos and deceive enemies.   |
| Celestial Moonstone   | Selene + Star Metal + Moonstone     | Selene         | Summons Selene, the moon goddess, to bless with lunar magic and protection. |

### Alchemy Formulas
#### Alchemy Formulas for Consumable Spells

| **Alchemy Formula**     | **Spell Name**      | **Description**                                                         | **Power** |
|-------------------------|---------------------|-------------------------------------------------------------------------|-----------|
| Terralon + Terralon     | Rockslide           | A massive slide of rocks that crushes enemies.                          | 2         |
| Terralon + Aquanix      | Mudslide            | A torrent of mud that engulfs and slows enemies.                        | 1         |
| Terralon + Pyron        | Lava Burst          | Erupts molten rock that burns and traps enemies.                        | 1         |
| Terralon + Aerion       | Sandstorm           | Whips up a fierce sandstorm that blinds and slices through enemies.     | 1         |
| Terralon + Nocturne     | Voidquake           | A devastating earthquake infused with void energy that disrupts reality. | 2         |
| Aquanix + Aquanix       | Tsunami             | A gigantic wave that washes away everything in its path.                | 2         |
| Aquanix + Pyron         | Steam Blast         | A burst of scalding steam that burns and blinds enemies.                | 1         |
| Aquanix + Aerion        | Hurricane           | A powerful hurricane that drenches and blows away everything in its path.| 1         |
| Aquanix + Nocturne      | Abyssal Tide        | Summons a tide from the abyss that pulls enemies into the void.         | 2         |
| Pyron + Pyron           | Inferno             | An intense blaze that engulfs and incinerates everything.               | 2         |
| Pyron + Aerion          | Flame Cyclone       | A massive cyclone of flames that engulfs and burns everything it touches.| 1         |
| Pyron + Nocturne        | Hellfire            | Summons flames from the void that burn with unholy intensity.           | 2         |
| Aerion + Aerion         | Tornado             | A powerful tornado that tears through everything in its path.           | 2         |
| Aerion + Nocturne       | Ethereal Breeze     | A soothing breeze from the void that heals allies and confounds enemies.| 2         |
| Nocturne + Nocturne     | Annihilation        | A destructive force that obliterates everything it touches.             | 3         |
| Radiance + Radiance     | Divine Light        | Summons a blinding light that purifies and damages all enemies.         | 2         |
| Radiance + Nocturne     | Eclipse             | A combination of light and darkness that causes massive destruction.    | 2         |
| Nocturne + Nocturne     | Shadow Veil         | Envelops the battlefield in darkness, blinding all enemies.             | 1         |
| Selene + Selene         | Lunar Blast         | A powerful beam of lunar energy that devastates enemies.                | 2         |
| Selene + Nocturne       | Nightfall           | Calls down the power of the moon and darkness to crush enemies.         | 2         |
| Verdant + Verdant       | Nature's Wrath      | Summons the fury of nature to entangle and damage enemies.              | 2         |
| Verdant + Aquanix       | Vine Whip           | Conjures water-infused vines that bind and drown enemies.               | 1         |
| Verdant + Pyron         | Wildfire            | Unleashes a wildfire that spreads and incinerates everything.           | 1         |
| Verdant + Aerion        | Leaf Storm          | Summons a storm of razor-sharp leaves that cut through enemies.         | 1         |
| Verdant + Nocturne      | Shadow Grove        | Creates a grove of shadowy trees that ensnare and drain life from enemies.| 2         |


### Alchemy Formulas for Legendary Spells 
Each Legendary spell can progress from its base [Element], to [Element]+, to its [Legendary Spell]. For example, the Earth elemental spell is acquired at level 1. It may to Earth+ between levels 25 and 50, and between 75 and 85 to Gaia's Wrath. Forging a Spell requires the following formula, plus an additional mix of Consumable spells and Essence. All of these will be considered when Forging the Spells unique Genetics. 

| **Element** | **Legendary Spell**  | **Formula**                                           | **Description**                                                                 |
|-------------|----------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|
| Earth       | Gaia's Wrath         | Earth Crystal + Earth Hammer                            | Unleashes the fury of the Earth, causing massive earthquakes and upheaval.      |
| Water       | Poseidon's Fury      | Aqua Gem + Ocean's Heart + Glacial Spear              | Summons a colossal tidal wave and torrential rain to devastate enemies.         |
| Fire        | Inferno Blaze        | Flame Ruby + Inferno Axe + Phoenix Cape       | Engulfs the battlefield in intense flames, incinerating everything in sight.    |
| Wind        | Tempest of the Skies | Ocean Pendant + Thunder Blade + Gale Whip              | Conjures a massive storm, with powerful winds and lightning strikes.            |
| Light       | Radiant Judgment     | Light Diamond + Ring of Radiance + Celestial Mace     | Calls down beams of divine light to smite and purify the land.                  |
| Darkness    | Cataclysm     | Shadow Onyx + Shadow Dagger + Void Ring               | Summons a void of darkness, engulfing enemies and disrupting their senses.      |
| Moon        | Lunar Eclipse        | Lunar Pearl + Moonlight Robe + Ethereal Cloak         | Brings forth an eclipse, casting a shadow over the battlefield and empowering allies. |
| Nature      | Verdant Rebirth      | Nature Emerald + Venom Dagger + Nature Boots          | Revitalizes the land, causing plants to grow rapidly and heal allies.           |

## Forging
Equipment and Spells can be used to increase a Cards statistics. Forging Weapons, Armor, or Accessories to a card will essentially burn the item, embedding it to the card of choice, altering the cards genetics and the images shown on the face of the card. As all of these items will have utility in future games, players are encouraged to earn as multiple copies of each throughout the season, and to not Forge every item to a card. 

### Game Progression
- **Match-Based Play:** Players enter matches, competing against both AI and other players. To play against AI, players must "Ante-up". 
- **The Iron Price** Upon match end, the winning player may take a perishable copy of one card from the opponents deck. 
- **Crafting and Upgrading:** Post-match, players use collected essence and materials to craft and upgrade spells, weapons, and pets.

- **Items, Relics, and Artifacts:** Collect in game items of various utility in future games. 

## 3. Story and Setting

### World
Blockchainia is a virtual on-chain realm where the separation of magic and technology has been obfuscated from the public by a shadowy organization. Ancient ruins and mines scatter the landscape, providing rich sources of elemental essence and raw materials. NPC characters inhabit the land, littered with monuments, fountains, as well as various spiritual relics left from their ancestors. Most of these relics reside in the hands of families belonging to the Noble class. Player interactions will reveal a deep, unspoken culture, as the lowest class NPC's in Blockchainia also love to play video games, not knowing they exist explicitly inside of one. Paying close attention to NPC interactions reveals clues to the history of this strange world, guiding the player towards easter eggs holding the secrets of the beginning of this unique realm, ultimately leading each player on a unique journey to understand the prophecy behind the NPC's very existence.

Blockchainia's society resembles a world where war ceased to exist during the medieval period. Every since, the inhabitants have referred to their world as The Realm. The true history of these foundational moments in their history has been obfuscated from the NPC's minds. Various theories are being pushed amongst the Realm's Ministers, the name given to Blockchainia's scholar's and spiritual leaders. While swords and armor remain the most advanced lethal weapons, they are carried by Knights whom hold a mostly ceremonial status in society. However, entertainment technology was never hindered by the "forgotten events" of the past. Most recently, the release of the long awaited "Gamechainia 3", a console said to be connected to the fabric of the universe itself, has promised players eternal glory. The solution to Blockchainia's problems sets off a series of events that will change the face of the world forever: both theirs and ours. 

Through forbidding the teaching of the true history, the institutional leaders of Blockchainia believe the have successfully staved off the NPC's natural inclination to wage war against one another via magic and weaponry. Only aware of a history beginning the Lost Events, the NPC's no longer believe in an individual ability to produce magic, they believe the only characters strong enough to wield magic are scholars and nobles, and have left the running of society to these elites. That is until the day a Player enters the Realm and befriends a special NPC, inspiring a belief in himself so strong that he conjures a magical spell, something unheard of in the modern age. Not fully understanding the risks, he spreads this newfound spiritual growth to the other NPCs, who shortly thereafter begin to slaughter each other in a massive civil war involving various factions, the most prominent being Red vs. Blue.


### Narrative
Blockchainia exists in a realm where the flow of time is replaced by something its inhabitants refer to as "state", a plane where games of past, present, and future are slowly and unknowingly being drawn together by an unknown force.  

Players will become members of various guilds vying for control over resources and power in a virtual world fractured by misinformation. Each player's actions and alliances will influence the eventual storyline and available craftables, collectibles, and mechanics as they evolve through each season of game play.

It is initially unknown to the player, but most NPC's despise the powerful invaders that enter through yet-unknown virtual means. From the NPC's perspective, players entered their world as harmless AI Bots, whom one day are embedded into virtual avatars that take over their world through brute force. These "avatars" enjoy playing a brutal sport annihilating each other while pillaging the NPC world in the process, forcing their leaders to create every more powerful technology and magic. They yearn for a savior, one who will provide the governance necessary to banish these barbarians from the realm of Blockchainia forever.

While most NPCs view these invaders as a threat, others have found opportunity, offering "smart contracts" to players for completing certain tasks and rewarding them heavily for their efforts. 

The NPCs are introduced to the player through in-game interactions. Each NPC will have a unique personality and emotional state, which can change depending on how many rounds it has recently won or lost. This will alter what it says and what Resources are dropped at the end of each match. The NPCs intend intend their left Essence as a tip to the player for entertaining them with a game of cards. They also drop Resources for hard fought games, whether the challenging player wins or loses.  From the players perspective, they are receiving the spoils of each victory, as they do in most other video games. 

The bridge between the realm of Blockchainia and ours is now intertwined through Blockchainia: CardBrawl, connected through Chain State. To the NPCs, this is the only universe they know, and they believe they are playing against AI beings trapped inside a their version of a game console. One day, a traveler arrives, fully implemented in their world as Blockchainia's first Playable Character. The storyline will be experienced through the Role Playing Game Blockchainia: Paradigm Shift. The grind experience will move from Blockchainia: CardBrawl to Blockchainia: CryptoRoyale, enabled by our online gaming infrastructure, Blockchainia: OpenWorlds. While players of CryptoRoyale will be able to craft weapons and magic, all of the Legendary Spells and Equipment will be created during the founding seasons of CardBrawl. 

## 4. Art Style
TBA

### Visuals
TBA

## 5. Technology

- **Engine:** Unity
- **On-chain Competative Gameplay:** 

## 6. Monetization

- **Entry Fees and Rewards:** Players can play without minting by the "Ante-up" system, and can pick from a deck of common cards. If the player wins, they can still steal a perishable copy of a card from the opponent. 
- **Microtransactions:** Crafting through Forging, Alchemy, and Synthesis have a small on-chain overhead.
- **Season Pass:** Enables free entry into games for the season via an NFT.
- **Founders Pass:** Enables free entry for life via an NFT. 
- **Staker's Pack:** $200 in Cards, comes with all 8 original Concept art pieces, plus a chance to win a print or the original copy. 
- **Starter Pack:** $20 for 6 AI generated cards and one hand drawn concept art. Collect all 8 original Concept Art Pieces, collect a full deck, and upgrade a Card to Mythical in Season 1


## 7. Development and Marketing

### Team
- Ed Anderson
- Will Chastka

### Milestones
1. Prototype - 2-3 months
2. First Playable Alpha - 3-6 months
3. First Playable Beta - 6-9 months
3. Beta Testing and Feedback - 12 months
4. Launch - 15 months

### Marketing Strategy
- Series of verticle slice trailers showing spoofs of the OpenWorld and CryptoBrawl games
   - Reveal Brand/Narrative and Mechanics as close to gameplay as possible
   - Key interactions:
     - Combat
     - Crafting and Economics
     - Game Interoperabiity
     - Lore/Backstory
   - Frequent releases that communicate to audience the benefits of Early Access to drive Follows and Signups through unique rewards. 
- Promote the CardBrawl as a Companion Application
  - Reveals, Live Streams, and Q&A via Social Media
  - Early Access for feedback and hype building

- Layer Teaser Trailers with content produced by popular gaming influencers to create better brand recognition and recall
- Launch Event
- Recruit charitable organizations that allow players to complete specific game contracts and win end of season Tournaments to earn tokens paid to the charity of their choice

### Community Feedback
- NPC interactions will allow users to submit feedback about the game as they converse with thier opponent, whom will sometimes pose a question to the player about the game they are playing. 

## Conclusion

Blockchainia: CardBrawl utilizes a collect, craft, compete loop to create a strategic and dynamic card game, offering players a wealth of options for customization and tactical decision-making.
