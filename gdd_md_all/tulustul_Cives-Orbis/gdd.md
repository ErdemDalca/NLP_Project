# Table of contents

- [Overview](#Overview)
  - [Why another civ clone?](#Why-another-civ-clone)
  - [Design philosophy](#Design-philosophy)
  - [Game title](#Game-title)
- [The world](#The-world)
- [Cities](#Cities)
- [Military](#Military)
  - [Supplies](#Supplies)
  - [Zone of control (ZOC)](<#Zone-of-control-(ZOC)>)
  - [Unit stacking](#Unit-stacking)
  - [Armies](#Armies)
  - [Generals](#Generals)
- [Resources](#Resources)
- [Economy](#Economy)
- [Trade](#Trade)
- [Knowledge](#Knowledge)
- [Nation](#Nation)
- [Religion](#Religion)
- [Happiness](#Happiness)
- [Health](#Health)
- [Culture](#Culture)
- [Slavery](#Slavery)
- [Public works](#Public-works)
- [Great people](#Great-people)
- [Diplomacy](#Diplomacy)
- [Internal politics](#Internal-politics)
- [Espionage](#Espionage)
- [Barbarians](#Barbarians)
- [The beginning of the game](#The-beginning-of-the-game)

## Overview

`Cives Orbis` is a turn-based strategy game inspired by the Civilization series. Some may even say it's a Civilization clone. The base concept is the same as in Sid Meier's famous title and a lot of mechanics are very similar. For this reason, I won't write a lot about the game's concept. Let's just say it is about **leading a civilization from prehistory to modern times**.
Despite being the civ clone, the game has some distinct attributes which in my opinion justify is's creation.

### Why another civ clone?

- There is no good open-source alternative to civ.
  - [FreeCiv](http://www.freeciv.org/) mimics old and outdated civ 2 and is written in an unsafe language.
  - [Unciv](https://github.com/yairm210/Unciv) is a pure civ 5 clone so why not play civ 5?
- I disagree with a lot of design choices in Civilization series, `Cives Orbis` is going to be my interpretation of the Sid Meier's idea.
- Civilization games and most of its clones require a powerful gaming pc. I have a brand new business laptop and I can barely run Civ 5 which is already a 10 years old game. Therefore `Cives Orbis` is going to have a simple, clear 2d graphics and low spec requirements.
- It will run in your browser. Accessible everywhere, runs on anything, clear path to mobile version.
- The turn times in classic civ games are terrible, especially in the late game. This can be improved.
- Classic civ games have no proper Linux support.

### Design philosophy

#### Emphasis on historic correctness

It is much less a computer board game and much more a world history simulator. All the core mechanics are modeled after the real world. This makes the overall feel of the game very different than in Civilization series.

#### A game about decision making

A decision making in a classic civ game is a choice between one benefit and the other. I believe that choosing between good and good is not a real choice. Here we break that rule. Most of the decisions have a positive and negative side effect just like in the real world. You have to sacrifice something to gain what you need.

### Game title

`Cives Orbis` means `Citizens of the world`. First and foremost it sounds cool. It also corresponds with one of the game's main distinct features -> nations.

## The world

TODO

## Cities

- Founded by settlers.
- Each population point spawns one worker in the city.
- The worker works on a selected city tile adding its yields to city yields.
- The production in the city is used to construct buildings and recruit units.
- Each building adds various bonuses to the city.
- Instead of units or buildings the city can focus (?) to transfer part of it's production to e.g. food, production or knowledge. TODO need a name for it.

### Attributes

- Population
- Yields (food, production, etc.)
- Manpower - adds to global manpower
- [Happiness](#Happiness)
- [Health](#Health)
- Defense
- Health points?
- List of buildings
- Main religion
- Main nation

### Growth

- City population increments when enough food is accumulated.
- Each city worker consumes some food, specialists consume double the food.
- When food per turn is not enough to feed city workers, the accumulated food deteriorates.
- When accumulated food is lower than zero, the city shrinks.
- TODO take unhealth into account.

### Specialists

- Some buildings have specialist slots (artists, scientists, priests, etc.).
- City workers can be appointed as specialists.
- The specialists cannot work on city tiles but grant some bonuses (e.g. scientists grants extra knowledge points).

### Border expansion

- When enough culture is accumulated, a new tile is added to the city from the pool of available tiles. The tile must have a majority population of a nation most represented in the city.
- The pool of available tiles consists of tiles neighboring current city tiles not yet owned by any other state.
- The player can buy the land. The less nation's representation there is in the tile the more expansive this tile is.
- The maximum distance of available tiles is limited by the city size. (how exactly?)

### Capturing a city

TODO

## Military

All military units have the following attributes:

- power
- movement points (**MP**)
- health points (**HP**)
- supply points (**SP**)
- ...various bonuses

### **Recruting**

TODO

### **Supplies**

Supplies are the concept that limits the power of stacks of doom and adds a bit of tactic and deep to the combat. It also limits the potential of military units being used as scouts and explorers.

- Each unit has supply points.
- Supply points will deteriorate when in foreign territory.
- When supplies are deteriorated, the health points will start to decrease which can lead to the unit being disbanded.
- Supply points can be replenished by pillaging tile improvements or cities, by defeating an enemy army and taking over their supplies or by intercepting enemy supply units.
- To take care of the supply lines the player must build a special supply unit.
- Supply units also have supply points, though much more of them. They replenish some amount of other units SP when they are in range. The equivalent amount of SP is taken from the supply unit.
- Supply units can replenish the SP in cities.

### **Zone of control (ZOC)**

Each military unit establishes a zone of control that consists of neighboring tiles (naval or land depending on unit type). If an enemy controls a particular tile:

- Moving to that tile costs twice as much.
- A city cannot work on this tile.
- Supply lines are blocked.
- When a unit is surrounded by enemy ZOC then it starts to lose SP even if it's on friendly territory.

### Unit stacking

- Military units can stack together.
- The maximum stack size is based on the player's bonuses.
- When attacking stacked units the defenders issue the best unit.
- Stacked units can be grouped and move as one.
- The speed of the group is limited by its slowest unit.

### Armies

- A [general](#Generals) can transform a group into an army.
- An army fights as one unit.
- Damage to an army is distributed evenly across all units (with small random variations)
- TODO combat algorithm

### Generals

- Generals move like an ordinary unit.
- There's a limit to how many generals a player can own.
- Generals gain experience in fights. Higher-level generals provide better bonuses and can operate larger armies.
- Let's say for now that generals are trained in the cities just like normal units. One of the alternatives is to gain them through combat like in Civ games. Training a general and letting him gain experience in combat so that he becomes great seems to be better mimicking the real world.

## Resources

There is no distinction between strategic and luxury resources. Each resource has its bonuses which can be extended with buildings, techs, and other bonuses.

Each resource has:

- yields bonuses
- quantity
- other bonuses (health, happiness)

Resources can be traded using the trade network. Players can prevent certain resources from going into the trade network if they want to keep those resources for themselves.
They can also embargo certain players from getting certain resources from you.

## Economy

### Yields

At the beginning of the game, tile yields are very poor. River valleys are the only sensible sources of food and resources are the only source of production and gold + they can yield some extra food. Various bonuses later in the game increase the yields making other areas worth colonizing.

A great deal of production can be acquired from slavery. In the case of gold, trade routes can do a tremendous job.

## Trade

Trade is represented as a graph with cities as nodes and trade routes as edges.

- When a city establishes a trade route with another city, a portion of its food, gold, culture, knowledge, slavery, and luxuries are duplicated and transferred through the route to the other city.
- Trade routes work two ways and are beneficial for both sides. They are not symmetrical though and the goods transferred in both ways can differ.
- Various bonuses can enhance the quantity of the transferred goods.
- The bonuses distinct between domestic/foreign trade routes and land/overseas trade routes.
- Pillaging a trade route nullifies its transfer for x turns. All yields are added to the pillager's global yields. Pillager also has it's SP replenished.
- Trade routes have a maximum length.
- A trade route from A to B visits all cities in-between.
- Trade routes can stack if they occupy the same edge.
- A market is required to join the city into the trade network.
- Land trade routes require a road or river connection.
- Each edge carries goods from a list of cities.

### Resources

- If a city needs a particular resource it takes it from the route and puts some gold in the opposite direction.
- Each edge in the network defines a resource demand which is calculated by the needs of the cities which are connected to that edge.
- A city put all excessive resources to the trade network. It is distributed proportionally to the edges' demands.
- The bigger the city the larger quantity of the resource a city requires.

## Knowledge

Knowledge is the equivalent of science is the classic civ games. Knowledge seems to be a better metaphor though since in old times there was no science and scientist but there were knowledge and wise men. It also sounds more proper that civilization accumulate knowledge than accumulate science. In later stages of the game, players can transfer some gold into knowledge which is a good enough metaphor of modern scientific research.

The mechanic is pretty much the same as in civ games. Various buildings/politics/trade routes/tiles generate knowledge points. These points are used to research technologies in the tech tree.

### Tech tree

- New tech unlocks new staff and grant bonuses.
- The tech may have specific requirements like resources or politics
- Some technologies are optional e.g. specific weapon improvements.

## Nation

The Nation is a mechanism that steers centrifugal forces of a state and adds an organic feeling to the game.

- The game starts with a few tribes.
- Several players can share the same tribe.
- Culture points are used to enhance a tribe into a nation.
- Each nation has specific bonuses.
- There is a specific "tech" tree for nations called `culture tree`, culture points are used to progress through that tree.
- The `culture tree` is not linear like the `tech tree`. It starts in the center and branches in all directions. It's up to the player how the nation will develop, some branches might never even be started.
- The city will use bonuses of a nation with most representatives in the city. (Maybe use bonuses proportional to the population?)
- Each tile have a distribution of population
- In every turn each tile population is recalculated:
  - Each nation in every city has a `nation pressure power`.
  - `nation pressure power` is based on a city's culture per turn but different modifiers are possible.
  - Trade routes carry `nation pressure power` from an originating city (Do all cities along the route are affected equally or the effect is lessened with each city?).
  - The pressure is emitted into neighboring tiles (formula?).
  - When two pressures meet, the stronger slowly overtakes the weaker one.

#### Some general clues

- Some nations may be resistant to occupation and rebel often, others may be artistic, some are traders...
- A typical empire consists of many conquered nations, each with its traits meaning that different parts of empires may have very different needs and require special treatment.
- Maybe it's worth to have a federal government or grant autonomy to some trouble nations?
- A city or whole nations can rebel if treated badly.
- Sometimes a genocide or a relocation might be a solution :)

## Religion

- `faith points` are required to progress through religion.
- When enough `faith points` are accumulated, a pantheon may be founded.
- A great prophet is needed to found a religion.
- Religion has a religious tree, similar to the tech tree. Some branches are blocked for specific religions.
- `faith points` are used to progress through the religious tree.
- The religion propagation/pressure mechanic is the same as the nation's propagation but uses `faith pressure power`.

## Happiness

Happiness is calculated per city so parts of a state can be happy and parts can be unhappy.

- Each population point in a city increases `unhappiness`.
- Every luxury resource in a city creates `happiness` (until the demand for this resource is surpassed)
- Buildings can increase `happiness` or `unhappiness`.
- When `unhappiness` is bigger than `happiness` then the city is `unhappy`.
- Each `unhappiness` in `unhappy` cities slowdowns production.
- Slowdown formula: `production = production per turn * (1 - (happiness - unhappiness) / population)`
- If unhappiness reaches the population then the city automatically rebel.
- A nation under foreign rule generates additional `unhappiness`.
- A perpetuating `unhappiness` can lead to rebel.
- Players lose control of rebelled cities. Rebeliants spawn around the city.
- If the rebelled city is not pacified before `x` turns, a new state is created or the city joins a neighbor state ruled by a nation with the majority in this city.
- A prolonged conflict increases `unhappiness` state-wise due to war-weariness.

## Health

- Every population point in a city creates `unhealth`.
- Every food resource in a city creates `health` (until the demand for this resource is surpassed).
- Buildings can increase `health` or `unhealth`.
- When `unhealth` is bigger than `health` then the city is `unhealthy`.
- Each `unhealth` in `unhealthy` cities is taken into account in a growth formula resulting in slower growth or even in a city shrinkage.
- A perpetuating `unhealthy` state can lead to epidemics.
- Epidemics are of a specific disease. Disease parameters:
  - `unhealth` multiplier
  - lifetime
  - hidden state lifetime
  - contagion rate
- A city under epidemic has more `unhealth` points for some turns, according to disease parameters.
- A disease spreads along trade routes.
- A contagion rate says what chance there is for a city along a trade route to be infected in a turn.
- A disease is hidden for some time. There are no `unhealth` penalties but the disease can spread along the trade routes.

## Culture

- Culture points are accumulated per city and allow [border expansion](#Border-expansion).
- Culture points are accumulated globally and are used to progress through [culture tree](#Nation).
- Culture points influence [nation pressure power](#Nation).

## Slavery

Early economies can greatly benefit from slavery. Later in the game slavery generates more and more unhappiness and it becomes beneficial to abolish slavery. By picking the right bonuses the players can keep the slavery to the end of the game and it will still be profitable.

Each city has it's slavery output per turn. The player also has global slavery points.

Slaves are part of the cities population and are taken into account when processing city population logic.

### Slavery sources

- Defeating enemy units.
- Pillaging.
- Sacking cities.
- Trade routes.
- Buildings e.g. slave market

### Slavery usage

- Part of slavery output in a city is added to production when constructing buildings.
- Speeding up building production by consuming global slavery points + some food/population
- TODO Public works, how?

## Public works

The player accumulates `public work points` by specialized buildings or `slavery`. Then he can spend those points to build various tile improvements.

Tile improvements consume some `public work points` per turn. When run out of `public work points` random tile improvement is damaged.

## Great people

TODO

## Internal politics

- Taxing (the higher taxing, the more money, more unhappiness and less productivity)
- Science spendings (in the late game)
- Picking a state [religion](#Religion)
- [Nolan Chart](https://en.wikipedia.org/wiki/Nolan_Chart)

### Policies

There are several areas where each state needs to pick a solution for. Changing the policies results in a couple of turns of anarchy during which the player has no control of the cities.

#### Government

- Autocracy
- Oligarchy
- Republic
- Democracy

#### Economy

- Tribalism
- Despotism
- Feudalism
- Capitalism
- Communism
- Socialism
- Anarchism

#### Religion

Religion is similar to how [nations](#Nation) work. You accumulate `faith` points which enables you to found religion and progress through the religion tree. Every tile on the map has a distribution of religions. Each city generate `religion pressure power` and in each turn the distribution is recalculated.

Each player can pick a state religion if his policies allow that. Cities with a majority of this religion get extra happiness and cities with foreign religion get extra unhappiness. Some of the religion bonuses are active only if the religion is a state religion. You get better relations with states with the same state religion.

### Lawmaking

Each policy area has several law slots which can be filled with laws. Some laws require specific policies. A few turns of a gap is required between changing the law.

## Diplomacy

TODO

### Leagues

TODO

## Espionage

TODO

## Barbarians

- Barbarians reside in encampments which spawn randomly in no man's land.
- Barbarian units spawn in the encampments and they belong to this specific encampment.
- Each encampment belongs to a tribe.
- (?) Encampments work like a mini-civilizations. They train units, can be in a war or peace state with other encampments or civilizations.
- When encampment lives for long enough and it has contact with civilization then it can progress into a city and play as a new player.
- Barbarians cannot occupy cities, they can only sack them.

# The beginning of the game

Defining the number of civilizations at the start of the game, like in the Civ games, is highly artificial and makes the game predictable. `Cives Orbis` takes another approach.

- The player can set "civilization density" at the map creation phase.
- The game starts only with the settler which can found an encampment.
- In the encampment, which basically is a city with a size of 0, the player can train units and construct buildings.
- TODO
