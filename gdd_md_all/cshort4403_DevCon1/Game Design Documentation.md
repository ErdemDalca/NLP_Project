
# Dev Con 1 Game Design Documentation  

#### 9/14/2024  

**Chris**  
- Add third person character controller  
	- [Starter Assets ThirdPerson by Unity Technologies](https://assetstore.unity.com/packages/essentials/starter-assets-thirdperson-updates-in-new-charactercontroller-pa-196526)
- Add simple geometry for testing  

#### 9/17/2024  

**Chris**  
- Add portal manager class  
	- Handles creation and destruction of portals  
	- Manages lifespan of portals and makes sure there is only two  
	- Handles traversal of objects through the portals  
- Attach portal manager class to empty game object in the scene

  #### 9/18/2024

  **Ethan**
  - Added portal asset with rigidbody and collision
    	- [Magic Effects FREE by Hovl Studio](https://assetstore.unity.com/packages/vfx/particles/spells/magic-effects-free-247933)
  - Create empty game object called "PortalManager" and add the PortalManager script to it

#### 9/19/2024

**Parker**
- Added portal placement to the character controller
	- Added collision checking so player can't place portals inside colliders.
- Created empty game object that is a child of the player, object's transform determines where portal is placed.  

#### 9/23/2024

**Chris**
- Merge portal placement into main and create testing logic branch to bring it all together
- Fixed bug where portals were not deleting.
- Portals place properly but there is a bug moving the player.

#### 9/23/2024

**Ethan**
- Started designing the map and created a "tutorial" level with the following packs
- [Destroyed Building Kit - Demo by Loknar Studio](https://assetstore.unity.com/packages/3d/environments/destroyed-building-kit-demo-174899)
- [Flooded Grounds by Sandro T](https://assetstore.unity.com/packages/3d/environments/flooded-grounds-48529)
- Implemented post-processing
- Added electricity effect to character

#### 9/24/2024

**Chris**
- Fixed portal not teleporting bug by disabling character controller during transit  
- Added cooldown timer for teleport so that the player does not get stuck in an infinite loop  

#### 9/25/2024

**Ethan**
- Implemented place portal animation from [Mixamo](https://www.mixamo.com/#/)
- Created audio source sound effect for placing a portal [Freesound](https://freesound.org/people/User391915396/sounds/683828/)

#### 9/26/2024

**Chris**
- Added raycasting to place the portal
- Added rotating the portal to the normal of the target
- Added offset so portal no longer clips into the wall
- Fixed bugs
- Added git lfs to track .tif files

**Parker**
- Added the GDD to repository
  - Detailed out our game mechanic, objective statement, design rationale, and resources
  - Formatted it as a markdown file

