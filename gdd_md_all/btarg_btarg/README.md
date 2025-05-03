# btarg
<img align='left' height='75' src='https://github.com/btarg/Origami/blob/master/crane.png?raw=true' style='padding-right: 10px;' />

My favourite programming language is C#, and I mostly focus on game development and modding. I code in my spare time to learn as much as I can and to create the best solutions to problems I have with existing software and games.

I also own and operate [the 21st portfolio](https://21stportfolio.com), a student-run literature blog, and I occasionally write poetry and reviews for the site.

## Projects

### [Project Requiem (WIP - current)](https://github.com/btarg/third-person-controller)
![Godot Engine](https://img.shields.io/badge/GODOT-%23FFFFFF.svg?style=for-the-badge&logo=godot-engine)

Project Requiem is a work-in-progress turn-based RPG made in [**Godot 4**](https://godotengine.org) using **GDScript**. It is heavily story-driven and features an expansive design document with over 6,000 words outlining the game’s intricate narrative and mechanics. [You can explore the design doc here](https://docs.google.com/document/d/1ciNLXNb76iGfoPWgEIhHHFKyTaYyUXYv_RmkQ1yvwhU/edit?usp=sharing).

![Design document screenshot](https://i.imgur.com/P0jkkxS.png)


#### Implementing the gameplay
In this project, I make heavy use of **state machines** to manage the gameplay flow. For example:

- **Exploration vs. Battle**: State machines manage whether the player is in exploration mode or engaged in battle.
- **Character Battle States**: During battles, each character has a state machine that determines whether they are attacking, defending, waiting, etc.

These states would then be responsible for updating the appropriate gameplay logic: for example, the `ExplorationState` updates the third-person player controller, whilst the `BattleState` updates a top-down player controller. These states are **Nodes within the scene,** that are children of the State Machine itself.

![An example of a simple state in my state machine system](https://i.imgur.com/ZrxpdWZ.png)

While **GDScript** was a new language for me, my previous experience with **C# in Unity** and **AngelScript in Unreal Engine** allowed me to quickly adapt and implement gameplay systems effectively.

The design of my data structures and gameplay flow is informed by previous attempts at creating similar RPG mechanics in **Unity** and **Unreal Engine**, as well as working with others (especially the friendly people in the official [Godot Discord server](https://discord.gg/bdcfAYM4W9)) to collect feedback and improve the visuals and gameplay accordingly.

![Early indev screenshot of the player in the "exploration state"](https://i.imgur.com/KIvQsmP.png)

> Disclaimer

As of late 2024, I am yet to source art assets. The code portion of this project is simply a way for me to sharpen my skills in Godot, whereas the [**Game Design Document**](https://docs.google.com/document/d/1ciNLXNb76iGfoPWgEIhHHFKyTaYyUXYv_RmkQ1yvwhU/edit?usp=sharing) has had far more time put into it. I am continuing to write the game's story, workshopping plot and characters with members of my student group at university.

### [ByteReserve](https://github.com/btarg/AWS-Upload) (halted for now)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

![Screenshot of main page](https://i.imgur.com/Qd8ajwo.png)
![Screenshot of pricing page](https://i.imgur.com/0WmyJWZ.png)



ByteReserve is a pay-as-you-go, end-to-end encrypted file upload service (similar to **DropBox**, for example). The current code in the repo does not work, as I stopped developing it mid-rewrite.
ByteReserve is my first large-scale full-stack **JavaScript** application.

It uses [Node.js](https://nodejs.org/) on the backend, and [Vue](https://vuejs.org/) with [Tailwind](https://tailwindcss.com/) on the frontend. This was my first time making a dynamic and responsible frontend user experience, but I was quickly able to adapt to using Vue from previous experience writing basic HTML pages for other projects.

The site would encrypt all user-uploaded files entirely within the browser, before uploading to [BackBlaze B2.](https://backblaze.com) **This ensured strict user privacy, and the storage was incredibly cheap.** For further increased privacy, my **PostgreSQL** database would not store any sensitive information about users or files.

Users would be charged hourly based on "credits" that they could top up, rather than monthly out of real money on a card. This would ensure that people would not be charged when forgetting to renew a subscription: an annoyance I have with many other alternative services like Google Drive which I believe to be solved by ByteReserve.

> Why I stopped working on this

Currently, the project's development is halted. The credits and billing systems are not yet implemented. At the moment, this project is **too large in scope** for me to test and deploy properly by myself. Also, a single point of failure in a privacy-focused application like this could lead to compromised user privacy (e.g. if my accounts are hacked, then the site could go down as there is no corporate entity backing it.) I made good progress in the time I spent on the application.

### [Origami](https://github.com/btarg/origami) (Discontinued)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Gradle](https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white)

Origami is a Minecraft server plugin for the [Paper](https://papermc.org/) platform, which allows for server owners to create more a customised experience closer to that of modded Minecraft, regardless of the players' clients.

I used many tricks and hacks present in vanilla Minecraft code to create custom blocks and items, implementing a system which allowed the server owner to write simple **YAML files** to define custom properties for each item or block.

The plugin also featured [extensive, easy-to-follow documentation](https://btarg.gitbook.io/origami-docs), marking my first time writing proper docs for a programming project. I believe they turned out helpful and well-organised.

> Why I stopped working on this

Other, more [feature-complete alternatives](https://modrinth.com/mod/polymer) exist now for server-side modding, but I learned a lot about backend and server development for games while working on Origami.


### [CraftGPT](https://github.com/btarg/CraftGPT) (Proof of concept)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Gradle](https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white)

CraftGPT was an experiment with [Langchain4J](https://github.com/langchain4j/langchain4j) and PaperMC. The plugin allows a player on a Minecraft server to speak to a **GPT-powered LLM**, which could execute commands in the game. For instance, the player could ask for "something useful for mining," and be given a pickaxe by the LLM.

The plugin also **observed more general information about the players **in the server: for instance, if that player had asked more generally for "something useful," and they were low on health, they might recieve food or a healing potion to restore it.

> Why I stopped working on this

Other, better alternatives for this idea exist, however I was **one of the first to implement** this particular idea in code, and I learned a lot about implementing **"Tools"** for large language models like **GPT-4.**

### [Unity Ink game](https://github.com/btarg/UnityInkGame)
![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white)![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white)

This unnamed 3D first-person exploration game was heavily dialogue-centric. It featured a **Quake level importer** so I could make levels with [Trenchbroom](https://trenchbroom.github.io/), which while adapted from existing open-source code, was highly customised to allow me to place **Invisible walls, triggers and Unity prefabs** within the Trenchbroom editor.

This was also my first experience **creating UI for a game,** which I believe turned out very well: the game features an Undertale-inspired and DOS-like main menu, pause menu, and functioning dialogue boxes using the [Ink](https://www.inklestudios.com/ink/) scripting language. The UI looked great and was easy to navigate with multiple control methods.

> Why I stopped working on this

I abandoned work on this game after I decided that the gameplay was lacking. I had not created a Game Design Document for this project like I later did for **Project Requiem,** which severely hindered my ability to craft a fun experience. I have used this as a valuable lesson for projects since, and have been creating more **detailed documentation for both systems and narratives** in current projects.


### [Twitch Vs Minecraft](https://github.com/btarg/TwitchVsMinecraft2)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Gradle](https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white)

Twitch vs Minecraft is a Minecraft Forge mod which allows a player's Twitch chat to **directly interact with their game** through commands.

It was heavily inspired by other existing projects like [CrowdControl](https://crowdcontrol.live/), but offered the easiest setup out of all available livestream interactivity mods, with pre-defined commands that I programmed myself.

Twitch Vs Minecraft was the project I used for learning Java, and served as a testbed for my Java development skills for a few years while I maintained it. These days there are again more feature-complete and up-to-date alternatives available, but I believe that my mod was the best in the category in terms of user experience (especially its unparalleled ease of use) while I actively worked on it.

## Skills
[![My Skills](https://skillicons.dev/icons?i=vscode,github,java,cs,unity,godot,unreal,python,idea,discord,bots,linux,nginx,gcp,aws,ps,md,netlify,postgresql,javascript,typescript)](https://skillicons.dev)

## Contact
You can contact me on [LinkedIn](https://www.linkedin.com/in/benjamin-targett-1298ab29a/) if you are interested in hiring a developer with any of these skills!
