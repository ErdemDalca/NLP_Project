# Wizard Duel
Wizard Duel is a mobile game for Android, written in Java. It was made as part of the Mobile Application Development University module in 2024, earning a final mark of 90. 

It is a simple two-player arcade game, played locally with each player taking over one side of the screen with their own Wizard, engaging together in a magical duel. A player is able to unleash fireballs with a swipe gesture, releasing the fireball in a direction based on the swipe trajectory. The fireballs travel in said direction, bouncing off walls, until they reach the opposite end of the screen, either hitting the opponent and dealing damage, or missing them. The amount of fireballs at either player’s disposal is limited, but recharges continuously. If two fireballs hit each other, they both fizzle out. 

To defend themselves, a player is also able to conjure a shield with an outwards pinching gesture. This shield is maintained as long as the player holds their fingers down and the player may not throw fireballs while they have a shield active. A shield can only be upkept for a limited time, as it depletes when used, and recharges when not. Additionally, the larger the shield, the faster it depletes. Any fireballs hitting a shield fizzle out.

When a player’s wizard is hit by a fireball enough times to deplete their health points, they lose the game.

The game was made for very large screens, such as a Google TV, but has also been tested to work on tablet devices. Standard mobile screens are too small to play the game effectively in its current state.

Demo video, including a live play session at the end, can be found on Google Drive: [here](https://drive.google.com/file/d/18ybpr5ITpjCa_FCiSLSK519CnOzsx5fg/view?usp=sharing).

## Technology Used
The game was built in raw Java using Android Studio. No game frameworks or libraries were employed. The game itself is a Custom View, with a custom draw on a Canvas. The application follows best practices of the standard Android MVVM design pattern as best as possible, as well as observing principles of solid games programming.

The following list shows only some of the aspects of Android used in this project:
* Service, for managing the game thread and orchestrating the game loop
* Choreographer, for synchronising the game thread to application frames,
* Gesture listeners, gesture detectors, and a multitouch controller by Luke Hutchinson (licence in the relevant file) for creating a GameInputManager and handling complex multi touch input with gestures,
* AnimationDrawables, for animation, the implementation of which in custom view canvas drawing was a lot more complicated than it should have been,
* Fragments, for the pause menu (modal)

Particularly the multitouch inputs, the custom canvas drawing of game objects, including animations, and the collision system have been the most complex features to implement.

## Design
Before implementation, I produced a [game design document](https://github.com/mkocvara/WizardDuel/blob/master/Design_Document.pdf) for the game, which explains all the feature as they were expected to be implemented, as well as UI sketches and feature prioritisation.

## Screenshots
![image](https://github.com/user-attachments/assets/8c0aaa54-946d-4ecb-be9f-fc8bf74a3c79)
![image](https://github.com/user-attachments/assets/a4df2d6a-748b-4f09-a231-ee3d37173d64)
![image](https://github.com/user-attachments/assets/4556fdad-6122-49bc-a83f-41819e4dac26)
