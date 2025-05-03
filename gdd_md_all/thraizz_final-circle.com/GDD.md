# Final-Circle.com - Game Design Document (MVP)

## 1. Overview

**Final-Circle.com** is a browser-based battle royale shooter inspired by Fortnite and PUBG but stripped down to its core mechanics. The game focuses on gunplay and survival, eliminating complex mechanics like building, vehicles, and special abilities. It is designed as an MVP (Minimum Viable Product) to test gameplay viability and performance.

## 2. Game Mechanics & Features

### 2.1 Players & Matches

- **Max Players:** 20-50 per match (adjustable based on testing and performance)
- **Match Duration:** ~10-15 minutes
- **Shrinking Play Area:** Circular zone that gradually shrinks over time, forcing player encounters

### 2.2 Weapons

- **Basic Firearms:**
  - Pistol
  - Rifle
  - Shotgun
  - SMG
  - Sniper
- **No Special Weapons:** No explosives, grenades, or futuristic guns
- **Ammo Management:** Limited ammo to encourage strategic use

### 2.3 Gameplay Mechanics

- **Landing:** Players start at random spawn points
- **Looting:** Weapons and ammo randomly placed across the map
- **Combat:** Simple hit-detection with recoil and accuracy mechanics
- **Health System:** Players have a single health bar with no regenerating health
- **Victory Condition:** Last player standing wins

## 3. Technical Stack

### 3.1 Frontend

- **Game Engine:** Whatever brings the best performance, must be 3D
- **Rendering:** WebGL for optimized performance

### 3.2 Backend

- **Networking:** Standard WebSockets using Go
- **Server-Side:** Go for match management and game state
- **Anti-Cheat:** Basic server-side validation (e.g., movement speed, damage verification)

## 4. Art Style & Graphics

- **Style:** Minimalistic, low-poly, or simple geometric shapes
- **Color Scheme:** Muted earthy tones (greens, browns, grays) for an immersive atmosphere
- **Animations:** Basic character movement and shooting effects

## 5. Game Progression

- **Ranking System:** Basic ELO-style ranking for matchmaking
- **Stats Tracking:**
  - Kill/Death ratio
  - Wins
  - Accuracy
  - Survival time
- **Unlockables:** None in MVP (possible future skins or cosmetics)

## 6. Multiplayer Infrastructure

- **Matchmaking:** Simple, skill-based grouping
- **Game Modes:** Solo only (expandable to duo/squad later)
- **Communication:** No voice chat, only basic text-based pings or chat

## 7. Performance Targets & Optimization

- **Target FPS:** 60 FPS for smooth gameplay
- **Minimum Requirements:** Mid-range desktops & modern mobile browsers
- **Optimization Techniques:**
  - Server-authoritative hit registration
  - Delta compression for network updates
  - Simplified physics for low latency

## 8. Future Enhancements (Post-MVP Considerations)

- **New Weapons:** More firearm variations
- **Customization:** Player skins and cosmetic items
- **New Maps:** Additional battlegrounds with different layouts
- **Ranked Mode:** Advanced matchmaking and ELO progression
- **Mobile Optimization:** Further improvements for mobile devices

---

This document serves as a foundational plan for **Final-Circle.com**. The focus is on simplicity, accessibility, and tight gameplay mechanics. Once the MVP is tested, additional features can be iteratively added based on player feedback.

**Next Steps:**

1. Develop a prototype with core mechanics
2. Test networking performance and server load
3. Conduct closed alpha testing for gameplay feedback
4. Optimize and expand based on early testing data
