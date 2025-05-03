Name: CODENAME- GalagaSurfers
Stakeholders:  
* Thavindu
* John McGuff
* Long Nguyen
* Kha Le

Overview
Concept: A hybrid 2d galaga clone and an autorunner in the same vein as some mobile games like Subway Surfers on the windows platform.

Story: TBD

Setting: TBD

Structure: The game takes place on a 2D plane with players avoiding enemies and moving forward for as long as they can until something destroys them. The game continues to increase in difficulty by spawning more and different kinds of enemies until the game ends with the player's death. As the game continues, the player gains score based on time survived and enemies destroyed. The goal of the game is to simply get as high of a score as you can before you inevitably lose.

* 1.0 Basic Menus
    * 1.1: When the game is opened, the player is shown a Start Menu
        * In Unity, this is our Initial Scene in the build.
        * 1.11: The initial scene will require user interface options that let the player start the game, quit out, or other pertinent functionality
            * This can be provided for using unity Button.TMP objects. Font can be provided for via free Unity asset Thaleah Fat Font
    * 1.2: When the player hits the Escape button, a menu should open, and the game should pause. Player should then be given the option to exit back to the initial scene or continue the game
        * This can be accomplished using a disabled canvas object in unity that is re-enabled when the player hits the Escape key, and in the same function that re-enables the menu, we can set the timescale of the game to 0 'pause' the game. The buttons in this menu can be more Unity Button.TMP objects with respective functions embedded in. 
        * When the player is ready to continue, the timescale is reset to 1 and the menu is disabled again. If the player elects to quit to the initial scene instead, we can additionally load the initial scene.
    * 1.3: The player can view High Scores in the initial scene
        * This can be accomplished by loading a scene with a UI Canvas that populates with the names and scores of the High Scorers
        * 1.31: When the game ends by the player's destruction, the player will be prompted to add their name to the high score list (if applicable)
            * This can be accomplished with another unity scene, this one similar to the previous mention, but instead with an interactable text element that the player can use to add their name to their score. We can keep track of High Scores via a text file in the project assets.

* 2.0 Player Functionality
    * 2.1: Controllable Player Character
        * Player character is controllable using keyboard controls
        * This is implemented using the Unity Legacy input system which captures keyboard inputs
    * 2.2: Moves left and right with keyboard controls
        * Using ← and → keyboard buttons on the keyboard, player can move left and right on the screen
    * 2.3: Player character fires a projectile
        * 2.31: Projectile is fired upon pressing a key
            * Upon pressing the `<SPACEBAR>` key once, the player spaceship fires a projectile
            * Keep button mashing to fire more!
    * 2.4: Powerups that alter fired projectile/player stats
        * Powerups will spawn from the top of the screen
        * Player has to catch them in order to equip
        * Two Types of Powerups
            * Projectile Powerup: 
                * Upgrades to firing two projectiles at once
            * Shield: 
                * A temporary shield provides protection from enemy attacks
                * The shield lasts 10 seconds before depleteion or if it gets hit before that
        * Powerup Drop Frequency:
            * If the Projectile Powerup is already equipped, it will not spawn again
            * The Shield Powerup will keep spawning after it has been depleted
    * 2.5: Player character can be damaged after getting hit once by an enemy
        * 2.51: Player character is briefly invincible after being hit (indicated by blinking model)
            * The player spaceship blinks three times after getting hit by an enemy attack
        * 2.52: Player has three hearts
            * The hearts are indicated on the top left of the screen
            * Each time a player gets attacked by an enemy, one heart is lost
        * 2.53: Player regenerates where they were attacked as long as there are lives
            * Player can progress from where they lost
            * Player will also lose the Projectile Powerup if it was equipped
        * 2.54: Player has to restart when all lives are lost (game over)
            * Progress from the beginning

3.0 Enemy Functionality

 3.1 Different Types of Enemies:
	 
  * 3.11 Unique Attacks and Behaviors:
	   * Different enemies have their own ways of attacking and moving. For instance, some enemies might rush straight at the player, while others might attack from far away.
	
   *  3.12 Visual Differences:
	    * Enemies look different from each other, which helps players recognize them quickly. This makes it easier for players to know what kind of enemy they're dealing with. They might have different colors, shapes, sizes, or other visual clues. It helps players make decisions faster while they're playing.

 3.2  Enemy Health:
* Enemies have different amounts of health. When players hit them, their health decreases.

3.3 Score Rewards:
* Players earn different scores for defeating different enemies. This encourages players to think strategically about which enemies to tackle

3.4 Increasing Difficulty:
* As players progress through the game, enemies become faster. This keeps the game challenging and exciting.


* 4.0 Game Environment
    * 4.1: Visually appealilng space-themed background with scrolling
        * Can accomplish this by creating a background sprite larger than the viewing size of the camera (IE bigger than the player can see), then having the background sprite fall slowly, be replaced by spawning additional background sprites above the camera, and deleted after the sprites fall below a certain threshold on the Y-axis (when it is clearly out of view)
    * 4.2: UI elements for player health, game time, score
        * This can be accomplished by using a unity canvas to instantiate the text UI objects, then running a script in the background that checks these variables each update and changes them as necessary. For example: Game time should always be increasing, and so every update the text for the timer should be incremented by itself +1.

* 5.0 Audio
  * 5.1: Sounds for gameplay
    * A variety of sound effects for different gameplay actions, e.g.:
        * Player ship movement
        * Shooting 
        * Enemy movements and attacks
        * Explosions and destruction
        * Items pick-up
    * Sounds triggered by specific game events:
        * Boss encounter
        * Power-up
  * 5.2: Background music
    * For in-game music
    * A dynamic soundtrack that adapts to the intensity or progress of the gameplay, e.g.:
        * Slow-paced when chilling
        * Fast-paced when intense
        * Game over/ Score page music
    * Music loops seamlessly
  * 5.3: Menu sounds
    * A menu music that is different from gameplay background music
    * Menu music also loops
    * Sound effects for button clicks
  * 5.4: Music and sound is adjustable 
    * Implement audio settings in the options menu for both music and sound effects independently.
    * Provide sliders UI elements for controlling audio volume levels.
