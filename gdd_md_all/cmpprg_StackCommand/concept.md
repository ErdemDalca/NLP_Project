# Stack Command - Game Design Document

## Game Overview
**Genre:** Real-Time Strategy (RTS)  
**Platform:** Windows, Linux, Mac  
**Engine:** Unity 6, 6000.0.26f1
**Programming Language:** C#  

## Core Mechanics

### Units
- Basic form: Flat, coin-like cylinders
- Can be stacked up to 10 levels
- Serve as both army and resource
- Can capture territory by sacrificing one unit

#### Unit Properties
- Range attack capability
- Can perform a kamikaze manuever
  - This will take the enemy stack down by 1. Needs more thought and tuning. Maybe 2 kamikaze takes stack down by 1
- Line of sight based on stack height
  - a 2 stack can not shoot through a 2 stack. A 2 stack can shoot over a 1 stack.
- Cannot shoot through higher stacks
- Attributes change/upgrade with each stack level:
  - Range (up)
  - Firepower (up)
  - Defense (up)
  - Speed (down)
  - Manueverablity (down)
  - Other stats TBD

### Buildings

#### Home Base
- Starting structure
- Generates 1 unit every 30 seconds
- Victory/defeat condition
- Initial unit count: 5

#### Unit Generator
- Secondary unit production facility
- Supplements home base unit generation
- Cost: TBD units

#### Unit Fuser
- Creates specialized unit formations
- Different standard fusion patterns available
  - User will be able to create custom patterns in time.
- Cost: TBD units

#### Unit Stacker
- Combines units vertically
- Upgrades unit capabilities
- Maximum stack: 10 units
- Once a unit is stacked it is considered 1 unit. Can not be unstacked.
- Cost: TBD units

### Territory Control
- Capturable by sacrificing 1 unit
- Provides strategic advantages:
  - Heals friendly units
  - Damages enemy units
- Territory influence radius: TBD

## Game Flow
1. Match starts with home base and 5 units
2. Players expand territory and generate resources (units)
3. Strategic decisions:
  - Unit production
  - Building placement
  - Stack management
  - Territory control
    - Do we want another victory condition. 51% of territory?
  
4. Victory achieved by destroying enemy base

## Visual Style
- Clean, minimalist aesthetic
- Clear visual distinction between stack levels
- Easy-to-read territory boundaries
- Distinct building designs

## Technical Considerations
- Pathfinding system for units
- Stack management system
- Territory influence calculation
- Unit generation timing system
- Combat resolution system