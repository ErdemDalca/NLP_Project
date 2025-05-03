# Game Design Document (GDD)

## Game Overview
<p align="center">
  <img src="MarkdownResource\title.png", width = 700>
</p>
"Just 5 More Minutes" is a 2.5D action roguelike game. Players will assume the role of the Chief Archmage of the Italian Mage Association, who inadvertently triggers a world-scale catastrophe in their quest to resurrect a beloved person. Players must endure for 5 minutes amidst waves of monsters to complete the ritual of reviving their loved one.

The game draws inspiration from the "Hades" and the "OPUS" game series. It incorporates the unique growing mechanics of "Hades" deviating from the traditional roguelike model. Meanwhile, its narrative and background story are influenced by the "OPUS" game series.

The game is targeted towards a general audience of gamers and doesn't cater to a specific group, making it suitable for players of all ages. Players can range from seasoned roguelike enthusiasts who enjoy experimenting with different gameplay mechanics to newcomers who have never experienced a roguelike game before.

## Story and Narrative

### 📔Backstory:
In a distant future where multidimensional materials have revolutionized reality manipulation, the Italian Mage Association stands as a pinnacle of power and knowledge. The protagonist, once a brilliant mage and now the Chief Archmage, undertakes a forbidden ritual to resurrect his beloved. However, this desperate act unleashes unforeseen consequences, leading to a cataclysmic event that threatens the world.

### 📼Setting:
The game is set in a world where advanced technology and magic coexist. The Italian Mage Association is located in a grand citadel at the heart of an enchanted city.

### ⚔Main Conflict:
The main conflict centers on the protagonist's attempt to resurrect his loved one and the unintended consequences that result from this desperate act. The cataclysmic event triggered by the ritual releases a wave of monstrous creatures, and the protagonist must now battle through hordes of these creatures.

### 📓Story Progression:
As players progress through the game, they will uncover fragments of the protagonist's past. With each defeated wave of monsters, he will gather valuable resources, unlock new spells, and gradually unveil the story between him and his loved one. The narrative unfolds through hidden journals, and enigmatic glyphs scattered throughout the world.

### 🙎‍♂️Characters:
<p align="left">
  <img src="MarkdownResource\character.png", width = 70>
</p>
Protagonist (Player Character): The Chief Archmage of the Italian Mage Association, driven by love and remorse. Their deep connection to the beloved fuels their determination to reverse the tragedy they inadvertently caused. Players will experience the protagonist's growth, regrets, and inner conflicts as they strive to mend their mistake.

Beloved: The person the protagonist seeks to resurrect. Their background and relationship with the protagonist are revealed gradually, adding emotional weight to the story.

Monstrous Entities: These creatures are the result of the protagonist's ritual gone awry. As players engage with them, they might uncover hidden truths about the catastrophe.

### 👨‍👩‍👧‍👧Character Relationships:
The protagonist's relationship with the beloved drives the narrative, encapsulating their longing and desperation.

### 🥅Character Goals and Personalities:
The protagonist's goal is to resurrect his beloved and rectify the disaster he caused. His personality evolves from a determined and grief-stricken mage to a more complex individual seeking redemption.


## Gameplay and Mechanics
### <strong>1.🎦Player Perspective:</strong>
The player perspective of this game will be a ``Top-down 2.5D perspective`` between 2D and 3D. We will use a camera in 3D space but choose ``orthogonal projection`` to capture players and game interfaces to showcase the effects of a 2D game. Yes, the plane of the game will be perpendicular to the x-axis and parallel to the z-axis. The character controlled by the player is like this. 


<center><span style="color:Aqua"><strong>The camera in the game</strong></center>
<p align="center">
  <img src="MarkdownResource\camera.png", width = 500>
</p>

In the game, the camera always follows the player, but not entirely. I applied some small magic to the camera!

<center><span style="color:Aqua"><strong>Camera looking foward</strong></center>
<p align="center">
  <img src="MarkdownResource\CameraLookingForward.gif", width = 500>
</p>

