# POC Town Management Minigame Design Document

## Premise
An ancient evil awakens and attacks a medieval human kingdom. As the war draws on, towns fall and innocents are killed. Humanities end is near. Strong men and, women, who are willing to risk their lives on the bloody battlefields, are called into action to make the last glorious stand against the invading forces of evil. Unfortunately, you are not one of these brave fighters. You could not defeat a demon imp if your life depended on it. Frankly, the thought of toddling along for weeks, fighting desperate battles and scavenging hellish artifacts does not seem very appealing to you. Especially since adventurers don't earn much anyway.
Instead, you decide to take on a different role, as a quartermaster and a military advisor to your hometown. Your job would be to plan missions into enemy territory and supply the adventurers, which are tasked with fulfilling them. Every successful mission brings invaluable artifacts and pushes back the forces of evil.
Perhaps your efforts will mark the turning point of the war.

## Gameloop
### Primary Tasks
The players have two primary tasks:
- maintain an inventory of provisions and equipment for adventurers
- plan missions for adventurers to retrieve loot and influence the game world

### Challenges
The challenges for the player are:
- keep inventory balanced (e.g., don't run out of provisions for the adventurers)
- decide on the right amount of risk for the missions (too much risk -> adventurers die -> negative outcomes)
- decide on the right targets for the missions (sometimes it could be better to attack an evil camp that supplies an evil fortress, then to attack the fortress head on)

## World Map
The world map consists of enemy and allied settlements.
The player has control only over one settlement, which will serve as a starting point for player missions. After a mission is finished, parties will return to the settlement, which issued the mission.

![POC Town Management Minigame Design Document World Map](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20World%20Map.excalidraw.svg)

Settlements project control zones, which may have positive or negative effects on adventuring parties. When settlements are destroyed by a raid, their control zones also vanish.

![POC Town Management Minigame Design Document Control Zones](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20Control%20Zones.excalidraw.svg)
![POC Town Management Minigame Design Document Plan Missions](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20Plan%20Missions.excalidraw.svg)
![POC Town Management Minigame Design Document party customization UI](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20party%20customization%20UI.excalidraw.svg)
![POC Town Management Minigame Design Document parties fulfill missions](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20parties%20fulfill%20missions.excalidraw.svg)
![POC Town Management Minigame Design Document Destroyed Settlements](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20Destroyed%20Settlements.excalidraw.svg)
![POC Town Management Minigame Design Document reinforce missions](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20reinforce%20missions.excalidraw.svg)

## Encounters
When entering enemy control zones, encounter enemy parties.
![POC Town Management Minigame Design Document control zones generate encounters](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20control%20zones%20generate%20encounters.excalidraw.svg)

Encounters are mostly automatic. Maybe later implement player micromanagement for queuing abilities.
![POC Town Management Minigame Design Document Encounter UI](Media/POC%20Town%20Management%20Minigame%20Design%20Document%20Encounter%20UI.excalidraw.svg)

# Rough Task overview
For the POC only need the basic necessities:
- [ ] map
	- [ ] settlements
	- [ ] control zones
- [ ] missions planning
	- [ ] player
	- [ ] allies
	- [ ] enemies
- [ ] parties
	- [ ] party inventory
	- [ ] parties movement and return movement
- [ ] auto battle encounters
- [ ] loot rewards
- [ ] settlement destruction
	- [ ] enemy raids
- [ ] enemy settlement expansion ai