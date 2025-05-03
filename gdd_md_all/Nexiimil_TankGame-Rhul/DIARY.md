# Project Diary - Building a Game
## 28/09/2022
This diary has been created to keep myself in line with my goals, as well as actually being able to outline them here over time. Currently, i have:
 - A project plan draft with all the key sections
 - This repo cloned for editting .md files in VSCode
 - Some small collection of papers/books/games for reserach and analysis
 - A proof of concept for auto-tiling rooms correctly in Unity
 - A loose game design document
 - ideas i havent writen out, which im gonna do below

What i am doing right now:
 - The second draft of my project plan, tuning back the abstract, because its a page long
 - Figuring out how i want to format this diary
 - Getting unity to work with this gitlab repo

Final goals:
 - A game with some form of PCG, a character to navigate with, and enemies to defeat
 - A detailed report on all the complexities of the above task, especially noting all the Design Patterns

 ---
## 29/09/2022
I have modified my initial draft of my project plan, replacing the risk table for a more verbose risk assessment section. I have inserted a gantt chart, and further broken down my almost biweekly/triweekly time plan into a weekly breakdown, bar 2 weeks, in which coding large sections of the final game may take much more time and effort.

---
## 02/10/2022
Handed in my second draft of my project plan to my supervisor, with much more detail on what i will be using to do my research, what proof on concepts, reports and test tools i will be writing, and have written notes next to each of my milestones as to why each one is important. I will commit it to my Gitlab once it has been looked over tomorrow, in my meeting with Hugh.

---
## 03/10/2022

### Meeting notes

Two things to note

    Abstract:
        Acts like a pre-summary, 2 paragraphs
        Sentence 1: purpose of the paper
        Sentence 2: what it contains

    Bibliography:
        References and bibliography could serve as 1

---
## 04/10/2022

Uploaded my current unity files to the repo, realised that it was trying to sync my Library files, which unity generates itself, to the repo as well, which was trying to commit 10k file changes, which is not ideal, so a .gitignore was also added to make sure there was no issue. Was quite scary to see 10k additions. Turns out it was only about 150 files instead, and i dont think i even needed to commit my logs, or usersettings folders, but figured since nothing online mentioned it, i would simply commit them anyways, i can remove them later if they become an active issue.

---
## 05/10/2022
managed to complete a proof of conecpt, i have all basic motion and collision sorted, i now just need to focus on research and the further proof of concepts until i have a prototype. The prototype should be super required until my interim, but the prood of concept is good for my next meeting with Hugh. Next bit of research i will focus on is likely the major elements of a roguelike game, just so i can have everything i need infront of my when developing proofs of concpets, because in thoery all proofs can be derived from that bit of research in some form.

---
## 07/10/2022
Made some tweeks to accomodate for a slight bug in the collision on my proof of concept, and i understand now why the bug existed too.

---
## 10/10/2022
 I have done some product research that i will upload very soon, as its almost finished. I currently am also working on a document that would outline the thoeretical algorithms and structures i would be able to apply to my project, allowing me to place my thoughts onto a single document that i can go back to whenever i need. I may have both of these documents converted into markdown, for a similar format to what i have in this diary here. These bits of research can later be translated to LaTeX, but i currently use VsCode to write this diary, which syncs to the gitlab repo for me, and if im writing my history into that repo, writing my research bit by bit is doing exactly that, rather than writing into google docs and transfering it over in pdf form when im finished.

 ---
 ## 18/10/2022
 After 8 days of little to show for myself i have reminded myself i need to actually update this diary and the gitlab in order for progress to be made. doing things on my own machine doesnt mean much if the history cant be seen, so i am uploading the current state of notes into the notes section. I may have to reorganise them later if i add to them in the future.

 ---
 ## 19/10/022
 I have finalised the roation method for enemeies to envoke, in order to track the player. It was very difficult, and requried me to learn about quaternions, which are really not very fun to learn about either, i will need to explain these in my vive, but roughly, its a method to rotate a 3D object using 4 dimensions, x,y,z, and an additional w imaginary number. It is not directly linked to Euler rotation with degrees, and i need to convert euler rotations to Quaternions to use them on my transforms.

 ---
 ## 21/10/2022
 I have begun work on a damage system for the proijecftiles that the player and the enemies can shoot. Main issue right now is that the projeciles will also be able to collide, and i have realised that my code is less than ideal modularity wise, so i will need to a small refactor ro make sure i am not depending on single classes for many functions, this is not how Dave taught me, and i intend to correct for this.

 ---
 ## 25/10/2022
 ### Meeting Notes

    Hugh mentioned that i have no real evidence of formal testing, which is true. I need to outline how i am doing my testing, as i have actually been doing it, but it isnt very obvious at all. Essentially, sinc ei cannot isolate my scripts from the game environment, i will need to write tests that i can perform in the game, therefore acting as unity tests. I do also need to start writing my document in which i breakdown my required design patterns, a UML may go will with this.
 
---

 ## 28/10/2022
 I have finished the damage system, and finally gotten round to updating my diary, again, as i had forgotten. The refactor is next on the list to do, which i should be able to do very soon. I will need to work on a simple item system within the next 2 weeks. This is a very achievable task.

---
 ## 01/11/2022
 I had to take a brief break due to personal matters, but I have started to construct the documents requested of me, beginning with the testing document, outlining what I need to perform in order to ensure elements of my code that i cannot test automatically work.

---

