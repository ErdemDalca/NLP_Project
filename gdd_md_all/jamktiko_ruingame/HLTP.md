# High Level Test Plan
**RUIN GAME**

Authors:

Aapo Hyyryläinen

**VERSION NUMBER 1.1**

## Table of Contents 

- [High Level Test Plan](#high-level-test-plan)
  * [References](#references)
  * [Intro](#intro)
    + [Project Introduction](#project-introduction)
    + [Purpose of this document](#purpose-of-this-document)
  * [Testing Strategy](#testing-strategy)
    + [Testing Subjects](#testing-subjects)
    + [Testing Activities](#testing-activities)
    + [Features to be tested](#features-to-be-tested)
    + [Features not to be tested](#features-not-to-be-tested)
  * [Testing Approach](#testing-approach)
    + [Key Principles applied](#key-principles-applied)
    + [Testing constraints](#testing-constraints)
    + [Acceptance Criteria](#acceptance-criteria)
    + [Testing pausing and continuation](#testing-pausing-and-continuation)
  * [Products](#products)
  * [Environment](#environment)
  * [Responsibilities](#responsibilities)
  * [Expertise and Guidance](#expertise-and-guidance)
  * [Timetables and milestones](#timetables-and-milestones)
  * [Risks](#risks)
  * [Assumptions and dependencies](#assumptions-and-dependencies)

## References

[Project plan](./ProjectPlan.md)

[Game Design Document](./GDD.md)

[Bug report form](https://docs.google.com/spreadsheets/d/1UkeBcV-mZ7PwsgvJWJJCiUxvYgYJ5370cGh-ks6_nQg/edit?usp=sharing)

## Intro

### Project Introduction

RUIN is an upcoming third-person action roguelite developed as a part of TiCorporate 2021 Demo Lab. The development project aims to develop 3 proof of concept demos

### Purpose of this document

The following document aims to explain the course of action taken to test the concept and product of RUIN. 

## Testing Strategy

### Testing Subjects

- **Testing** will use a balanced mix of Screenshots from game view, Video recording for finding bug origin and written recreation steps.

- **Concept testing**; The concept will be shown to peers at TiCorporate and testing will aim to collect feedback in the following categories: Visual, Story, Gameplay and Overall feeling.  Possible testing done with people outside of TiCorporate if possible.

- **Demo testing;** The project will produce 3 playable demos during it's lifespan and as such, each will be introduced to the project group and other available testers for feedback in the following categories: Visual, Gameplay and Overall feeling.

- **QA Testing**; The project will also be handled by testers weekly where bugs will be reported in a concise manner described in the Testing Activities chapter. The concept and gameplay feel will be tested through the product owner.

- **Tested items** will be showcased through online video chat due to Covid-19 limitations and if possible, shown on the developer's system. Any deliverables will be given through OneDrive and Google Drive.

### Testing Activities

- Testing will be conducted bi-weekly via a gameplay test and concept evaluation discussion. 

- Feedback will be submitted via a form or recorded by a member of the testing team.

- This testing will be done internally and feedback will be collected from the project group and product owner. Bugs found in the demo will be reported in the following manner:

  - Can it be described via text? Add it to the bug reporting list with a concise description. If not ->
  - Can it be described via a screenshot? Add it to the bug reporting list with a screenshot of the problem. If not ->
  - Can it be described via a video? Add it to the bug reporting list with a video file attached of the problem. If not ->
  - After checking the above, evaluate the severity of the bug using the following criteria:
    
    - **Blocker**; No further testing can be done at the moment
    - **Critical**; Application crashes, Loss of Data.
    - **Major**: Major loss of function
    - **Minor**: Minor loss of function.
    - **Trivial**:  Graphical or feel issue or a result from other bugs.
    - **Feature**
    
  - The description consists of at least the following: Bug Id, Reproduction Steps and Evaluation
  - Other testing sessions will be arranged through TiCorporate where more feedback can be gathered but testing will be done in a larger scale where issues and singular bugs can     be ignored.
  
The following 4 step process will be used for testing:
1. Identify the bug 
2. Report the bug using the previously mentioned guidelines (RED)
3. Analyse the bug (YELLOW)
4. Verify that the bug has been fixed. (GREEN)

The state of the bug will also be maintained using these 3  phases in sync with a color code in the bug reporting file. 

Testing will also take advantage of the professional guidance provided by JAMK where hard to fix and find bugs will be presented to the appropriate faculty member to seek guidance in fixing them.

### Features to be tested

Using manual testing, all current features are tested through functional testing. Functional testing is done to determine process, load durability, and user logic. From this, concerns over redundancies, UI flow and gameplay feel addressed through feedback from the product owner

### Features not to be tested

Game dependencies such as the Unity Game Engine will not be tested as we rely on the product to develop our game and plan to not make interruptive changes to it. 

Compatibility will not be tested due to limited availability to different machines and scope of the project being a technical demo. 

Load and multiplayer testing will not be done due to no server requirement or multiplayer intended for the project.

## Testing Approach

### Key Principles applied

- **Absence of errors fallacy**: The testing will include Concept testing due to the product itself being developed for entertainment. If the game is not enjoyable, no amount of perfect code will fix it.

- **Early Testing principle**: The testing will be done weekly to avoid major bugs and developmental issues from slipping through. This will save a lot of time during the later stages of the development cycle. 

- **Exhaustive testing is Impossible**: As we're continuously testing the product, we must avoid the fallacy that we can find all of the bugs with the limited resources we have.

### Testing constraints

- Limited amount of developers to fix bugs and develop new content at the same time Some bugs will inevitably slip through and will have to be carefully evaluated
- Limited amount of time so testing should identify key issues instead of finding minor bugs and features.
- Limited availability of testers outside of the project group due to Covid-19 limitations.
- Testing automation will only be done if the schedule allows for sufficient testing development

### Acceptance Criteria

In general, we will adapt a case-case approach on acceptance:

 - Product Owner will be responsible for gameplay feel, story guideline and world building details and such, will handle evaluating if the feature implemented corresponds to the overall vision and approach of the game.
 - Testing Supervisor will be responsible for technical analysis; Is the codebase properly done according to SOLID principles and naming conventions used in our coding guidelines.

For example: A movement system is deemed acceptable when the Product Owner deems it suitable for the game vision (Speed is fast paced, commands are fluid, controls are intuitive..) and the Testing Supervisor checks the codebase (Movement is constructed using SOLID principles)

- A feature will get a passing score from 6-10 in review when both of these criteria are met. A failing score of 1-5 will mean it will go back to testing or production depending on the disqualifying feature (Movement was slow but implemented correctly)

### Testing pausing and continuation

- Testing will be suspended if a game breaking critical or major bug that affects gameplay is found and not fixed before testing deadlines. 
  The game will not be presented in a broken state to any audience and as such, if a required demo would have a broken game version, it will be reverted to the last stable version for the showcase.

- Smoke tests will be conducted before any showcase with time to spare for possible bug fixes that could majorly affect the gameplay of the end product. The following procedure will be followed if game breaking bugs are found and reported during any testing:

  - Testing will resume after all and any Critical bugs are fixed. 
  - Severity of Major can be ignored if the feature is in progress or if the bug 
    doesn't affect the playability of a single playthrough.
      - For example: A bug that causes the player to lose control after clearing the game once due to a faulty implementation of the input system.
  - Minor and under can be ignored for showcase purposes.

## Products

- High Level Test Plan
- Bi-Weekly test reports for the Concept and Demo categories
- Organized meeting test reports for the Concept and Demo categories
- Scripts and testing data
- Bug report file. (Included in references)

## Environment

- Remote access and Video chat due to Covid-19 Limitations
- Testing Hardware will be reported in the test report in the following manner:
   - **Operating System**: Windows 10
   - **CPU**: Intel Core i7 7700K @ 4.20GHz
   - **RAM**: 16gt @ 1339mhz
   - **Graphics**: 11000 Nvidia GeForce GTX 1080 Ti
   - **Drive**: 119GB SSD
   - **Software**
    - Unity
    - Possible automated testing and TDD using Unity's Test Framework.
  
## Responsibilities

- The testing team will include the Lead Programmer and Product Owner in every test and the whole project group in major tests. Testing will also include TiCorporate personnel for organized, course wide tests.

- The development team is responsible for reporting any bugs as well as Product Owner determining the priority of bug fixing over new content.

## Expertise and Guidance

- The team has prepared a testing plan as well as provides feedback on testing progress weekly to prepare for production.

- Testers have a good understanding of gameplay balance and testing but need more experience in recording bugs comprehensively and fixing them.

- The testing team will use resources provide by JAMK to find better ways to conduct testing and planning if current planning is found inefficient for the purposes of this project.

## Timetables and milestones

<table>
  <tr>
   <td>
<strong>Event</strong>
   </td>
   <td><strong>Date</strong>
   </td>
   <td><strong>Additional information/Participants</strong>
   </td>
  </tr>
  <tr>
   <td>Preproduction Begins
   </td>
   <td>18.1.2021
   </td>
   <td>Online meeting space, Full work group.
   </td>
  </tr>
  <tr>
   <td>Initial sprint
   </td>
   <td>1.2.2021
   </td>
   <td>Online meeting space, Full work group
   </td>
  </tr>
  <tr>
   <td>Demo #1
   </td>
   <td>25.2.2021
   </td>
   <td>Online meeting space, TIKO students
   </td>
  </tr>
  <tr>
   <td>Demo #2
   </td>
   <td>1.4.2021
   </td>
   <td>TBD, Online meeting space, TIKO students
   </td>
  </tr>
  <tr>
   <td>Demo #3
   </td>
   <td>12.5.2021
   </td>
   <td>TBD, Online meeting space, Unknown
   </td>
  </tr>
  <tr>
   <td>Project ending
   </td>
   <td>12.5.2021
   </td>
   <td>Unknown
   </td>
  </tr>
</table>

Other milestones such as sprint demos are case specific and will not be listed in the overall timetabling. The same rule applies to demos arranged later on with TiCorporate personnel.

## Risks

- Limited amount of programmers doing the work meaning writing tests can be difficult to find a time and place for in addition to creating new content.

  - Limiting testing to Concept on some weeks might alleviate the need for constant codebase reconstructing
  
- Programmer exhaustion: Programmers might find testing to be inconclusive and demotivating while the game is still being made resulting in lack of documentation and poor followup.

  - Planning other ways of testing to allow programmers to refocus on creating enjoyable content, having programmers do something other than coding (ex. 2 days of 3D, Small audio recording etc.)
  
- Large and cohesive planning for testing might be too large for a small team of programmers to fully utilize.

  - Lessening the required amount of testing and feedback on a weekly basis.

## Assumptions and dependencies

- In the making of this plan our group has assumed that the majority of coding and testing work will be focused to one or two individuals, making extensive codebase testing and automation ineffective to implement due to the requirement of actually getting a demo together.

- In addition to this, we assume that there are no major bugs in the software or hardware we intend to use and can therefore assume fault in our own design of the game.

- We depend on JAMK personnel for guidance and expertise in the event of a critical or major bug that our development team cannot resolve with their current abilities








