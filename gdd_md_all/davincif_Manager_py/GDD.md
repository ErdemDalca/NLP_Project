# Game Design Document

Since some features, like font coloring, are not surportted by the GitHub _.md_ file, it's recommended the use the another interpreter that does!

You can choose to read this docs, we recommend [here](./GDD_at_jbt.md).

## Index

1. [Target Audience](#Target-Audience)
1. [Inspirations](#Inspirations)
1. [Short Description](#Short-Description)
1. [Theme](#Theme)
    1. [Cultural Reference](#Cultural-Reference)
    1. [Look and feel](#Look-and-feel)
1. [Mechanics](#Mechanics)
    1. [Map](#Map)
    1. [Terrains](#Terrains)
    1. [Time](#Time)
    1. [Raw Material](#Raw-Material)
    1. [Resource Tier](#Resource-Tier)
    1. [Structures](#Structures)
1. [Non Functional Requerements](#Non-Functional-Requerements)
1. [A Better Place to Read The Docs](./GDD_at_jbt.md)

<a name="Target-Audience"></a>

## Target Audience

Poeple that where **fans of the RTS and Tycoon games**, browser managers. An audience that takes fun into **strategy**,
optimizing **processes** and **exploring**.

Probably **adults** into their **late 20's and beyoung** that grew with **references** like **SimCity** and **Age of Empires**.

<a name="Inspirations"></a>

## Inspirations

The games takes inspiration into a list of games that, in some degree or another, already made this **mix** between **exploration**, **commerce** and **war**.

For exemple:

-   City builders, like:
    -   [SimCity IV](https://store.steampowered.com/app/24780/SimCity_4_Deluxe_Edition/)
    -   [Cities Skylines](https://store.steampowered.com/app/255710/Cities_Skylines/).
-   Games where the focus was on the industries, like:
    -   [Simutrans](https://store.steampowered.com/app/434520/Simutrans/)
    -   [Rise of Industries](https://store.steampowered.com/app/671440/Rise_of_Industry/)
-   Some more ballances between the City Builds and the RTS gener, like:
    -   [Pharaoh](https://store.steampowered.com/app/564530/Pharaoh__Cleopatra/)
    -   [Black and White II](https://en.wikipedia.org/wiki/Black_%26_White_2)
-   The classics RTS games, like:
    -   [Age of Empires II](https://store.steampowered.com/app/221380/Age_of_Empires_II_Retired/)
    -   [Age of Mythology](https://store.steampowered.com/app/266840/Age_of_Mythology_Extended_Edition/)
-   The old RTS games like:
    -   [Travian](https://store.steampowered.com/app/266840/Age_of_Mythology_Extended_Edition/)
    -   [Tribal Wars](https://www.tribalwars.com.pt)

<a name="Short-Description"></a>

## Short Description

The attractiveness of this game should come from a of simple concept:

**The power dynamic of the real world!**

It's hard and unfair, but not everything is about war and, was every player peacefully, so would be the game.

1. One is unlikely to survive alone.
1. Economy is the most important part, it's delicated and intrincated.
1. An Army is only needed if you need to protect yourself; or if you want to conquer others.
1. Armies are an expensive asset to build and maintain.

<a name="Theme"></a>

## Theme

What's the teme of the game? The ambience, how it should look.

<a name="Cultural-Reference"></a>

### Cultural Reference

The game is set in **early madieval** era, where **powender was yet not used as weapon**. But **war ships** and long
distance **navigations** where already possible.

<a name="Look-and-feel"></a>

### Look and feel

The game is **text based**.

Ech tile in te map, item, or information of any sort is represented by a combination of caracter(s) and color(s).

Each section, whenever needed, will inform the character/color code of each item.

<a name="Mechanics"></a>

## Mechanics

This section will explain, in detail, each and every one of the mechanics that the game should support.

**Note**: All the mesurements in this documentation are in SI (International System of Units).

<a name="Map"></a>

### Map

On a global scale, the **world map** is a squared title set. Where the player can see the biomes, cities and any other
player contructed mega structure in it.

| **Biomes**        | Crossing Effort |
| ----------------- | --------------- |
| Plain green lands | 100%            |
| Water             | ❌              |
| Forest            | 115%            |
| Mountains         | 200%            |

The player must be able to diferenciate both the biome and the human constructed mega structure in it.

<a name="Terrains"></a>

### Terrains

Inside each title in the world map there is an also squared **local map**.

Here is where the player can place the human structures avilable in the game, like a woodcutter, a foundry or a wall,
for exemple.

It's also at this level that the player can actually see the resources available for exploration. Each one of them comes
with a randomized ammount of resources per title.

A player cannot place structure on certain terrains.

| **Biomes** | constructable | Symbol                                                | Font-Color                                        |
| ---------- | ------------- | ----------------------------------------------------- | ------------------------------------------------- |
| Grass      | ✔️            | <section style="color: #78be2c">"~"</section> or 🌱   | ![](https://placehold.co/20x20/78be2c/78be2c.png) |
| Water      | ❌            | <section style="color: #00a6ed">(~)</section> or 🌊   | ![](https://placehold.co/20x20/00a6ed/00a6ed.png) |
| Forest     | ✔️            | <section style="color: #3e811b">/\|\\</section> or 🌲 | ![](https://placehold.co/20x20/3e811b/3e811b.png) |
| Mountains  | ❌            | <section style="color: #2f1b3c">/\\</section> or 🗻   | ![](https://placehold.co/20x20/2f1b3c/2f1b3c.png) |

<a name="Time"></a>

### Time

The ration of days:second in the game is of **1d:3s**.

That is to say: _1 day in the game takes excatly 3seconds of gameplay_.

This give roughly _18 min for 1 year_.

<a name="Raw-Material"></a>

### Raw Material

The raw materials, a.k.a [teir 0 materials](#Resource-Tier), are the base resources.

Only raw matherials can be extracted directly from the local [terrains](#Terrains).

Each resource tile is generated with an average amount of materials, according to the table bellow.

They are:

| **Material** | Symbol                                              | ≈Material/Tile | Font-Color                                        |
| ------------ | --------------------------------------------------- | -------------- | ------------------------------------------------- |
| Water        | <section style="color: #00a6ed">(~)</section> or 💧 | ∞              | ![](https://placehold.co/20x20/00a6ed/00a6ed.png) |
| Food         | <section style="color: #d79a57">(o)</section> or 🥔 | 1T             | ![](https://placehold.co/20x20/d79a57/d79a57.png) |
| Wood         | <section style="color: #623f30">[=]</section> or 🪵 | 10T            | ![](https://placehold.co/20x20/623f30/623f30.png) |
| Clay         | <section style="color: #ae5626">[@]</section>       | 10T            | ![](https://placehold.co/20x20/ae5626/ae5626.png) |
| Stone        | <section style="color: #595959">[•]</section> or 🪨 | 100T           | ![](https://placehold.co/20x20/595959/595959.png) |

The ammount of resources in a tile must be randomized, varying in a range of ±2% from the expected value.

<a name="Resource-Tier"></a>

### Resource Tier

[TO BE DEFINED]

<a name="Structures"></a>

### Structures

[TO BE DEFINED]

<a name="Non-Functional-Requerements"></a>

## Non Functional Requerements

The **core logic** of the game, must be as **decoupled** as possible **from** how the game implements its rendering,
input treating and everything else that can be call "**engine**".

So as said before, we must be able to change the game **from** a **text based** game to a **to** a **2d game**, using
_pygame_ for eg., without having to rewriting all the game logic.

Same goes for multithreading processing.

And even, for the title set system as much as possible. We might wanna use a hexagonal system at some point in the
future.

<a name="A-Better-Place-to-Read-The-Docs"></a>

<!--
<a name="Population"></a>
 ## Population


Population is **the most important** resource!

Each person in the game is called a **Villain**; and Each villain consumes -1 Food.
-->
