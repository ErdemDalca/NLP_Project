# Game Design Document (GDD) for "Blockchainia: CryptoRoyale"

## 1. Game Overview

### Title
Blockchainia: CryptoRoyale

### Concept
Blockchainia: CryptoRoyale is a first-person shooter (FPS) where players use both magically and technologically enhanced weapons  to compete against each other and AI enemies. Players can invest an entry fee ("ante-up") to join matches, with performance-based returns in game currency and various raw "materials" and magical "essence". The unique feature of the game lies in its combination of magic and technology, where players collect resources to craft spells and weapons, and breed magical pets to assist them in combat. Forging together any combination of these results in more powerful weapons and pets with unique abilities. Game play will feature fast, fun, and repeatable mechanics that consistently provides new incentives for player interactions to fuel a robust in-game economy. 

### Platform
PC/Mobile, Ported to VR after successful launch.

### Genre
First-person Shooter, RPG Elements

## 2. Gameplay

### Mechanics
- **Ante-Up and Rewards:** Players pay an entry fee to enter a match and can earn currency based on kills, "contract" completions, and final placement. Player skill, measured through a formula accounting for eliminations, accuracy, and round placement, enables higher skilled players to ante-up larger amounts, creating games with a high probability of minting higher-tier loot. 
- **Combat:** Standard FPS mechanics with additional magic spells. Players must balance between using firearms and magic spells based on their character's adeptness and the situation. Serious players will pour over strategies to find the best combinations of weapon and magic to bring into each match, competing with an ever-evolving player-driven meta to outwit their opponents in the Play-to-Own arena. 
- **Respawn:** The initial entry will be five (5) tokens granting the player 5 respawns in the match. Each kill earning back one (1) token. Additional respawns can be purchased through a vending machine, or looted from the environment. Placement bonus tokens will be awarded for the top 3 players/squads. 
- **Collection and Crafting:**
  - **Resources:** The basic resources of the game are elemental essence of magic and raw materials used to create technology (armor, weapons, etc). Resources can be gathered by eliminating AI enemies, looting, as well as drawn from fountains knowns by some as "drips" or "faucets".
  - **Essence:** Collected from fallen enemies and environment, used to create and upgrade spells through Alchemy.
  - **Materials:** Gathered from the environment and used to Forge new weapons or upgrade existing ones.
  - **Alchemy, Forging and Synthesis:** Visit NPC Achemy shops to combine essence and Synthesis shops to Forge materials into new weapons. Certain Synthesists also understand Alchemy, allowing players to upgrade gear and magic to legendary status.
  - **Vending:** Lost cherished loot in game and want to retrieve it? Visit the Vending Machine to purchase back recently lost items. Other vending machines allow players to purchase items, weapons, armor, and increase inventory space.  
- **Magic and Adeptness:** Usage of magic improves the adeptness stat, unlocking the ability to cast more powerful spells.
- **Playable Characters:** Each playable character is minted with unique genetic DNA. This DNA assigns their base stats and is used as a seed to generate their unique enhancement graph, which allows players a choice in how their characters evolve. 
- **Pets:** Spells can be Synthesized into an egg which hatches into a pet after being incubated in game for a certain period of time. Pets can be leveled and bred to create diverse companion types, aiding in various aspects of gameplay. 
- **Equipment Slots:** Forge weapons, armor, and accessories to increase available embedding slots. These slots allow for magic Spells and Items to be temporarily embedded to the weapon, creating ever-unique combinations of elemental damage and support spells and enabling new weapon commands and special attacks. Players are free to swap the Spells in these slots at any time, from any available in their inventory. This mechanic limits the number of spells players can bring into a game, as they must be equipped to an equipment slot to be available as a spell command. Spells can also be carried in the extraction backpack. Keep in mind, carried magic has an effect on player statistics: only magic in an equipment slot can have a benefit to a statistics. Magic in the backpack will only negatively effect statistics. 

### Forging, Alchemy, and Synthesis in Depth
***Material Types***

