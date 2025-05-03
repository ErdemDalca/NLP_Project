# Game Design Document

## 1. Game Overview

- **Title (Working):**
- **Genre:** Text-based RPG, Loot Hunter, Turn-based
- **Platform:** Discord Bot
- **Target Audience:** casual Discord users, RPG fans, loot grinders
- **Tone / Theme:** fantasy

---

## 2. Game Concept

- **Elevator Pitch:**
A medieval themed looter and rpg game where you can go on quests to get money new armor, weapons, and magic items to help you take out the evil that has take over this world. Has a short story along with alot of action and different enemies that are either scaled to your level or have level based dungeons for you to progress the story by defeating bosses.

- **What Makes It Unique:**
This game blends the thrill of D&D-inspired stat crunching with quick, casual Discord interaction. It’s a fantasy looter you can play in 5-minute sessions—grind hard, flex your legendaries, and bring your server to glory.

---

## 3. Core Gameplay Loop

- **Start Action:** (e.g., Player uses `/hunt` or `/battle`)
- **Middle:** Fight → Earn XP → Gain loot
- **End:** Equip loot, level up, repeat

- **Secondary Loops:**
  - Daily logins
  - Co-op raids
  - Crafting/enhancing

---

## 4. Player Progression

- **How do players grow?**
	The leveling system is going to be xp based and follow the rule set of dnd 5e, each monster is going to have a cr level based on its defense and attacks and will follow normal dnd 5e xp calculations based on the persons level and cr of the monster.

- **Is there a max level or tier cap?**
	Max level is probably going to be around level 20
- **Prestige/rebirth system?** 
	might add a prestige system but not sure what it would look like as i would like it not have the same game play loop or at least a different story or some sort.
- **Will gear scale with your level?**
	no gear will not scale with your level a gears stats wil be based on the level of the monster you get it from
- **Classes?** Yes there will be classes 3 or 4 right now barbarian, knight, ranger, mage
	each class will have different stats and will be able to use different weps and armor, weps might be restricted by the stats of your character

---

## 5. Combat System

- **Combat Type:** turn based
- **Commands:** will use buttons to attack and if no action is given within 30 seconds it will skip your turn
- **Stat Influences:**
  - HP, ATK, DEF, (might want to see how todo crit hits)
- **Enemy types / behavior:**
  - Random enemies
  - with dungeons having bosses that give either more loot or higher quality loot

---

## 6. Loot System

- **Item Rarities:**
  - Common -> uncommon -> rare -> epic -> legendary -> Developer(for testing)
- **Item Types:** armor(helmet, chest, legs, boots), weps(range, melee, wands / staffs), rings, necklesses
- **Random Stats** All items will have random stats except for the base starting items
- **Special effects / Affixes?** they will be rare but there will be some special effects and affixes that add extra dmg to more defense etc.

---

## 7. User Experience in Discord

- **Command Style:**
  - Slash commands
  - Reactions/buttons
- **Feedback Style:**
  - Embed messages with maybe some ai generated art
- **Avoiding Spam:**
  - When a command to battle is used all messages will be silent and they will not be able to use the battle for 5 mins 

---

## 8. Social Features (Optional)

- **Parties / Raids?** Multiplayer battles are planned ie special events every everyone can join in (from every server? maybe)
- **Leaderboards?** yes will have o figure out a ranking system either be through level monsters killed total dmg done etc
- **Guilds or teams?** Each server will be its own guild and there will be a leaderboard for this
- **PvP?** yes

---

## 9. Economy

- **Currency Name(s):** right now gold(want to think of something more creative)
- **Use of Currency:**
  - Shop
  - Trade (maybe player to player trade)

---

## 10. Stretch Features / Future Ideas

* There will be game wide events and maybe seasonal stuff
* There is going to be a small story mostly explained when you create a character

---

## 11. Player Motivation

- **Why will players come back daily?**
	- I might add daily login rewards or extra rewards for doing battles daily
- **What will they want to achieve long-term?**
	- mostly trying to kill the final boss after the story
- **What emotions should the game evoke?** (e.g., thrill, humor, mystery)
	- mostly fun and maybe some sadness

---

## 12. Notes for Future Self

* things that might not make it to the game for a while
	* raids / multiplayer stuff (want to get the singe player loop working as much as possible )
	* trades
	* seasonal stuff
	* pvp (most likely to be the first of these features to be added)
	* leaderboards for guilds and player leaderboards
- Things i am not sure about if i should add
	- stuff todo with guilds (events made and run by server owners etc)