Web-based Simon game
====================

This game is developed using the Behavior Driven Development methodology. It serves as a practical example to illustrate my public talk 'Bug-Free Games from Day One with Behavior Driven Development'.

Play this Simon game at [jerle76.github.io/simon-game/](http://jerle76.github.io/simon-game/)

Repository structure
--------------------

From the commit where the Game Design document is added, Behaviour Driven Development is observed:
- the 1st commit will turn a portion of the Game Design document into a series of failing testcases.
- the following commits will implement this portion of the Game Design document and progressively make the failing testcases pass.
This repeats until the Simon game is complete and playable.


Getting started
---------------

This game was bootstraped using Yeoman, Grunt and Bower. Before you begin, make sure Grunt and Bower are installed globally by running the following command:

> npm install -g grunt bower

Once you've checked out a fresh copy of this repository, install all the Nodejs and client-side library dependencies by running the following command from the root of the repository:

> npm install && bower install

To run the game:

> grunt server

To run the testsuite:

> grunt server:test
