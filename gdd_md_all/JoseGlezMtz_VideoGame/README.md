# **Forest Adventure**

## _Game Design Document_

---

##### José Antonio González Martínez, Valentina González, Enrique Martínez

##
## _Index_

---

1. [Index](#index)
2. [Game Design](#game-design)
    1. [Summary](#summary)
    2. [Gameplay](#gameplay)
    3. [Mindset](#mindset)
3. [Technical](#technical)
    1. [Screens](#screens)
    2. [Controls](#controls)
    3. [Mechanics](#mechanics)
4. [Level Design](#level-design)
    1. [Themes](#themes)
        1. Ambience
        2. Objects
            1. Ambient
            2. Interactive
        3. Challenges
    2. [Game Flow](#game-flow)
5. [Development](#development)
    1. [Abstract Classes](#abstract-classes--components)
    2. [Derived Classes](#derived-classes--component-compositions)
6. [Graphics](#graphics)
    1. [Style Attributes](#style-attributes)
    2. [Graphics Needed](#graphics-needed)
7. [Sounds/Music](#soundsmusic)
    1. [Style Attributes](#style-attributes-1)
    2. [Sounds Needed](#sounds-needed)
    3. [Music Needed](#music-needed)
8. [Schedule](#schedule)

## _Game Design_

---

### **Summary**

Forest Adventure" is a TCG that tells the story of our seven characters trying to defend their camp which is suddenly invaded by creatures from another dimension.... themselves. Our campers and staff have the responsibility to defend the camp at all costs with the help of multiple power ups and each other.

### **Gameplay**

The game consists of a P v CPU where players will fight against the different creatures trying to attack their campsite. Before the match starts, you will be able to select 5 cards from the different characters that are available as well as which two cards you wish to start fighting with.

When the match begins, the user will be assigned to either one of the sides. Each player will have 2 characters on the board and 3 in their hand. Each character has different abilities and statistics that will define their fighting style. Each round you'll have different options such as using your character's abilities to boost other allies or attack enemies as well as swapping between your active campers. In addition, remember to use your power ups to boost your team throughout the battle.

The game will end when either your campers defeat all the monsters or lose their lives at battle. 
### **Mindset**

We want players to feel ambitious about progressing in the game. We aim for them to sense the ability to create their own strategies within the arena and to improve their proficiency in the game's mechanics.

## _Technical_

---

### **Screens**

1. Title Screen
    - Play Game
    - Build-Deck
    - Exit
2. Build-Deck
3. Play_game
4. Register Player
5. Login

**Temporary Title Screen**

![Title Screen](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/TitlePage.png)

**Playing Screen**

![In-Game Scene](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/game%20scene.png)

**Example of deck scene**

![Deck scene](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/deck%20scene.png)

This is where the player will create his deck. The 'Add' button is to add the selected character to his deck, the 'Remove' button to remove this character, and the 'Save' button is for saving your deck. The images of the characters that are at the bottom of the screen are the ones that are in your deck.

**Final Game Scene**
![In-Game Scene](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/finalGameScene.png)

**Final Deck Scene**
![In-Game Scene](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/finalDeckScene.png)

**Final Starting Scene**
![In-Game Scene](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/finalTitleScene.png)

### **Controls**

The player will interact with all the UI with the mouse and by clicking on the buttons

### **Mechanics**
![Mechanics Image](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/mechanics.png)

#### Before the game:
Before starting the game, the player have the option to configurate their deck of 5 characters, giving them the option to create a team based on the best strategy that the player considers. Additionaly, players can select two cards which will be the first ones they use when starting the game.


#### In-game:
At the start of the match, 2 cards will be sent into battle whilst the other three will wait in the bench.

At the start of each round, the player will obtain a "Power-up" card, and will have two options:

1. Use it in a card that is on the field
2. Save it to for a later round
   1. Some cards have a limit toime to save it, maening that after specific number of rounds, they will disapper
   2. If the powr-ups deck run out of cards, it will shuffle and reestart again
  
After this, the player will have several option:

1. Attack the enemy: this attack will cost certain amount of energy.
2. Change a card: The player can swap a character with one card from their hand. The player can only perform this action if they haven't attacked an enemy card and after swapping two of their cards, their turn will automatically end.
3. End turn: The player can chose to end their turn if they can not use any other ability or if they want to save energy for later rounds or execute any other strategic maneuver.

   
At the end of the turn, the energy bar will restore a given amount depending on which round they are currently in.
After the player's turn, the enemy will follow a similar flow, with stronger enemies on each new round.

## _Rounds Design_

Every time the player wins a round, new stronger enemies will be spawned. Thus, making new rounds more challenging to win.

### **Game Flow**

1. The player register
2. Players' log-in
3. Create the deck
4. Enters battle

## _Development_


### **Abstract Classes / Components**
1.Register Manager
2.Login Manager
3.Buld_deck manager
4.BoardManager 
    1. Cards Manager
    2. Enemy Controller
    3. Power Ups Manager
4.Scene Manager
5.Conection with the API
6.Audio controller


## _Graphics_

**Card Template:**

![Wendy Card Design](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/wendy.png)

**Initial Character Models**
![Early character models](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/initialCharacterModels.png)


### **Style Attributes**
**Color Palette:**
![Color Palette](https://github.com/JoseGlezMtz/VideoGame/blob/main/VideogameProject/Assets/colorpalette_forestAdventure.png)

**Graphic Style:** The style that we decided to use is a 2d cartoony inspired by the animation of the Disney series Gravity Falls which is a simple style with minimal, flat shadows and a black outline for the key elements in the scene. 

### **Graphics Needed**

1. Cards
    1. Characters
    2. Power Ups
2. Backgrounds
    1. Main Page
    2. In-Game
    3. Deck Building
3. UI
    1. Buttons
    2. Energy Bar
    3. Win/Loss sign
    4. Character statistics (health, speed, resistance)
4. Animations

## _Sounds/Music_

---

### **Style Attributes**

We're looking for a soft music for the main menu, something that transmite a forest vibe, that make the player to feel inside the camp, but also in the match we want them to feel the tension of the fight.

## _Schedule_

---
Week 1
    1. Unity
        1. Start cards in positions
        2. Attack and change mechanic
        3. Main menu
    2. Data base
        1.Creation of data base
Week 2
    1.Web Page
        1.Create Power ups
        2.jrn
   2.Unity
   3. Data Base
Week 3

Week 4
    1. Web Page
    2. Unity
    3. Data Base
Week 5 
    1.Web Page
        1. Design
        2. Receive and send stats information
    2. Unity
        1. Game Music
        2. Implement new rounds
        3. Improve Deck UI
    3. Data Base
        1. Create Views for statistics
Week 6
    1. Web Page
        1. Display statistics
        2. Create Build
    2. Unity
        1. Enemies made stronger
        2. Finish Scenes UI
    3. Data Base
        1. Balance Cards


