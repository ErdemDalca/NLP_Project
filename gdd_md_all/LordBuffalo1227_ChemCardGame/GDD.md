# Chemistry Trading Card Game (CTCG) - Game Design Document (GDD)

## 1. Game Overview
**Title:** Chemistry Trading Card Game (CTCG)  
**Genre:** Educational Trading Card Game (TCG)  
**Target Audience:** High school and college students, chemistry enthusiasts, and TCG players  
**Platform:** Physical card game (option for digital adaptation)

### **1.1 Game Concept**
CTCG is a competitive, educational card game where players use chemistry-themed cards to engage in strategic battles. Players build decks composed of Elemental, Compound, Reaction, Catalyst, and Scientist cards to perform chemical reactions, strengthen molecules, and outmaneuver their opponents.

### **1.2 Game Objective**
Players compete to either:
- Destroy all of the opponent’s Compound Cards.
- Complete a scientific goal (such as forming a set of specific compounds).
- Reduce the opponent’s deck to zero cards.

---
## 2. Game Components
### **2.1 Card Types**
1. **[[01. Cartas de elementos|Element Cards]]** – Represent chemical elements and provide energy for reactions.
	1. Alkali Metals
	2. Alakline earth Metals
	3. Transition Metals
	4. Post-transition Metals
	5. Metalloids
	6. Non-metals
	7. Halogens
	8. Noble Gases
2. **[[02. Cartas de compuestos|Compound Cards]]** – Represent molecules and have special effects based on chemistry.
	1. Essential Compounds
	2. Advanced Chemistry Compounds
	3. Legendary Compounds
3. **[[03. Cartas de reacción|Reaction Cards]]** – Trigger chemical reactions that transform or modify gameplay.
	1. Basic Reactions
		1. Combustion
		2. Double Displacement
		3. Neutralization
		4. RedOx
	2. Intermediate reactions
		1. Photosynthesis
		2. Electrolysis
		3. Polymerization
		4. Fermentation
	3. Advanced reactions
		1. Nuclear Fission
		2. Catalytic Cracking
		3. Dehydration Synthesis
		4. Precipitation
	4. Environmental reactions
		1. Acid Rain Formation
		2. Ozone Depletion
		3. Greenhouse Effect
	5. Specialized reactions
		1. Corrosion
		2. Enzyme Catalysis
		3. Buffer Formation
		4. Radical Chain Reaction
		5. Coordination Complex
	6. Expert reactions
		1. Supersaturation
		2. Diels-Alder Cycloaddition
		3. Bioluminescence
		4. Phase Transition
		5. Entropy Increase
4. **[[04. Cartas de catálisis|Catalyst Cards]]** – Speed up or enhance reactions.
	1. Inorganic Catalysts
	2. Biochemical Catalysts
	3. Industrial Catalysts
	4. Environmental Catalysts
	5. Specialty Catalysts
5. **[[05. Cartas de Científicos|Scientist Cards]]** – Provide strategic advantages based on real scientists’ contributions.
6. **[[06. Cartas de Estado|State Cards]]** – Introduce conditions like temperature, pressure, and phase changes.
	1. Calor Abrasador
	2. Frío Glacial
	3. Presión Extrema
	4. Vacío Espacial
	5. Flujo Líquido
	6. Ionización Plasmática

### **2.2 Deck Composition**
- Each player’s deck consists of **40-60 cards**.
- A deck must contain at least **10 Elemental Cards** and **5 Compound Cards**.
- Players may use **up to 4 copies of any single card** in their deck.

---
## 3. Gameplay Mechanics
### **3.1 Turn Structure**
Each turn consists of:
8. **Draw Phase** – Draw one card.
9. **Elemental Phase** – Play up to **one Elemental Card** per turn.
10. **Action Phase**
   - Play **Reaction Cards** to modify molecules.
   - Use **Scientist or Catalyst Cards** for special effects.
   - Attack opponent’s molecules (if applicable).
11. **End Phase** – Resolve lingering effects and pass the turn.

### **3.2 Energy System (Elemental Cards)**
- Every Compound Card requires **specific Elemental Cards** to be activated.
- Elements must be attached to compounds **before a reaction can occur**.
- Some reactions consume elements, removing them from play.

