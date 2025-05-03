# Game Design Document - Cat-Butterfly Platformer

Cat-Butterfly Platformer

Tag line:

Last updated: 2025-01-29

## Section 1: Game Overview

    Purpose:

        This game is intended to be a fun platformer with some exploration and story elements. While some skill will be needed, the game should leave the player with a more cozy feeling.
        
    Target audience:

        The target audience is adults 25-60 years old. They may have grown up with video games from the 80s, 90s, and 00s, and the pixel art style will connect with them via nostalgia for those classic platformers, but that don't require the seemingly unending time they had when they were kids.

    Genres:

        Main genre: platformer
        Sub genres: exploration; narrative

## Section 2: Gameplay

    Objective/Goal:

        The main goal of this game is to rescue your people from the monsters that took them. Each level will have an end goal to reach through platforming and avoiding obstacles.

    Game Progression and Play Flow:

        Players will control the character through a platforming level with a end goal to reach (similar to the flag pole in SMB). Levels should build in difficulty until the end.

    Challenge:

        Challenge in this game will mainly come through platforming mechanics -- jumping and running through the level, avoiding obstacles and defeating enemies.
        
## Section 3: Mechanics

    Rules:

        Will the player have lives or a life-bar? For cats, the normal way would be to do some variation of 9 lives, but I think for this game I don't want to do that extreme a thing; maybe more of a "you need to restart a level or section but no permanent death."
        What happens when they fall off of a platform? Are there endless abysses, or does every level have a bottom to which the player falls?
        What direction do the levels go? Up? Right? some combination?

    Model of the Universe:

        I imagine the physics of the world being similar to other platformers with exaggerated physics -- ability to jump higher than normal, climb up the sides of walls, double-jump, etc.

    Player Actions:

        Movement:

            walk and run -- I imagine there being a difference between walking and running, apart from speed
                - The first difference would be the ability to stop; walking should allow the player to stop faster, whereas running would carry momentum and reuqire more distance to stop.
                - The second difference would be the effect on jumping -- running should allow the player to jump farther than walking.
                - I'm not sure about this part, but I imagine that walking and running might also affect how different enemies respond. For example, some enemies might run away if the player is running towards them, while others might only notice the player if they're running but not if they're walking.

            Some basic movement brainstorming:
                left/right
                    walk - a basic stroll; legs go in a 1, 2, 3, 4 pattern with left-front/rear, then right-front/rear: lf, lr, rf, rr
                    trot - a faster walk; lf/lr then rf/rr
                    run - a gallop -- back legs propel forward; front legs land one-at-a-time
                jumps
                    leap - reaches higher platforms in one smooth motion; back legs land *before* front legs. Can only be done from a walk
                    a running jump - leaps farther left or right but not as high
                crouch
                    gets down low - hide behind objects/grass - could add power to a pounce
                climb
                    cats can climb some surfaces (wood, carpet, etc) but not others
                    cats can also hang from a ledge to pull themselves up (for example, if they almost miss a jump) but only for a short time before they fall

        Actions:

            swipe - basic attack -- uses claws
            bat - pushes/shoves things without claws -- could be made stronger when done from a run
            pounce - captures an item or enemy; stronger from a crouch; can be powered up by a butt wiggle

            Combos:

                These combos will make their respective actions stronger or provide other benefits, such as stunning :
                    - pounce + swipe
                    - pounce + bat
                    - run + bat
                    - crouch + pounce
                    - crouch + pounce + bat/swipe
                    - run + leap
                    - walk + jump

    Butterfly helpers:

        Each of these comes to aid the cats in their journey. At the moment, I imagine them giving the cats specific benefits, such as:
            - monarch butterfly - strength
            - white butterfly - dodge or speed
            - yellow butterfly - health or defense
        These might be a bit too basic, but it could work in conjunction with the story. For example, the butterflies might show up at specific moments to help, can be instrumental in unlocking new levels, etc.
            - Although these "power up" things *could* be something else -- maybe its really a matter of visual design and aesthetics rather than the power-up itself that would make it special; some graphical fun that looks cool.
        Also, maybe the butterflies are "unlocked" at certain points and then their help is time limited and needs to be recharged after being used.

    Screen Flow

        Start Screen:

            The game will start on a title/start screen that includes the following buttons:
                - New Game
                - Continue
                - Options
                - Exit
            
        New Game:

            Player chooses a character; this might change if I decide to allow the player to change characters mid-level or something like that, but even then, I might have the player choose a specific cat to start the game, even if they can switch later or mid-level.

            Level Start
                The player will see a level start screen. This could include a title/location information for each level as well as maybe a map of the overall world, showing how far the player has progressed.

        Gameplay Screen:

            I imagine that the player can move freely through a level without any screen transitions.
        
        Pause Screen:

            - Continue
            - Options
            - Go to Title Screen
            - Exit Game

        Game Over:

            At this point, I am unsure if the game will have a hard "Game Over" screen or anything like that. Because I want the game to not be too intense and more cozy, I think it will basically have infinite continues.
            
        Replaying and Saving:
        
            At this point, I anticipate having specific checkpoints in each level (at a minimum, a single checkpoint in the middle of a level) as well as a hard save at the end of each level. I am unsure whether the player will be able to save at any point.

## Section: Story and narrative
