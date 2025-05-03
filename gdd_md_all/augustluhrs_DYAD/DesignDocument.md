# Game Design Document
---
### Rough Sketch for now

## Design Guidelines
---
### Overall System
1. Unity version 2019.3.7f1
2. AR Packages
   1. AR Foundation 3.0.1
   2. AR Subsystems 3.0.0
   3. ARCore 3.0.1
   4. ARKit 3.0.1
3. VS Code
4. Build Settings
   1. Android
      - Remove Vulkan from Graphics APIs
      - Uncheck Multithreaded Rendering
      - Minimum API Level: Android 8.0 "Oreo"
      - Package Name: com.augustluhrs.DYAD_AR
      - Default Orientation: Landscape Right (camera by right hand, opposite left scroll
   2. iOS
      - Package Name: com.augustluhrs.DYAD_AR
      - Camera Usage Description: "Camera is required for AR"
      - target minimum iOS version: 11.0
      - Architecture: ARM64
      - Default Orientation: Landscape Right (camera by right hand, opposite left scroll

### Assets/Resources
1. Prefab Settings
   - All prefabs scaled to .8 for now 
   - Name standard = "AR_FurnitureName_color" (note capitalization)
   - Have to attach PhotonView and MySynchronizationScript

### Editor//UI
1. Canvas
   - Canvas Scaler: Scale to Screen Size && Expand
     - Nope that doesn't work either...
   - Okay, gotta anchor to the corners!
### Level Prefabs
1. Model
   - Going pretty freeform right now with walls and colliders other than using the average sqft as a guide.
   - Should redo these, maybe in blender
2. Colliders
   - Arbitrary height -- 15?
3. Text
   - Character size .01
   - Font Size 100
   - Scale all 1
   - Center everything
4. Colors
   - Material a pale yellow
   - Text a pale blue

### Github Practices
- went ahead and made AR the master, will probably push to master every major feature/version? (current version... 0.3.3?)
