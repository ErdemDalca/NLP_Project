# Gamebuilders Game Jam Fall 2016
Welcome to the first Gamebuilders Game Jam of the year, and the last game-making event of the semester! I'm Brad and I'll be working as the Project Lead for this game. If you need anything, let me know and I'll try to help. I hope you're all excited to work on this game, cause you'll be working on it for the next 24 hours. 

<b>Please read through this entire document before you start working, it'll help make sure we're all on the same page and don't step on each other's toes too much. If you don't, when you run into an issue I'm gonna ask you to read through this page to see if it explains your problem before I come help you.</b>


## Design
We'll be using a separate document, DESIGN.md, as our game design document, but as a quick refresher or for those who don't know much about the game we're making, I'll give a brief overview here.

This game will be a 2D top-down horror-puzzler with Metroidvania elements and will be made in Unity. For those who don't know the term Metroidvania, the basic idea is there's a lot of backtracking to previous areas to access things you couldn't before after getting new abilities. The game will take place in a Resident Evil / Luigi's Mansion style mansion, and gameplay be based around collecting and using various lenses. Each lens will apply a different visual effect to the screen, and will change certain objects in the house into different things. For example, one lens might change a portrait into a door, but also a chair into a spider monster that chases you. The player will be unable to fight directly, but instead will have to use their lenses in clever ways to survive and navigate the mansion. For more information, please refer to [DESIGN.md](https://github.com/branderson/MansionHorror/blob/develop/DESIGN.md "Game Design Document").


## Setup
### Unity
First, make sure you have Unity 5.5 installed. Opening the project with an older version of Unity will not work. If this is not installed, install it before doing anything else. You can download Unity [here](https://store.unity.com/download?ref=personal "Unity"). 

### IDE
If you'll be working on the game's code, get a decent IDE installed ([Visual Studio 2015 Community Edition](https://www.visualstudio.com/downloads/ "Visual Studio") on Windows, [Jetbrains Rider](https://www.jetbrains.com/rider/download/ "Rider") on Mac or Linux). I recommend against using the Visual Studio 2017 Release Candidate because it might have compatibility issues with Unity.

### SourceTree
We'll be using git as our version control system for this game. We'll use a program called SourceTree to manage our version control, because it will make collaborating easier and will hopefully minimize the amount of time we have to spend dealing with merge conflicts. You can download SourceTree [here](https://www.sourcetreeapp.com/ "Atlassian SourceTree"). It'll make you set up an Atlassian account, so do that. Tell it not to install a default global .gitignore or you'll have problems. Once you have SourceTree installed and opened, open <nobr>Tools-\>Options</nobr> and set Default User Information to your Full Name and the email address associated with your GitHub account (if you don't have a GitHub account, make one now).

### Repository
The repository is hosted at https://github.com/branderson/MansionHorror (the website you're most likely viewing this document at). 

Clone the repository to your computer using SourceTree:
1. Click Clone / New
2. Type the repository's URL into Source Path / URL
3. Set Destination Path to some place you'd like to put it on your computer
4. Under Advanced Options, make sure Recurse Submodules is checked. This is necessary because the repository contains a git submodule (at Assets/Scripts/Utility) which we're telling git to download and initialize. Don't worry about what this means, it doesn't matter.
5. Click Clone, which will download the repository to your computer and open it in SourceTree.

### Trello
We'll be using a Trello board to keep organized during the Game Jam. Please make an account on [Trello](https://trello.com "Trello"). I'll add each of you to the Gamebuilders team I've set up. This will allow us to keep track of what everyone is doing, raise issues to alert teams of things that need to be done, and easily share links amongst ourselves.

### Tiled
For level editing we'll be using a program called Tiled which allows us to design our levels in a tile-based 2D grid. There is no nice, straightforward way to do this in the Unity editor, so Tiled will be much nicer to work with. You can download Tiled [here](http://www.mapeditor.org/ "Tiled Map Editor").

### TiledLoader
Unity does not have built-in support for Tiled, so we'll be using a tool that I wrote to assist with loading our levels into Unity. There's a free version of the tool available [here](https://github.com/branderson/TiledLoader "TiledLoader"), but we'll be using a version with more features which I intend to release on the Unity Asset Store soon. The tool consists of two DLL files, TiledLoader.dll and TiledLoaderEditor.dll. TiledLoader.dll is essentially the same across both the free and paid versions of the tool, and is just a set of components to help TiledLoader keep track of objects it instantiates. I don't care about this file being stored in a public repository so I've already added it to the repository. TiledLoaderEditor.dll is the tool itself, so I don't want this file in the public repository. I've configured our repository to ignore this file so it doesn't get included. I'll set up a link to the file through Dropbox which I'll write on the board during the game jam so you can all download this file. Place this file into Assets/Scripts/TiledLoader/bin/Editor/. It's important that it is placed in an Editor folder or it will not work.


## Workflow
### Development Teams
We will be grouped into teams depending on what portion of the project we want to focus on. These are fairly loose teams, and a few of us (myself included) will probably drift between teams, helping out where we're needed. That said, the main teams will be:

#### Core Game Development 
<b>Team Lead:</b> Asaf and Brad  
<b>Role:</b> Program the game and gameplay. Make sure everything comes together nicely and functions. This team will most likely have multiple sub-teams for different features.

#### Shaders and Visual Effects
<b>Team Lead:</b> Brad  
<b>Role:</b> Design and implement cool looking visual effects for the various lenses and other effects.

#### Level Design
<b>Team Lead:</b> Mike  
<b>Role:</b> Work in Tiled to design the layout of the mansion and the progression of the game.

#### Art
<b>Team Lead:</b> Adina  
<b>Role:</b> Make creepy art assets.

#### AI
<b>Team Lead:</b> Victor  
<b>Role:</b> Write AI scripts to make each of the game's enemies feel different and interesting.

### Trello
Our Trello workflow will be pretty simple. If you think of something that needs to be done, make a card on the ToDo list and write a description describing exactly what needs to be done. Drag it up or down based on the priority of the feature/bug. If you start working on something that isn't on the ToDo list, make a card on the Assigned list and click Members on the card and add yourself. If you're looking for something to do, pick a card off the ToDo list, drag it to Assigned, and add yourself to the card. Most of us should be assigned to exactly one card at pretty much all times. When you're done with a card, drag it to Done. If you have an Idea you want to discuss, make a card on the Ideas list describing your idea. We can discuss Ideas through comments on the card. An Idea can be moved to ToDo once we decide we want to implement it. Finally, the Random Stuff list is for random posts and discussion unrelated to game features.

### We are the Asset Makers, and We are the Makers of Memes
This section is specifically targetted at Adina, Mike, and anyone else working primarily on assets. For you guys, you won't be working directly with version control very much since it'll be unnecessarily cumbersome to deal with. Instead, you guys will use a public Dropbox folder that I'll set up for you, and will keep everything you make in there. When something you make needs to be used in the game, someone will copy the file into the game's Assets directory and push it to version control. We've found this method of dealing with asset production is by far the easiest and most efficient.

### Version Control
For the rest of us, everything we make will be directly version controlled. Version control with Unity (or any editor based game engine, really) can be a complete nightmare unless certain precautions are followed. Thus...

#### The Five Commandments of Unity Version Control:

1. <b>Thou shalt not open, modify, and save to any scene that they do not own.</b>

    When you open the project for the first time, the first thing that you should do is create a new scene <nobr>(File-\>New Scene)</nobr> and name it "\[YourName\]Scene" and save it to Assets/Scenes <nobr>(File-\>Save Scene As</nobr>). This scene is your workspace. You are only ever allowed to make changes to this scene, or another scene you've created, unless explicitly told to modify another scene. This is extremely important because it's basically impossible to resolve a conflict between two people who've modified the same scene without throwing out one person's changes. If you make a change to someone else's scene, your changes will almost definitely be overwritten.

2. <b>Thou shalt be very, very careful about modifying prefabs.</b>

    Unity prefabs are reusable bags of components and values that can be instantiated. They're very useful, and just about everything in the game should be a prefab. One of the advantages to prefabs is that by making a change to the prefab itself, the change will propagate to all instances of the prefab across all scenes. The issue is that if two people modify a prefab at once, they could end up with a merge conflict within the prefab's serialized data. Usually we'll be able to solve this by storing one person's changes to the prefab in a separate temporary prefab, pulling the other person's modified prefab, and then reapplying the changes on top of their version of the prefab.

3. <b>Thou shalt always press File-\>Save Project before committing to source control.</b>

    Changes made to prefabs and other assets in the project are not necessarily saved to disk immediately but are instead kept in memory. If you commit without telling Unity to save these changes to the disk, the changes will not be included in your commit.

4. <b>Thou shalt never, under any circumstances, commit broken code.</b>

    This goes for any version controlled project, really, and is not specific to Unity projects. If your code does not compile, it absolutely should not be committed. Above that, it should definitely not be pushed to GitHub. The last thing anyone wants is to pull from the develop branch before committing their code, and suddenly have the project refuse to compile because someone pushed broken code. If your code is unfinished or buggy and refuses to compile or breaks existing features, don't commit. If you absolutely must commit something but have broken code in your project, don't stage the file with the broken code, or any other files which rely on changes you've made to that file. We don't want another "You only jump once" situation...

5. <b>Thou shalt never commit directly to master or develop.</b>

    We will be using the Git Flow workflow for this project, so all commits should be first committed to a feature branch for the feature they work on. Once a feature is in a state that it's ready to be added to the project, you should submit a pull request as described below. We will only pull to master from develop for major versions, such as the end of the Game Jam, so we won't be using master very much during the Game Jam.

If all of that is followed, version control should be a relatively smooth and painless task. The general process goes like this:

1. You want to start working on a new feature, so you open SourceTree and click Git Flow. In the window that opens, click Start New Feature. This will open a window to start a new feature branch. Name it after your feature, and set it to start at the latest development branch. This will setup your local git repository so that you're working on a new branch for your feature.
2. Write your feature.
3. Once you've finished the feature and want to push it to the project, make ABSOLUTELY SURE that your code doesn't break any existing features and runs without issues.
4. Open SourceTree and click Commit. Select each file that's relevant to your feature and click Stage Selected. If everything in the list of unstaged files should be committed, you can click Stage All instead. 
5. Now commit your changes to your local feature branch. In SourceTree, type a commit message and press Commit. Your commit message should have a short (less than 80 characters) description, which should be written in the imperative mood (think of it as saying what the commit does to the project when someone adds the commit to their project), followed by a blank line and a paragraph description explaining details about the commit, if necessary.  

    Here's an example of a good commit message:  

    Fix player's head exploding when they they press the Q key

    This commit fixes a bug in which the player's head would violently explode whenever they pressed the Q key. This was caused by Cthulu having taken up residence in the code related to handling the Q key in the player controller. Whenever the player pressed the key, it disturbed Cthulu, resulting in him taking vengence on the player by making their head explode. This was fixed by adding warding incantations to the player controller's code, forcing Cthulu to leave.
6. Before adding your feature to the develop branch, you'll need to pull from origin/develop first. Click Pull in SourceTree and select origin/develop as the remote branch to pull from. Make sure Pull Into Local Branch is set to your local feature branch. If not, you'll need to checkout your local feature branch. Click OK.
7. Fix any merge conflicts that come up. The easiest way to deal with this is usually just to select files in conflict and click Discard if your changes weren't intentional and can be thrown out. If you made intentional changes to the file, you'll need to actually resolve the conflict which can get complicated. If this happens, call me over.
8. Now that your local feature branch is up to date with origin/develop, you can merge it to origin/develop by clicking Git Flow in SourceTree. Click Finish Feature. This will open the Finish Feature window. Select Delete Branch if you're done with the feature and click OK.

If while working on a feature something comes up that you need to address quickly, you can commit a fix directly to develop by following a slightly different process:

1. Checkout the develop branch and click Fetch in SourceTree to update your local develop branch to the state of origin/develop.
2. Write your fix in your local develop branch.
3. Once your fix is finished, commit to develop.
4. Pull from origin/develop to your local develop to incorporate any new commits on origin/develop into your local branch.
5. Resolve any merge conflicts.
6. Push from develop to origin/develop.

### Unity
#### Standard Assets
Please don't import any Unity Standard Assets. They tend to pull way too many random assets into the project which will not be used. If you absolutely must use something from the Standard Assets, let me know and I'll make sure we only pull in exactly what we need, rather than 50MB of random images and a separate input manager.

#### Prefabs
Use prefabs for everything. Every object in the game should be an instance of a prefab, even if there's only one of that object in the entire game. It's much easier to change objects when there's a prefab stored on the disk somewhere that can be edited from any scene to change all instances of it at once. Prefabs should be given descriptive names and no two prefabs should have the same name. Use a folder hierarchy to organize prefabs.

#### Code
Use hierarchial namespaces to enclose all classes for each major feature. Namespaces should be named after the folder hierarchy to the script, ignoring the Scripts folder. If a script is at Assets/Scripts/AI/Bosses/, its namespace should be "Assets.AI.Bosses".

Try to follow a consistent coding style. Make all of your classes' fields (class variables) private unless they absolutely need to be public, and prefix them with the \[SerializeField\] attribute if they need to be edited in the Inspector. Name private fields using \_camelCase (starting with a \_) and public fields using PascalCase. Similarly, make all methods (class functions) that are only used by the class private. All methods should be named using PascalCase. Variables local to functions should use camelCase without the \_. Following this will help minimize your class's public API to what should actually be public, and the naming scheme will help everyone keep track of which variables are public, private, or local.

Make use of classes in the Assets.Utility namespace, particularly CustomMonoBehaviour. Every component you instantiate should inherit from CustomMonoBehaviour. It provides a bunch of really helpful methods for calculating distances and directions between objects, as well as caching references to components. Normally, components on objects are accessed by calling `GetComponent<TypeOfComponent>()`. This is a slow call, so you want to avoid calling this in an Update loop. Usually you'd want to call this for every component your class needs access to in Awake and store the references to the components in private fields in the class. This is still the best thing to do, but CustomMonoBehaviour has versions GetComponent that automatically cache the components for you, which is convenient. Assets.Utility.Static also has some really useful functions for manipulating transforms.

Above all, don't worry if your code isn't perfect. This is a game jam and it's much more important that we get features working than that our code is nice and clean. Try to make your code readable and try to follow these suggestions as well as you can, but you don't have to treat them as rules.


## Finally...
If you got this far and actually read all of that, thanks for reading! Now go ahead and get started, and have fun. Hopefully by the end of this we'll have something made that we can all be proud of!
