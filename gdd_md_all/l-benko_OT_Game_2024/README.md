# **OT_Game_2024 - Game Design Document - SK**

Na danom repozitáre sa nachádza implementácia prototypu hry v Pygame, ktorá bola realizovaná počas cvičení k predmetu Objektové technológie. Na danej hre boli prezentované podstatné herné funkcionality a repozitár slúži ako vzor k vývoju hry určenej pre projekt k predmetu.

**Autor**: Ľubomír Benko

**Vybraná téma**: Swarms (príklad témy)

---
## **1. Úvod**
Navrhnutá hra slúži ako ukážka pre predmet Objektové technológie, s cieľom vytvorenia funkčného prototypu hry ako projektu ku skúške. Vytvorená hra spĺňa požiadavky zadanej témy (Swarms - príklad témy). Hra má charakter hráč proti celému svetu, kde na hráča útočia príšery a jeho cieľom je prepracovať sa k cieľu.

### **1.1 Inšpirácia**
<ins>**Archero**</ins>

Archero je hra zameraná na osamelého lukostrelca, ktorý prechádza rôznymi úrovňami, pričom bojuje s rôznymi nepriateľmi. Koncept hry je založený na ***jeden proti celému svetu***, doplnený o rôzne herné mechaniky, ktoré časom vylepšujú hlavného hrdinu v boji s väčším množstvom silnejších nepriateľov. Hráč si v hre dokáže vylepšovať svoje skilly a zbroj.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/archero.jpg" alt="Archero">
  <br>
  <em>Obrázok 1 Ukážka hry Archero</em>
</p>

<ins>**Survivor.io**</ins>

Survivor.io je mobilná hra zameraná na jedného hrdinu bojujúceho proti veľkému množstvu nepriateľov. Cieľom je prežiť stanovený čas a poraziť všetkých nepriateľov. Počas boja sa hráč ***voľne pohybuje po mape*** a snaží sa prežiť, prípadne nájsť správny okamih zasiahnutia nepriateľov. Nepriatelia ***vždy prenasledujú hráča*** s cieľom ho poraziť.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/survivor.jpg" alt="Survivor.io">
  <br>
  <em>Obrázok 2 Ukážka hry Survivor.io</em>
</p>

### **1.2 Herný zážitok**
Cieľom hry je, aby hráč prežil ***určitý časový interval v hre***, pričom sa nenechá poraziť veľkým množstvom nepriateľov, ktorí sa na neho rútia a pri kontakte mu spôsobujú zranenia. Hráč sa môže pohybovať po mape a zároveň môže likvidovať nepriateľov, čím zvyšuje svoje šance úspešného prežitia časového intervalu.

### **1.3 Vývojový softvér**
- **Pygame-CE**: zvolený programovací jazyk.
- **PyCharm 2024.1**: vybrané IDE.
- **Tiled 1.10.2**: grafický nástroj na vytváranie levelov.
- **Itch.io**: zdroj grafických assetov a zvukov do hry.

---
## **2. Koncept**

### **2.1 Prehľad hry**
Hráč ovláda svoju postavu a snaží sa prežiť v hre stanovený ***časový interval*** (napr. 90 sekúnd). Počas tohto času ***na neho útočia*** nepriatelia, ktorí sa v pravidelných intervaloch spawnujú na mape. Hráč má možnosť nájsť a využiť na mape objekty, ktoré mu pomôžu získať bezpečie a nebyť vystavený útokom zo všetkých strán.

### **2.2 Interpretácia témy (Swarms - príklad témy)**
**"Swarms"** - hráč je prenasledovaný veľkým množstvom nepriateľov, ktorých môže zabíjať, avšak sú opätovne generovaný do sveta. Nepriatelia majú nastavený pohyb vždy smerom k hráčovi a tak sa ho snažia premôcť obrovským množstvom. Vo vyšších leveloch je možné zvýšiť intenzitu generovania nepriateľov a zvyšovanie ich odolnosti voči hráčovým útokom.

### **2.3 Základné mechaniky**
- **Prekážky**: na mape sa nachádzajú objekty, ktoré tvoria aktívnu prekážku ako pre hráča, ak aj pre nepriateľov.
- **Bonusové predmety**: hráč môže na mape zbierať predmety, ktoré mu pridajú napr. život, silu útokom alebo znížia čas do konca kola.
- **Pevne stanovené miesta generovania nepriateľov**: nepriatelia sa negenerujú hocikde na mape, ale majú na to pevne stanovené miesta, aby nenastala situácia, že sa nepriateľ spawne doslova na hráčovi, čím sa zníži hrateľnost.
- **Hráč môže likvidovať nepriateľov**: hráč vystreľuje ohnivú gulu, ktorá pri náraze do nepriateľa spôsobuje jeho zranenie.

