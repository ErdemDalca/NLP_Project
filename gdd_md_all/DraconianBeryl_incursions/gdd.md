# Incursions

Game Design Document

## Common Abbreviations

+ AH - Arkham Horror
+ AH2 - Arkham Horror, Second Edition
+ AH3 - Arkham Horror, Third Edition
+ AHtCG - Arkham Horror, the Card Game
+ CM - [Cthulhu Mythos](https://en.wikipedia.org/wiki/Cthulhu_mythos)
+ CO - [Candela Obscura](https://en.wikipedia.org/wiki/Candela_Obscura)
+ DMD - Death May Die
+ EH - Eldritch Horror
+ MoM - Mansions of Madness
+ MoM2 - Mansions of Madness, Second Edition
+ PACG - Pathfinder Adventure Card Game
+ SH - [Secret Histories](https://weatherfactory.biz/sixth-history-community-licence/)
+ TES - [The Elder Scrolls](https://en.wikipedia.org/wiki/The_elder_scrolls)

## Overview

### Vision

A cooperative narrative-focused board game of investigation and horror
with a sliding scope and mechanics that can go from global all the way
down to a single hideout.

### Target Characteristics

1. Mechanical tension through competing pressures
   1. Gentle, but firm, time pressure to finish the investigation before
      "bad things" happen
   2. The need to improve character capabilities to be effective in
      preventing the "bad things".
   3. Growing risk to characters as the scope narrows and as individual
      capabilities grow.
   4. Increasing difficulty as the game progresses.
2. Narrative-first encounters where the mechanics of resolution play a
   supporting role.
3. Uniformity of gameplay in all scope "zoom levels".
4. No reliance on a strict turn or round structure to drive the tempo of
   the investigation or escalate the game.
5. Systemic flexibility for the scenario to control the tempo and
   pressures.
6. Limited opportunities for there to be a long interval between a
   player taking one meaningful action and them taking their next.
7. Replayability through scenarios that define the outline of an
   investigation while being able to leave many of the details to
   chance.
8. Manages game "weight" by keeping each individual action focused and
   simple to resolve.
9. The game comes with summaries of iconography, game structure, and
   common actions in sufficient quantity for all players.

### Mechanics

Referring to things by the codes assigned by "Building Blocks of
Tabletop Game Design (second edition)" or where previously used in other
games where possible.

1. STR-02 Cooperative, or STR-04 Solo
2. STR-08 Scenario/Mission/Campaign
3. (optionally, maybe) STR-10 Legacy
4. Variant of TRN-13 Time Track - "Doom Clock"
5. ACT-12 Variable Player Powers
6. (maybe) ACT-13 Once-Per-Game Abilities
7. ACT-15 Gating and Unlocking
8. ACT-17 Events
9. ACT-18 Narrative Choice
10. RES-02 Stat Check - very much like AH2
11. RES-05 Die Icons
12. (maybe) RES-21 Rerolling and Locking
13. UNC-07 Unknown Information
14. UNC-09 Probability Management
15. UNC-10 Variable Setup
16. ECO-01 Exchanging
17. ECO-02 Trading
18. (maybe) ECO-07 Loans
19. (maybe) ECO-11 Upgrades
20. CAR-09 Tags
21. Abstract Map, a mixture of PACG, AHtCG, and other ideas
22. Variant of CAR-07 Deck Construction - combination of a variant of
    PACG combined with another mechanic "Clue Trails"
23. Extension of RES-05 Die Icons mixing in some ECO-12 Random
    Production and ACT-17 Events for "Warp and Ward Dice Corruption"

### Setting

Original IP that melds elements primarily from real-world folklore, the
Cthulhu Mythos, and the "standard" Dungeons & Dragons cosmology.  The
main world is Earthlike with magic-based technology late into their
industrial revolution.  There are many other worlds, e.g. fairy,
elemental, or shadow, and each world has its own magic.  Native magic is
safe while alien magic corrupts.  The only thing that the many alien
worlds have in common is that their natives find us tasty.

Art Style

Art style is indicative of origin, with the contemporary main world
represented by the subset of Art Nouveau by Alphonse Mucha, especially
his lithography, though perhaps reinterpreted in watercolor and ink.
Alien worlds will each be given a distinctive style and medium, for
example fairy might be slightly surrealistic oil painting, shadow might
be charcoal, and elementals might be mosaics or stained glass.  If an
illustration represents things from multiple sources then each of those
elements will be rendered in their assigned style.

* A scene showing a fire elemental in a local street would show the
  street in the typical Art Nouveau while the creature might be stained
  glass.
* A portrait of a character who has been tainted by shadow might have
  one body part that is partially, or completely, drawn in (or drawn
  over with) charcoal.

## Vision

A cooperative narrative-focused board game of investigation and horror
with a sliding scope and mechanics that can go from global all the way
down to a single hideout.

These elements are all core to the identity of this game.  There is some
room for the precise meaning of these, as expanded upon in this section,
to be tweaked and tuned, but none of them can be discarded without
turning this into some other game.

### A cooperative ...

1. Strictly cooperative.
2. While it's kind of cute from a certain perspective, I especially
   dislike AH2's "Join the Winning Team" card because it's an opt-in
   betrayal rather than a game-assigned "betrayal" in a role-based
   hidden loyalty game, and I also dislike MoM2's changed goals due to
   insanity.
3. Some players may not want to be forced to play as a "betrayer", so no
   game effect will ever force this.  For the purposes of this design
   requirement a "betrayer" would be a character with victory conditions
   that are different from the group victory conditions.  A subtle
   example of this is MoM2's Insanity cards where an additional
   requirement is added for only that player, e.g. "Instead, you win
   only if [normal victory requirements] and you have 1 or more Spells."
   because this may force the player to prevent or delay victory until
   they have met their private requirements (that they are not permitted
   to talk about) because to them a general failure is "no worse" than
   failing to meet their special requirements.
4. If for narrative or mechanical reasons a character is ever taken out
   of player's control, it MUST be stated explicitly what is being
   forced and the duration of the loss of control, and if it is
   permanent then from the player perspective it is mechanically
   equivalent to permanent character death.
5. This does not preclude giving additional restrictions to a character,
   so long as they are limited to things that would be considered
   acceptable as "quirks" on a cooperative character at the start of the
   game, e.g. "you cannot give money to another character ...", and
   preferably with a cost that can be paid as an alternative to
   following the new restriction, e.g. "... unless you resolve a Faerie
   Unforseen Consequences draw with 1 Warp."

### ... narrative-focusted ...

1. As opposed to "mechanically-focused".
2. I would consider PACG to be a "mechanically-focused" game, in that
   you construct the location encounter decks based on the results of
   the encounter, which then drive the mechanics of the encounter, and
   if there's any narrative to that encounter it is something created
   solely by the players and has no effect on anything in-game.
3. To put it another way, every encounter or deviation from the standard
   game structure MUST start with the narrative, and the mechanics of
   the encounter or change to the game structure exist solely to
   implement the narrative within the framework of the game.

### ... board game ...

1. Resist the urge to veer off into RPG territory.
2. Yes, even for "campaign" or "legacy" play.
3. While it may be good or necessary to have character continuity across
   multiple plays in such a structure, it should be emphasized that it
   is not expected that there be a strong player-character link over
   multiple plays.  The Pandemic Legacy series of games does a good job
   with this, emphasizing at the beginning that character customization
   is a group decision and that there will be times when different
   scenarios call for different mixes of characters.
4. For some reason, Aeon's End Legacy feels like it misses this
   requirement.  This is perhaps something that should be looked into in
   more detail.
5. It would be both thematically appropriate and reinforce this part of
   the vision if the mechanics of gameplay tended to naturally result in
   some "permanent" (only for campaign or legacy play) character
   elimination in each session, either through death, voluntary
   retirement, or other means.
6. Perhaps one way to emphasize this would be to start any "campaign" or
   "legacy" playthrough by creating more characters than the game
   supports at one time, or by splitting up the character creation
   process among multiple players.
   1. E.g. each player starts the process for two characters, then hands
      them to their left, and then everyone performs the next step for
      the two characters they were just handed, and so on until all of
      the characters are complete.  Might want to emphasize that
      table-talk and group planning are encouraged.

### ... of investigation ...

1. With all due respect to the franchise, neither AH2 nor AH3 really
   shine in this regard.  I haven't played enough of AHtCG to have an
   opinion on how well it creates this feeling.
2. On the other hand, this isn't a puzzle game either, meaning that it
   shouldn't rely on player cleverness to be successful in an
   "investigation".
3. The goal here is to create the feel of an investigation unfolding
   rather than turning this into a highly-complex Clue variant or escape
   room game.
4. The idea at the moment is to have multiple details about the
   adversary and their plans available for the characters to uncover
   through encounters.  The only detail necessary for moving on to the
   next zooming-in of scope is the location, but each additional detail
   uncovered SHOULD both progress the narrative, give the players a
   mechanical advantage that's linked to the narrative, and provide
   information for the players when making choices so that they can
   tailor their "loadout" for the expected challenge.

### ... and horror ...

1. By horror, I'm talking about narrative horror rather than mechanical
   horror.
2. To a player being directed to "Lose 1 Sanity" is no more inherently
   horrifying than "Lose 1 Health", and if the character has a high
   starting Sanity and low starting Health, it will probably create more
   tension and trepidation for the player to lose Health than it will be
   to lose Sanity.
3. Mechanical Sanity tends to end up becoming nothing more than "just
   another resource" that you manage in your pursuit of victory.  This
   is especially true when Sanity can be restored, but also tends to be
   true in other games.  The game DMD makes this explicit because
   character progression is only possible through permanent Sanity loss.
4. Therefore, there are no mechanics around tracking "sanity" or
   "horror".
5. Instead, the goal is to create an atmosphere of the unsettling
   through narration; showing rather than telling.  If the player has to
   be told that their character is horrified or unsettled then the
   writer has failed.
6. "Horror" and "Sanity" are used in other media as a way to create
   tension for the consumer as part of the entertainment.  In this game
   the goal is to create that tension for the player through
   irreversible compounding corruption of the body and mind through
   Warp.
7. None of this rules out game mechanics that affect player agency as a
   result of corruption of the mind, just as there are mechanics that
   affect player agency as a result of corruption of the body.  But
   these should still be  narrative-first, show rather than tell, and
   not presented to the player as a "horror" or "sanity" system.
8. Further, none of this is saying that it's a bad thing for the player
   to make choices about when they allow their character to knowingly
   take actions that will be detrimental to the character's long-term
   mental health.  These choices are as meaningful, and should be as
   difficult, as decisions about taking actions that may be detrimental
   to the character's long-term physical health.  It is simply the case
   that as a writer and designer these things cannot be considered to be
   contributing to the texture of "horror" that the game is supposed to
   convey.

### ... with a sliding scope ...

... and mechanics that can go from global all the way down to a single
hideout.

1. This is one of the core premises of the design of this game.
2. Though it may perhaps be best considered to be a theory that is not
   yet proven.
3. The mechanics described in this document are currently believed to be
   able to create this vision, and when they are found to be lacking
   they MUST be either augmented or discarded until they do.
4. One thing that's worth making explicit about this is that it is
   intended that a single play session will cover three scopes: Global,
   Regional, and Local.  This implies that many of the setup and
   teardown steps will have to be performed three times during this one
   play session.  Therefore, it is vital that these steps be easy to
   follow, fairly quick to accomplish, and amenable to cooperation among
   all players to finish more quickly.  It's fine if a group chooses to
   have one person who handles all of it and everyone else gets a break,
   but it's not fine if it MUST be that way.  Even someone new to the
   game should be able to be given discrete tasks that allow them to
   contribute to both setup and teardown.

## Setting

The first thing that needs to be addressed when talking about the
setting is the question of "Why create an original setting rather than
using one that already exists?".

There are at least two similar settings that could be freely used.  The
first is the Cthulhu Mythos (CM) and the other is the Secret Histories
(SH) from the Weather Factory games.  There's also Candela Obscura (CO),
which may not be available but is a closer fit than either of the
others.

The short answer is that none of them are a good-enough fit.  The longer
answer is found in the detail of the characteristics desired in the game
and, by extension, the setting.

1. Has a "native" magic that is safe and plentiful, but relatively weak.
   This mechanically encourages the players to take risks because things
   built on the native magic will be underpowered late in the game.
   1. For those familiar with D&D magic, you can think of this as a
      setting where the "native" magic usually only goes up to second
      level, and instead of gaining higher-level spell slots magic users
      would gain even more second level slots (e.g. instead of a fourth
      level spell slot they gain two second level slots), so a
      high-level wizard can cast spells like "Scorching Ray" all day
      long, but it would take a ritual to cast a single "Fireball".
      Along with this lack of high-level spells, almost everyone gets
      cantrips.
2. Uses a version of "tech" that is based on magic.  I think that the
   dynamics of having a blurry dichotomy between tech and magic will
   complicate and distract from some of the other mechanics I want to
   develop, such as corruption based on "alien" magic.
   1. Iron, and its alloys, will absorb all flavors of magic, so it
      tends to not be used for things.  The precise mechanics of this
      are TBD, but it is limited.  It's entirely probable that no one
      has bothered yet to do any systematic research into this effect.
   2. Iron ore can be transformed into an ore for "Adamant", a metal
      that will generally play the role of steel.
   3. Copper ore can be similarly transformed into an ore for
      "Orichalcum", a metal that is critical in "Thaumostatic"
      machinery, which generally plays the role of electrical machinery.
   4. Other metallic ores can also be transformed, with the details TBD.
3. Has multiple flavors of "alien" magic.
   1. Each "flavor" of "alien" magic originates from one (or more?)
      other lands/worlds/realms/planes that connected to the primary
      world in a way that is more like the world of faerie from folklore
      than like the planes from D&D (except possibly Sigil from the
      Planescape setting), though that doesn't necessarily rule out some
      of them having very different spatial rules.
   2. No effect or (alchemical) element is exclusive to any "flavor" of
      magic, though most "flavors" are better suited for some effects
      than others.
   3. As an example, "native" magic can produce fire, as can most other
      "flavors" of magic, but there are worlds that lean very heavily
      towards fire and it's easier to produce fire using the magic from
      those worlds.
4. While the beings from the "alien" worlds are incredibly diverse, and
   only some of them are sentient, the one thing that they all have in
   common is that they find things from the primary world to be
   especially tasty.  While there may be limitations in what things each
   being can feed upon, generally inorganics are least tasty, then
   plants, animals, and finally people.
   1. Intelligent beings will usually be able to keep their hunger under
      control when following orders or when necessary to accomplish a
      long-term goal.  This includes the more intelligent non-sentient
      beings as well as most sentient beings.
5. When something from the primary world is exposed to "alien" magics
   there is a chance that it will absorb some of that essence and become
   corrupted.  This corruption can grow and eventually dominate that
   being so that they behave more like something from that "alien" realm
   than something from the primary world.  This is called "Warp".
6. It is possible to contain and/or protect against the corrupting
   influence of "alien" magics, though usually only one specific
   "flavor".  This is called "Ward".

## Narrative Arc

### Overview

The narrative arc will be explicitly split up over the base game and
expansions.

### Base Game

The base game will only provide for "one-off" missions initiated and led
by ad-hoc teams of independents.  This is explicit in the rules and
written narrative.

In mechanical narrative the game balance should lean towards a very high
rate of heroic sacrifice KIA and ending the game at "Dead Man Walking"
(DMW) levels of corruption.

While most will probably score themselves on a pass/fail basis, the game
will provide a way of calculating an end game score as a means of
furthering this narrative by mechanics.  In this scoring the
success/failure of the mission is the largest determinant, but
individual outcomes also feature greatly with surviving scoring best,
but KIA and DMW not far behind (and identical).  Bonus points can be
awarded for becoming KIA or DMW as part of a heroic sacrifice to bring
about the success of the mission.  This scoring will be the basis for
team performance evaluations when campaign play is introduced later.

### Expansions

## Mechanics

### Doom Clock

In all stages of the game, no matter what duration it represents, each
space on the Doom Clock is a "Tick", and all game mechanics will give
duration in Ticks, allowing them to work no matter what scale currently
applies. For the sake of player comfort there will probably be a set of
spaces on the Doom Clock with a marker to indicate what the current
scale is - Days, Hours, or 5 Minutes - but this exists only to give the
players a sense of grounding and urgency as the scale gets shorter.

### Player Attributes

#### Attribute Hierarchy

Player characters will have a hierarchy of attributes that skills are
based on.  Each level in the hierarchy contributes dice to the
attributes that fall under it.

1. Soul - the core of a person

Under Soul a person is made up of three parts:

1. Body - the physical part of a person, built on soul
2. Spirit - the ... (intangible?) part of a person
3. Mind - the mental part of a person, built on soul

Each of these three subparts will have an expression in Force and an
expression in Finesse.  This results in six attributes, though there may
be times and places where Soul, Body, Mind, and Spirit are tested
directly separate from the Force/Finesse expressions.  The names of
the Force/Finesse expressions are not final.

1. Body/Force - Strength, Brawn, or Might
2. Body/Finesse - Dexterity, Nimbleness, or Agility
3. Spirit/Force - Will
4. Spirit/Finesse - Charm
5. Mind/Force - Intellegence or Intellect
6. Mind/Finesse - Cleverness

Possibly the expressions won't be given official names and will remain
(Body|Spirit|Mind)/(Force|Finesse).  If we have standard iconogoraphy
we'll need iconography for Body/Spirit/Mind and Force/Finesse even if we
use the specific names.  If we use the specific names then we probably
ought to also have specific icons for each of those things, but if we
don't use specific names then we definitely don't need thsoe six icons.

To give examples of what these represent:

1. If presented with a locked door, using Body/Force would result in
   something getting broken to allow passage through the door while
   using Body/Finesse would be something like picking the lock.
2. If presented with a guard in the way, using Spirit/Will would be
   getting past them by overwhelming personality, authority cues,
   and intimidation in some combination while using Spirit/Charm would
   (probably) be more subtle, invoking some combination of confusion,
   seduction, and misdirection.
3. If presented with a puzzle, using Mind/Intellect would be working out
   the intended correct solution while using Mind/Cleverness would be
   noticing a way to circumvent or bypass the mechanism.

The dice in the Soul area will be used for all checks and the dice in
the three primary subares (Body/Spirit/Mind) will be used for all
Force/Finesse checks, and then each of the Force/Finesse expressions can
have their own dice.

The starting point for balance is two Soul dice, one or two dice in each
of Body, Spirit, and Mind, and zero to two dice in each Force/Finesse
expression, so characters will be rolling three to six dice per check
before adding in equipment or specific skills.

#### Checks

When multiple attributes are available for a check it is player's choice
which to use, though some equipment may only be usable with certain
attributes or may make additional non-standard options available.  There
are some general guidelines.

It is intended to give each area and speciality distinct meaningful
things to do of roughly equal overall value to the mission.

Combat uses Body/either, with its contribution being straightforward and
easy to understand.  Spell casting uses (Spirit|Mind)/Force,
contributing in a wide variety of outcomes, but usually not as the only
solution to those obstacles.  Thaumostatic device control uses
(Spirit|Mind)/Finesse and is intended as the major contribution purpose
for those attributes.

This will take deliberate design decisions to remain meaningful, but it
does fit with the setting and theme - part of why there's this
widespread problem now is that the adoption of the thaumostatic engine
trivializes access to top-tier (for this world) magical power, and is
therefore indispensible to powering the ritiuals necessary to enable
serious incursions and summonings.  It allows things to be accomplished
in wweks that previously took decades of careful (and easily disrupted)
work.  Therefore the manipulation of thaumostatic devices should have a
central role in the final confrontation and at many other points along
the way, including interactions not directly related to the threat.

There are also uses of lesser importance, but still well-defined.
Physical tools use Mind/either.  Magical (non-thaumostatic) tools use
Spirit/either.  Social interactions use Spirit/either.  Puzzles use
Mind/either.  Interactions with non-sentient beings use
(Spirit|Mind)/Finesse.  Searching/observing uses Mind/either.  Unaided
physical actions use Body/either.

Luck uses Soul, and only Soul.

Note that due to the corruption mechanics there will not be any
modifiers applied to the number of dice rolled (e.g. for difficulty),
instead all of the adjustment will have to be done through the number of
successes or other means.  Leaving dice out (subtracting) will either
allow players to prune out their more harmful dice or will require a
special rule (remove native dice first).  Extra temporary dice (adding)
will allow players to circumvent harmful effects (e.g. "corrupt one die
used in this check") unless there's a special rule to prevent it
(bonus dice can't be corrupted).  Keeping all of the difficulty tuning
to modifying the number of needed successes eliminates the need for both
of those special rules and streamlines the gameplay.  Adjusting the
number of needed successes is less granular than adding and removing
individual dice, by roughly 1:3, so there may be need for something else
new in this space.

#### Health Pools

Characters will have "health" in each of the three parts of their Soul.
Though the names for these are still TBD, if one were to use an AH spin
on the names they might be Stamina for Body Health, Sanity for Mind
Health, and Focus for Spirit Health.  But I'm also fundamentally opposed
to "Sanity" for Mind Health because of the connotations to "losing
sanity" which are contrary to the intended design.

Perhaps "Heartiness" for Body, "Resolve" for Spirit, and "Reason" for
Mind.

Mechanically, each of these "healths" will have a maximum capacity that
matches the total number of dice in that area, plus the Soul dice.  So
for Health the total would be Soul + Body + Might + Agility, which will
provisionally range from three to eight.

Having one of these health pools reach zero must be detrimental, but
should also be minimally disruptive - the AH2 rule of moving to the
hospital or asylum, or even worse lost in time and space, has been
solely responsible for games being lost by completely derailing careful
planning.

Drawing inspiration from AH2's Injury/Madness cards, giving the player
choice of consequences seems like a good idea, provided those choices
are meaningful.

Provisionally the general term for one of these health pools being
depleted is "Broken".

Options for resolving a "Broken" status:

1. Some time delay, possibly with options
2. Possibility for emergency assistance from another character within a
   certain timeframe
3. Lose a die from one of the associated areas, with removing a Soul die
   affecting all areas (maximum health as well as rolls going forward).
   The assocciated Health is restored to the new maximum and there is
   little, or no, further penalty.
4. Character is only Lost when the last die is removed from their Soul
   pool.  Possibly when the last Native die is removed from their Soul
   pool, though players will likely want to remove "Alien" dice first
   even without reinforcement like this, but having this be the rule
   would also allow for characters to be Lost due to the corruption of
   their last Native Soul die.
5. Possibility to function in unbroken areas - e.g. someone Broken in
   Body might still be able to fast-talk or cast spells - for some
   period of time (e.g. while waiting for rescue), which might be
   necessary for dealing with an actively hostile source of the injury.
6. Automatic failure of further checks in that area until remediated.
   As a "mercy", no rolls would be made so there wouldn't be any
   additional risk of further corruption on these failed rolls, if for
   some reason (such as combat) the character were forced to make such
   checks.

Possible terms include "Infirm" for Broken Body, "Disheartened" for
Broken Spirit, and "Irrational" for Broken Mind.  Especially if the
character is able to function in other areas the name of the condition
should reflect and imply that (e.g. "Apathy" would be a poor choice for
Broken Spirit since it implies general inaction).

The states of "Infirm", "Disheartened", and "Irrational" could be
general conditions that can be applied temporarily by various effects
and are applied automatically, and permantent until healed, when the
pools are depleted.

#### Game Component

These are likely to be presented on character cards along the lines of:

    ┌─┬──┬────┐
    │ │  │    │
    │ │  ├────┤
    │ │  │    │
    │ ├──┼────┤
    │ │  │    │
    │ │  ├────┤
    │ │  │    │
    │ ├──┼────┤
    │ │  │    │
    │ │  ├────┤
    │ │  │    │
    └─┴──┴────┘

Though it does look a bit distorted here because the line-drawing
characters aren't square.

Rather than placing actual game dice on the character cards, with the
implication that they would have to be removed, rolled, and then
replaced exactly as they were, tokens of some sort will represent the
dice, probably colored cubes.  If using plastic cubes, could use solid
cubes as the tokens for "safe" dice and transparent cubes as tokens for
"unsafe" dice, but that's probably premature window dressing.

With three items (Body, Mind, and Spirit) contributing to a whole it is
very tempting to give each of them a primary color and blend them
together for the Soul, though an argument can be made for both the
addative and subtractive methods of color mixing.

Using the addative method I could have the Body be red, the Mind be blue
(following AH conventions), and the Spirit be green, resulting in a
white Soul, with the blending of Spirit plus Body being yellow, Spirit
plus Mind being cyan, and Body plus Mind being magenta.

Using the subtractive method I could have the Body be yellow, the Mind
be cyan, and the Spirit be magenta, resulting in a black Soul and the
blending of Spirit plus Body being red, the blending of Spirit plus Mind
being blue, and the blending of Body plus Mind being green.

Any such coloration will be primarily aesthetic, though possibly used as
reinforcement by repeated association in various places.  It MUST NOT be
used for gameplay or to communicate information that the player needs
(color blindness).

Force and Finesse will be differentiated within each color through
brightness and saturation.

Having either black or white souls invokes shades of TES series where
there is a fundamental distinction between "people" (man/mer/beastfolk)
souls and other souls (though the handling and treatement of this is, as
with all things TES, uneven in the lore).  In this universe the
distinction would be between "native" souls (of all sizes and stages of
sentience) and "alien" souls (of all sizes and stages of sentience).

## Art Style

## Appendices