| Material Type      | Description                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------|
| Iron               | A common and sturdy metal used for basic weaponry and armor.                                     |
| Steel              | An alloy of iron, stronger and more durable, ideal for high-quality weapons and armor.           |
| Mithril            | A lightweight, silver metal known for its exceptional strength and magical properties.           |
| Adamantine         | A rare and nearly indestructible metal, perfect for legendary weapons and armor.                 |
| Obsidian           | A volcanic glass that can be sharpened to a razor edge, though brittle and best for slicing weapons. |
| Dragonbone         | Bones from ancient dragons, incredibly strong and imbued with magical energy.                    |
| Crystal            | Mystical crystals that can channel magical energies, used in crafting magical weapons.            |
| Darkwood           | A rare and sturdy wood with dark coloration, used for crafting bows and staves.                  |
| Orichalcum         | A mythical metal with a golden hue, known for its durability and enchantment capabilities.        |
| Moonstone          | A pale, luminescent stone with magical properties, often used in crafting magical jewelry and weapons. |
| Dwarven Steel      | Superior steel forged by dwarven smiths, known for its exceptional quality and strength.         |
| Elven Silver       | A fine and elegant metal used by elves, light and strong with magical properties.                |
| Froststeel         | Steel imbued with the essence of ice, causing weapons to have a chilling effect.                 |
| Bloodstone         | A dark, crimson stone that can enhance the power of blood magic in weapons.                      |
| Star Metal         | Metal forged from meteorite fragments, possessing unique otherworldly properties.                |
| Voidsteel          | A dark, shadowy metal that absorbs light, used in forging weapons with void or dark magic.       |
| Living Wood        | Enchanted wood that retains the essence of life, used for crafting living weapons and armor.     |
| Thunderstone       | A rare stone that can store electrical energy, used to forge weapons with thunderous power.      |
| Phoenix Feather    | Feathers from the mythical phoenix, used to craft weapons with regenerative and fiery properties. |
| Shadowglass        | A dark, reflective glass that can absorb and manipulate shadows, used in stealth weapons.        |

***Forging***
| Materials Combination                                   | Weapon Name            | Weapon Type  | Description                                                                                 |
|---------------------------------------------------------|------------------------|--------------|---------------------------------------------------------------------------------------------|
| Iron + Steel + Dwarven Steel                            | Titan Blade            | Sword        | A massive, incredibly durable sword with exceptional sharpness and strength.                |
| Mithril + Elven Silver + Moonstone                      | Elven Moonblade        | Sword        | A lightweight, enchanted sword that glows with a magical luminescence.                       |
| Adamantine + Dragonbone + Orichalcum                    | Dragon's Wrath         | Sword        | A nearly indestructible sword with immense power, forged from legendary materials.           |
| Obsidian + Darkwood                                     | Shadow Reaver          | Sword        | A sleek, sharp blade with a hilt made of darkwood, ideal for stealth and quick strikes.      |
| Crystal + Star Metal + Moonstone                        | Celestial Bow          | Bow          | A mystical bow that shoots arrows imbued with celestial energy.                              |
| Froststeel + Thunderstone + Iron                        | Stormbringer           | Crossbow     | A crossbow that fires bolts charged with icy and electrical energy.                          |
| Bloodstone + Voidsteel + Obsidian                       | Bloodseeker            | Dagger       | A dark, cursed dagger that drains the life force of its victims.                             |
| Living Wood + Crystal + Elven Silver                    | Nature's Wrath         | Staff        | A staff that channels the power of nature, perfect for druids and elemental mages.           |
| Steel + Iron + Dwarven Steel + Thunderstone             | Thunder Hammer         | Hammer       | A heavy hammer that delivers powerful, thunderous strikes.                                   |
| Orichalcum + Star Metal + Voidsteel + Shadowglass       | Starfall Rifle         | Firearm      | A futuristic rifle that fires energy projectiles with dark and otherworldly properties.      |
| Adamantine + Mithril + Phoenix Feather                  | Phoenix Blaster        | Firearm      | A powerful firearm that shoots fiery projectiles with regenerative properties.               |
| Dragonbone + Froststeel + Thunderstone + Adamantine     | Frostfire Cannon       | Firearm      | A cannon that combines the elements of ice and fire to devastating effect.                   |
| Darkwood + Living Wood + Crystal                        | Enchanted Longbow      | Bow          | A bow made from enchanted woods, perfect for long-range, precise shots.                      |
| Obsidian + Star Metal + Moonstone + Voidsteel + Mithril | Nightfall Greatsword   | Sword        | A colossal sword that combines light and dark energies, dealing massive damage.              |
| Iron + Steel + Dwarven Steel + Orichalcum               | Guardian Shield        | Shield       | A nearly impenetrable shield forged from the strongest metals.                               |
| Froststeel + Bloodstone + Voidsteel                     | Frostmourne            | Sword        | A cursed sword that emanates chilling darkness and drains the life force of its victims.     |
| Adamantine + Dragonbone + Phoenix Feather               | Eternal Flame Sword    | Sword        | A legendary sword with eternal flames, capable of incinerating foes with each strike.        |
| Living Wood + Crystal + Moonstone                       | Celestial Staff        | Staff        | A staff imbued with celestial and natural magic, ideal for powerful spellcasting.            |
| Elven Silver + Mithril + Moonstone + Star Metal         | Starlight Crossbow     | Crossbow     | A crossbow that shoots radiant bolts of light, effective against dark creatures.             |
| Iron + Steel + Obsidian + Shadowglass                   | Assassin's Blade       | Dagger       | A stealthy, razor-sharp dagger perfect for silent takedowns.                                 |

