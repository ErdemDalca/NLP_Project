# 1-HP-Wizard

![1 HP Wizard Menu](./Images/Picture_Title.png)

## Introduction
1 HP Wizard is a multi-level, gesture-based, spellcasting game. In this game, the user stands in a stationary location and fends off waves of enemies homing in on their position. 

The player will have to react quickly and strategically since it only takes one hit to defeat them.

**Notice: The server that this game runs its gesture recognition on has been shut down. You can contact me if you still wish to try this game out so we can work something out.**

**UPDATE: The server is back and running again! You will need to recompile the game with Unity.**

## Getting Started (Just Playing)
### Prerequisites
* Oculus (Software)
* Oculus Rift (Hardware)
* Internet connection

### Downloading (55.3MB)

1. Go to the release page by clicking this link

	https://github.com/scott0123/1-HP-Wizard/releases

2. Click the most recent `Build.zip` to download the latest build

3. Unzip the `Build.zip` at the location where you would like to store the game.
	
	Only the Windows version is available at present time.

### Running

Double click `1 HP Wizard.exe` from the folder from the previous step to start the game.

## In-game Pictures

![1 HP Wizard Level 1](./Images/demo1.png)

## Getting Started (Development)
### Prerequisites
* Oculus (Software)
* Oculus Rift (Hardware)
* Unity 2018.2.14f1 (for development)

### Downloading (1.77G)

Clone this project.

`cd CLONE_LOCATION` (use cd to navigate to your desired clone location)

`git clone git@github.com:scott0123/1-HP-Wizard.git` or `git clone https://github.com/scott0123/1-HP-Wizard.git`

### Scenes

* `1-HP-Wizard/Assets/Scenes/Menu.unity`
* `1-HP-Wizard/Assets/Scenes/Tutorial.unity`
* `1-HP-Wizard/Assets/Scenes/Level1.unity`
* `1-HP-Wizard/Assets/Scenes/Level2.unity`
* `1-HP-Wizard/Assets/Scenes/Level3.unity`

### Building

`File > Build Settings`

Select your target platform.

`Build`

Select your build location.


## Design

### Scenes

![1 HP Wizard Scene 1](./Images/scene1.png)
![1 HP Wizard Scene 2](./Images/scene2.png)
![1 HP Wizard Scene 3](./Images/scene3.png)

### Modeling (Blender)

![1 HP Wizard Inferno](./Images/inferno.gif)
![1 HP Wizard Desert](./Images/desert.png)

### Spell gestures
![Fireball gesture](./Images/fireball_icon.png)
![Lightning gesture](./Images/lightning_icon.png)
![Ice gesture](./Images/ice_icon.png)
![Earth gesture](./Images/earth_icon.png)
![Air gesture](./Images/air_icon.png)
![Shield gesture](./Images/shield_icon.png)

### Game Design Document
https://docs.google.com/document/d/1hs4El7qzT2vCHhaPN9zTqvtF0LksF_KemcwoVwB_Los/edit?usp=sharing

### Project initial proposal
https://s3.us-east-2.amazonaws.com/scott-liu-storage/Project+Proposal+498.pdf


### Gesture collection data sample
3D representation of one of our earth gestures datasets.

This is used to train the `Earth` Class in our model.
![Earth gesture 3d](./Images/earth.gif)

3D representation of one of our erroneous gestures datasets.
This is used to train the `Unknown` Class in our model.
![Error gesture 3d](./Images/error.gif)

### Gesture Model Serving Architecture
![Gesture Model Serving Architecture](./Images/GestureServingArchitecture.png)

### Class Hierarchy
![Hierarchy image](./Images/hierarchy.png)

### Theme
![Theme image](./Images/theme.png)


## Contact

You may reach me at `1hpwizard@scott-liu.com` to inquire about this project.
