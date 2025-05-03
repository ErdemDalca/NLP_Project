Day 1-3

Spent a lot of time reading the documentation trying to understand things as much as possible
Worked out the idea for the game I wanted to create
Inspired by games like Binding of Isaac and Vampire Survivors

Monkey Mayhem: Jungle Survival Game Design Document
Introduction
"Monkey Mayhem" is a 2D survival game where the player controls a monkey defending itself against waves of hostile jungle animals. Inspired by the core mechanics of "Vampire Survivors," the game emphasizes strategic movement, auto-attacking weapons, and survival against overwhelming odds. Developed using the LittleJS engine with JavaScript for web platforms, the game aims to provide an engaging and replayable experience within the context of a game jam, targeting completion by December 12th.

Game Overview
Genre: Survival, Action, Arcade
Platform: Web (HTML and JavaScript using LittleJS)
Theme: Animals
Objective: Survive against continuous waves of enemy animals for as long as possible, aiming for a set time limit (e.g., 30 minutes).

Game Mechanics
Core Gameplay Loop
Spawn: Player starts as a monkey in the jungle.
Survival: Enemy animals continuously spawn and attack the player.
Combat: The monkey auto-attacks using acquired weapons.
Experience Gain: Defeated enemies drop experience bananas/gems.
Level Up: Collect experience to level up and choose new weapons or passive abilities.
Progression: Survive increasingly difficult waves and defeat boss animals.
Objective Completion: Aim to survive until the time limit is reached.

Controls
Movement: Arrow keys or WASD for directional movement.
Interaction: Mouse or keyboard input for menu navigation during level-up screens.
No Attack Buttons: Weapons auto-attack based on their unique properties.

Player Mechanics
Auto-Attacking Weapons: Weapons fire automatically, allowing the player to focus on movement and positioning.
Leveling Up: Collect experience to increase the monkey's level and enhance abilities.
Weapon and Passive Slots: Limited slots encourage strategic selection for synergistic builds.
Health Management: Avoid enemy contact to preserve health; collect health pickups when available.
Speed and Magnetism: Movement speed and item pickup range can be improved through passive items.

Enemy Mechanics
Continuous Spawning: Enemies spawn in waves that increase in difficulty over time.
Variety of Animals: Different enemy types (e.g., snakes, birds, tigers) with unique behaviors.
Boss Enemies: Stronger animals appear at intervals, offering greater challenges and rewards.
Attack Patterns: Enemies move toward the player, with some possessing special movement or attack behaviors.

Leveling and Progression
Experience Collection: Enemies drop bananas or gems that grant experience when collected.
Randomized Upgrades: Upon leveling up, the player chooses from random weapons or passive items.
Weapon Evolutions: Max-level weapons can evolve into more powerful forms when combined with specific passive items.

Objects and Classes
Player Class
Attributes:
Health: Current and maximum health points.
Level: Player's progression within a run.
Experience (XP): Points from collected bananas/gems.
Weapons: List of acquired weapons with auto-attack functionality.
Passive Items: List of enhancements providing ongoing benefits.
Movement Speed: Affected by certain passive items.
Magnetism: Determines the pickup range for items and experience.

Enemy Class
Attributes:

Health: Varies based on enemy type and progression.
Type: Defines behaviors (e.g., charging rhinos, swooping eagles).
Damage: Health lost upon contact with the player.
Speed: Movement speed toward the player.
Experience Value: XP granted upon defeat.
Drop Items: Chance to drop coins or chests containing upgrades.

Item Class
Types of Items:

Experience Bananas/Gems: Collected to gain XP.
Weapons: Auto-attacking tools defining offensive capabilities.
Passive Items: Boost stats like damage, speed, or area of effect.

Game Flow
Start Game: Player selects the monkey character and begins the game.
Early Waves: Initial enemy animals spawn slowly with lower health.
Leveling Up: Collect experience to level up and select new weapons/passives.
Increasing Difficulty: Waves become more challenging with diverse enemy types.
Boss Encounters: Defeat boss animals to obtain chests with upgrades.
Weapon Evolution: Max out weapons and combine with passives for evolved forms.
Survival Challenge: Survive until the time limit to complete the game.
Game Over: If health reaches zero or time limit is achieved.
Post-Game: Earn coins based on performance for meta-progression upgrades.

