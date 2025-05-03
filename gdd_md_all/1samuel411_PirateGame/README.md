# PirateGame

The repository for the uncompleted game built for a pirate-based battle royale game.

[Link to Game Design Document](https://docs.google.com/document/d/19fifzVWuw7CY9fiCjpY0VLw-2T_jBMtJVToUnzLqMaY/edit?usp=sharing)

# View a demo of the networking base
[![Networking Showcase](http://img.youtube.com/vi/u7PV6JSmpco/0.jpg)](https://www.youtube.com/watch?v=u7PV6JSmpco "Networking Demo")

# Networking breakdown (Self-written socket based server)
- Master Network Server
  - Every player in a region (NA, SA, EU, AU, etc) connect to this server
  - This server contains logic for
    - Matchmaking
    - Online status updater
    - Party invites
    - Party forwarding
  - It contains a list of every in-game server and their status (In-Game, Out-of-game, Needs players)

- Party Server (Self-written socket based server)
  - All party servers are connected to the master network server and vice versa, and are based on that particular region
  - Every player is in a party at all times
  - Party servers contain arrays of parties which contain the party's data (Users connected, text chat, voice chat, and play mode)
  - A party server can have up to x parties before a new server is required. (Ideally new servers would be added or removed depending on our network load)
  
- In-Game Server (UNET)
  - Handles logic for in-game and is ran by an authoritative server in a specific network's region.

- Playfab backend
  - Contains backend data for user information
  - Handles friends lists
