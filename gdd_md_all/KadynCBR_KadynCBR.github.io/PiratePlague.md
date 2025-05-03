---
layout: page
title: Pirate Plague
description: Unreal strategy and management game
img: assets/img/PiratePlague/piratelanding.png
importance: 3
category: Game Dev
---

<!-- 
    Summary & Purpose
        

    noteable stuff:
        Working with a team of 5 people
        Windows and Linux builds
        full gameplay loop
        Perforce.
 -->

## Summary & Purpose
Pirate Plague is a gamejam game created for the PirateSoftware PirateJam #14. The jam ran for a duration of about 2 weeks and was probably the biggest jam I had attened in earnest thus far. I ended up having to be a free agent and found a team of 5 strangers to create a game with on the PirateSoftware discord. This marks the first time I've meaningfully worked in a group with other people. It's also one of my most complete projects to date as well as being a debut in the Unreal Engine. 

Discussion points:
- Working with a team
- Subversioning
- Full gameplay loop
- Working with Unreal with the intent of shipping
- 
 <div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/wfc/im4.png" title="bitmap WFC" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/PiratePlague/pp1.gif" title="Patching" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/PiratePlague/pp2.gif" title="Shooting" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/PiratePlague/pp3.gif" title="Chaos" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Manage your time and your hands wisely, if anything is left unchecked it can get out of hand incredibly quickly.
</div>

---

## Teamwork makes the dream work
I formed a team with 5 other people from the PirateSoftware discord, it went pretty well everyone was really agreeable throughout the time. This is very different from my usual projects where I'm normally doing everything. I ended up being asked to lead programming efforts due to prior experience with the engine and development in general. There were two other developers which I was leading, but they did well enough that its more like I was around to answer questions if even that. 

We had come together and created a game design document adding suggestions and concerns from each persons individual area of expertise. This design document ended up being quite ambitious, which personally I'm a big fan of, however it became apparent about half way through we would need to triage the most important features to create a working minimum viable product.

---

## Subversioning
<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/PiratePlague/helixcore.png" title="Perforce" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
Working with 5 people from different areas of the game development process as well as different levels of experties it became quite apparent there was going to be a roadblock that I've yet to hit in unreal. Subversioning. Primarily, working with blueprints and git and multiple people do not make for a happy time. 

Until this point I had worked exclusively in git not really minding the binary overwriting because I was the only one working on the system. Within the first 5 hours of working on this game we had 3 merge conflicts and 1 of them resulted in the loss of someones work. This wasn't really going to be sustainable for the next 24 hours nevermind the next 2 weeks. One of the members of the team worked in industry and recommended using perforce. This required quickly learning the minimum knowledge required to bootstrap a server on digital ocean as well as use the intergration with Unreal. It ended up working incredibly nicely and I can see why this might be used in broader industry. 

While git can also handle locking of files, it think perforce seems to handle it much more nicely and in a way that requires any untangling unless something has gone very wrong. 

It's also worth noting, to the weary traveler, do not add everything to the perforce repository. I believe either the "saved" or "deriveddatacache" folders were added, and that ended up causing everyones unreal engines to hang every 10 seconds while it attempted to modify files that were write locked. That issue took a bit to figure out. 

---

## Ship to ship
Considering that this game was made for a gamejam I'm normally not so underpressure to finish these but this time with a team everyone had a hand in bringing this to completion on time. This is the first unreal engine game I've created which I've built and released to the public. it features both PC as well as Linux builds, and was tested and iterated on to work on a steam deck.


Where there isn't a whole lot of technical achievements in this game, it does mark the first time working as a team, and my first official publish of a game on PC. We shipped a title!
There's a lot of little things I learned but nothing big enough to warrant its own section other than the above.

You can play the game currently here:
[Pirate Plague on Itch.io](https://kronoshark.itch.io/pirate-plague)
 <div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <a href=https://kronoshark.itch.io/pirate-plague>
        {% include figure.html path="assets/img/PiratePlague/piratelanding.png" title="Pirate Plague" class="img-fluid rounded z-depth-1" %}
        </a>
    </div>
</div>
