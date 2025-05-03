# Game Design Document (GDD) - Android Escape 

  

## 1. Game Overview 

  

**Game Title:**   

*Android Escape* 

  

**Genre:**   

3D, stealth, action, puzzle. 

  

**Platform:**   

PC. 

  

**Target Audience:**   

Players who enjoy immersive stealth mechanics, puzzle-solving, and sci-fi narratives.   

Target age: 16+. 

  

--- 

  

## 2. Gameplay Overview 

  

The player takes the role of an android created in a high-security facility. The goal is to escape the facility by using a **shapeshifting mechanic** . The player must avoid detection, outsmart guards and solve environmental puzzles to make their way to freedom. 

  

### Core Gameplay Loop: 

- **Shapeshift:** Upon contact with other characters, the player takes on their form and abilities, allowing access to new areas or interactions. 

- **Infiltrate:** The player uses stealth and shapeshifting to avoid detection by guards and security systems. 

- **Escape:** Navigate through complex levels, solving puzzles, avoiding detection, and adapting to new forms to progress. 

- **Game Progression:** Unlock new forms and abilities, solve increasingly difficult environmental puzzles, and evade more complex security measures. 

  

--- 

  

## 3. Game Objectives 

  

### Primary Objective:   

Escape the facility by using the shapeshifting mechanic to overcome obstacles, avoid detection, and adapt to new forms for different challenges. 

  

--- 

  

## 4. Player Objectives (Prototype Focus) 

  

The prototype will aim to answer the following question:   

**"How does shapeshifting enhance stealth gameplay and affect player problem-solving and progression?"** 

  

--- 

  

## 5. Shapeshifting Mechanic 

  

### Shapeshifting System: 

- **Contact-Based Shapeshifting:** The player takes the form of anything when they come near it and press the F key. Each form has unique abilities and limitations. 

- **Form-Specific Abilities:** Different forms allow  access to restricted areas or the ability to bypass certain security measures. 

 --- 

  

## 6. AI Behavior and Detection System 

  

### Types of AI: 

- **Guards:** NPCs that patrol areas. They react based on the player's actions and will pursue the player if detected. 

  

### Detection System: 

- **Line of Sight:** AI reacts to the player if they are within visual range, depending on the form they have taken. Certain forms may allow the player to blend in. 

--- 

  

## 7. Puzzle Mechanics  

- **Environmental Puzzles:** Players must solve puzzles by switching between different forms. Some puzzles require physical strength and some others require the ability to bypass specific security systems. 

- **Form-Specific Progression:** Each new area of the facility introduces new forms for the player to shapeshift into which offers new ways to solve puzzles and progress. 

  

--- 

   

## 8. Progression System 

  

- **Puzzle-Based Progression:** As the player solves puzzles throughout the facility, they unlock new areas and get closer to achieving their goal of escaping.  

   

- **Form Unlocks:** With each solved puzzle, the player gains access to new forms, each providing unique abilities. These forms are essential for solving specific puzzles and going into restricted areas that bring them closer to the exit. 

    

--- 


## 9. Resources

This section lists all external assets, tools, or references that were not created by the team and have been used in the development of "Android Escape."

-**Unity Assets :**

[Asset Link](https://assetstore.unity.com/packages/3d/environments/sci-fi/sci-fi-construction-kit-modular-159280)

-**Youtube Resources:**

[Line of Sight Detection](https://youtu.be/znZXmmyBF-o)

[AI Enemy](https://youtu.be/UjkSFoLxesw)

-**AI USAGE**

The **ShapeShiftTrigger code** in unity was created by using AI.

## Code Block
```C#
using UnityEngine;
 
public class ShapeshiftTrigger : MonoBehaviour
{
    public float shapeshiftRange = 5f;           // Distance within which you can shapeshift
    public LayerMask npcLayer;                   // Layer for NPCs
    public float shapeshiftDuration = 10f;       // Time in seconds for how long the player stays shapeshifted
    private GameObject targetNPC;                // The NPC the player will shapeshift into
    private bool isShapeshifted = false;         // Track if the player is shapeshifted
    private float shapeshiftTimer = 0f;          // Timer for shapeshifting
 
    // Variables to store original player data
    private Mesh originalMesh;
    private Material[] originalMaterials;
    private RuntimeAnimatorController originalAnimatorController;
    private Avatar originalAvatar;
 
    private SkinnedMeshRenderer playerMeshRenderer;
    private Animator playerAnimator;
 
    void Start()
    {
        // Store the player's original mesh, materials, and AnimatorController
        playerMeshRenderer = GetComponentInChildren<SkinnedMeshRenderer>();
        playerAnimator = GetComponent<Animator>();
 
        originalMesh = playerMeshRenderer.sharedMesh;
        originalMaterials = playerMeshRenderer.materials;
        originalAnimatorController = playerAnimator.runtimeAnimatorController;
        originalAvatar = playerAnimator.avatar;
    }
 
    void Update()
    {
        // Detect NPC when not shapeshifted
        if (!isShapeshifted)
        {
            DetectNPC();
        }
 
        // Press 'E' to shapeshift into NPC
        if (Input.GetKeyDown(KeyCode.E) && !isShapeshifted && targetNPC != null)
        {
            Shapeshift(targetNPC);
        }
 
        // Handle shapeshift timer
        if (isShapeshifted)
        {
            shapeshiftTimer -= Time.deltaTime;
 
            // Automatically revert when the timer runs out
            if (shapeshiftTimer <= 0)
            {
                RevertToOriginalForm();
            }
        }
    }
 
    void DetectNPC()
    {
        Collider[] npcsInRange = Physics.OverlapSphere(transform.position, shapeshiftRange, npcLayer);
        if (npcsInRange.Length > 0)
        {
            targetNPC = npcsInRange[0].gameObject;
        }
    }
 
    void Shapeshift(GameObject npc)
    {
        SkinnedMeshRenderer npcMeshRenderer = npc.GetComponentInChildren<SkinnedMeshRenderer>();
 
        if (npcMeshRenderer != null)
        {
            // Swap player mesh and materials with NPC's
            playerMeshRenderer.sharedMesh = npcMeshRenderer.sharedMesh;
            playerMeshRenderer.materials = npcMeshRenderer.materials;
 
            // Swap the animation controller and avatar to match NPC
            Animator npcAnimator = npc.GetComponent<Animator>();
 
            if (npcAnimator != null)
            {
                playerAnimator.runtimeAnimatorController = npcAnimator.runtimeAnimatorController;
                playerAnimator.avatar = npcAnimator.avatar;
            }
 
            // Set the timer for the shapeshift duration
            shapeshiftTimer = shapeshiftDuration;
            isShapeshifted = true;
        }
    }
 
    void RevertToOriginalForm()
    {
        // Restore original player mesh, materials, and AnimatorController
        playerMeshRenderer.sharedMesh = originalMesh;
        playerMeshRenderer.materials = originalMaterials;
        playerAnimator.runtimeAnimatorController = originalAnimatorController;
        playerAnimator.avatar = originalAvatar;
 
        // Reset shapeshift status
        isShapeshifted = false;
    }
}
```
----
   

## 10. Conclusion 

  

The primary focus of this 3D stealth game is to explore how the **shapeshifting mechanic** can enhance stealth gameplay, affect player problem-solving, and dynamically impact progression. By analyzing how players adapt to new forms and abilities, we aim to create a unique stealth experience with varied challenges and innovative gameplay mechanics. 

  

--- 

 
