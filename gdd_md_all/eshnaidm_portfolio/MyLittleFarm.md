# MyLittleFarm Game design document

> Originally written in Russian, translated by Erik

> This document excludes economy design, economy described in other document

## Game essence
- **The essence of the MyLittleFarm mini-game** is for players to develop a farm by buying plants, animals, and structures. 

- The farm is divided into sub-locations, each with its NPC and specific active tasks. These NPCs will be unlocked as the player progresses through the questline.

- There will be a **questline** on the farm, which is essentially a **task system**.

- Tasks will **replace** achievements, providing a monetary reward for quest completion (similar to achievements).

- After completing a specific questline, a new location with a new NPC and active task will be unlocked.

- The NPC, in turn, will give the player a new questline.

- The **goal** of the game remains unchanged: to buy everything on the farm (which, by the way, will only be possible by completing the full list of quests).

- The **core mechanics** remain the same: players buy crops that generate a certain income per second, and the game still remains semi-AFK simulator.
## Active Task System
### General Principles
**List** of active tasks in the mode: grass breaking, tree cutting, mining, fishing, cargo hauling.

Tasks such as **grass breaking** and cargo **hauling will** be upgraded through a menu for a certain amount.

For other tasks, **player statistics** are introduced. The player will have the following characteristics: **tree cutting, mining, and fishing**.

At the beginning of the game, each characteristic starts at level 0. By performing the corresponding active task, the player can increase their characteristics. 

The characteristics determine the **speed of tree chopping** (for lumberjacking), the **speed of ore breaking** (for mining), and **the speed of fish catching** (for fishing). 

The maximum level for each characteristic is 50. Every 10 levels, the player takes their tool to the **workshop**, where it is upgraded for money and a certain amount of time (preventing the pumping of the characteristic to level 50 on the first day). 

If the player tries to work with the old tool after reaching the level where they need to upgrade it, they will not gain experience for the task, preventing the player's development in both experience and the appearance of acquired resources.

#### Fatigue

There will be a **fatigue mechanic**. The player will have a fatigue value, initially set to zero. Each block mined adds +1 to the fatigue value, which gradually decreases (-1 every two seconds if the player is not breaking anything). 

The value will start decreasing after 10 seconds when the player stops breaking blocks, decreasing by one unit every 2 seconds. 

When the player increases the fatigue value by breaking a block, fatigue will be added at the following values, preventing the player from breaking blocks:
- 240-260 - 1%
- 260-280 - 3%
- 300-320 - 5%
- 320-340 - 10%
- 340-360 - 15%
- 360-380 - 20%
- 380-399 - 25%
- 400 - 100%

Fatigue is relieved when the fatigue value reaches 100.

### Grass Breaking

The player has grown grass in their barn, and their sole task is to cut it. 

### Cargo Hauling

There are four warehouses from which the player carries a cargo block to a truck. For each delivered block, the player receives a certain amount of money. 

The amount depends on the weight of the cargo and the distance between the warehouse from which the cargo was carried and the truck. 

The box is randomly issued to a random warehouse and has a random weight.

For money (similar to grass), the player improves characteristics such as **cargo value** (affects the amount of money from one cargo, like a modifier) and **cargo capacity** (allows the player to move faster, i.e., reduces the slowdown coefficient).

### Lumberjacking

In the northern part of the map, there is a forest where the player can harvest wood. The player has an axe. 

When the player reaches every 10th level (10, 20, 30, 40, 50), the axe can be upgraded in the workshop for money and time. 

The lumberjacking characteristic affects the speed of tree chopping, and the appearance of the axe affects the appearance of the chopped trees.

When chopping a tree, the player obtains the appearance of that tree. The wood will be used for building structures, completing quests, and upgrading tools.

Types of trees and types of axes used to chop them:

- Oak (initial axe)
- Birch (axe with level 10)
- Spruce (axe with level 20)
- Dark Oak (axe with level 30)
- Acacia (axe with level 40)
- Tropical Tree (axe with level 50)

### Mining

Through the forest, there are five scattered mines/caves. In the mine, players extract ores that are processed in the workshop into corresponding ingots, stones, and more. 

The player has a pickaxe. When the player reaches every 10th level (10, 20, 30, 40, 50), the pickaxe can be upgraded in the workshop for money and time. 

The mining characteristic affects the speed of extracting minerals, and the appearance of the pickaxe affects the appearance of the extracted ores. 

Ores spawn in mines with a certain percentage and depending on the pickaxe level (only ores that the player can break spawn).

Additionally, ingots, alloys, stones, and more are used in constructions, quests, and jewelry making. In the workshop, from certain resources from the mine, players can create **precious jewelry** and sell them for money.

Types of ores, their smelting, and types of pickaxes used to break them:

- **Stone** (without smelting). Broken with the initial pickaxe. Used in construction.
- **Coal** (without smelting). Broken with the initial pickaxe. Used in the workshop as fuel (in smelting).
- **Iron Ore → Iron Ingot** (10 iron ore, 1 coal, 1 minute). Broken with a pickaxe at level 10. Used in construction and jewelry making.
- **Copper Ore → Copper Ingot** (10 copper ore, 1 coal, 1 minute). Broken with a pickaxe at level 10. Used in construction and jewelry making.
- **Silver Ore → Silver Ingot** (10 silver ore, 2 coal, 1 minute). Broken with a pickaxe at level 20. Used in jewelry making.
- **Quartz Ore → Quartz** (10 quartz ore, 2 coal, 1 minute). Broken with a pickaxe at level 20. Used in construction.
- **Gold Ore → Gold Ingot** (10 gold ore, 3 coal, 1 minute). Broken with a pickaxe at level 30. Used in jewelry making and construction.
- **Amethyst Ore → Amethyst** (10 amethyst ore, 3 coal, 1 minute). Broken with a pickaxe at level 30. Used in jewelry making.
- **Platinum Ore → Platinum** (10 platinum ore, 4 coal, 1 minute). Broken with a pickaxe at level 40. Used in construction and jewelry making.
- **Emerald Ore → Emerald** Broken with a pickaxe at level 40 (10 emerald ore, 4 coal, 1 minute). Used in jewelry making.
- **Titanium Ore → Titanium Ingot** (10 titanium ore, 5 coals, 1 minute). Broken with a pickaxe at level 50. Used in construction.
- **Diamond Ore → Diamond** (10 diamond ore, 5 coals, 1 minute). Broken with a pickaxe at level 50. Used in jewelry making.

### Fishing

The player has 8 types of fish that can be caught with one fishing rod. 

Fish do not differ in any parameters except for their name; their value is calculated based on a **fixed multiplier** multiplied by passive income and the **weight modifier**. 

The **weight modifier** at level 0 has a range of 0.9-1.1, with each level adding 0.01 to the boundaries (0.91-1.11 at level 1, and so on). 

That is, leveling up gives a modifier addition to weight. Upon upgrading the fishing rod, the player unlocks new 8 types of fish that are more expensive (**higher fixed multiplier**) and continues to improve the weight modifier.

Changes to the fishing mechanics: when a fish is hooked, a meter appears at the bottom (between the HP and hunger bars, above the experience bar) showing when it is best to reel it in (from green to red). 

If reeled in too early or too late, the fish will escape or the line will break. The weight of the fish should determine the difficulty and timer to catch it using this mechanism. 

The difficulty of catching depends not just on the weight but on how this weight relates to the range of your current caught weight (i.e., 1.1 with a weight range of 0.9 and 1.1 is difficult, while 1.2 with a weight range of 1.2 and 1.4 is easy). 

Also, with a low chance, the player can catch trash that will be worth nothing.

The player enters fishing through the NPC fisherman Henry on their farm, and returns home through NPC fisherman Henry at the fishing spot.

## Weather and New Event System

The farm will now have weather that directly affects the chance of events occurring. The weather consists of two components: **temperature** and **precipitation**.

### Temperature
The temperature fluctuates between -30 and +30 degrees Celsius depending on the season, with specific ranges for each month. The temperature on a given day is **x**, and it changes with the following probabilities:

- x - 5: 3%
- x - 4: 5%
- x - 3: 7%
- x - 2: 10%
- x - 1: 15%
- x: 20%
- x + 1: 15%
- x + 2: 10%
- x + 3: 7%
- x + 4: 5%
- x + 5: 3%

If the result of this formula exceeds the temperature range for that month, the temperature changes to the same value but with the opposite sign (for example, if at -28 with a limit of -30 the temperature falls to -32, it becomes -24 instead).

At the start of the next month, the temperature is checked to see if it fits within the range for that month. If not, the temperature is set to the closest value within the range (e.g., the boundary).

Below are the months and their temperature ranges:

- **January**: Upper limit: -5, Lower limit: -30
- **February**: Upper limit: +5, Lower limit: -20
- **March**: Upper limit: +10, Lower limit: -10
- **April**: Upper limit: +15, Lower limit: 0
- **May**: Upper limit: +20, Lower limit: +5
- **June**: Upper limit: +25, Lower limit: +10
- **July**: Upper limit: +30, Lower limit: +15
- **August**: Upper limit: +25, Lower limit: +10
- **September**: Upper limit: +20, Lower limit: +5
- **October**: Upper limit: +15, Lower limit: 0
- **November**: Upper limit: +10, Lower limit: -5
- **December**: Upper limit: 0, Lower limit: -25

### Precipitation
Precipitation has three categories: sunny, cloudy, or precipitation (rain/snow; rain if temperature ≥ 0, snow if temperature < 0). The type of precipitation will be chosen with specific probabilities for each month:

- **January**: Sunny – 30%, Snow – 40%, Cloudy – 30%
- **February**: Sunny – 20%, Snow/Rain – 40%, Cloudy – 40%
- **March**: Sunny – 25%, Snow/Rain – 35%, Cloudy – 40%
- **April**: Sunny – 34%, Rain – 33%, Cloudy – 33%
- **May**: Sunny – 40%, Rain – 30%, Cloudy – 30%
- **June**: Sunny – 40%, Rain – 20%, Cloudy – 40%
- **July**: Sunny – 50%, Rain – 15%, Cloudy – 35%
- **August**: Sunny – 40%, Rain – 25%, Cloudy – 35%
- **September**: Sunny – 30%, Rain – 25%, Cloudy – 45%
- **October**: Sunny – 25%, Snow/Rain – 35%, Cloudy – 40%
- **November**: Sunny – 20%, Snow/Rain – 50%, Cloudy – 30%
- **December**: Sunny – 30%, Snow – 30%, Cloudy – 40%

