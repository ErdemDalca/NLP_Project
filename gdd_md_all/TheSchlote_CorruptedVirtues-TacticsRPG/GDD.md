# Corrupted Virtues - Game Design Document (GDD)
**A turn-based tactics RPG built in Godot 4 with C#.**  
*Inspired by LucasArts' Gladius, Paper Mario: The Thousand-Year Door, and classic RPGs.*  

---

## 1. Game Overview
### Title:
**Corrupted Virtues**  

### Genre:
Turn-Based Tactics RPG  

### Platform:
PC (Godot 4, C#)  

### Target Audience:
Fans of tactical RPGs, fantasy worlds, and games like *Gladius*, *Paper Mario: The Thousand-Year Door*, and *Fire Emblem*.  

### Controller Support:
Full controller support is a core part of the gameplay experience, emphasizing fluid navigation, combat input, and QuickTimeEvent (QTE) mechanics.  

---

## 2. Core Concept
**Corrupted Virtues** is a turn-based tactics RPG that merges grid-based combat with mythological and fantasy storytelling. Players lead a Guardian through corrupted lands, purifying the once-noble Virtues. Inspired by *Gladius*’s unique QTE combat system and *Paper Mario’s* action timing, the game challenges players to combine strategy with reflex-driven mechanics.  

### Unique Selling Points (USPs):
- **Gladius-Inspired Tactical Combat** – Grid-based movement and QTE-driven attack mechanics.  
- **Mythological Setting** – A world built on divine Virtues and biblical lore, filled with angelic and corrupted forces.  
- **Corruption System** – Players must purify corrupted Virtues, facing mythological boss creatures.  
- **Guardian Focused** – Players step into the role of a Guardian angel tasked with rallying allies across Areti.  

---

## 3. Story and Setting
### The World of Areti:
Our story begins in the land of Areti. This peaceful and prosperous world is home to many wonderful people and creatures alike.  

Areti’s secret to peace and prosperity lies in the cooperation and support each of the seven main regions provide for one another. The strength of their unity is what has kept the lands safe for centuries.  

At the center of Areti lies **Paradeisos**, a massive tower that reaches to the heavens. Here resides **The First King of Areti**, a benevolent ruler who for hundreds of years has been the bridge between God and the divine sovereigns.  

Each of the Seven Lands is governed by its own divine sovereign, sworn to protect and serve their people. These rulers are known as **The Virtues**:  

- **Temperance** – Ruler of *Enkrateia (Nature)*  
- **Purity** – Ruler of *Katharot (Water)*  
- **Charity** – Ruler of *Filanthropia (Earth)*  
- **Patience** – Ruler of *Epimony (Fire)*  
- **Kindness** – Ruler of *Kalosine (Energy)*  
- **Diligence** – Ruler of *Epimaleia (Darkness)*  
- **Humility** – Ruler of *Tapenoteia (Light)*  

The land of Areti thrives under the guidance of these divine rulers, each embodying their Virtue and protecting their people.  

### Narrative Overview:
Areti is also protected by **The Choir**, a group of powerful Archangels that guard the world from external threats and aid the Virtues in their duties. There are seven leaders within The Choir, one to assist each one of the Virtues.  

Alongside The Choir, smaller villages across Areti are protected by **Guardian Angels**, known simply as **Guardians**. These Guardians serve as divine protectors for their communities.  

Our story follows one such Guardian from a remote village on the other side of Areti, far from Paradeisos. As corruption spreads across the land, this Guardian must gather allies and travel across the Seven Lands, purifying the corrupted Virtues and ultimately saving Areti from destruction.  

---

## 4. Gameplay
### Game Loop:
1. **Exploration Phase** – Traverse regions, interact with NPCs, and gather resources.  
2. **Combat Phase** – Grid-based battles where units perform actions based on turn order.  
3. **Progression** – Gain XP, upgrade abilities, and purify Virtues to unlock new paths and skills.  

### Combat System:
- **Turn-Based Tactics** – Move and position units across a 3D grid during combat encounters.  
- **Action Timing (QTE)** – Enhance attacks and abilities through timed button presses.  
- **Combat Focus** – Player actions focus on positioning, attack accuracy, and environmental interaction.  

---

## 5. Characters and Customization
The current focus is on developing core gameplay before finalizing specific characters or classes.  

### Customization:
- **Equipment** – Weapons and armor influencing stats and abilities.  
- **Leveling** – Gain XP through combat to improve core stats.  
- **Abilities** – Unlock and upgrade special skills as the game progresses.  

---

## 6. Systems and Mechanics
- **Grid Movement:** Astar3D for pathfinding and grid-based navigation.  
- **Turn Economy:** Move, attack, or perform both based on unit capabilities.  
- **QTE:** Core combat system to enhance player engagement.  

---

## 7. Progression and Rewards
- **XP and Leveling** – Level up through combat and quests.  
- **Holy Artifacts** – Purifying Virtues grants divine relics, providing party-wide bonuses.  

---

## 8. Development Timeline
A detailed breakdown of tasks and milestones can be found on the [GitHub Projects Page](https://github.com/users/TheSchlote/projects/4).  

---

## 9. Notes and References
- **Core Inspiration:** *Gladius* (LucasArts), *Paper Mario: The Thousand-Year Door*, classic RPGs.  
- **Follow Development:** [Moral Support Studios - Blog]([https://moralsupportstudios.com](https://theschlote.github.io/))  
