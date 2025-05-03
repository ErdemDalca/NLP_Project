# Wingsuit Bowling - Game Design Document


## Team Members
Our team consisted of: 

**Dave Coventry**
- Physics math
- Code review/QA
- GDD

**Ignacio Cajiao**
- Pin/Score/UI coding
- Visuals
- GDD

**Trevor (TJ) Beckham**
- Wingsuit coding
- Project management
- GDD

## Game Overview
Inspired by the classic Flatout racing games, Wingsuit Bowling! looks to bring the fun of bowling with the chaos of using a wingsuit for a crazy good time. 

Players will be tasked with knocking down as many bowling pins as possible with only two shots, but instead of using bowling balls, they will have to harness the laws of physics to glide themselves into the pins. 

It’s not just falling with style, players will have to be mindful of their pitch, yaw, and speed to ensure they can not only get to the pins, but get the best hits possible. 


## Controls
The controls for Wingsuit Bowling! Are: 

- Start Gliding - Space
- Gain Speed/Aim Down - W
- Lose Speed/ Aim Up - S
- Turn Character Left - A
- Turn Character Right - D 
- Rotate Character Left - Q
- Rotate Character Right - E
- Reset Character Position - R
- Exit Game - ESC


## Metric Research and References

For this prototype, simulating real world physics required some research into real world dynamics. For our wingsuit, we took into account the average weight of an adult man to create the mass of the object that would be our player character - roughly 90.7kgs. The rate of descent was determined through finding the fastest recorded wingsuit flight speed - 220km/h - the rate of freefalling speed - 120 km/h - and the average of the slower cruising speed of a wingsuit - 190km/h. These factors were reduced by one decimal point to make our numbers manageable and more easily balanced while still simulating the same feeling in the Unity engine. 

When it came to creating a “real feeling” of gliding in our prototype, we chose to use a dot vector read of the player’s angle of ascent and descent and used code that would read vector time along with a gradual increase or decrease of speed respectively. When we were working on realism, we found an issue with the way the  wingsuit would behave as it ascended. Rather than slow the forward velocity and begin to fall faster toward the ground, our player would simply be stuck in the sky until they oriented themselves back down again in a descent toward the ground. The dot vector allowed for us to create stronger gravity when ascending to simulate the feeling of falling due to loss of speed.

This small change made the rest of our gliding physics feel more realistic and was a large part of our initial goal with this prototype.


## Gameplay Mechanics

### Wingsuit Gliding

The wingsuit is the one thing the players get a chance to control, but even then it’s at the whim of world physics. Players will have to manipulate the wingsuit and use physics to their advantage to reach the bowling pins and get the highest score possible. 

Players will need to consider the following:

- Wingsuit angle (pitch)
  - The angle of the wingsuit will determine if the player is gaining speed & losing altitude (angled down) or if they are maintaining/gaining little altitude while losing speed (angled up)
- Speed
  - Not only will having a higher speed help get players to the bowling pins faster, but it can help knock more pins down due to the speed the pins are hit. 
- Position
  - Finally, when hitting the pins, the position of the player matters, what angle are the pins being hit, what rotation does the player have, which pins are being hit. The right mix of positioning can be the difference from a strike and a split. 

### Bowling Pins

The bowling pins are set up in a traditional 10 pin formation, where hitting them in specific places increases the chances of knocking more down. The formation includes the head pin at the front. Followed by rows of pins forming a triangle. Hitting the head pin slightly off center can cause a domino effect. Knowing where to hit the pins and being accurate is crucial to knocking the pins down optimally and getting a high score.

## Objective Statement

Prototype a wingsuit mechanic where players have to manage body position to leverage physics and glide down to hit bowling pins. 

The goal is to test how we would design a wingsuit mechanic and implement physics to replicate a real-world wingsuit experience. 


## Design Rationale
When it comes down to the key aspects of our game, we had set out with some initial concepts that both worked as planned and were far from the optimal solution. Let’s look at the four key areas of our game design and how they came to be. 

### Wingsuit Gliding & Physics

