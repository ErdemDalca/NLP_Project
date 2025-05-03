### **Objective:**  
Reconstruct a **complete and structured game design document** using the provided materials:  

1. **Origin Game Document** (if provided) – The initial design document, which may be incomplete or outdated.  
2. **Game Concept** – A conceptual description of the game, including its mechanics and gameplay vision.  
3. **HTML Game File** – A functional or semi-functional prototype of the game in HTML format.  

If the **Origin Game Document** is not provided, deduce it from the **Game Concept** and **HTML Game File**.  
The **deduced game document** should be surrounded by `ORIG-DOC-BEGIN` and `ORIG-DOC-END`, with these tags forming standalone lines.  

Before `MOD-DOC-BEGIN`, output the **suggested game name**, surrounded by `SUGGEST-GAME-NAME-BEGIN` and `SUGGEST-GAME-NAME-END`, with these tags forming standalone lines.  

The **modified game document** should be surrounded by `MOD-DOC-BEGIN` and `MOD-DOC-END`, with these tags forming standalone lines.  

The goal is to extract, consolidate, and refine information from all sources to create a **coherent, playable, and fully documented** game design document.

---

### **Section 1: Extract & Validate Information from Sources**  
- If the **Origin Game Document** is available, extract **existing structured content** (mechanics, objectives, progression, rules).  
- Compare the **Game Concept** with the **HTML Game File**, identifying **features that were implemented, omitted, or altered**.  
- Identify **missing details, inconsistencies, or incomplete mechanics** by cross-referencing all sources.  
- Extract and document **all defined mechanics, abilities, rules, and gameplay loops**.  

---

### **Section 2: Resolve Gaps & Standardize Mechanics**  
- If mechanics are missing or unclear, **reconstruct them** using contextual clues from the **game concept** and the **HTML file**.  
- Define **interactions, controls, physics, and balancing factors** if they are underdeveloped or absent.  
- If discrepancies exist between the **game concept** and **HTML implementation**, determine which is more functional and adjust accordingly.  

---

### **Section 3: Final Game Design Document (GDD) Reconstruction**  
- Structure the **recovered document** in a standard format:  
  - **Title & Game Overview**  
  - **Core Gameplay Mechanics & Features**  
  - **Controls & Player Interactions**  
  - **Level Design & Progression**  
  - **Objectives, Scoring, and Win/Loss Conditions**  
  - **Abilities, Power-ups, and Item Descriptions**  
  - **Game Rules & Balance Adjustments**  
  - **Technical Notes (if applicable, based on HTML implementation)**  
- Ensure that all mechanics are **logically structured, functional, and implementation-ready**.  
- The final document should be **complete enough for a developer to continue or rebuild the game**.  

---

### **Example Input & Output**
#### **Example Input:**  
- **Origin Game Document:** _(A draft document describing a side-scroller RPG with missing level progression details.)_  
- **Game Concept:** _(A high-level vision of an adventure game where enemies adapt to player actions.)_  
- **HTML Game File:** _(A working prototype where the player can move but abilities and enemy AI are incomplete.)_  

---

#### **Example Output (Excerpt of Final GDD Reconstruction):**  

ORIG-DOC-BEGIN  
*(If provided, or deduced from the game concept and HTML file)*  
*...Extracted or deduced game document content...*  
ORIG-DOC-END  

SUGGEST-GAME-NAME-BEGIN  
Adaptive Quest  
SUGGEST-GAME-NAME-END  

MOD-DOC-BEGIN  
### **Game Title:** Adaptive Quest  
**Genre:** Side-scroller Action RPG  
**Core Gameplay:**  
- Players control a hero who **adapts to enemy behavior dynamically**.  
- Movement is controlled via arrow keys, **jumping and attacking with spacebar and shift**.  
- Levels feature **progressive enemy AI** that learns player movement patterns.  

**Abilities & Mechanics:**  
- **Adaptive Reflex Mode:** Player movement speed increases when evading multiple attacks in succession.  
- **Combo System:** Attacking enemies in rapid succession grants a damage multiplier.  

**Level Design Adjustments:**  
- The HTML file includes **basic movement and physics**, but **enemy AI needs scripting**.  
- Level transitions were missing in the prototype; added a **checkpoint system** to balance difficulty.  
MOD-DOC-END  