### Magic in Depth
***Essense Types***:
  - Earth  
  - Water
  - Fire
  - Wind
  - Void

***Alchemy***
| Combination   | Spell Name       | Description                                                                 |
|---------------|------------------|-----------------------------------------------------------------------------|
| Earth + Earth | Rockslide        | A massive slide of rocks that crushes enemies.                              |
| Earth + Water | Mudslide         | A torrent of mud that engulfs and slows enemies.                            |
| Earth + Water | Swamp Surge      | Summons a swampy mire that entangles and poisons foes.                      |
| Earth + Fire  | Lava Burst       | Erupts molten rock that burns and traps enemies.                            |
| Earth + Fire  | Magma Wave       | A wave of superheated magma that scorches everything in its path.           |
| Earth + Wind  | Sandstorm        | Whips up a fierce sandstorm that blinds and slices through enemies.         |
| Earth + Wind  | Quake Gust       | A powerful quake combined with a fierce gust that shakes and topples foes.  |
| Earth + Void  | Petrify          | Turns enemies to stone, immobilizing them completely.                       |
| Earth + Void  | Voidquake        | A devastating earthquake infused with void energy that disrupts reality itself. |
| Water + Water | Tsunami          | A gigantic wave that washes away everything in its path.                    |
| Water + Fire  | Steam Blast      | A burst of scalding steam that burns and blinds enemies.                    |
| Water + Fire  | Boiling Rain     | A rain of boiling water that scalds foes over a wide area.                  |
| Water + Wind  | Hurricane        | A powerful hurricane that drenches and blows away everything in its path.   |
| Water + Wind  | Frost Gale       | A chilling gale that freezes enemies solid.                                 |
| Water + Void  | Abyssal Tide     | Summons a tide from the abyss that pulls enemies into the void.             |
| Water + Void  | Shadow Mist      | A dark mist that saps the life force of those within it.                    |
| Fire + Fire   | Inferno          | An intense blaze that engulfs and incinerates everything.                   |
| Fire + Wind   | Inferno Whirlwind| A swirling vortex of fire that incinerates everything in its path.          |
| Fire + Wind   | Flame Cyclone    | A massive cyclone of flames that engulfs and burns everything it touches.   |
| Fire + Void   | Hellfire         | Summons flames from the void that burn with unholy intensity.               |
| Fire + Void   | Nether Blaze     | A black fire that consumes the very essence of its targets.                 |
| Wind + Wind   | Tornado          | A powerful tornado that tears through everything in its path.               |
| Wind + Void   | Phantom Tempest  | A ghostly tempest that drains the life force of those caught within it.     |
| Wind + Void   | Ethereal Breeze  | A soothing breeze from the void that heals allies and confounds enemies.    |
| Void + Void   | Annihilation     | A destructive force that obliterates everything it touches.                 |