## 04/11/2022
I am currently working on several courseworks, so work on this project has been slow, but i have written most of my testing document, and now am writing my design patterns document. The resources stipulated by the brief have been very useful.

---

 ## 08/11/2022
 Due to other courseworks, my attention had been diverted to other important submissions, but i can now continue with the design patterns doument for my meeting later today with Hugh. I have created the shell of my interim report, placing the headers where i think they should be.

 ### Meeting Notes

    I should divide mny paragraphs into theory and application to stand the best chnace of deswcibing what i intend to descibe concisely. i have a habit of being execcsively verbose when i dont think i've put the meaning of what ive written across very well. The design patterns document could do with some diagrams and some areas of the test documuent need clarity. I also need to focus on referencing everything i can, re-digging up any websites or papers i have read.

---

 ## 12/11/2022
 I have decided it is likely important to push back my item system into the second term/winter break in order to complete my interrim submissions. This time will be addressed in my evaluation of my planning. I need to start working on diagrams for my design patterns, but for now i am writing up all the theory i have learned for this project. I will likely be tight on time, but i will be able to manage.

 ---

 ## 22/11/2022
I have been writing my interim report non-stop for over the last week, from the 14th-ish, and it has been read by Hugh, who i had a meeting with today to discuss it.

Meeting notes:

    - There are a few sections i do not need right now, i need to focus on aligning my time with the actual mark scheme.
    - I need to reference everything i write, nowhere near enough references
    - Software engineering section is good, but needs refrences and how im using each pattern clearly.
    - Need to clearly mark what i've actually schieved
    - I need to stop focussing on game design as opposed to software design.
    - Reformat my product analysis notes into a table, more useful that way
    - Need to paste in this diary.
    - Need to re-explain quaternions, and why i use them
    - label every image and table
    - provide definitions from literature to all precise terms

---

 ## 18/01/2023
This will be a very large diary entry, as i have been putting off writing up what i have been up to over the winter holidays.
To my knowledge, i am not graded on stuff i do over the winter, however, i did need the extra time to insert elemenets i had not thoroughly considered.

Over winter i finished the proof of concept for GUIs, and will likely add in some nice quality of life ones later, like the victory/death screen, and perhaps some item pickup flair. I had started work on the item system as well.

I have as of 2 hours ago finished writing the system and JSON template to import items into my game, in such a way that i can simply add whatever item i want, as long as its on the end of that JSON text file. This is a huge step in the further development of my game, and noiw i just need to have these items be interacted with physically by the player, such that they can be picked up, and the stats applied to the player. All stats have been unified into a single stat array, which works very well, decoupling a ton of code. In theory, new stats could even be added in, simply by adding them to the dictionary, and any class that were made in the future, could simply ask for that stat as a key from the dictionary and retrieve the stat.
I feel incredibly motivated now, as i have spent several hours solving this item import issue, and much like many problems, was actually solved rather neatly, with very little code. Turns out JSON deserializers are not a huge fan of Dictionaries, so i wrapped aech dictionary into a class, and it worked. Unity doesnt let me peer into dictionaries from the inspector, so i'll write some code probing the stats of each item, likely a .toString override in the item class. After the item system is complete, the only major system left will be random generation, which has several steps:
Map generation
Map visualisation
Room Templating
Enemy Templating
And integration hell.
I look forward to working on generation very soon.
My next steps are to create an item prefab, and find a way to generate a reward to strap to it, spawning it in the test room once all enemies have been killed.

 ## 09/02/2023
I have finally finished the item system for my game, at least fundamentally. Stats, effects and items images are all important from external files, and Items can be loaded from Json. Loading whole C# scripts as may have wanted to do with effects seems to be slightly out of scope compared to what i can achieve at the moment. Stats can indeed be added at will through items, but without effects to use them, the amount a modder could do with custom stats is basically none.

Adding QoL elements will come after each system is finished. The above steps stand true in my previous entry, as my next step is to do map generation. This will largely be coded in a much rawer C# script, only interacting with Unity for the minimap and room navigation.
I will later also work on trimming down how much 'Unity' is packaged with the game, while im very happy with a 48mb game size, i think some of the Dlls it packages are still largely unneccesary(?).
I have given myself some slack days before starting this next system to get a mental refresh before i have to think in a more graph-oriented manner, but i should be able to outline my approach today.

Currently my plan is to implement some floorgenerator which takes a number of rooms to generate, and attempts to generate rooms from a given root room breadth-first. Dead-ends will be placed on a stack, and then the furthest dead-end, which will be generated last, will become the boss room.

Visually, i'll need to draw out the map, which should be simple enough, given that my sprites are of a known size.

 ## 15/02/2023
The minimap now renders appropriately, as if finished most of my first and second major algorithm for generation: creating rooms, and displaying them graphically
Now i just need to make these rooms work for the player to traverse between them

 ## 22/02/2023
the map generation proof is essentially completed in its most fundamental form, the rooms are traversable, the player can go room to room and kill enenmies in order to get an item. Rooms also have a memory of sorts, allowing players to come back for items they've not yet picked up, and players can descend to new floors.
Polish and some additional minor features can now be added.

 ## 02/03/2023
Terrain templates can now be loaded into rooms, allowing for a unique way of playing each room from each door. did some reorganising of enemies and how they are loaded in as well. 

 ## 11/03/2023
Playtesting revealed:
 - a need for the death screen
 - a small health bug
 - and a lack of visible controls