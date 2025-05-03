# Introduction

I was given this assignment by Microverse to complete within 5 days. The main goal was to create a simple shooter game with Phaser 3, the process of development is as follow:

# Story:

This is a game in the spirit of the old school retro shooter game such as Asteroids or Space Invaders. This is a game developed to pay homage to the retro games of the past: my childhood.

# Main Dynamics:

- One Live
- Score as many points as you can
- Try to make it to the top 5 worldwide!
- Share your accomplishment with the rest of the world (or maybe just your friends)

# Development

## 1 Day Tutorials + Tutorials:

There were three tutotrials which were needed to be learned and applied: how to use Phaser, how to use webpack with Phaser, how to write a shooter game.

## Day 2 More tutorials and Game Design:

The tutorials took longer than the day and the rest of the day was spent developing a simple blueprint for the design of the game:

## Day 3-5 Development, Testing and Playing:

### Create a Menu

Develop the menu page, take out the button from the tutorial an introduce a background with a key event for ENTER. Use the template to introduce this stage.

#### Menu

![Menu](https://user-images.githubusercontent.com/43377799/91501094-92f9b700-e8cd-11ea-817e-b4115eeacc82.png)

### Add Enemies and Sprites

I spent about two days here. I had to re-learn how to introduce new characters. I introduced music. New dynamics. There are colliders everywhere for a better experience. Lots of sound effects for a better experience. The global score is here. All kinds of differetn scores depending on the enemy killed. Loops for background music and parallax.

### Play

![Play](https://user-images.githubusercontent.com/43377799/91501166-b886c080-e8cd-11ea-9117-da16d2d536fe.png)

### Score Scene

Introduce score scene from the template. Use global scores to update player score. Introduce API listening, introduce menu for player to type the player name. Validate.

### Score

![Score](https://user-images.githubusercontent.com/43377799/91501223-dce29d00-e8cd-11ea-91cd-52f07ebb8373.png)

### LeaderBoard

A lot happens behind the scene: the API is delivered and a promise is received. Data is parsed, cleaned, combed and ready to be displayed as a retro leaderboard. I make sure that only the top 5 are display because I want to follow the spirit of a retro game.

### LeaderBoard

![LeaderBoard](https://user-images.githubusercontent.com/43377799/91501310-069bc400-e8ce-11ea-9b5d-39c5e101fa4c.png)

## Technology Used

- Phaser 3
- Javascript
- Jest
- Visual Code
