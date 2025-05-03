# Tokyo Train Station Adventure: Language Learning Game Design Document

## Game Overview
A pixel art adventure game where the player navigates a Tokyo train station with a bilingual companion dog. The player, an English speaker with basic Japanese knowledge (JLPT N5), must interact with Japanese-speaking NPCs to book a ticket to Odawara for a udon noodle lunch with a friend.

## Core Game Elements

### 1. Player Entity
- Controls character movement in the station
- Interacts with NPCs, companion, and environment
- Has language proficiency attributes (JLPT N5 level)
- Maintains inventory/progress tracking
- Authentication state (Google/Facebook login)

### 2. Companion (Dog) Entity
- Follows player throughout the game
- Provides language assistance when prompted
- Has dialogue system with multiple helper functions:
  - Translation confirmation
  - Vocabulary hints
  - Direction guidance
  - Character suggestions
- Personality traits: patient teacher + enthusiastic cheerleader
- Activated via a "dog whistle" icon
- Can direct player attention to important objects by dancing around them

### 3. NPC Entities
- Information booth attendant
- Ticket machine operator
- Station attendants (3)
- Train conductor
- Visual indicator (floating question mark) for interactive NPCs
- Japanese-only dialogue system

### 4. Environment Objects
- Information board in the main area
- Ticket machines
- Vending machines (one per platform)
- Japanese signage throughout station
- Train platforms and trains

### 5. Interaction Systems
- Dialogue system (multi-modal input handling)
- Japanese keyboard input processing
- Multiple-choice selection
- Text-to-speech for dialogue
- AI language processing for player inputs
- Gentle correction system for language errors

### 6. Progression System
- Task completion tracking
- Badge/achievement system
- Language proficiency tracking
- Save/load functionality via external auth

## Game Flow Architecture

### 1. Player Login/Authentication
- Google/Facebook OAuth integration
- SQLite database connection for progress tracking

### 2. Tutorial Phase
- Introduction to companion mechanics
- Basic movement and interaction tutorial
- Explanation of game objectives

### 3. Main Game Loop
- Player explores Tokyo station at their leisure
- Companion provides guidance when prompted
- Sequential NPC interactions:
  1. Information booth for ticket booking guidance
  2. Ticket machine for purchasing
  3. Station attendant for platform directions
  4. Train conductor for boarding

### 4. Interaction Model
- Player approaches NPC/object
- Interaction prompt appears
- Player selects input method (typing/multiple choice)
- AI processes language input
- Feedback based on correctness
- Companion assist available as needed

### 5. Companion Assistance Loop
- Player activates dog whistle
- Assistance menu appears with options:
  - Who to talk to next
  - Vocabulary help
  - Translation confirmation
  - General hints
- Companion responds based on player's current situation

## Technical Architecture Considerations

### 1. Frontend Layer
- HTML5 Canvas for rendering
- JavaScript game engine (Phaser.js could work well)
- Pixel art assets (8-bit Famicom style)
- Input handling for keyboard/mouse

### 2. Game Logic Layer
- State management for game progress
- Character movement systems
- Interaction systems
- Dialogue tree management

### 3. Language Processing Layer
- AI integration for language assistance
- Japanese input processing
- Speech recognition (optional)
- Text-to-speech synthesis

### 4. Data Persistence Layer
- OAuth authentication
- SQLite database integration
- Progress tracking schemas
- Achievement storage

## Visual Design Elements

### 1. Map Layout
- Main concourse with information board and booth
- Ticket machine area
- Multiple platforms with directional signage
- Each platform has a vending machine

### 2. Character Design
- Player avatar (simple 8-bit design)
- Companion dog (expressive, distinct animations)
- NPCs with unique appearances based on roles

### 3. UI Elements
- Japanese/English text display system
- Dialogue boxes
- Companion assistance interface
- Achievement notifications
- Language input methods

## Language Learning Elements

### 1. Input Methods
- Japanese keyboard typing
- Multiple choice selections
- Potential for writing recognition
- Text-to-speech for pronunciation practice

### 2. Learning Progression
- Assumes basic knowledge of hiragana/katakana
- Focus on practical, situational Japanese
- Station-related vocabulary building
- No time pressure to allow for learning

### 3. Feedback System
- Gentle corrections for mistakes
- Positive reinforcement for correct usage
- Companion avoids direct translations of signage
- Confirmation of player's own translation attempts