Causing the center of the lens to deviate from the player and shift in the corresponding direction when the player moves in a certain direction. Then, after the player stops moving, the center of the lens is restored to the player (also known as the lookahead effect). In addition, the process of the camera chasing the player will be smooth. These features can be easily implemented through powerful camera plugins.



### <strong>2.🎮Controls:</strong>
<strong>Character Movement:</strong>

Players can use the traditional W, A, S, D keys to control the character's movement in the game.

<strong>Dodge/Dash:</strong>

Press the Shift key to make the character perform a dodge or dash action.
<p align="left">
  <img src="MarkdownResource\360_controls.gif", width = 300>
</p>

```c#
void Update()
{
    float horizontal = Input.GetAxis("Horizontal");
    float vertical = Input.GetAxis("Vertical");

    Vector3 movement = new Vector3(horizontal, 0.0f, vertical);
    transform.Translate(movement * speed * Time.deltaTime, Space.World);
    if (Input.GetKey(KeyCode.LeftShift))
    {
        // do the dashing
    }
}
```
<strong>🎯Aim Control:</strong>

Use the mouse to control the character's aiming.
Then... Press the left mouse button to make the character shoot projectiles. 
<p align="left">
  <img src="MarkdownResource\mouseclick.gif", width = 300>
</p>
Fire！！！💢

```c#
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
RaycastHit hit;
if (Physics.Raycast(ray, out hit))
{
    // adjust aim point
}
if (Input.GetMouseButtonDown(0))
{
    // shooting projectiles
}
```


### <strong>3.🌟Progression:</strong>
<strong>💪Challenge:</strong>

Players are tasked with surviving under the constant onslaught of mutated pizza monsters for 5 minutes. During this time, players must constantly dodge close-combat attacks (through collision detection) and ranged bullet barrages from the pizza monsters, all while using their own weapons and bullets to fend off the relentless wave of foes.

<strong>😈Difficulty:</strong>
<p align="left">
  <img src="MarkdownResource\monster.png", width = 300>
</p>

The objective is to survive the mutant pizza monsters' assaults for 5 minutes. Within this brief timeframe, adversaries become progressively stronger as you endure. Specifically, for every minute that passes, the challenge escalates. This might manifest as new types of pizza monsters with augmented abilities, such as firing bullets at the player, teleporting, or suddenly altering their speed. Moreover, the frequency at which these creatures spawn increases, intensifying the pressure of survival.

<strong>🏆Victory/💀Defeat Conditions:</strong>
<p align="left">
  <img src="MarkdownResource\healthpoint.gif", width = 300>
  <img src="MarkdownResource\loss.gif", width = 300>
</p>


The ultimate goal for players is to survive for five minutes without their health reaching zero. Upon achieving this, the pizza mutation event concludes, and the player is declared victorious. Conversely, if the player's health gets depleted within these 5 minutes, the game ends in defeat.

<strong>💯Scoring System:</strong>

Survival isn't the only objective; those aiming for a higher score should focus on defeating more enemies and collecting more coins.

| item         | score    
| -------- | -------- 
| health remain  | 100score/point    | 
| destroy level1 monster  | 1score/monster    | 
| destroy level2 monster    | 2score/monster    | 
| destroy level3 monster    | 4score/monster    | 
| destroy level4 monster    | 8score/monster    | 
| destroy level4 monster    | 8score/monster    | 
| collect coins| 1score/coin|


<strong>🥳Incentive to Keep Playing:</strong>

The randomized ability upgrade system ensures every game session offers players a distinct experience. Experimenting with various ability combinations to achieve diverse outcomes and aiming for higher scores provides a compelling reason for players to remain engaged.


### <strong>4.🧠Gameplay Mechanics:</strong> 

<strong>🔶What can player do：</strong>


As a legendary Italian, you can manipulate your character's movements to avoid Pizza Monster attacks, or fire barrages at them to counterattack. You can also pick up coins on the ground to enhance your abilities, everything is for survival, waiting for the end of the pizza mutation event！

<strong>🔺Core: Upgrades & Abilities:</strong>

