# Game Design Document (GDD)

### Table of Contents

- [Game Overview](#game-overview)
- [Story and Narrative](#story-and-narrative)
- [Gameplay and Mechanics](#gameplay-and-mechanics)
- [Levels and World Design](#levels-and-world-design)
- [Art Style and Audio](#art-style-and-audio)
- [User Interface (UI)](<#user-interface-(UI)>)
- [Technology and Tools](#technology-and-tools)
- [Team Communication, Timelines and Task Assignment](#team-communication,-timelines-and-task-assignment)
- [Possible Challenges](#possible-challenges)

### Game Overview

![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/Start.gif)

#### Core Concept

The Library of Lost Souls is a 3D, eerie adventure game where you play as John Sinclair, a university student who stumbles upon a hidden section of the campus library. This forgotten library is filled with books that bear the names of people who mysteriously vanished, each one detailing their lost fate.

As the player, you must navigate the dark and unsettling corridors, uncovering secrets and solving intricate puzzles to escape the library’s grip. But beware—the Librarian watches your every move, waiting for the moment you falter. If you fail to escape, John will become the library’s next lost soul, his fate sealed in a book that will forever bear his name.

#### Related Genre(s)

- _Psychological Thriller_: The game creates tension and unease through atmosphere and story rather than traditional horror mechanics. The library is designed so as to provide an eerie environment making it thrilling for the player.
- _Adventure_: The game focuses on exploration, discovery, and unraveling the mysteries of the library and pursuing the librarian makes it further adventurous and exciting for the player.
- _Mystery/Puzzle_: Solving simple puzzles to uncover clues and piece together the story of the library's previous victims are central to the gameplay.

##### Similar Games

- Limbo (atmosphere and tension)
- Inside (exploration and dark themes)
- The Stanley Parable (narrative-driven)

##### What makes our game different?

- _Living Library Concept_: The library itself is an unpredictable environment that actively resists the player's attempts to escape.
- _Concise Experience_: Designed for a 10 minute playtime, delivering a powerful, focused narrative in a short session.

#### Target Audience

The game is particularly suited for fans of minimalist, atmospheric games and those who enjoy stories that challenge their perception of reality. Players who prefer games like Oxenfree, Limbo, and Inside, who appreciate subtle horror, mysterious narratives, and exploration will find The Library of Lost Souls appealing. The game is designed to be accessible, with straightforward mechanics and a focus on narrative. It targets a mature audience (ages 16 and up) who appreciate suspense, mystery, and games that provoke thought rather than rely on jump scares or gore.

#### Unique Selling Points (USPs)

- _Atmospheric and Eerie Setting:_ The game creates a haunting and mysterious atmosphere, drawing players into its unsettling world without relying on traditional horror tropes.
- _Narrative-Driven Gameplay:_ The unique storyline, where John discovers his own fate within the library, offers a compelling mystery that drives the gameplay.
- _Minimalist Horror:_ The game evokes fear through subtlety, focusing on psychological tension and environmental storytelling.
- _Concise, Impactful Experience:_ Designed to be completed in a single session (A 10 minute gameplay) , offering a memorable experience in a short timeframe.

### Story and Narrative

#### Backstory

John Sinclair, a university student, discovers a strange, hidden door in the campus library while researching late at night. Behind the door is a forgotten section of the library filled with dusty books, each bearing the name of a missing person. Realizing something is terribly wrong, John begins to search through other books and notices eerie similarities in the stories. Each person disappeared without a trace after uncovering the library's dark secrets.

As John delves deeper into the library's mysteries, he finds notes left by a previous victim, hinting at the existence of the Librarian, a malevolent figure who traps those who discover the library's hidden truths. With time running out and the library's influence growing stronger, John knows he must confront the Librarian and find a way to escape. The final confrontation forces John to perform a ritual to escape the library by forming a symbol that is made up by selecting 3 shapes.

In the end, John manages to escape the library, but the experience leaves him deeply changed. The final moments suggest that the library still exists, waiting for its next victim, and that John's escape may only be temporary…If the player fails to overcome the challenges, the player would also become a soul trapped within a book.

#### Characters

1. John Sinclair (Player)

<p align="center">
  <img src="Images/john.png" width="300">
</p>

- _Background:_ A diligent university student majoring in psychology. John has always been curious and has a deep love for books, often spending late nights in the library but one night his life takes a dark turn when he discovers the forbidden section of the library that houses books documenting the lives of people who mysteriously disappeared.
- _Motivation_: John’s motivation is to uncover the truth behind the library's dark secrets and escape before becoming its next victim. John's determination is fueled by the realization that his life is at stake, as well as a strong sense of justice for those who have disappeared before him.
- _Personality:_ Curious, intelligent, and resourceful, but also cautious. As the story progresses, John’s initial suspicion turns into fear, which he must overcome to survive. He is very observant, often thinking through situations carefully before acting.
- _Appearance_: John is in his early 20s. He wears casual attire: jeans and a shirt. All the characters will be minimalist to reflect the eerie and surreal atmosphere of the game.

2. The Librarian (Villain)

<p align="center">
  <img src="Images/librarian.png" width="300">
</p>

- _Background_: The Librarian is a mysterious and evil figure who serves as the guardian of the hidden section of the library. Once a student like John, the Librarian was trapped by the library's curse many years ago and has since become its unwilling gatekeeper, responsible for ensuring that no one who discovers the library's secrets escapes.
- _Motivation:_ The librarian traps anyone who uncovers the library's dark secrets and thereby feeds the library's hunger for souls. The Librarian is bound to the library and cannot leave, but finds solace in ensuring that others share the same fate.
- _Personality:_ Cold, calculating, and mysterious. The Librarian shows no remorse for those who fall into the library's trap, seeing them as necessary sacrifices to keep the library’s curse alive. The Librarian is manipulative, often speaking in riddles and half-truths to confuse and demoralize John.
- _Appearance:_ The librarian would be a male that is also monotone to reflect his eerie and evil figure.

3. Previous Victim/Souls

- _Background:_ Former students who were trapped by the library many years before John. These characters left behind cryptic notes and warnings scattered throughout the hidden section of the library, hoping that someone would find them and escape the fate they couldn’t avoid.
- _Motivation:_ Their goal is to help future victims avoid the same fate by providing clues about the library and the Librarian. Their notes and hints play a crucial role in guiding John through the library’s maze of secrets.
- _Personality:_ They were once hopeful but became increasingly desperate as they realized their doom was inevitable. Their tone fluctuates between helpful and despairing, reflecting the emotional toll of being trapped.
- _Appearance:_ The souls do not interact directly. They interact with clues.

#### Relationship between the characters

- _John and The Librarian:_ The central conflict of the game revolves around John’s struggle to outwit the Librarian and escape the library. The Librarian views John as another inevitable victim, while John sees the Librarian as the key to his survival.
- _John and the Previous Victims:_ Although they never meet, the previous victims' notes are John's only ally in the library, providing crucial information that helps him piece together the truth and find a way to escape.

### Gameplay and Mechanics

#### Player Perspective

- The player perspective will be far third-person perspective
- Using a static camera
<p align="Left">
  <img src="Images/GameWorld.png" width="500">
</p>

#### Controls

- Movement controls:
  - The usual 'WASD' keys to move front, back, left and right
- Object Interaction controls:
  - ‘F’ key to inspect books
  - 'E' key to interact with objects (doors and piano)
  - ‘Mouse Click’ to choose the piano notes (during the 2nd scenario) and to choose the correct symbols (during the 3rd scenario)
  <p align="Left">
    <img src="Images/Controls.png" width="500">
  </p>

#### Progression

- Stage 1: Discovery
  - The discovery of the hidden library and the core mysteries behind it.
  - Challenges: The introduction of the various gameplays that are provided in the game.
    - Movement controls

    ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/movement.gif)

    - Book Inspection

    ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/BookInteraction.gif)

- Stage 2: Investigation

  - The encounter with the Librarian and the search for clues left by the previous victim to trap the Librarian and to free the lost souls.
  - Challenges: Complete the piano note music challenge

    - In this stage, a strange piano lies around in the room and the player has to press the 'E' key to interact and find out what it is.
    - Player should solve a puzzle(A piano note challenge) when interacted with the piano in order for the door to unlock to move to the next stage.

      ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/PianoInteraction.gif)

    - For those who run out of time, this is game over for them.


- Stage 3: Escape
  - The final act of this adventure is to esacape the dark and eerie library by guesing the correct symbol.
  - Challenges: After the piano music note challenge, player is moved on to the next level where he should find and match 3 shapes to form up a symbol. Three of these shapes would make the Symbol needed to perform a ritual at the altar and thereby escape the library. The clues to form up the symbol is given in stage 1. 
  - A time limit would be imposed for this task. Player should match them before the time runs out to escape or else it is game over.

- Win or Lose
  - If the player manages to complete all the tasks within the given time, Stage 3 will transition to the end credit scene.

![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/EndCredit.gif)

  - If the player fails to complete any given tasks within the given time frame. The current scene will transition to the game over scene.

 <p align="Left">
          <img src="Images/GameOver.png" width="620">
 </p>
    
#### Gameplay Mechanics

- Exploration and Discovery
  - Players are given the ability to move in a 3d-axis where they can interact with the one of the core elements of this game which are books containing the forgotten souls
  - Mechanics that are relevant:
    - Movement controls
    - Object interaction
- Puzzle Solving
  - Players have to complete some puzzles in order to progress throughout the game and ultimately complete it
  - This is tightly related to the exploration and discovery gameplay as players need to explore and collect the clues for the puzzles
  - Mechanics that are relevant:
    - Book Inspection
    - Clue Deduction
- Time Pressure

  - The mechanic of time limit poses a constant threat to players emphasizing the element of tension and thrill of impending danger
  - This mechanic works side by side along with the puzzles to create the main gameplay loops of this game that mainly involves deduction and quick thinking
  - Mechanics that are relevant: Time Limit

  ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/timeCounter.gif)

### Levels and World Design

- The game world would be in 3D with a dark eerie monotone theme.
- There are multiple stages in the game, followed by a single screen to point out the stages.
- In the gameplay, the player moves from room to room for each stage to navigate through the game world.
- Since the world map is not that big, we don’t use either a map or a minimap.
- We use a door to navigate to each level by pressing the "E" key.

 ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/Leave.gif)
 ![](https://github.com/feit-comp30019/2024s2-project-2-spectro-studio/blob/main/Images/Enter.gif)

#### Objects

- Book as a clue to finish the game.
- Book shelves as a placeholder for the book.
- The soul acts as the one who is trapped in the book.
- Piano as a clue to proceed to the next stage.

<p>
  <img src="Images/Book.png" width="250" align="Left">
  <img src="Images/Paper.png" width="320" align="Center">
</p>

#### Physics

- Character Movement:
  - The player’s character moves on a 3D plane with predefined speeds.
- Object Movement:
  - Books and items within the game world follow simple physics when interacting with the player.
- Interaction with the environment:
  - Collision: Physics handles collision detection to make sure that the player’s character doesn’t walk through walls or objects.
  - A keyboard will pop up when player interacts with the piano.

### Art Style and Audio:

- Overall Aesthetic:

  - Dark and Monotone: The game embraces a dark and monotone visual aesthetic, emphasizing atmosphere and mood over intricate detail.
  - Minimalism: A minimalist approach is taken, with characters and objects rendered as simple silhouettes, and environments kept intentionally sparse to evoke a sense of mystery and tension.
  - Inspiration: The art style is inspired by the game Limbo, known for its use of contrast, simplicity, and atmospheric depth.
  <p align="center">
    <img src="Images/limbo.png" width="500">
  </p>
  <p align="center">
    <img src="Images/inside.png" width="500">
  </p>
  <p align="center">
    <img src="Images/little nightmare.png" width="500">
  </p>

- Shapes:
  - Geometric Simplicity: Shapes are kept simple and angular, using basic geometric forms to create characters, objects, and environmental features.
  - Silhouetted Characters: All characters are represented as silhouettes, enhancing the sense of mystery and focus on the overall shape rather than details.
  - Sharp Edges and Angular Forms: Objects and environmental elements often feature sharp edges and angular forms, contributing to the sense of danger and unease within the game world.
- Textures:
  - Grainy and Rough: Textures are minimal but grainy or rough to evoke a sense of decay and to complement the dark atmosphere.
  - Flat with Lighting Depth: While textures themselves are flat, lighting is used to create depth and dimensionality, ensuring that even simple forms have a presence in the environment.
- Lighting:
  - High Contrast Lighting: Lighting plays a crucial role in defining the visual tone. High contrast between light and shadow is used to create tension and highlight important gameplay elements.
  - Flickering Lights: Often used to cast dramatic lighting that enhance the eerie atmosphere of the game.
- Concept Art & References:
  - Limbo: The game draws heavily from the aesthetic of Limbo, particularly its use of silhouettes, contrast, and minimalism.
  - Inside and Little Nightmares: Lighting and setting aesthetics
- Audio and Sound:
  - Dark and Atmospheric: The audio design will maintain the game's dark, monotone aesthetic while incorporating "soul sounds" and wind to create an eerie and otherworldly atmosphere. These sounds will evoke a sense of mystery and unease, enhancing the player's emotional connection to the game world.
  - Minimalistic and Subtle: Audio elements will be sparse, with the use of soul sounds providing a haunting backdrop. Silence will be used strategically, with soul sounds emerging at key moments to amplify the tension.

### User Interface(UI)

#### Start Screen

This screen displays the title of the game, "LOLS: The Library of Lost Souls," and a play button at the center. The background shows a dimly lit library with bookshelves filled with books, emphasizing the game's eerie and mysterious atmosphere. There is a menu icon at the top right corner for game options such as settings and volume.

<p align="center">
    <img src="Images/Start.png" width="500">
</p>

#### During Gameplay Screen

This screen shows the player character standing in the library, with books that has the names of the vanished lying around the shelves. The UI elements include time counter in the bottom left (for some stages) and a menu icon in the top right. This screen represents the main gameplay, where the player navigates the library.

<p align="center">
    <img src="Images/World.png" width="500">
</p>

#### Pause Screen

This screen is displayed when the player presses "Esc" button. The background remains consistent with the library theme. The "Resume" option is hovered upon suggesting that players can resume the game after pausinga and the "Restart" button should be pressed when player needs to start from the first stage. The "Exit" button is to quit the game. The pause screen allows players to customize their gameplay experience.

<p align="center">
    <img src="Images/Pause.png" width="500">
</p>

#### Controls Screen

This screen explains the game's controls. It displays an illustration of a keyboard with specific keys highlighted:

- _“W(Climb up), A(Move left), S(Climb down), D(Move right)”_ - for movement.
- _“F”_ - to read books.
- _“E”_ - to interact with objects.
- _“Esc”_ - to pause or exit the game.
  The background remains consistent with the library setting, providing a clear and informative guide for players on how to interact with the game.

<p align="center">
    <img src="Images/Controls.png" width="500">
</p>

These UIs are designed to be cohesive and monotone, with the dark, mysterious library setting consistently reflected across all screens, supporting the game's eerie atmosphere.

### Technology and Tools

- Github for the version control among the members
- Unity as the main development tool for the game
- VS Code as a framework to edit the game elements' scripts
- Trello for task assignments

### Team Communication, Timelines and Task Assignment

- Whatsapp is used as the main communication channel
- Trello board for timeline viewing and task assignment (https://trello.com/b/qKgKiRgA/lols-project)

### Possible Challenges

#### Maintaining an eerie game atmosphere

- _Challenge:_ Ensuring that the game maintains a constant eerie tone without traditional horror effects like jumpscares, zombies etc.

- _Mitigation:_ We should especially focus on sound effects and lighting. Regular playtesting would be important as we could make adjustments on the go so as to support the consistent eerie environment.

#### Time constraints

- _Challenge:_ Designing the game so as to balance the scope of it with the time available for development. Ensuring that all key features are implemented without rushing towards the end.

- _Mitigation:_ Prioritize essential features and mechanics early in the development process. Use agile development practices to ensure steady progress and regularly assess the project timeline.

#### Technical Implementation in Unity (WebGL Build)

- _Challenge:_ Developing the game to run smoothly in a WebGL environment, which may have performance limitations compared to standalone builds.
- _Mitigation:_ Optimize code use for WebGL from the start, keeping an eye on performance. Test the WebGL build regularly to identify and fix any performance issues early on.

#### Ensuring a well balanced game in a Short Playtime

- _Challenge:_ Telling a compelling story within a short gameplay duration(10 minutes), ensuring that players are both engaged and able to understand the plot and also is able to finish the game in the given short time.

- _Mitigation:_ Focus on concise storytelling, using environmental clues and key interactions to convey the narrative. Streamline the story to fit the gameplay duration without going deep.

#### Managing Team Collaboration

- _Challenge:_ Coordinating work among team members, ensuring consistent communication, and managing different skill levels and availability.

- _Mitigation:_ Establish clear roles and responsibilities early on. Using collaboration tools like GitHub for version control and project management tools like Trello to track progress and tasks.
