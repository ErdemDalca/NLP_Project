# *Across the Board*
*Communicate with the living. Restore your lost memories. Awaken your spiritual powers.*

This is a work in progress which when it's complete will hopefully resemble a visual novel.

This project is being made for the [Spooktober Visual Novel Jam 6](https://itch.io/jam/spooktober-2024), September 2024.

# Game Design Document (WIP)

## DISCLAIMER
This document will contain heavy game spoilers and should not be read if you want to play the game.

## Introduction

### Game summary
When you wake up, everything is dark. You don't know where you are, who you are or how you got here, but you can feel someone calling for you.

Following the call, you find a candle-lit room, three young girls and an Ouija board. It doesn't take a rocket scientist to figure out that you're dead.

Who are you? What happened to you? How can you get your memories back? And why are you here, now, in this room? Will the Ouija board be just a teenage party game, or can it help you find the answers you're looking for?

### Platform
The game runs in the browser and can be played on any device with an Internet connection and Javascript support.

### Languages and software
* The game itself is programmed in React / TypeScript.
* The narrative is written in [Ink](https://www.inklestudios.com/ink/).
* Specifically, the narrative is imported into the code using the Ink port [inkjs](https://github.com/y-lohse/inkjs).

### Genre
*Across the Board* is a horror visual novel.

### Target audience
The story is written with a Young Adult audience in mind, in particular for readers who enjoy psychological thrillers with supernatural horror elements, and the all-female cast may tilt the story in the direction of being a better match for women than for men.

The mechanics of the game, such as it being fully playable in browser, including on phones, are intended to make the game available for casual readers who don't have a lot of experience with visual novels.

## Concept

### Gameplay overview
The main game loop is that the humans in the room will ask you questions, and you must give them satisfying answers.

An on-screen "spirit meter" shows your current spiritual power. Answering questions in such a way that the three girls bond with you will increase your spiritual power, and every three questions or so you will have enough power to gain a spirit level. Every time you gain a new spirit level, you get a new power, and one memory of your life is unlocked in the form of a flashback.

Example of spirit powers are the ability to manipulate small objects or the ability to read minds.

The first questions you receive are easy to answer, but as the game progresses, you will need to look around and examine the room, using your new powers, to gain information.

### Theme interpretation
The theme of the jam is to make a horror or halloween-themed visual novel.  This will be a horror story, starring a ghost.

