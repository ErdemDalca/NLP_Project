# Dungeon Rogue Game ![Status](https://github.com/madmed677/dungeon-rogue/actions/workflows/general.yml/badge.svg)

> **Note**
> The work is still in progress

## Description
Dungeon Rogue is a simple pet project that
helps me to understand the basic of game development.

During this pet project I'd like to learn:
### Map
- [x] How to deal with `map`. How to render the map, how to add collisions to the map and some interactions with it
- [x] How to create multiple levels
- [ ] How to create multiple game behaviour. Like in [It Takes Two](https://www.hazelight.se/games/it-takes-two/)


### Animations
- [x] How to animate the player
- [x] How to animate the enemies
- [ ] How to animate the player with multiple animations (when the player are walking, climbing) 

## Game Design Document
### Game design
The player has different maps with different game design.
1. Platformer. The user has side view camera and the usual platformer mechanics
   - Jumping
   - Fighting
   - Climbing to reach different map levels
   - Level progression (you may boost your level and it cause better armour, attack, etc)

2. Dungeon Crawler. User has top view camera and the usual dungeon crawler mechanics
   - Fighting
   - Crafting
   - Level progression (you may boost your level and it cause better armour, attack, etc)

### Technical requirements
The game should work as:
- `[required]` Native App
- `[required]` Web App
- Mobile App

### Documentation / Tests
All the code should be covered by documentation and tests and integrate it into
CI / CD pipeline.

## Run
### Development
```shell
cargo run

# For faster compilation use this command
# cargo run --features bevy/dynamic
```

### Debug
```shell
cargo run --features bevy/dynamic --features debug
```
