---
layout: default
title: Quests
nav_order: 4
---

# Game Design Quests and Assessments
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# Required Games

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> For this class, you are required to play two different games that we will analyze throughout the semester.

| __A Short Hike__ by adamgryu | __Celeste__ by Maddy Makes Games |
| :----------------------------: | :--------------------------------------: |
| ![A Short Hike Title Card](/assets/images/ashorthike.png) | ![Celeste Title Card](/assets/images/celeste.png)
| Available at: [itch.io](https://adamgryu.itch.io/a-short-hike), [Steam](https://store.steampowered.com/app/1055540/A_Short_Hike/), Nintendo eShop, and other platforms | Available at: [itch.io](https://mattmakesgames.itch.io/celeste), [Steam](https://store.steampowered.com/app/504230/Celeste/), Nintendo eShop, and other platforms
| _Objective:_ Complete the main story of the game | _Objective:_ Complete through the beginning of Chapter 4 with and/or without assists turned on | 
| _Estimated time to complete:_ 2 hours | _Estimated time to complete:_ 3 hours |

_Note:_ We are going to be talking specifically about the assist options in _Celeste_.  Even if you can get to Chapter 4 without the assists, make sure to play the game with them at some point to see how they work.  Also, if you need to use the assists to make it to Chapter 4, that's fine.  Try to at least get through Chapter 1 without them, however.

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png">  No submission required specifically for playing the games.

# Critical Analysis Quest

First, watch this:

<iframe width="800" height="450" src="https://www.youtube.com/embed/bb3HQlFmfds" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> What is a critical analysis, and why do we care?

Critical analysis is not just a game review. We are not concerned with how many out of five stars, or any numbers from 0 to 10, or whether or not a game is “fun” (whatever that means to you).

Critical analysis does not just mean a list of things that are wrong with the game. The word “critical” in this context does not mean “fault-finding” but rather a thorough and unbiased look at the game.

Critical analysis is useful when discussing or comparing games. You can say “I like the card game Bang! because it’s fun” but that does not help us as designers to learn why it is fun. We must look at the parts of games and how they interact in order to understand how each part relates to the play experience.

Critical analysis is also useful when examining our own works in progress. For a game that you’re working on, how do you know what to add or remove to make it better?

To complete a Critical Analysis assignment, write a paper (probably at least 2-3 pages) that does the following (and most likely somewhat in this order):

* Give a high-level description of the game, game’s history, or other introductory information you think is appropriate. I would expect also to see what you believe the games main aesthetics are here (as defined by the MDA paper).
* Describe the game’s formal elements. Do not interpret at this point, simply state what is there.
* Describe the results of the formal elements when put in motion. How do the different elements interact? What is the play of the game like? Is it effective?
* Specifically discuss the mechanics, dynamics, and aesthetics of the game.
* Try to understand why the designer chose those elements and not others. Why this particular player structure, and why that set of resources? What would have happened if the designer had chosen differently?

Some questions to ask yourself during a critical analysis at various stages:

* What challenges do the players face? What actions can players take to overcome those challenges?
* How do players affect each other?
* Is the game perceived by the players as fair? (Note that it may or may not actually be fair. Perception and reality often differ.)
* Is the game replayable? Are there multiple paths to victory, varied start positions, or optional rules that cause the experience to be different each time?
* What is the game’s intended audience? Is the game appropriate for that audience?
* What is the “core” of the game - the one thing you do over and over that represents the main “fun” part?

NOTE: Literally just answering the above questions WILL NOT result in a good score.  I expect you to put some thought into how best analyze the game you are looking at.  Some of these questions make no sense for certain games and tossing "an answer" to them in your paper would be frowned upon.

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

Submit a PDF of your paper to the appropriate assignment in [Gradescope]({{ site.data.externallinks.gradescope }}).

[An example Critical Eye on Hearthstone from Spring 2014](/assets/materials/HearthstoneCriticalEye.pdf)

You will complete this assessment at least twice: 

* once for either _A Short Hike_ or _Celeste_
* once for a game of your choosing (including the other option of _A Short Hike_ or _Celeste_) 
* optionally one more time as your Player's Choice Quest

If you choose your own game, it can be a game you have already played, although you may need to refresh your memory.  If you need some thoughts on what games to play, I'm happy to offer suggestions.  

Some content here used with permission from [Game Design Concepts by Ian Schreiber](http://gamedesignconcepts.wordpress.com/2009/07/06/level-3-formal-elements-of-games/).


# MonoGame - Level 1: Animation and Control

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Over the course of three levels, you will be building out some basic functionality for a game built on MonoGame.  Level 1 will focus on animation and control.  You are welcome to use any tutorials or example code you find, but make sure to cite any sources used in your code and in the submission to Gradescope.

1. Accept the assignment from GitHub Classroom: [https://classroom.github.com/a/qa9BdJCd](https://classroom.github.com/a/qa9BdJCd)
2. Clone the repo locally and create a new project inside this folder named "Level 1".
3. Import a sprite sheet of your choosing, but it needs to be loosly a character with the following animation states for the noted XP:
   * When standing still (either at the bottom of the Cornflower Blue window or a platform (invidible or not)), there should be a minimum 3 frame idle animation [5 XP]
   * The idle animation should be mirrored when the character is turned left or right [5 XP]
   * The character should be able to be controlled in the following way: A moves left, D moves right, W jumps [5 XP]
   * Gravity should affect the character and bring it back down to a resting state in a "reasonable" way after they jump [10 XP]
   * When the character jumps, there should be a switch to an appropriate jumping animation set [10 XP]
   * Implement one other "action" of some kind with another animation set and map it to the space bar [10 XP] (Examples could include an attack animation, a slide animation, casting a spell, etc.)

If you are looking for spritesheets and assets there are MANY available at [https://itch.io/game-assets](https://itch.io/game-assets) for free or for a small price/donation.

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

Make sure to push the final version of your code to GitHub before the deadline.

Answer the questions in [Gradescope]({{ site.data.externallinks.gradescope }}) under "MonoGame - Level 1: Animation and Control" regarding your project [5 XP].


# MonoGame - Level 2: Collision and Physics

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Building on your code from Level 1, you will now implement some basic physics and collision detection for your mini-game.

1. Before making any changes to your code, go to your repo in GitHub and create a new branch called "Level 1" so you can have a version of the code as it was before you started this next assignment.  You can now continue on your `main` branch for Level 2.  It is fine that your project is still called Level 1.
2. Add the following sprites and functionality to your mini-game:
   * Import three new sprites (these do not have to be animated): two different types of platforms and a box/crate/brick/block of some kind.  The actual sprites don't really matter as long as you can tell them apart.  [5 XP]
   * Platform type 1 should be completely solid on all sides.  The player sprite cannot jump up through it from the bottom or the side.  The player sprite should land on it and not fall through if they jump on top of it.  [10 XP]
   * Platform type 2 should only be solid from the top.  The player sprite should be able to jump up through the sprite and then land on top.  Same with jumping from the side or at an angle.  [10 XP]
   * The Box sprite should be sitting on the type 2 Platform.  The player sprite should be able to move it by pushing against it.  When the box is no longer touching the platform, it should fall to the ground (which could just be the bottom of the window or you could make an actual ground).  [10 XP]
   * Your "action" button (space bar) from Level 1 should knock the box in a straight line until it collides with another object.  Note that if your gravity is working in the item above, the box should fall as it's flying in a given direction. [10 XP]

If you are looking for spritesheets and assets there are MANY available at [https://itch.io/game-assets](https://itch.io/game-assets) for free or for a small price/donation.

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

Make sure to push the final version of your code to GitHub before the deadline.

Answer the questions in [Gradescope]({{ site.data.externallinks.gradescope }}) under "MonoGame - Level 2: Collision and Physics" regarding your project [5 XP].


# MonoGame - Level 3: Tiled Level Design

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Continuing to build on your code from Level 2, you will now create a full level using Tiled for your character to explore.

1. Before making any changes to your code, go to your repo in GitHub and create a new branch called "Level 2" so you can have a version of the code as it was before you started this next assignment.  You can now continue on your `main` branch for Level 3.  It is fine that your project is still called Level 1.
2. Using Tiled - available at [https://www.mapeditor.org/](https://www.mapeditor.org/) - create a "level" for your character to explore.  This can be just a single screen or it can scroll. 
   * Working level map [25 XP]
   * Use all three of the platforms/boxes that you had from level 2 [10 XP]
   * Have a way for the level to "end" - even if that makes the program exit [10 XP]
   * Bonus!  Have more than one map that the user can choose! [10 XP]
   * Bonus!  Add things to collect, like coins, and a counter on the screen that shows how many you collected! [10 XP]

If you are looking for spritesheets and assets there are MANY available at [https://itch.io/game-assets](https://itch.io/game-assets) for free or for a small price/donation.

There are lots of resources you can use to learn how to use Tiled with MonoGame.  The basic thing to remember is that the Tiled program isn't anything more than a graphical interface that outputs `.tmx` files.  Which are just `.xml` or you can also do `.json.`  There's no magic library here.  There are several libraries you can use to then read in the files generated by Tiled to build your level.  

* TiledCS - [https://github.com/ironcutter24/TiledCS-example-MonoGame](https://github.com/ironcutter24/TiledCS-example-MonoGame)

## UPDATE

As mentioned in class, the main learning objective here is "data-driven design."  If you build your mini-game _in some fashion_ where a level is loaded from a data file (`.csv`, `.xml`, `.tmx`, `.json`, etc) and not hard-coded into your C# code, then I believe the learning objective has been met.  If you do not use Tiled or TiledCS in the end, it is okay.  But your level __must__ be loaded from outside the code.

If you do something different, __make sure to explain it fully in the Gradescope submission.__

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

Make sure to push the final version of your code to GitHub before the deadline.

Answer the questions in [Gradescope]({{ site.data.externallinks.gradescope }}) under "MonoGame - Level 3: Tiled Level Design" regarding your project [5 XP].

# Team Game Project

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Build a game!  Okay, you need more than that... :-)  Every game will be different, so there's no way to say "you must have X feature" in reality.  But here is how the staff will evaluate your games.

__Is it a working game?__ 

Simply put, the game should function without any obvious bugs or failures.  The game should:

* play and feel like a completed product, not something still in beta form;
* have an obvious start and end to the game, with the ability to "play again," depending on the nature of the game;
* have working and understandable controls.

Points are earned for how well the game performs during playtesting.

__Is the game engaging?__

Does the game grab the player and make them want to play more?  A successful game will:

* draw the player in and entice them to keep playing;
* have a unique and interesting mechanic;
* feel good to play (appropriate controls, difficulty, etc.);
* be fun/enjoyable to play.

__Does the game meet its aesthetic goals?__

Can a staff member quickly and easily identify one or two aesthetics from your game?  Does your game focus on and emphasize those aesthetics?

__How polished / refined is the game?__

We do not expect perfect art assets or anything like that.  We do expect the game to look “put together,” is playable, and feels like something that could be given to someone not in the class and they could play it without a ton of assistance.

__How did the team work together?__

Game documentation, team evaluations, use of GitHub all fall under this category.  XP is earned here through:

* high evaluation marks from teammates;
* the documentation submitted follows the outline and contains all necessary information;
* GitHub was used effectively, showing good software development techniques.

### Setup and GitHub Classroom
{: .no_toc }

* One member of your team should accept the GitHub Classroom assignment at [https://classroom.github.com/a/lSFanMG-](https://classroom.github.com/a/lSFanMG-) and name the repo the name of your game.
* I expect your team to use good development practices with git, branching, etc.
* You can use any frameworks/libraries that you find available.  Make sure to cite them!

### Project Check #1

At this stage, you must have:

* The repo initialized
* The project created and can launch to at least Cornflower Blue
* Some ideas/examples of what your sprites/assets could be

You do not have to have any significant functionality at this point.  However, note that your design document is also due on the same day!

### Project Check #2

At this stage, you must have:

* Your basic mechanics working to the point that they can be demoed
* More sprites/assets in the game

You do not have to have done any significant level design at this point.

### Project Beta

At this stage, you must have at least two levels (or whatever equivalent that is for your game) that are fully functional and can be played by someone NOT on your team without significant instruction or guidance.  We will be doing playtesting of games and the game needs to be up and running!

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

In the root of your repository, create a `README.md` file that contains the following sections in this order, with headings identified to make it easier to read through the document.  Also include this information in a PDF that is submitted to Gradescope.

* Name of game
* List of all team members, including computing IDs
* GitHub link (PDF for Gradescope Only)
* Game pitch - Two to three sentences describing your game (you can reuse old text for this from previous assignments)
* How to play - What do we need to know in order to play the game?  Controls?  Setup?  Anything and everything you think we need.
* Amount/type of content available - Explain how many levels, what major features are available, etc, basically so we don’t miss anything you created
* Lessons learned - What did you learn about game development through this process?

[Team Game Final Submission Document Template](https://docs.google.com/document/d/1zhqKBV7OHbZoCVR6CzlDwDwYkzRhCN8ccM4Gmz6dU7A/edit?usp=sharing)

# Team Game Physical Prototype

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Using the materials provided, create a physical prototype of some aspect of your game.  This could be a level or a mechanic, but it should be something that is:

* Representative of your game
* Shows part of your design process for your game
* Is "playable" in some fashion
* Shows some thought was put into the design

Basically, the goal is to do a "rough draft" of some aspect of your game to help you think about how you will translate your design into code.  Consult the prototyping chapters of Fullerton for more information.

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

One member of your team should fill out the following document: [Physical Prototype](https://docs.google.com/document/d/1xAbtTfR1nKugrc1_TnFsWR_ZMQO8VLz_PgU0n6BCS8A/edit?usp=sharing)

As a part of this document, you MUST have pictures of your prototype!  

We will also be demoing these in class on Monday, March 20.  Make sure yours is ready by then!  (The final version of the document is not due until 11:59 that night.)

Submit the document into Gradescope, making sure to add all team members when submitting.


# Team Game Design Document

## Quest Information
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/quest.png"> Based on the generic game design document by Benjamin Stanley and Alec Markarian @ [https://dkrikun.files.wordpress.com/2016/11/game-templatea-strategy.pdf](https://dkrikun.files.wordpress.com/2016/11/game-templatea-strategy.pdf), complete your own game design document from this Google Doc template: [https://docs.google.com/document/d/19fnqYeRXly8SpMzW-6bxTWp-Dn4pprCihvJw_edlhtE/edit?usp=sharing](https://docs.google.com/document/d/19fnqYeRXly8SpMzW-6bxTWp-Dn4pprCihvJw_edlhtE/edit?usp=sharing).

## Quest Submission
{: .no_toc }
<img style="float: left; padding: 10px" src="/assets/images/turnin.png"> 

One member should submit the design document as a PDF into Gradescope, making sure to add all team members when submitting.