**Game Design Document: Coral Reef Survival Simulator**

---

### **Game Overview**

**Title:** Coral Reef Survival Simulator  
**Genre:** Simulation, Educational  
**Platform:** PC (Python with `pygame`)  
**Target Audience:** Ages 10+; gamers interested in environmental conservation and educational games.  
**Objective:** Players manage and protect a virtual coral reef by maintaining environmental factors, responding to challenges, and keeping the reef’s health above critical levels for 10 rounds.

---

### **Game Concept**

The game is a single-player experience where players take on the role of a coral reef steward. Players manage critical environmental factors (temperature, salinity, and pH) while responding to random events like storms, pollution, or coral growth. Success depends on maintaining reef health through strategic adjustments and using limited resources to counteract negative effects.

---

### **Key Features**

1. **Environmental Management:**
   - Players adjust temperature, salinity, pH, light exposure, and nutrient levels using interactive sliders or buttons.
   - Incorrect adjustments penalize reef health.

2. **Dynamic Reef Health System:**
   - A health meter ranges from 0 (dead reef) to 100 (thriving reef).
   - Health responds dynamically to player actions and random events.

3. **Random Events:**
   - Events like storms, pollution, algae blooms, or tsunamis occur randomly between rounds, with timing varying to create an unpredictable and engaging challenge for players.
   - Events increase in intensity as the game progresses. Later rounds introduce more challenging and impactful events to keep players engaged and tested.
   - Positive events (e.g., new coral growth, increased fish biodiversity, or the introduction of new marine species) provide health boosts and enrich the ecosystem, making the reef more vibrant and dynamic.

4. **Visual Feedback:**
   - Background visuals update to reflect reef health (e.g., thriving coral or a dying reef).
   - Animations for fish, coral growth, and environmental effects.

5. **Educational Elements:**
   - Fun facts about coral reefs are displayed between rounds.
   - Provide actionable suggestions about improving coral reef ecosystems, such as reducing water pollution, promoting sustainable fishing practices, implementing artificial reef programs, and raising public awareness through education campaigns.
   - Players learn about real-world challenges facing coral ecosystems.

6. **Progression System:**
   - The first round serves as an interactive tutorial, introducing players to the game mechanics, controls, and objectives in a clear and engaging way, ensuring they are prepared for the challenges ahead.
   - Players complete the game by surviving 10 rounds, with a final score calculated based on the reef’s health and actions taken.
   - The lose condition occurs if health drops to 0 at any point, ending the game immediately.

---

### **Gameplay Mechanics**

#### **Thresholds Summary Table**

| Factor                   | Threshold                                 | Effect                              |
|--------------------------|-------------------------------------------|------------------------------------|
| Temperature              | >30–32°C (bleaching); <18°C (cold stress) | Bleaching, mortality               |
| pH                       | <7.8                                      | Weak skeletons, slow growth        |
| Salinity                 | <25 ppt; >40 ppt                          | Stress, tissue damage              |
| Suspended Sediments      | >10 mg/L for extended periods             | Smothering, blocked sunlight       |
| Depth/Light Availability | >50 meters                                | Reduced photosynthesis, coral death|
| Nutrient Levels          | Excess nitrates/phosphates                | Algal overgrowth, competition      |
| Heavy Metals             | >0.1 mg/L                                 | Toxic to corals                    |
| Pesticides               | >1 μg/L                                   | Toxic to polyps and algae          |
| Wave Energy              | Storm intensity                           | Physical destruction of reefs      |
| Sea Level Rise           | >5 mm/year                                | Drowning of reefs                  |

#### **Core Loop:**

1. Start a new round.
2. Display current reef health and stats.
3. Introduce a random event affecting reef health. Random events will occur every 10 to 30 seconds and last for 30 seconds, creating dynamic and time-sensitive challenges for players.
4. Allow players to adjust temperature, salinity, pH, light exposure, and nutrient levels.
5. Update health based on player actions and events.
6. Each round lasts 1 minute, with increasing difficulty as the game progresses. End the round; repeat until 10 rounds are completed or health drops to 0.

#### **Random Events Examples:**