Embracing the roguelite genre, a vast upgrade system has been integrated. Defeating pizza monsters yields random coin drops.
<p><img src="MarkdownResource\coin.gif", width = 50><img src="MarkdownResource\coin.gif", width = 50><img src="MarkdownResource\coin.gif", width = 50><img src="MarkdownResource\coin.gif", width = 50><img src="MarkdownResource\coin.gif", width = 50></p>

Accumulating sufficient coins grants players an upgrade opportunity, allowing them to 
choose from three randomly drawn abilities to enhance their character. The myriad of available upgrades promises a unique gaming experience each time：
<p align="left">
  <img src="MarkdownResource\ab.png", width = 300>
</p>

* Ranging from bullets that can split, 
* Automatic tracking missile 
* Explosive bullet 
* Or even enhanced mobility and maximum health.

Every time you upgrade, you have the opportunity to choose various powerful abilities to strengthen yourself. Through the mechanism of randomly combining abilities, you can experience the powerful power displayed by combining different abilities together. In this way, you can better face stronger enemies and survive longer. 5 mins are'nt so long!


## Levels and World Design
<strong>📜Levels Design:</strong>

In this game, the term "levels" does not refer to distinct stages or maps, but rather to the escalating difficulty and complexity over the duration of gameplay. This progression is segmented based on time, with every passing minute introducing heightened challenges for the player.

🕒 Time based difficulty progression:


<strong>Minute 1:</strong> The beginning is an introduction to familiarize players with control and basic mechanisms. The initial enemy, or "pizza monster," will be a basic type with predictable patterns and slower movement.

<strong>Minute 2:</strong> As the second minute approaches, the second level pizza monsters will begin to generate on the map. These enemies may have slightly more health, faster movement, or new and unexpected behaviors to keep players alert.

<strong>Minute 3:</strong> Monsters at the third level begin to appear, not only will they become stronger, but they may also have new abilities. For example, some people may fire shells, making evasion and movement more critical. The reproduction rate of these organisms has increased, ensuring that the screen is always full of challenges.

<strong>Minute 4:</strong> In this stage, players will face the most advanced pizza monsters to date. They may have the ability to teleport, unstable movement modes, and even summon other smaller monsters. The environment has become a crazy battlefield, requiring players' maximum attention and skills.

<strong>Minute 5:</strong> The final paragraph is a true test of everything the player has learned. The attack of pizza monsters is ruthless, with each type of enemy attacking the player simultaneously. Their movement speed has reached its peak, and players must use every ability upgrade and strategy they acquire to confront huge challenges.

During these five minutes, players are not only battling pizza monsters, but also battling the ticking clock, making every decision and action crucial. Essentially, a level is the climax of a challenge, ultimately reaching an exhilarating climax, ensuring that players always invest and strive to reach the finish line.

<strong>🌍World Design:</strong>

This world will be a flat ground, with some stones and trees as obstacles to increase the difficulty for players to avoid enemies. 
<p align="left">
  <img src="MarkdownResource\world.png", width = 300>
  <img src="MarkdownResource\range.png", width = 300>
</p>
In addition, there are boundaries in this world. At the beginning of the game, the player is born in the center of the map, centered around the player's birth point, and the area outside the radius of about 100 player positions is inaccessible. This means that players cannot flee in one direction all the way. The pizza monsters in the game world will be randomly generated around the player and move towards them. Players need to learn to navigate with enemies in this limited space


## Art and Audio
### <strong>1.🎨Art Style:</strong>
<strong>✨Main Style：</strong>
The main artistic style of this game will use pixel art, a style commonly used in early electronic games. It is created at lower resolutions, using pixels as the basic units of art. In this style, each pixel represents a small dot in the image, and different colors of pixels are arranged to form the entire image.

In line with other pixel art creations, this game will simplify and abstract images to convey fundamental characteristics of objects, characters, or scenes rather than pursuing intricate details.
<p align="center">
  <img src="MarkdownResource\ChangeToPixelStyle.png", width = 500>