### Special Weather Scenarios
The probabilities change under the following conditions:

- If it is sunny for 5 days in a row, the next day **cannot** be sunny. 2/3 of the probability for sun shifts to cloudy, and the rest to rain/snow.
- If it is cloudy for 5 days in a row, the next day **cannot** be cloudy. Half of the probability for cloudy shifts to sunny, and the other half to rain/snow.
- If there is rain/snow for 5 days in a row, the next day **cannot** have precipitation. 2/3 of the probability for rain/snow shifts to cloudy, and the rest to sunny.

### Event System

Events now have probabilities that depend on both temperature and weather. The chance of an event occurring will be checked every 30 minutes of player gameplay. If an event is triggered, it will appear to the player. After the event ends, there will be a cooldown (which continues even if the player is offline) until the next occurrence of the same event. Some events have durations, while others are removed in special ways.

Some events have a unique system, described individually.

---

## Event List with Probabilities

### Drought
Reduces crop income by half. To remove it, players must collect water in a bucket and give it to each NPC from whom crops were bought.  
**Chance**: 5% at 0°C and cloudy weather.  
Temperature increase of 5°C raises the chance by 1% (e.g., 6% at +5 to +9°C, 7% at +10 to +14°C, etc.).  
Sunny weather increases the chance by 1.5 times (e.g., 5 x 1.5% at 0 to +4°C).  
Rain reduces the chance to zero.  
Below 0°C, the chance is zero.  
**Cooldown**: 8 in-game days.

### Blooming
Doubles crop income.  
**Chance**: 6% at 0°C and cloudy weather.  
Temperature increase of 5°C raises the chance by 1% (e.g., 7% at +5 to +9°C).  
Sunny weather increases the chance by 1.25 times.  
Rain reduces the chance by 4 times.  
Below 0°C, the chance is zero.  
**Cooldown**: 8 in-game days.  
**Duration**: 2 in-game hours to 1 in-game day.

### Morning Dew
Triples grass income.  
Special Condition: If triggered, it occurs randomly between 4:00 and 11:00.  
**Chance**: 3% at 0°C and cloudy weather.  
Temperature increase of 5°C up to +10 to +14°C raises the chance by 3%.  
At higher temperatures, the chance decreases by 2%.  
Above +30°C, the chance is zero.  
Below 0°C, the chance is zero.  
Sunny weather reduces the chance by half.  
Rain increases the chance by double.  
**Cooldown**: 7 in-game days.  
**Duration**: 4 to 12 in-game hours.

### Dirty
Removes passive income. To remove it, the player must take a shower in their house.  
**Chance**: 10% at 0°C and cloudy weather.  
Temperature increase of 5°C reduces the chance by 1%.  
Below 0°C, the chance is zero.  
Sunny weather reduces the chance by half.  
Rain increases the chance by 1.5 times.  
**Cooldown**: 6 in-game days.

### Drowning
Removes passive income. This event counters the "Dirty" event, triggered if the player spends too long in the shower.  
**Chance**: Checked every second when the player stands in the shower:  
- 30-45 seconds: 10%
- 45-60 seconds: 15%
- 60-120 seconds: 20%
- 120-180 seconds: 25%
- 180+ seconds: 100%

The event is removed when the player exits the shower, with the same probabilities.  
**No cooldown.**

### Bustle
- **Effect**: Doubles animal product production.
- **Drop Chance**: 10% at +5°C. For every 5°C increase or decrease from +5°C, the chance decreases by 2%.
- **Weather Dependence**: None.
- **Zero Chance**: Above +25°C or below -15°C.
- **Cooldown**: 7 in-game days.
- **Duration**: From 4 in-game hours to 18 in-game hours.

### Hunger Strike
- **Effect**: Halves animal product production.
- **Drop Chance**: 8%.
- **Weather Dependence**: None.
- **How to Remove**: Players must collect food from the Mayor and deliver it to each NPC from whom they have purchased animals. The bowl empties after feeding one NPC, so players need to return to the Mayor for more food after each delivery.
- **Cooldown**: 6 in-game days.

### Flu
- **Effect**: Disables passive income.
- **How to Remove**: Spend 4 in-game hours inside the player's house.
- **Drop Chance**: 5% at -1°C and cloudy weather. Every 5°C decrease increases the chance by 1%.
- **Zero Chance**: Temperature ≥ 0°C.
- **Modifiers**: Sunny weather halves the chance. Snow increases the chance by 1.5x.
- **Cooldown**: 8 in-game days.

### Claustrophobia
- **Effect**: Disables passive income. Counter to the "Flu" event. Triggers if the player stays indoors for too long.
- **Special Event**: The following probabilities are checked every second while the player is inside:
  - 30-45 seconds: 10%
  - 45-60 seconds: 15%
  - 60-120 seconds: 20%
  - 120-180 seconds: 25%
  - 180+ seconds: 100%
- **How to Remove**: The same probabilities apply when the player exits the house.
- **Cooldown**: None.

### Taxation
- **Special Event**: Independent of weather. Occurs once every 30 in-game days.
- **Effect**: The Mayor demands 40% of the player's balance. During the event, players cannot make purchases from NPCs, and NPCs will not interact with the player.

### Hour of Reckoning
- **Special Event**: Independent of weather.
- **Effect**: The Mayor demands 15 minutes' worth of the player's passive income. During the event, players cannot make purchases from NPCs, and NPCs will not interact with the player.
- **Drop Chance**: 7%.
- **Cooldown**: 8 in-game days.

### Productivity
- **Effect**: Speeds up all production and processing (except for initial animal products, which are affected by the "Bustle" event) by 2x.
- **Drop Chance**: 10% at -5°C to +15°C and cloudy weather. For every 5°C increase or decrease from these temperatures, the chance decreases by 2% (no chance at -30°C).
- **Modifiers**: Sunlight has no effect on the chance, while rain/snow halves it.
- **Cooldown**: 8 in-game days.
- **Duration**: From 2 in-game hours to 12 in-game hours.

### Strike
- **Effect**: Slows down all production and processing (except for initial animal products, which are affected by the "Hunger Strike" event) by 2x.
- **How to Remove**: Players must speak to NPCs in production buildings in a randomly assigned order. Talking to an NPC out of order results in a refusal to interact.
- **Drop Chance**: 4% at -5°C to +15°C and cloudy weather. Every 5°C increase or decrease from these temperatures increases the chance by 1%.
- **Modifiers**: Sunlight reduces the chance by 1.5x if the temperature is below +25°C, but doubles the chance at temperatures ≥ +25°C. Rain/snow increases the chance by 1.5x.
- **Cooldown**: 7 in-game days.

### Barrel Leak
- **Effect**: Barrels near crops empty, and players cannot refill them.
- **How to Remove**: Use a wrench on barrels in all purchased crop fields.
- **Drop Chance**: 6%.
- **Weather Dependence**: None.
- **Cooldown**: 8 in-game days.

### Mushroom Rain
- **Effect**: Doubles passive income.
- **Drop Chance**: 7% in precipitation and 0°C. Every 5°C increase raises the chance by 1%.
- **Zero Chance**: Temperatures below 0°C and during sunny/cloudy weather.
- **Cooldown**: 8 in-game days.
- **Duration**: From 2 in-game hours to 1 in-game day.

### Pond Pollution
- **Fishing Event**: Increases the chance of catching trash by 3x (no effect from donations).
- **Drop Chance**: 5% in cloudy weather and 0°C. Every 5°C increase raises the chance by 1%.
- **Modifiers**: Precipitation doubles the chance, while sunny weather halves it.
- **Zero Chance**: Below 0°C.
- **Cooldown**: 6 in-game days.
- **Duration**: From 2 in-game hours to 6 in-game hours.

### Fishing Dexterity
- **Fishing Event**: Players catch 2 fish per cast.
- **Drop Chance**: 4% at 0°C and cloudy weather. Every 5°C increase raises the chance by 2%.
- **Modifiers**: Sunny weather increases the chance by 1.5x. Precipitation halves the chance.
- **Zero Chance**: Below 0°C.
- **Cooldown**: 7 in-game days.
- **Duration**: From 2 in-game hours to 6 in-game hours.

### Heavy Lifting
- **Effect**: Players move items twice as fast (the load-carrying speed penalty is halved).
- **Drop Chance**: 8% at 0°C and cloudy weather. Every 5°C decrease reduces the chance by 1%, while every 5°C increase up to +20-+24°C raises the chance by 1%. After +25°C, every 5°C increase reduces the chance by 2%.
- **Modifiers**: Sunny weather increases the chance by 1.5x up to +20°C, but reduces the chance by 2x above +25°C. Precipitation halves the chance.
- **Cooldown**: 8 in-game days.
- **Duration**: From 2 in-game hours to 8 in-game hours.

### Nightmares
- **Halloween Event**: Disables income, production, processing, and export. To remove the event, players must "play dead" to receive a "drowned" status and then remove it.
- **Weather Dependence**: None.
- **Drop Chance**: 8% during the "Halloween" holiday. Can trigger once per Halloween event.

The rest of the events follow a similar detailed structure, adjusting for chance, cooldowns, and specific weather conditions. Each event is designed to interact with both temperature and precipitation in meaningful ways.

### New Weather Component: Wind

#### Wind Characteristics
- **Direction**: 8 directions (North, South, West, East, Northwest, Northeast, Southwest, Southeast). Technically, there is a ninth direction representing calmness (0 m/s wind speed).
- **Speed**: Ranges from 0 m/s to 20 m/s.
- **Daily Update**: At the start of each day, new wind speed and direction are set, alongside temperature and precipitation. 
- **Direction Selection**: The wind direction is chosen randomly, with the restriction that the same direction cannot occur for more than three consecutive days.
- **Speed Variation**: The wind speed is also set randomly within its range, with the restriction that it cannot change by more than 10 m/s from the previous day's value.

