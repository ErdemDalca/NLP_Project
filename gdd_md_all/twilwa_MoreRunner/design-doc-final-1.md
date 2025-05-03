# End of Line
## Comprehensive Game Design Document

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Game Concept](#game-concept)
3. [Faction Design](#faction-design)
4. [Core Systems](#core-systems)
5. [Gameplay Loops](#gameplay-loops)
6. [Technical Architecture](#technical-architecture)
7. [Art Direction](#art-direction)
8. [Development Roadmap](#development-roadmap)
9. [Appendices](#appendices)

---

## Executive Summary

**Game Name**: End of Line

**High Concept**: End of Line is a multiplayer roguelike deckbuilder-RPG hybrid featuring asymmetric gameplay between Corporation and Runner factions. Players compete to control territory in a cyberpunk world through strategic card play, stealth, hacking, and resource management, with persistent character progression across sessions.

**Key Selling Points**:
- Two interconnected card systems: strategic overworld territory control and tactical instanced missions
- Asymmetric gameplay with corps as "commanders" and runners as "soldiers"
- Dynamic territory control affecting the evolving game world
- Persistent character progression and deck building with roguelike elements
- Procedurally generated environments for endless replayability
- Multiple runners can form parties for cooperative mission play

**Target Audience**: 
- Primary: Fans of strategic card games (Netrunner, Magic: The Gathering)
- Secondary: Cyberpunk enthusiasts, RPG players, roguelike fans
- Tertiary: Strategy gamers who enjoy asymmetric gameplay and territory control

**Unique Value Proposition**: End of Line combines the deep strategic gameplay of Netrunner's asymmetric design with the persistent world control of territory-based games and the character progression of RPGs. The dual card systems—one for city-level strategy and one for mission-level tactics—provide a unique layered gameplay experience that rewards both long-term planning and tactical excellence.

---

## Game Concept

### Setting

End of Line takes place in CyberCity, a sprawling metropolis dominated by megacorporations that control all aspects of digital infrastructure, resource distribution, and public life. In the shadows of these corporate monoliths operate the Runners—hackers, outcasts, and digital revolutionaries seeking to expose corruption, steal valuable data, and disrupt corporate control.

The game world exists across two interconnected layers:
- **Physical Territory (Real World)**: Controlled primarily by Corporations, containing physical infrastructure and assets
- **Digital Networks (Cyberspace)**: Where Runners have the advantage, a more volatile and dynamic environment

### Core Experience

Players choose their faction alignment (Corporation or Runner) and navigate both the physical and digital landscapes of CyberCity. 

- **Corporation players** function as "commanders," focusing on strategic territory control, resource management, deployment of assets, and advancing agendas. They shape the environment that runners must navigate and can interact with runner missions, though typically in more limited and asynchronous ways.

- **Runner players** function as "soldiers," engaging directly in tactical missions, hacking, and infiltration. Multiple runners can form parties to tackle particularly challenging objectives, combining their specialized skills and deck strategies.

The game's dual card systems interact constantly—overworld events trigger mission opportunities, while mission outcomes reshape the overworld, creating a dynamic, evolving gameplay experience.

### Game Sessions

End of Line supports multiple game session types:
- **Quick Play** (15-30 minutes): Single-objective missions with focused gameplay
- **Campaign Mode**: Connected missions with persistent effects on the city, creating emergent narrative based on the changing "board state" of the overworld grid
- **Sandbox Mode**: Open exploration and experimentation within the systems

### Narrative Themes

- Corporate power vs. individual freedom
- Digital identity and consciousness
- Technological dependence and its consequences
- Class struggle in a hyper-capitalist future
- The blurred line between human and machine

### Key Player Activities

1. **Strategic Territory Control**: Corp players build and defend infrastructure while runners subvert and sabotage, changing the city's power dynamics
2. **Deck Construction**: Build and evolve specialized card decks for both overworld strategy and mission tactics
3. **Resource Management**: Balance limited resources across competing priorities
4. **Character Development**: Progress through specialized paths that enhance faction-specific abilities
5. **Mission Execution**: Deploy tactics in isometric instanced missions with specialized card play
6. **Market Acquisition**: Acquire new cards through a dynamic market system that evolves based on territory control

---

## Faction Design

End of Line features deeply asymmetric gameplay between two main faction types, each with distinct sub-factions that offer unique playstyles, aesthetics, and strategic approaches.

### Corporation Factions

Corporations function as "commanders" in the game, focusing on strategic control of territory, resource development, and agenda advancement. They shape the environment that runners must navigate, setting up the challenges and obstacles that define the game world.

#### Haas-Bioroid
- **Color Scheme**: Blue/Gray (#4D7B94, #78A1BB, #EBF5EE)
- **Aesthetic**: Clinical, efficient, artificial humanity
- **Philosophy**: "Human ingenuity improved upon by machine precision."
- **Opposition**: Flexible, adapts against all runner types
- **Role**: Hybrid faction that can function as both commander and soldier
- **Mechanics**: 
  - Deploy bioroid NPCs that function like runner characters but serve corporate interests
  - Enhanced recursion capabilities (reusing trashed cards)
  - Click efficiency (extra actions per turn)
  - Direct participation in instanced missions through android proxies
- **Weaknesses**:
  - Higher operational costs
  - Dependence on synergistic combinations
  - Vulnerabilities in specialized breakers

#### Jinteki
- **Color Scheme**: Red/Purple (#8A1A4B, #BB4575, #FFD6E5)
- **Aesthetic**: Traditional yet futuristic, elegant, deceptive
- **Philosophy**: "Every action you take is one we anticipated."
- **Opposition**: Criminal
- **Role**: Commander (strategic deception and trap-setting)
- **Mechanics**:
  - Powerful ambush/trap cards in both overworld and instances
  - Misdirection abilities to hide server contents
  - Net damage effects causing brain damage to runners
  - Ability to manipulate mission parameters mid-run
- **Weaknesses**:
  - Limited economy options
  - Resource-intensive operations
  - Reliance on Runner mistakes

#### NBN
- **Color Scheme**: Yellow (#F8CB3C, #FFDD55, #FFF5D6)
- **Aesthetic**: Bright, attention-grabbing, always-on, reality TV
- **Philosophy**: "Someone is always watching. Make sure they're watching what we want."
- **Opposition**: Shaper
- **Role**: Commander (information control and surveillance)
- **Mechanics**:
  - Enhanced tagging capabilities
  - Tag punishment effects
  - Media cycle cards with fluctuating effectiveness
  - Ability to gather intelligence on runner activities
- **Weaknesses**:
  - Weaker ICE strength
  - Tag removal countermeasures
  - Infrastructure vulnerabilities

#### Weyland Consortium
- **Color Scheme**: Black/Green (#1D361D, #3A563A, #D8E1E9)
- **Aesthetic**: Industrial, brutalist, practical, overwhelming force
- **Philosophy**: "What stands in our way will be removed."
- **Opposition**: Anarch
- **Role**: Commander (brute force and retaliation)
- **Mechanics**:
  - Enhanced agenda advancement
  - Powerful retaliation for successful runs
  - Superior resource generation and territory control
  - Ability to inflict meat damage on runners in the physical world
- **Weaknesses**:
  - Less subtlety in operations
  - Public relations vulnerabilities (Bad PR instead of tags)
  - More predictable strategies

### Runner Factions

Runners function as "soldiers" in the game, focusing on tactical execution of missions, direct engagement with corporate assets, and subverting the strategic landscape created by corporations. They can form parties to tackle particularly challenging objectives.

#### Criminal (Blue)
- **Color Scheme**: Blue tones (#0A5EB0, #2994E6, #D8E1E9)
- **Aesthetic**: Sleek, professional, urbane, high-tech but subtle
- **Philosophy**: "Why use the front door when the back door is open?"
- **Opposition**: Jinteki
- **Progression Paths**:
  - **Face → Infiltrator**: Specializing in stealth and social engineering
  - **Face → Fixer**: Specializing in connections and resource management
- **Mechanics**:
  - Enhanced credit generation (150% of base rate)
  - Connection networks providing information and bypass options
  - Special black market equipment access at reduced costs
  - Evasion abilities to avoid security systems
- **Special Abilities**:
  - **Silver Tongue**: Retry failed social checks once per mission
  - **Ghost**: Temporarily disappear from security view
  - **Bank Run**: Signature card that provides massive economic advantage at risk of being tagged
- **Weaknesses**:
  - Tag vulnerability increases trace strength
  - Tag penalties more severe (loss of connection cards)
  - Inefficient at direct confrontation
- **Signature Cards**:
  - "Inside Job" - Bypass the first piece of ICE encountered during a run
  - "Security Testing" - Gain credits from successful runs on specific servers
  - "Emergency Shutdown" - Derez a piece of ICE that was encountered this turn

#### Anarch (Red)
- **Color Scheme**: Red/orange tones (#D02D24, #F77F00, #FCBF49)
- **Aesthetic**: Raw, chaotic, DIY, jury-rigged technology
- **Philosophy**: "The system is broken. Break it more."
- **Opposition**: Weyland
- **Progression Paths**:
  - **Renegade → Gutterpunk**: Specializing in physical confrontation and "front door" approaches
  - **Renegade → Hacker**: Specializing in viruses and digital sabotage
- **Mechanics**:
  - Virus programs that strengthen over time
  - Destructive icebreakers breaking ICE efficiently but causing damage
  - Abilities generating chaos and random beneficial effects
  - Strength in disadvantaged positions
- **Special Abilities**:
  - **Wrecker**: Destroy obstacles that would normally be impassable
  - **Viral Propagation**: Virus counters grow faster
  - **Riot Starter**: Can trigger civil unrest in territories, increasing danger but disabling surveillance
- **Weaknesses**:
  - Self-damage from powerful effects
  - Less predictable outcomes
  - Risk of system crashes and collateral damage
- **Signature Cards**:
  - "Immolation" - Trash a program to destroy a piece of ICE
  - "Scrubber" - Reduce the cost of trashing cards
  - "Hivemind" - Share virus counters between programs

#### Shaper (Green)
- **Color Scheme**: Green tones (#0CA75D, #57D9A3, #EBF5EE)
- **Aesthetic**: Organic meets technical, elegant solutions, community
- **Philosophy**: "The right tool for the right job. If it doesn't exist, build it."
- **Opposition**: NBN
- **Progression Paths**:
  - **Builder → Engineer**: Specializing in physical tech and cloud architectures (powerful but slow)
  - **Builder → Wunderkind**: Specializing in jury rigs and modifications (quick and dirty solutions)
- **Mechanics**:
  - Increased memory limit for programs
  - Ability to reconfigure installed programs during runs
  - Resource generation from Community Support
  - Custom hardware modifications
- **Special Abilities**:
  - **Modding**: Improve hardware mid-run
  - **Overclock**: Temporarily boost program strength
  - **Maker Spirit**: Install programs at reduced cost
- **Weaknesses**:
  - Setup time requirements
  - Resource intensive specializations
  - Vulnerability to direct damage
- **Signature Cards**:
  - "Test Run" - Install a program directly from the stack
  - "Personal Workshop" - Install programs gradually over time
  - "Self-Modifying Code" - Search for and install a program during a run

### Faction Interactions and Balance

The factions in End of Line interact through both direct confrontation and strategic positioning on the overworld map:

- **Faction Oppositions**: Each Corporation sub-faction has a natural opposition among the Runner sub-factions, creating dynamic matchups:
  - **Haas-Bioroid ↔ All Runners**: As a hybrid faction, adapts to counter all runner types
  - **Jinteki ↔ Criminal**: Deception vs. subtlety, traps vs. bypasses
  - **NBN ↔ Shaper**: Information control vs. innovation, media vs. tech community
  - **Weyland ↔ Anarch**: Brute force vs. chaos, corporate muscle vs. disruptive tactics

- **Territory-Based Interactions**:
  - Controlling adjacent territories creates border conflicts
  - Faction-controlled territories generate faction-specific resources
  - Runner activities in corporate territories can trigger corporate responses
  - Corporate initiatives can affect runner safe havens

- **Event-Based Interactions**:
  - Anarch players can burn resources to start riots, increasing physical danger but disabling surveillance
  - Criminal players benefit from city volatility, gaining economic advantages during unrest
  - Shaper players can establish community networks, providing territory-wide benefits to runners
  - Corps can initiate coordinated responses to runner activities

- **Balance Mechanisms**:
  - Asymmetric victory conditions and resource curves
  - Risk/reward trade-offs for powerful abilities
  - Counter-play options for each strategy
  - Dynamic difficulty scaling through territory control shifts
  - Multi-runner parties can balance against powerful corporate setups

---

## Core Systems

### Dual Card Systems

End of Line features two interconnected but distinct card systems that operate at different levels of gameplay:

#### Overworld Card System (Strategic Layer)

The overworld card system governs the strategic city-level gameplay, focusing on territory control, resource development, and long-term planning.

- **Card Types**:
  - **Corporate Infrastructure**: Permanent installations that generate resources or provide ongoing effects
  - **Security Assets**: Defensive structures and personnel that protect territories
  - **Operations**: One-time strategic actions that affect multiple territories
  - **Agendas**: Long-term plans that provide victory points and special abilities when advanced
  - **Runner Networks**: Permanent underground connections and safe houses
  - **Runner Resources**: Ongoing effects that provide strategic advantages
  - **Runner Events**: One-time citywide actions or reactions

- **Deck Construction Rules**:
  - Corporation Overworld Decks: 40-60 cards, 15-20 influence points
  - Runner Overworld Decks: 30-45 cards, 10-15 influence points
  - Faction-specific card limitations
  - Agenda density requirements for corporation decks

- **Play Pattern**:
  - Turn-based strategic play on the city grid
  - Resource investment and allocation
  - Territory development and control
  - Event resolution and responses
  - Agendas advanced or subverted

#### Instanced Mission Card System (Tactical Layer)

The instanced mission system represents the moment-to-moment tactical gameplay during specific runner operations or corporate defense scenarios.

- **Card Types**:
  - **Corporation ICE**: Defensive barriers protecting servers and assets
  - **Corporate Assets**: In-server resources and traps
  - **Corporate Operations**: Tactical responses to runner activity
  - **Runner Hardware**: Physical equipment and tools
  - **Runner Programs**: Software for breaking ICE and manipulating systems
  - **Runner Resources**: Tactical advantages and connections
  - **Runner Events**: One-time tactical actions during a run

- **Deck Construction Rules**:
  - Runner Mission Decks: 35-50 cards, 10-15 influence points
  - Corporation Mission Decks: 40-55 cards, 10-15 influence points
  - Deck size can be traded off for more powerful identity abilities

- **Play Pattern**:
  - Real-time tactical gameplay in isometric view
  - Card drawing and hand management during mission
  - Program installation and activation
  - ICE breaching and server access
  - Multiple runners can coordinate card play in party missions

#### System Interplay and Dependencies

The two card systems interact constantly, with outcomes in one affecting the state and possibilities in the other:

- **Overworld → Instanced**:
  - Territory control determines available server types and security levels
  - Corporate installations define ICE types and strength
  - Runner networks provide access points and resources
  - Ongoing events modify mission parameters and available options

- **Instanced → Overworld**:
  - Successful runs can subvert corporate agendas
  - Discovered information changes territorial control dynamics
  - Stolen resources can be deployed on the overworld
  - Critical breaches can trigger citywide events

- **Trigger Points**:
  - Completed narrative instances
  - Uncontested corporate agendas
  - Side mission outcomes
  - Stolen and flipped runner agendas
  - Critical territory state changes

#### Card Acquisition and Market System

Cards are acquired through a dynamic market system that evolves based on game state:

- **Non-Static Market**:
  - Available cards rotate based on territory control
  - Resources spent to acquire cards from the market
  - Market refreshes when certain conditions are met
  - Faction influence affects card availability

- **Acquisition Methods**:
  - Mission rewards and successful runs
  - Territory control bonuses
  - Reputation with factions
  - Crafting/upgrading systems
  - Limited-time events and opportunities

- **Card Evolution**:
  - Cards can be upgraded through repeated use
  - Specialization paths affect card modifications
  - Territory-specific variants can be discovered
  - Meta-progression unlocks enhanced versions

### Territory Control System

The territory control system creates a strategic meta-game layer that affects resource generation, mission availability, and gameplay advantages.

#### Territory Structure

- CyberCity is divided into a hex grid of 24 distinct territories
- Each territory has attributes:
  - Corporate Influence (0-100%)
  - Security Level (1-5)
  - Resource Value (1-5)
  - Stability Index (0-100%)
  - Population (1-5)

#### Territory Types

1. **Corporate Zones**:
   - High corporate influence (70%+)
   - High security level (4-5)
   - Moderate resource value (3)
   - Examples: Corporate HQ, Research Campus, Manufacturing Zone

2. **Fringe Zones**:
   - Moderate corporate influence (30-70%)
   - Moderate security level (2-3)
   - Moderate resource value (2-3)
   - Examples: Commercial Districts, Tech Parks, Residential Areas

3. **Underground Zones**:
   - Low corporate influence (<30%)
   - Low security level (1-2)
   - High resource value (4-5)
   - Examples: Black Markets, Hacker Dens, Abandoned Infrastructure

#### Control Mechanisms

1. **Corporation Control Methods**:
   - Playing infrastructure cards to establish permanent presence
   - Deploying security assets to increase defense
   - Advancing agendas to lock in control
   - Installing surveillance systems to detect runner activity

2. **Runner Control Methods**:
   - Establishing network connections between territories
   - Creating safe houses and underground facilities
   - Disrupting corporate infrastructure
   - Flipping corporate agendas to runner benefit

3. **Card-Based Control Dynamics**:
   - Infrastructure and network cards provide control points
   - Event cards can shift control temporarily or permanently
   - Control points decay over time without maintenance cards
   - Contested territories enable special card effects

4. **Dynamic Events**:
   - Anarch players can burn resources to start riots
   - Corporate players can initiate security crackdowns
   - Natural disasters or city events can affect multiple territories
   - Media campaigns can shift public opinion and territory stability

#### Strategic Benefits of Territory Control

1. **Resource Generation**:
   - Credits based on territory resource value
   - Data tokens based on security level
   - Influence based on population and stability
   - Special resources tied to territory type

2. **Mission Opportunities**:
   - Controlled territories unlock specific mission types
   - Adjacent controlled territories enable multi-territory operations
   - Territory configurations can trigger special narrative missions
   - Control thresholds unlock powerful mission options

3. **Card Availability**:
   - Territory control affects market card pools
   - Specialized cards only available in certain territories
   - Increased draw or resource options in controlled territories
   - Upgraded card versions in fully controlled territories

4. **Faction-Specific Benefits**:
   - Weyland gains enhanced resource generation in industrial zones
   - NBN gains enhanced surveillance in residential areas
   - Jinteki gains enhanced trap effectiveness in research zones
   - Haas-Bioroid gains enhanced bioroid deployment in commercial zones
   - Runners gain faction-specific advantages in underground zones

#### Territory Events and Evolution

Territories evolve based on player actions and global events:

- **Player-Triggered Events**:
  - Anarch riots increase physical danger but disable surveillance
  - Criminal operations boost black market resources
  - Shaper community networks provide shared benefits
  - Corporate initiatives reshape territory attributes

- **Automated Evolution**:
  - Security Responses: Increased corporate security after successful Runner operations
  - Public Opinion Shifts: Population response to faction actions
  - Infrastructure Development: New assets becoming available
  - Environmental Hazards: Random events affecting territory availability

- **Narrative Consequences**:
  - Long-term territory control shifts affect city storyline
  - Critical mission outcomes permanently alter territories
  - Threshold control percentages trigger major story events
  - Secret agenda completion can transform territory types

### Procedural Generation

The procedural generation system creates diverse and replayable environments for both the overworld and instanced missions.

#### Generation Approaches

1. **Overworld Generation**:
   - Initial city layout with predefined faction strongholds
   - Randomized territory attributes and connections
   - Procedural assignment of territory types and resources
   - Balanced faction starting positions

2. **Instanced Mission Generation**:
   - Server layouts based on corporation and security level
- Dynamic ICE placement and strength
   - Procedural trap and asset distribution
   - Multiple path options based on runner capabilities
   - Environmental variations based on corporation and territory type

#### Environment Diversity and Variability

1. **Overworld Environments**:
   - Corporate districts with unique architectural styles
   - Underground networks with faction-specific aesthetics
   - Dynamic weather and lighting conditions
   - Evolving cityscape based on faction control

2. **Instanced Mission Environments**:
   - Server architectures reflecting corporation identity
   - Physical spaces with corporation-specific security measures
   - Variable connection points between physical and digital spaces
   - Environmental hazards tied to territory conditions

#### Difficulty Scaling and Content Generation

1. **Adaptive Difficulty**:
   - Security levels scale with player progression
   - Dynamic adjustment based on party size and composition
   - Corporate response intensity tied to runner success rate
   - Specialized challenges based on runner abilities

2. **Content Diversity Mechanisms**:
   - Server template system with modular components
   - Encounter tables tied to territory types
   - Faction-specific challenge sets
   - Narrative-driven special conditions

### Encounter System

The encounter system manages player interactions and combat during both overworld and instanced gameplay.

#### Multiplayer Runner Party Dynamics

1. **Party Formation**:
   - Multiple runners can join the same instanced mission
   - Complementary skill sets and deck strategies
   - Shared rewards with individual bonuses
   - Role specialization (breaker, support, resource generation)

2. **Coordination Mechanics**:
   - Shared vision and information
   - Ability to transfer resources and cards
   - Combo effects from multiple runner abilities
   - Position-based tactical advantages

3. **Party Size Scaling**:
   - Increased ICE strength and server complexity
   - Enhanced reward potential
   - More complex objectives and challenges
   - Additional escape routes and access points

#### Corporation Direct Interaction Options

1. **Haas-Bioroid Direct Control**:
   - Deploy and control bioroid NPCs during runner missions
   - Counter-hacking options during digital encounters
   - Direct upgrades to ICE and security systems mid-mission
   - Ability to reconfigure server layout

2. **Asynchronous Corporation Responses**:
   - Pre-set trap and response cards
   - AI-driven security system responses
   - Automated defense protocols
   - Alert level escalation mechanics

3. **Real-time Notification System**:
   - Corporation players receive alerts about runner activity
   - Option to deploy emergency response assets
   - Limited direct intervention opportunities
   - Resource allocation decisions during active runs

#### Encounter Types and Scenarios

1. **Corporation vs. Runner (Asymmetric)**:
   - Digital runs on corporate servers
   - Physical infiltration of secure facilities
   - Social engineering and corporate espionage
   - Theft and sabotage operations

2. **Corporation vs. Corporation (Symmetric)**:
   - Territory disputes and economic warfare
   - Competitive agenda advancement
   - Proxy conflicts using hired runners
   - Resource denial operations

3. **Runner vs. Runner (Symmetric)**:
   - Racing to hack objectives first
   - Territory influence competition
   - Resource competition
   - Reputation challenges

4. **PvE Encounters**:
   - AI-controlled corporate security
   - Automated defense systems
   - Rogue AI entities
   - Third-party threats (government, rival organizations)

#### Resolution Mechanics and Rewards

1. **Success Conditions**:
   - Data theft objectives
   - Server breach and access
   - Asset destruction or sabotage
   - Agenda manipulation

2. **Failure Conditions**:
   - Character damage thresholds
   - Trace detection and identification
   - Time limits and security escalation
   - Resource depletion

3. **Reward Structures**:
   - Credits and resources
   - Reputation with factions
   - Unique cards and upgrades
   - Territory influence points
   - Experience for character progression

4. **Failure Consequences**:
   - Character damage or retirement
   - Resource losses
   - Decreased territory influence
   - Reputation penalties
   - Increased security in the territory

### Meta-Progression System

The meta-progression system provides persistent advancement outside of individual missions and game sessions, creating long-term engagement and strategic depth.

#### Character Development and Specialization

1. **Runner Progression Paths**:
   - Criminal: Face → Infiltrator or Fixer
   - Anarch: Renegade → Gutterpunk or Hacker
   - Shaper: Builder → Engineer or Wunderkind

2. **Corporation Progression**:
   - Division specializations within each corp
   - Executive advancement tracks
   - Research and development priorities
   - Security protocol advancements

3. **Specialization Benefits**:
   - Unique ability unlocks
   - Exclusive card access
   - Enhanced resource generation
   - Special mission opportunities

4. **Development Mechanics**:
   - Experience points from successful actions
   - Skill trees with specialization paths
   - Achievement-based unlocks
   - Challenge completion milestones

#### Faction Loyalty and Reputation

1. **Faction Standing System**:
   - Reputation tracks with all factions
   - Standing affects card availability and costs
   - Faction-specific mission opportunities
   - Reputation thresholds unlock special abilities

2. **Loyalty Rewards**:
   - Unique cards for faction loyalty
   - Enhanced resource generation from faction territories
   - Special abilities when operating in faction territories
   - Discounted card acquisition from loyal factions

3. **Cross-faction Dynamics**:
   - Reputation penalties for opposing faction actions
   - Opportunity costs for multi-faction operations
   - Diminishing returns on split loyalty
   - Faction-specific challenge missions

#### Persistence Across Runs

1. **Roguelike Progression**:
   - Character death or retirement is possible in runs
   - Meta-progression persists across character iterations
   - Earned cards remain in collection
   - Faction reputation remains largely intact

2. **Knowledge Persistence**:
   - Discovered server layouts remain logged
   - Known ICE configurations are saved
   - Corporation tendencies are tracked
   - Territory knowledge accumulates

3. **Resource Management**:
   - Strategic resource allocation between runs
   - Investment in territories and infrastructure
   - Banking and savings mechanisms
   - Resource decay or maintenance costs

#### Unlockable Content and Abilities

1. **Card Pool Expansion**:
   - Higher rarity cards unlock through progression
   - Specialized versions of existing cards
   - Faction-specific premium cards
   - Cross-faction hybrid cards at high levels

2. **Ability Unlocks**:
   - Enhanced base actions (additional clicks, higher starting resources)
   - Special movement or access abilities
   - Economic advantages and efficiencies
   - Unique interaction options with the environment

3. **Territory Development**:
   - Advanced infrastructure options
   - Enhanced territory defense capabilities
   - Special territory attributes and bonuses
   - Secret research and development facilities

4. **Narrative Development**:
   - Story mission unlocks based on progression
   - Character relationship development
   - Faction storyline advancement
   - City evolution and transformation

### Economy & Resource Management

The economy system governs resource generation, acquisition, and allocation, creating meaningful strategic choices for players.

#### Resource Types and Generation

1. **Primary Resources**:
   - Credits: Universal currency used for most transactions
   - Data Tokens: Specialized currency for digital operations
   - Influence: Used for political and social actions
   - Memory Units: Limits program installation for runners

2. **Faction-Specific Resources**:
   - Weyland: Construction Materials and Security Contracts
   - NBN: Media Influence and Viewer Metrics
   - Jinteki: Research Data and Clone Development
   - Haas-Bioroid: Manufacturing Capacity and Bioroid Units
   - Runner Factions: Specialized hacking tools and underground connections

3. **Generation Methods**:
   - Passive generation from controlled territories
   - One-time gains from card effects
   - Mission and run rewards
   - Special events and opportunities

#### Card Economy and Market System

1. **Dynamic Card Market**:
   - Available cards rotate based on game state
   - Territory control affects available card pools
   - Faction influence impacts card costs
   - Limited-time special card offerings

2. **Acquisition Costs**:
   - Credit costs for purchasing cards
   - Influence costs for out-of-faction cards
   - Installation and usage costs
   - Maintenance costs for persistent effects

3. **Market Mechanics**:
   - Market refresh conditions (time, actions, events)
   - Card rarity distribution algorithms
   - Territory-specific market variants
   - Black market and underground economy for runners

#### Investment and Speculation

1. **Territory Investment**:
   - Infrastructure development increases yield
   - Security investment protects assets
   - Research and development investments unlock new options
   - Long-term vs. short-term investment strategies

2. **Card Investment**:
   - Card upgrading and customization
   - Investing in specific deck strategies
   - Card synergy development
   - Adaptation to meta-game shifts

3. **Risk Management**:
   - Asset protection strategies
   - Diversification of investments
   - Insurance and backup systems
   - Redundancy planning

#### Faction-Specific Economic Advantages

1. **Corporation Economies**:
   - Weyland: Resource exploitation and construction efficiency
   - NBN: Information monetization and market manipulation
   - Jinteki: Research patents and clone workforce
   - Haas-Bioroid: Manufacturing efficiency and bioroid labor

2. **Runner Economies**:
   - Criminal: Enhanced credit generation and black market access
   - Anarch: Resource reclamation and system exploitation
   - Shaper: Efficient hardware and community support

3. **Economic Warfare**:
   - Account siphoning and fund diversion
   - Resource denial operations
   - Market manipulation tactics
   - Supply chain disruption

---

## Gameplay Loops

### Tactical Loop (Instanced Missions)

The tactical gameplay loop focuses on moment-to-moment decisions during instanced missions, primarily from the runner perspective but with corporate interaction points.

#### Card Play and Decision Points

1. **Runner Turn Structure**:
   - Resource allocation phase
   - Movement and positioning
   - Card installation and activation
   - Server interaction and ICE breaching
   - Special ability usage

2. **Decision Types**:
   - Path selection through servers
   - Resource allocation between programs
   - Risk assessment for runs
   - Timing of special abilities
   - Reaction to corporate responses

3. **Card Usage Patterns**:
   - Program installation strategy
   - Event card timing for maximum impact
   - Resource card development
   - Hardware configuration optimization

#### Runner Party Coordination

1. **Role Specialization**:
   - Breaker specialists focus on ICE interaction
   - Support runners provide resources and buffs
   - Tank runners absorb damage and distract security
   - Scout runners gather intelligence and expose threats

2. **Resource Sharing**:
   - Credit transfers between runners
   - Shared program usage
   - Tag clearing assistance
   - Damage distribution tactics

3. **Coordinated Actions**:
   - Synchronized server approaches
   - Distraction and main thrust tactics
   - Redundant breaker coverage
   - Recovery and rescue operations

#### Corporation Direct Interaction (Haas-Bioroid)

1. **Bioroid Deployment**:
   - Controlling android NPCs during runner missions
   - Direct opposition to runner actions
   - Security system manipulation
   - Asset protection and server reconfiguration

2. **Other Corporation Interactions**:
   - Pre-set trap activation
   - Security response card play
   - ICE strength boosting
   - Server reconfiguration within limits

3. **Resource Allocation**:
   - Credit spending to enhance defenses
   - Emergency protocol activation
   - Rerouting security forces
   - Asset sacrifice decisions

#### Mission Success Conditions and Outcomes

1. **Objective Types**:
   - Data theft and extraction
   - System sabotage
   - Asset destruction
   - Intelligence gathering
   - Corporate infiltration

2. **Success Rewards**:
   - Card rewards based on mission type
   - Credit and resource bonuses
   - Experience for character advancement
   - Territory influence changes

3. **Failure Consequences**:
   - Character damage or retirement
   - Resource and card losses
   - Territory control penalties
   - Increased difficulty in future missions

### Strategic Loop (Overworld)

The strategic gameplay loop focuses on territory control, resource development, and long-term planning on the citywide map.

#### Territory Management and Control

1. **Corporation Territory Strategy**:
   - Infrastructure development for resource generation
   - Security deployment for defense
   - Server installation for agenda advancement
   - Territory connection for synergy bonuses

2. **Runner Territory Strategy**:
   - Network establishment between territories
   - Safe house creation for resource generation
   - Access point development for mission opportunities
   - Territory disruption to weaken corporate control

3. **Control Mechanics**:
   - Infrastructure and network cards for control points
   - Control decay over time without maintenance
   - Contested territory dynamics
   - Control threshold benefits at different percentages

#### Resource Allocation and Development

1. **Resource Investment Decisions**:
   - Territory development vs. card acquisition
   - Security investment vs. expansion
   - Short-term gains vs. long-term development
   - Offensive vs. defensive resource allocation

2. **Development Strategies**:
   - Specialized territory clusters
   - Connected territory networks
   - Balanced development approaches
   - Rush strategies for specific territories

3. **Economy Management**:
   - Credit generation optimization
   - Resource type conversion
   - Maintenance cost management
   - Investment in future capabilities

#### Event Triggering and Response

1. **Player-Initiated Events**:
   - Anarch riots and disruption
   - Corporate security crackdowns
   - Media campaigns and public relations
   - Black market operations and underground activities

2. **System-Generated Events**:
   - Random city occurrences
   - Environmental changes and disasters
   - Third-party faction activities
   - Global political and economic shifts

3. **Response Options**:
   - Event card play for mitigation or enhancement
   - Resource allocation to affected territories
   - Tactical mission opportunities
   - Strategic repositioning based on event outcomes

#### Agenda Advancement and Subversion

1. **Corporation Agenda Mechanics**:
   - Agenda installation in protected servers
   - Advancement using actions and resources
   - Scoring conditions and victory points
   - Special abilities upon completion

2. **Runner Subversion Mechanics**:
   - Agenda theft through successful runs
   - Flipping agendas to runner benefit
   - Counter-agenda operations
   - Denial strategies to prevent scoring

3. **Agenda Effects on Gameplay**:
   - Territory control modifiers
   - Resource generation bonuses
   - Special ability unlocks
   - Narrative progression triggers

### Interplay Loop

The interplay loop describes how the tactical (instanced) and strategic (overworld) gameplay systems interact with and influence each other.

#### How Mission Outcomes Affect Overworld

1. **Territory Control Impact**:
   - Successful runs decrease corporate control in territories
   - Failed runs can increase corporate control
   - Critical successes can flip territories to runner influence
   - Server breaches can disable corporate infrastructure

2. **Resource Effects**:
   - Stolen assets provide resources on the overworld
   - Destroyed infrastructure reduces corporate income
   - Revealed information changes market dynamics
   - Successful runs unlock new card options

3. **Narrative Consequences**:
   - Story progression based on key mission outcomes
   - NPC relationship changes
   - Faction reputation shifts
   - City evolution based on major events

#### How Overworld State Determines Mission Parameters

1. **Mission Generation**:
   - Territory control level determines security difficulty
   - Corporate infrastructure defines available server types
   - Runner networks provide access point options
   - Territory stability affects environmental conditions

2. **Available Resources**:
   - Control level determines starting resources
   - Territory type affects available support options
   - Connection networks enable backup and escape routes
   - Faction presence provides specialized assistance

3. **Opposition Strength**:
   - Security level determines ICE strength and quantity
   - Corporate presence affects response intensity
   - Previously successful runs increase security
   - Territory adjacency enables reinforcement options

#### Trigger Points and State Changes

1. **Critical Mission Outcomes**:
   - Agenda theft or scoring
   - Infrastructure destruction
   - Key data theft
   - Character death or capture

2. **Territory Control Thresholds**:
   - 25%, 50%, and 75% control milestones
   - Full corporate lockdown or runner liberation
   - Contested territory volatility
   - Neutral territory opportunities

3. **Resource Accumulation Triggers**:
   - Investment thresholds for development
   - Critical resource shortages
   - Market saturation effects
   - Resource conversion opportunities

#### Narrative Evolution Through System Interaction

1. **Emergent Storytelling**:
   - City narrative evolves based on territory control
   - Character relationships develop through missions
   - Faction conflicts generate dynamic storylines
   - Personal character journeys through progression paths

2. **Structured Narrative Elements**:
   - Key story missions unlock based on conditions
   - Critical choice points affect future options
   - Faction storylines advance through specific actions
   - City evolution milestones based on overall state

3. **Dynamic World Response**:
   - NPC behavior adapts to player actions
   - Territory characteristics evolve based on control history
   - New factions or entities emerge based on power dynamics
   - Environmental changes reflect the consequences of actions

### Progression Loop

The progression loop defines how players advance their characters, decks, and strategic options over time.

#### Character Advancement Paths

1. **Runner Specialization**:
   - Criminal Face → Infiltrator (stealth, social engineering) or Fixer (connections, economic advantages)
   - Anarch Renegade → Gutterpunk (physical, direct approach) or Hacker (viruses, sabotage)
   - Shaper Builder → Engineer (physical tech, cloud) or Wunderkind (jury rigs, modifications)

2. **Corporation Advancement**:
   - Weyland: Resource focus vs. security focus
   - NBN: Information control vs. media influence
   - Jinteki: Research and development vs. deception
   - Haas-Bioroid: Manufacturing vs. bioroid development

3. **Advancement Mechanics**:
   - Experience point accumulation from actions
   - Skill tree unlocks with specialization nodes
   - Ability upgrades through usage
   - Challenge completion milestones

#### Deck Construction and Evolution

1. **Card Acquisition**:
   - Mission rewards for specific card types
   - Market purchases with resources
   - Reputation-based faction cards
   - Special event and challenge rewards

2. **Deck Strategy Development**:
   - Initial starter decks with basic options
   - Specialization into focused strategies
   - Counter-meta adaptations
   - Hybrid approaches for flexibility

3. **Card Customization**:
   - Card upgrading through resources
   - Modification slots and options
   - Specialization bonuses for character path
   - Set completion bonuses

#### Faction Development

1. **Reputation Mechanics**:
   - Standing increases through aligned actions
   - Reputation thresholds unlock benefits
   - Cross-faction reputation management
   - Specialization within faction sub-groups

2. **Faction Territory Development**:
   - Faction-controlled safe zones
   - Specialized infrastructure in aligned territories
   - Connection networks between faction territories
   - Narrative development in faction strongholds

3. **Faction Special Abilities**:
   - Unique powers unlocked at reputation tiers
   - Faction-specific card accessibility
   - Enhanced effectiveness in faction territories
   - Special mission opportunities

#### Meta-game Strategies

1. **Long-term Planning**:
   - Territory control strategies
   - Character development paths
   - Deck evolution roadmaps
   - Faction relationship management

2. **Adaptation Mechanics**:
   - Counter-strategy development
   - Resource allocation shifts
   - Specialization reorientation
   - Territory priority adjustments

3. **Community Interaction**:
   - Emerging meta tracking
   - Strategy sharing and discussion
   - Deck archetype development
   - Achievement and challenge community

---

## Technical Architecture

### System Architecture

The technical architecture for End of Line is designed for modularity, testability, and efficient browser-based deployment.

#### Entity-Component System + MVC Hybrid

1. **Entity-Component System Core**:
   - Entities represent game objects (cards, players, territories)
   - Components provide reusable behaviors and data
   - Systems operate on entity collections with specific components
   - Optimized for efficient state management and updates

2. **MVC Pattern Integration**:
   - Models: Data structures for game state
   - Views: UI components for player interaction
   - Controllers: Logic connecting models and views, handling player input
   - Clean separation of concerns for testability

3. **Service Layer**:
   - Global systems accessible throughout the codebase
   - Manages cross-cutting concerns (networking, persistence, logging)
   - Dependency injection for modular testing
   - Centralized configuration management

4. **Event Bus**:
   - Decoupled communication between systems
   - Publish-subscribe pattern for event handling
   - Replay capabilities for testing
   - Performance optimization for frequent events

#### Browser-based Implementation Considerations

1. **No Loading Screen Requirement**:
   - Progressive asset loading
   - Initial minimal download for core functionality
   - Background loading of additional assets
   - Efficient caching strategy

2. **No Sign-in Requirement**:
   - Anonymous session management
   - Local storage for game state persistence
   - Optional account linking for cross-device play
   - Guest mode with full functionality

3. **Browser Compatibility**:
   - Cross-browser testing and compatibility
   - Progressive enhancement for different capabilities
   - Responsive design for various screen sizes
   - Mobile browser considerations

#### Multiplayer State Management

1. **Client-Server Architecture**:
   - SpacetimeDB as the central server component
   - Client prediction for responsive gameplay
   - Server authority for game state validation
   - Efficient state synchronization

2. **Real-time Communication**:
   - WebSocket-based communication for instanced missions
   - REST API for non-time-critical operations
   - Binary protocol for efficient data transfer
   - Fallback mechanisms for connection issues

3. **Player Session Management**:
   - Connection tracking and recovery
   - Timeout and reconnection handling
   - State synchronization after disconnection
   - Graceful session termination

### Data Management

Efficient and reliable data management is crucial for the complex state tracking required by End of Line.

#### SpacetimeDB Integration

1. **Core Data Storage**:
   - Tables for persistent game entities
   - Relationships between game objects
   - Efficient queries for gameplay operations
   - Transaction management for consistency

2. **Real-time Synchronization**:
   - Subscription model for live updates
   - Delta compression for efficient transfers
   - Conflict resolution strategies
   - Event-based update propagation

3. **Authentication and Authorization**:
   - Player identity management
   - Session validation
   - Action permission checking
   - Secure data access controls

#### Cross-session Persistence

1. **Save State Management**:
   - Automatic state saving at key points
   - Manual save options for players
   - Versioned save states for rollback
   - Save compression for efficiency

2. **Character Persistence**:
   - Character state serialization
   - Progression data storage
   - Inventory and deck persistence
   - Cross-character shared progression

3. **World State Persistence**:
   - Territory control state
   - Infrastructure and network placement
   - Global event status
   - Narrative progression checkpoints

#### Data Flow Between Systems

1. **System Communication**:
   - Event-based data exchange between systems
   - Standardized data formats for interoperability
   - Clear ownership and responsibility boundaries
   - Explicit dependencies and interfaces

2. **Cache Management**:
   - Strategic caching of frequently accessed data
   - Invalidation strategies for changed data
   - Memory usage optimization
   - Performance profiling and tuning

3. **Error Handling and Recovery**:
   - Graceful degradation on data issues
   - Automatic recovery attempts
   - Data validation and sanitization
   - Logging and diagnostics for issues

### Development Methodology

The development process for End of Line embraces test-driven development and agile practices.

#### Test-Driven Development Process

1. **Testing Framework**:
   - Unit tests for core game rules
   - Integration tests for system interactions
   - UI testing for user interfaces
   - Performance testing for critical paths

2. **Coverage Goals**:
   - Core gameplay systems: 90%+ coverage
   - UI components: 80%+ coverage
   - Helper utilities: 70%+ coverage
   - Test quality metrics and maintenance

3. **Testing Approaches**:
   - Behavioral testing for game rules
   - Property-based testing for complex algorithms
   - Mock objects for dependencies
   - Snapshot testing for UI components

#### Red-to-Green Workflow

1. **Test-First Development**:
   - Write failing tests before implementation (Red)
   - Implement minimal code to pass tests (Green)
   - Refactor for cleanliness and maintainability
   - Document and iterate

2. **Continuous Integration**:
   - Automated test runs on commit
   - Build verification tests
   - Performance regression detection
   - Code quality metrics

3. **Documentation Integration**:
   - Test-driven documentation
   - Living specification through tests
   - API documentation generation
   - Design document maintenance

#### Playtesting Integration

1. **Playtesting Cadence**:
   - Regular internal playtesting sessions
   - Structured feedback collection
   - Metrics tracking for game balance
   - Feature validation through play

2. **Feedback Incorporation**:
   - Prioritization of playtest findings
   - Technical debt management
   - Refactoring based on gameplay insights
   - Balance adjustments from real play

3. **User Experience Iteration**:
   - Usability testing methodology
   - A/B testing for UI improvements
   - Accessibility testing and improvement
   - Performance optimization based on user feedback

#### Feature Prioritization

1. **Minimum Viable Playable**:
   - Core card system implementation
   - Basic territory control
   - Simple mission execution
   - Fundamental faction differences

2. **Iterative Enhancement**:
   - Feature prioritization based on gameplay impact
   - Technical feasibility assessment
   - User value evaluation
   - Development complexity estimation

3. **Feature Implementation Cycle**:
   - Design specification and test cases
   - Implementation and testing
   - Playtesting and refinement
   - Documentation and release

### Technology Stack

End of Line is built on a carefully selected technology stack optimized for browser-based gameplay.

#### Godot and Blender for Engine and Assets

1. **Godot Engine Core**:
   - Scene-based architecture
   - Built-in physics and animation
   - UI framework for game interfaces
   - Cross-platform compatibility

2. **Custom Godot Extensions**:
   - Card game specific components
   - Territory control visualization
   - Procedural generation systems
   - Networking enhancements

3. **Blender Asset Pipeline**:
   - 3D model creation and optimization
   - Animation development
   - Texture creation and management
   - Export automation for Godot integration

#### GodotJS and TypeScript for SDK

1. **TypeScript Implementation**:
   - Strong typing for code reliability
   - Interface-based design
   - Module organization for maintainability
   - Advanced type features for game state

2. **GodotJS Integration**:
   - WebGL rendering pipeline
   - JavaScript interoperability
   - DOM integration for UI elements
   - Performance optimization for web

3. **Development Tooling**:
   - TypeScript compiler configuration
   - ESLint for code quality
   - Jest for unit testing
   - Webpack for bundling

#### SpacetimeDB for Multiplayer

1. **Core SpacetimeDB Features**:
   - Real-time database synchronization
   - Event-driven architecture
   - Scalable infrastructure
   - Secure authentication

2. **Custom SpacetimeDB Implementation**:
   - Game-specific schema design
   - Optimized queries for game operations
   - Custom reducers for game logic
   - Efficient state synchronization

3. **Multiplayer Features**:
   - Player session management
   - Party system for runner teams
   - Matchmaking for PvP
   - Tournament and competition support

#### Browser-based Requirements

1. **Performance Optimization**:
   - Asset loading strategies
   - Memory management
   - Rendering optimization
   - Network traffic minimization

2. **Browser Compatibility**:
   - Feature detection and graceful degradation
   - Polyfills for cross-browser support
   - Touch and mouse input handling
   - Screen size adaptation

3. **Offline Capability**:
   - Service worker implementation
   - Local storage for game state
   - Synchronization on reconnection
   - Progressive Web App features

---

## Art Direction

### Visual Design

The visual design for End of Line establishes a distinctive cyberpunk aesthetic while providing clear gameplay information.

#### Overworld Map Style (SimCity-like)

1. **Isometric City Grid**:
   - Hex-based territory layout
   - Detailed building and infrastructure models
   - Faction-influenced architectural styles
   - Day/night cycle and weather effects

2. **Control Visualization**:
   - Color overlays representing faction control
   - Intensity gradients showing control percentages
   - Infrastructure and network connection visualization
   - Activity and security level indicators

3. **Information Clarity**:
   - Territory type iconography
   - Resource generation visualizations
   - Status effect indicators
   - Interactive territory details

4. **Environmental Storytelling**:
   - Visual evolution based on faction control
   - Population activity representation
   - Environmental condition visualization
   - Corporate vs. underground aesthetic contrasts

#### Isometric View for Instanced Missions

1. **Mission Environment Design**:
   - Detailed server and physical space representation
   - Corporation-specific architectural language
   - Security system visualization
   - Interactive environmental elements

2. **Character Representation**:
   - Distinctive runner and bioroid models
   - Faction-specific styling and equipment
   - Animation sets reflecting abilities
   - Status effect visualization

3. **Action Visualization**:
   - Card effect representations
   - Program activation effects
   - ICE interaction visuals
   - Combat and hacking animations

4. **Information Overlays**:
   - Threat indicators
   - Opportunity highlights
   - Path visualization
   - Status and resource displays

#### Card Design and Visual Language

1. **Faction-Specific Card Styling**:
   - Color schemes matching faction identity
   - Distinctive frame designs
   - Typography reflecting faction character
   - Iconography systems for card types

2. **Dual Card System Differentiation**:
   - Visually distinct overworld and mission cards
   - Clear type indicators and grouping
   - Cost and effect visualization consistency
   - Rarity and specialization indicators

3. **Card Art Direction**:
   - Cyberpunk-inspired illustrated style
   - Character-focused art for identities
   - Action scenes for events
   - Environmental art for locations

4. **Information Hierarchy**:
   - Clear cost and effect presentation
   - Type and subtype indicators
   - Rules text legibility
   - Flavor text integration

#### Faction-specific Visual Elements

1. **Corporation Visual Identity**:
   - Weyland: Industrial, imposing, utilitarian design
   - NBN: Bright, omnipresent media aesthetic
   - Jinteki: Traditional Japanese influences with futuristic biotech
   - Haas-Bioroid: Clean, clinical, efficient design

2. **Runner Visual Identity**:
   - Criminal: Sleek, professional, luxurious elements
   - Anarch: Raw, chaotic, repurposed technology
   - Shaper: Organic meets technological, elegant solutions

3. **Environment Influences**:
   - Corporation-controlled areas reflect corporate identity
   - Runner-influenced areas show signs of hacking and repurposing
   - Contested areas display visual conflict between styles
   - Neutral areas have their own distinct aesthetic

### UI Design

The UI design prioritizes clarity, responsiveness, and game immersion while accommodating the card game interface in all gameplay contexts.

#### Card Game Interface Integration

1. **Hand Management**:
   - Intuitive card display and organization
   - Drag-and-drop play mechanics
   - Card preview and zoom functionality
   - Context-sensitive card highlighting

2. **Card Interaction**:
   - Target selection mechanics
   - Cost payment visualization
   - Effect resolution animation
   - Card state indicators

3. **Deck and Discard Visualization**:
   - Compact representation of collections
   - Easy browsing and searching
   - Card quantity indicators
   - Key card highlighting

4. **Card Market Interface**:
   - Available card display
   - Cost and requirements visualization
   - Card filtering and sorting
   - Purchase and acquisition effects

#### Strategic View UI

1. **Overworld Map Interface**:
   - Territory information display
   - Resource visualization
   - Control status indicators
   - Action availability highlighting

2. **Resource Management**:
   - Resource type indicators
   - Generation and consumption tracking
   - Resource allocation interface
   - Economy visualization

3. **Turn Structure Management**:
   - Phase indicators
   - Action point visualization
   - Turn sequence reminders
   - Timer display for timed actions

4. **Strategic Planning Tools**:
   - Territory planning overlay
   - Resource projection tools
   - Goal and objective tracking
   - Strategic information filtering

#### Tactical View UI

1. **Mission Environment Interface**:
   - Grid movement visualization
   - Interactive environment elements
   - Line of sight and access indicators
   - Hazard and opportunity markers

2. **Character Status Display**:
   - Health and resource visualization
   - Status effect indicators
   - Action availability display
   - Special ability cooldowns

3. **Combat Information**:
   - Attack and defense values
   - Success probability indicators
   - Damage prediction display
   - Counter opportunity indicators

4. **Multiplayer Party Interface**:
   - Party member status display
   - Coordination tools and indicators
   - Resource sharing interface
   - Team objective tracking

#### Information Hierarchy and Accessibility

1. **UI Organization Principles**:
   - Critical information always visible
   - Secondary information available on demand
   - Progressive disclosure for complex data
   - Consistent positioning and styling

2. **Accessibility Features**:
   - Colorblind-friendly palette options
   - Adjustable text size and contrast
   - Keyboard shortcuts for all actions
   - Screen reader compatibility

3. **Localization Support**:
   - Text expansion space for translations
   - Cultural sensitivity in iconography
   - Right-to-left language support
   - Font support for multiple languages

4. **Platform Adaptation**:
   - Responsive layout for different screen sizes
   - Touch interface optimization
   - Mouse and keyboard controls
   - Variable performance modes

### Audio Design

The audio design creates an immersive cyberpunk atmosphere while providing crucial gameplay feedback.

#### Music Style and Themes

1. **Faction-Based Musical Identity**:
   - Corporation themes: Ordered, structured, cold synthetic compositions
   - Runner themes: Edgy, rebellious, human elements mixed with glitchy electronics
   - Neutral/city themes: Ambient urban soundscapes

2. **Adaptive Music System**:
   - Dynamic layering based on game state
   - Tension adjustment for encounters
   - Territory-specific musical elements
   - Transition system for seamless atmosphere

3. **Musical Progression**:
   - Theme development tied to narrative evolution
   - Character-specific leitmotifs
   - Faction victory and defeat themes
   - Special event musical cues

#### Sound Effect Design

1. **Card Interaction Audio**:
   - Distinct sounds for card types
   - Faction-specific card play effects
   - Cost payment and resource generation audio
   - Special ability activation sounds

2. **Environmental Audio**:
   - Territory-specific ambient sounds
   - Weather and time of day effects
   - Population density audio cues
   - Security level indicators

3. **Interface Audio**:
   - Menu navigation feedback
   - Selection confirmation
   - Error and warning indicators
   - Achievement and milestone celebration

4. **Combat and Encounter Audio**:
   - ICE interaction effects
   - Program activation sounds
   - Success and failure indicators
   - Damage and defense sounds

#### Faction-specific Audio Elements

1. **Corporation Audio Signatures**:
   - Weyland: Industrial machinery, heavy impacts, rumbling bass
   - NBN: Media chatter, broadcast tones, alert sounds
   - Jinteki: Traditional Japanese instruments with biotech elements
   - Haas-Bioroid: Synthetic voices, servo motors, clean tones

2. **Runner Audio Signatures**:
   - Criminal: Smooth jazz elements, sleek electronic tones
   - Anarch: Distorted guitars, glitchy electronics, noise elements
   - Shaper: Complex evolving synthesizers, elegant transformations

3. **Vocal Design**:
   - Corporate announcements and alerts
   - Runner communication effects
   - Character-specific voice modulation
   - Faction-specific terminology and slang

#### Ambient and Environmental Audio

1. **City Soundscape**:
   - Traffic and crowd dynamics
   - Industrial and commercial zones
   - Underground and fringe areas
   - Weather and environmental effects

2. **Server Environment**:
   - Digital processing sounds
   - Data transfer effects
   - Security system alerts
   - Network topology audio cues

3. **Positional Audio**:
   - 3D audio for spatial awareness
   - Distance attenuation effects
   - Environment-based reverberation
   - Threat direction indicators

---

## Development Roadmap

The development of End of Line follows a phased approach focusing on test-driven development and incremental feature addition.

### Phase 1: Core Systems Development (3-4 months)

1. **Technical Foundation**:
   - Set up Godot project with TypeScript integration
   - Implement SpacetimeDB connection and basic state sync
   - Establish testing framework and CI/CD pipeline
   - Create core entity-component framework

2. **Card System Implementation**:
   - Develop card data structures and interaction systems
   - Implement basic deck building functionality
   - Create card visualization and interaction UI
   - Test card interaction rules and mechanics

3. **Basic Gameplay Loop**:
   - Implement simplest playable version of tactical gameplay
   - Create minimal strategic layer with territory control
   - Develop basic AI for testing
   - Establish core loop interconnection

4. **Deliverable**: Minimal viable prototype demonstrating core mechanics with test faction

### Phase 2: Single-Player Experience (3 months)

1. **AI Development**:
   - Implement advanced AI behavior for corporations
   - Create AI runner opponents
   - Develop dynamic difficulty adjustment
   - Test AI against human players

2. **Progression System**:
   - Implement character advancement mechanics
   - Create deck evolution and card acquisition
   - Develop faction reputation system
   - Test long-term progression balance

3. **Content Creation**:
   - Develop initial card set for all factions
   - Create basic territory types and attributes
   - Implement mission generation templates
   - Establish narrative framework

4. **Deliverable**: Single-player experience with progression and AI opponents

### Phase 3: Multiplayer Implementation (2-3 months)

1. **Network Architecture**:
   - Optimize SpacetimeDB integration
   - Implement client prediction and reconciliation
   - Create matchmaking and session management
   - Develop runner party system

2. **Multiplayer UI**:
   - Create social interface elements
   - Implement party coordination tools
   - Develop spectator mode
   - Design competitive match UI

3. **Security and Performance**:
   - Implement anti-cheat measures
   - Optimize network traffic
   - Improve client performance
   - Create reconnection handling

4. **Deliverable**: Functional multiplayer with basic matchmaking and party system

### Phase 4: Content and Expansion (3-4 months)

1. **Expanded Content**:
   - Complete full card set for all factions
   - Implement all territory types and features
   - Create diverse mission scenarios
   - Develop full narrative content

2. **Advanced Features**:
   - Implement market system for card acquisition
   - Create advanced progression pathways
   - Develop tournament and competition features
   - Implement community features

3. **Polish and Balance**:
   - Extensive playtesting and balance adjustments
   - Visual and audio polish
   - Performance optimization
   - Usability improvements

4. **Deliverable**: Feature-complete game with full content set

### Phase 5: Launch and Support (Ongoing)

1. **Beta Testing**:
   - Closed beta with invited players
   - Open beta period
   - Balance adjustments based on feedback
   - Performance optimization

2. **Launch Preparation**:
   - Marketing and community building
   - Server infrastructure scaling
   - Documentation and tutorials
   - Launch event planning

3. **Post-Launch Support**:
   - Regular balance patches
   - Bug fixes and improvements
   - New content additions
   - Community event support

4. **Feature Expansion**:
   - New faction or identity additions
   - Expanded territory types
   - Additional game modes
   - Narrative expansions

### Prioritization Strategy

The development prioritizes core gameplay loops and testability:

1. **Horizontal Slicing**: Implement minimal versions of all core systems first
2. **Vertical Implementation**: Deep-dive into specific features based on dependencies
3. **Playtest-Driven**: Prioritize features based on playtest feedback
4. **Risk Mitigation**: Address technical risks early in development
5. **Incremental Polish**: Continuously improve rather than leaving polish to the end

---

## Appendices

### Appendix A: Sample Cards

#### Overworld Card Examples

**Corporation Cards**:

```
CORPORATE INFRASTRUCTURE
"Advanced R&D Center"
Type: Asset - Facility
Faction: Haas-Bioroid
Cost: 4 credits
Install in a territory you control.
This territory generates +1 data token per turn.
When you score an agenda, gain 2 credits.
```

```
CORPORATE AGENDA
"Project Atlas"
Type: Agenda
Faction: Weyland
Advancement Requirement: 3
Agenda Points: 2
When scored: Place 1 agenda counter on Project Atlas.
Hosted agenda counter: Search your deck for a card and add it to HQ. Shuffle R&D.
```

**Runner Cards**:

```
RUNNER RESOURCE
"Underworld Connections"
Type: Resource - Connection
Faction: Criminal
Cost: 2 credits
Influence: 2
Gain 1 credit whenever you make a successful run on a central server.
When tagged, trash this resource.
```

```
RUNNER EVENT
"Day Job"
Type: Event
Faction: Neutral
Cost: 2 credits
Gain 4 credits.
Skip your next turn.
```

#### Instanced Mission Card Examples

**Corporation Cards**:

```
CORPORATION ICE
"Enigma"
Type: ICE - Code Gate
Faction: Neutral
Rez Cost: 3 credits
Strength: 2
The Runner loses 1 click if able.
End the run.
```

```
CORPORATION ASSET
"Aggressive Secretary"
Type: Asset - Ambush
Faction: Haas-Bioroid
Rez Cost: 0 credits
Trash Cost: 3 credits
When accessed, you may pay X credits to trash X programs.
```

**Runner Cards**:

```
RUNNER PROGRAM
"Gordian Blade"
Type: Program - Decoder
Faction: Shaper
Install Cost: 4 credits
Memory: 1
Strength: 2
1 credit: +1 strength for the remainder of this run.
1 credit: Break code gate subroutine.
```

```
RUNNER HARDWARE
"Desperado"
Type: Hardware - Console
Faction: Criminal
Install Cost: 3 credits
Influence: 3
+1 Memory Unit
Gain 1 credit whenever you make a successful run.
Limit 1 console per player.
```

### Appendix B: Territory Map Examples

#### Sample Territory Layout

```
   ┌───┐   ┌───┐   ┌───┐
  /     \ /     \ /     \
 │  NBN  │  WEY  │  JIN  │
  \     / \     / \     /
   ├───┤   ├───┤   ├───┤
  /     \ /     \ /     \
 │  NEU  │  HB   │  NEU  │
  \     / \     / \     /
   ├───┤   ├───┤   ├───┤
  /     \ /     \ /     \
 │  UND  │  NEU  │  UND  │
  \     / \     / \     /
   └───┘   └───┘   └───┘
```

Legend:
- NBN: NBN Corporate Zone
- WEY: Weyland Corporate Zone
- JIN: Jinteki Corporate Zone
- HB: Haas-Bioroid Corporate Zone
- NEU: Neutral Fringe Zone
- UND: Underground Zone

#### Sample Territory Attributes

```
Territory: Downtown Commercial District
Type: Fringe Zone
Corporate Influence: 45% (NBN)
Security Level: 3
Resource Value: 4
Stability Index: 72%
Population: 5

Control Benefits:
- 3 credits per turn
- 1 data token per turn
- Access to Commercial District Market

Connected to:
- Financial District (North)
- Industrial Zone (East)
- Residential Blocks (South)
- Entertainment District (West)
```

### Appendix C: UI Mockups and Wireframes

#### Overworld Interface (Strategic View)

```
┌───────────────────────────────────────────────────────────────────┐
│ RESOURCE BAR                                                       │
│ Credits: 12  |  Data: 5  |  Influence: 7  |  Turn: 3  |  Phase: 2 │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│            ┌───┐                                                   │
│           /     \                                                  │
│          │  T1  │                                                  │
│           \     /                                                  │
│    ┌───┐   ├───┤   ┌───┐         TERRITORY INFO                   │
│   /     \ /     \ /     \        ┌────────────────────────┐       │
│  │  T2  │  T3   │  T4  │        │ Downtown District       │       │
│   \     / \     / \     /        │ Type: Fringe Zone      │       │
│    ├───┤   ├───┤   ├───┤        │ Control: 45% (NBN)      │       │
│   /     \ /     \ /     \       │ Security: ■■■□□         │       │
│  │  T5  │  T6   │  T7  │        │ Resources: ■■■■□        │       │
│   \     / \     / \     /        │ Population: ■■■■■       │       │
│    └───┘   └───┘   └───┘        └────────────────────────┘       │
│                                                                    │
│                                   ACTIONS                          │
│  MINI-MAP                        ┌────────────────────────┐       │
│  ┌──────────────┐                │ □ Build Infrastructure  │       │
│  │              │                │ □ Deploy Security       │       │
│  │              │                │ □ Advance Agenda        │       │
│  │              │                │ □ Launch Operation      │       │
│  └──────────────┘                └────────────────────────┘       │
│                                                                    │
├───────────────────────────────────────────────────────────────────┤
│                           HAND AREA                                │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐   │
│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│   │
│  │ 1  │  │ 2  │  │ 3  │  │ 4  │  │ 5  │  │ 6  │  │ 7  │  │ 8  │   │
│  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘   │
└───────────────────────────────────────────────────────────────────┘
```

#### Instanced Mission Interface (Tactical View)

```
┌───────────────────────────────────────────────────────────────────┐
│ MISSION INFO                                        TIMER: 05:23   │
│ Objective: Access R&D Server  |  Security Level: 3  |  Alert: 2    │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  RESOURCES                             ISOMETRIC VIEW              │
│  ┌──────────────┐                     ┌──────────────────────┐    │
│  │ Credits: 7   │                     │                      │    │
│  │ Memory: 3/5  │                     │                      │    │
│  │ Actions: 2   │                     │                      │    │
│  │ Brain: 3     │                     │                      │    │
│  └──────────────┘                     │                      │    │
│                                       │                      │    │
│  INSTALLED                            │                      │    │
│  PROGRAMS                             │                      │    │
│  ┌──────────────┐                     │                      │    │
│  │ ┌───┐ ┌───┐  │                     │                      │    │
│  │ │P1 │ │P2 │  │                     │                      │    │
│  │ └───┘ └───┘  │                     │                      │    │
│  │ ┌───┐        │                     │                      │    │
│  │ │P3 │        │                     │                      │    │
│  │ └───┘        │                     └──────────────────────┘    │
│  └──────────────┘                                                  │
│                                                                    │
│  PARTY                                SELECTED ICE                 │
│  MEMBERS                             ┌──────────────────────┐     │
│  ┌──────────────┐                    │ Name: Enigma         │     │
│  │ Runner 1     │                    │ Type: Code Gate      │     │
│  │ Runner 2     │                    │ Strength: 2          │     │
│  └──────────────┘                    │ Subs: 2              │     │
│                                      └──────────────────────┘     │
│                                                                    │
├───────────────────────────────────────────────────────────────────┤
│                           HAND AREA                                │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐   │
│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│  │Card│   │
│  │ 1  │  │ 2  │  │ 3  │  │ 4  │  │ 5  │  │ 6  │  │ 7  │  │ 8  │   │
│  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘  └────┘   │
└───────────────────────────────────────────────────────────────────┘
```

### Appendix D: Example Gameplay Scenarios

#### Scenario 1: Corporation Strategic Turn

1. **Resource Collection Phase**:
   - Weyland corporation collects 8 credits from controlled territories
   - Receives 3 data tokens from R&D facilities
   - Gains 2 influence from media operations

2. **Card Draw and Planning**:
   - Draws 2 cards from R&D
   - Plans deployment of a new security grid in Downtown territory
   - Evaluates advancing "Hostile Takeover" agenda

3. **Action Execution**:
   - Spends 4 credits to install a new security grid in Downtown (enhancing ICE strength)
   - Allocates 3 credits and 2 actions to advance "Hostile Takeover" agenda
   - Deploys an operation to increase security level in adjacent territory

4. **Turn Resolution**:
   - "Hostile Takeover" reaches advancement threshold and is scored
   - Corporation gains agenda points and special ability
   - Territory control percentage increases
   - Influence on adjacent territories shifts

#### Scenario 2: Runner Mission Execution

1. **Preparation Phase**:
   - Criminal runner assembles mission deck targeting NBN infrastructure
   - Spends resources to acquire specialized breaker programs
   - Forms party with Shaper runner for additional support

2. **Mission Initialization**:
   - Selects NBN Data Center as target
   - Chooses approach vector through adjacent runner-controlled territory
   - Initiates run with stealth approach (reduced detection)

3. **Server Penetration**:
   - Encounters first ICE: "News Hound" (Sentry)
   - Shaper runner assists with ICE weakness analysis
   - Criminal runner uses "Femme Fatale" program to bypass
   - Deeper penetration reveals second ICE: "RSVP" (Code Gate)
   - Criminal uses "Inside Job" event to bypass

4. **Server Access and Resolution**:
   - Runners access server contents
   - Discover and steal "Market Research" agenda
   - Trigger alarm system during extraction
   - Criminal runner uses "Emergency Shutdown" to delay pursuit
   - Both runners escape successfully

5. **Mission Aftermath**:
   - Stolen agenda flips to runner control on overworld
   - NBN territory control percentage decreases
   - Security level increases in surrounding territories
   - Runners gain experience and card rewards
   - New mission opportunities appear based on stolen data

#### Scenario 3: Territory Control Conflict

1. **Initial Situation**:
   - Downtown Commercial District is 55% Weyland controlled
   - Criminal runners have 25% influence through network presence
   - 20% remains as neutral civilian infrastructure

2. **Weyland Actions**:
   - Plays "Hostile Architecture" infrastructure card adding 10% control
   - Deploys additional security assets for 5% control
   - Attempts to advance "Gentrification" agenda

3. **Runner Countermeasures**:
   - Anarch runner initiates riot in the district
   - Security effectiveness temporarily reduced
   - Criminal runner exploits chaos to establish new access points
   - Criminal's "Black Market Connections" add 15% runner influence

4. **Escalation**:
   - Weyland deploys "Punitive Counterstrike" operation
   - Targets known runner safehouses
   - Runners must sacrifice resources or lose influence

5. **Resolution**:
   - Final control: Weyland 60%, Runners 35%, Neutral 5%
   - Territory stability decreases to 40%
   - New mission opportunities appear:
     - Corporation: Restore order and increase security
     - Runners: Exploit instability for major server breach
   - Adjacent territories affected by spillover events

#### Scenario 4: Multi-Runner Party Coordination

1. **Party Formation**:
   - Criminal "Face" runner: Specialized in bypass and economy
   - Anarch "Wrecker" runner: Focused on ICE destruction
   - Shaper "Tech" runner: Provides program support and enhancement

2. **Role Distribution**:
   - Criminal runner leads initial approach and handles security systems
   - Anarch runner prepared for aggressive breakthrough if stealth fails
   - Shaper runner maintains support programs and resource distribution

3. **Coordinated Action**:
   - Criminal initiates run on Jinteki server
   - Encounters unexpected "Neural Katana" ICE
   - Unable to bypass, signals to Anarch runner
   - Anarch uses "Parasite" and "Datasucker" to destroy ICE
   - Shaper boosts memory capacity for additional program installation
   - Criminal resumes lead with enhanced resources

4. **Server Breach and Objective**:
   - Team accesses Jinteki R&D server
   - Shaper uses "Maker's Eye" to access additional cards
   - Criminal steals "Genetic Resequencing" agenda
   - Anarch installs virus to weaken future ICE
   - Team coordinates extraction with minimal trace exposure

5. **Reward Distribution**:
   - Primary reward: Stolen agenda worth 2 points
   - Criminal gains additional credits from successful run
   - Anarch gains virus counters for installed programs
   - Shaper gains technical data for program development
   - Team gains collective reputation with underground factions