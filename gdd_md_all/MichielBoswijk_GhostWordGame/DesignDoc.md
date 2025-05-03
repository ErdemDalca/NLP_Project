# Ghost Word Game Design Document

* Michiel Boswijk, michiel.boswijk@gmail.com
* University of Amsterdam, 10332553

This is an initial design document for an implementation of the Ghost game (https://en.wikipedia.org/wiki/Ghost_(game)). The application, called Ghost Word Game, will run on Android devices (both smartphones and tablets). For a list of features and UI walkthrough, please check out the README file in the Ghost Word Game project.

## Controllers / Activitiy classes with menu items

##### IntroScreen

![Intro](/doc/Sketches/intro.jpg)

##### Highscores

![Highscores](/doc/Sketches/highscores.jpg)

##### Settings

![Settings](/doc/Sketches/settings.jpg)

##### NameInput

![Names](/doc/Sketches/names.jpg)

##### GameScreen

![Game](/doc/Sketches/game.jpg)

##### WinnerScreen

![Winner](/doc/Sketches/winner.jpg)

## Additional Classes

##### Classes with some variables / functions

![Classes](/doc/Sketches/classes.jpg)

##### Some interactions between classes

![interactions](/doc/Sketches/interactions.jpg)

One (or two) APIs will likely be used for the Dutch and English dictionaries.

## Visual Representation

Color Palette: Grey/Green or Grey/Orange (two themes)

Drawables:

* Ghost Icon (Launcher and IntroScreen)
* Play Icon (IntroScreen, Highscores, NameInput)
* Highscores icon (IntroScreen, WinnerScreen)
* Information icon (IntroScreen and HowToPlay dialog)
* Settings icon (Introscreen)
* Enter icon (GameScreen)
* Star icon: gold, silver, bronze, and green
* Ribbon image/icon (Highscores)
* Cup image/icon (WinnerScreen)
* (Optional: ) Handshake icon (Acknowledgements dialog)

### Acknowledgements

* (Future) Icons designed by Mees Daalder

