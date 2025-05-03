Incremental Game Design Document
Blending Clicker Heroes Progression with Old School RuneScape Nostalgia
(Complete with Formulas, Examples, and Explanations)

1. Core Concept
A hybrid idle/incremental game where players:

Recruit heroes inspired by OSRS skills and gear.

Battle monsters across regions (Misthalin, Asgarnia, Wilderness).

Prestige to unlock god-aligned buffs and endless scaling.

Collect rare drops (pets, cosmetics, gear) via a completionist log.

2. Hero System
Hero Tiers & Unlocks
Heroes are divided into 5 tiers, unlocked progressively via regions and prestiges:

Tier	Region	Heroes Unlocked	Role
1	Misthalin	1-5	Basic DPS, Click Damage
2	Asgarnia	6-10	AoE, Crit Buffs
3	Kandarin	11-15	Debuffs, Gold Farming
4	Wilderness	16-20	Infinite Scaling
5	Prestige 1+	21-25	God-Aligned (Saradomin, Zamorak, etc.)
Hero Formulas
Cost Formula
Copy
HeroCost(n, R) = base_cost * (1.2^n) * (1.5^(R - 1))  
n: Hero level.

R: Region tier (Misthalin = 1, Wilderness = 4).

Example:

Hero 1 (Lumbridge Warrior) at Level 10 in Misthalin (R=1):
100 * 1.2^10 ≈ 619 gold.

Hero 20 (Abyssal Demon) at Level 25 in Wilderness (R=4):
30,000 * 1.2^25 ≈ 28.6M gold.

DPS Formula
Copy
HeroDPS(n, R, P) = base_dps * (1.25^n) * (2^R) * (1.1^P)  
P: Prestige tier.

Example:

Hero 5 (Cursed Archer) at Level 10 (R=1, P=0):
50 * 1.25^10 ≈ 465 DPS.

Hero 25 (Zaros’ Shadow) at Level 25 (R=4, P=5):
15,000 * 1.25^25 * 2^4 * 1.1^5 ≈ 117M DPS.

3. Monster System
Monster HP & Gold Scaling
HP Formula
Copy
MonsterHP(S, R, P) = base_HP * (1.25^S) * (2^R) * (1.3^P)  
S: Sub-zone number.

Example:

Cowpen (S=1) in Misthalin (R=1, P=0):
100 * 1.25^1 * 2^1 = 250 HP.

Wilderness (S=100) at Prestige 5 (R=4, P=5):
100 * 1.25^100 * 2^4 * 1.3^5 ≈ 4.8B HP.

Gold Drop Formula
Copy
Gold(S, R, P) = base_gold * (1.2^S) * (1.5^R) * (1.1^P)  
Example:

Goblin Village (S=10) in Misthalin (R=1, P=0):
10 * 1.2^10 * 1.5^1 ≈ 62 gold.

Wilderness (S=50) at Prestige 5 (R=4, P=5):
50 * 1.2^50 * 1.5^4 * 1.1^5 ≈ 1.9M gold.

Bosses
Minibosses (Every 10th Sub-Zone)
Copy
MinibossHP = MonsterHP(S, R, P) * 10 * (1.2^(S/10))  
MinibossGold = Gold(S, R, P) * 10 * (1.5^(S/10))  
Example:

Lesser Demon (S=10) in Misthalin (R=1, P=0):
HP = 931 * 10 * 1.2^1 ≈ 11,172 HP,
Gold = 62 * 10 * 1.5^1 ≈ 930 gold.

Elite Bosses (Sub-Zone Cap)
Copy
EliteBossHP = MonsterHP(S, R, P) * 50 * (1.5^(S/10))  
EliteBossGold = Gold(S, R, P) * 100 * (2^(S/10))  
Example:

General Graardor (S=30) in Asgarnia (R=2, P=3):
HP = 14,300 * 50 * 1.5^3 ≈ 2.4M HP,
Gold = 14,300 * 100 * 2^3 ≈ 11.4M gold.

4. Region & Sub-Zone Progression
Regions
Misthalin: Early-game (Cowpen, Lumbridge Swamp).

Asgarnia: Mid-game (Falador, Ice Mountain).

Kandarin: Late-game (Ardougne, Camelot).

Wilderness: Endless scaling (Revenants, Corporeal Beast).

Sub-Zone Scaling
Copy
SubZoneMultiplier(S, R, P) = (1 + S^1.5) * (1.5^R) * (1.2^P)  
Example:

Varrock Palace (S=3, R=2, P=1):
(1 + 3^1.5) * 1.5^2 * 1.2^1 ≈ 20.4x difficulty.

5. Prestige & God Offerings
Prestige Mechanics
Requirements: Defeat the region’s elite boss + reach level cap.

Rewards:

Global Buff: 1 + 0.5 * P (e.g., +50% DPS at P=1).

Offerings: Earn 10 * (1.5^P) per prestige.

God Buffs (Offerings Shop)
God (OSRS)	Offering Cost	Buff
Saradomin	10	+15% DPS
Zamorak	8	-10% Hero Cost
Guthix	12	+20% Gold Drops
Example:
After Prestige 3, a player spends 10 offerings on Saradomin:
HeroDPS *= 1.15.

6. Collection Log & Completionism
Drop Tiers
Tier	Drop Rate	Example Drops
Common	50%	Bones, Herbs
Uncommon	30%	Rune Bars
Rare	1%	Pets (e.g., Baby Dragon)
Ultra-Rare	0.1%	3rd Age Gear
Completion Rewards
50% Log: "Explorer" title (+5% movement speed).

90% Log: "Completionist Cape" (+10% all stats).

100% Log: "Trimmed Cape" (cosmetic aura).

7. Additional Addictive Mechanics
Daily/Weekly Systems
Daily Challenges: "Kill 100 Goblins" → 5 offerings + 1-hour 2x gold.

Weekly Boss Rush: Co-op raid vs. random bosses for leaderboard rewards.

Clans & Social Play
Clan Buffs: +5% DPS per active member.

Shared Loot: Split gold from co-op boss kills.

Seasonal Events
Halloween: Headless Horseman boss (limited-time pet).

Christmas: Snowverload event with 2x XP.

8. Example Player Journey
Day 1: Grind Cowpen (S1) for Hero 1 (Lumbridge Warrior).

Week 1: Unlock Asgarnia, defeat Lesser Demon (S10 miniboss).

Month 1: Prestige 3, equip Saradomin’s Champion (Hero 21).

Year 1: 100% Collection Log + Ascension Level 50 in Wilderness.

9. Balancing & Adjustments
Hero Cost/DPS: Reduce 1.2^n to 1.15^n if progression is too slow.

Monster HP: Lower 1.3^P to 1.25^P if prestiges feel grindy.

Playtesting: Use analytics to track drop rates vs. player retention.

10. Conclusion
This design merges Clicker Heroes’ exponential growth with OSRS’s nostalgic depth, creating a loop where players:

Grind sub-zones for incremental power.

Prestige for god-aligned buffs.

Chase rare drops for completionist goals.

Compete socially via clans and leaderboards.

Adjust formulas and drop rates based on playtesting, and lean into OSRS’s iconic monsters (e.g., KBD, Zulrah) for maximum nostalgia! 🎮✨