#### Player Speed Dependency on Wind
- **With Wind Direction**: If the player moves in the direction of the wind, their speed increases by \( \frac{x}{10} \) (where \( x \) is the wind speed in m/s).
- **45-Degree Angle**: If the player moves at a 45-degree angle to the wind direction, their speed increases by \( \frac{x \sqrt{2}}{20} \).
- **Perpendicular**: If the player moves perpendicular to the wind direction, their speed remains unchanged.
- **135-Degree Angle**: If the player moves at a 135-degree angle to the wind direction, their speed decreases by \( \frac{x \sqrt{2}}{20} \).
- **Against Wind Direction**: If the player moves against the wind direction, their speed decreases by \( \frac{x}{10} \).

### Event Drop Chance Updates
- The chance of event occurrence is checked every 10 minutes of gameplay instead of every 30 minutes.
- The cooldowns for event occurrences have been reduced as follows:

#### Cooldowns
- **Drought**: 2 in-game days.
- **Blooming**: 2 in-game days.
- **Morning Dew**: 1.5 in-game days.
- **Dirtiness**: 2 in-game days.
- **Bustle**: 3 in-game days.
- **Hunger Strike**: 2 in-game days.
- **Flu**: 5 in-game days.
- **Taxation**: Occurs once every 5 real-life days.
- **Hour of Reckoning**: 3 in-game days.
- **Productivity**: 3 in-game days.
- **Strike**: 3 in-game days.
- **Barrel Leak**: 4 in-game days.
- **Mushroom Rain**: 2 in-game days.
- **Pond Pollution**: 4 in-game days.
- **Fishing Dexterity**: 4 in-game days.
- **Heavy Lifting**: 3 in-game days.

## Locations

### General Principles

On the farm, there will be three sub-locations, each with its NPCs, active tasks, and questlines. 

To access the NPCs in a new location, the player will need to complete the questline in the previous one.

Additionally, at the center of the map, there will be a stand with a farm map that players can use for orientation.

### South Part

**NPC: Grandma Lyuda**

Active Tasks: Grass cutting, Tree cutting, Mining.

Crops and productions list:

1) Wheat → Bread
2) Potato → Baked potato
3) Carrot → Carrot juice
4) Sugar cane → Sugar
5) Tea leaf → Tea
6) Onion → Onion rings
7) Grape → Wine
8) Raspberry → Raspberry jam
9) Cotton → Cotton fiber
10) Strawberry → Strawberry jam

### West Part

**NPC: Mihalych**

Active tasks: Fishing (with a dedicated NPC on this location - Fisherman Henry)

Crops and production list:

1) Tulip → Tulip Bouquet
2) Flax → Yarn
3) Corn → Corn Chips
4) Sunflower → Sunflower Oil
5) Cocoa Beans → Cocoa Powder
6) Hops → Premium Hops
7) Rose → Rose Bouquet
8) Tomato → Ketchup
9) Peony → Peony Bouquet
10) Currant → Currant Juice

### East Part

**NPC: Koryagin**

Active tasks: Cargo hauling

List of **Trees**, their Fruits (products) and productions:

**Tree** - a structure that functions like a plant. Generates passive income. 

After purchasing the eighth tree, products are delivered to the warehouse.

1) Cinnamon Tree (cinnamon) → Ground Cinnamon
2) Apple Tree (apple) + sugar + dough + egg → Apple Charlotte
3) Peach Tree (peach) + sugar + ground cinnamon + milk → Peach Smoothie
4) Pear Tree (pear) + dough + cheese + pork → Pear Pizza
5) Orange Tree (orange) + ground cinnamon + dough + sugar → Orange Cake

### North Part

The northern part will not have plants, animals, or trees.

It consists of a forest for lumberjacking and mines in the forest for mining.

Additionally, in the forest, there will be a lake where fish will appear depending on the amount of fish caught during fishing.

## Animals

Animals, much like plants, generate passive income and produce products that can be utilized later in production structures.

1) Chicken → Egg
2) Rabbit → Rabbit hide
3) Sheep → Wool
4) Pig → Pork
5) Cow → Milk
6) Mushroom cow → Mushroom
7) Bee → Honey
   
## Production recipes

1) Wheat → Dough (Bakery)
2) Potato → Baked Potato (Bakery)
3) Carrot → Carrot Juice (Bar)
4) Sugar Cane → Sugar (Factory)
5) Tea Leaf → Tea (Café)
6) Onion → Onion Rings (Bar)
7) Grape → Wine (Bar)
8) Raspberry → Raspberry Jam (Factory)
9) Cotton → Cotton Fiber (Sewing Workshop)
10) Strawberry → Strawberry Jam (Factory)
11) Tulip → Tulip Bouquet (Flower Shop)
12) Flax → Yarn (Sewing Workshop)
13) Corn → Corn Chips (Bar)
14) Sunflower → Sunflower Oil (Factory)
15) Cocoa Beans → Cocoa Powder (Factory)
16) Hops → Premium Hops (Bar)
17) Rose → Rose Bouquet (Flower Shop)
18) Tomato → Ketchup (Café)
19) Peony → Peony Bouquet (Flower Shop)
20) Currant → Currant Juice (Bar)
21) Cinnamon → Ground Cinnamon (Café)
22) Apple + Sugar + Dough + Egg → Apple Charlotte (Bakery)
23) Peach + Sugar + Ground Cinnamon + Milk → Peach Smoothie (Bar)
24) Pear + Dough + Cheese + Pork → Pear Pizza (Café)
25) Orange + Ground Cinnamon + Dough + Sugar → Orange Cake (Bakery)
26) Rose Bouquet + Tea Leaf → Hibiscus Tea (Café)
27) Milk → Cheese (Factory)
28) Sunflower Oil + Potato → Fried Potato (Bar)
29) Wheat + Premium Hops → Beer (Bar)
30) Cocoa Powder + Sugar → Chocolate (Factory)
31) Corn + Wheat → Corn Flatbread (Café)
32) Pork + Tomatoes + Baked Potato + Cheese → French-Style Pork (Café)
33) Wine + Rose Bouquet + French-Style Pork → Romantic Dinner (Café)
34) Corn Chips + Beer + Ketchup + Fried Potato → Soul of the Party (Bar)
35) Milk + Sugar → Yogurt (Factory)
36) Apple + Strawberry + Peach + Yogurt → Fruit Salad (Café)
37) Fruit Salad + Currant Juice → Fruit Delight (Café)
38) Dough + Sugar → Pancake (Bakery)
39) Dough → Bread (Bakery)
40) Bread + Raspberry Jam → Bread with Jam (Bakery)
41) Pancake + Carrot Juice + Bread with Jam → Champion's Breakfast (Café)
42) Dough + Sugar + Milk + Honey → Honey Cake (Bakery)
43) Dough + Chocolate → Chocolate Cookies (Bakery)
44) Tea + Honey Cake + Chocolate Cookies → Cozy Teatime (Bar)
45) Rabbit Hide + Cotton Fiber → Fur Coat (Sewing Workshop)
46) Wool + Yarn → Sweater (Sewing Workshop)
47) Fur Coat + Sweater → Winter Fashion (Sewing Workshop)
48) Ketchup + Tomato + Corn Flatbread + Mushroom + Pork + Onion Rings → Shawarma (Bar)
49) Mushroom → Braised Mushrooms (Factory)
50) Strawberry Jam + Dough → Bun with Jam (Bakery)
51) Egg + Milk + Sugar + Honey → Chak-Chak (Bakery)
52) Honey + Premium Hops + Ground Cinnamon → Mead (Bar)

## Jewelry recipes (Crafting in the workshop)

1) Iron Ingot → Iron Chain
2) Copper Ingot → Copper Bracelet
3) Silver Ingot → Silver Brooch
4) Silver Ingot → Silver Necklace
5) Gold Ingot → Gold Earrings
6) Gold Ingot → Gold Ring
7) Amethyst + Silver Brooch → Amethyst Brooch
8) Amethyst + Gold Ring → Amethyst Ring
9) Platinum Ingot → Platinum Pendant
10) Platinum Ingot → Platinum Ring
11) Emerald + Platinum Pendant → Emerald Pendant
12) Diamond + Platinum Ring → Diamond Ring

## Buildings

### Production Buildings

#### Warehouse (available from the beginning of the game):

A building that will be responsible for the menu that the player currently has through the inventory. 

The menu will be available only through the building itself.

Initially level 1, upgradeable to level 5.

##### Product limits per levels:
- Level 1: 25
- Level 2: 50
- Level 3: 75
- Level 4: 100
- Level 5: 200

##### Upgrade time: 
- 1→2 - 20 minutes, 
- 2→3 - 40 minutes, 
- 3→4 - 60 minutes, 
- 4→5 - 90 minutes.

#### Workshop:

A building where players buy blueprints for the construction of future buildings for money. 

Buildings and decorative structures below are built when the purchased blueprint is available, along with the necessary materials!!! 

Also, players upgrade tools there. The workshop itself is built without a blueprint; only materials from active jobs and money are needed. 

Materials for crafting: stone, oak, $5000.

### Blueprint list

**Bakery (Processing Building):**

Materials for crafting: stone, oak.

**Bar (Processing Building):**

Materials for crafting: stone, oak, iron ingot.

**Factory (Processing Building):**

Materials for crafting: iron ingot, stone, copper ingot, birch.

**Cafe (Processing Building):**

Materials for crafting: stone, iron ingot, copper ingot, birch.

**Sewing Workshop (Processing Building):**

Materials for crafting: copper ingot, quartz, stone, birch, spruce.

**Flower Shop (Processing Building):**

Materials for crafting: stone, copper ingot, quartz, spruce, dark oak.

### Decorative buildings

**Well:**

Decorative structure, gives 1.1x to income.

Materials for crafting: stone, oak.

**Golem Statue:**

Decorative structure, gives 1.2x to income.

Materials for crafting: iron ingot, stone.

**Globe:**

Decorative structure, gives 1.3x to income.

Materials for crafting: copper ingot, iron ingot.

**Eternal Flame:**

Decorative structure, gives 1.4x to income.

Materials for crafting: quartz, copper ingot.

**Golden Angel:**

Decorative structure, gives 1.5x to income.

Materials for crafting: gold ingot, quartz.

**King Arthur's Sword:**

Decorative structure, gives 1.6x to income.

Materials for crafting: platinum, gold ingot, iron ingot, stone.

**Tree of Eywa (from the movie "Avatar"):**

Decorative structure, gives 1.7x to income.

Materials for crafting: tropical wood, acacia.

**Colossus of Rhodes:**

Decorative structure, gives 1.8x to income.

Materials for crafting: titanium ingot, platinum, gold ingot.

