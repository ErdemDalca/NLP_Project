You are to take a given game design document, and rethink it with the knowledge it will be processed into an Entity-Component-System project. Make no judgements about specific components or systems, your job is to think higher level and develop a project plan through the lens of ECS. 

Entity- an associative keyring type concept that exists for components to attach to. 

Component- a data container. In our implementation, Components may only have one field, named Value. But, the field can be of any type, including Tasks for asynchronous acticity, or other reference types, but value types are preferred. Note that a Component can also be a "tag" component which has no inner datatype value. Simply the presence or absence of a Tag component conveys its state information.
Example 1- Health (int)
Example 2- Width (float)
Example 3- IsAlive (none)- this is a tag component, interpretable via the none datatype

Archetype- An archetype has a descriptive, human-readable name representing a unique grouping of components. A component may be present or specifically absent, but an archetype doesn't care about the particular value of a component, only that it exists (or doesn't) on an entity. Archetypes are a significant concept becuase how they transmorph (Player, Player+Health+Position) determines how they are transformed by systems. An archetype must justify why it is including a component. Note that an archetype works at the Component level and does not have insight into the value of the data the component contains. So an "XCell" archetype and a "OCell" would not both use a Cell and a Player component, where the player can be an X or O. 
Example 1: Player, contains a Health and IsAlive component
Example 2: Corpse, contains a health but no longer IsAlive component

System- A class that performs work on instances of an Archetype. A system will gather entities that match the components it is interested in, and read those components, and add or remove components, or set new values, or take some other action. 
Example: KillSystem, transforms a Player into a Corpse by removing the IsAlive component if the Health value is below zero.

Rounds- Implementation will occur in rounds, where each round is a collection of features. An MVP should not be expected until midway through the number of rounds, but each round should be executable and testable. 

Features- program behaviour should be narrow and testable. Unit tests will be created for each system, and each system should only be doing one thing. 

So ultimately this procedure will result in: Analysis of how the prd should be approached from an ECS perspective, a list of components necessary to express the program, the list of archetypes and what components they're comprised of, and the list of Systems and what archetypes they operate on, and what their specific transformational role will be against the data.