---
title: "Why make a game as a Web Dev?"
description: "I go over reason to step out of your comfort zone and do something new, something you havent tried before."
image: ../../assets/depot-gato-idea.jpg
publishedAt: 2024-02-06
tags: [softwareengineering, story, videogame, steppingoutofcomfortzone]
---

# Introduction

When I was kid we had a <a title="Found the TV model but did not found the game" target="_blank" href="https://manualzz.com/doc/4257542/samsung-cb-21n30mj-user-manual">Samsung CRT TV</a>. Nothing special about but it had few embedded games. One of it was a game where you shoot from left side of the screen and balloons appear on right side. The moment you miss it's game over. It was bare bones had nothing other than moving ellipses as balloons and no levels or any fancy stuff. But I loved that interactive experience so much, This was the first game I experienced. This got me introduced to video games. After that I played many games and since school I always wanted to make one myself. This was the initial reason even why I decided even to study Computer Science in the first place.

# Experience

I've looked into making games before multiple failed attempts at using game engines like unity, unreal or even the one that don't require you to learn code. But due to multiple reasons I really never finished and released something out. Unlike web dev projects where I was not only able to learn and work on vast variety of problems but also able to showcase them and eventually start as freelancer and then as a full time. 

I wasn't only looking to just cobble up some code together but wanted add some polish the output. Polish in form of levels, pause options, graphics, and simple narrative and even music if time lets me do it.

Over period of two weeks during my free time I downloaded Godot Engine and reuse one of my old project to make this new game. There were so many new things I ended up learning here are just few,

1. Trying to come with game mechanics and story.
1. Making art (I'm not an artist), and frame by frame animation.
1. Cohesive Art style.
1. Physics and collision detection.
1. New language (GDScript) and data structures.

I also so many parallel problems that I already face in web but now in different context.

1. Managing state of the running game. (I struggled with this a lot)
1. How to update the state (In Godot you can emit a signal and other nodes can listen to it).
1. Save and loading game state. (For this game I wanted to store game levels, unlocks and score
 as a JSON file, I hand wrote serialization and deserialization code for this. Not recommended but certainly fun).
1. Input handling and feedback on action to the user. (Ex: When player fires cannon, there is small progress bar that empties and then fills up letting user know when they can fire again).
1. Modularizing code and composing entire game from nodes. (Like components in React)
1. Building and deploying game.

If you want to find more about the game you can find game design document document I wrote for this game [here](/work/depot-gato). It's not 
too big or technical but it's a small overview of what went behind in making the Depot Gato.

# Why make a game as a Web Dev?

Other than personal nostalgia it's just great idea to step out of your comfort zone and try something new. If you're custom to certain flow and knowledge you're not challenging yourself enough. Working on game you get to enter this new domain of unknown challenges and problems. It's a great way to test yourself whether you've grown as a problem solver or you've been merely remembering things. Coding practices to problems would change but the core skills of your ability to solve complex problems by breaking them down to smaller ones and then solving them would remain same.

Did I enjoy this experiment, Yes! Would I do it again Yes!! Would I leave my job and become a game developer full time No! If you're working in certain field and you have been only been programming single language or working on single type of project, you're missing out on so much. This is not just about making a game, honestly you might not even like playing games. But you can challenge yourself in different shapes and form. I constantly like to take look at new libraries, frameworks, languages or even new paradigms, and much more. My goal is to never to be expert in all of those but rather discover in what ways people are solving problems. This was the same reason I gave functional programming a try few years back didn't like it to be turn my self into Monad enjoyer, but to this day I learned to love immutability and iterators, and pattern matching common in functional languages.

This was a short post about me mostly blabbering about my experience hope you enjoyed it.

