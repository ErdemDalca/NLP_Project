---
title: "Druids in the Dark"
tags: ["devlog", "technical devlog", "jam"]
date: 2024-21-08
emoji: "🧙‍♂️"
---

Welcome to my devlog for the game [Druids in the Dark](https://pandaqi.itch.io/druids-in-the-dark/). It was made for a Game Jam (by PirateSoftware) in very little time, because I was too busy finishing other projects. That's why the devlog will be quite short and the game idea isn't as creative/experimental as I'd normally do. Nevertheless, I wanted to detail the general process.

## What's the idea?

The theme of the Game Jam was "Shadows & Alchemy". No further restrictions, besides the usual "don't be an asshole" and "make sure you're allowed to use your assets" and such.

I almost exclusively make and play local multiplayer games, so I immediately thought: "what if you run a potion shop TOGETHER?"

One special part of this jam is that you must provide both the game _and_ a Game Design Document for it. It's one of the reasons I chose to participate. I have never made a GDD before, and I don't think it will suit me, but I want to at least _try_ and maybe learn something.

While writing that document, I had to explain how my game fit the theme, which forced me to come up with a few more twists.

* SHADOWS I: Each player has a shadow around them with a limited range. This means you _can't see what's on those adjacent tiles._ You must either memorize where the thing is that you need, or walk away until it's visible again. (Or, if playing together, hope the other player knows and communicates that.)
* SHADOWS II: 
* ALCHEMY I: Obviously, you're running around collecting the right ingredients for potions.
* ALCHEMY II: These ingredients don't just grow in your shop / await you in storage, however. The only thing that automatically appears are _finished potions_. By walking through those, you dissolve/break them into their original components. _Those_ can be picked up.
* ALCHEMY III: The recipes are randomly generated. The only way to view them is by visiting the Recipe Book cell, which is similar to discovering new formulas / hidden knowledge all the time.

I thought this would work quite well. The shadow forces you to memorize or communicate with your fellow players. The fact you need to break down potions and build them in a different way fits the core process of alchemy, and is different from what such games usually do.

Most importantly, we only need a _single_ control for all of this: walking. It simplifies development for me. It also makes it far more likely people will try the game (and/or be able to convince someone else to try it with them).

Bringing it all together, this is the general game loop.

* Customers appear that want specific potions.
* You must break down existing potions, then fumble through the dark to grab their components that you need, and deliver the wanted potion in time.
* Fail once ( = the timer runs out before you deliver the right thing) and you die.
* If you've served all customers before dying, you pass this round.

## My personal challenges

It's boring and useless, to me, to repeat the exact same workflow all the time. So, even if I'm quite happy with certain habits of mine (or my game engine, or my coding style), I still want to try 1 or 2 completely different approaches to challenge myself.

For this game jam, my "personal challenges" were ...

* No UI. Everything is an actual part of the game world and I must find clever ways to get rid of any interface.
* When coding, turn every possible action/interaction into a small "module" on the player. (For example, the interaction "if there's anything on your new cell, pick it up" is a tiny module with 10 lines of code. The same for "walk over a potion? break it into pieces" or "walk over the garbage bin? throw away what you have" and so forth.)
* When coding, only use a shared reference or state when _absolutely necessary_. (For example, instead of having several Global Singletons that everything can access whenever they want, only inject dependencies wherever needed and make nothing global/shared.)
* Hopefully, with a simpler game design, focus more on unique graphics or sounds that I would normally never even try.

My laptop is still too old and broken to make video games. So I'm making this game on a temporary workaround that also isn't great, so I'll still have to be minimal in terms of assets, code complexity, project size, etcetera.

## The first approach

My first approach was as follows.

### Player Movement

This is nothing special. I reused my "input manager" script from previous games, which allows logging keyboard and gamepad players on/off. Each player has one module that reads/polls their own input, and one module that responds to it by moving over the grid.

While playing the animation ( = movement takes time, snapping into place looks bad), it ignores all input. The map checks that you don't go out of bounds or whatever. And when done, it fires a signal `cell_entered` that all those other modules react to.

### Map

Every cell on the map is a scripted object that tracks three things.
* Which player(s) are on it
* Which element it holds (potion, core element, or nothing)
* Which machine it has (recipe book, garbage bin, etcetera, or nothing)

I decided to call it a "machine" because it was short and worked for me. That variable simply means "some object on the cell that _does something_ and can't be picked up".

Normally, I'd have a function like `interact_with_cell` or `check_cell` whenever a player enters a new cell. This would contain a (perhaps complicated) switch statement---or series of if-statements---that called the right code depending on the specific situation.

It's a garbage bin? Oh, do this. It's the recipe book? Oh, do that. Are there other players here? Oh, do this instead.

But that's ugly. And experience tells me that this seems fine at first but always gets out of hand as your game grows in complexity or you must handle unexpected corner cases.

So, instead, those _modules_ are fully responsible for all interactions.

* The player has ~10 modules of 10--20 lines each. Whenever you enter a new cell, all of them check if they must do something. And if so, do it of course.
* Sometimes, however, the cell also has custom logic or state. That's why, if there's a _machine_ on it, the cell instantiates the right _module_ for executing that machine too. (Which can then be accessed under the `machine` property of the cell.)

It was a bit of a difficult structure to wrap my head around at first. In a sense, we've now decoupled every "complex interaction" into two parts: a module on the player and a module on the cell. For example,

* The player has a `RecipeReader` that flips the recipe book to a new recipe if you walk over it.
* The cell has a `RecipeBook` machine that actually tracks this, then responds and updates to display the right thing.

So far, though, it leads to much cleaner code that's easier to maintain or scan.

### Shadows

I decided to create one shadow script that handles it for all players, instead of giving each player their own shadow module.

* Any time someone changed position, 
* It loops through all cells in the grid
* And checks if that cell is within range of any player's shadow
* If so, hide its contents. Otherwise, show them.

Why did I do this?

* Shadows might overlap. And if you check per player, then you're going to accidentally set them to the wrong value if someone _walks away_ but the other player _stays within range_.
  * You can prevent this by looping through the entire grid and resetting all values to `false` first, but that's more costly.
  * If shadows overlap, and we treat them as separate, then we'll also likely be re-calculating the same cell several times. Which is also more costly.
* Most of all, however, I wasn't sure where this mechanic would lead. Maybe I wanted to add some more twists to how these work. Maybe I wanted individualized shadows. By having one manager that does the entire shadow pass at once, it's more flexible and less prone to sneaky bugs.

### General Game Loop

Normally in such games, the orders appear as some UI element at the top of the screen. Because I didn't want UI, I decided to simply turn certain cells (at the edge of the map) into "order cells".

But even that's not enough. The player also wants to know when they win the level---how many customers can they expect, and how many have they already served? To do this without UI, I used the following rule.

> Every order cell can only be used once. After serving it, it disappears/changes appearance. This means that you always know how many you have left to go---and where customers can spawn---by checking the order cells that are left on the map.

Similarly, the _timer_ on the order is also displayed by turning the cell itself into a progress bar. (Instead of adding a separate UI element.)

## How's that?

All of this felt ... fine? But, as usual, you start out by putting _too much stuff_ in the game and then have to simplify.

I realized a few things.

* We can start the first level with only a single recipe. Moving around in the darkness, as you learn how the game actually works, is enough challenge.
* The interaction between players on the same cell also isn't crucial at level 1.
* We can even move the recipe book to a later level! By dissolving potions, you can figure out their recipe anyway.
* I considered that it might be even simpler if you simply lose the game as soon as you try to deliver the wrong potion to a customer. (Instead of the extra step of adding a timer.) This, however, would remove the _only_ aspect of the game that adds _urgency_! Without those timers, you can walk around extremely slowly and carefully, making almost no mistakes, which does not make it more fun.

At this point, I desperately needed some simple sprites to see what the hell I'm even doing. I also decided it was time to already craft the tutorial for the game. I like to do this early because it clearly highlights if it's simple enough or where it should be streamlined further. (And to make sure we don't forget at the end :p)

And so I did. I created most assets I'd need---some already pretty and final, some just a crude sketch---and plugged them into the game.

This finally allowed me to play the game, missing only the inventory display. (So I couldn't actually see what was in my inventory, or what specific order somebody wanted.)

And by playing through the game, I stumbled upon a few major problems that stand in the way of an actual functioning game.

## The Second Attempt

### Major Problem: no "new" recipes or combinations

Currently, the only way to get ingredients is by walking through a potion, which dissolves into its separate components. But ... those potions are the _exact thing_ that customers want. So, 90% of the time, walking through a potion and just collecting whatever comes out is _all you need to do_. Pretty boring, not much depth.

I see this as a major flaw at the _core_ of the game. With the current setup, you never actually have to build something new from the components you get, and remembering where 2 or 3 ingredients are hidden isn't that hard.

How do we solve this?

* By forcing you to juggle more things at once.
* By making the core action---movement/navigating with uncertainty---harder.
* By rethinking the rules around recipes and ingredients to get more variety and creativity.

I wrote down 15+ possible solutions. Some of them excluded the others, some could be used together.

I've learned to simply implement all these rules tweaks or extra systems, but place them behind an easy debugging toggle so I can turn game mechanics on/off at a dime. This way, I can try all solutions, abandon those that don't work, without needing to copy-paste code, or comment out parts of it, or potentially ruin the other code from all the doing and undoing of ideas.

Some solutions were straightforward. For example: just place more garbage bins. This makes it much harder to navigate without accidentally losing what you have.

Some solutions were wacky or more complicated, but those are always the ones that feel most impactful and promising. For example: "The longer/more something is in shadow, the more likely it is to _mutate_ into something else." People change their orders, ingredients are suddenly something else, and you need to keep paying attention.

### So?

I implemented all those ideas (and a few more). Most were fine, some were bad. 

I kept the fine ones and sorted them based on complexity to get "levels" (where one new rule is introduced for each level). This sort is also simply based on variety and not overwhelming players.

Then I created the tutorial system that displays the image + text for this new rule, and modifies the required properties/numbers behind the scenes. (It's cumulative: the changes of the previous tutorial are kept, and the new one simply loads its own stuff on top of that.)

The **biggest** realization (to keep the game simple, but already interesting from level 1) was to simply **make holes deadly**.

* You can walk into them just fine.
* But it will kill you.
* And shadows hide these holes. (At the start/end of the game, all shadows are turned off, so you have a few seconds to see where everything is and what the map looks like.)

This is very intuitive to most players. (Of course you die by falling into a pit, and a pit is just any place where there's no cell.)

At the same time, this makes the game much more challenging and tense in a good way. You have to memorize the locations of cells, and not---in your panic or haste---accidentally walk into one.

Now we finally had a core structure and progression to the game. That doesn't mean the game is any good: I need to playtest it myself and tweak loads of numbers.

### Tweaking for fun

I made maps slightly smaller than I originally intended, and had my algorithm take bigger bites out of it. (Otherwise, holes would be so tiny you could almost ignore them, or they'd only appear at the edges anyway.)

I made the timer (for making new customers appear, new potions/ingredients, etcetera) _much_ faster.

I made movement a bit slower by default. Otherwise, moving too fast both makes the game too easy (you can get anywhere you want at an instant), and also too annoying (you're far more likely to accidentally run into a hole with such movement). Also to allow _speed up_ powerups later to make sense.

I added _more orders_ by default, right from the start. This increases the probability of being far away from an order, having to juggle multiple at the same time, and just felt like a better balance in terms of challenge.

Of course there was a lot more tweaking, but those were _tiny_ changes to numbers or settings or whatever and not that interesting.

## Polishing

The usual suspects: Sound, Animation/Tweens, Particles, and Graphics in general. 

### Sound

The process was ...

* Find royalty free sound effects (or create them myself, if I can)
* Edit them _a lot_. (They always have wildly different volumes, lots of empty space at start/end, perhaps sections that I don't need, and they're almost always too SLOW.)
* Plug them all into the game.

My hardware is still too broken for any serious work on music or graphics. So I did all this in Audacity with quick destructive edits. 

The soundtrack was done in Reaper with a mix of MIDI-input + a free Piano VST, recording my Egg Shakers with my laptop microphone, and using more royalty free sounds for subtle ambience and some sparkling here and there.

Then my computer was done with it and I decided to stop the arrangement there. 

As usual, I am a musician, so inventing a catchy melody happens easily. Some ambient looping sounds, some chords or shakers, and a very simple arrangement can sound fine. The biggest issue is actually recording/transfering those issues when your hardware is working against you every step of the way.

No, wait, the biggest challenge was that _the home is being renovated_. I couldn't hear what the fudge I was doing. Volume balancing is hard enough as it is. (How loud should each sound be? How loud should game sounds be compared to background music? Sounds that repeat a lot should be much softer and a bit randomized, otherwise they're annoying. Single-instance sounds should be a bit louder than normal.) With drills and hammers all around you, this was a nightmare and I just gave it my best "guess" really.

### Graphics

In my Game Design Document, I stated that I'd get inspired by the visual style of _Lovers in a Dangerous Spacetime_. And I did! 

Because I still had to draw new stuff completely myself, of course, the style ended up deviating more and more and becoming its own thing. I think the game looks quite nice, unique and consistent.

I had to abandon any idea of glow/bloom, or lighting effects, or any more complexity. My own computer can't handle it, and if I can't make/play the game, then this all stops :p

In fact, the game just has 3 small spritesheets, as that's the maximum my computer could take.

* Elements => components, ingredients, machines
* Misc => UI-stuff, player icons, any other "miscellaneous" things (such as a blurry circle for both player shadows and particle effects)
* Tutorials => a very tiny spritesheet with ~20 tutorial images for each level

### Animations/Tweens/Particles

In Godot 4, tweens are a "fire-and-forget" thing, and that's one of the best improvements they ever did.

All throughout the game, it takes 10 seconds to write a simple tween (pop up, fade in-out, wiggle) to respond to certain elements. If that's impossible, the AnimationPlayer is equally simple and powerful.

I still have things that don't really react or are missing tweens, because I ran out of time. But I wrote them down on a "future to-do list", just in case.

I do wish it was easier to animate Control/UI nodes in Godot. Now I'm _very_ restricted in how I can smoothly make those transition. (Such as when the Tutorial appears, I wanted a more splashy animation, but had to settle for a simple pop-up and fade-in-each-element-separately.) Still nice, not as nice as it could've been.

Similarly, I have only a single particles scene: some fuzzy circles flying in different directions and fading away quickly (with lots of randomness). I re-use that when you do anything special, such as delivering an order. 

It's always a few hours of "boring work", if you ask me. But the results simply can't be ignored. For those few hours, the game feels much more like an actual game, more responsive and alive. In fact, after adding the sound for "new customer arrived", I almost immediately shifted to exclusively relying on that recognizable bell when playtesting the game myself. That's how particles, feedback, and sound can also be incredibly useful/functional (despite being pretty or juicy).

### Menus

Especially in game jams, menus are barebones. I'm fine with that. My marketing image for the game already helps the main menu a lot, just by looking more detailed and pretty as opposed to the buttons :p

I did spend some extra time on the input select screen. Both so that it's easy to use and clear, but also to prepare for future games.

I _want_ to make more local multiplayer games again once I have a functioning computer. And to do so, I want a really strong input system that makes input selection and management easy. So I used this project to improve my own library and fix some things.

(For example, in previous games, controls are all _fixed_. I'd create an image with WASD or the arrow keys and display that. This obviously isn't very flexible and stops working once I give a game reconfigurable controls---which is the next thing my input system should get, once I have time.)

In the end, I think the menus are _fine_ and _functional_, but they could've had more love too if I had time. (At the same time, the non-game parts of this game look better and more polished than in some other games of mine, on which I worked much longer xD)

## Conclusion

Because I wanted to finish my current project first, and I forgot about time zones, I really only had 4 days for this one. That's not a lot. Especially not when you actually want to push yourself to make a worthwhile game (even after the jam).

As such, once the game was finished ... I actually realized the _better_ ways to make it more fun. That's just how it goes. It takes time to try stuff, realize what your game is about, and finally get to the better ideas.

For example, remember how I told you that "make holes kill you" was a simple rule that finally made the game work? Well, now I realize I should've obviously _expanded_ on that idea. (Instead of introducing other rules or ideas all the time.) 

* I could've added tiles that break down over time. (Such as after walking over it X times, or being in shadow Y seconds.)
* I could've moved them around in some predictable way.
* I could've added powerups that gave more lives, or single-time protection against the holes, or a "see holes even in shadow"-bonus.
* Etcetera

The same thing with "movement". The entire game is _movement_ and how you go about it, so I should've done more variation on it, right? Perhaps moving in Tetris patterns was needed to create ingredients. Perhaps something would allow you to _jump_ over holes.

All great ideas that probably would've been simpler to implement and created a better game. But that's how it goes. Only 4 days, jam is over, I have other work to do.

I wrote all that in a future to-do list. I've actually become much better in recent years at coming back to projects (even after years) and giving them a great update in a few days. So maybe it will happen for this one too. There's a good core that _can_ become more, but it certainly doesn't feel _so promising_ that I'm ditching everything else to continue work on this game.

{{% remark %}}
Also because my hardware is still crap, so it's not ... very fun to work on games that aren't tiny anymore.
{{% /remark %}}

That's it for this devlog! Very short, no images or videos really to show. But I think the final game is _okay_. More importantly, I created _something_ and _send it_ to the jam, and that's really the only goal here.

Keep playing,

Pandaqi