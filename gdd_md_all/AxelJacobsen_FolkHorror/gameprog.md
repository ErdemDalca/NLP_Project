# gameprog
## Group members
List of group members:
- Lars Lahlum Ruud
- Axel Elias Wollebekk Jacobsen
- Daniel Hao Huynh
- Maren Skårestuen Grindal

## Individual report
Individual reports can be found here: [Reports](./Reports/)

## Game design document
The game design document can be found here: [GDD](./game_design_document.pdf) 

We have not really used the document that much. It was great at the very beginning of the project, as it showed us what parts we had to think about. It also helped to make sure we were all on the same page about game design.

## Work distribution
|-        |Lars   |Axel   |Daniel |Maren|
|---------|-------|-------|-------|-----|
|Player   |Most   |Some   |Some   |     |
|Enemies  |All    |       |       |     |
|Boss     |All    |       |       |     |
|Effects  |All    |       |       |     |
|Items    |All    |       |       |     |
|Map      |       |All    |       |     |
|Meshes   |       |All    |       |     |
|Scene composition||Most  |Some   |Some |
|Prefabs  |Most   |Some   |Some   |Touched     |
|Camera   |All    |Touched|       |     |
|Dialogue |       |       |       |All  |
|Quest    |Touched|       |       |All  |
|Shop     |       |Touched|All    |     |
|Tutorial |Touched|       |       |All  |
|Audio    |Some   |       |Most   |     |
|UI       |Touched|       |Half   |Half |
|Art      |Half   |       |Half   |Some |
|SceneMove|All    |Touched|       |     |

## Gameplay video
The gameplay video can be found here: [Gameplay](https://www.youtube.com/watch?v=F-kSJ7kDnZo)<br>
Note: After uploading this video, items were rebalanced and snow+wind added to the final boss.

## Code video
We decided to not make a code video.

## Game engine
When discussing which game engine to use, we quickly agreed on Unity. We all had little to no experience with it, and most of us were not even familiar with C#, but for creating our little 2.5D game it seemed like the best option. Unreal Engine would be more suited for a completely 3D game and GoDot for a 2D game, while Unity fell somewhere in the middle. After a bit of searching we found multiple forum posts agreeing on Unity being the best choice for a 2.5D Indie game, as it’s easy to get into and set up both 2D and 3D elements in the same scene. It also has a large indie community, which makes finding tutorials and answers to questions often easy.

When initially setting up unity for collaborative work, we quickly found multiple suggestions on how to do it. We experimented with using Unity Teams, but it had a limited number of cooperators. Secondly we tried to use Unity Collaborate, but it was outdated and replaced with Plastic SCM. At this point we found a forum post detailing how to set up your .gitignore for collaborative work in Unity, which we decided on using as we were well versed with GIT already.

Using Unity was more bothersome than first suspected. Many forum posts and tutorials were outdated and unusable, as unity recently changed a lot of its systems. Unity’s official documentation was luckily easy to use and navigate, which made the process much easier. Merging scenes in Unity also proved to be a lot of work sometimes, but we mainly kept to our own scenes which kept it clean.

## Development process
[Conceptual Moodboard](https://github.com/AxelJacobsen/FolkHorror/blob/main/Dev_Moodboard.pdf)<br>
We followed an agile development process, where weekly meetings were held on tuesdays. During these meetings each team member showed what they had done since the last meeting, and problems encountered were discussed. This made it possible to give each other feedback and acquire new knowledge. As we all worked on separate parts of the project, it was interesting and educational to see how other aspects worked.

After we had gone through everyone's work, it was time for planning work for the next week. We picked issues from the backlog, and assigned them to a team member. We made sure to not assign too many tasks to each person, as they were mostly only worked on for a week at a time.

We used Discord as a communication tool. The weekly meetings were held there, and if needed we sent messages throughout the week to discuss problems or changing plans.

## Version control
We used GitHub as our version control system. To keep track of issues and the state of the project, we utilized GitHub’s project feature. This feature lets you create a kanban board, with custom columns (status) to place issues in. We had the following columns in our project:
- Backlog - project backlog 
- In progress - issues that are being worked on 
- Deadline - issues that have a set deadline 
- In review - issues that are done, but needs to be reviewed during the next meeting 
- Done - closed issues 

This feature allowed us to keep track of all group members’ progress, and ensured we were on the same page. Each issue was labeled with a priority and a size label. This ensured we did not take on more responsibility than we could handle during the week. 

When a group member started working on a new issue, a branch was created. We did not have a set development branch, but merged the feature branches directly to the main branch. When making commits to the branch, the commit message contained a reference to the issue it was connected to. By doing this, we could quickly get an overview of what had been worked on. 

Before merging a feature branch to the main branch, we usually did a code review. The developer opened a pull request and another team member reviewed it. Some things the reviewer looked for were code documentation, big red flags and redundant code. As we all have different experiences and strengths, both the reviewer and the developer learned from each other.

Link to the project: https://github.com/users/AxelJacobsen/projects/3
