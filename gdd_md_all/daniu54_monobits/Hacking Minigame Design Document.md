# Hacking Minigame Design Document

The goal of this project is to implement an accessible hacking minigame, which still offers the joy of creating and executing a plan for infiltrating and taking down the defenses of a network.

# Network Structure
## Nodes
The network consists of multiple nodes which the player can traverse. By clicking a node, the player avatar can move to that node. When the avatar has reached the node, it can install various [programs](#Programs) to influence the structure of the network. While most of the nodes in a network are "empty" and serve as paths for the player avatar, there are some special types of nodes, which facilitate the game loop by e.g. providing gameplay incentives to the player or posing obstacles to player progression.

These are the special types of nodes:
- Gateway: the spawning point and the extraction point for the player avatar
- Database: needs to be hacked by the player to gain points
- Firewall: obstacle which has to be broken down before it can be traversed by the player

### Example Network
![Example Network](Example%20Network.svg)

## Programs
In order to interact with the network, the player can install programs on the nodes.
The programs include:
- `BREAK`: transforms firewalls to empty (traversable) nodes after a delay
- `COLLECT`: collects data from databases
- `DISCONNECT`: ends the level if the player is at the gateway, all collected data is counted towards the players score

# Ui and Player Interaction
- display of the programs which can be installed at the current node
- player movement using the mouse

# Out of Scope
## Enemy Ai Actors
Need solid network implementation first. Very welcome in future iterations.
## Camera
Networks should not get large enough to require a mobile camera.