The end goal for the wingsuit gliding was to have the player feel like they were gliding in the real world. So we knew we needed to leverage real world mass, gravity, etc. The biggest thing we were trying to do was have it so when the player aimed down, they would gain speed and lose altitude, and as they angled upward, they would gradually lose speed but maintain/slightly gain altitude, until the point they lost all of their speed and started to fall to the ground. 

While we got the initial build working, and had very little issue with having the player gain speed when aiming down, we ran into multiple problems as we tried to get the gradual loss of speed to work, including:
- The player would lose speed to a point and instead of stalling and falling, they would just hover in place
- The player would angle up and start to lose speed, but then start gaining speed in the opposite direction, resulting in them going backward. 
- The player would be angled upward but still have a small amount of speed, resulting in them flying more than gliding. 

After weeks of trial and error, the team finally found a solution that would make the game feel more like what was intended, dot products. We leveraged dot products to determine the angle the player was facing and had it dictate the speed gain/loss over time. While this solution still has its issues and doesn’t match the real-world, it was a major step above the previous iteration and helped the gliding feel a bit more real and fun. 


### Bowling Pins

Initially we had figured the bowling pins were going to be pretty straight forward given we were able to find a lot of resources around dimensions, weight, centre of mass, etc. We quickly learned that ease of access to information does not mean it’ll be easy to replicate in Unity. 

When we set the pins up to be as close as possible to real bowling pins, including the centre of mass, it resulted in the pins being very “floaty” as if they were less affected by gravity. While we spent time tinkering trying to get it to feel more natural with the real centre of mass, we were having an impasse. 

So the team made the executive decision to lean into the Cade part of Simcade in this instance. We revert the centre of mass to the original position in Unity, while retaining all other real-world metrics (i.e. mass) the pins felt a lot more natural and satisfying to hit. 

### Score

For the scoring, we opted for a simple system similar to traditional bowling. Given the game’s short duration, we implemented a single frame structure where players have two chances to knock down as many pins as possible. After each frame, the game resets allowing the players to try again.

We Initially intended for the score to increase when the bowling pins fell over by using the Y-axis value, which would change when the pins fell to count the score. However, we had issues with the bowling pins axes showing weird values. To simplify, we made it so that when the player or pin comes in contact with another pin, it counts as a point. This approach worked well and seems to be reliable. 

## Playtesting

### Playtest Questions

**1. Let’s start with your feedback. Tell us about your experience with this prototype.**

- It looks cool. But it’s kind of hard to control at first. Getting the hang of it. Feels slow maybe?
- Movement feels a bit strange. If the body was normal it would be better. 
- Maybe use A and D instead of Q and E
- Another comment on removing the ragdoll effect.
- Mechanics are fun, like the idea of being the bowling ball. 

In summary, the feedback was very positive - the majority of testers enjoyed the gliding mechanic and having to use your character as the “bowling ball” for this simcade game. The feedback about the character model was quickly corrected by our team to meet the 


**2. What about this works toward simulating the feeling of gliding?**

- The way you can point down and stuff, and all the controls feel like gliding.
- Speed feels realistic, gravity isn’t pulling down too much so there’s time to prepare the approach to pins.
- Gravity is good.

In summary, the simulation seems to mirror the feeling of gliding in this early iteration, but it was not as realistic as we would like it to be as a team. We continued to improve on the simulation by adding and changing variables to achieve an even more realistic gliding simulation that would include stopping and falling when no velocity is present. 

**3. What could be changed or improved to make the feeling more real?
**
- Faster falling pins. It feels sort of slow - could add a glider on the character. Change the model to look more like gliding. 
- Adding a glider will make it feel like he’s gliding more.
- Wind effects maybe.
- Add Menu/Start Screen
- Maybe a number to show distance/altitude
- Things in the background to make it feel like you’re moving. 

Though a lot of the feedback here is cosmetic in nature, there were a few points raised that we took into consideration for our final design. The distance trackers were a consideration for some time but a little outside of our original design intention. The mention of objects or textures to help dictate the distance traveled and the speed the player is moving were fantastic suggestions that we incorporated into our final design.