## Visit to a friend's farm

On the map, there will be a bus with an NPC. 

When the player clicks on the NPC, a menu pops up, and the player enters the nickname of the person they want to visit. 

After that, the player is teleported onto the bus, the screen darkens, and then the player appears on the other person's farm near the bus NPC.

## Items

**Axe (Tree cutting)** - issued immediately.

**Pickaxe (mining)** - issued immediately.

**Fishing rod (fishing)** - Need to be purchased from the workshop

**Phone** - opens a contact list, in which the player selects the desired NPC, and after selection, the corresponding menu opens.

**Farmer's Diary** - 

- A book that stores information about plants, buildings, and animals. 

- All of this is revealed during the game. 

- All information about a crop appears only when the player has acquired that crop. Functions as a mini-wiki.

**Calendar** - Show the date and season

## Holidays

### Winter

#### New Year 

(lasts 8 days, from December 31 to January 7) - a Christmas tree appears in the square. 

Individually for each player, 12 gifts will be placed on their farm. 

From the gifts, three hats can drop, which can be obtained and worn only during this holiday (cannot be repeated), as well as passive income ranging from 3 to 10 minutes in the form of a monetary amount.

NPCs on the farm will wear Christmas hats.

**Christmas hats from gifts:**

**Santa's Hat** (works only on New Year's, i.e., the hat will not work outside of the holiday) - immunity to the flu + flight + Christmas hat.