| Event                      | Impact     |
|----------------------------|------------|
| Storm hits the reef!       | -10 health |
| Pollution spills nearby!   | -15 health |
| Algae bloom occurs.        | -5 health  |
| New coral growth spotted!  | +10 health |
| Fish population increases! | +5 health  |
| Excessive sedimentation!   | -8 health  |
| Overfishing in the area!   | -12 health |
| Optimal light exposure!    | +7 health  |
| Tsunami strikes!           | -20 health |

#### **Player Actions:**

- Adjust sliders for:
  - **Temperature** (20-30°C): Correcting temperature can mitigate the impact of heat-related events like coral bleaching.
  - **Salinity** (30-40 ppt)
  - **pH Level** (7.8-8.4)
  - **Light Exposure** (0-100%): Adjusting light exposure can counter the effects of excessive shading or bright conditions.
  - **Nutrient Levels** (0-10 mg/L): Balancing nutrients helps prevent algae blooms or nutrient deficiency.
- Correct adjustments provide a health boost; incorrect ones result in health penalties.

---

### **Visual and Audio Design**

#### **Graphics:**

- **Background:** A vibrant reef image that degrades or improves based on health.
- **Sprites:** Moving fish, coral growth, and pollution effects.
- **UI Elements:**
  - Health bar at the top of the screen.
  - Sliders or buttons for adjusting environmental factors.
  - Pop-ups for event descriptions.

#### **Audio:**

- Background music: Relaxing ocean sounds to provide a soothing ambiance that immerses players in the underwater environment.
- Sound effects:
  - Thunder for storms: Enhances the dramatic impact of storm events.
  - Bubbling water for pH changes: Adds auditory cues for environmental adjustments.
  - Splashing sounds for fish population events: Creates a sense of life and activity within the reef, making the gameplay more engaging.
  - Winning sound effects for successfully completing the game to motivate players.

---

### **Technical Details**

#### **Tools and Libraries:**

- **Python** with `pygame` for game development.
- Image editing tools for background and sprites.
- Audio editing tools for sound effects.

#### **System Requirements:**

- OS: Windows, macOS, or Linux
- Processor: 2 GHz or faster
- Memory: 4 GB RAM
- Graphics: Integrated GPU
- Storage: 100 MB free space

#### **Game States:**

1. **Main Menu:** Start Game, Instructions, Quit.
2. **Game Screen:** Display health, stats, and reef visuals.
3. **Game Over Screen:** Show win/loss and final stats.

---

### **Development Roadmap**

#### **Phase 1: Planning and Prototyping** (12/29/2024~12/31/2024)
- [ ] Create initial design and mockups.
- [ ] Set up `pygame` framework.
- [ ] Implement basic game loop.

#### **Phase 2: Core Gameplay** (1/1/2025~1/2/2025)
- [ ] Add sliders for temperature, salinity, pH, light exposure, and nutrient levels.
- [ ] Implement health system.
- [ ] Add random events and effects.

#### **Phase 3: Visual and Audio Enhancements** (1/2/2025~1/3/2025)
- [ ] Add background and sprite animations.
- [ ] Integrate sound effects and background music.
- [ ] Create visual feedback for health changes.

#### **Phase 4: Testing and Polishing** (1/2/2025~1/3/2025)
- [ ] Test for bugs and balance gameplay.
- [ ] Add educational facts and fun animations.
- [ ] Finalize UI and UX.

#### **Phase 5: Release** (1/4/2025)
- [ ] Package the game for distribution.
- [ ] Create documentation and instructions.

---

### **Potential Future Expansions**

1. **Multiplayer Mode:** Collaborate with friends to save a shared reef.
2. **New Ecosystems:** Introduce reefs like the Great Barrier Reef or Red Sea Reef with unique challenges.
3. **Upgrades:** Add tools like artificial shading or waste filters to assist players.
4. **Mobile Version:** Port the game to mobile platforms using `Kivy` or similar tools.

---

### **Conclusion**

The Coral Reef Survival Simulator is an engaging and educational game that combines fun gameplay with real-world environmental lessons. Unlike other educational simulation games, it emphasizes interactive management of multiple environmental factors, dynamic visual feedback, and real-world challenges like storms and pollution, providing an immersive and unique learning experience. It aims to inspire players to learn about and appreciate the delicate balance of coral reef ecosystems while providing a challenging and rewarding simulation experience.

