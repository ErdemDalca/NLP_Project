[ Game Design Document ]

---SCENARIO---

The player will play as a firm in a capitalist economy.

The player will have the initial choice of one company type:

coffee shop

The player will have to make microeconomic decisions to help the firm stay afloat,

but macroeconomic decisions will be made by the Government.


---GAME MECHANICS---

The player will be able to change their product prices, based on the supply levels in the geographical area.

The player will be able to change the quality of their products, leading to good/bad online reviews.

The player will be asked to make ethical decisions, which will affect consumer's opinions of their brand.

The player will be able to control the location of the coffee shop, (higher rent on the high street, dirt cheap in the middle of nowhere).

The player will be able to view the current economic report for the month whenever they want.

Time will pass (one day is 30 seconds irl).

Every month, the economic report will be delivered to the player, with statistics based on how they are doing.

The player will be able to pay for marketing to attempt to boost their brand.

[MAYBE] The player will be able to manage staff (hire, fire, discipline and reward) based on performance.

As customers enter the shop, they will each have a maximum number of products they will buy.

-These products will be randomly selected based on the current supply/demand for the product

[MAYBE] The play will need to manage supply levels of each product

-Too many and the product goes out of date without making any money

-Too few and the product sells out, and therefore doesn't make any money.

[MAYBE] The game will have a difficulty system, caused by the economy state. (Difficult may mean the macroeconomy is in a recession state).


---GRAPHICS/UI---

The UI will be a console based menu.

[MAYBE] Two consoles, one for the player interaction (menus, information etc). The other for the monthly report/current time of day?

---TECHNICAL DETAILS---

The storage of the save will be done via text file.

-Databases are large and unnecessary for such a simple storage system.

-This allows me to store things in a "one file fits all" kinda way.

"Locations" and firm types should be stored in text files, then read when the game boots up.

-This will make adding new firm types/locations super easy.

Due to the nature of how the files work, the game will auto-save.

Maybe it can take a backup of the file every 30 minutes or so? So if anything is corrupted it can be automatically rolled back.

-If this is implemented, include the time that the file was backed up, as well as how long the user has played since then.

-This will allow text like the following:

"Your game save was corrupted, we have rolled back to the latest backup, which was taken 7 minutes ago."