### **2.4 Návrh tried**
- **Game**: trieda, v ktorej sa bude nachádzať hlavná herná logika (úvodná obrazovka, herná slučka, vyhodnotenie hry, ...).
- **Player**: trieda reprezentujúca hráča, ovládanie hráča, vykreslenie postavy a schopnosti.
- **Enemies**: trieda nepriateľov, ich herná logika a pohyb smerom k hráčovi, vykreslenie postáv a schopnosti.

---
## **3. Grafika**

### **3.1 Interpretácia témy (Swarms - príklad témy)**
Hra chce byť vizuálne príťažlivá, kde pomocou assetov z itch.io boli vybrané assety hráča a následne nepriateľov, pričom nepriatelia tým, že budú na hráča útočiť vo veľkom množstve, tak boli vybrané assety rytierov a potom príšer (slime). Zameranie je na 2D kreslené objekty, ktoré budú mať minimalistické animácie pohybu.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/enemies.png" alt="Nepriatelia">
  <br>
  <em>Obrázok 3 Ukážka sprite-ov nepriateľov</em>
</p>

### **3.2 Dizajn**
V hre boli použité assety z itch.io, konkrétne Tiny Swords (https://pixelfrog-assets.itch.io/tiny-swords), s tým, že niektoré objekty budú slúžiť ako aktívne prekážky. Cieľom bolo dosiahnuť na pohľad príjemný animovaný dizajn v kontexte stredovekej fantasy. Ďalšie levely budú vychádzať z rovnakých assetov, pričom sa budú kombinovať rôzne terény a prostredia.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/level.png" alt="Level dizajn">
  <br>
  <em>Obrázok 4 Ukážka dizajnu levelu</em>
</p>

---
## **4. Zvuk**

### **4.1 Hudba**
Výber hudby do pozadia bol zameraný na RPG žánrovo orientovanú hudbu, ktorá bola vybraná z Free RPG Music Pack (https://gianni-canetti.itch.io/free-rpg-music-pack) a bude poskytovať vhodný nádych stredoveku a RPG tématiky, ktorý vhodne dopĺňa grafický dizajn hry.

### **4.2 Zvuky**
Zvuky v hre boli podobne orientované na RPG zvuky, pričom boli opätovne použité voľne dostupné assety vo forme RPG Maker Skit (https://theambientfort.itch.io/rpgmakerskit1), z ktorých bol vybraný zvuk pre výstrel ohnivej gule a zvuk pre zásah nepriateľa.

---
## **5. Herný zážitok**

### **5.1 Používateľské rozhranie**
Používateľské rozhranie bude orientované do ostatného grafického štýlu a úvodná obrazovka bude obsahovať možnosť spustiť a ukončiť hru.

### **5.2 Ovládanie**
<ins>**Klávesnica**</ins>
- **WASD**: pohyb hráča po mape.
- **Klávesy šípok**: alternatívne ovládanie pohybu hráča po mape.

<ins>**Myš**</ins> 
- **Ľavé tlačidlo**: výstrel ohnivej gule.

---

# **OT_Game_2024 - Game Design Document - EN**

The repository contains a prototype implementation of a game in Pygame, which was implemented during an exercise for the Object Technologies course. The created game presented essential game functions and the repository serves as a example for the development of a game intended for the course project.

**Author**: Ľubomír Benko

**Chosen theme**: Swarms (example)

---
## **1. Introduction**
The proposed game serves as a demonstration for the subject Object Technologies, with the aim of creating a functional prototype of the game as a project for the exam. The created game meets the requirements of the assigned topic (Swarms - example of the topic). The game has a player against the whole world character, where the player is attacked by monsters and his goal is to work his way to the goal.

### **1.1 Inspiration**
<ins>**Archero**</ins>

Archero is a game focused on a lone archer who goes through different levels, fighting with different enemies. The concept of the game is based on ***one against the whole world***, supplemented with various game mechanics that improve the main character over time in the fight against a larger number of stronger enemies. The player can improve his skills and armor in the game.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/archero.jpg" alt="Archero">
  <br>
  <em>Figure 1 Preview of Archero</em>
</p>

<ins>**Survivor.io**</ins>

Survivor.io is a mobile game focused on a single hero fighting against a large number of enemies. The goal is to survive for a set amount of time and defeat all enemies. During the fight, the player ***freely moves around the map*** and tries to survive, or find the right moment to hit the enemies. The enemies ***always chase the player*** with the aim of defeating him.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/survivor.jpg" alt="Survivor.io">
  <br>
  <em>Figure 2 Preview of Survivor.io</em>
</p>

### **1.2 Player Experience**
The goal of the game is for the player to survive a ***certain time interval in the game*** while not being defeated by a large number of enemies that rush at him and cause him injuries upon contact. The player can move around the map and at the same time eliminate enemies, which increases his chances of successfully surviving the time interval.

### **1.3 Development Software**
- **Pygame-CE**: chosen programming language.
- **PyCharm 2024.1**: chosen IDE.
- **Tiled 1.10.2**: graphical tool for creating levels.
- **Itch.io**: source of graphic assets and sounds for the game.

---
## **2. Concept**

### **2.1 Gameplay Overview**
The player controls his character and tries to survive a ***time interval*** set in the game (e.g. 90 seconds). During this time, he is ***attacked*** by enemies who spawn on the map at regular intervals. The player has the opportunity to find and use objects on the map that will help him gain safety and not be exposed to attacks from all sides.

### **2.2 Theme Interpretation (Swarms - example)**
**"Swarms"** - the player is chased by a large number of enemies, which he can kill, but they are re-spawned into the world. The enemies are always set to move towards the player and so they try to overwhelm him with a huge number. At higher levels, it is possible to increase the intensity of enemy generation and increase their resistance to the player's attacks.

### **2.3 Primary Mechanics**
- **Obstacles**: there are objects on the map that create an active obstacle for both the player and the enemies.
- **Bonus items**: the player can collect items on the map that will add, for example, life, attack power or reduce the time until the end of the round.
- **Fixed enemy spawning locations**: enemies do not spawn anywhere on the map, but have fixed locations to prevent the situation where the enemy literally spawns on the player, which reduces gameplay.
- **The player can eliminate enemies**: the player shoots a fireball that, when hitting an enemy, causes the enemy injury.

### **2.4 Class design**
- **Game**: class that will contain the main game logic (start screen, game loop, game ending, ...).
- **Player**: class representing the player, player control, character rendering and abilities.
- **Enemies**: class of enemies, their game logic and movement towards the player, character rendering and abilities.

---
## **3. Art**

### **3.1 Theme Interpretation (Swarms - example)**
The game wants to be visually appealing, where using assets from itch.io, the player's and enemies assets were selected,as for the enemies, since they will attack the player in large numbers, were selected knights' assets and then monsters (slimes). The focus is on 2D cartoon objects that will have minimalistic movement animations.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/enemies.png" alt="Enemies">
  <br>
  <em>Figure 3 Preview of enemy sprites</em>
</p>

### **3.2 Design**
The game uses assets from itch.io, specifically Tiny Swords (https://pixelfrog-assets.itch.io/tiny-swords), with some objects serving as active obstacles. The goal was to achieve a visually pleasing animated design in a medieval fantasy context. Additional levels will be based on the same assets, combining different terrains and environments.

<p align="center">
  <img src="https://github.com/l-benko/OT_Game_2024/blob/main/level.png" alt="Level design">
  <br>
  <em>Figure 4 Level design concept</em>
</p>

---
## **4. Audio**

### **4.1 Music**
The selection of background music was focused on RPG genre-oriented music, which was selected from the Free RPG Music Pack (https://gianni-canetti.itch.io/free-rpg-music-pack) and will provide an appropriate touch of the Middle Ages and RPG themes, which appropriately complements the game's graphic design.

### **4.2 Sound Efects**
The sounds in the game were similarly oriented towards RPG sounds, reusing freely available assets in the form of RPG Maker Skit (https://theambientfort.itch.io/rpgmakerskit1), from which the sound for the fireball shot and the sound for the enemy hit were selected.

---
## **5. Game Experience**

### **5.1 UI**
The user interface will be oriented towards the overall graphic style and the start screen will include the option to start and exit the game.

### **5.2 Controls**
<ins>**Keyboard**</ins>
- **WASD**: move the player around the map.
- **Arrow keys**: alternate control of player movement around the map.

<ins>**Mouse**</ins> 
- **Left button**: a fireball shot.