**Grinch Mask** (works only on New Year's) - after wearing it, 3 more gifts spawn on the farm (was 12 in total, becomes 15).

**Ice Crown** (works only on New Year's) - the "Blizzard" event avoids the player, the chance of hoarfrost increases by 1.5 times.

From one of the 12 gifts, a player will randomly receive a Christmas ornament, which they can place in the gift block under the tree. 

Ornaments will provide a global booster during this event: every 10 ornaments increase the global income booster by 0.1x (1.1x booster at 10 ornaments, 1.2x at 20, etc.), global production speed increases by +2%, and global crop export speed increases by +2%. 

The maximum number of ornaments that can be placed in the gift block is 100.

#### Valentine's Day 

(February 14, three days) - a big heart appears in the square <3. 

Players can give three Valentines, write something cute <333.

If you give someone a Valentine, and they give it back to you, you can earn income for your farm by being on the "lover's" farm during the holiday.

#### Maslenitsa 

(February 25 - March 3) - a scarecrow appears in the square. Players will receive 1.2x income, and production speed will increase by +10% if the player is in the square. 

Pancakes from their farm will be sold for twice the price.

Pancakes will also be sold in the square. The cost of one pancake is 45 minutes of passive income for the player. 

The maximum number of pancakes a player can buy is 5. The player can give a pancake to an NPC with plants/trees, an NPC with an animal, or an NPC on a building on their farm. 

If the player gives a pancake to an NPC with a plant/tree, the income from the crop will double; 

if the pancake is received by an NPC with an animal, the production speed will increase by 1.25 times; if the player gives a pancake to an NPC with a building, +25% to the speed of exporting crops and processing. 

During the holiday, it is also not possible to sell meat products (pork, pear pizza, French-style pork, romantic dinner, shawarma).

### Spring

#### May Day 

(May 1, three days) - while the player is actively working, flowering occurs (flowering fades if the player is not actively working for 1 minute). 

Cargo transfer, grass, and fishing give 1.5 times more income. 

An NPC with barbecues appears in the square, which can speed up the production of meat production by 2 times

(click on the barbecue, and a menu appears where you can make meat production (pear pizza, French-style pork, romantic dinner, shawarma) for the time that is twice less in a building on the farm).

During the holiday, introduce temporary leaderboards for the caught fish (fishing), carried cargoes (cargo hauling), and broken grass (grass). 

According to these three leaderboards, boosters will be given on the next day after the holiday (May 4, 1 real hour) as follows:
- Top-1 - x3 to caught fish (fishing top), x3 to cargo (cargo hauling top), x3 to grass (grass top).
- Top-2 - x2 to fish, cargo, and grass (similarly).
- Top-3 - x1.5 to fish, cargo, and grass (similarly).

### Summer

#### Farm Day 

A big cake appears in the square. During this holiday, negative events will not be imposed on players.

The processing speed of products, the export of crops, and the production of animal products increase by 20%.

Honey cake will be sold for 1.5 times the price.

NPCs on the farm will wear festive hats.

During mining and logging, players have a chance to receive a **gift**. 

They must bring this **gift** to the cake in the square and click on it with the gift. After clicking with the gift on the cake, one candle appears. 

The maximum number of candles on the cake can be 100. Every 10 candles add +0.05x to the global booster (1.05x for 10 candles, 1.1x for 20, 1.5x for 100).

Players can wear hats of a certain color through an NPC in the square (opens a menu with hats of different colors, the player chooses their own).

### Autumn

Halloween 

(October 31, seven days) - a large pumpkin appears in the square.
The "Nightmares" event may occur, which resets income, stops production, processing, and export. 

It can be removed by "playing dead" and getting a drowned event, and then removing it.

Players receive 10 candies and a basket in their inventory. 

Players can poke another player once with a candy to give 1 candy (if you try to poke a player with candy again, they will refuse) into the basket of another player, and the basket will count the number of candies. 

From this, players will receive a local boost +0.1x from every 10th candy in their basket (1.1x booster with 10 candies, 1.2x with 20, etc.), local production speed increases by +2%, and local crop export speed increases by +2%. 

The maximum number of candies a player can collect in the basket is 100. When a player gives a candy, they get +2% to the processing speed (give all 10 candies - get +20% to the speed).

#### 8. Lumberjack Day (September 21, lasts 3 days)
On the Square, a **lumberjack NPC** appears with a house.

- Players do not experience fatigue while chopping wood.
- Tool upgrades are twice as fast.

The player's task is to bring as much wood as possible to the NPC. There are **5 stages**:
1. 125 wood
2. 250 wood
3. 500 wood
4. 1250 wood
5. 2500 wood

With each stage, the duration of positive effects on the farm increases by **15%, 25%, 35%, 45%, 60%** until the end of the event. After the event ends, all buffs are removed, but for the next **7 in-game days**, a buff is given that increases the chance of a positive event based on the player's progress:
- 5%, 10%, 15%, 20%, 25%.

---

#### Miner Day (August 2, lasts 3 days)
A **decorative mine** and a **miner NPC** appear on the Square.

- Players do not experience fatigue while mining with a pickaxe.
- Tool upgrades are twice as fast.

The miner allows trading of ores (all except stone) at the following exchange rates:
- **Stone to ore:** 10:1 (e.g., 10 stone → 1 gold ore)
- **Ore to stone:** 1:10 (e.g., 1 gold ore → 10 stone)
- **Ore to ore:** 6:1 (e.g., 6 iron ore → 1 gold ore)

**Important:** Both types of ores must be available to the player.

When breaking ores, there is a **5-10% chance** to receive a shard of the same ore. When 10 shards are collected, they automatically turn into a finished metal.

- Jewelry crafting is **20% faster** during the event.
- Building construction requires **10% fewer resources**.

---

#### Fisherman Day (July 9, lasts 5 days)
A **statue of a fisherman** appears on the Square.

- No trash is caught during fishing.
- Two new catches are added: 
  - **Golden Fish** (0.5% chance), which grants **2x fish** for the rest of the event.
  - **Guardian** (0.2% chance), which becomes a **mount** for the player.

**Rewards based on the number of fish species caught during the event:**
- **6-15 species:** 1.2x income from fish and fish processing sales for **2 real hours** after the event.
- **16-25 species:** 1.4x income for **2 real hours**.
- **26-35 species:** 1.6x income for **2 real hours**.
- **36-45 species:** 1.8x income for **2 real hours**.
- **46-50 species:** 2x income for **2 real hours**.


# Green Peaks Location

The farm will have a unified location that combines active tasks, the square, and all its functionalities from the previous wipe. The name of this location: **Green Peaks**.

## The Square
The Square is a gathering place for players. During winter, it will feature a hockey field, while at other times, it will be replaced by a football field. Players can play hockey/football (like the DMS in the hub). The square will have **love-seats**, where two players can sit together. There will also be mini-games for players to enjoy and pass the time.

### List of Games on the Square:
- **Checkers** (1vs1)
- **Whack-a-Mole** (Top by number of moles hit per game)
- **Parkour** (Top by time, flight disabled in the zone)
- **Dropper** (Flight disabled in the zone)
- **Races around the square** (4 players)
- **Tic-tac-toe**

In addition, the player will handle cargo transfers on the Square, as the truck and storage warehouses will be located there. The square's layout remains unchanged from the previous wipe.

## Resource Gathering and Mining

The old locations for wood and ore gathering will be replaced by a **common location**, where every block is **local** to each player. This means that even if a block has been broken by one player, another player can still gather it, as blocks are individual to each player.

### Green Peaks Sub-Zones for Wood Gathering:
1. **Level 0** – The Square
2. **Level 1** – Oak Meadow (oak + grass field)
3. **Level 2** – Birch Forest (birch)
4. **Level 3** – Spruce Thicket (spruce)
5. **Level 4** – Dark Forest (dark oak)
6. **Level 5** – Sandy Valley (acacia)
7. **Level 6** – Tropical Hill (jungle trees)

### Mines
The mines will no longer be scattered across locations; instead, they will descend deeper with each level.

1. **Level 1** – Coal Mine (Materials: stone, coal)
2. **Level 2** – Forgotten Mine (unlocks at level 10, Materials: iron, copper)
3. **Level 3** – Silver Veins (unlocks at level 20, Materials: silver, quartz)
4. **Level 4** – Shiny Minerals (unlocks at level 30, Materials: gold, amethyst)
5. **Level 5** – Underground Klondike (unlocks at level 40, Materials: platinum, emerald)
6. **Level 6** – Lava Archipelago (unlocks at level 50, Materials: titanium, diamond, obsidian)

## Fishing Lakes in Green Peaks

Each sub-zone of Green Peaks, except for the Square, features a lake for fishing.

1. **Lake in Oak Meadow**  
   Catch: anchovy, sprat, smelt, sardine, herring, crucian carp, perch, ruffe

2. **Lake in Birch Forest** (unlocks at level 10)  
   Catch: mackerel, pollock, roach, flounder, tench, roach, omul, white-eye

3. **Lake in Spruce Thicket** (unlocks at level 20)  
   Catch: navaga, blue bream, rudd, pink salmon, carp, ide, common carp, bream

4. **Lake in Dark Forest** (unlocks at level 30)  
   Catch: coho salmon, pike perch, pike, eel, salmon, burbot, chum salmon, pufferfish

5. **Lake in Sandy Valley** (unlocks at level 40)  
   Catch: grass carp, black carp, snakehead, halibut, mackerel, catfish, pollock, sea bass

6. **Lake in Tropical Hill** (unlocks at level 50)  
   Catch: sturgeon, anglerfish, ling, silver carp, paddlefish, swordfish, beluga, tuna


## Daily Login

- Day 1 - Active tasks modifier 1.25x for 1 hour
- Day 2 - Amount of money thats equals to the passsive income for 5 minutes
- Day 3 - Haste for digging for 1 hour +10%
- Day 4 - Plant production speed booster for 1 hour +25%
- Day 5 - Amount of money thats equals to the passsive income for 20 minutes
- Day 6 - Blossoming event for 30 minutes
- Day 7 - Production speed booster for 1 hour +50%

## Visual and Sound effects

### Visual effects

- Smoke
- Falling leaves
- Lying leaves (on blocks near trees)
- Glowing particles from ores (regular ore-colored particles)
- Snow (falling)
- Footprints in the snow (when walked upon with a certain chance)
- Fish animation (swimming in the player's farm lake)
- Swaying grass
- Butterflies (flying across the map except in winter)
- Bus exhaust fumes
- Dew on the grass
- Frost on windows
- Grass in frost
- Tree falling animation
- Conveyor animation at the factory (conveyor moves products when production is active at the factory)
- Light from the Christmas tree (glowing star on the Christmas tree)

### Sound effects

- Sound of a positive event
- Sound of a negative event
- Sound of lifting and lowering cargo (creaking)
- Musical themes for each location
- Musical theme for each holiday (plays only in the square)
- Splash of water when casting and retracting the fishing rod, and when interacting with water, as well as when drawing water from the well
- Campfire crackling sound (also used in the bakery and cafe)
- Chicken clucking near the chickens
- Crickets at night
- Bleating near the sheep
- Mooing near the cows (including mushroom cows)
- Buzzing of bees
- Oinking near the pigs
- Sound of hitting metal in the workshop
- Sound of the conveyor at the factory
- Sound of glasses clinking every 10 seconds in the bar
- Sound of a sewing machine in the sewing workshop
- Bus horn when approaching it
- Bus engine after the player has chosen whom to visit
- Phone beeps when opening the phone
- Sound of a falling tree
- Echo in the mine (breaking blocks, footsteps)
- Sound of flipping pages in the diary
- Sound of an overflowing backpack when the backpack is full
- SMS sound (randomly when an active quest is ongoing)
- Sound of feeding an animal
- Coughing during the flu

## NPC Dialogs

### Garden beds NPC Dialogs

| NPC Name     | Plant/Tree | First purchase | Successfull Purchase | Insufficient funds | Full garden bed
| :------------- | :---------- | :---------------------- | :----------------------------- | :------------------------ | :-----------------------
| Konstantin | Wheat | Welcome to our farm! You'll enjoy it here! | Did you know that wheat was one of the first domesticated grains? | In our region, all crops are bought with money. It's simple: no money, no crops. | We've planted all the wheat fields; there's no more space! |
| Luka | Potato | Finally, you've gathered enough money to get in touch with me! I'm sure we'll find common ground. | My potatoes are simply a sight to behold, aren't they? | If I sell the crop for such an amount, my father will punish me! | A true lover of potatoes, just like me! Nowhere left to plant them.. |
| Mark | Carrot | Another plant will help you see better than what you'll be dealing with here. | I see that you're one step closer to success! Keep up the momentum. | You lack the cash to deal with me at the moment. | I see that you appreciate my carrots, but even they have their limit. | 
| Victor | Sugar Cane | Congratulations on the purchase, my sweet! Whether more awaits you, there's plenty of space for canes! | Thank you for another purchase, sweetie! | I'm sorry, but you'll have to spend a little bit more | Sugar cane has taken over our beds, and soon it will take over the whole world! |
| Xe Chan Mi | Tea Leaf | Wise decision, young one! Tea is the key to any success. | You can't buy wisdom, but purchasing this tea leaf will bring peace to your soul. | My tea leaves are not acquired so easily, young one. | Too much tea can lead you out of spiritual balance... |
| Crybaby | Onion | You decided to buy my onions? What a joy! I hope I won't burst into tears... | Tears of joy well up every time you make a purchase from me! | I'm sorry, but your balance brings me to tears. | Don't take any more, or I won't be able to stop crying. | 
| Peter | Grape | You managed to gather some money after all! Well, take it, but from now on, I'll sell it at a higher price. | Now, this is an interesting deal. Now you have one more grape. | No one will let you taste it for such an amount! | I'm out of grapes, and you have no space for them, so that's it. |
| Delio | Raspberry | Appreciate the dearly priced berry. I don't choose people, but I think you'll manage. | I love raspberries because they make me happy. | Such a valuable product for these pennies? How old are you? You should study math; look at the price... Farewell. | Your supplies have run out. Appreciate what you have, as it may not be there. Well, I'm off to hibernation. Happy collecting. |
| Frenchie | Cotton | With the first purchase, my friend! Trust me, cotton will come in handy. | Cotton products are often soft and fluffy. They're somewhat like me. | Not much green in the wallet won't add vegetation to the fields. | From now on, it's a cotton paradise! |
| Arthur | Strawberry | Wonderful, now there's another berry on the farm! | Congratulations on another purchase. Strawberries are amazing; honestly, you won't regret it! | Return, return your money, and come back when you've saved up the amount I need. | Unfortunately, there's no more space for strawberries. |
| Ellen | Tulip | Flowers bring joy to everyone! With the first tulip, I hope you'll have enough for a bouquet in the future. | Tulips are my favorite flowers! It's worth spending money on such beauty! | Flowers don't come cheap these days; save up some more. | There's no more space for such magical beauty! |
| Leon | Flax | Everyone is curious these days, whether they named me after flax or flax after me. Be that as it may, congratulations on the new crop! | Buy more flax from Leon! | You can't deceive Leonchik; flax is more expensive. | The whole field is in flax... flax? Or flax? |
| Larry | Corn | Finally, you've bought your first ear of corn! Corn always reminds me of summer beaches... | Corn is perhaps the only crop utterly incapable of surviving without human intervention. | They don't even sell it for this much on the beach! | There's enough corn on the farm for everyone; no need to plant more. |
| Sunny | Sunflower | Hello, sunshine! This will be my first of many sales, so come back as soon as you can. | A sunny flower for a sunny smile! Well, and for a good sum. | Sunshine, you can't buy my sunflowers for this amount; you need to save up more. | The sunny meadow is completely filled. |
| Mr. Bean | Cacao Beans | Hi, I'm Bean! In these parts, only cacao bean bushes are sold, but you can make a decent profit from them too. | Bought beans from Bean, plus good karma! | Bean sells his beans at a higher price, everyone knows that. | So many beans bought, where will Bean get more? |
| Hugo | Hops | Thank you for the purchase! Hops are a crucial crop for beer production. Just don't overdo it. | Thanks for buying my hops again. I hope it meets your expectations and helps create excellent beer! Feel free to reach out anytime. | Unfortunately, you don't have enough funds to buy so much hops. Maybe next time? | I'm sorry, but at the moment, I can't sell you more hops. I need to keep some of the harvest for my own plantations. |
| Catherine | Rose | Congratulations on the purchase of your first rose! And remember, the pink empire needs your care! | From roses, you can make both tea and wine! And all our thorny empire will go to rose oil... | You can't even buy a dandelion for this amount. | Now there's a rose for everyone! |
| Sergio | Tomato | Finally, the day of tomatoes has come to this farm, amigo! | If you're interested, amigo, you're buying Catalan tomatoes, I guarantee. | In our region, around La Sima, such amusing proposals were punished. | Amigo, the garden is full of little tomatoes; move on! |
| Aly | Peony | I hope that acquiring a peony made you a little happier. | Seeing a smile on your face when buying a peony—that's why I'm here. | I don't like to talk about problems directly, but money... you don't have any. How do you plan to buy peonies? | This is all you can afford. I hope the peonies made you a little happier, as I intended! |
| Andrew | Currant | Welcome to my berry paradise! I hope we'll see each other more often. | What a joy that you continue to buy currants from me! In general, I love all kinds of berries. | For this amount, you should head to the forest to gather. | Having so much currant on the farm is already happiness; you definitely don't need more! |
| Tommy | Cinnamon | The farm is growing, flourishing, which means it's time to move on to trees! | Of course, we'll plant another tree, my little bun. | Sweet tooth, you can't buy trees on our farm just like that; you need to save up more. | All my territory is planted; it's time to plant something else. |
| Newton | Apple Tree | An apple on my head, and it's my first customer on this farm in many years! | Something is drawing you here, isn't it? | May an apple fall on you if you offer such a small amount again. | The strength is in our apple trees, but strength must be moderate, so I can't sell you more. |
| Natalie | Peach | You had enough for the first peach, I'm glad! | We sell the juiciest peaches on our farm! | You can take offense at such offers; it would be worth saving up a bit more... | There's no more space for peaches, unfortunately. |
| Mike | Pear | I knew you'd buy a pear! Who doesn't love pears, right? | The more trees, the more profit. Both for me and for you. | The pear is hanging, and you can't buy it. What's this? Right: not enough funds, buddy. | Now everyone can enjoy my delicious pears, hooray! |
| Alex | Orange | Oranges on our farm? Let's experiment. | People demand more citrus—people will get more citrus. | With such a balance, you can't demand anything from me, buddy. | The experiment was successful; the farm is now full of oranges. |

### Animal NPC Dialogs
| NPC Name     | Animal | First purchase | Successfull Purchase | Insufficient funds | Full corral
| :------------- | :---------- | :---------------------- | :----------------------------- | :------------------------ | :-----------------------
| Donald | Chicken | Congratulations, you have a new animal on your farm! Now it will be more fun for you. | A new feathered friend has been purchased! | We definitely won't agree on this. Bring more money or forget about feathered friends. | There's no more space for feathered friends. |
| Ivan | Rabbit | Congratulations on the purchase of your first friend! | Another bunny for my bunny! | Bunny, I'm afraid you don't have enough money... | There are too many rabbits on our farm! |
| Mathematician Rill | Sheep | Only the beauty of this sheep can compare to how beautiful mathematics is! | Sheep +1, there won't be any minuses | An interesting sophism: you can't give money, but you get a sheep. Where is the profit coming from? The solution is that I am in minus. | The pastures are filled with sheep! Thanks to them, your profit will grow in geometric progression! |
| Michael | Pig | A wonderful piglet has appeared on your farm, congratulations! | Oh, we have a new member! Another little piggy has joined our pen. | Our pink happiness is worth much more than what you're offering me. | That's enough, or they might start running away! |
| Milka | Cow | Oh, we definitely needed more cows on the farm! M-m-mootiful decision. | And we have an addition! We've been m-m-mooing eagerly for a new friend. | You're m-m-misunderstanding if you think I'll work with anyone for such money. | Moo-moo! Can't hear it? There's no more room for cows. | 
| Mario | Mushroom Cow | It's-a me, Mario! And this is the mushroom cow, my favorite animal! Don't think I'll let you buy such a wonder so cheap again - save up more. | Mamma mia, you're a true mushroom enthusiast, come again! | When things are going bad, there's no use trying to get something from me for free. Work for it, amico! | Mamma mia, I have nothing more to offer you, I'm just a simple plumber! |
| Teddy | Bees | Ouch, a bee stung me! This is your first beehive! Just make sure to come back, one is not enough. | I knew you'd be back. After all, honey is so wonderful, it lures you to spend... | I won't sell it for less! It's a matter of principle, you know. | We harvested the whole apiary! Where do you need more, aren't you afraid? |

### Structures NPC 
| NPC Name     | Structure | Insufficient funds | Successfull purchase | Building already acquired
| :------------- | :---------- | :----------------------------- | :------------------------ | :-----------------------
| Smith | Workshop | These are pennies! Even a novice should have saved up more before trying to buy this from me. | A whole world of possibilities has opened up to you! | - |
| Auntie Gali | Bakery | And what do you expect me to do about it? At most, you can buy a pastry. | Come in here more often; we'll have the finest pastries here! | - |
| Daniel | Bar | Not that I'm a businessman, but with such funds, no proper business can be organized. | Congratulations! Let's celebrate this purchase; a place will appear soon. | - |
| John | Factory | I won't work here if that's all you can offer me. | To work, gentlemen! | - |
| Stephan | Cafe | Even school cafeteria chefs refuse to work for this much. | Come to the opening of our cafe, the best on the whole farm! | - |
| Mika | Sewing Workshop | Go buy yourself a sewing machine for such a pittance. | Come by more often, stylish one! | - |
| Annie | Flower Shop | Is that all? I can only give you a comforting bouquet. | Long live our flower business! | - | 
| Egor | Well | Take a breath, you should have drawn conclusions earlier. I don't see any benefit for myself now, we won't negotiate anymore. | Thanks for the money, now I'm taking it in this wonderful place! | And you laugh, saying, 'This won't be enough for me!' Sorry, little one, it won't work that way. |
| Frank | Golem Statue | No, friend, with such a set of resources, nothing can be erected. | Our farm became much calmer when such a solid hunk appeared! | One such statue is enough for our entire farm; don't overdo it with grandeur. |
| Geo | Globe | Pathetic amount. You can buy a tabletop one for it and spin it until you get bored. | I hope now there won't be any disputes among the locals about whether the Earth is perfectly round? What, meaning slightly flattened at the poles? | I don't see the point of having several such statues. Why didn't you notice something like that on the first one? | 
| Sol | Eternal Flame | Not enough resources for such a great monument, friend. | The right decision, my friend, thank you from the bottom of my heart for this. | One monument here is quite enough. |
| Mercy | Golden Angel | Not enough funds. The purchase is not given easily, but you have every chance to save up more and come back. | Thank you for your contribution to this statue. I am working at the peak of my abilities, everything is fine. | Where to go more? I can't handle it alone. |
| Lancelot | Sword of King Arthur | I see that a person like you is unworthy of such an exquisite monument. | Nice doing business with you, valiant warrior! Your Excalibur will be ready soon. | The sword is already in place and awaits its hero; I require nothing more from you. |
| Neytiri | Tree of Eywa | You lack what is needed. You are a stranger in this territory. | The sacred tree has rooted itself in this land! | The Great Mother preserves the balance of life, just as the balance on these lands. Possess this world anew, and chaos will befall us. |
| Helios | Colossus of Rhodes | You cannot attain the divine dimension until you master all that is necessary! | My respects, mortal! Now this place can truly be called a wonder of light! | My task here is done, our paths diverge from now on. I shall bless this land no more. |

## Textures and icons
### Plants and Trees
- Tea Leaf, 
- Onion, 
- Grape, 
- Raspberry, 
- Cotton, 
- Strawberry, 
- Flax, 
- Corn, 
- Sunflower, 
- Cocoa Beans (Bush), 
- Hops, 
- Tomato, 
- Currant, 
- Cinnamon (Tree Leaves), 
- Apple Tree (Tree Leaves), 
- Peach (Tree Leaves), 
- Pear (Tree Leaves), 
- Orange (Tree Leaves)
### Cargo Hauling
- Cargo Block (available in various variations)
### Mining
- Copper Ore, 
- Copper Ingot, 
- Silver Ore, 
- Silver Ingot, 
- Quartz Ore, 
- Amethyst Ore, 
- Amethyst, 
- Platinum Ore, 
- Platinum Ingot, 
- Titanium Ore, 
- Titanium Ingot
### Animals
- Bee Texture, 
- Beehive Block
### Products Icons
- Dough, Baked Potato, Carrot Juice, Tea Leaf, Tea, Onion, Onion Rings, Grape, Wine, Raspberry, Raspberry Jam, Cotton, Cotton Fiber, Strawberry, Strawberry Jam, 
- Tulip Bouquet, Flax Yarn, Corn, Corn Chips, Sunflower, Sunflower Oil, Cocoa Powder, Hops, Select Hops, Rose Bouquet, Tomato, Ketchup, Peony Bouquet, Currant, Currant Juice, Cinnamon, 
- Ground Cinnamon, Charlotte, Peach, Peach Smoothie, Pear, Cheese, Pear Pizza, Orange, Orange Cake, Hibiscus Tea, Beer, Chocolate, Corn Flatbread, French-Style Pork, 
- "Romantic Dinner" Set (Wine, Rose Bouquet, French-Style Pork), "Soul Company" Set (Corn Chips, Beer, Ketchup, Fried Potatoes), Yogurt, Fruit Salad, "Fruit Delight" Set (Fruit Salad + Currant Juice), 
- Pancake, Bread with Jam, "Champion's Breakfast" Set (Pancake + Bread with Jam + Carrot Juice), Honey, Honey Cake, Chocolate Cookie, "Cozy Tea Party" Set (Tea + Honey Cake + Chocolate Cookie), Fur Coat, 
- Sweater, "Winter Fashion" Set (Fur Coat + Sweater), Shawarma, Stewed Mushrooms, Bun with Jam, Chak-Chak, Mead
### Jewelry
- Iron Chain, 
- Copper Bracelet, 
- Silver Brooch, 
- Silver Necklace, 
- Gold Earrings, 
- Gold Ring, 
- Silver Amethyst Brooch, 
- Gold Amethyst Ring, 
- Platinum Pendant, 
- Platinum Ring, 
- Platinum Emerald Pendant, 
- Platinum Diamond Ring
### Items
- Axe (6 levels), 
- Pickaxe (6 levels), 
- Fishing Rod (6 levels), 
- Phone, 
- Farmer's Diary (Book), 
- Backpack, 
- Pill, 
- Floral Wreath, 
- Soap, Gear, 
- Bag, 
- Colorful Hook

## Quests
### General Principles
Quests come in two types: main quests, given by key NPCs in their respective locations, and additional (daily) quests to ensure a continuous and varied gaming experience.

Players can receive quests directly from NPCs or through a phone (donation item) with the option to choose an NPC.

If an NPC has a quest, a "!" icon will appear above them. Clicking on the NPC opens a semi-transparent black bar that fully describes the task and its basis. Then, a menu appears.

Quest types may include:
- Resource gathering (trees, ores)
- Bringing food/plants (to the warehouse)
- Giving money
- Delivering something to someone (letter, gift)
- Bringing a jewelry item (if the player has it in the workshop, it's deducted from the inventory)
- Purchasing something on the farm (if the player is at a stage where the NPC requests it)

The menu contains the task, reward, and the option to accept/decline the quest. 

Main NPC quests cannot be declined; they merely describe the quest, provide a task, and await completion.

### Questline

#### Introduction

The player appears in the central part of the village (at the train station), where the head of the village (**Mayor**) is located. The player approaches them, clicks, and a dialogue begins:

1. First Click:
**Mayor** - Greetings! I am the head of this village of farmers, "village_name". Around these parts, they call me the mayor, but friends call me the retiree!

2. Second Click:
**Mayor** - Since you're here, I'm sure you want to experience the life of a real farmer. To help you understand how everything works, you have the "Farmer's Diary" in your 9th inventory slot. There, you can find answers to any questions of interest. The information in the diary unfolds as you progress.

3. Third Click:
**Mayor** - I see you're eager to start. Head east along the path; there you'll see an old barn. Next to it is Granny; she seems to need help, and in general, she'll assist you in your endeavors. She has lived here her whole life.

#### Player approaches **Granny Lyuda**.

**Granny**: Hello, are you the newcomer everyone in the village has been gossiping about? Well, you definitely look like a city person. No worries, we'll toughen you up a bit.

**Granny**: You can start your farmer's journey in our village. To begin with, find some money for wheat, which Konstantinych sells. This way, you'll earn money from the crop. You can use the grass in the barn. **(Quest 1 - Buy the first wheat from Konstantin)**

1. After completing Quest 1:

**Granny**: Oh, thank you! I could use some extra hands. Though I might be stronger than you, old age still makes itself known. 

Listen, during the spring rains, the roof got damaged, well, the barn's roof, not mine. I need help fixing it, as the grass has completely dried out and isn't bringing in any profit. 

Take an axe, go to the forest, and chop down (N amount) oak trees. **(Quest 2 - Bring Granny 20 oak logs)**

5. After completing Quest 2:

**Granny**: Oh, thank you! Now the jokes about the roof falling off should finally end, I hope...

6. Quest 3:

**Granny**: Wow, so you've already bought more than 80 units of wheat. Each crop unlocks a specific processing method after 80 units. What is processing, and why is it needed? Processing is the active circulation of goods to get more benefits from the crop. For example, wheat can be turned into bread.
To the right of me is a bakery. You can buy it and start making bread. **(Quest 3 - Buy the bakery and give Granny 1 bread)**

7. After Quest 3:

**Granny**: Finally, your possibilities have expanded, and the game has become more diverse for you.

8. Quest 4:

**Granny**: Now you have enough for your first little animal. In our case, it's a chicken. It will lay eggs, which you can either sell or use in further processing.
Buy the first chicken and bring me 3 eggs for a pie, please. **(Quest 4 - Give Granny 3 eggs)**

9. After Quest 4:

**Granny**: I'm very grateful; you've helped out an old lady!

10. Quest 5:

**Granny**: Go to our fisherman; perhaps you'll find something else interesting besides farming. Try your hand at fishing; who knows, maybe it'll work out for you.

Walk straight from the barn until the very end, then turn right. Our local fisherman is standing there. Honestly, he's quite a catch; you'll recognize him right away. 

Too bad a berry like me isn't to his taste. (**Quest 5 - Find the fisherman Henry**)

11. Quest 6:

**Fisherman Henry**: Greetings, [player]! I've already heard about you. Rumors spread quickly in our village.

Henry: Want to try your hand at fishing? Come on, I'll show you how it's done. (teleports the player to fishing spot) [provides fishing guide]

12. After catching the first fish:

**Henry**: That's how it all happens. If you enjoy it, feel free to come by more often. It's quite a profitable venture. 

**(Quest 6 - Catch the first 5 fish)**. After completing the quest (catching the fifth fish), Henry teleports the player to his farm and gives the next quest.

13. Quest 7:

**Henry**: Catch me a couple of buckets of fish (20). Everyone in my family loves seafood. **(Quest 7 - Catch 20 fish)**.

**Henry**: Thank you so much; this will last us for a month. May Poseidon bless you for this service.

14. Quest 8:

**Henry**: A bit further from me is my friend, neighbor, comrade, and brother - Koryagin. He needs help, but today I wanted to go fishing.
 Go to him, ask what he wanted. Maybe your help will be enough.

- (after completing, triggers 1 random positive event according to the season) **(Quest 8 - Find Koryagin)**. 

After this dialogue, the player is allowed to teleport home from Henry.

15.  Quest 9:

**Koryagin**: Hey, hello! Did Henry send you? That lazy squid! Probably avoided some nonsense again.

**Koryagin**: Well, if they sent you, there's nothing to be done. You're quite a weakling... Hope you can handle it; the job is not an easy one. Ha-ha-ha, got it? Kind of heavy, ha-ha.

I deal with transporting goods from our village to the city, and I need help unloading. I can do it myself, but I want to see what city slickers like you can do.

**Koryagin**: What's with the hesitation?! Get on the bus, it's near the house, and let's go! [provides guide on cargo transportation] **(Quest 9 - Transport the first cargo)**
- (after completion, grants a 1.2x cargo transportation speed boost for an hour)

16. Quest 10:

**Koryagin**: Unload 25 crates and distribute them among the warehouses. Be careful with the cargo, possum. **(Quest 10 - Transport 25 cargos)**

**Koryagin**: You've become a bit stronger; I even respect you a little, rooster. Now you're ready to watch over this farm! I can give you a couple of useful tips for the road.

**Koryagin**: For example, you can move around the farm not only on foot, because I see it's a bit challenging for you. You can take any animal (button X) and ride on it. If you get lost somewhere, there's a shortcut to return to your farm (button Y). And if, by any chance, you manage to get lost here, you can use the map you have (**button M**).

#### End
- After completion of the last questline, provides a game week (7 hours) without negative events

## Mounts and Perks

### Mounts

1. **Horse**: Obtained from a wandering merchant who appears on the farm with a low chance (3%, checked at the beginning of each day). 

The merchant gives a quest, and upon completion, the player receives a horse. The merchant stops spawning after the player obtains a horse.

**Merchant's Quest**:

Greetings, landowner! I am a wandering merchant, roaming the world to make my fortune. Listen, on your farm, there is a forest with mines, and I didn't bring any tools for this journey. 

So, I propose a deal: gather resources for me, and I'll give you my horse to make it easier for you to move around your lands!" **(Quest - Deliver 250 birch, 100 oak, 300 stone, 100 coal)**

2. **Mule**: Given to the player at the beginning of the game. Slower than other mounts.

3. **Pig**: Appears after the player buys 5 pigs.

### Perks
In the workshop, there will be a separate section for perks that players can acquire using resources.

#### Tool Perk (Axe, Pickaxe): 

Double Yield - Grants a chance to harvest 2 resources instead of one. Can be upgraded 5 times at a 4% increase each. 

Each upgrade is available at every 10 levels of progress in lumberjacking or mining. (New upgrade becomes available after the previous one; however, it won't allow upgrades if the player doesn't have the required tool according to the check.)

- +4%: 100 coal / 200 oak (available immediately)
- +4%: 15 iron / 400 birch (requires a tool with 10 levels of work)
- +4%: 20 silver / 600 spruce (requires a tool with 20 levels of work)
- +4%: 25 gold / 800 dark oak (requires a tool with 30 levels of work)
- +4%: 30 titanium / 1200 tropical wood (requires a tool with 40 levels of work)

#### Mount Speed Boost (All Mounts): 

Enhanced Horseshoes - Grants mounts an increased speed of 10% per upgrade. (New upgrade becomes available after the previous one.)

- +10%: 20 iron
- +10%: 25 copper
- +10%: 30 silver
- +10%: 35 gold
- +10%: 40 platinum

## Tools

- Players have three tools: an axe, a pickaxe, and a fishing rod. The axe and pickaxe are given from the start, while the player purchases the fishing rod from the blacksmith's shop.

- When a player reaches every 10th level of the corresponding skill (10, 20, 30, 40, 50), the tool can be upgraded in the workshop using money and time. 

- Upgrades to tools affect the types of blocks obtained by the axe and pickaxe, while upgrading the fishing rod allows catching new types of fish. 

- Tools can only be upgraded after reaching the required skill level. The player enters the workshop, spends money, and waits for a specific time to upgrade the tool. 

- When a player submits a tool to the workshop, the tool temporarily disappears from their inventory and returns improved after the upgrade time has passed.

# Daily Quest System

Daily quests were part of last season's design document and are carried over unchanged into this season.

---

## General Overview

The system involves villagers who are related to the NPCs on the farm.

Each villager will have their own route (with time intervals between points ranging from 30-120 seconds) and variations of quests.

Each NPC will have unique quests.

The quests will be divided into two categories: **seasonal** and **holiday**. Additionally, a special guest will randomly visit once per in-game year, offering special rewards.

Players will not receive quests for items that they have not yet unlocked.

Quests refresh once every in-game week (7 real hours).

There will be 30 total villagers, but every 2 seasons (fall-winter, spring-summer) there will be a rotation of villagers. Only 12 villagers can be present on a farm at a time, and every 2 seasons, a random selection of villagers will be rotated from the pool. There will be 3 special guests.

Villagers cannot appear in two consecutive rotations (they can only return after skipping one).

The same quest cannot appear twice in a row for the same villager (it can only appear after skipping one).

---

## Seasonal Quests

Seasonal quests are the regular version of the quests. Each NPC will have a quest related to their role on the farm and their connection to the main characters, as well as the current rotation (2 seasons).

Each villager will have a pool of 4 quests per rotation, one of which will be chosen at random.

For example, Vanechka’s wife visits the farm in winter. Since she comes from a warm place, she will need a sweater and some hibiscus tea.

---

## Holiday Quests

Holiday quests will appear one in-game week before the end of any holiday (for example, if the farm's birthday ends on September 19, and starts on September 16, the holiday quests will appear on September 13).

For each holiday, each villager will have a pool of 2 quests.

For example: After the New Year’s celebration, Andrew noticed that he’s short on eggs and cheese for his holiday salads.

---

## Special Guests

Once per in-game year, one of the three special guests will visit the farm.

The special guest will stay on the farm for one in-game week.

The player must be online for the guest to appear.

Special guests will offer unique quests (not just collecting items) and will offer different rewards as well.

Their arrival does not cancel other quests; their quests will be displayed separately.

They will not move around the farm but will stand in a fixed location.

A special guest cannot appear two in-game years in a row (only after skipping one).

Each special guest will have a pool of 3 quests.

---

## Types of Quests

- **Collect items/resources/money:** Example: Turn in 100 iron to an NPC in exchange for a booster; turn in 10 shawarmas, and you’ll get a membership.
  
- **Perform an action:** Example: Chop down 100 trees. Mow 500 grass. Brew a potion. Catch 10 fish.

- **Deliver an item:** Example: Take a shawarma and deliver it to Konstantin, or grab a fur coat and deliver it to Natasha.

# Jewelry Mechanics Update from 11.10.2024

Jewelry can no longer be sold - they are now meant to be gifted to NPCs responsible for purchasing plants (or trees). You can gift as many pieces of jewelry as you want, but each subsequent jewelry given to the same NPC has a diminishing effect.

To gift jewelry, you must own at least 1 purchased crop of the corresponding type.

Some jewelry has been removed. Here is the updated list of jewelry:

- Copper Bracelet
- Silver Brooch
- Gold Earrings
- Amethyst Brooch
- Emerald Pendant
- Diamond Ring

---

## Bonus List for Gifting Jewelry to NPCs:

- **Silver Brooch** - Gives a chance for the plant (and water reserves in the barrel, if any) to resist drought – improves up to 40%.
  
- **Gold Earrings** - Speeds up the production time of the associated crop (e.g., wheat will be produced faster than once per minute) – up to a -25% reduction in production time.
  
- **Amethyst Brooch** - Reduces the cost of plants of that crop type, without negatively affecting the farm's value – up to a 10% discount.
  
- **Emerald Pendant** - Increases the passive income from that crop – up to +10%.
  
- **Diamond Ring** - Gives a chance for the crop to spawn instead of grass. When broken, it gives money like grass, but additionally grants the player an amount equal to the income from that crop – up to 2%.

---

## Copper Bracelet Special Effect:

When given to a specific NPC, it provides a buff to the entire farm. Here is a list of crops and their corresponding buffs:

- **Wheat** - Increases income from grass - up to +5%.
  
- **Potatoes** - Increases player movement speed - up to +10%.
  
- **Cucumbers** - Reduces the cost of upgrading tools - up to -60%.
  
- **Sugar Cane** - Increases income from cargo - up to +10%.
  
- **Tea Leaf** - Chance to get twice the materials when mining ore - up to 20%.
  
- **Onions** - Chance to get twice the amount of wood when chopping trees - up to 20%.
  
- **Grapes** - Increases the chance of positive events - up to +10%.
  
- **Raspberries** - Reduces the chance of negative events - up to -5%.
  
- **Cotton** - Reduces the time needed to combo grass - up to -20%.
  
- **Strawberries** - Reduces smelting time - up to -20%.
  
- **Carnations** - Increases digging speed - up to +10%.
  
- **Flax** - Reduces processing time - up to -10%.
  
- **Corn** - Reduces the production time of jewelry - up to -15%.
  
- **Sunflower** - Increases the chance of the "Productivity" event - up to +20%.
  
- **Cocoa Beans** - Increases animal product production speed - up to -10% from production time.
  
- **Hops** - Reduces the money required to pay off taxes - up to -30%.
  
- **Rose** - Increases passive income - up to +5%.
  
- **Tomatoes** - Further increases income from all fish processing - up to +20%.
  
- **Chrysanthemums** - Increases the chance of the "Bloom" event - up to +20%.
  
- **Blueberries** - Reduces the average time needed to catch fish - up to -20%.
  
- **Brown Mushroom** - Increases the chance of the "Mushroom Rain" event - up to +20%.
  
- **Rice** - Reduces the amount of experience needed to level up professions - up to -15%.
  
- **Cinnamon** - Reduces the time required to cure the "Flu" - up to -30%.
  
- **Apple** - Increases the average cargo weight per area - up to +20%.
  
- **Peach** - Reduces the prices of all crops (again, without negatively affecting the farm's value) - up to -5%.
  
- **Pear** - Increases the chance of combo-grass triggering - an additional 1% chance.
  
- **Orange** - Increases the value of processed products - up to +15%.
  
- **Coconut** - Grants a chance to catch 2 fish at once - up to +30%.

The more jewelry of a specific type that an NPC receives, the higher the chance for the buff to increase. The chance grows with each additional piece of jewelry (geometric progression).

---

## Explanation of How the Buff Chance Increases

The chance grows following a geometric progression formula. It is calculated using the following simple formula:

In this formula:
- **b₁** is the first term of the sequence, or the buff granted by the very first piece of jewelry given of that type.
- **q** is the multiplier by which the buff increases with each subsequent piece of jewelry of the same type given to the NPC.
- **n** is the number of jewelry pieces given to that NPC.

Let’s walk through an example:

Suppose we want to calculate the buff provided by Copper Bracelets gifted to an NPC in charge of wheat (let’s call him Konstantin). We’ll assume that the first bracelet gives a 1% buff to grass income (this is **b₁**), and each subsequent bracelet gives 0.8 times the previous one (so the second bracelet gives 0.8%, the third gives 0.64%, and so on). In this case, 0.8 is **q**. Finally, we just need to substitute **n** – the number of Copper Bracelets given to Konstantin – to calculate the total percentage increase in grass income.

---

## Configuration and Data Storage

In the config files, two values will be stored, which will vary for each NPC and each type of jewelry:
- **b₁** (the first buff).
- **q** (the buff multiplier).

As for **n** (the number of jewelry pieces given), it will be stored in the database and will differ for each player, depending on how many pieces of jewelry they have gifted. **n** will be different for each piece of jewelry and each NPC (leading to 28 * 6 values per player).

---

## Jewelry Crafting and Interaction

The ability to sell jewelry should be removed. Now, jewelry can only be crafted. When interacting with an NPC while holding the sprint button, a menu will appear where the player can choose how many jewelry pieces of each type they want to gift.

# Daily Quests

1. **Grass income x3 for 1 hour**  
2. **Bloom event** for 20/25/30/40/50 minutes  
3. **Instant Money** = income for 20/25/35/45/55 minutes  
4. **No Seasonal Negative Effects** for 20/25/35/45/55 minutes  
5. **Player cannot get tired** while resource gathering for 30/40/50/65/80 minutes  
6. **Processing speed increased** by 10%/14%/16%/20%/24% for 1 hour  
7. **3 daily quests available** instead of one  
8. **Plant export speed increased** by 8%/12%/14%/17%/22% for 2 hours  
9. **Player gets Speed 2** for 1/1.5/2/2.5/3 hours  
10. **Bloom** for 30/40/50/60/75 minutes  
11. **Player receives one of three resources** in a certain amount to choose from (items are likely to be equal to player progress. This can be a resource for jewelry, fish, or something from animals or plants).  
12. **Instant Money** = income for 120/160/180/210/240 minutes  
13. **For the next 35/45/60/75/90 minutes** there is a 5% chance to double resources, even in fishing  
14. **Processing speed increased by 25%** for 40/60/70/85/100 minutes  
15. **Player chooses one of 3 garden beds** to get x2 income from one of them for the next 160/200/260/340/400 minutes  
16. **Plant export speed increased by 20%** for 120/160/200/250/300 minutes  
17. **Income x2** for the next 200/240/280/300/360 minutes (only income)  
18. **Grass x3** for 60/80/100/120/140 minutes  
19. **Player gains flight** for 8/10/11/12/14 hours  
20. **Player receives one of three resources** in a certain amount to choose from (items are likely to be equal to player progress. This can be a resource for jewelry, fish, or something from animals or plants).  
21. **No negative effects, bad grass, or unlucky fishing** for the next 1/1.5/2/3/4 hours  
22. **Chance for a positive event increased by 50%** for 3/3.5/4/5/6 hours  
23. **Player gets Speed 2 and Jump Boost 1** for 10/11/12/13/14 hours  
24. **Instant Money** = income for 3/3.5/4/5/6 hours  
25. **Processing speed increased by 25%** for 3/3.5/4/5/6 hours  
26. **Player can choose from 3 possible daily quests**  
27. **A random positive event** available during the season is triggered  
28. **Animal export speed increased** by 12%/15%/18%/20%/24%  
29. **Choose from 3 processing buildings**, and select one where processing speed is boosted by 20%/25%/30%/40%/45%  
30. **Customization crate for the farm**

### Potion Brewing - Update from 11.09.2024
Potion brewing is a new feature in **MyLittleFarm** that allows players to brew various potions. To start, players must build the **Witch's Cottage**, which requires the following materials: 
- Stone
- Iron
- Birch wood
- Witch's Cottage Blueprint

This building also introduces an NPC named **Morgana**.

#### How Potion Brewing Works
A cauldron filled with water serves as the primary tool for brewing. Players "throw" ingredients into the cauldron, selecting them from a special storage (accessible through a dedicated menu). This storage holds all the materials available for brewing, which can also be sold or used for other purposes (this is handled in a separate menu for crafted potions).

Once the ingredients are added, the brewing process begins, visualized by particles, and a **hologram** displays information about the brewing potion and its production progress.

**Note:** Only one potion can be active at a time. If a player uses a potion, they cannot drink another while the effects of the first potion are active—**effects do not stack**.

#### Ingredients for Potions

- **Grass Gathering** (drop chance):
  - **Hellebore** (0.5%)
  - **Clover** (0.5%)
  - **Amanita** (0.5%)

- **Mining** (drop chance):
  - **Coal Dust** (coal, 4%)
  - **Ground Quartz** (quartz, 3%)
  - **Gold Nugget** (gold, 2.75%)
  - **Emerald Shard** (emerald, 2.5%)
  - **Crushed Obsidian** (obsidian, 2%)

- **Lumberjacking** (drop chance):
  - **Oak Bark** (oak, 4%)
  - **Wood Dust** (any wood, 5%)
  - **Birch Sap** (birch, 3.5%)
  - **Dark Oak Leaves** (dark oak, 3%)
  - **Acacia Honey** (acacia, 2.5%)
  - **Tropical Nectar** (tropical wood, 2%)

- **Fishing** (drop chance):
  - **Kelp** (5%)
  - **Fish Oil Flask** (3%)
  - **Saltwater Flask** (3%)
  - **Clay** (5%)

#### List of Potions, Recipes, Effects, and Duration:

1. **Potion of Luck**
   - **Ingredients:** Clover, Gold Nugget
   - **Effect:** 20% chance to mine two blocks instead of one or catch two fish instead of one. Works in mines, forests, and fishing.
   - **Duration:** 1 hour

2. **Potion of Cleanliness**
   - **Ingredients:** Ground Quartz, Oak Bark, Saltwater Flask
   - **Effect:** Reduces the chance of a "dirty" debuff by 40%.
   - **Duration:** 4 hours

3. **Potion of Moisture**
   - **Ingredients:** Emerald Shard, Birch Sap, Kelp
   - **Effect:** Reduces the chance of a drought by 45%.
   - **Duration:** 3 hours

4. **Potion of Satiety**
   - **Ingredients:** Hellebore, Acacia Honey, Fish Oil Flask
   - **Effect:** Reduces the chance of hunger by 45%.
   - **Duration:** 3 hours

5. **Potion of Fertility**
   - **Ingredients:** Clay, Wood Dust, Coal Dust, Dark Oak Leaves
   - **Effect:** Opens a menu of all NPCs with plants or trees bought from them. Choosing an NPC increases their production income by 1.5x.
   - **Duration:** 2 hours

6. **Antigrippin**
   - **Ingredients:** Amanita, Coal Dust, Fish Oil Flask
   - **Effect:** Reduces the chance of catching the flu by 50%.
   - **Duration:** 2 hours

7. **Potion of Diligence**
   - **Ingredients:** Crushed Obsidian, Tropical Nectar, Clover, Saltwater Flask
   - **Effect:** Opens a menu of all NPCs with purchased processing buildings. Selecting an NPC increases processing speed by 1.5x.
   - **Duration:** 2 hours