Due to the discrete nature of pixels, lines and edges tend to appear very distinct and sharp. Therefore, we plan to use this characteristic by using obvious color boundaries to emphasize shapes. For instance, using darker lines for outlining objects.
<p align="center">
  <img src="MarkdownResource\ObviousColorBoundaries.png", width = 500>
</p>

<strong>🖋️Main tone：</strong>
Given that the game is set in a futuristic world, the main tone will choose darker and cool colors. Additionally, some high-luminance and highly saturated colors will be included to describe a sense of futuristic technology.
<p align="center">
  <img src="MarkdownResource\FuturisticTechnologyTone.png", width = 500>
</p>
An example of utilizing such a main tone can be found in "Hyper Light Drifter," where a similar approach is used to depict its futuristic setting.
<p align="center">
  <img src="MarkdownResource\HyperLightDrifter.png", width = 500>
</p>

<strong>💻2.5D technology：</strong>
Additionally, as mentioned before, the game will use 2.5D technology. This technique combines both 2D and 3D elements to create a distinctive visual effect. It retains the stylistic elements of 2D while adding a sense of depth and dimensionality, just like controlling a paper character moving in 3d environment.
<p align="center">
  <img src="MarkdownResource\PaperMario.png", width = 500>
</p>
Similar to "Octopath Traveler," this game will combine both 2.5D and pixel art styles.
<p align="center">
  <img src="MarkdownResource\OctopathTraveler.png", width = 500>
</p>

<strong>🦸🏻Character Design：</strong>
Since the theme of "Italians Battling Pizzas" is somewhat absurd and humorous, it is not suitable for a serious and realistic style. Therefore, the design for character and monster will be cute.
<p><img src="MarkdownResource\character.png", width = 80><img src="MarkdownResource\pizza.png", width = 80><img src="MarkdownResource\pizza2.png", width = 80></p>


### <strong>2.🎼Sound and Music:</strong>
The game's sound and music will use 8-bit style. This type of music is typically low-fidelity, but it is also very unique and leaves a lasting impression on players. We chose the 8-bit style of music because it suits for pixel art style and also has a sense of futuristic technology.