Unique Selling Points
Animal Theme: A fresh take on the survival genre with a jungle setting and animal characters.
Monkey Protagonist: Play as a monkey, offering unique weapons and abilities themed around jungle survival.
Diverse Enemy Animals: Face a variety of jungle creatures, each with distinct behaviors.
Weapon and Passive Synergy: Create powerful combinations that reflect the jungle theme (e.g., Banana Boomerangs, Vine Whip).
Accessible Gameplay: Simple controls focusing on movement, suitable for a wide audience.

Weapons and Passive Items
Weapon Examples
Done:
Large projectile at nearest enemy			            Coconut Cannon
Whip to left and right of character			            Tail Whip
Large projectile in direction of cursor			        Banana Bazooka
Area of effect damage zone around player		        Millipede Toxin Zone
Orbital around player					                Soldier Ant Swarm
Long controllable orbital around player			        Bamboo Staff
Large projectile at nearest enemy that passes through	Boulder Roll
Summon ability that homes in on enemies			        Hornet Swarm
Spore cloud damaging area at cursor			            Fungus Spores

To Do:
Directional Conical Screech brief STUN/SLOW		        Monkey Screech
trailing slowing/damaging area				            Feces Trail
Nearest enemy within fixed range slowed			        Pocket Sand
Decoy at cursor						                    Shadow Clone
Exploding Decoy	at player position			            Kaboomki
targeted area on contact SLOW 1	- Auto Attack upgrade 	Banana Peel


Passive Item Examples
To Do:
Spicy Pepper        Increases overall damage.
Ancient Scroll      Reduces weapon cooldown times.
Twin Fruit          Adds extra projectiles to weapons.
Jungle Drums        Increases the area of effect for all weapons.
Monkeys Paw		    Random Curses
Primal Instinct		Increased stats for X duration after killing Y enemies
Need to adjust damage formula to accomodate damage stat of player

Weapon Evolution Examples
To Do:
Evolved Tail Whip: Requires maxed Tail Whip and Spicy Pepper; deals increased damage with added burn effect.
Evolved Coconut Cannon (Explosive Nuts): Requires maxed Coconut Cannon and Jungle Drums; coconuts explode on impact, dealing area damage.

Project Timeline
Development Start: November 29th
Core Mechanics Implementation: By November 30th
Player movement and auto-attacking weapons
Enemy spawning and basic AI
Experience and leveling system
    Nov 29:
        Spent this day following littlejsengine documentation tutorial to make breakout
        Read the documentation a lot
        Brainstormed ideas
        Finalized idea EOD
    Nov 30:
        Started creating core mechanics of movement, weapons, enemy spawning, basic ai, and leveling system

Map and Content Creation: December 1st - December 5th
Design game map
Design weapons, passive items, and enemy types
Implement weapon evolutions and unique abilities

    Dec 1: Spent first day exploring available free assets and collecting sprites
        Had a tough time finding something that I liked and would fit the game
        https://otterisk.itch.io
        The Hana Caraka Base character asset by Bagong Games seemed to fit my desires the best
        I plan on modifying the base asset to fit my purposes
    Dec 2-3: Spent time searching for assets and integrating them into the enemy and player classes
        I liked this asset pack
        https://finalbossblues.itch.io/animals-2
        It provided relevant animals and animations for 4 directional movement
        Finished implementing sprites and enemy types
        Still need to work on Audio, more passives, weapon evolutions, and game map
        I found assets I would like to use in designing map
        https://vinchy007.itch.io/mini-survival
        For ground tiles and foliage
    
        


Balancing and Tuning: December 6th - December 8th
Adjust difficulty scaling and enemy waves
Fine-tune weapon and passive item effectiveness

Testing and Debugging: December 9th - December 10th
Playtesting for bugs and gameplay issues
Optimize performance for web platforms

Polishing and Finalization: December 11th
Implement placeholder art and sounds
Prepare for submission

Submission Deadline: December 12th