### Synthesized Spells
| Essence Combination                        | Spell Name              | Description                                                                                      | Perk/Ability                                |
|--------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------|
| Essence of Fire + Steel                    | Flame Armor             | Envelops the caster in fiery armor.                                                              | Increased defense and fire resistance.      |
| Essence of Water + Mithril                 | Aqua Shield             | Summons a shield of water around the caster.                                                     | Damage absorption and healing over time.    |
| Essence of Earth + Adamantine              | Stone Skin              | Turns the caster's skin into rock.                                                               | Increased physical defense and resilience.  |
| Essence of Wind + Elven Silver             | Gale Speed              | Grants the caster enhanced speed and agility.                                                    | Increased movement speed and evasion.       |
| Essence of Void + Obsidian                 | Shadow Cloak            | Envelops the caster in shadows, making them harder to detect.                                    | Stealth and reduced detection by enemies.   |
| Essence of Lightning + Crystal             | Thunder Strike          | Empowers the caster's weapon with lightning.                                                     | Increased weapon damage with lightning effects. |
| Essence of Ice + Froststeel                | Frostbite               | Imbues the caster with icy power.                                                                | Slows enemies and adds frost damage to attacks. |
| Essence of Light + Moonstone               | Radiant Heal            | Channels the power of light to heal the caster and allies.                                       | Healing over time and light resistance.     |
| Essence of Nature + Living Wood            | Verdant Growth          | Causes plants to rapidly grow around the caster.                                                 | Health regeneration and increased healing received. |
| Essence of Darkness + Voidsteel            | Dark Pact               | Empowers the caster with dark energy at a cost.                                                  | Increased attack power but drains health.   |
| Essence of Fire + Phoenix Feather          | Phoenix Rebirth         | Revives the caster upon death with full health.                                                  | One-time automatic revival.                 |
| Essence of Water + Bloodstone              | Blood Bond              | Links the caster to an ally, sharing health.                                                     | Shared health pool with a linked ally.      |
| Essence of Earth + Dragonbone              | Dragon's Resolve        | Grants the caster immense physical strength and endurance.                                       | Increased attack power and defense.         |
| Essence of Wind + Star Metal               | Meteoric Dash           | Allows the caster to dash forward at incredible speed.                                           | Quick dash movement with invincibility frames. |
| Essence of Void + Shadowglass              | Phantom Strike          | Teleports the caster behind an enemy and strikes.                                                | Instant teleportation and critical strike.  |
| Essence of Lightning + Thunderstone        | Stormcall               | Summons a storm that strikes enemies with lightning bolts.                                       | Area-of-effect lightning damage.            |
| Essence of Ice + Elven Silver              | Winter's Embrace        | Surrounds the caster in a freezing aura.                                                         | Slows nearby enemies and reduces damage taken. |
| Essence of Light + Orichalcum              | Divine Shield           | Creates an invulnerable barrier around the caster for a short time.                              | Temporary invincibility.                    |
| Essence of Nature + Darkwood               | Woodland Sentinel       | Summons a protective spirit to aid the caster.                                                   | Summons an ally that attacks enemies and heals allies. |
| Essence of Darkness + Iron                 | Nightfall               | Engulfs the battlefield in darkness, blinding enemies.                                           | Reduces enemy accuracy and vision.          |
| Essence of Fire + Adamantine               | Inferno                 | Unleashes a powerful burst of flames around the caster.                                          | High area-of-effect fire damage.            |
| Essence of Water + Mithril + Crystal       | Tidal Wave              | Summons a massive wave that sweeps over the battlefield.                                         | Large area-of-effect water damage and knockback. |
| Essence of Earth + Dwarven Steel + Orichalcum | Titan's Fury             | Grants the caster immense strength and resistance.                                               | Greatly increased attack power and defense. |
| Essence of Wind + Elven Silver + Star Metal | Astral Leap              | Allows the caster to leap great distances.                                                       | Enhanced jump height and distance.          |
| Essence of Void + Obsidian + Shadowglass   | Nether Shift            | Shifts the caster into the void, making them untouchable for a short duration.                   | Temporary invincibility and phase through objects. |


### Game Progression
- **Match-Based Play:** Players enter matches, fighting both AI and other players.
- **Resource Gathering:** During matches, players must focus on looting essence and materials while also engaging enemies.
- **Extraction:** Extract your loot before being eliminated and forfeiting your stash. Utilize extraction zones, deposit through a vending machine, or find an in game item that enables portable extraction. Players spawning in with Legendary loot will be unable to extract themselves in early stages of the game. 
- **The Iron Price** Only players/squads who deal final damage to a player will be able to loot items from an eliminated player, but they must reach the loot before it expires and reverts into essence and materials. Other players will be able to steal a perishable copy of the item, but it will not result in the loss of the item by the eliminated player. If players do not reach the loot, it may be returned to its original owner if they have certain configurations equipped or have used special items or magic.
- **Earn the Dub:** Be the last player standing and collect your spoils in a bonus round while the rest of the lobby prepares for a new round to start. Runners-up obtain a placement bonus.
- **Crafting and Upgrading:** Post-match, players use collected items to craft and upgrade spells, weapons, and pets.
- **Pet Management:** Leveling, breeding and training pets for different abilities and tactical advantages. Pets enable airdrops and other incentives, including a racing mini-game in the RPG. 
- **Items, Relics, and Artifacts:** Collect in game items of various utility. Some items enable the summoning of powerful allies when the player reaches a certain number of eliminations in a row without dying. 
- **Card Game:** Each AI NPC, Pet, and Playable character will be embodied in various Semi-Fungible cards, which can be collected, traded, or burned for resources. Each card will have unique statistics, as well as an arbitrary number of arrows in any of the cardinal and ordinal directions, representing the directions they will attack when placed on the game board. Players win by capturing more cards on the board than their opponent, forfeiting one card from their deck for a loss to the other player. These cards can be minted in packs or found in-game by random looting.  

