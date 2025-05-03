# Asteroid 3D

## Description

This is a project to learn more about the Godot Enginge and Blender. The main focus is to learn how to make use of unit testing in Godot. The ideal would be to have a CI/CD pipeline that runs the unit tests and builds and deploys the game itself. The second goal is to learn how to export the game to itch.io and make it playable.

## Documentation

The documentation is written in Markdown and can be found in the `docs` folder.

- [Game Design Document](docs/GameDesignDocument.md)

## Dependencies

- Godot 4.2.2 or later
- Blender 4.1.0 or later

### Godot Addons

- [GdUnit4](https://github.com/MikeSchulze/gdUnit4)
- [Little Camera Preview](https://github.com/anthonyec/godot_little_camera_preview)

## Status

This project is currently in development. The first playable version will be released on Itch.io.

### CI

So basically I tried setting up CI pipeline with Github and GUT as unit testing tool. I tried different Github actions.

- [Godot CI](https://github.com/abarichello/godot-ci)
- [Godot GUT CI](https://github.com/ceceppa/godot-gut-ci)

The issue was that I couldn't get the unit tests to run. After some digging I found out that it was a common Godot issue due to the import files. There is a good description of why here: https://github.com/alessandrofama/fmod-for-godot/issues/23#issuecomment-1754475551
With Godt 4.2.2 the issue was [resolved](https://godotengine.org/article/maintenance-release-godot-4-2-2-and-4-1-4/#improved-command-line-export-pipeline), but GUT did not work with the new version. So I decided to use GdUnit4 instead. GdUnit4 also has a [CI action](https://github.com/marketplace/actions/gdunit4-test-runner-action) that works perfectly. So now the CI pipeline is set up and runs the unit tests. 🎉

### CD

So the CD pipeline is not set up yet, but I have a plan. I will use Github Actions to build the game and then upload it to Itch.io. Most likely I will use the [Godot CI Action](https://github.com/marketplace/actions/godot-ci) for this.
