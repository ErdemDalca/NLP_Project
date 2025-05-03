---
title: Boot Hill GM Documentation
aliases: [Home, Documentation Home]
tags: [documentation, home, index]
created: 2024-12-28
updated: 2025-04-03
---

# Boot Hill GM Documentation

## Overview
This documentation serves as the central knowledge base for the Boot Hill GM project, covering system architecture, game rules, development processes, and AI integration.

## Purpose
The documentation aims to:
- Provide comprehensive technical references for developers
- Maintain consistent game rules and mechanics
- Document architectural decisions and implementation details
- Support onboarding of new contributors

> [!note]
> This documentation uses Obsidian for optimal viewing. Maps of Content (MOC) are available for each major section.

## Quick Navigation
- 🎮 [[meta/project-overview|Project Overview]]
- 📋 [[planning/roadmap|Development Roadmap]]
- 🔧 [[technical-guides/setup|Development Setup]]
- ❗ [[issues/index|Project Issues]]

## System Documentation
### Core Systems
> [[core-systems/_index|Core Systems Overview]]
- [[core-systems/combat-system|Combat System]]
- [[core-systems/state-management|State Management]]
- [[core-systems/journal-system|Journal System]]
- [[core-systems/player-decision-tracking|Player Decision Tracking System]]
- [[core-systems/player-decision-relevance-system|Player Decision Relevance System]]
- [[core-systems/combat-modifiers|Combat Modifiers]]

### Technical Guides
> [[technical-guides/_index|Technical Guides]]
- [[technical-guides/setup|Development Setup]]
- [[technical-guides/state-management/state-unification|State Unification Guide]]
- [[technical-guides/testing/testing-patterns|Testing Patterns]]

### Features
> [[features/_index|Features Overview]]
- 🚧 **Current Development**
  - [[features/_current/narrative-formatting|Narrative Formatting]]
  - [[features/_current/inventory-interactions|Inventory Interactions]]
  - [[features/_current/journal-enhancements|Journal Enhancements]]
- ✅ **Completed Features**
  - [[features/_completed/character-creation|Character Creation]]
  - [[features/_completed/combat-base|Combat Base]]
  - [[features/_completed/reset-game|Reset Game]]
  - [[features/_completed/storytelling|Storytelling]]

### AI Integration
> [[ai/_index|AI Systems Overview]]
- [[ai/game-master-logic|Game Master Logic]]
- [[ai/gemini-integration|Gemini Integration]]
- [[ai/prompt-engineering/core-prompts|Core Prompts]]

### Technical Architecture
> [[architecture/_index|Architecture Overview]]
- [[architecture/architecture-decisions|Architecture Decisions]]
- [[architecture/component-structure|Component Structure]]
- [[architecture/api-integration|API Integration]]

## Game Documentation
### Meta
- [[meta/game-design|Game Design Document]]
- [[meta/project-overview|Project Overview]]

### Boot Hill Rules
- [[boot-hill-rules/game-overview|Game Overview]]
- [[boot-hill-rules/combat-rules|Combat Rules]]
- [[boot-hill-rules/equipment|Equipment]]
- [[boot-hill-rules/weapons-chart|Weapons Chart]]

## Development
### Workflows
> [[development/workflows/index|Development Workflows]]
- [[development/workflows/feature-workflow|Feature Development]]
- [[development/workflows/ai-workflow|AI Development]]

### Issues
> [[issues/index|Project Issues]]
- [[issues/issue-142/cleanup-tasks|Issue #142 Cleanup Tasks]]

### Reference
- [[reference/_index|Reference Documentation]]
- [[examples/_index|Code Examples]]
- [[templates/_index|Document Templates]]

---

```mermaid
graph TD
    A[Documentation] --> B[System Docs]
    A --> C[Game Docs]
    A --> D[Development]
    B --> E[Core Systems]
    B --> F[Features]
    B --> G[AI]
    B --> H[Architecture]
    B --> O[Technical Guides]
    C --> I[Meta]
    C --> J[Rules]
    D --> K[Workflows]
    D --> L[Reference]
    D --> M[Examples]
    D --> N[Templates]
    D --> P[Issues]
```