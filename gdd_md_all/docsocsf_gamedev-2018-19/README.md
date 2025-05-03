# Game Dev Karma Game
#### Using Phaser 3 + ES6 + Webpack

ACTIVE: Repo for the gamedev Karma game Game Design Document: https://docs.google.com/document/d/1Ctt2m0ErAWTGdbF28D6xZCM1ODkzASjJUx4vugNpew8/edit?usp=sharing

The boiler plate code is based on the Bootstrap project https://github.com/nkholski/phaser3-es6-webpack which was based on the Boostrap project for Phaser 2 "Phaser + ES6 + Webpack" (https://github.com/lean/phaser-es6-webpack), https://github.com/belohlavek/phaser-es6-boilerplate and https://github.com/cstuncsik/phaser-es6-demo.

# Setup
You’ll need to install a few things before you have a working copy of the project.

## 1. Clone this repo:

Navigate into your workspace directory.

Run:

```git clone .....```

## 2. Install node.js and npm:

https://nodejs.org/en/


## 3. Install dependencies (optionally you could install [yarn](https://yarnpkg.com/)):

Navigate to the cloned repo’s directory.

Run:

```npm install```

or if you choose yarn, just run ```yarn```

## 4. Run the development server:

Run:

```npm run dev```

This will run a server so you can run the game in a browser.

Open your browser and enter localhost:3000 into the address bar.

Also this will start a watch process, so you can change the source and the process will recompile and refresh the browser.


## Build for deployment:

Run:

```npm run deploy```

This will optimize and minimize the compiled bundle.
