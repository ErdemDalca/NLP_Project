---
title: "Learn about Game Design Documents"
slug: Game-Design-Document
---

#Game Design Documents

A Game Design Document (GDD) is meant to detail the objective, mechanics, level design, technical requirements, and development milestones for your game.

It is a living document. You should be changing and tweaking it at least twice a week.

Once you have made a GDD, it becomes much easier to visualize everything you have to complete to get your game done and you will be able to keep track of your progress.

Whever you decide to change some aspect of your game's design or development schedule, make sure to update your GDD!

Let's take a look into what goes into a GDD in more detail.

#Objective

Explain the goal of your game in 2-3 sentences. 

#Gameplay Mechanics

This is where you explain your game's core loop(s), whether your game is real time or turn based, single player or multiplayer, social or not, and any key aspects of your gameplay - this could be anything from your powerup system to special enemy types to the ability to rewind time.

#Level Design

Here you need to think about what principles you will follow when designing a level. Describe what a typical level will look like but also list any constrinats your game's design will place on the levels. For example, you may decide that every level will have a section where the player cannot mess up, like in Tiny Wings, or you may want to note that levels in your game should not be designed to force the player to backtrack. 

#Technical

Here we describe three key aspects of our game. 

Controls: How will the player interact with the game.

Scenes: Describe each screen in your game, from the main menu to the gameplay to your high score screen and anything in between.

Are there any screens you could remove from your MVP? For example, what if there was no main menu and players started immediately at the gameplay?

Classes/CCBs: Based on what you learned about game architecture, list all the Swift classes and SpriteBuilder CCBs you will need to create your game. 

#MVP Milestones 

This is the section that should get updated the most often. On a week by week basis, list what you plan on completing. 

[Here is an example of a GDD](https://github.com/mgwu-students/dion-larson/wiki/ "Example GDD")for a game made by one of our SF Instructors.

Read it through before you start making your own GDD.

#Crafting Your GDD

Go to Github.com and create a new project. When viewing your empty project, there will be a link in the right sidebar that says "Wiki".

Create a new page in your project's Wiki and name it "GDD".

Create five main sections: Objective, Gameplay Mechanics, Level Design, Technical, and MVP Milestones.

Inside of Technical, create three subsections: Controls, Scenes, and Classes/CCBs.

Inside of MVP Milestones list each remaining week of development.

Time to start writing your GDD!

1. Fill in your game's Objective and Mechanics.

2. Fill in the Control and Scenes subsections of your GDD.

3. Describe the Level Design for your game.

4. Start breaking your game down into tasks you will complete every week. 

    If you're new to projects this long, you will have to make best guesses as to how long things will take.

    Before ordering your tasks on a week by week basis, first list every task on your plate. This should include everything you've listed in your GDD that will be in your MVP and all the non-technical work your game requires.

    For every task, estimate how many days it will take. If you think it will take less than a day, round up to a day.

    Add all the days together. Multiply by 1.2 to give yourself buffer time for unexpected delays. If you end up with more than 25 days of estimated tasks, do not change your estimates. Unless you have significant experience with large projects you should almost never change your estimates to be more optimistic. It is a big red flag if your gut tells you a task will take N days but after thinking about it you decide it won't take as long. You're almost always wrong. 

    If you have more than 25 days of work left, cut features.

    If it doesn't hurt, you aren't cutting enough features.

    Revise your GDD if necessary if you end up making significant changes to your game's design.

    Only once you have a list of tasks that fit in 25 days should you start dividing them up week by week.

5. Write all the classes and CCBs your game will require.

Congratulations, you have a GDD!