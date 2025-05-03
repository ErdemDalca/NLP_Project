# Sandbox 

## Group members

* [Mateusz](Reports/mateusz.md)
* [Magnus](Reports/magnus.md)
* [Ole](Reports/ole.md)
* [Berkay](Reports/berkay.md)
* [Viktor](Reports/viktor.md)
* [Julian](Reports/julian.md)

## Gameplay video
[Gameplay video](https://youtu.be/QmkOJ7SxWUs)

Bug list:
* Enemies falling through the ground
* Inventory breaking when changing scenes
* Movement in cave scene
* Rebinding keys not working in video

Not implemented
* Axe/pickaxe animation not implemented
* Boss battle scene
* Crafting and loot
* Animals

## Code video
[Code video](https://youtu.be/8Jg-XYgFbog)

### Work distribution matrix

|                                         | Viktor  | Ole     | Magnus | Mateusz | Julian | Berkay |
|-----------------------------------------|---------|---------|--------|---------|--------|--------|
| Procedural generation                   |         | All     |        |         |        |        | 
| Day-night cycle                         |         |         | All    |         |        |        | 
| Inventory                               |         | Touched |        | All     | Touched|        | 
| Wood cutting / object destruction logic |         | All     |        |         | Touched|        | 
| Chunk objects                           |         | All     |        |         |        | Touched| 
| Lakes                                   |         | All     |        |         |        | Touched| 
| Caves                                   |         | Half    | Half   |         |        |        |
| Animals                                 |         |         |        |         |        | All    |
| Enemies                                 | All     |         |        |         |        |        |
| Input system                            |         |         |        |         | All    |        |
| Main menu                               |         |         | Some   |         | Most   |        | 
| Pause menu                              |         |         | All    |         |        |        | 
| health system                           |         |         | All    |         |        |        |
| Weapon                                  | All     |         |        |         | Touched|        | 
| Boss battle                             | All     |         |        |         |        |        |
| Audio                                   | All     |         |        |         | Touched|        |




### Gameplay
The game is a  first person 3D exploration game, where the player explores a changing world, gathers resources, and fights enemies along the way. The world is procedurally generated with a forest biome, and other minor biomes that change the color of ground. There are lakes, vegetation and cave entrances to explore. The caves are static levels filled with enemies.

There are 3 types of enemies in the game and 1 boss encounter. Some enemies use borrowed assets while the Squidman is using a self made animation and model.

The player has 3 types of equipment, a knife, a pickaxe and an axe. The knife is used for combat purposes as the world is filled with different enemies. The axe and pickaxe is used for collecting lumber, storing it in the player inventory.

The inventory is used to store items, mainly the resources gathered from the world. There is also an equipment bar where you can drag items from your inventory. The functionality for using the items on the equipment bar is not yet implemented.

### Teamwork And Development process

For this project we used the Agile development method SCRUM. We organized the work with sprints lasting 2 weeks, with a sprint review at the end of each cycle. The different tasks were defined and distributed using a kanban/SCRUM board where each member assigns themselves a card with a task, and places it according to their current progress. An example of a sprint can be seen here: [SCRUM board](https://github.com/oleelnes/Sandbox/blob/master/Reports/images/terllo_board.png?raw=true) We planned one 1 meeting a week to discuss our progress, 1 online coding session from 10:00 to 13:00 on Wednesdays, and a sprint review on Monday every two weeks. The sprint reviews were physical if possible, so the team had the opportunity to meet each other. 

One of the benefits of working online is not everyone in the group could be physically present a majority of the time. We tried to have the non code related meetings happen in person and on campus, but as we closed in on exam season this proved more difficult. People's schedules were conflicting, as more time was dedicated to other subjects, and rooms at campus became more difficult to book. By moving the meetings online more people were able to participate. 

Another benefit was pair programming, as it is easy to share your screen to get input from another developer. This way you can collaborate and get another pair of eyes on your code. The drawback was the project became more disconnected by not having group members see each other for large periods of time. It is difficult to bounce ideas off each other in an online setting, and there is a different atmosphere when you can talk with other people during a break. Some of the interpersonal relationships are lost when only interacting through a screen. 

When initially pitching the game we had a very broad game design with a lot of different features. None of the developers had created a video game before and set too ambitious goals. You can see the outline in the [Game design document](https://github.com/oleelnes/Sandbox/blob/master/Reports/Game%20Design%20Document.pdf?raw=true) Everyone had different aspects they wanted to work on, and with such a large scope we lost sight of what the game was supposed to be. The result of this was a demo with a small amount of gameplay, but aspects of several bigger features. A clear vision beyond a 3D procedurally generated world was not properly established during development. 

We did a good job delegating tasks and working individually, but a consequence of this was a lack of cohesion when it came to development. Different group members worked on different features for the game without cooperating. This caused problems further down the line, as the gameplay elements overlapped. A better approach would be more cooperation when developing core parts of the game, so everyone knew how key features worked. An example was Ole working on the procedural generation, and other members needed to place items in the world. To solve this he made a short tutorial of how this was done. This was a good solution to bring everyone up to speed, but could have been avoided if we collaborated more.

Our team has been working together on this project for several months now, and we have come a long way. We started out with just a rough idea and now we have a fully functional video game. It has not been an easy journey, but we have persevered and learned a lot along the way. Overall, our team has been a great success. We have learned a lot, we have created something we are proud of, and we have had fun along the way.

### Technical aspects

To challenge ourselves and learn how to work on Unity more effectively, we wanted to include more technical elements. The main focus of our game shifted over time to be about the technical aspects instead of the gameplay and story. This was as a result of the direction it naturally headed in when we chose to make a game that takes place in a procedurally generated 3D world as our first experience with game programming. 

There is no need to reinvent the wheel. And as such, for many of the technical features, we followed tutorials. The code architecture and general functionality of the procedural generation was made following several tutorials. However, we added our own spin to some parts of it, and to all parts, we added several new and self-made features. This includes, but is not limited to:

* Coloring/texturing of the ground
* Lakes
* Procedural object placement forests, bushes, etc. - A unique/secondary noisemap for tree/bush placement
* Dynamic polygon size modifier for the mesh

As the world was procedural, none of the objects or the terrain itself could be pre-placed. It was a challenge to figure out how to create a system that was able to dynamically place things around the world for a number of reasons, but the greatest difficulty was perhaps in making it all seem natural, and not out-of-place.

For the forests, we wanted the trees to be spread wider apart around the edges, and more densely further in. We also wanted subforests inside the forest for increased variety. The way we solved this: after a certain perlin noise threshold (0.6), there was a non-zero probability that a tree might be placed, represented in part by a random number. This probability grows as the perlin noise value gets higher. This way we the density of the forests got more naturally varied. To place the trees, we looped through each terrain chunk at a time with increments of 10 in both x and y, and when it was decided that a tree should be placed, it was placed randomly inside that 10-by-10 grid, making the forest look even more natural. 

Most games need to have an inventory system in order to display, use and store player items in the game. Our interpretation implements a complete inventory system, with a player backpack, a chest inventory and an action bar. These systems are dynamically scalable, which means we can easily change the maximum item size. Items in the game are created as Scriptable Objects; their fields are defined in a C# script and by using [CreateAssetMenu] method, we can simply create new items in Unity and add their properties. Items, when picked up by player, are displayed in the inventory system UI and can be stacked up to their predefined maximum stack size. Stacks can also be split in half. Players can move items between these systems and they will be correctly stored in memory. Overall our inventory system is robust and easily scalable. 

We started out using Unity’s old input system, where at any place in the game you can call to check the state of a key, as this was the easiest for the developers to use. Later we moved the project to Unity’s new Input System, which centralizes all inputs around an Input Action Asset. This opens up a great deal of opportunities, but for our project the biggest one was controller support out of the box. The new Input System works by having the developer set up “actions”, things like jump or crouch, and then give those actions bindings, which we have configured to include both controller and gamepad bindings. One of the big changes this brings is that now all input goes through a centralized class, which binds different action events, like when a button is pressed or released, to methods in different scripts. To use this a class was created for the main “action map”, in Actions_OnFoot.cs. The centralized nature of this system makes it easier to create a system for rebinding controls, as it allows us to have only one instance of the class that reads inputs, which we did. When the player rebinds an action a string containing the information for that action and binding is saved to storage, overriding previous entries for this specific binding, and every time the game loads up every stored binding is applied to a static instance of the Input Action class, which creates the effect of persistent rebinding.

**Note**: In the gameplay video, the rebinding system wasn't working after building the game and running it as an .exe. This was fixed shortly after, but isn't included in the video as it was fixed after the gameplay video was exported. The white background in the rebinding menu was also fixed to look better, the asset it used to use was removed.

### Unity 
Unity Real-Time Development Platform is the go-to development environment for indie and mobile games. The Unity engine, which supports over 25 platforms, has an approximate user base (developers + users) of over 2.7 billion people.

## Strengths:
One of the biggest strengths of Unity lies within its community. Since the vast majority of Unity developers are indie developers, there is a lot of information and guides/tutorials available on the internet, making it easier to learn and fix issues with. Unity is also fairly easy to get started with, and is better suited for small-scale projects than Unreal. It also has the largest developer market by far, and the biggest marketplace for assets, like for visuals and sound. Unity also has a very high level of modularity, in the way that most things are done by attaching scripts to different gameobjects, which also makes it easy to understand how other people’s contributions work by just a glance. This makes it a lot easier to collaborate on big projects with, as people are unlikely to be working on the same file at the same time, especially with how much we separated functionality into different scripts. Godot and Unreal are both more powerful for their own primary purposes, Godot with 2D games and Unreal for graphics-intensive 3D games, but they lack Unity’s simplicity and ease-of-scriptability. The Unreal engine is known to have a higher skill requirement than Unity, and in a game with so many people, Unity’s accessibility and modularity benefitted us. 

## Weaknesses
For a sandbox game like ours, where graphics plays a bigger role then for example for a 2D game, Unity engine has weaker graphical capabilities than Unreal. A major unrelated issue we did experience with Unity was a difficulty merging scenes using Git, which made us avoid having more than one person working on the same scene at the same time. Thankfully, we were able to work around that, with the help from Simon.

For a first time experience as game developers we chose to use Unity as our platform because of its strengths and modularity. Unity is probably the best platform to begin this journey and we are satisfied with our choice, altho we want to acknowledge that if this project were to continue and scale up in size, then the preferred choice of game engine would probably be Unreal. 










