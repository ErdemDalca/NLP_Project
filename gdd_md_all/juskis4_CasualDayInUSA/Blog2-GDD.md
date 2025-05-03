# Game Concept Document Template - Casual day in USA

## High Level Concept/Design 


#### Working title
- **Casual Day in USA**
___
#### Concept statement
- A kid in your school has went ape shit and is now trying to kill as many people as he can, until the cops arrive. Do you run for your life or do you stay and try to be a hero?
___
#### Genre(s)
- Survival
- Strategy
- Role-playing
___
#### Target audience
- The game is aimed at individuals aged 17 to 30, particularly appealing to those who align with modern definitions of being 'edgy.' It caters to enthusiasts of bold humor, intense narratives, and dark comedy, making it a unique blend for an audience that appreciates unconventional and provocative content. In other words, this game is NOT for snowflakes.
- ESRB rating - Mature 17+ or Adults Only 18+
___
#### Unique Selling Points
- **The setting**. There are close to zero games where in a setting like that, you have the ability to choose to be a hero, or you can be selfish and leave everyone to their destiny
- **Dark homour**
- **Arcade feel** for mechanics. Simillar to Escapists 2 game
___
#### Player Experience and Game POV
- **Player** - An average 10th grader, black skinny jeans with a plain hoodie. Doesnt really have "real" friends in class, yet knows a lot of people. Popular loner.
- **Setting** - Average high school in the north of USA, on an average day in an average classroom with stereotypical teachers and classmates.

> In the beggining, the player must feel like he was actualy brought back in time to the 10th grade. Seeing a group of nerds in the front of the class, while the cool kids with Jordan 4's are at the back, recording a video for their private snapchat story. Of course, lets not forget the kids who would eat in class like it was their last meal (this time it might actually be their last meal, but it all depends on you).

>Player engagement and duration of their play, all depends on the Player itself. If he chooses, that he just wants to escape the school as soon as he hears shots in the hallway, that is up to him. In this case the duration of the session wont be over 5 minutes. Otherwise, the player can choose to hunt, trap or gruesomely kill the shooters, which might take up to 20 minutes, because in order to do most of the stuff, you got to prepare for it first (gathering resources, npc interaction, etc.).
___
#### Visual and Audio Style
- Easyest way to call it, would be a top down Escapist 2, but less pixely, more 3d.
___
#### Game World Fiction
- **Setting:** The game unfolds in an American high school, situated in USA. In addition, essential school stereotypes are all around, cliques, everyday dramas and etc.
- **Premise:** On what appears to be just another routine day, the mundane reality of a high school life is shattered. A crisis unfolds as a student's actions threaten the safety of everyone in the school. The once familiar hallways become a maze of danger, transforming the school into a battleground of survival and moral choices.
- **Narrative Tone:** While the game addresses dark themes, it is infused with dark humor and satire, reflecting the absurdity and unpredictability of life. The narrative tone walks a fine line between the gravity of the situation and a critique of societal norms

___
#### Monetization
- Monetization is currently not in plans as it is a non-profit project. Closer to the release, this might change, depending on gathered attention during pre-release phase.
___
#### Platform(s) Technology and Scope (brief)
- Currently only PC Unity version will be in development.
- The team consists of me and me only.
- Development of the base game should take up to 3 months, without full functionality, polishing, bugs and etc.
___
#### Risks
1. Path finding algorithms for NPC's might be difficult to implement and may be the cause of a lot of bugs.
2. Art side of things. Making the game appealing to the eye and at the same time keeping the overall vibe of the game, as its been writen down.
___
#### Core Loops - Survival and Decision-Making Loop

**Situation Awareness:** The player starts by navigating the school environment, gathering information about the crisis unfolding. This involves listening to NPC conversations, observing changes in the environment, and receiving updates on the situation (e.g., through PA announcements).

**Decision Making:** Based on the information gathered, the player must make decisions on how to proceed. This includes choosing to hide, escape, confront the threat, or help others. Each decision impacts the game's narrative and the player's survival chances.

**Action Execution:** The player carries out their chosen action. This might involve solving puzzles to unlock doors, stealthily moving past dangers, crafting weapons or traps (This would involve gathering resources, which could be a core loop in itself), or engaging in dialogue with NPCs to influence their actions or gain their assistance.

**Feedback and Consequences:** The game provides immediate feedback on the player's actions through changes in the game world and the player's status (health, inventory). Long-term consequences are reflected in the unfolding narrative and eventual game endings.

**Reflection and Adaptation:** The player reflects on the outcomes of their actions, which influences their future decisions. This loop encourages players to experiment with different strategies and explore the game's moral and ethical dimensions.
___
#### Objectives and Progression
The objectives all depend on a chosen playstyle:
1. **Escape:** Player can choose to escape as fast as possible from the school, without trying to save classmates or trying to trap and kill the school shooter. It is the most straighforward playstyle of the game.
2. **Kill:** Player needs to find some sort of weapon in order to kill the shooter. Once this is accomplished, the player wins the game. Finding a weapon can consists of sub-objectives, like finding the right materials if the player cant find a weapon and decides to craft it. To find materials, the player has two options. First one, is checking places randomly and hoping for luck. Second one, is interacting with classmates, teachers and the rest of school personel in order to receive crafting items or get clues on where to find some particular item.
___
#### Game Systems
- What systems are needed to make this game? Which ones are internal (simulation etc.) and which does the player interact with?
- **Pathfind algorithm** for npc and the shooter. 
- **Inventory** for the player to carry a limited amount of crafting items.
- **Crafting** mechanics so that the crafting items could be used to craft some sort of weapon or a trap.
- **Traps** mechanics, so that the player could stop the shooter with a trap, making him an easier target.
- **Dialogue** system for interacting with NPC. The interactions should reward the player with clues for locations of the crafting items or with the items itself.
- **Stealth and Agro mechanics**. The player must be detectible from eyesight or by sound and automaticly agro the shooter. Stealth mechanics includes hiding from the shooter to remove the agro, or sneaking in order to not make a sound when moving.

___
#### Interactivity
**Action/Feedback**
- Players interact with the game environment through **point-and-click** mechanics for movement and interaction with objects. Actions have immediate feedback, such as picking up an item, opening a door, or successfully hiding from danger. The game uses visual and audio cues to inform the player of the impact of their actions.

**Social/Cultural Context**
- While the game features a fictional scenario, it touches on real-world issues such as violence in schools and the impact of individual actions on a community. By presenting these themes through gameplay, the game invites players to reflect on these topics in a broader social and cultural context.

**Movement and World Interaction**
- Navigation within the game world is facilitated through a combination of keyboard controls (WASD) for movement and action keys (E, F) or a joystick for movement and A, B for specific actions, such as engaging with NPCs or interacting with objects. The environment plays a significant role in gameplay, with players needing to pay attention to details that could affect their survival or progress.

**Combat and Physics**
- If confrontation is part of the chosen strategy, the game includes a simplified combat system that relies on timing and resource management rather than detailed combat mechanics. The game's physics are designed to support a realistic interaction with the environment, such as the effects of traps or the use of items as makeshift weapons.
- Shooting is straight forward as the player with a gun in hand must look in the direction of the shooter and press the main action key (E on PC, A on game console) and try to hit the target.
___
#### Conclusion 
The game world of **"Casual Day in USA"** is a microcosm of high school life pushed to its extreme. It's a narrative sandbox that invites players to explore, interact, and ultimately decide what kind of person they want to be when faced with the unthinkable. Through its fiction, the game aims to entertain, provoke thought, and perhaps offer a dark mirror to our own world.