### **3.3 Attacks & Defense**
- Each Compound Card has **Attack Power** and **Stability Value**.
- Attacks reduce the Stability of opposing molecules.
- If Stability reaches **0**, the molecule is destroyed and discarded.

---
## 4. Win Conditions
A player wins by achieving one of the following:
12. **Destroying all of the opponent’s Compound Cards**.
13. **Reaching a scientific goal**, such as completing a complex reaction chain.
14. **Running the opponent out of cards**.

---
## 5. Card Design
### **5.1 Card Layout**
15. **Header:** Card title and type (Elemental, Compound, etc.).
16. **Artwork:** Central area for molecular diagrams or thematic illustrations.
17. **Stats & Attributes Panel:** Displays Reactivity, Stability, Energy.
18. **Ability/Effect Box:** Describes the card’s effect.
19. **Flavor Text:** Includes an educational tidbit.
20. **Footer:** Energy cost indicator and card edition.

### **5.2 Sample Cards**
#### **Elemental Card Example**
**Name:** Oxygen (O₂)  
**Type:** Elemental Card  
**Effect:** Required for combustion and oxidation reactions.

#### **Compound Card Example**
**Name:** Sulfuric Acid (H₂SO₄)  
**Type:** Compound Card  
**Energy Requirement:** 2 Hydrogen, 1 Oxygen, 1 Sulfur  
**Effect:** Doubles the damage of oxidation reactions.

#### **Reaction Card Example**
**Name:** Combustion  
**Type:** Reaction Card  
**Requirement:** Hydrocarbon + O₂  
**Effect:** Deals 30 damage to an opponent’s organic molecule and removes O₂ from play.

#### **Scientist Card Example**
**Name:** Marie Curie – Radioactive Genius  
**Type:** Scientist Card  
**Effect:** Allows the use of radioactive elements without energy cost for one turn.

---
## 6. Elemental Stats & Bonuses
To reflect real chemistry, each element group has specific stats and bonuses:

### **Alkali Metals** (e.g., Sodium, Potassium)
- **Reactivity:** 9/10  
- **Stability:** 3/10  
- **Bonus:** “Explosive Reaction” – When combined with a Halogen, deal extra damage.

### **Alkaline Earth Metals** (e.g., Magnesium, Calcium)
- **Reactivity:** 7/10  
- **Stability:** 5/10  
- **Bonus:** “Compound Formation” – Boost compound effectiveness.

### **Transition Metals** (e.g., Iron, Copper)
- **Reactivity:** 5/10  
- **Stability:** 7/10  
- **Bonus:** “Catalytic Effect” – Reduces the cost of Reaction Cards.

### **Post-Transition Metals** (e.g., Aluminum, Tin)
- **Reactivity:** 4/10  
- **Stability:** 8/10  
- **Bonus:** “Structural Shield” – Provides extra stability to molecules.

### **Metalloids** (e.g., Silicon, Arsenic)
- **Reactivity:** 6/10  
- **Stability:** 6/10  
- **Bonus:** “Versatility” – Can switch between offense and defense.

### **Nonmetals** (e.g., Carbon, Oxygen)
- **Reactivity:** 6/10  
- **Stability:** 7/10  
- **Bonus:** “Adaptive Bonding” – Strengthens compounds it forms.

### **Halogens** (e.g., Fluorine, Chlorine)
- **Reactivity:** 8/10  
- **Stability:** 4/10  
- **Bonus:** “Bond Formation” – Weakens opposing molecule stability.

### **Noble Gases** (e.g., Neon, Argon)
- **Reactivity:** 2/10  
- **Stability:** 10/10  
- **Bonus:** “Inert Shield” – Can negate a Reaction Card effect.

---
## 7. Expansion & Future Features
- Additional **biochemistry** and **polymer science** expansions.
- Unique **legendary scientist** and **laboratory equipment** cards.
- Digital version with **AI-based opponent challenges**.

---
## 8. Conclusion
CTCG blends **fun, strategy, and education** into an engaging experience. By combining deck-building, reaction planning, and scientific principles, players will deepen their understanding of chemistry while enjoying a dynamic trading card game.

---