[▶️example 8-bit style music](https://youtu.be/HzO9wW6ZOiY)

<strong>🥁Sound Effects：</strong>
We have divided the game's sound effects into three categories: system sound effects, item sound effects, and battle sound effects. They include:
| SE type         | content    
| -------- | -------- 
| System Sound Effects  | Selection, confirmation, and cancellation sound effects. These sound effects are typically composed of single notes or short sequences of 2 to 3 notes.    | 
| Item Sound Effects  | These include sound effects for coin drops, item pickups, etc. These will simulate real-world sound effects - and they will be processed to fit the 8-bit style as well. Like the system sound effects, these will also be short.    | 
| Battle Sound Effects    | This category includes sound effects for character attacks, magic effects, and getting hurt. These types of sound effects are not commonly heard in real life, so we will refer to movies, TV shows, and other games for inspiration and reference when selecting and creating them.    | 

<strong>🎹Background Music：</strong>
Similarly, the music will be divided into main menu music, story music, and battle music:
| BGM type         | content    
| -------- | -------- 
| main menu music  | Music played in the main menu before entering the game. The melody will be light and soothing, setting the tone for the upcoming gameplay.    | 
| story music  | Music played during story progression, such as serious music for background narration and happy/sad music for win/lose scenes.    | 
| battle music    | This music will loop during battle phases, and it will become increasingly tense as the battle progresses.    |

### <strong>3.📋Assets:</strong>
The following are some of the graphics and audio resources that will be used in the game:

<strong>🎨Graphics:</strong>
- Character and monster images: Using Aseprite to create.
- Map tiles and item images: Purchased from the Unity Asset Store. [https://assetstore.unity.com/2d](https://assetstore.unity.com/2d)
- Story CG (Computer Graphics): Commissioned from a professional illustrator.

<strong>🎼Sound Effects & Music:</strong>
- Sound Effects: Create using the Magical 8bit Plug or downloaded from websites such as <p>
MaouDamashi: [https://maou.audio/category/se/se-8bit/](https://maou.audio/category/se/se-8bit/).
- Music: Download from websites like <p>
MaouDamashii: [https://maou.audio/category/bgm/bgm-8bit/](https://maou.audio/category/bgm/bgm-8bit/)<p>
otonosono: [http://oto-no-sono.com/](http://oto-no-sono.com/) <p>
T-STUDIO: [https://tnosite.com/en/contents-3/](https://tnosite.com/en/contents-3/)<p>
or commissioned from a professional 8-bit composer if necessary.

## User Interface (UI)
### 1.Main screen：
<p align="left">
  <img src="MarkdownResource\ui4.png", width = 500>
  <img src="MarkdownResource\ui3.png", width = 500>
</p>
### 2.Game screen：
<p align="left">
  <img src="MarkdownResource\ui2.png", width = 500>
  <img src="MarkdownResource\ui.png", width = 500>
</p>

## Technology and Tools

### 1. Game design: Unity 2022.3.5 (LTS)

[unity](https://unity.com/)

Unity is the platform for creating and operating real-time 3D interactive content. All creators, including game developers, artists, architects, automotive designers, film and television, bring their ideas to life with Unity, a complete software solution for creating, operating, and realizing any real-time interactive 2D and 3D content on mobile phones, tablets, PCs, consoles, augmented reality, and virtual reality devices.

 

### 2. Code editor: VS Code v1.81

[vscode](https://code.visualstudio.com/)

VS Code (Visual Studio Code) is an open source, free and cross-platform code editor. It does a great job in terms of performance, language support, and open-source community. 

VS Code is positioned as an editor, not an IDE, but VS Code is much richer in features than a normal editor. 

It has many features, such as:

- Cross-platform support for MacOS, Windows and Linux.
- The source code of VS Code is open source under the MIT protocol.
- Support for third-party plug-ins, powerful features and a complete ecosystem.

 

### 3. Pixel drawing software: Aseprite v1.3-rc6

[Aseprite](https://github.com/aseprite/aseprite)


Aseprite is an open-source software dedicated to drawing pixel art, users can download the source code on GitHub to compile it into runnable software by themselves, or you can buy it on the official website or steam platform.

Its main features are:

- Sprites are composed of layers & frames as separated concepts.
- Support for color profiles and different color modes: RGBA, Indexed (palettes up to 256 colors), Grayscale.
- Animation facilities, with real-time preview and onion skinning.
- Export/import animations to/from sprite sheets, GIF files, or sequence of PNG files (and FLC, FLI, JPG, BMP, PCX, TGA).

<p align="center">
  <img src="MarkdownResource\Aseprite.png", width = 500>
</p>



### 4. Music editor: Fruit Loops Studio

[FL Studio](https://www.flstudio.com.au/)

FL Studio offers a note editor, which allows you to edit the rhythms of any instrument, such as drums, cymbals, gongs, piano, flute, cello, zither, yangqin, etc., according to the composer's requirements.

Secondly, it provides a sound effects editor, which can edit all kinds of sounds for different music requirements, for example, all kinds of sounds in a particular musical environment to show the high, low, long, short, continuation, intermittent, flutter, burst and other special sound effects.

The software also provides a convenient and fast audio input, for the music involved in the sound of special instruments, as long as through a simple external recording can be conveniently called in FL Studio, the audio source of the convenient collection and simple call FL Studio created a strong editing capabilities.

 

### 5. Project management: Monday

[Monday](https://monday.com/)

Monday is an efficiency tool with excellent compatibility for different industries, which can be used by freelance designers to manage projects, as well as projects that require the collaboration of multiple teams.

There are many reasons for choosing Monday. One of the most important things is that Monday is customizable. This project management tool makes it easy to customize your workflow and you don't have to adjust your workflow to match the tool.

The visual design of Monday is also an outstanding feature. The designers of the tool have made it easy to use with the help of colors, and as a user you can easily determine the status of tasks and projects by their colors and status.

In addition, Monday is very mobile-friendly.

