# Game Design Document: Project Day Automate (Working Title)

**Version:** 0.1 (Project Day - Draft)
**Date:** 2023-10-27

## 1. Overview

* **Game Concept:** A minimalist orthographic top-down automation game inspired by Factorio/Shapez, built within a 6-hour game jam constraint. Players place miners on resource nodes, transport resources via belts, process them using simple machines, and deliver specific crafted items to a central Hub to unlock new technologies and progress.
* **Jam Goal:** To create a *playable prototype* demonstrating the core loop: resource extraction -> transport -> processing -> delivery -> unlock. Finishability over features.
* **Genre:** Automation, Simulation, Puzzle (Resource Chain Management).
* **Target Platform:** PC (Standalone).
* **Visual Style:** Utilizes the clean, low-poly "KayKit Resource Bits" assets for resources and items. Machines will be represented by extremely simple geometric shapes (cubes, boxes - potentially created quickly using Asset Forge or engine primitives) with clear UI icons overlaid to indicate function. Ground textures will be simple grids or solid colors with distinct patches for resource nodes.

## 2. Core Gameplay Loop

1. **Identify Need:** The Hub requires specific resources/items for the current tier.
2. **Place Extractor:** Place a Miner machine on the corresponding resource node (Tree, Stone, Iron, Gem).
3. **Transport:** Connect the Miner's output to processing machines or the Hub using Belts.
4. **Place Processor:** Place necessary processing machines (Sawmill, Furnace, Assembler, Polisher) along the belt path.
5. **Connect & Chain:** Connect machines outputs to inputs of other machines or the Hub using Belts.
6. **Deliver:** Ensure the final required items reach the Hub input.
7. **Unlock:** Once the Hub requirement is met, the next tier's machines/recipes are unlocked.
8. **Expand & Optimize:** Place new machines, create new production lines, and optimize layouts to meet the next tier's goals.

## 3. Progression Tree

* **Tier 0: Manual Start & Basic Automation**
  * **Start:** Manual harvest (limited), Place Hub, Place Miners (Wood/Stone).
  * **Goal:** 10 Logs + 10 Stone -> Hub.
  * **Unlock:** Belts, Sawmill Machine (`Log -> Plank`), Iron Nodes.
* **Tier 1: Basic Processing**
  * **Start:** Miners, Belts, Sawmill, Hub. Access to Wood, Stone, Iron.
  * **Goal:** 20 Planks + 15 Iron Ore -> Hub.
  * **Unlock:** Furnace Machine (`Iron Ore -> Iron Ingot`), Assembler placement.
* **Tier 2: Simple Assembly**
  * **Start:** Miners, Belts, Sawmill, Furnace, Hub. Place Assemblers.
  * **Goal:** 20 Iron Ingots + 10 Planks -> Hub.
  * **Unlock:** Assembler Recipes (`Ingot -> Gears`, `Plank + Gear -> Package`), Gem Nodes.
* **Tier 3: Advanced Resources**
  * **Start:** All previous. Access to Gems.
  * **Goal:** 25 Gears + 15 Packages -> Hub.
  * **Unlock:** Polisher Machine (`Raw Gem -> Polished Gem`), Final Goal reveal.
* **Tier 4: Final Goal**
  * **Start:** All previous.
  * **Goal:** 20 Polished Gems -> Hub.
  * **Unlock:** **Win Condition!** (Simple "You Win!" message).

## 4. Resources & Assets

* **KayKit Assets:**
  * **Required:** KayKit Resource Bits (Base Pack). Includes Logs, Rocks, Ingots (use for Iron), Planks, Crates/Boxes, Gems (raw/polished).
  * **Recommended:** KayKit Resource Bits (Extra Pack). Provides more variety (Money, Fruit, alternative crates if needed for visual distinction).
  * **Optional:** KayKit Nature Bits (or similar) for a Tree model if desired for wood nodes.
* **Machine Models:**
  * **Source:** Ultra-simple primitives (Cubes, Rectangles) from the game engine OR quickly generated simple shapes from Asset Forge. Consistency is key.
  * **Needed Representations:** Miner, Sawmill, Furnace, Assembler, Polisher, Hub (distinct model/primitive).
* **UI Icons:**
  * **Source:** Free icon pack (e.g., game-icons.net) or quickly drawn simple symbols.
  * **Needed Icons:** Pickaxe (Miner), Saw (Sawmill), Flame (Furnace), Gears/Wrench (Assembler), Sparkle/Gem (Polisher), Belt, resource icons for Hub display. Icons should overlay the simple machine models in world-space or appear in UI when selected.
