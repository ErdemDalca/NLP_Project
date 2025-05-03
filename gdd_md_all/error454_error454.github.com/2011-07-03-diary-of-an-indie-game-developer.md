---
title: Diary of an Indie Game Developer
author: error454
layout: post
permalink: /2011/07/03/diary-of-an-indie-game-developer/
categories:
  - Shiva 3D
tags:
  - angry satellites
  - diary
  - games
  - indie
  - shiva
  - shiva3d
---
Dear Diary,

A little over 3 months ago, my brother and I were sitting around the man-cave throwing ideas around.  We were strongly impressed by the concept of a game like Angry Birds only in outer space where orbital physics would be used to slingshot projectiles around planets.  After much sleep deprivation, school-girl giddiness and white-board scribblings, we embarked on the journey of indie game development.

I've always wanted to make video games, my code-closet can attest that I'm great at starting them and chronically horrible at finding the motivation to finish them.  For the first time though, I am not alone in this effort.  So far this has been one of the most challenging and enjoyable projects of my life.
<!--more-->
At times it feels like the project will never end, sometimes it even feels like we make negative progress, but bit-by-byte it is starting to look like an actual game.  I only hope that when finished that it's half-as-fun as our original vision.

## Scheduling Life & Indie Games

There are 3 contributors to this game, which I shall refer to using the shop title Angry Satellites (AS for short).   My brother is a full-time student at Portland Art Institute studying game graphic design, he also has a 2-year old; he does all the modeling, graphics and figures out cool particle effects.  My college friend Matt works full-time as an electrical engineer, he solves our more difficult math problems and in-general helps out with code.

We've all got pretty full days with work/school/family during the week, so this has been a project that we typically work on once per week together.  Typically Sunday is our big day where we all huddle together in my office which reaches sweat-shop temperatures with 3 computers/warm bodies.  I take public transit to work on most days which gives me 2 hours of code-time, but after 8 hours of coding at work, you can only take so much.

## Project Planning

Like most projects, when you start out with the initial concept, you think gee, this will be easy.  We figured it would take about a month to finish the game.  Lol!  In retrospect, I believe the biggest challenges and setbacks were due to poor planning.  Let's just say that our game design strongly adheres to Agile software development practices  no Big Design Up Front.  This, I believe was a folly.

When you don't know what exactly you're working on, you get easily side-tracked into making things that might not have any place in your game.  Often we would get to a point where someone would say, Well, I finished implementing XYZ? and someone else would say I thought we were doing UVW instead and then we'd have to sit down and figure out what in the world kind of game we were making.

When you do the above a half-dozen or so times, well, it can get old.  Now I understand why every game design book I have read begins by explaining how to write a game design document.

## Technical Decisions

It was decided early on that we would use Shiva as the game engine and that we would target mobile devices.  The decision to use Shiva was mandated by myself because from my research, Shiva had the widest range of platform support, the best pricing model and a completely free editor to test until we were ready to publish.  I had been learning Shiva for a couple months prior and felt ready to take on a full project.

On the graphics front, Blender and Gimp, that's it.  I \*think\* most of the texturing has been offloaded to the Shiva side since we are doing a lot of UV animation.  You can see a few production tutorials on a <a href="http://3dlowvertmodeling.wordpress.com/2011/06/16/how-i-made-4-vertices-into-a-game-model/" target="_blank">low vert spaceship</a> along with some <a href="http://3dlowvertmodeling.wordpress.com/2011/06/16/low-vert-modeling-for-smart-phones/" target="_blank">mothership models</a>.

## Game Details

What is unique about our game is that using your phone, you are actually in direct control of a real satellite.  When you tap the screen to fire your Gatling gun, you are firing a real Gatling gun in outer space at real aliens.  Oddly enough, spaceships and projectiles in outer space all tend to align themselves on the XZ plane, this lends nicely to displaying the battlefield from a top-down perspective where movement is constrained on the Y-Axis.

<a href='{{ site.url }}/assets/uploads/2011/07/battlefield.png'><img src='{{ site.url }}/assets/uploads/2011/07/battlefield.png?w=300' alt=''></a>

There's really almost too much to talk about here.  In my next diary entry I will include videos, screen-shots and a deep-dive on some of the more technical aspects of the game.  Including:

*   Drone AI navigation implementation
*   Dynamics vs Translation for movement
*   Camera AI system
*   Projectiles vs Raycasting for projectiles
*   Rocket orbital physics
*   Explosions & Particle systems