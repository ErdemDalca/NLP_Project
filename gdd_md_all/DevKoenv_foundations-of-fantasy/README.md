# Foundations Of Fantasy

## Title: `Foundations of Fantasy (FOF)`

## Genre: `Open-World Sandbox RPG`

## Setting: `Medieval Fantasy World`

## Core Features:

- **Dynamic NPCs with AI Personalities:**
    - Each NPC will have a unique AI-driven personality, allowing them to make decisions, form relationships, build structures, and evolve within the game world.
    - NPCs can interact with each other, form alliances, create families, and build their own settlements, empires, or guilds.
    - NPCs will have memories and emotions, influencing their interactions and decisions.

- **Living World:**
    - The game world will be fully dynamic, with NPCs able to modify the environment by constructing buildings, roads, farms, and even entire cities.
    - The world will evolve over time based on NPC actions, creating a truly living and breathing environment.
    - No player intervention is needed; NPCs will organically develop the world.

- **Quests and Storylines:**
    - NPCs will be capable of generating unique, procedurally generated quests based on their needs, desires, and life situations.
    - Quests can range from simple tasks like gathering resources to complex narratives involving politics, war, or family matters.
    - Quests will evolve and change depending on the player’s actions or inactions and the dynamic world state.

- **Reproduction and Population Control:**
    - NPCs can form families, reproduce, and pass on traits, skills, and even memories to their offspring.
    - The population will be self-sustaining, with new NPCs born as older ones die, ensuring the world remains populated.
    - A population threshold will be set to maintain balance, with new NPCs spawned only when the population drops below a certain level.

## Technical Challenges and Considerations

- **NPC AI Development:**
    - **AI Framework:** A robust AI framework is needed to support complex behaviors like decision-making, memory retention, and emotional states. Consider using behavior trees, GOAP, or other AI libraries.
    - **Procedural Content Generation:** NPCs will need to generate content (like quests and dialogue) dynamically. This involves procedural generation techniques, potentially combined with AI-driven narrative systems.

- **World Building and Modification:**
    - **Voxel-Based Terrain:** A voxel-based terrain system will allow NPCs to modify the environment at a granular level, building or destroying structures as needed.
    - **Procedural Generation:** Cities, buildings, and other structures could be procedurally generated based on NPC needs and the surrounding environment.
    - **Resource Management:** NPCs will need to gather and manage resources to build and sustain their structures. A simulation of a basic economy (e.g., supply and demand) could be implemented to govern resource distribution.

- **Game Engine and Programming Language:**
    - **Game Engine:** The game will be developed using libGDX, a powerful and flexible game framework that supports both 2D and 3D game development.
    - **Programming Language:** Kotlin will be used to develop the game, leveraging its modern features and full compatibility with Java, which is natively supported by libGDX.

- **Scalability and Population Management:**
    - **Population Dynamics:** A system to handle NPC birth, death, and reproduction will be needed to maintain a balanced population. This could involve simple rules governing NPC relationships and genetic algorithms.
    - **LOD (Level of Detail):** Implement a Level of Detail system for NPCs and world interactions to manage the processing load efficiently, simulating only the most relevant entities in detail.

- **Quests and Narrative Design:**
    - **Quest Generation:** A system where quests are generated based on NPC goals, needs, and the state of the world will be implemented. Quests might involve interactions with other NPCs, exploration, or resource gathering.
    - **Dynamic Narrative:** A dynamic narrative engine will integrate NPC-driven quests into a larger, evolving story. The player’s actions will influence the narrative direction.

## Development Plan

- **Phase 1: Research and Planning**
    - Conduct research on libGDX and relevant AI frameworks.
    - Finalize the game design document (GDD) detailing all core features, world lore, and mechanics.
    - Set up the initial project structure in Kotlin and integrate libGDX.

- **Phase 2: World Building and Saving**
    - Develop the basic world structure and terrain using libGDX.
    - Implement a system for saving and loading the game world.
    - Create a small, static world where initial interactions can take place.

- **Phase 3: Player Entity and World Interaction**
    - Develop the player entity with basic movement and interaction capabilities.
    - Implement basic world interaction mechanics, such as gathering resources and building structures.

- **Phase 4: Monster AI Development**
    - Introduce basic monster entities with simple AI behaviors.
    - Implement combat mechanics, allowing the player to interact with monsters.
    - Develop systems for monster spawning and behavior.

- **Phase 5: Advanced NPC AI Development**
    - Develop advanced AI systems for NPC decision-making, memory, and emotions.
    - Implement NPC interactions, allowing them to build, form relationships, and evolve within the game world.

- **Phase 6: Quest System and Narrative**
    - Implement the quest generation system, allowing NPCs to create and assign quests based on their needs.
    - Develop the dynamic narrative engine to integrate quests into a cohesive storyline.

- **Phase 7: Testing and Iteration**
    - Playtest the game extensively to identify and fix bugs, optimize performance, and refine gameplay mechanics.
    - Introduce NPC reproduction and population management systems.

- **Phase 8: Expansion and Polish**
    - Expand the world with more diverse environments, NPC types, and structures.
    - Add more complex AI behaviors, quests, and storylines.
    - Polish the game, improving graphics, sound, and user interface.

## Long-Term Vision

After the initial release, you can expand the game by adding new features such as:

- **Monsters and Combat:** Introduce more complex monsters and combat mechanics, allowing NPCs to form militias, defend their cities, and go on monster-hunting quests.
- **Multiplayer Mode:** Allow multiple players to interact with the NPC-driven world, possibly in a cooperative or competitive manner.
- **Magic and Fantasy Elements:** Introduce magic systems, fantasy races, and other elements to enrich the world and NPC interactions.

## Contributing

This `README.md` provides a comprehensive overview of your "Foundations of Fantasy" project, tailored to your use of Kotlin and libGDX, and should be a useful guide for contributors and future development.

## Platforms

- `core`: Main module with the application logic shared by all platforms.
- `lwjgl3`: Primary desktop platform using LWJGL3.
- `server`: A separate application without access to the `core` module.
- `shared`: A common module shared by `core` and `server` platforms.

## Gradle

This project uses [Gradle](https://gradle.org/) to manage dependencies.
The Gradle wrapper was included, so you can run Gradle tasks using `gradlew.bat` or `./gradlew` commands.
Useful Gradle tasks and flags:

- `--continue`: when using this flag, errors will not stop the tasks from running.
- `--daemon`: thanks to this flag, Gradle daemon will be used to run chosen tasks.
- `--offline`: when using this flag, cached dependency archives will be used.
- `--refresh-dependencies`: this flag forces validation of all dependencies. Useful for snapshot versions.
- `build`: builds sources and archives of every project.
- `cleanEclipse`: removes Eclipse project data.
- `cleanIdea`: removes IntelliJ project data.
- `clean`: removes `build` folders, which store compiled classes and built archives.
- `eclipse`: generates Eclipse project data.
- `idea`: generates IntelliJ project data.
- `lwjgl3:jar`: builds application's runnable jar, which can be found at `lwjgl3/build/libs`.
- `lwjgl3:run`: starts the application.
- `server:run`: runs the server application.
- `test`: runs unit tests (if any).

Note that most tasks that are not specific to a single project can be run with `name:` prefix, where the `name` should be replaced with the ID of a specific project.
For example, `core:clean` removes `build` folder only from the `core` project.
