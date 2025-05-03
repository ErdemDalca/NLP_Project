# TODO
Meaningful talents

Focus - Ultimates: Unlocked at Level 5, requires full "Focus" meter (earned via taking damage).
Turn order determined by Agility.

# Overview
Name: Sidescroller RPG
Genre: 2d, sidescroller, rpg, fantasy, turn-based combat, adventure, tactical

# Main objects/entities
* Entities: player, enemies
* Ally NPC: traders, quest givers
* Abilities
* Effects: buffs/debuffs (applied by abilities)
* Items

# Gameplay
Game world is represented by different screens, which can be switched, when you reach it's left or right border.

The screen consits of the following:
* Background image
* Screen interactive objects/images (chests, doors, furniture, etc.)
* Player sprite
* NPC sprites
* Enemy sprite (only one per screen)

# Player
Player can be moved across the screen on the X axis using keys A and D. Player can interact with objects, NPC and initiate a combat with enemies.

# Combat
When players is in a hostile screen (zone) there's a chance of an enemy spawning on the opposite side to where the player came. 

Example:
The players moves from *Town screen* to *Forest screen* using the left screen border (Forest <- Town).
The players comes from the RIGHT side of the screen, upon entering there's a chance of an enemy spawning on the LEFT side of the screen (Enemy - Player).
Once player gets close enough to the enemy, combat initiates.

Combat is turn-based, 1 vs 1, players always has the first move. Each entity (player and enemy) can either Attack (basic move, that any entity has, requires no mana, always available) or cast an Ability.
Attack and most of the abilities end the caster's turn, some the abilities preserve turn, allowing use to perform multiple actions on the turn.
Some abilities can apply an effect (buff or debuff) on a caster or on the opponent. Effects have duration (in turns), some effects are stackable, multiplying the effect power.
Some abilities have a cooldown in turns.

At the end of combat you receive XP = EnemyLevel * 20. There's a chance you receive an item as loot.

# Stats
Each entity during combat has the following:
* Health = 10 * Strength 
* Mana = 10 * Intelligence 
* Mana Regeneration = 1 * Intelligence 
* Level
* Stats:
    * Strength
    * Agility
    * Intelligence
* List of applied effects
* List of abilities on cooldown
* Equipment that provides stats
* Crit chance = 5% + 0.5% * Agility
* Crit multiplier = 50% + 10% * Agility
* Atttack damage = 2 * Strength + 0.5 * Agility

# Levelling
You earn XP by defeating enemies and completing quests.
XP required for levelup = 100 * Level
Once you Level up, you get:
* 3 Stat points to increase your STR/AGI/INT
* 1 Ability point to put inside talent tree

# Equipment/Items/Inventory
Player has an inventory with 16 slots. Items can obtains from enemy loot or from buying it from trader NPCs.
Each item can provide bonus to one of the Stats.

The player has the following equipment slots:
* Amulet/Necklace
* Ring x 2
* Relic x 2
* Weapon

The item can be one of the following category:
* Amulet/Necklace
* Ring
* Relic
* Weapon
* Quest
* Junk
* Consumable

The item can one of the following rarity type:
* Gray (junk)
* White (common item)
* Green (uncommon)
* Blue (rare)
* Purple (epic)
* Gold (unique/legendary) 
