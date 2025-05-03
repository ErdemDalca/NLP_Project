# Game Design Document

<b>Title</b>: Cats Out of the Bag \
<b>Description</b>: Rougelike match-3 game

The game starts on a game board. This game board can be different shapes and sizes.
Level 1 starts with a 7x7 grid.

Player starts with a bag of items (starting number TBD). \
Top tray is filled with items from the bag. \
Items fall from the tray into the grid. \
There is 1 item per square with different colors, patterns, and materials. \
Player selects and moves item one space in cardinal direction. \
Matching 3+ pops items off the grid back into the bag. \
Items fall and may combo to more matches. \
Matched items are replaced from the tray until empty. \
If the tray is empty, no more items are replaced. \
Once all matches are finished, items from the bag are returned to the tray.

In between levels are shops to purchase power-ups or consumables that increase score \
or manipulate the bag of items. 

Players earn money per match, power-up effects, or consumable effects. 

See <i>Item designs</i>.

## Item designs
### Cats
White \
Gray \
Black \
Orange \
Calico \
Tabby 

### Collar
No bell - None \
Silver - Adds points \
Cat tag - Dropping increases odds of breaking below item by 25% per square \
Gold - Adds money \
Red  - Adds combo 

### Specials
None - None \
Horizontal - clears horizontal according to power \
Vertical - clears vertical according to power \
Bomb - clears neighbors according to power \
Rotate - rotates neighbors and becomes random color \
CTRL-F - clears swapped color 
