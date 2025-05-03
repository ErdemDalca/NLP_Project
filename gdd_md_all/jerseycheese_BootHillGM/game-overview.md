---
title: Game Overview
aliases: [Boot Hill Overview, Game Rules Overview, Boot Hill v2 Rules, Core Rulebook]
tags: [rules, overview, boot-hill-v2, core-rules, reference]
created: 2024-12-28
updated: 2024-12-28
---

# Boot Hill v2 Game Overview

Boot Hill is a Western-themed role-playing game designed to function in two ways:

1. As a set of rules for man-to-man gunfighting action
2. As an outline guide for setting up quasi-historical or fictional role-playing campaigns

## Key Features
- Players take on the roles of individual characters in the American Old West
- Can be played as one-off scenarios or as part of a larger campaign
- Focuses on gunfights, brawls, and other Western-themed actions
- Allows for both player characters and non-player characters (NPCs)

For implementation details, see [[../core-systems/ai-integration|AI Game Master Integration]].

## Game Scales

1. Tactical Tabletop Play
   - Each turn represents approximately 10 seconds
   - 1 square/inch = 6 feet
   - For combat details, see [[combat-rules|Combat Rules]]
   - For weapon information, see [[weapons-chart|Weapons Reference]]

2. Campaign Play
   - Gamemaster moderates time passage (days, weeks, months)
   - Can zoom in for tactical play when needed
   - For campaign guidelines, see [[campaign-rules|Campaign Rules]]

## How to Play
1. Create characters by rolling for abilities
2. Equip characters with period-appropriate items
3. Set up scenarios or campaign situations
4. Resolve actions using dice rolls and game rules
5. Engage in gunfights, brawls, and other Western activities
6. Progress characters through experience and survival

For character creation details, see [[character-creation|Character Creation Guide]].
For equipment details, see [[equipment|Equipment Rules]].

## Role of the Gamemaster
- Moderates game activity
- Creates campaign settings and scenarios
- Oversees all game actions, both on and off the tabletop
- Manages information and "behind the scenes" developments

For AI implementation, see [[../ai/game-master-logic|AI Game Master Logic]].

## Combat Overview
- Turn-based tactical combat
- Detailed weapon and range mechanics
- Brawling and gunfighting rules
- Wound and damage tracking

For combat details, see:
- [[combat-rules|Combat Rules]]
- [[base-numbers|Base Numbers Calculation]]
- [[observation-sighting|Observation and Sighting]]
- [[brawling-context|Brawling Rules]]

## Character Management
- Detailed character creation system
- Equipment and inventory tracking
- Experience and progression
- NPC interaction guidelines

For character details, see:
- [[character-creation|Character Creation]]
- [[equipment|Equipment Rules]]
- [[misc-characters|NPC Reference]]

## Implementation Notes
The game is designed to be flexible, allowing for both structured scenarios and freeform play in a Western setting. Our digital implementation maintains this flexibility while adding AI-driven storytelling and automated rule management.

For technical details, see:
- [[../core-systems/combat-system|Combat System Implementation]]
- [[../core-systems/state-management|State Management]]
- [[../features/_current/inventory-interactions|Inventory System]]
- [[../features/_current/journal-enhancements|Journal System]]

## Related Documentation
- [[../meta/game-design|Game Design Document]]
- [[../ai/prompt-engineering/storytelling|Storytelling Prompts]]
- [[../planning/roadmap|Development Roadmap]]