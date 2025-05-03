# Game Design Document - Untitled Malwarebytes RPG
## Table of Contents
1. Introduction
    1. Purpose
    2. Scope
2. Development System
    1. Target System
    2. Software Used
3. Specification
    1. Concept
    2. Story
    3. Game Structure
    4. Players
    5. Action
    6. Objective
    7. Graphics
4. Gameplay
    1. World
    2. Battles
    3. Menus
        1. Malware Glossary
        2. Status
    4. NPCs (Non-Player Characters)
    5. Enemies
5. Front End
6. Team
7. Time

## Introduction
### Purpose
We are a hackathon team made from mainly the Iris Client and Server team passionate about making fun products and software for our users.  We want to create a game that can be used to entertain and educate our users about different malware, company cultural references and personality of Malwarebytes, and have users interact with us in a positive way.
### Scope
This document is intended to be used by the programmers, artists, and producers involved in the design of the game.
## Development System
### Target System
The game is intended to be loaded in a web browser on any Operating System that can use Javascript.
### Software Used
We will use Javascript and the Kaboom JS Library.

https://kaboomjs.com/
## Specification
### Concept
The aim of the game is produce a fun role-playing game that will teach the user about different types of Malware, share well known threats/scams, as well as express unique information about Malwarebytes.
### Story
The game will be set in a representation of the "Internet" with the Malwarebytes Robot Zero accompanying you to protect you from Malware.
### Game Structure
There will be different areas representing a physical form of the "Internet" that the user will navigate through fighting off Malware.  Players will walk around these areas fighting off Malware in random battles that can occur.  Occasionally the player will fight a boss that impedes them from progressing further until finally they find the final Boss.  Defeating the final boss will win the game.
### Players
This will be a single player game/experience.
### Action
Players will walk around until they encounter Malware.  When encountered, a battle will occur.  After the battle is finished, the player is returned to the world and can continue moving forward.  Occasionally there may be dialogue after a boss battle.
### Objective
Players are tasked by Marcin to defeat the final boss.
### Graphics
The game will be 2D and viewed from the top down.  The game will be made with sprite art.
## Gameplay
### World
The player is able to walk around different worlds.  They may encounter Malware randomly while walking, or they may see an NPC that will attack the player.
There are NPC bosses that will block the path of the player and they must defeat the boss in order to move forward.
### Battles
Battles will change the scene and it will be from the viewpoint of the player facing the enemy.
The Malwarebytes robot will appear in front of the player on the screen, and then the Malware will appear in the background.
The Robot and Malware will have HP values that will be visible.
There will be different attacks that the player's robot can choose to attack the Malware.
After defeating the Malware, the Player will be able to Quarantine the threat.  Each defeated Malware will be added to the Malwarebytes Glossary to be able to see more information about that Malware.
### Menus
#### Malware Glossary
An encyclopedia of all the defeated enemies.
Undefeated Malware will be hidden and information will not be shown.
Defeated Malware will appear and additional information will be viewable.  This may include a greater description, weaknesses, and other various information.
#### Status
A menu to view Zero's HP and to restore HP so that the player does not lose in future battles.
Gives the player the opportunity to use additional defenses like "Real-Time Protection" to prevent the player from getting attacked from random battles for a certain number of steps.
### NPCs (Non-Player Characters)
The player will encounter different NPCs within the game.
Neutral NPCs will be interactable and have something to tell the player.  They will be seen as other "Users" in the "Internet" and may have a fun tidbit or helpful hint to tell the player.
Enemy NPCs will attack the player when they "see" the player directly in front of them.  Other boss type NPCs will block the way forward and must be defeated in battle before the player can progress forward.
### Enemies
Reference to the glossary we are using to create different enemies.  https://www.malwarebytes.com/glossary

- Malware - General Malware
- Ransomware - Enemies that steal and encrypt your data
- Exploit - Exploits are a type of malware that takes advantage of bugs and vulnerabilities in a system in order to allow the exploit’s creator to take control.
- Trojan - Trojans are programs that claim to perform one function but actually do another, typically malicious.
- Nigerian Prince - A well known phishing scam that involves telling the user that they are a Nigerian Prince and will give them a large amount of money in return for some form of help. Victims are usually asked to make an advance payment or share their personal details to get their reward.
- Phishing - Phishing scams attempt to obtain your information by presenting themselves as legitimate websites, then asking for your password, credit card details, or other sensitive information.  We are planning on calling the Phishing enemy the "Phisherman".
- Keylogger - In the context of malware, a keylogger is a type of Trojan spyware that is capable of stealing or recording user keystrokes.
- Junk Mail - Junk mail is, essentially, email spam.
- Distributed Denial of Service (DDoS) - A distributed denial of service (DDoS) attack is a network attack wherein threat actors force numerous systems (usually infected with malware) to send requests to a specific web server to crash, distract, or disrupt it enough that users are unable to connect to it.
## Front End
There may be a Start Screen to start the game.
Afterwards there will be a pre-drawn image of Marcin to introduce the player to the world and give them their object.
Then the player is brought to the world map and the game will begin.
## Team
- Project Manager: Jon Eco
- Programming: Jon Eco, Carlos Gomez, David Hatcher, Jamie McCaw, Poonam Nigade
- QA: Jon Eco, Carlos Gomez, David Hatcher, Jamie McCaw, Poonam Nigade
- Art: Jon Eco, Poonam Nigade
- Design: Jon Eco, Carlos Gomez, David Hatcher, Jamie McCaw
## Time
- Official Start Date: Dec 4th, 2023
- Milestone 1 - Engine: Dec 5th, 2023
- Milestone 2 - All Menus/Scenes: Dec 6th, 2023
- Milestone 3 - First Playtest: Dec 7th, 2023
- End of Project: Dec 8th, 2023
