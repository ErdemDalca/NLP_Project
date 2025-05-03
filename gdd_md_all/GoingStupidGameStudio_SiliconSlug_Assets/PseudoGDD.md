#CODENAME: Aux

This game is a 2D side scroller similar in style to the Metal Slug series. Each level is a map in which you advance to the right finding different sets of enemies that can hit you with either melee attacks or ranged projectiles like bullets, grenades, bombs, etc. At the end of the level you would find a boss that is thematically related to the map itself and its style.

##Theme and Story
Our main character is an old PC Tower who wants to join the glorious PC Master Race group. In order to do this he needs to obtaind new components for himself some of which can be a new processor, a graphics card, motherboard, RAM, Power Supply, etc. He can use this components to upgrade himself and acquire a new ability with each one.

The problem is that this components have been stoled/are protected/whatever by consoles and console gamers. Our protagonist needs to go to the worlds/levels/maps of each big console developers, fighting and winning against the barrages of consoles that will try to stop him from getting into its boss. When he wins against the boss of each map he will obtain the component that was being protected.

The final map should lead the player into PC Master Race's headquarters. There he will find out that the main leader of the PC Master Race secretly likes playing with consoles. For this blasphemy the player will need to fight the final boss in order to restore the PC Master Race gang to its original purity.

##Characters

###Main Character
Our character can move left and right, jump, melee attack and range attack. This options will be available at the beginning of the first map. There is the posibility to add new abilities with each new component. Such abilities could be different projectiles or melee attacks, double jump, dashes to left and right, more health, etc.
He would be faster than the Metal Slug character in order to give the game a bit more speed.

###Simple enemies
The enemies in this game will have either the abilities and movement of the player or a subset of them. This abilities can be highly modified in ways such as changing speed, damage, range, etc. We could also have slow and tanky, fast and squishy and ranged annoying enemies as the team sees fit.

###Bosses
All bosses follow the pattern system in which they keep iterating (maybe randomly) between different custom made attacks that they have. In such attacks they can be invulnerable or not, normally giving the posibility of being hit when the player succesfully avoids the current pattern.
This bosses tend to be big in comparison to the player and take up quite a bit of space in the scene but we could have some exceptions.

##Visual design
This will be a low res pixel art game in which we will work with tiled maps for composing each level and spritesheets to create the animations for the characters.
The tilesets will vary on each level since the theme changes from one console "world" to another. The sprites will be very low res (in the order of 32x32 for the main character) but they will try to show a high degree of fluidity using a lot of frames for each animation.
The tiled maps could be in the "front" of the game while we have a full image on the background but this could be discussed.

##Initial Ideas for Tools used:
- MonoGame as the game engine (http://www.monogame.net/).

- Aseprite for drawing the sprites(https://www.aseprite.org/).

- Pyxel Edit for drawing tiles(http://pyxeledit.com/).

- Texture Packer + Physics Editor to make the sprite texture atlas and the collisions(https://www.codeandweb.com/).

- Some library like MonoGame.Extended or Nez for loading tiled maps(.tmx) into the engine(https://github.com/craftworkgames/MonoGame.Extended or https://github.com/prime31/Nez).

- TexturePacker-MonoGameLoader to load the sprite atlases into the engine (https://github.com/RandolphBurt/TexturePacker-MonoGameLoader).

- Cubase for making the music (http://www.steinberg.net/en/products/cubase/start.html).