* **Environment:** Simple gridded ground texture, distinct colored patches for resource nodes (Wood=Brown patch with tree model?, Stone=Grey patch, Iron=Dark Grey/Metallic patch, Gem=Sparkly/Crystal patch).

## 5. Controls

* **Mouse:**
  * Left Click: Place selected building (Belt, Machine), Interact with UI.
  * Right Click: Remove building (or cycle through belt directions?).
  * Mouse Wheel (Optional): Zoom camera.
* **Keyboard:**
  * Number Keys (1-6): Select Belt / Miner / Sawmill / Furnace / Assembler / Polisher for placement.
  * WASD (Optional): Pan camera (if not fixed view).
  * ESC: Pause Menu (Ultra simple: just "Resume" / "Quit").

## 6. Scope & Constraints (6-Hour Jam)

* **IN SCOPE:**
  * Grid-based placement.
  * Basic belt transport (straight lines, maybe simple 90-degree turns).
  * Functional Miner, Sawmill, Furnace, Assembler, Polisher, Hub.
  * Tiered unlocking system as defined.
  * Using KayKit assets for resources.
  * Using minimalist shapes + icons for machines.
  * Clear visual feedback for machine processing (simple timer bar or icon change).
  * A defined win condition.
* **OUT OF SCOPE (Unless time permits miraculously):**
  * Power management.
  * Fluids.
  * Complex belt mechanics (splitters, mergers, underground belts - maybe add basic splitter if *essential* and time allows).
  * Machine upgrades.
  * Enemies / Combat.
  * Research tree (using Hub delivery *is* the research/unlock).
  * Complex UI / Tooltips.
  * Sound effects / Music (add placeholder sounds *only* if core loop is 100% done).
  * Save/Load system.
  * Optimization beyond basic functionality.

## 7. Notes

* Prioritize getting the *entire* loop functional for Tier 0/1 first. Build -> Test -> Iterate rapidly.
* Hardcode values (machine speeds, recipe costs) - don't build complex data structures unless necessary.
* Keep it simple! Resist adding features not core to the defined loop.

## 8. Technical Implementation (ECS Approach - TypeScript)

This section outlines a potential implementation using an Entity Component System (ECS) architecture in TypeScript.

* **Entities:** Represent game objects like Miners, Belts, Furnaces, Resources on belts, etc. Each entity is just an ID.
* **Components:** Pure data containers attached to entities. Examples:
  * `PositionComponent { x: number; y: number; }`
  * `ResourceNodeComponent { resourceType: ResourceType; }`
  * `MinerComponent { targetNodeId: EntityId; cooldown: number; outputBuffer?: ResourceItem; }`
  * `BeltComponent { direction: Direction; speed: number; inputBuffer?: ResourceItem; outputBuffer?: ResourceItem; nextBeltId?: EntityId; }`
  * `ProcessorComponent { recipe: Recipe; processingTime: number; progress: number; inputBuffer: ResourceItem[]; outputBuffer?: ResourceItem; }`
  * `ResourceItemComponent { type: ResourceType; }` (Attached to entities representing items *on* belts or in buffers)
  * `HubComponent { requiredItems: Map<ResourceType, number>; currentItems: Map<ResourceType, number>; }`
