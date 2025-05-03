# Hunted
A survival horror pattern recognition game.

_You are being hunted! Can you find the hunter before he finds you first?_

* [Try it](https://github.com/Slideshow776/Hunted/releases/latest) on desktop and Android.
* [Play it](https://play.google.com/store/apps/details?id=no.sandramoen.hunted) on Google Play.

[![Image link of a youtube trailer](https://user-images.githubusercontent.com/4059636/157228448-7ee6e08a-4926-4321-ab8e-168ea120e5bf.png)](https://www.youtube.com/watch?v=trP7xkboZHk)

![demo of the game](https://user-images.githubusercontent.com/4059636/155588323-9d5097fd-37f3-4dfe-90b4-8d3932e36ab8.gif)

The hunter looks like this

![idle](https://user-images.githubusercontent.com/4059636/156218407-f857740f-33b2-4071-9c85-a2adef5868b7.png)


Read on below for project specifics.

1. [Game Design Document](#game-design-document)
2. [Credits](#credits)
3. [Project Comments](#project-comments)
4. [Other](#other)
5. [Project Kanban Board](https://github.com/Slideshow776/Hunted/projects/3)



## Game Design Document

1. Overall Vision
    * **Write a short paragraph explaining the game:**
    
        A single player pattern recognition game set in an alien forest. You are being hunted! If you spot the hunter first, you might just have a chance to get away.
            
    * **Describe the genre:**

        A hidden object pattern recognition game.
        
    * **What is the target audience?**

        The game is appropriate for children older than 8 (maybe?) and is thought to be enjoyed by casual gamers. The target platform is Android devices and on Desktop.
        
    * **Why play this game?**

        The challenge presented is to find the hunter amongst an alien forest, and discover the story dialogue as it develops. Gameplay sessionss only meant to be a few minutes long. The unique theme is complemented by visual effects and other telltale gameplay information.
       
    
2. Mechanics: the rules of the game world
    * **What are the character's goals?**

        To find and click the hunter before the time runs out.
           
    * **What abilities does the character have?**

        No abilities, the entire game world is presented at once, and the controls are only to click.
        
    * **What obstacles or difficulties will the character face?**

        The hunter to be found is camouflaged and is therefore hard to spot. The forest is big and the hunter is tiny, further increasing the difficulty. The forest is also alive in its own sense of movements and other distractions.
        
    * **What items can the character obtain**

        No items.
        
    * **What resources must be managed?**

        Time is the only resource to be managed, as to give a sense of urgency fitting to the situation and further increasing the difficulty.
    
        
3. Dynamics: the interaction between the player and the game mechanics
    * **What hardware is required by the game?** 

        * Android devices needs to have a functional touch screen.
        * Desktop needs to have a functional mouse and screen.
        
    * **What type of proficiency will the player need to develop to become proficient at the game?**
       
    * **What gameplay data is displayed during the game?**
    
    * **What menus, screens, or overlays will there be?**
   
    * **How does the player interact with the game at the software level?**
    
4. Aesthetics: the visual, audio, narrative, and psychological aspects of the game
    * **Describe the style and feel of the game.**
   
    * **Does the game use pixel art, line art, or realistic graphics?**
        
    * **What style of background music, ambient sounds will the game use?**
       
    * **What is the relevant backstory for the game?**
        
    * **What emotional state(s) does the game try to provoke?**
       
    * **What makes the game fun?**
        
5. Development
    
    * **List the team members and their roles, responsibilities, and skills.**    
    This project will be completed individually; graphics and audio will be obtained from third-party websites that make their assets available under the Creative Commons license, and so the main task will be programming and creating some graphics.
    
    * **What equipment is needed for this project?**    
    A computer (with keyboard, mouse, and speakers) and internet access will be necessary to complete this project.
    
    * **What are the tasks that need to be accomplished to create this game?**    
    This project will use a simple Kanban board hosted on the project's GitHub page.
    The main sequence of steps to complete this project is as follows:    
        * Setting up a project scaffold
        * **Programming game mechanics and UI**
        * **Creating and obtaining graphical assets**
        * Obtaining audio assets
        * Controller support
        * **Polishing**
        * Deployment

    * **What points in the development process are suitable for playtesting?**    
    The main points for playtesting are when the basic game mechanics of the level screen are implemented, and when it is visualised. The questions that will be asked are: 
        * Is the gameplay and UI understandable?
        * Is the gameplay interesting?
        * How do the controls feel?
        * How is the pace of the game?
        * Are there any improvement suggestions?        
    
    * **What are the plans for publication?**
    This game will be made available for free on desktop. It will be deployed on the Google Play store for a small fee and advertised to various indie game-portal websites (LibGDX, Reddit, ...). Gameplay images and a trailer video will be posted and marketed via social media.

## Credits
* Ambient forest sounds by [klankbeeld](https://freesound.org/people/klankbeeld/) on [freesound.org](freesound.org).
* Music by [neolein](https://freesound.org/people/neolein/) on [freesound.org](freesound.org).
* Voice acting by the talented Øystein Sjøtveit.

## Project comments
* Found out `.ttf` fonts can have a shadow, like this:
   ```
   fontParameters.shadowColor = Color(0f, 0f, 0f, .25f)
   fontParameters.shadowOffsetX = 2
   fontParameters.shadowOffsetY = 2
   ```
   
* Music can be started at arbitraty positions like this: 
   ```
   ambient1Music.position = MathUtils.random(0f, 97f)
   ```
   This particular setup randomizes ambient music (in seconds), so that the player dosen't hear the same sounds upon starting a new game.
   
 * Voice-over flowchart:
![image](https://user-images.githubusercontent.com/4059636/156520718-4329fef7-e3a1-4dcd-8409-5537fc59a320.png)

## Other
For other project specifics check out the [commits](https://github.com/Slideshow776/Hunted/commits/main).

[Go back to the top](#hunted).
