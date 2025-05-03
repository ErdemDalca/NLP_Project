---
title: "Lei3D & SkyLei"
date: 2023-08-10T23:29:21+05:30
draft: false
github_link: "https://github.com/kevinsadi"
author: "Kevin Sadi"
tags:
  - Math
  - Computer Graphics
  - Learning
image: /images/blogs/skylei/skylei_blog.png
description: "SkyLei is a game I've been working on for the past while."
toc:
---

This blogpost is a quick discussion of SkyLei, a game that I've been working on for quite some time, and the corresponding engine I've created with friends to build the game. I thought of the initial game idea about a year ago as of the time I'm writing this blog. I grew up playing games like TF2, CSGO, and GMOD. Specifically, I loved the feeling of the physics in those games. Thus, I wanted to try my own hands at implementing those physics. I played around with building rendering engines in the past, so I wanted to dive into a far larger challenge. Thus, I thought to make a bespoke 3D game engine using C++ and OpenGL. The primary inspiration would be CSGO Surf, born out of the airstrafing "bug" introduced in Quake, and carried over for many games henceforth. After getting some of the core features in the game, some of my friends wanted to extend some help, which I very quickly accepted. I am now co-leading this project with a friend for the Georgia Tech Video Game Development club. It's an incredibly exciting opportunity, but there is a lot of work to be done, and I'm sure I'll be writing a series of blog posts to update as we progress. 

## Quick Description
SkyLei is a game that presents a unique twist in the world of speed running games by focusing on slowing down.

In a world that is shattered to pieces and taken to islands in the sky, SkyLei follows the exhilarating plight of Leilani Leaf through a colorless, once beautiful world. Primary gameplay consists of racing around and exploring a surreal-dreamlike world with physics-based movement. The levels of the world add new features that inspire new routes and discovery of the world. This adds challenge and enjoyment to players of any skill-level. At the very end of each level, Leilani brings color back to the world when she discovers the beauty of all that surrounds her. 

## What I've Done

While I have worked heavily on games in the past, there was a lot of overhead with setting up this project for collaboration with other people of drastically different backgrounds. I had to ensure that there was well documented work for people who are extremely experienced, as well as for people who have never touched code in their life. Of course, this was a challenge made even more difficult by the fact that I was also learning along the way. 

For a couple months, I used the engine as a means to test and visualize work that I was doing with professor Greg Turk during a 1:1 research project that we were doing together. This allowed me to get used to the basics of OpenGL, as well as slowly work through LearnOpenGL.com on my own time. Eventually, I had everything in a single file, which was obviously not going to work for collaboration. I refactored the engine to have something akin to it's current structure, linking everything using CMake and FetchContent to allow the building process to be as easy as possible to newcomers. From there, I implemented model loading through ASSIMP and a basic material system. I got a basic fly camera in the engine and started slowly implementing physics into the engine. It took me quite some time to wrap my head around how to link the rendering to the physics, but I eventually came to it. I got basic GUI tools into the game and added an audio engine. After this point, I focused on refactoring the engine a bit to feel more cohesive to anyone who wanted to work on the project.

At this point, some of my peers started to see what I was doing! And, since it was a learning project, there were a lot of best practices that I was not following. Two of my good peers started to signficantly work on the engine, so we had a great small team chugging away on working on the engine! The main goal was to have a solid demo to present if we had the opportunity to pitch the game to the Video Game Development Club. A successful pitch would mean that we would get a talented team of artists, musicians, level designers, narrative designers, and programmers. 

From here, I took a brief aside from the engine to focus on higher level strategy. I set up a discord for collaboration between anyone who was interested in the project, and drafted up a game design document to explain the vision of the game. I have a large background in music, so I grabbed some of my jazz buddies and we recorded some music to show the general vision of the game. We played a lot of synthy, jazzy, breakbeat drums to create this sort of liminal feeling to the world. I focused on the game design and general vision of the game. I reached out to peers who would be interested, and we started drafting 3D art for testing levels and getting concept art to show the vision of the game.

(TO BE CONTINUED)
