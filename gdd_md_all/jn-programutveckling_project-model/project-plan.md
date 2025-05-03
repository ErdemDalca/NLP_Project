# Background

Explain why there is a need for the project and describe the original idea behind it. Tie that to the project purpose and perhaps also how the project can contribute to overall business benefit.

# Purpose

For what effects will the project aim? Describe what the outcome will be when the project is finished, for example:

> This racing game will be a short and relaxing distraction while commuting.

> This budgeting software will help small businesses and households to keep track of their vacation money.

# Budget

Define the budget parameters and constraints in terms of money and time. Not so important with my own projects, but useful when it comes to contract work.

# Activities

When planning what to do and when to do it, normally one would first create a work breakdown structure, WBS for short, to list everything that needs to be done to meet the project goals and requirements, regardless of the order in which they need to be done. Then with the WBS in hand, one would construct a network map, in which the time line of when to do each thing and in which order is made visible.

However, because I work alone, I feel that this process is too cumbersome to do in multiple steps. Therefore these steps are merged into one in my project model. I still go through the aforementioned steps, but only implicitly. I don't maintain separate documents for the WBS and network map; instead I combine them in a table in this very document, for example:

> Latest assigned ID: 3
>
> | ID   | Description                                           | Priority (MoSCoW) |
> | ---- | ----------------------------------------------------- | ----------------- |
> | 1    | Ability to save the open document to disk.            | M                 |
> | 2    | Ability to print the open document.                   | S                 |
> | 3    | Auto-save the open document in ten-minutes intervals. | C                 |

As one can see, the table is sorted by priority, which is based on MoSCoW ("must have", "should have", "could have", "won't have"). Take care to order the activities in such a way not to break any dependencies. A higher priority activity shouldn't be placed before a lower priority activity, if the latter needs to be completed before the former. 

The line *Latest assigned ID* is just meant to keep track of assigned ID's if the activity list gets unwieldy.

Don't forget that documentation and design are also important activities to include. This is more important in larger or complex projects, for example in game development, a game design document is very important and should absolutely be part of the activities.

The list of activities can, and should, be revisited many times throughout the lifetime of the project, whether it is to add new items, remove finished items or something else.

If there is a budget in place, the activities should also take into account duration (how many time units I expect to work on this activity) and cost (how much this activity is expected to cost).

# Limitations

It's a good idea to make any limitations to the scope explicit in the project plan. Doing that reduces the risk of so-called scope creep, a situation where one slowly and often without noticing expands the scope of a project beyond what was initially planned and budgeted for. These limitations can both be defined on the project level or feature level. An example of limitations on a feature can be as follows:

> We will not implement the ability to login via physical pass cards.

# Delivery or integration

Describe how the end product should be delivered or integrated into a target environment. Where the product should be made available, at which price etc. 

Also describe how any intermediary deliveries will be handled in this regard. Software is rarely really finished, so it's fair to say that all but abandonware is in an intermediary stage.