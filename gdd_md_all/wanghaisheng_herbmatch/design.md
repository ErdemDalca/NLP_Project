# Herb Match - Game Design Document

## Overview
Herb Match is a match-3 puzzle game with educational elements about different medicinal herbs. The game features a battle pass system with various herb-themed reward tracks.

## Core Gameplay
- Match 3 or more identical herbs in a row or column
- Swap adjacent herbs to create matches
- Earn points based on match length
- Complete level objectives before time runs out

## Level Design System

### Level Structure
Following industry practices from successful match-3 games, our levels are designed with:

1. **Progressive Difficulty**: Difficulty increases gradually to allow players to develop skills
2. **Varied Objectives**: Different objectives keep gameplay fresh and challenging
3. **Limited Resources**: Time constraints and move limitations create strategic decisions
4. **Recovery Periods**: Easier levels occasionally appear after difficult ones to maintain player motivation

### Level Types
1. **Score Target Levels**: Reach a specific score within the time limit
2. **Collection Levels**: Collect specific herb types (e.g., "Collect 15 Mint herbs")
3. **Obstacle Levels**: Clear special obstacles by matching herbs adjacent to them
4. **Combination Levels**: Combine multiple objectives (e.g., reach score + collect specific herbs)

### Difficulty Progression

#### Early Game (Levels 1-10)
- Focus on basic mechanics
- Simple score targets
- Generous time limits
- Tutorial elements integrated into gameplay

#### Mid Game (Levels 11-30)
- Introduction of collection objectives
- Moderate time constraints
- Multiple objectives introduced
- Special herb combinations appear more frequently

#### Late Game (Levels 31+)
- Complex combinations of objectives
- Strict time limits
- Special obstacles
- Strategic thinking required

### Level Parameters
- **Score Requirements**: Incrementing by 15-25% between levels
- **Time Limits**: Gradually decreasing with level progression
- **Board Size**: Standard 6x6 for most levels, potential for special dimensions in advanced levels
- **Special Herb Frequency**: Increased probability in higher levels

### Detailed Level Design

#### Objective Balancing
- Collection objectives scale with level number (Level × 1.5 herbs to collect)
- Time limits decrease by 1 second every 2 levels after level 5
- Score targets follow a logarithmic curve to maintain challenge without frustration

#### Special Level Features
- **Milestone Levels** (Every 5th level):
  - Introduce new mechanics or herb types
  - Feature slightly reduced difficulty as "breather levels"
  - Provide special rewards upon completion

- **Challenge Levels** (Every 10th level):
  - Significantly higher difficulty with multiple objectives
  - Include time pressure and special board configurations
  - Rewards include premium currency and battle pass boosts

#### Board Configuration Variations
- **Standard Configuration**: Balanced distribution of herb types
- **Harvest Configuration**: Higher concentration of specific herbs (collection levels)
- **Restricted Configuration**: Limited herb variety for increased challenge
- **Obstacle Configuration**: Special tiles that must be cleared by adjacent matches

#### Level Completion Rewards
- 1 Star: Complete the primary objective
- 2 Stars: Complete the primary objective with 20% higher score
- 3 Stars: Complete the primary objective with 50% higher score and all secondary objectives

All star thresholds are carefully calibrated based on level difficulty to ensure consistent challenge throughout the game.

## Battle Pass System

The battle pass system includes themed tracks related to:
- Detoxification herbs
- Anti-humidity herbs
- Kidney health herbs
- Anti-hair loss herbs

Each battle pass track:
- Contains 30 levels of progression
- Features both free and premium rewards
- Requires XP earned through gameplay
- Unlocks educational content about herbal medicine

## Player Progression

### Short-term Progression
- Level completion
- Score improvements
- Collection of specific herbs

### Mid-term Progression
- Battle pass advancement
- Unlocking new herb varieties
- Achievement completion

### Long-term Progression
- Mastery of advanced levels
- Collection of all premium herbs
- Learning about medicinal properties of herbs

## Reward System
- **Regular Rewards**: XP for battle pass, score points
- **Special Rewards**: Unique herb unlocks, educational content
- **Premium Rewards**: Rare herbs, special effects, exclusive knowledge

## Monetization System

### Revenue Streams
The game's monetization strategy is built around multiple complementary revenue sources:

1. **Battle Pass System**
   - Basic free tier available to all players
   - Premium tier with exclusive herb unlocks ($4.99 monthly subscription)
   - Battle pass progress boosts ($1.99 - $9.99)

2. **In-Game Shop**
   - Time boosters ($0.99 - $2.99)
   - Hint packages (5 hints for $0.99, 20 hints for $2.99)
   - Special herb unlock bundles ($4.99 - $19.99)
   - Limited-time seasonal themes ($2.99 - $9.99)

3. **Advertising**
   - Rewarded ads for extra hints
   - Interstitial ads between gameplay sessions (skippable with premium)
   - Banner ads on non-gameplay screens (removed with any purchase)

4. **Seasonal Special Offers**
   - Holiday-themed herb bundles
   - Limited availability offers creating urgency
   - Discounted bundles combining multiple item types

### Balancing Free vs. Paid Content
- Core gameplay remains fully accessible to free players
- Premium content focuses on convenience, cosmetics, and collection completion
- Regular free updates to maintain player engagement
- Premium content provides meaningful value without creating pay-to-win dynamics

### Player Conversion Strategy
- First-purchase special offers
- Graduated difficulty curve leading to natural monetization opportunities
- Clear visual indicators of premium benefits
- Loss aversion techniques (limited-time offers, daily rewards)

## Visual Design
- Soothing, nature-inspired color schemes
- Clear visual hierarchy
- Calming animations for matching and rewards
- Informative UI for educational components

## Future Development
- **Seasonal Events**: Limited-time herb collections and challenges
- **Social Features**: Friend leaderboards and gifting
- **Custom Difficulty**: Player-adjustable settings for personalized experience
- **Additional Battle Pass Themes**: More medicinal herb categories and knowledge

## Future Expansion
- **Subscription Model**: Monthly herb club with exclusive benefits
- **Multi-game Ecosystem**: Cross-promotion with related wellness apps
- **Content Partnerships**: Collaborations with herbal medicine brands