* **Systems:** Logic that operates on entities possessing specific combinations of components.
  * **MinerSystem:**
    * Queries for entities with `MinerComponent` and `PositionComponent`.
    * Checks proximity to entities with `ResourceNodeComponent`.
    * Handles cooldowns. When ready and output buffer is empty, creates a `ResourceItem` entity with `ResourceItemComponent` and `PositionComponent` (at miner's output), placing it in the `MinerComponent`'s `outputBuffer`.
  * **BeltSystem:**
    * Queries for entities with `BeltComponent` and `PositionComponent`.
    * Handles item transfer:
      * Checks `outputBuffer` of preceding entity (Miner, Belt, Processor). If an item exists, tries to move it to the current belt's `inputBuffer`.
      * Moves item from `inputBuffer` to `outputBuffer` based on `speed` and `dt` (delta time).
      * Checks `nextBeltId` or adjacent Processor/Hub. If the next entity has space in its `inputBuffer`, moves the item from the current belt's `outputBuffer` to the next entity's `inputBuffer`.
    * Updates the `PositionComponent` of `ResourceItem` entities currently on the belt.
  * **ProcessorSystem:**
    * Queries for entities with `ProcessorComponent`.
    * Checks `inputBuffer` for required items according to its `recipe`.
    * If ingredients are present and `outputBuffer` is empty, consumes inputs, increments `progress` based on `processingTime` and `dt`.
    * When `progress` completes, creates the output `ResourceItem` entity and places it in the `outputBuffer`. Resets `progress`.
  * **HubSystem:**
    * Queries for the Hub entity (`HubComponent`).
    * Checks its `inputBuffer` (similar to a processor).
    * If an item arrives, checks if it matches `requiredItems`. If yes, increments `currentItems` count.
    * Checks if `currentItems` meets `requiredItems` for the current tier. If yes, triggers the unlock logic (e.g., enabling placement of new machine types).
  * **PlacementSystem:**
    * Handles player input (mouse clicks, key presses).
    * Creates new entities (Miner, Belt, Processor) with appropriate components based on player selection and grid position.
    * Validates placement rules (e.g., Miner on Node, valid belt connections).
  * **RenderingSystem:**
    * Queries entities with `PositionComponent` and visual components (e.g., `SpriteComponent`, `MeshComponent`).
    * Draws the game state based on component data. Renders items on belts based on their `PositionComponent`.

## 9. Wonderland Engine Implementation Ideas

This section suggests potential Wonderland Engine `Component` classes to bridge the engine's scene graph with the ECS logic and handle specific engine interactions.

* **`GridManagerComponent`:**
  * Responsible for generating the visual grid representation (e.g., using meshes or decals).
  * Holds grid dimensions and potentially spatial lookup structures for efficient querying of objects/entities at specific grid cells.
  * Provides methods for converting world coordinates to grid coordinates and vice-versa.
  * Could manage the placement validation logic (checking if a cell is occupied or valid for a specific building type).
* **`PlayerInputComponent`:**
  * Attached to the main camera or a dedicated input manager object.
  * Handles mouse clicks and keyboard inputs (using `engine.input` or similar event listeners).
  * Translates screen clicks to world/grid coordinates using the `GridManagerComponent`.
  * Communicates player actions (e.g., "place Miner at X,Y", "select Belt type") to the `PlacementSystem` (or directly manages placement logic if not using a strict ECS separation for this).
* **`MachineVisualComponent`:**
  * Attached to objects representing Miners, Processors, Hubs.
  * Holds references to the mesh/model for the machine.
  * Could potentially display status indicators (e.g., simple color change when processing, overlaying UI icons for the machine type).
  * Links the visual representation to the corresponding ECS entity ID.
* **`BeltVisualComponent`:**
  * Attached to objects representing belt segments.
  * Selects the correct mesh/model based on the belt's direction and connections.
  * Could potentially handle the visual movement of items along the belt (though this might also be managed by an `ItemVisualComponent` updated by the `BeltSystem`).
  * Links the visual representation to the corresponding ECS entity ID.
* **`ResourceNodeVisualComponent`:**
  * Attached to objects representing resource nodes on the map.
  * Holds the mesh/model for the resource patch (e.g., rock pile, tree stump).
  * Links the visual representation to the corresponding ECS entity ID.
* **`ItemVisualComponent`:**
  * Attached to objects representing items currently on belts or potentially inside machine buffers (if visualized).
  * Holds the mesh/model corresponding to the `ResourceType` (e.g., Log mesh, Iron Ore mesh).
  * Its world position would be updated by the `BeltSystem` or `ProcessorSystem` based on the item's progress along the belt or within the machine.
  * Links the visual representation to the corresponding ECS entity ID.
* **`UiManagerComponent` (Potentially using Wonderland React-UI):**
  * Attached to a dedicated UI object in the scene.
  * Responsible for rendering the game's UI elements.
  * Would query the `HubComponent` data (via the `HubSystem` or directly if needed) to display current requirements and progress.
  * Displays the currently selected building type for placement.
  * Could show simple alerts or the "Win Condition" message.
  * If using React-UI, this component would extend `ReactUiBase` and define the React component structure for the UI.

This hybrid approach allows leveraging Wonderland Engine's scene graph and rendering capabilities while using an ECS-like pattern for managing game state and logic, promoting better organization, especially as complexity might grow (even within a jam scope). The Wonderland Components act as the "View" and interact with the engine, while the ECS Systems handle the "Model" and "Controller" aspects.
