﻿# Unity RPG Course - Section 3 - Modifiers And Abilities

Welcome to Section 3 of the [Unity RPG](http://gdev.tv/rpggithub) course – the full course is part of a Kickstarter campaign which was over 200% funded. You will benefit from the fact we have already taught over 360,336 students game development, many shipping commercial games as a result.

Customise character abilities, weapons, characters and enemies. This includes multiple damage types, modifiers, sounds, animations. By the end you can create your core combat experience. 

You're welcome to download, fork or do whatever else legal with all the files! Please note that future sections contain assets with commercial use restrictions. The real value is in our huge, high-quality online tutorials that accompany this repo. You can check out the course here: [Unity RPG](http://gdev.tv/rpggithub)

## In This Section 

### How To Build / Compile
This is a Unity project. If you're familiar with source control, then "clone this repo". Otherwise download the contents, and navigate to `Assets > Levels` then open any `.unity` file.

This branch is the course branch, each commit corresponds to a lecture in the course. The current state is our latest progress.

### Lecture List
Here are the lectures of the course for this section...

### 1 Section 3 Introduction

+ What’s coming in this section.


### 2 Design Planning And Decisions

+ Review and update your WBS
+ CHALLENGE
+ Decide on next priorities


### 3 Your Game Design Document

+ GDD Template And Our GDD
+ CHALLENGE


### 4 Unity 5.6 And VS Community 2017
+ My chosen options for upgrading to Unity 5.6
+ Review Unity's release notes


### 5 Using Namespaces In C#
+ What a namespace is and why it's useful
+ How to use namespaces in C#


### 6 The Animator Override Controller
+ Fixing a possible projectile bug
+ What is an Animator Override Controller?
+ How to override animations at runtime


### 7 Protecting Our Interfaces
+ The hidden dependency in our asset pack
+ How to prevent animation events breaking code
+ Challenge: Apply animations to weapons.


### 8 Untangling Standard Assets
+ Taking control of our animations
+ Drawing out our dependencies
+ Taking control of Standard Assets


### 9 Trigger Animations From Code
+ Refactor our Player class
+ Move properties from Player to Weapon


### 10 Triggering Audio On Radius
1. Review AudioTrigger.cs from Gist
2. Set-up and test sound trigger prefab
3. How to source your audio clips


### 11 Terrain Optimization
1. Performance issues from terrain
2. Challenge: Tune terrain settings


### 12 Our First Dialogue
1. Our level's requirements
2. Pitch shifting a character
3. Challenge: create your dialogue


### 13 Tasks And Bugs
1. Our bug fixing workflow
2. Bug tracking and task scheduling
3. Challenge
4. Lets fix some issues


### 14 Placing Props
1. Tidy up scene and import new assets
2. Challenge: Place props in your scene


### 15 Weapon Design
1. Quick look at visual improvements
2. Weapon damage design
3. Prototype requirements for weapons
4. Adding a third weapon and tuning all three


### 16 Changing Your Skybox
1. Lets investigate our scene lighting
2. Import and set up a new skybox


### 17 Bridges And Navmesh
1. Desired bridge look and navmesh issue
2. Create your bridge


### 18 Enemy Mesh Antics
1. Import and set up new character meshes


### 19 Adding An Energy Mechanic
1. Unity 5.6.1 upgrade, Mac differences
2. Extending the player by composition


### 20 Extension By Composition
1. Setup a new delegate in CameraRaycaster
2. De-bounce the right-click button with `GetButtonDown`
3. Subscribe to event in new `Energy.cs` class
4. Reduce energy on each right click
5. Update the energy bar.


### 21 Detecting By Layer In 3D
1. How to use source control to keep refactors honest
2. Our new `CameraRaycaster` architecture


### 22 Simplifying Click To Move
1. Adding `onMouseOverPotentiallyWalkable` event
2. Removing our custom editor script
3. Ensuring click to move still works.


### 23 Simplifying Click To Attack
1. Remove `CursorAffordance.cs` altogether!
2. Remove the `CameraRaycasterEditor` editor script
3. Implement move to enemy on power attack
4. Simplify the `CameraRaycaster`, `Energy` and `PlayerMovement`


### 24 Player Choice In Combat
1. What are the choices the player can make in your combat?
2. Types of Special Abilities
3. Where to start with implementation


### 25 RPG Special Abilities System Overview
1. Abilities require serialisable data AND behaviour
2. We can only serialise MonoBehaviours via prefab or scene
3. This causes more contention on those files, and is wrong place
4. A ScriptableObject moves ability config data to a .asset file
5. ... but SOs cannot interact with the world
6. so the Ability also needs a MonoBehaviour
7. One ability can have multiple configs
8. Therefore make the config add the behaviour component at runtime.


### 26 Storing Special Ability Config data
1. Setup an 'ISpecialAbilty' interface
2. Use an abstract class to create `SpecialAbilityConfig`
3. Inherit 'PowerAttackConfig' from this new abstract class
4. Provide right-click asset menu to create new special ability.


### 27 Making A Class Single Purpose
1. Remove `pointsPerHit` from our `Energy` component
2. Move right-click handling to the `Player`
3. Prepare to read energy cost from special ability.


### 28 Implementing Power Attack Behaviour
1. Fix a bug with our AudioTrigger component
2. Make it possible for the player to equip several abilities
3. Use a protected property to reference `behaviour` component
4. Use this property to forward calls to `Use()` to the component.


### 29 Using Structs For Parameter Sets
1. Combine top-level special ability code into one file
2. Create a struct to pass ability use parameters
3. Finish Power Attack behaviour inc energy cost.

### 30 Create An Area Of Effect Ability
1. Describe your challenge
2. Introduce `Physics.ShpereCastAll()` API
3. Demonstrate my Area Of Effect solution.


### 31 Regenerating Energy Over Time
1. Why we're not using coroutines yet
2. Challenge: make energy regenerate over time
3. Fix enemy sliding bug (and extra animator).


### 32 Game Feel Intro
1. The importance of game feel
2. What things to look for with your audit


### 33 Game Feel Audit
1. Words to describe your game feel
2. Examples of poor game feel
3. Tuning of player to enemy collision


### 34 Spreadsheet Strategy
1. A structure for approaching your spreadsheet design
2. Specific implementation of some "Soul" aspects


### 35 Spreadsheet Spine
1. Different options for progression
2. Progression theory and preferences
3. Populating our spreadsheet's spine


### 36 When Mouse Leaves Game Window
1. Detect when the mouse is in the game rectangle
2. Stop raycasting when the mouse is over Unity editor UI.


### 37 Coroutine For Death Sequence
1. How to test if the player is dead
2. Use an `IEnumerator` coroutine for timing
3. Use `WaitForSecondsRealtime()` method.


### 38 Player Damage & Death Sounds
1. Add an array of damage sounds
2. Add a single death sound (for now).


### 39 Player Death Animation
1. Fix health bug
2. Implement death animation
3. Projectile firing rate variation?


### 40 Using Image Fill In UI
1. Import brand-new HUD graphics
2. Make liquid effect health and energy
3. How a "Filled" image works
3. Use "Fill Amount" property to animate UI.


### 41 Adding Special Ability UI
1. Adding special ability icons to slots
2. Fixing bug with game window resizing.


### 42 Level Design Paradigms
1. Discussing our current Linear approach
2. Introducing a range of level design paradigms and what they could mean for your game.


### 43 Level Design Choice
1. Challenge: add choice to your level
2. Review our current level for ideas on how to add more choice.


### 44 Assets And Improvements
1. Updated grass textures
2. New free assets as part of student pack from Synty
3. Synty particle pack


### 45 Particle Effects Intro
1. Particle effects overview
2. Where to use particles - a review of Torchlight 2
3. Where we will add particles to our game


### 46 Glowing Dust Effect
1. Create an ambient particle effect in the world
2. Have the particle effect follow the character


### 47 Spawning Particles At Runtime
1. Create particle system prefabs for special abilities
2. Access prefabs from our scriptable objects
3. Trigger particle systems at runtime in C#
4. How to destroy a particle when it has finished playing.


### 48 Self Heal Special Ability Challenge
1. Create a self-heal special ability yourself.


### 49 Triggering Special Abilities From Keys
1. Adding key affordances to the UI
2. Scanning for number key presses
3. Triggering and tweaking special abilities.


### 50 Finishing The Self Heal Ability
1. Separate damage and healing methods
2. Add sound triggers to all abilities
3. Tantalise idea of changing interface to inheritance
4. Parent healing particle system to player.


### 51 Critical Hit And Weapon Bonus
1. How to count lines of code added
2. Adding additional weapon damage
3. Adding critical hit calculation & particles.


### 52 AOE Particle Effect
1. Creating particle systems within particle system
2. Alter rotation of emission
3. Use burst emission
4. Tune and tweak particles


### 53 Self Heal Particle Effect
1. Create plus symbol texture for a different look
2. Implement self heal particle system


### 54 Section 3 Wrap Up
1. We now know what our game will be, so its time to shift gears.
2. Well done on your great work so far!

That's it, in the next section we will be adding the final features, refactoring and making our core combat fun.