### Modes
- **Blockchainia: OpenWorld RPG:** Narrative-driven missions with rich backstory on the world and its resources.
- **Blockchainia: CryptoRoyale: Arena PvPvE:** Player vs. player vs. AI combat with ante-up and on-chain rewards, including contracts allowing squads to work together to complete high-stakes missions against AI opponents.
- **Off-Chain:** Private lobbies for free-play and practice, and custom configurations.
- **Configurations:** Game servers are privately run by individuals, governed through a DAO. Influences and streamers will be encouraged to become Server Owners and grow their own player communities. Operating as game-jockeys, they will lead player guilds towards greater influence in the future of Blockchainia's web3 interoperability, while experimenting with custom configurations to create new, fun, and exciting game play experiences.

## 3. Story and Setting

### World
The game is set in a virtual on-chain realm where the separation of magic and technology has been obfuscated from the public by a shadowy organization. Ancient ruins and mines scatter the landscape, providing rich sources of elemental essence and raw materials. NPC characters inhabit the land, and have littered it with monuments, fountains, as well as various spiritual relics and artifacts revealing a deep but unspoken culture. Their interactions give clues to the history of this strange world, revealed through easter eggs holding the secrets of the beginning of this unique realm, ultimately leading each player on a unique journey to understand the prophecy behind the NPC's very existence.

### Narrative
The realm of Blockchainia exists outside of the concept of time itself, a plane where games of past, present, and future are slowly being connected by an unknown force.  

Players will become members of various guilds vying for control over resources and power in a virtual world fractured by misinformation. Each player's actions and alliances will influence the eventual storyline and available craftables, collectibles, and mechanics as they evolve through each season of game play.

It is initially unknown to the player, but the NPC's despise the powerful invaders that enter through yet-unknown virtual means. From the NPC's perspective, players start as AI Card Bots, whom one day take the form of robots that take over their world. These robots enjoy playing a brutal sport annihilating each other while pillaging the NPC world in the process, forcing their leaders to create every more powerful technology and magic. They yearn for a savior, one who will provide the governance necessary to banish these barbarians from the realm of Blockchainia forever.

Yet, while most NPCs view these invaders as a threat, others have found opportunity, offering "smart contracts" to players for completing certain tasks and rewarding them heavily for their efforts. 

## 4. Art Style

### Visuals
A mix of dark gritty mines beneath a vibrant over-world, each environment brought to life with vibrant magical effects. Smooth yet blocky semi-realistic character models with stylized magical and technological gear. 


## 5. Technology

- **Engine:** Unity
- **On-chain Multiplayer:** Chain-connected, DAO authorized dedicated servers for seamless online integration.
- **Off-Chain:** Private lobbies for free-play and practice.

## 6. Monetization

- **Entry Fees and Rewards:** Players can opt into higher-stake matches for greater rewards. The Ante-Up fee is forfeited to the server running the game. Players can earn back their stake in the game by eliminating other players and extracting their tokens, or by being the last player standing. The server will share a portion of the play-fee with other stakeholders in the ecosystem.
- **Microtransactions:** Cosmetic items for characters and pets, weapons and magic spells, and items from NPC Vendors
- **Season Pass:** Enables free entry into games for the season, except for the highest tier, via an NFT.
- **Founders Pass:** Enables free entry for life via an NFT. 
- **Diminishing Returns:** A treasury of tokens will be made available to earn in game. Seasonally changing scarcity will create a sense of urgency to promote rapid upfront player growth. Players will be informed of these changes by seasonally released episodes of a continuous RPG titled Blockchainia: OpenWorld

## 7. Development and Marketing

### Team
- Ed Anderson
- Will Chastka

### Milestones
1. Prototype - 1 months
2. First Playable Alpha - 6 months
3. First Playable Beta - 9 months
3. Beta Testing and Feedback Incorporation - 12 months
4. Launch - 15 months

### Marketing Strategy
- Teasers and Reveals via Social Media, Q&A, Live Streams via Twitch, Youtube, TikTok
- Partnerships with popular streamers and influencers
- Early Access for feedback and hype building
- Launch Event
- Work with charitable organizations that allow players to complete specific game contracts and earn tokens paid to the charity of their choice
- Work with past and popular gaming brands and sports drinks to offer giveaways

## Conclusion

Blockchainia: CryptoRoyale combines dynamic FPS game play with deep RPG crafting and pet management, set in a unique world where magic meets technology. The game is designed to attract both casual and hardcore gamers with its innovative mechanics and rewarding game play loop.
