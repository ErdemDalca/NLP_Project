# Game Design Document

## Table of Contents

1. [Game Overview](#game-overview)
    - [Game Concept](#game-concept)
    - [Genre](#genre)
    - [Platform](#platform)
    - [Target Audience](#target-audience)
2. [Gameplay Mechanics](#gameplay-mechanics)
    - [Core Mechanics](#core-mechanics)
    - [Game Flow](#game-flow)
    - [Player Actions](#player-actions)
    - [Controls](#controls)
3. [Story and Narrative](#story-and-narrative)
    - [Story Summary](#story-summary)
    - [Characters](#characters)
    - [World and Setting](#world-and-setting)
4. [Levels and Environment](#levels-and-environment)
    - [Level Design](#level-design)
    - [Environment Art](#environment-art)
5. [Art and Visual Style](#art-and-visual-style)
    - [Visual Theme](#visual-theme)
    - [Character Design](#character-design)
    - [User Interface (UI) Design](#user-interface-ui-design)
6. [Audio and Music](#audio-and-music)
    - [Sound Design](#sound-design)
    - [Music Style](#music-style)
    - [Voice Acting](#voice-acting)
7. [Technical Requirements](#technical-requirements)
    - [Target Platform Specifications](#target-platform-specifications)
    - [Game Engine and Tools](#game-engine-and-tools)
    - [Performance Considerations](#performance-considerations)
8. [Monetization Strategy](#monetization-strategy)
    - [Pricing Model](#pricing-model)
    - [In-Game Purchases](#in-game-purchases)
    - [Advertising](#advertising)
9. [Appendices](#appendices)
    - [Concept Art](#concept-art)
    - [Additional Documents](#additional-documents)

---

## Game Overview

### Game Concept

The game is a simple incremental (idle) crafting and clicker game where players begin by manually gathering basic resources like Berries, Fibers, and Rocks. Utilizing a 2×2 crafting grid, players craft basic tools and structures, progressing to mining and smelting ores. As players advance, they unlock grid expansions, allowing more complex recipes and automation structures. The game offers a satisfying progression from manual foraging to automated resource collection within a small, manageable scope.

### Genre

- **Idle/Incremental Game**
- **Crafting and Resource Management**
- **Clicker Game**

### Platform

- **Primary**: Web Browser (HTML5)
- **Secondary**: Mobile Devices (iOS and Android)
- **Tertiary**: PC (Windows, macOS, Linux)

### Target Audience

- **Age Range**: 10 and above
- **Gamer Type**: Casual gamers, fans of idle and crafting games
- **Interests**: Resource management, crafting mechanics, incremental progression, simple and accessible gameplay

---

## Gameplay Mechanics

### Core Mechanics

- **Resource Gathering**: Players collect resources manually by clicking on objects like bushes and rocks.
- **Crafting System**: A 2×2 grid used to combine resources into tools and structures; expands to 3×3 as the game progresses.
- **Tool Upgrades**: Crafting better tools increases resource yields and unlocks new resource types.
- **Automation**: Players build structures that automate resource collection, embodying the idle game aspect.
- **Progression Loop**: Gather resources → Craft tools → Unlock new resources and recipes → Expand crafting grid → Automate processes.

### Game Flow

1. **Start**: Manual gathering of basic resources.
2. **Early Game**: Craft initial tools using the 2×2 grid to improve resource collection.
3. **Mid-Game**: Expand crafting grid, mine ores, smelt metals, and craft advanced tools.
4. **Late Game**: Build automation structures to passively gather resources, enhancing the idle aspect.
5. **Transition**: Potential to expand into more complex systems if the scope is increased.

### Player Actions

- **Clicking**: Manually collect resources from bushes, trees, rocks, and ores.
- **Crafting**: Combine resources in the crafting grid to create tools and structures.
- **Mining and Chopping**: Use tools to gather resources from larger sources.
- **Smelting**: Process ores into ingots using the Furnace.
- **Building**: Construct automation structures for passive resource generation.
- **Upgrading**: Enhance tools and structures for better efficiency.

### Controls

- **Mouse Input** (Web/PC):
    - Left-click to gather resources and navigate menus.
    - Drag-and-drop items into the crafting grid.
- **Touch Input** (Mobile Devices):
    - Tap to collect resources and select menu options.
    - Drag-and-drop with a touch interface for crafting.
- **Accessibility**:
    - Simple and intuitive controls suitable for all ages.
    - Options for sound, music, and notifications.

---

## Story and Narrative

### Story Summary

In a serene and untamed wilderness, the player assumes the role of a resourceful pioneer aiming to harness nature's bounty. Starting with nothing but their hands, they gradually craft tools, explore the environment, and build structures. The narrative focuses on the journey from survival to mastery over the natural world, emphasizing self-sufficiency and progression.

### Characters

- **Player Character**:
    - An anonymous pioneer representing the player.
    - Embodies exploration, innovation, and growth.
- **Non-Player Characters (Optional)**:
    - Wildlife that can appear as part of the environment.
    - No direct interactions to keep gameplay focused on mechanics.

### World and Setting

- **Environment**:
    - A lush wilderness with forests, rocks, and mineral veins.
    - Simplified representation focusing on resource nodes.
- **Atmosphere**:
    - Calm and relaxing, encouraging casual play.
- **Narrative Elements**:
    - Environmental messages or tips guiding the player.
    - Achievements or milestones marking progression.

---

## Levels and Environment

### Level Design

- **World Structure**:
    - Abstract representation of a natural environment.
    - No traditional levels; progression is through resource tiers and crafting.
- **Resource Nodes**:
    - **Bushes**: Provide Berries and Fibers.
    - **Trees**: Small and medium trees yield Wood.
    - **Rocks**: Yield Rocks and Stone.
    - **Ore Veins**: Copper and Iron ores accessible with better tools.
- **Progression**:
    - New resource nodes unlock as the player crafts better tools.

### Environment Art

- **Visual Indicators**:
    - Distinctive icons or sprites for each resource type.
    - Visual upgrades to resource nodes as the player progresses.
- **Animations**:
    - Subtle animations when collecting resources (e.g., shaking bushes).
- **Layout**:
    - Simple and intuitive interface where resources are easily accessible.

---

## Art and Visual Style

### Visual Theme

- **Style**:
    - Minimalistic and clean graphics.
    - Bright and soft color palette for a calming effect.
- **Inspiration**:
    - Games like "Forager" and "Clicker Heroes" for simplicity.
- **Consistency**:
    - Uniform art style across all assets for cohesiveness.

### Character Design

- **Player Representation**:
    - Optional avatar or simply a cursor.
- **Resource Nodes**:
    - Stylized icons representing bushes, trees, rocks, and ores.
- **Tools and Items**:
    - Clear and distinguishable images for each tool and crafted item.

### User Interface (UI) Design

- **Layout**:
    - Main screen displays resource nodes and current inventory.
    - Crafting grid accessible via a dedicated button or always visible.
- **Crafting Grid**:
    - 2×2 grid expanding to 3×3 visually represented.
    - Drag-and-drop functionality for combining items.
- **Menus and HUD**:
    - Resource counters displayed prominently.
    - Tooltips provide information on resources and recipes.
- **Feedback**:
    - Visual cues for successful actions (e.g., resource collected).

---

## Audio and Music

### Sound Design

- **Resource Collection**:
    - Subtle sounds for collecting different resources (e.g., rustling for bushes, clinking for mining).
- **Crafting**:
    - Satisfying sound effects when crafting items or tools.
- **Ambient Sounds**:
    - Gentle environmental sounds to enhance immersion.

### Music Style

- **Background Music**:
    - Relaxing and loopable tracks.
    - Possibly dynamic music that evolves as the player progresses.
- **Genres**:
    - Ambient, light instrumental melodies.
- **Considerations**:
    - Music should not be distracting; focus on enhancing the experience.

### Voice Acting

- **Implementation**:
    - Likely minimal or none to maintain simplicity.
- **Alternatives**:
    - Use of sound effects or minimal vocal cues if necessary.

---

## Technical Requirements

### Target Platform Specifications

- **Web Browser**:
    - Compatibility with major browsers (Chrome, Firefox, Safari).
    - Optimized for HTML5 and JavaScript.
- **Mobile Devices**:
    - iOS 11.0 and above.
    - Android 6.0 (Marshmallow) and above.
    - Touchscreen support and responsive design.
- **PC**:
    - Windows 7 and above.
    - macOS 10.12 and above.
    - Linux distributions supporting necessary runtime environments.

### Game Engine and Tools

- **Game Engine**:
    - Unity Engine (with WebGL export) or
    - HTML5 with frameworks like Phaser or React.
- **Development Tools**:
    - Visual Studio Code or preferred IDE.
    - Graphic editors (Adobe Photoshop, Illustrator, or equivalent).
- **Version Control**:
    - Git for source code management.

### Performance Considerations

- **Optimization**:
    - Efficient code to ensure smooth performance on low-end devices.
    - Lazy loading of assets to reduce initial load times.
- **Compatibility**:
    - Responsive design for various screen sizes.
    - Touch and mouse input compatibility.
- **Testing**:
    - Regular testing on target devices and browsers.

---

## Monetization Strategy

### Pricing Model

- **Free-to-Play**:
    - The game is free to access and play in its entirety.

### In-Game Purchases

- **Optional Microtransactions**:
    - Cosmetic upgrades (e.g., themes, skins for tools).
    - Time savers or boosters that do not impact core progression significantly.
- **Fairness**:
    - Ensuring that all content is accessible without purchases.
    - Avoiding "pay-to-win" mechanics.

### Advertising

- **Implementation**:
    - Non-intrusive ads, such as banner ads in designated areas.
    - Optional rewarded ads for in-game bonuses.
- **User Experience**:
    - Maintaining a balance to not disrupt gameplay.

---

## Appendices

### Concept Art

*Include sketches, mock-ups, and visual references supporting the game's design.*

- **Resource Icons**:
    - Preliminary designs for Berries, Fibers, Rocks, etc.
- **Crafting Grid UI**:
    - Mock-up of the 2×2 and expanded 3×3 grid interfaces.
- **Tools and Structures**:
    - Visual concepts for pickaxes, axes, Furnace, and automation structures.

### Additional Documents

*Attach any other relevant documents, such as technical specs or design prototypes.*

- **Recipe List**:
    - Detailed spreadsheet of all crafting recipes.
- **Progression Flowchart**:
    - Visual representation of resource and crafting progression.
- **User Interface Wireframes**:
    - Detailed layouts of screens and menus.

---

**Note:** This design document outlines the foundational elements of the game based on the initial design notes. Adjustments and additions may be made as development progresses to enhance gameplay and user engagement.