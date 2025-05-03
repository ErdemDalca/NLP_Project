# Game Design Document
# Overview
Sujusterea: Civil War is a Single-Player or Co-op Realistic Tactical Shooter in which you play as part of an insurgent group, fighting against the Sujusterean Military in a fictional modern-day civil war.

The game takes place in sessions where you decide an infiltration location, and then retake Forward-Operating Bases (FOBs) by infiltrating the location and clearing it of enemies. There are multiple side-objectives to each infiltration, such as picking up intelligence, freeing prisoners etc.
Once you have completed the objectives that you can, you then proceed to an exfiltration area (on the other side of the map from your spawn).

You play against multiple AI enemies that take defensive positions inside the map, and you have an AI teammate that you can direct to suppress fire, watch your back, or stay back and keep quiet for stealth segments. 
# Controls and Player 
Since the game is intended to be realistic, I want to approximate a real human's capabilities with the player controller. This means mechanics like a relatively slow base movement speed, weapon sway and inaccuracy while walking (so you need to stay still to shoot accurately), as well as the ability to lean around corners and slow walk for silent/quiet movement. This adds a lot of complexity and depth to the movement mechanics, for example the enemies need to consider if they are close enough that they can hear you. I aim for the gameplay to be relatively slow and tactical.
Additional controls such as crouching and laying prone are also planned, as it makes sniping much more viable as a tactic. 
Taking inspiration from the ArmA series, I decided to add a feature where you can hold down the right click button to zoom the camera in by 1.5x. This is a fun game mechanic as it allows you to survey the area in much more detail than you could with a higher Field of View (FOV), and potentially spot enemies further away. However, I think it would be a bit too powerful if you could aim down sights as well as zoom, especially with a magnified optic, so you are only able to use the ArmA-style zoom if you are not aiming down the sights.
# Theme/Setting
<span style="color:#FF0000">It is set in the fictional Eastern-European country of Sujusterea (located along the Baltic sea, neighbouring Latvia and Lithuania), in which the current government is starting to ally with Russia. Historically, during the USSR, Russia has oppressed Sujusterea, and the citizens now believe that the politicians at the top of the Sujusterean Government are accepting bribes from Russia. Picking up any weapons they can find, and quietly aided by NATO and the US, the Force of Operations for the Republic of Sujusterea (FORS), led by Sebastianas Forsentaciuki will rise up against the Sujusterean Military Forces (SMF).</span>
![[Pasted image 20240516190922.png]] 
# Visuals
I aim for the visuals to be as realistic as possible, however as this will just be a game prototype, I will use free assets I find online using platforms such as the Unity Asset Store and Sketchfab to fill out the game world. This means that the game will likely look quite simple and there will be many assets with a different art style. 
# Game Loop
Once you choose a map from the main menu screen, it shows the Infiltration Screen which includes the functionality to select where you are infiltrating from, selection for the guns that you want to bring in, selection of your teammates and the current objectives + objective locations. Once you have selected all of that, you can infiltrate. Then, you spawn in with your teammate(s) and begin attacking the objectives. Objectives may be things like clearing an area of enemies, picking up a piece of intelligence, 
Once you have completed all the objectives that you want, you head to the exfiltration zone and exit the map.
# AI
There are 2 types of AI that will be in the game- Enemy and Friendly.

Enemy AI will be more defensive, holding positions in cover and waiting for your attack to retaliate. They will spawn in different pre-set places randomly, so that each play-through will play differently and replay value is increased. 
If you fire on an enemy that does not know you're there (stealth), then they may retreat and find a piece of cover to hide from you, or if they have the jump on you (I.E. they can hear you coming close), then they can push you aggressively and maybe throw a grenade. The likelihood to perform these actions are influenced by multiple variables, such as how many friendly AIs are nearby, current enemy health, if they just hit a shot on you, if they have low ammo, etc.

The other type of AI will be friendly teammates that support you and can be indirectly controlled using an interface you can open with the middle mouse button.
You can command teammates to:
- Open suppressing fire on a specific area to keep enemies heads down
- Open and flash a door for you
- Watching your back
- Toggle stealth/standing mode

 Each AI teammate has a unique name, and you can hire new teammates with different skill levels as you progress through the game. AI teammates can also get shot and you may need to heal/help them up if they are downed. They also have perma-death, meaning if they are downed for too long and die, you cannot revive them or restore a save. This is intended to give you a more personal connection to the teammates that you play alongside, as you may miss a particularly high-skilled teammate if they die in combat.
 This is where I think the prompt is reflected the most. I aim to code my own AI system using Unity's Navmesh system, which is something I have not attempted before. 
 
<span style="color:#FF0000">
When deciding which AI system to use, I looked back at the research I did earlier. Each system has upsides and downsides, and specific use cases that would be best suited for.<br>
I ruled out GOAP, mainly because my enemies have very few actions they can perform. There aren't any actions that have to be sequenced either, only shooting, moving and reloading, so I would not be making advantage the main upside of GOAP. It has a much more in-depth and complicated implementation procedure, so would take longer to debug and perfect.<br>
Behaviour trees would be a suitable solution to use, and I prefer it to FSM as it is much easier to understand and debug, as well as not needing any code. As well as this, it is one of the most used systems for AI in modern games, and it would be good to have an understanding of how to create them for the future. However, unlike Unreal 5, Unity does not have a built-in behaviour tree system. In order to make one, I would need to purchase a user-made one from the Asset Store. As I don't have a budget for this game, I decided to use an FSM instead. <br>
While this makes it harder to implement, I think it is good practice for coding and allows me to learn a simple design pattern that can be used in many different scenarios, even outside of game design in general. <br>
As the AI will be relatively simple, an FSM shouldn't be too hard to implement.
</span>
# Level Design
Taking inspiration from games like Escape from Tarkov and S.T.A.L.K.E.R., the game takes place in multiple large areas of around 500m^2 to 1000m^2. Each map will include forested areas, as well as locations such as towns, industrial parks, military bases, factories, etc.
Each area will have 2-4 infiltration points, where you can choose to start the map at a different location. This adds replay value as it allows for a lot of player freedom and expression. For example, a location might be more heavily guarded towards the north side, so you can choose to sneak in through the south and take them out from behind.
At any point, you can head to an extraction zone and exfiltrate the area, ending that game, however the objectives you did not complete will fail.
# Health / Death
Enemies will die in one hit to the head, or 2-4 shots in the body. They can sit in place and slowly heal, however are vulnerable to pushes while this is happening as their gun is not ready.
The player's health system is similar, in the way that you can heal by putting your gun away. As well as this, If you get killed, you enter a "coma" state, in which your teammate must rush to you and give you aid, or you will die in 90 seconds. Your teammate can enter the same "coma" state, and you will need to help them up.
# HUD and Menus
I want the UI to be minimal and clean, only showing information when it is necessary. For example, the ammo indicator will only show while you are shooting or reloading the gun. There will be a crosshair on screen, using a raycast from the barrel of the gun to determine its end position. This means that when weapon sway from walking, breathing, moving etc. is added, it also affects the position of the crosshair, so it is always accurate to where the bullet will go. This is the way I will add moving inaccuracy.
I have also make a mockup of the Infiltration Screen and the UI for commanding friendly NPCs.
# Audio
I intend to add audio to my game, again making it as realistic as possible.
I also want AI enemies to be able to hear you, and react even if you are on the other side of a wall.