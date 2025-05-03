# Solar Clipper: First Light
## Game Design Document

## 1. Core Concept
Solar Clipper: First Light is a text-based ship management simulation focused entirely on maintaining a small cargo vessel during interstellar transit. The player must balance ship systems, personal needs, and unexpected events to complete deliveries successfully. The game prioritizes immersion through contextual interfaces, meaningful decision-making, and the satisfaction of mastering ship maintenance routines.

## 2. Ship Environment

### Ship Layout
- **Bridge**: Navigation, communications, ship status monitoring
- **Engine Room**: Power management, repairs, system diagnostics
- **Cargo Hold**: Small but secure storage for current delivery
- **Living Quarters**: Sleep, personal storage, meal preparation
- **Maintenance Bay**: Tools, spare parts, specialized repairs

### Interface Access Points
- **Bridge Terminal**: Accessible only when physically at the bridge
- **Datapad**: A physical item carried by the player for personal info
- **Engineering Station**: System diagnostics only available in engine room
- **Maintenance Tools**: Located in specific compartments

## 3. Core Systems

### Player Needs System
- **Energy/Rest**: Depletes over time, restored by sleeping
- **Nutrition**: Requires food preparation or packaged meals
- **Morale**: Affected by events, success/failure, recreation activities
- Each need has consequences when neglected (decreased efficiency, system control accuracy)

### Ship Systems
- **Power Plant**: Generates energy for all systems
- **Life Support**: Oxygen, temperature, water recycling
- **Propulsion**: Main engine for transit
- **Navigation**: Course plotting and maintenance
- **Cargo Systems**: Environmental controls for cargo

### Time System
- All actions consume time
- Ship transit occurs in real-time (with time-skip option)
- Systems degrade based on time and use
- Scheduled maintenance tasks create routine

### Event System
- Random technical failures
- Space phenomena affecting systems
- Personal events (dreams, memories, messages)
- Cascading failures when issues are left unaddressed

## 4. Interface Modes

### First-Person Navigation
- Text descriptions of ship compartments
- Movement between areas consumes time
- Interactions with objects/systems through simple commands
- Hybrid navigation with text commands and clickable elements

### Bridge Terminal (accessed only at bridge)
```
+--------- BRIDGE TERMINAL -----------+
|                                     |
| NAV STATUS: [In Transit]            |
| DESTINATION: Alpha Centauri         |
| ETA: 4d 7h 23m                     |
|                                     |
| SYSTEM STATUS:                      |
| POWER: 87% [████████  ]             |
| LIFE SUP: 93% [█████████ ]          |
| ENGINES: 76% [███████   ]           |
|                                     |
| FUEL: 65% [██████    ]              |
| CARGO INTEGRITY: 100% [██████████]  |
|                                     |
| OPTIONS:                            |
| [1] Ship Status Details             |
| [2] Navigation Control              |
| [3] Communications                  |
| [4] System Diagnostics              |
+-------------------------------------+
```

### Datapad Interface (used when accessing datapad item)
```
+----------- DATAPAD -------------+
|                                 |
| [PERSONAL LOG]                  |
| [CONTRACT DETAILS]              |
| [INVENTORY]                     |
| [NOTES]                         |
| [PERSONAL STATUS]               |
|   REST: 72% [███████   ]        |
|   NUTRITION: 54% [█████     ]   |
|   MORALE: 81% [████████  ]      |
|                                 |
| TIME: 0437 SHIP TIME            |
|                                 |
+---------------------------------+
```

### Engineering Interface (engine room only)
```
+------- ENGINEERING SYSTEMS -------+
|                                   |
| POWER DISTRIBUTION:               |
| [LIFE SUPPORT]: 30% [███       ]  |
| [PROPULSION]: 45% [████      ]    |
| [NAV/COMMS]: 15% [█         ]     |
| [CARGO]: 10% [█          ]        |
|                                   |
| EFFICIENCY: 87%                   |
| TEMPERATURE: NOMINAL              |
|                                   |
| MAINTENANCE REQUIRED:             |
| - [COOLANT FILTER]: 7h REMAINING  |
| - [POWER CELLS]: 2d REMAINING     |
|                                   |
+-----------------------------------+
```

## 5. Gameplay Loop

