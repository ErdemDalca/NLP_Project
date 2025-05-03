# D&D Combat Simulator: Roguelike RPG
## Comprehensive Game Design Document

---

# Table of Contents

- [Game Overview](#game-overview)
  - [Concept](#concept)
  - [Key Features](#key-features)
  - [Target Experience](#target-experience)

- [Core Gameplay Loop](#core-gameplay-loop)
  - [Macro Loop](#macro-loop)
  - [Session Loop](#session-loop)
  - [Combat Loop](#combat-loop)

- [Character Creation](#character-creation)
  - [Design Philosophy](#design-philosophy)
  - [Creation Flow](#creation-flow)
  - [Customization Options](#customization-options)

- [Classes and Races](#classes-and-races)
  - [Classes](#classes)
    - [Fighter](#fighter)
    - [Wizard](#wizard)
    - [Cleric](#cleric)
    - [Rogue](#rogue)
    - [Barbarian](#barbarian)
    - [Warlock](#warlock)
  - [Races](#races)
    - [Human](#human)
    - [Elf](#elf)
    - [Dwarf](#dwarf)
    - [Halfling](#halfling)
    - [Dragonborn](#dragonborn)
    - [Tiefling](#tiefling)
    - [Half-Orc](#half-orc)
    - [Gnome](#gnome)

- [Combat System](#combat-system)
  - [Design Philosophy](#design-philosophy)
  - [Combat Flow](#combat-flow)
  - [Streamlined Elements](#streamlined-elements)
  - [Tactical Depth](#tactical-depth)
  - [Special Combat Features](#special-combat-features)

- [Progression Systems](#progression-systems)
  - [Level Progression](#level-progression)
  - [Ability Score Improvements](#ability-score-improvements)
  - [Class Progression](#class-progression)
  - [Equipment Progression](#equipment-progression)

- [Game Content](#game-content)
  - [Enemy Design](#enemy-design)
    - [Enemy Categories](#enemy-categories)
    - [Enemy Scaling](#enemy-scaling)
  - [Spell System](#spell-system)
    - [Spell Categories](#spell-categories)
    - [Spell Schools](#spell-schools)
    - [Streamlined Spell Selection](#streamlined-spell-selection)
  - [Item Design](#item-design)
    - [Weapon Categories](#weapon-categories)
    - [Armor Categories](#armor-categories)
    - [Magic Items](#magic-items)
    - [Consumables](#consumables)

- [UI/UX Design](#uiux-design)
  - [Main Screens](#main-screens)
    - [Character Creation Screen](#character-creation-screen)
    - [Adventure Map Screen](#adventure-map-screen)
    - [Combat Screen](#combat-screen)
    - [Character Sheet Screen](#character-sheet-screen)
    - [Shop/Rest Screen](#shoprest-screen)
  - [UI Elements](#ui-elements)
    - [Combat UI](#combat-ui)
    - [Information Design](#information-design)
    - [Accessibility Features](#accessibility-features)

- [Balancing Framework](#balancing-framework)
  - [Difficulty Curve](#difficulty-curve)
  - [Run Difficulty Scaling](#run-difficulty-scaling)
  - [Encounter Balancing](#encounter-balancing)
  - [Class Balancing](#class-balancing)
  - [Item/Ability Balancing](#itemability-balancing)

- [Meta Progression](#meta-progression)
  - [Unlock System](#unlock-system)
    - [Unlockable Content](#unlockable-content)
    - [Unlock Currency](#unlock-currency)
  - [Persistent Upgrades](#persistent-upgrades)
  - [Achievement System](#achievement-system)

- [Game Content](#game-content)
  - [Adventure Structure](#adventure-structure)
    - [Encounter Types](#encounter-types)
    - [Non-Combat Encounters](#non-combat-encounters)
  - [Boss Design](#boss-design)
    - [Example Bosses](#example-bosses)
    - [Boss Mechanics](#boss-mechanics)
  - [Enemy Variety](#enemy-variety)

- [Technical Implementation](#technical-implementation)
  - [Unity-Specific Considerations](#unity-specific-considerations)
  - [Performance Optimization](#performance-optimization)
  - [Development Priorities](#development-priorities)
  - [Minimum Viable Product](#minimum-viable-product)

- [Marketing and Player Engagement](#marketing-and-player-engagement)
  - [Target Audience](#target-audience)
  - [Key Selling Points](#key-selling-points)
  - [Content Updates Roadmap](#content-updates-roadmap)
  - [Community Engagement](#community-engagement)


---

## Game Overview

### Concept
A fast-paced, roguelike RPG that simulates D&D combat with simplified mechanics. Players create characters, battle through procedurally generated encounters, and develop their characters until they die, then start fresh with new character builds.

### Key Features
- Character creation based on simplified D&D 5e rules
- Turn-based combat focused on spell/ability selection and dice rolls
- Procedurally generated combat encounters with scaling difficulty
- Permanent death with meta-progression elements
- Streamlined D&D mechanics that maintain strategic depth while eliminating complexity

### Target Experience
Players should feel like they're experiencing the combat highlights of a D&D campaign without the slower pacing of traditional tabletop play. Each run should last 30-60 minutes, encouraging multiple playthroughs with different character builds.

---

## Core Gameplay Loop

### Macro Loop
1. Character creation
2. Adventure path selection
3. Series of combat encounters
4. Character death
5. Unlock meta-progression elements
6. Begin new run with a new character

### Session Loop
1. Select next encounter from a branching path
2. Engage in combat
3. Gain rewards (XP, items, resources)
4. Level up character
5. Make strategic choices for character development
6. Proceed to next encounter or rest

### Combat Loop
1. Initiative roll determines turn order
2. On player turn: Select action (spell, attack, item)
3. Roll appropriate dice for action resolution
4. Enemy takes turn using AI-driven strategy
5. Repeat until combat resolves
6. Gain rewards and proceed

---

## Character Creation

### Design Philosophy
Character creation should be fast (under 2 minutes) yet meaningful, with choices that significantly impact gameplay. Automate mundane calculations while preserving meaningful choices.

### Creation Flow
1. **Select Race**: Choose from 8 core races with distinct racial abilities
2. **Select Class**: Choose from 6 streamlined classes
3. **Roll Stats**: Simplified stat generation (4d6 drop lowest for each ability score, or point buy system)
4. **Select Background**: Choose from 6 backgrounds that provide additional skills/bonuses
5. **Starting Equipment**: Auto-generated based on class/background
6. **Final Customization**: Name character, select portrait, choose color scheme

### Customization Options
- **Ability Score Distribution**: Players can reassign generated scores to preferred abilities
- **Starting Feat Option**: Players may sacrifice a stat point to gain one starter feat
- **Skill Selection**: Choose 2-4 skills to be proficient in based on class/background

---

## Classes and Races

### Classes
Each class is streamlined to focus on its core fantasy while eliminating excessive complexity.

#### Fighter
- **Core Mechanic**: Action Surge (extra action) and Combat Maneuvers
- **Key Abilities**: Strength/Dexterity, Constitution
- **Special Feature**: Can reroll one attack roll per combat
- **Progression Focus**: Weapon mastery, increased critical hit range, defensive abilities
- **Subclasses**: Champion (critical hits), Battlemaster (tactical maneuvers)

#### Wizard
- **Core Mechanic**: Spellcasting (Intelligence-based) with spell preparation
- **Key Abilities**: Intelligence, Constitution
- **Special Feature**: Arcane Recovery (regain spell slots once per day)
- **Progression Focus**: Spell discovery, increased spell slots, specialized schools
- **Subclasses**: Evoker (damage spells), Abjurer (defensive magic)

#### Cleric
- **Core Mechanic**: Divine spellcasting (Wisdom-based) and Channel Divinity
- **Key Abilities**: Wisdom, Constitution
- **Special Feature**: Turn Undead, healing capability
- **Progression Focus**: Divine favor, healing efficiency, domain powers
- **Subclasses**: Life Domain (healing), War Domain (combat)

#### Rogue
- **Core Mechanic**: Sneak Attack and skill expertise
- **Key Abilities**: Dexterity, Intelligence/Charisma
- **Special Feature**: Cunning Action (bonus action options)
- **Progression Focus**: Damage multipliers, evasion capabilities, critical damage
- **Subclasses**: Thief (utility), Assassin (burst damage)

#### Barbarian
- **Core Mechanic**: Rage (damage reduction and bonus damage)
- **Key Abilities**: Strength, Constitution
- **Special Feature**: Reckless Attack (advantage with drawback)
- **Progression Focus**: Damage resistance, critical hit damage, sustained rage
- **Subclasses**: Berserker (frenzy), Totem Warrior (animal aspects)

#### Warlock
- **Core Mechanic**: Eldritch Blast + Invocations, limited but refreshing spell slots
- **Key Abilities**: Charisma, Constitution
- **Special Feature**: Pact Magic (fewer but recovering spell slots)
- **Progression Focus**: Eldritch Invocations, pact boons, patron blessings
- **Subclasses**: Fiend Pact (damage), Archfey Pact (control)

### Races
Races provide meaningful passive abilities and one active ability that can be used strategically.

#### Human
- **Passive**: +1 to all ability scores
- **Active**: Determination (advantage on one save per combat)

#### Elf
- **Passive**: Darkvision, immunity to sleep, advantage on charm saves
- **Active**: Elven Accuracy (reroll one attack die per combat)
- **Subraces**: High Elf (cantrip), Wood Elf (speed/stealth)

#### Dwarf
- **Passive**: Poison resistance, weapon proficiencies, darkvision
- **Active**: Stone Endurance (reduce damage once per combat)
- **Subraces**: Hill Dwarf (extra HP), Mountain Dwarf (armor proficiency)

#### Halfling
- **Passive**: Lucky (reroll natural 1s), nimbleness
- **Active**: Brave Heart (advantage on fear save/check)
- **Subraces**: Lightfoot (stealth), Stout (resilience)

#### Dragonborn
- **Passive**: Damage resistance based on ancestry
- **Active**: Breath Weapon (cone/line attack once per combat)

#### Tiefling
- **Passive**: Darkvision, fire resistance
- **Active**: Hellish Rebuke (reactive damage once per combat)

#### Half-Orc
- **Passive**: Menacing, darkvision
- **Active**: Relentless Endurance (survive at 1 HP once per day)

#### Gnome
- **Passive**: Advantage on Int/Wis/Cha saves vs. magic, darkvision
- **Active**: Tinker's Curiosity (create small device with tactical effect)
- **Subraces**: Forest Gnome (minor illusion), Rock Gnome (gadgets)

---

## Combat System

### Design Philosophy
Combat should be fast (2-5 minutes per encounter) yet tactical, with meaningful decisions and the excitement of dice rolls. Simplify calculations but maintain the core D&D combat experience.

### Combat Flow
1. **Initiative**: Roll d20 + Dexterity modifier to determine turn order
2. **Action Economy**: Each turn includes:
   - 1 Action (attack, cast spell, use item)
   - 1 Bonus Action (if available through abilities)
   - 1 Reaction (if triggered)
3. **Resolution System**:
   - Attacks: d20 + modifiers vs AC
   - Saving Throws: d20 + ability modifier vs DC
   - Damage: Appropriate dice based on weapon/spell

### Streamlined Elements
- **Pre-calculated Modifiers**: Show final bonuses clearly
- **Automated Conditions**: Visual indicators for conditions like poisoned, stunned
- **Quick Roll Options**: One-click for advantage/disadvantage
- **Spell Management**: Simplified spell slot tracking
- **Health System**: HP bars with clear indicators for danger thresholds

### Tactical Depth
- **Positioning System**: Abstract positioning with Front Line/Back Line instead of grid
- **Targeting Rules**: Area effects hit multiple targets based on description
- **Cover System**: Simple cover bonuses for certain scenarios
- **Resource Management**: Manage spell slots, class resources, and consumables

### Special Combat Features
- **Critical Hits**: Natural 20 doubles damage dice
- **Advantage/Disadvantage**: Roll 2d20 and take higher/lower
- **Death Saving Throws**: When at 0 HP, roll to stabilize or die
- **Inspiration**: Gain advantage on one roll through good play
- **Combat Objectives**: Some fights have victory conditions beyond "reduce enemy to 0 HP"

---

## Progression Systems

### Level Progression
- **XP System**: Gain XP from defeating enemies, completing encounters
- **Level Range**: Characters progress from level 1 to 10
- **Level-Up Process**:
  1. Gain HP based on class Hit Die + Con modifier
  2. Gain class features based on level
  3. Gain new spell slots/spells for casters
  4. Ability Score Improvement at levels 4 and 8
  5. Unlock subclass features at predetermined levels

### Ability Score Improvements
- **Standard Improvement**: +2 to one ability score or +1 to two scores
- **Feat Alternative**: Select one feat instead of ability improvement

### Class Progression
Each class has a streamlined progression path focusing on core abilities:
- **Fighters**: Gain additional attacks, fighting styles, and maneuvers
- **Wizards**: Unlock new spell levels, increase prepared spells, gain school specialization
- **Clerics**: Unlock divine intervention, improved channel divinity, domain powers
- **Rogues**: Increase sneak attack damage, gain new cunning action options
- **Barbarians**: Improve rage damage, gain new primal paths, increase resistances
- **Warlocks**: Gain invocations, pact boons, and mystic arcanum

### Equipment Progression
- **Loot System**: Gain gold and items from combat encounters
- **Magic Items**: Rare but impactful upgrades categorized by rarity
- **Equipment Slots**: Weapon, Armor, Accessory (2), Consumables (3)
- **Shop System**: Spend gold at shops between encounters

---

## Game Content

### Enemy Design
Enemies are categorized into types with distinct behavior patterns and balanced to create appropriate challenges.

#### Enemy Categories
- **Beasts**: Lower intelligence, predictable attacks, often pack tactics
- **Humanoids**: Tactical, use equipment similar to players
- **Monstrosities**: Unique abilities, often with condition effects
- **Undead**: Resistance to certain damage types, debilitating effects
- **Aberrations**: Unpredictable, psychic abilities, reality-warping
- **Dragons**: Powerful, breath weapons, multiple attack options
- **Fiends**: Fire/necrotic themes, corruption abilities
- **Celestials**: Radiant damage, healing capabilities
- **Elementals**: Type-specific damage and immunities
- **Constructs**: Physical resistance, predictable patterns

#### Enemy Scaling
- **CR System**: Challenge Rating determines enemy stats
- **Level Appropriate Encounters**: Enemies matched to character level
- **Elite Enemies**: Upgraded versions with additional abilities
- **Bosses**: Unique enemies with multiple phases and special mechanics

### Spell System
Spells are streamlined for faster combat while maintaining tactical choices.

#### Spell Categories
- **Cantrips**: At-will minor spells
- **Leveled Spells**: Consume spell slots, scale with slot level
- **Ritual Spells**: Can be cast without slots outside combat

#### Spell Schools
- **Abjuration**: Protection and wards
- **Conjuration**: Summoning and creation
- **Divination**: Information and foresight
- **Enchantment**: Mind control and buffs
- **Evocation**: Elemental damage
- **Illusion**: Deception and misdirection
- **Necromancy**: Death and undeath
- **Transmutation**: Transformation and alteration

#### Streamlined Spell Selection
Include 15-20 spells per level focusing on:
- Direct damage spells
- Tactical control effects
- Buffs and debuffs
- Utility with combat applications

### Item Design

#### Weapon Categories
- **Simple Weapons**: Lower damage, accessible to all
- **Martial Weapons**: Higher damage, class restrictions
- **Ranged Weapons**: Distance advantage, ammunition management
- **Magic Weapons**: Special properties and bonuses

#### Armor Categories
- **Light Armor**: Lower AC, no penalties
- **Medium Armor**: Moderate AC, minor penalties
- **Heavy Armor**: High AC, movement penalties
- **Shields**: AC bonus, occupies one hand

#### Magic Items
- **Common**: Minor bonuses (+1)
- **Uncommon**: Moderate bonuses (+1) with situational abilities
- **Rare**: Significant bonuses (+2) with powerful abilities
- **Very Rare**: Major bonuses (+3) with game-changing abilities
- **Legendary**: Campaign-defining powers (limited to special runs)

#### Consumables
- **Potions**: Healing, buff effects
- **Scrolls**: One-time spell use
- **Bombs/Grenades**: Area damage
- **Elixirs**: Temporary stat boosts

---

## UI/UX Design

### Main Screens

#### Character Creation Screen
- Portrait selection
- Race/Class selection with visual previews
- Ability score allocation with clear modifiers
- Background selection with benefit preview
- Final character summary

#### Adventure Map Screen
- Branching path visualization
- Encounter type indicators
- Difficulty indicators
- Rest site locations
- Boss/elite encounters
- Path selection interface

#### Combat Screen
- Character avatar and stats
- Enemy display with health bars
- Action selection menu
- Dice roll visualization
- Spell/ability selection interface
- Turn order indicator
- Resource trackers (HP, spell slots, class resources)

#### Character Sheet Screen
- Stats summary
- Equipment display
- Spell/ability list
- Level progress
- Achievement/history log

#### Shop/Rest Screen
- Available items with costs
- Character gold total
- Purchase confirmation
- Rest options (heal, upgrade, prepare)

### UI Elements

#### Combat UI
- Streamlined action buttons
- Drag-and-drop targeting
- Visual dice rolls
- Animation for actions/spells
- Clear status effect indicators
- Danger indicators for low health

#### Information Design
- Tooltip system for detailed information
- Color-coding for damage types
- Visual language for advantage/disadvantage
- Clear indicators for action economy

#### Accessibility Features
- Colorblind mode
- Text size options
- Animation toggle
- Sound volume controls
- Combat speed settings

---

## Balancing Framework

### Difficulty Curve
- **Early Game (Levels 1-3)**: Forgiving, introducing core mechanics
- **Mid Game (Levels 4-7)**: Balanced challenge, introducing strategic complexity
- **Late Game (Levels 8-10)**: Challenging, testing mastery of systems

### Run Difficulty Scaling
- **Standard Run**: Balanced for average player skill
- **Hard Mode**: Unlockable, enemies have more HP and abilities
- **Challenge Runs**: Special conditions like "no resting" or "permanent debuff"

### Encounter Balancing
- **XP Budget System**: Each encounter has XP value based on enemy CR
- **Encounter Types**:
  - Easy: Below level CR, minimal resource expenditure
  - Medium: At level CR, moderate resource expenditure
  - Hard: Above level CR, significant resource expenditure
  - Deadly: Well above level CR, possible defeat without perfect play

### Class Balancing
- **DPS Parity**: All classes should be able to deal comparable damage over time
- **Utility Balance**: Lower damage classes have more control/utility
- **Resource Economy**: Short/long rest abilities balanced across classes
- **Scaling Balance**: All classes remain viable throughout level range

### Item/Ability Balancing
- **Power Curve**: Items and abilities power scales with character level
- **Rarity Balance**: Rarer items have more impactful effects
- **Synergy Design**: Items/abilities create interesting combinations without breaking game balance

---

## Meta Progression

### Unlock System
Players earn permanent unlocks that persist between runs:

#### Unlockable Content
- **New Classes**: Start with 3 basic classes, unlock 3 advanced classes
- **Class Variants**: Alternative versions with modified abilities
- **Subclasses**: Unlock additional subclass options
- **Starting Builds**: Pre-configured builds for faster starts
- **Special Items**: Unique items that can appear in future runs
- **Challenge Modes**: Special game modes with modified rules

#### Unlock Currency
- **Soul Shards**: Earned based on run performance
- **Achievement Rewards**: One-time bonuses for specific accomplishments
- **Challenge Completions**: Bonus currency for completing difficult runs

### Persistent Upgrades
- **Starting Bonuses**: Minor bonuses to starting characters
- **Enhanced Drop Rates**: Increased chance for better items
- **Extra Starting Gold**: Begin with additional resources
- **Additional Rerolls**: More chances to adjust random elements
- **Expanded Shop Options**: More items available in shops

### Achievement System
- **Class Mastery**: Complete runs with each class
- **Perfect Kills**: Defeat bosses without taking damage
- **Speed Runs**: Complete runs under time thresholds
- **Challenge Completions**: Finish special challenge modes
- **Collection Goals**: Find all items of certain types

---

## Game Content

### Adventure Structure
- **Run Length**: 12-15 encounters per successful run
- **Path Structure**: Branching paths with risk/reward choices
- **Region Types**: Themed areas with specific enemy types
- **Special Encounters**: Unique scenarios beyond standard combat

#### Encounter Types
- **Standard Combat**: Straightforward battle against enemies
- **Elite Combat**: Harder enemies with special abilities
- **Boss Fights**: Major encounters with unique mechanics
- **Mini-Boss**: Mid-tier challenge with special rewards
- **Ambush**: Combat with disadvantageous starting conditions
- **Horde Battle**: Multiple weaker enemies
- **Puzzle Combat**: Enemies with specific weaknesses to discover

#### Non-Combat Encounters
- **Shrines**: Offer blessings/curses with risk/reward
- **Treasure Rooms**: Resource acquisition
- **Merchants**: Buy/sell opportunities
- **Rest Sites**: Heal and prepare for next encounters
- **Events**: Narrative scenarios with choices and consequences

### Boss Design
Each boss should have unique mechanics that test player mastery.

#### Example Bosses
- **Ancient Dragon**: Phase-based fight with terrain changes
- **Lich**: Summons minions and has immunity phases
- **Giant Construct**: Destroyable parts that change attack patterns
- **Demon Lord**: Corrupts arena, inflicts status effects
- **Archmage**: Counterspell mechanics, magical shields

#### Boss Mechanics
- **Phase Changes**: Boss behavior changes at HP thresholds
- **Special Actions**: Unique abilities outside standard action economy
- **Arena Effects**: Environmental hazards or benefits
- **Minion Summoning**: Additional enemies during fight
- **Vulnerability Windows**: Strategic opportunities for bonus damage

### Enemy Variety
Game should include at least:
- 10 enemy types per region
- 5 elite variants per region
- 2-3 mini-bosses per region
- 1 major boss per region
- Total of 100+ distinct enemy encounters

---

## Technical Implementation

### Unity-Specific Considerations
- **Scene Structure**: Modular design for encounter types
- **Asset Management**: Categorization for easy content expansion
- **Save System**: Auto-save between encounters, run history
- **Procedural Generation**: Encounter composition, map layout

### Performance Optimization
- **Asset Loading**: Load only necessary assets for current encounter
- **Animation System**: Sprite-based for lower memory overhead
- **Particle Effects**: Optimized for mobile-capable performance
- **Memory Management**: Clear unused resources between encounters

### Development Priorities
1. **Core Combat Loop**: Build and test basic combat functionality
2. **Character System**: Implement character creation and progression
3. **Content Development**: Create enemies, items, abilities
4. **UI Implementation**: Design and implement user interface
5. **Balance Testing**: Iterate on game balance
6. **Meta Progression**: Implement between-run systems
7. **Polish & Optimization**: Final visual and performance improvements

### Minimum Viable Product
- 3 playable classes
- 2 regions with distinct enemies
- Basic meta progression
- Core combat functionality
- 50+ enemies/encounters
- 100+ items/spells/abilities

---

## Marketing and Player Engagement

### Target Audience
- D&D players looking for quick gameplay sessions
- Roguelike enthusiasts who enjoy build variety
- RPG fans who appreciate character development
- Mobile gamers looking for deeper experiences

### Key Selling Points
- Authentic D&D combat experience in quick sessions
- Deep strategic choices with simple mechanics
- High replayability through build variety
- Satisfying meta progression

### Content Updates Roadmap
- **Launch**: Core game with 6 classes, 8 races, 2 regions
- **Update 1**: New region with undead theme
- **Update 2**: 2 new classes (Paladin, Ranger)
- **Update 3**: Prestige system and legendary items
- **Update 4**: New region with abyssal theme
- **Update 5**: Challenge modes and daily runs

### Community Engagement
- Build sharing system
- Daily challenges
- Achievement leaderboards
- Run recording and sharing