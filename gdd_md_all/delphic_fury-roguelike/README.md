# Fury Roguelike

Using [Fury](https://github.com/delphic/fury/) to replicate [rusty_rogulike](https://github.com/delphic/rusty_roguelike)

See the [Game Design Document](gdd.md) for design details.

MVP and Stretch goals of the document have been completed and represent a completion of the functionality of rusty roguelike, 
The extensions are over and above the port which might be interesting or valuable to implement.

## Build
One time build: `browserify ./scripts/client.js -o ./build/scripts/fury-roguelike.js`

Continuous build: `watchify ./scripts/client.js -o ./build/scripts/fury-roguelike.js`