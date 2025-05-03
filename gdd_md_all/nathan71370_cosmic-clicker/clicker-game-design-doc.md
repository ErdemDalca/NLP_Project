# Cosmic Clicker: Game Design Document

## Table of Contents
1. [Game Overview](#game-overview)
2. [Core Mechanics](#core-mechanics)
3. [Progression System](#progression-system)
4. [Economy](#economy)
5. [Characters & Collectors](#characters--collectors)
6. [Special Events & Challenges](#special-events--challenges)
7. [User Interface](#user-interface)
8. [Audio & Visual Design](#audio--visual-design)
9. [Monetization](#monetization)
10. [Technical Requirements](#technical-requirements)
11. [Future Content & Expansion](#future-content--expansion)

---

## Game Overview

**Cosmic Clicker** is an incremental game where players build and expand their own cosmic empire by collecting "Cosmic Energy" through clicking and automated collectors. Starting with a single small planet, players will expand across galaxies, discover new characters, technologies, and mysteries of the universe.

### Concept
Players collect Cosmic Energy by tapping on their home planet and through automated collectors. This energy is used to upgrade collectors, unlock new characters with unique abilities, and expand their cosmic empire. The game features multiple prestige systems, limited-time events, and a rich progression path that continuously introduces new mechanics and content.

### Target Audience
- Primary: Casual gamers who enjoy incremental progression
- Secondary: Strategy gamers who enjoy optimization
- Age range: 10+
- Platform: Web app compatible with IOS and android

### Unique Selling Points
1. Multi-layered prestige system that introduces new mechanics at each tier
2. Character collection with unique synergy effects and storylines
3. Dynamic universe that visually evolves based on player progression
4. Mini-games that break up the clicking routine
5. Social features allowing for alliances and cooperative challenges

---

## Core Mechanics

### Clicking Mechanism
- **Basic Click**: Tap the home planet to generate Cosmic Energy (CE)
- **Click Power**: Base value starts at 1 CE per click
- **Critical Clicks**: 5% chance for a critical click that generates 5x CE
- **Combo System**: Consecutive clicks within 1 second of each other build a combo multiplier (up to 5x)

### Automated Collection
- **Collectors**: Automated units that generate CE without player interaction
- **Base Production**: Each collector has a base production rate per second
- **Efficiency**: Collectors have efficiency ratings that can be improved through upgrades
- **Offline Production**: Collectors continue to generate CE when the game is closed (at reduced efficiency of 60%)

### Energy Types
1. **Cosmic Energy (CE)**: Primary currency, used for basic upgrades and purchases
2. **Stellar Essence (SE)**: Premium currency earned through prestige, events, and occasionally from special clicks
3. **Dark Matter (DM)**: Late-game currency unlocked after first Galaxy Reset
4. **Quantum Particles (QP)**: End-game currency used for ultimate upgrades

### Upgrades
- **Click Power Upgrades**: Increase CE earned per click
- **Collector Upgrades**: Improve production rate of automated collectors
- **Global Multipliers**: Affect all production sources
- **Special Upgrades**: Unique effects like critical click chance, offline production boost, etc.

---

## Progression System

### Prestige Layers
The game features a multi-tiered prestige system that resets progress but grants powerful bonuses:

#### 1. Planet Reset (Tier 1)
- **Requirement**: Reach 1,000,000 CE
- **Reset**: Lose all CE and collectors
- **Reward**: Earn Star Crystals based on progress
- **Bonus**: Each Star Crystal provides +1% to all production
- **New Feature Unlock**: Character collection system

#### 2. Solar System Reset (Tier 2)
- **Requirement**: Accumulate 100 Star Crystals
- **Reset**: Lose all CE, collectors, and Star Crystals
- **Reward**: Earn Nebula Dust based on total Star Crystals earned
- **Bonus**: Nebula Dust unlocks permanent technologies in the Tech Tree
- **New Feature Unlock**: Tech Tree system and new collector types

#### 3. Galaxy Reset (Tier 3)
- **Requirement**: Complete 10 Tech Tree branches
- **Reset**: Lose all previous currencies except Stellar Essence
- **Reward**: Earn Dark Matter based on Tech Tree completion
- **Bonus**: Dark Matter enables powerful Galaxy Modifiers
- **New Feature Unlock**: Multi-dimensional gameplay where players can manage multiple planets simultaneously

#### 4. Universe Reset (Tier 4)
- **Requirement**: Reach Dark Matter capacity in 5 galaxies
- **Reset**: Complete game reset except for Cosmic Archives (achievements)
- **Reward**: Earn Quantum Particles that enable game-changing abilities
- **Bonus**: Each Universe Reset makes subsequent progression faster
- **New Feature Unlock**: Universe Customization where physical constants can be altered

### Milestones
- Every major CE threshold (powers of 10) unlocks new content
- Achievement system with tiered rewards
- Collection milestones for obtaining sets of characters
- Tech Tree completion rewards

---

## Economy

### Currency Balance
- **Early Game**: CE generation is primarily through clicking (first 10 minutes)
- **Mid Game**: Collector automation becomes the main source of CE
- **Late Game**: Synergies between characters, collectors, and Tech Tree provide exponential growth
- **End Game**: Multi-dimensional management across galaxies

### Soft Currency (Cosmic Energy)
- Used for basic purchases and upgrades
- Generation increases exponentially with progression
- Inflation is controlled through prestige mechanics

### Hard Currency (Stellar Essence)
- Premium currency that can be earned through gameplay or purchased
- Used for time skips, premium characters, and special upgrades
- Conversion rate: Approximately 100 SE earned per Planet Reset

### Special Currencies
- **Star Crystals**: Earned through Planet Resets
- **Nebula Dust**: Earned through Solar System Resets
- **Dark Matter**: Earned through Galaxy Resets
- **Quantum Particles**: Earned through Universe Resets

### Resource Sinks
- Character upgrades
- Permanent boosters
- Special event participation
- Collection system expansion

---

## Characters & Collectors

### Character System
Players can unlock characters that provide unique bonuses to their cosmic empire. Characters are obtained through:
- Cosmic Crates (standard unlocks via CE)
- Stellar Crates (premium unlocks via SE)
- Event achievements
- Milestone rewards

### Character Attributes
- **Rarity**: Common, Uncommon, Rare, Epic, Legendary, Mythic
- **Type**: Explorer, Scientist, Engineer, Mystic, Commander
- **Special Ability**: Unique effect or bonus
- **Synergy Effects**: Bonuses when certain character combinations are active

### Character List Examples
1. **Astro (Common Explorer)**
   - Ability: +10% click power
   - Synergy: +5% CE production when paired with any Scientist

2. **Dr. Nova (Uncommon Scientist)**
   - Ability: +15% to all Collector efficiency
   - Synergy: +10% critical click chance when paired with any Explorer

3. **Quantum (Rare Engineer)**
   - Ability: Automates clicking at 1 click per second
   - Synergy: Doubles offline production when paired with any Commander

4. **Galaxia (Epic Mystic)**
   - Ability: Chance to get double Star Crystals on Planet Reset
   - Synergy: Reduces Tech Tree costs by 15% when paired with any Scientist

5. **Commander Zeta (Legendary Commander)**
   - Ability: All production multiplied by 2x for 1 hour (once per day)
   - Synergy: All active character abilities are 50% stronger when paired with any Mystic

6. **Cosmic Entity (Mythic)**
   - Ability: Time warps that accelerate production by 5x for 10 minutes
   - Synergy: Universal synergy with all character types, +20% to their abilities

### Character Upgrade System
- Characters can be leveled up using duplicate cards
- Each level increases their ability strength by 10%
- Maximum level: 10 for Common, 8 for Uncommon, 6 for Rare, 4 for Epic, 3 for Legendary, 2 for Mythic

### Collector Types
1. **Cosmic Harvester**: Basic collector, generates 1 CE/second
2. **Stellar Extractor**: Unlocked after 1st Planet Reset, generates 10 CE/second
3. **Nebula Processor**: Unlocked after 1st Solar System Reset, generates 100 CE/second
4. **Dark Matter Condenser**: Unlocked after 1st Galaxy Reset, generates 1,000 CE/second
5. **Quantum Manipulator**: Unlocked after 1st Universe Reset, generates 10,000 CE/second

---

## Special Events & Challenges

### Limited-Time Events
- **Cosmic Anomalies**: Weekly events with unique mechanics and rewards
- **Celestial Alignment**: Monthly special event with premium rewards
- **Universe Birthday**: Annual celebration with exclusive characters and bonuses

### Challenges
- **Speed Runs**: Complete specific goals within time limits
- **Restricted Play**: Complete goals with certain limitations (no clicking, limited collectors, etc.)
- **Boss Battles**: Special clicking challenges against cosmic entities

### Mini-Games
- **Asteroid Field**: Tap asteroids for bonus CE
- **Constellation Connect**: Connect stars to form constellations for rewards
- **Gravity Puzzles**: Redirect cosmic objects using gravity wells

### Social Features
- **Alliances**: Form groups with other players
- **Alliance Challenges**: Cooperative goals with shared rewards
- **Trading System**: Exchange common characters with alliance members
- **Gift System**: Send and receive daily energy boosts

---

## User Interface

### Main Screen Elements
1. **Central Planet**: Main clicking area
2. **Resource Display**: Shows all currencies
3. **Collector Panel**: Lists all active collectors and their production
4. **Character Roster**: Shows active and owned characters
5. **Menu Bar**: Access to various game features
6. **Achievement Tracker**: Shows progress toward next milestone

### Navigation Structure
- **Main View**: Central planet and primary clicking interface
- **Collectors Tab**: Manage and upgrade automated collectors
- **Characters Tab**: View, upgrade, and assign characters
- **Prestige Tab**: Access to reset options and prestige shop
- **Tech Tree Tab**: Unlocked after first Solar System Reset
- **Events Tab**: Access to current and upcoming events
- **Shop**: Purchase Cosmic Crates and premium items

### HUD Design
- Minimalist design with expandable panels
- Color-coded resources and currencies
- Visual feedback for clicks (ripples, numbers, particles)
- Achievement notifications
- Production statistics

### Visual Progression
- The central planet evolves visually based on progress
- Background space scene evolves from single planet to galaxy view
- Collectors are visually represented around the planet
- Character portraits appear with special effects during activation

---

## Audio & Visual Design

### Art Style
- Colorful, stylized cosmic theme
- Slightly cartoonish character designs
- Particle effects for clicking and production
- Animated backgrounds that evolve with progress

### Animation
- Smooth transitions between screens
- Click feedback animations
- Character ability activation effects
- Collector operation animations
- Prestige reset special effects

### Audio Design
- **Sound Effects**:
  - Satisfying click sounds with variations
  - Collection sounds for resources
  - Achievement unlocks
  - Character ability activations
  
- **Music**:
  - Ambient space-themed background music
  - Intensity increases with combo builds
  - Special themes for events
  - Prestige ceremony music

### Visual Feedback
- Numbers pop up showing CE gained from clicks
- Glowing effects for critical clicks
- Visual cues for character ability activation
- Progress bars for all collectible resources

---

## Monetization

### Revenue Streams
1. **In-app Purchases**:
   - Stellar Essence packages
   - Special character bundles
   - Time skip boosters
   - Cosmetic upgrades

2. **Rewarded Advertising**:
   - Watch ads for temporary production boosts
   - View ads to speed up certain timers
   - Ad rewards for bonus Cosmic Crates

3. **Premium Subscription**:
   - "Cosmic VIP" monthly subscription
   - Benefits: +50% offline production, daily SE, exclusive character rotation

### Pricing Structure
- Small SE Package: $0.99 (100 SE)
- Medium SE Package: $4.99 (550 SE)
- Large SE Package: $9.99 (1200 SE)
- Mega SE Package: $19.99 (2500 SE)
- Cosmic VIP: $4.99/month

### Player Conversion Strategy
- First Planet Reset gives small taste of SE
- Early game is generous with rewards
- Premium characters offer unique abilities not available otherwise
- VIP benefits substantially improve quality of life

### Free Player Experience
- Complete game progression available without payment
- Regular events provide opportunities for premium currency
- Ad rewards as alternative to purchases
- Balance ensures free players can enjoy full game with more time investment

---

## Technical Requirements

### Performance Targets
- Minimum 60 FPS on mid-range devices
- Efficient battery usage
- Low memory footprint
- Fast loading times (<2 seconds on standard devices)

### Platform Support
- web, iOS, Android

### Backend Requirements
- Player account system
- Cloud save functionality
- Event management system
- Analytics integration
- Push notification service

### Data Storage
- Local save with cloud backup
- Approximately 5-10 MB storage requirement
- Efficient state serialization for quick save/load

---

## Future Content & Expansion

### Post-Launch Content Plan
- **Month 1**: Quality of life improvements, balance adjustments
- **Month 2**: New character set (5-10 new characters)
- **Month 3**: New mini-game and event type
- **Month 6**: New prestige layer with unique mechanics
- **Year 1**: Major expansion with new universe type

### Community Engagement
- Regular developer updates
- Community challenges with global rewards
- Social media integration
- Player feedback implementation strategy

### Expansion Possibilities
- PvP challenges
- Cooperative multi-player expeditions
- Universe customization expansion
- Narrative-driven special events

---

## Implementation Timeline

### Phase 1: Core Development (8 weeks)
- Basic clicking mechanics
- Initial collector system
- UI framework
- Save/load system

### Phase 2: Content Building (6 weeks)
- Character system implementation
- First 20 characters
- Initial prestige layer
- Basic achievements

### Phase 3: Feature Completion (6 weeks)
- All prestige layers
- Event system
- Tech Tree
- Mini-games

### Phase 4: Polish & Testing (4 weeks)
- Balance adjustments
- Performance optimization
- Bug fixing
- Closed beta test

### Phase 5: Launch Preparation (2 weeks)
- Store page preparation
- Marketing assets
- Final testing
- Soft launch in select regions

### Total Development Time: 26 weeks

---

## Appendix

### Balancing Guidelines
- Click power should increase by approximately 10x per prestige
- Collector costs follow an exponential curve (price = base_price * 1.15^owned)
- Character drop rates: Common (60%), Uncommon (25%), Rare (10%), Epic (4%), Legendary (0.9%), Mythic (0.1%)
- Time to first prestige: approximately 1-2 hours of active play

### Glossary of Terms
- **CE**: Cosmic Energy
- **SE**: Stellar Essence
- **DM**: Dark Matter
- **QP**: Quantum Particles
- **CPS**: Cosmic Energy Per Second

### References & Inspiration
- Cookie Clicker (pacing and upgrade system)
- Realm Grinder (prestige mechanics)
- Adventure Capitalist (automation balance)
- Idle Heroes (character collection system)