### Daily Routine
- Check ship systems via appropriate terminals
- Perform scheduled maintenance tasks
- Manage personal needs (rest, nutrition)
- Respond to any alerts or events
- Log activities in personal datapad

### Transit Management
- Balance power distribution
- Perform preventative maintenance
- Monitor cargo integrity
- Plot course adjustments if needed

### Event Response
- System failures require immediate attention
- External events may demand quick decisions
- Personal choices affect future options

## 6. Interface Approach

### Hybrid Input System
- **Text Commands**: Natural language inputs ("go to engine room", "check power levels")
- **Keyboard Shortcuts**: Simple commands ("e" for engine room, "b" for bridge)
- **Clickable Elements**: Interactive ASCII interfaces with clickable buttons
- **Command History**: Accessible with up/down arrows
- **Tab Completion**: For common commands

### Navigation vs. System Interaction
- First-person navigation primarily uses text commands
- System interfaces use more interactive clickable elements
- Creates natural rhythm between narrative movement and focused interaction

### Benefits of Hybrid Approach
- **Accessibility**: Different players can use preferred input method
- **Immersion**: Text maintains narrative feel while visual interfaces provide feedback
- **Learning Curve**: Start with clicking, graduate to efficient keyboard commands
- **Gameplay Depth**: Complex actions work better with specific input methods
- **Skill Development**: Players develop shortcuts for routine tasks

## 7. Technical Implementation Structure

### Core Object Model
- `Ship` containing:
  - `Systems` (collection of individual systems)
  - `Compartments` (locations)
  - `Inventory` (supplies and tools)
- `Player` containing:
  - `Needs` (rest, nutrition, etc.)
  - `Skills` (improve with use)
  - `Personal Inventory`
- `EventManager` to trigger random events
- `TimeManager` to track passing time and schedules

### Interface Manager
- Handles switching between different UI modes
- Renders appropriate ASCII interfaces based on context
- Manages interaction commands specific to each mode
- Processes both text and click inputs

### Text Generation System
- Creates descriptive text for:
  - Room descriptions
  - Event narratives
  - System status reports
  - Personal observations

## 8. Key Challenges to Address

### Variety and Replayability
- Creating enough random events and system failures to prevent repetitive gameplay
- Developing interconnected systems where one failure can cascade to others in different ways
- Implementing varied narrative elements that unfold during transit

### Meaningful Progression
- Designing skill improvement that feels tangible and impacts gameplay
- Creating satisfaction from system optimization and maintenance mastery
- Balancing the learning curve so players feel challenged but not overwhelmed

### Environmental Immersion
- Making the confined ship space feel alive and dynamic through rich text descriptions
- Creating distinct "personalities" for different ship systems
- Developing atmospheric elements like subtle sounds, vibrations, or lighting changes

### Interface Design
- Ensuring contextual interfaces are intuitive but distinctive
- Balancing information density with readability in ASCII displays
- Making interface transitions feel natural and immersive

### Gameplay Balance
- Creating tension without excessive punitive mechanics
- Balancing time constraints to create pressure without frustration
- Ensuring maintenance tasks feel purposeful rather than busywork

### Narrative Integration
- Weaving personal storylines into the mechanical gameplay
- Creating a sense of purpose beyond just system maintenance
- Developing a background narrative that unfolds through logs, messages, or dreams

### Technical Implementation
- Building a robust time management system that handles events and degradation
- Creating modular systems that interact in complex but predictable ways
- Implementing an event system with sufficient variety and balance

### Feedback Systems
- Providing clear visual/textual feedback when systems improve or degrade
- Creating satisfying "success states" for well-maintained systems
- Developing subtle cues for impending issues before they become critical

### Long-term Engagement
- Ensuring the core loop remains satisfying over extended play
- Creating "mastery goals" beyond basic system maintenance
- Developing discoverable aspects of gameplay that reward experimentation

### Expandability
- Designing systems with hooks for future expansion
- Maintaining clean separation between core mechanics and content
- Structuring the code to allow for LLM-generated content modules

## 9. Success Criteria for MVP

- Complete a single delivery journey with engaging maintenance gameplay
- Player feels immersed in ship environment
- Interface switching feels natural and contextual
- Ship systems are interconnected enough to create interesting decisions
- Time management creates meaningful tension
- Player can develop mastery and optimization strategies
- Both text commands and clickable elements feel responsive and intuitive