**4. What does the speed feel like when you are looking down and then back up?**

- Feels like down is still a bit slow. Pointing up looks good.
- Make the speed going down a bit faster. 
- Harder to pull up out of a dive.

This question was added during our first playtest interview as it was prompted by the thought of a playtester, as well as the design intention of our team. Points were raised here that conflicted with earlier feedback and we felt it was necessary to look at the initial question a bit different. This gave us the feedback that was valuable for our final design as it aligned with things we would like to know based on our design intentions.

**5. In what ways could the track itself be changed or improved to create a better playing experience?**

- Maybe it could be thicker, because most of the screen is green. The line is a little thin and the pins are far away. Adding a start screen and reset would be good to add.
- More background objects to feel more like movement. 
- Lines or shapes on the track to show that you’re getting closer.

Finally, this question yielded more cosmetic feedback but got the team thinking more about how the look of the scene could change the feel of the gameplay. Overall, we decided to include some of these suggestions into our final design to increase the appeal and impact of the game’s physics system and mechanics of gliding.

## Resources
Below is the list of resources leveraged for this project, including but not limited too videos, tutorials, forms, and manuels.

### Unity Manuel
  - [Rigidbody component reference](https://docs.unity3d.com/Manual/class-Rigidbody.html)
  - [Freeze rigidbody position in script](https://discussions.unity.com/t/freeze-rigidbody-position-in-script/110627/5)

### Unity forums
  - [What unit is Rigidbody Mass based on?](https://discussions.unity.com/t/what-unit-is-rigidbody-mass-based-on/30267)
  - [Freeze rigidbody position in script](https://discussions.unity.com/t/freeze-rigidbody-position-in-script/110627/5)
  - [Different prefabs having same scale have different size](https://discussions.unity.com/t/different-prefabs-having-same-scale-have-different-size/217039)
  - [Same scale, but different apparent size?](https://discussions.unity.com/t/same-scale-but-different-apparent-size/585862/3)
  - [How do I change the Unit size for a project?](https://discussions.unity.com/t/how-do-i-change-the-unit-size-for-a-project/31958)
 
### Research
- [Bowling Pins - Wikipedia](https://en.wikipedia.org/wiki/Bowling_pin#Tenpins)
- [Bowling Pin Size](https://www.google.com/search?q=bowling+pin+size&oq=bowling+pin+size&gs_lcrp=EgRlZGdlKg4IABBFGBQYORiHAhiABDIOCAAQRRgUGDkYhwIYgAQyBwgBEAAYgAQyDAgCEAAYFBiHAhiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhge0gEIMzIzMGowajGoAgCwAgA&sourceid=chrome&ie=UTF-8)
- [Converting Metrics to Unity](https://www.google.com/search?q=converting+real+measurements+ot+unity&oq=converting+real+measurements+ot+unity&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIHCAEQIRifBTIHCAIQIRifBTIHCAMQIRifBTIHCAQQIRifBdIBCDQwMzBqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8)

### Assets
- [Wingsuit Model](https://www.google.com/search?q=bowling+pin+size&oq=bowling+pin+size&gs_lcrp=EgRlZGdlKg4IABBFGBQYORiHAhiABDIOCAAQRRgUGDkYhwIYgAQyBwgBEAAYgAQyDAgCEAAYFBiHAhiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhge0gEIMzIzMGowajGoAgCwAgA&sourceid=chrome&ie=UTF-8)
- [Robot Kyle Model](https://assetstore.unity.com/packages/3d/characters/robots/robot-kyle-urp-4696?srsltid=AfmBOoo6UkSoeHaAkO0k3Nbr45KDaRm8j2hC6ROCRxGZj0SE4djJ2BSL)
- [Bowling Alley Return Models](https://sketchfab.com/3d-models/tekken-bowling-alley-c80ccd1903ff412389addc76b265ea97)

### Tutorials
- [Making The Wingsuit - Far Cry 5 (Inspired by Games) | Unity](https://sketchfab.com/3d-models/tekken-bowling-alley-c80ccd1903ff412389addc76b265ea97)
