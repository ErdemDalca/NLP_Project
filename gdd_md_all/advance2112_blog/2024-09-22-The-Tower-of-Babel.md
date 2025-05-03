---
layout: single
title:  "The Tower of Babel"
date:   2024-09-22 01:20:00 -0500
last_modified_at: 2024-12-01 20:01:00 -0500
header:
    image: "/assets/images/TheTowerOfBabel/DoorThin.png"
categories: games
---

A little card game about trying to have a conversation with someone after losing your ability to speak the common language of man.

---

[**The Tower of Babel**](https://advance2112.itch.io/the-tower-of-babel) was made in 9 days for the [Godot Wild Jam #73](https://itch.io/jam/godot-wild-jam-73). It was made with [ArcadeCrow](https://arcadecrow.itch.io/) and [purplewazard](https://purplewazard.itch.io/), two folks I met in the GWJ Discord server. The Jam's theme was "Tower".

### The Jam
After my [experience with the Pirate Software jam](https://advance2112.github.io/blog/games/2024/07/31/Moon-Viewing.html), I figured it was time to move to a smaller jam. Maybe not something tiny, but not something huge either. Also, I figured I ought to work with folks who, like me, are inexperienced but, let's say, more passionate about making games and more available to make games than my previous team was. Looking around for jams, I looked for a Godot specific jam, since I quite enjoyed using Godot. The Godot Wild Jam (GWJ) popped up, and seemed like a good fit. I was going through some things personally in August, things that took time and mental energy, so I waited until September to participate in GWJ #73. As for the team, we met in the team-up channel of the GWJ discord. These lads seemed passionate and determined to make a game. This was both of their first times doing a jam.

### The Theme
This theme, "Tower", was immediately agreeable to me. So many different ways this word can be interpreted. A tower can be a building, like the Eiffel Tower, the Twin Towers, the Tower of Pisa. Or other kinds of structures, like a radio tower or crane tower. Birds tower over man in the sky, a tall person towers over a short one. Lightning rod towers, cooling towers, launch towers, control towers. The Tower tarot card. Mythical towers, like the Tower of Babel.

Crow and I both had strong ideas and, I'll be damned, we went with mine. It came down to a literal (virtual) coin flip. In retrospect, I wish we went with Crow's idea of a top-down beat-em-up with tarot cards as powers. That seems so much cooler than my idea.

### The Plan

Of course my idea was heavily inspired by Balatro, which I had picked up again at the time. In fact, I probably played more Balatro during the course of this jam than I did working on the jam. That explains some things. Anyway, the idea was to make a language-based rogue-like deck builder based on the myth of The Tower of Babel. You would gather cards that described concepts in certain languages and would score points based on how closely related those concepts and languages are. Successfully converse with enough people and you win.

We divided the work in an unusual way. The idea with this team would be that we would each focus on doing whatever elements of making games that we wanted to improve at. So wazard took on programming, Crow took on art, and I focused on sounds and music. Of course we would assist each other when needed, but these were our assigned domains.

Once it was determined that we were going with my idea, I also became the defacto lead designer, as well as the defacto team leader. Oh joy, that went so well last time! Especially with the lack of making a proper game design document once again, this project was doomed to not go well. Lesson learned.

### The Work

I spent the first few days gathering languages and concepts, as well as getting the list of `16 x 40 = 640` words in order. That was such a pain. Crow got started on the art, wazard on getting card manipulation working in game. But in between getting things together I also spent some time coaching wazard. Of course, I had done similar things before with [Moon Viewing](https://advance2112.github.io/blog/games/2024/07/31/Moon-Viewing.html) and [Gwent Clone](), so it was natural for me at this point. And in between that, I worked on the music. 

I knew from the start I wanted to do something with a "vox" style to it, where most or all of the instruments were human voices. Fits with the theme, y'know, because you're like... speaking to people? Anyway, I made some vox sound effects with my mouth and lips by going "ooo" and whistling. I didn't love any of the free offerings at my disposal and it's easy enough to make those sounds on my own.

The first song I came up with I didn't love. I tried just doing a relatively simple chord progression then noodling on top of that. I tried using the trick of vocalizing the main melody, but I wasn't loving what was coming out. I took a day off from this and worked on the card data, finished that out. When I stepped back to the music, I scrapped what I had made and did it again with the same structure in mind. However this time I noodled on the keyboard.

I liked this better. Still didn't love it, but it was fine. 4 minutes of a highly repetitive bass and mid voice and a noodling whistle on top, with some swelling space-y sounds in the second half. I think [what came out](https://soundcloud.com/advance2112/tower-of-babel) was dramatic and retro in a charming way, but frankly would get old if you listened to it more that a few times.

By this time, we had some art, and some amount of getting cards working and we were something like 6 days into the jam. And I was losing steam fast. As mentioned, I was playing the shit out of Balatro during this jam, working on getting Completionist+, but the only reason why I was allowing myself to get distracted with it was because I no longer believed in this idea. After gathering all the card data, I knew this game was way too complex to do in any kind of satisfying way within the timeline and with the team I had. The idea was just too ambitious once again. And this lack of motivation trickled down to the team, and we all slowed down a lot.

Then we learned that wazard had a surprise trip that would take him away for the last two days of the jam, and Crow seemed nearly MIA. Once again, I would have to finish this game out. Well, at least it wasn't as bad as last time, since the plan to finish things seemed a lot more straight forward.

### The End

I spent a bit of time during the last two days of the jam finalizing some things. Putting the assets Crow had sent in, adding some tutorial text and a main menu, plus creating a fail state. Real basic stuff to just make the game into a game, rather than a tech demo.

<figure>
<img src="{{ '/assets/images/TheTowerOfBabel/Gameplay1.png' | relative_url }}" alt="A screen capture of gameplay from The Tower of Babel. There are 21 cards in a grid on the left and a board with 5 empty slots on the right. Each car has a word written on it. Some cards have clearly broken characters that display improperly. In the center is text explaining how to play the game. The gameplay is superimposed on an abstract image of a door.">
<figcaption>Final gameplay from the web build of The Tower of Babel, broken characters and all.</figcaption>
</figure>

Then, a couple hours before the end, I upload the game to itch.io and submit. And lo and behold... the text doesn't work for Chinese, Sanskrit, and Korean. And the audio is busted in several different ways. At this point I threw my hands up and say screw it, I don't have the time or energy to fix this. I uploaded the Windows build, which works fine, as a hail mary, in the hopes that at least one person would play that and see what we were going for.

In the end, we did get a lot of good feedback from other folks. Many praised our originality and concept, and some liked the music. The visual elements were panned, and overall... we got 80th place out of around 150 games. Middle of the pack.

### The Lessons
1. Do web builds early and often.
   
   I didn't know this at the time but Godot has a built-in and extremely convenient way to do test web builds. Knowing this would have saved the pain of that final build and seeing that the sound and text didn't work. This is a simple enough lesson, and one that I have wholeheartedly embraced for making web-targeted games in Godot.

1. My ideas aren't always the best ideas.

   Yeah, no shit. Every time I think about this project, I regret that moment where we chose whose idea we would make. I wish beyond anything it would have been Crow's idea. That would have taken some weight off my shoulders while simultaneously empowering him. And I think, frankly, whatever we made would have been so much cooler than The Tower of Babel. And it's not that I think all my ideas are bad, just that I want to try working off of someone else's idea for a change. Next time I work with other people, I don't want my idea to be the main one.


2. Being distracted means you are unmotivated.
   
   This is pretty straight forward. Game development is supposed to be the distraction from other things. If something else distracts me from game development, then obviously I'm not feeling like doing the game development, am I? Thankfully in this case I finally knuckled down and "finished" the game but sometimes I need to recognize when it's best to just step away from something. Should I have stepped away from this? I'm not sure.

3. I should make something that isn't a card game.
   
   With 3 major projects under my belt ([Moon Viewing](https://advance2112.github.io/blog/games/2024/07/31/Moon-Viewing.html), [Gwent Clone](), and now The Tower of Babel) and ALL THREE are card games. Yeah, I need a change of pace. I love card games, and I have ideas for more, but I can't just make card games. I need to broaden my horizons.

4. I should try working alone.

   Also in all three major projects I've done, I almost wind up working alone  anyway, no matter what I try. Either other people don't do what they say because of things going on in their lives or I get demotivated and wind up demotivating others along with me. It feels like I drag other people down exactly when I'm trying to lift them up by making something with them. Next jam, maybe the next two, I'm working alone.

### What's Next?

While the game didn't turn out very well, I still made due with it. I still want to make games, but as mentioned I wanted to try my hand at doing it alone. The next GWJ started soon, and I liked how the Jam was run, so it was a natural choice to do the next one as well. And for that I did work alone, and made [SUFFER.er](https://advance2112.github.io/blog/games/2024/10/20/SUFFER-er.html).