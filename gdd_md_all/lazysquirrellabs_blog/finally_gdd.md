---
layout: post
title:  "Finally, a proper Game Design Document (whatever that means)"
date:   2022/09/10 20:38:12 +0200
author: Matheus Amazonas
categories: jekyll update
description: "Game Design Documents (GDDs) are deemed essential by many developers, but are often neglected. In this article, we discuss why GDDs are so beneficial."
---
A Game Design Document (GDD) is a famous and popular tool used by game developers to… well, to document the design of a game. Even though some say it's an essential part of the development process, most of the projects I've worked on didn't use GDDs during the entire development of the game (or at all). On my last project at [Fantazm](https://www.fantazm.com), I had the opportunity to make some decisions from the start. I took this opportunity to experiment with some concepts and ideas, and trying to properly use GDDs (whatever that means) was one of them. Here's my testimonial on the experience of using a GDD for that project.

## The project

The project was commissioned by one of our clients. It was a turn-based, multiplayer, team strategy web game where each team controls their own company through a 10-year time period. Teams (between 3 and 15) compete against each other in different categories, tackling real world scenarios in order to establish a successful company. At the end of the 10 rounds, a winner is chosen based on some Key Points of Interest.

The development team consisted of one game developer (yours truly), a game artist and a project manager/game designer. The client also participated in the development process by providing domain knowledge and by testing all prototypes.

As the solo developer in this project, I was responsible for making some decisions. Investing in a GDD was one of them.

## Previous experience

Although Game Design Documents are essential tools in the industry, all projects I've worked on fell into one of the following categories (some were are a mix of these) when analyzing their GDD usage:

- They didn't have a GDD and the specifications were either fragmented across multiple systems and catalogues (e.g. task management tools, Wikis, emails), or they were in someone's brain (a.k.a. "I am the GDD"). This made it virtually impossible to easily find information about a given feature of the game, and sometimes different sources would give conflicting information.
- They did have a detailed GDD that was created in an early stage of development — usually during initial design — but that was never updated, sometimes to the point that the shipped project was completely different from the one specified in the GDD. This practice rendered the GDD useless after a few weeks of development and referring to it during development to back an implementation decision up became pointless.

With that in mind, I decided to try something new to me (but not really innovative): properly writing, using and maintaining a GDD during the entire development process. Here's how it went down.

## The plan

For this project, we've decided to:

- Write a GDD early in the process, during the initial design phase, to guide us through the development phase.
- Embrace the fact that the GDD was a living document and that its content was not set in stone. Something could have made sense in the design stage, but we later found out it wasn't a good idea.
- At the same time, be careful with GDD changes. A small change can have unpredicted consequences, sometimes even sprawling across teams. Communicating changes is crucial.
- Write everything that was deemed relevant, as small as it was. If something wasn't clear during development, we referred to the GDD for answers. If there wasn't a clear answer there, we would discuss a solution and then add it to the GDD.

With that in mind, we started writing the GDD before writing our very first line of code.

## Initial writing

The game in question was based on a previous project we've developed, so we already had a good idea of what it could be. We discussed it internally a couple of times before starting to write the GDD, and for that reason, we concluded that writing it would be a trivial task: just sit and type down everything we've discussed and we could call it a day.

Boy, we were wrong. As soon as we started writing down what we've discussed, the design gaps and contradictions became apparent — and that's when the real work started. Fixing each contradiction and filling each gap wasn't easy, and once we've done it, it would often surface another design gap. And then another. And another. Right on the first day of writing, we learnt how little we actually knew about the game. We knew its core, but we definitely haven't discovered its full potential. Writing the GDD was planned to be completed in two days (three days if it was really necessary) but in the end it took almost seven days — with other tasks in between.

There was a lot of internal communication (and sometimes external, with the client) during this period, and it was clear that we were slowly closing the design gaps and reaching a clearer, more well-defined game design. We knew that a lot of questions would still surface during development, but at least now we had a clear specification of what we envisioned. At a given point, we've decided we had enough to get started with, and we moved to the development stage.

## Outcome

In the end, the GDD usage following the rules presented above exceeded my expectations.  Even though writing and maintaining the document definitely took some time and effort (more than we anticipated), its benefits definitely paid off in later stages of development. 

Here's why I think that investing in a good GDD helped the game development process:

- Development decisions were easier — and sometimes non-existent. I didn't have to constantly ask myself about some small feature details. When I had to, the GDD was there to aid me.
- Constant redundant communication was eliminated. If the answer for a question I had during development wasn't in the GDD, I'd quickly discuss it with a team member and add the new information to the document. More often than never, I'd ask myself the same question again a few days later, but this time the GDD was there to help me. There were no more "what did we decide last week again? I forgot" messages.
- Expectations were often met. Sometimes during a conversation, some details about a feature are explained, but they are not documented. For the person who's listening, those easily slip their minds. For the person talking, those might be really important aspects that can't be ignored. If those details are written down on the GDD, they won't be missed anymore.
- Development meant solving mostly technical problems, not design problems. Personally, it's really frustrating when I'm in the zone, coding for some time, totally focused on solving a technical problem, and then suddenly I encounter a game design question that takes me out of the technical mindset and throws me in the design mindset. I have to stop, solve the design problem and then spend some precious time to go back in the technical mind zone. Having a GDD sitting right next to me with answers to most of the design questions I have was priceless. I could reduce the friction involved into those little breaks, going back sooner and easier into the technical mindset.
- In a sense, the GDD became not only the specification of what the game should be, but it was also the history of all the changes we made during the development process. Using a tool that allowed for history lookup (in our case, Google Docs) really exposed this potential.
- Project maintainability has definitely increased. Along with good code and project documentation, the GDD serves as a body of knowledge that facilitates newcomers onboarding. In addition, it's a great refreshing tool for developers that need to switch to another project and then jump back in (myself included).

In addition to helping during the development process of the relevant game, writing a GDD contributes to a team's body of knowledge. The document can be used for future reference during the development of other projects. Features can be easily borrowed, mechanics become easier to replicate and design decisions can be inspired by previous experience.

Personally, the benefits of writing and updating a good GDD are obvious and the necessary work involved certainly pays off. I will definitely invest in a good GDD on the next project I start.

## Lessons learnt

Despite the fact that the experience was great, we learned a few lessons:

- Laying down every aspect of a game early in development is quite a challenge. Of course every little detail can't be specified so early, but we missed some crucial elements that were essential to the experience. These points were mostly features that were not that exciting and "sexy" to design, but were equally important. Some examples: login method, matchmaking strategy, lobby screen. The good news is that the more GDDs you write, the better you become at it.
- Completeness and succinctness are hard to balance. Ideally, the GDD should describe every little corner of the game, but doing so became impractical for two reasons. First, we did not have a full-time Game Designer in the team that could dedicate most of their time into it. Second — but most importantly — writing down every single detail turns the GDD into this massive document that's hard to navigate and consult. Having an easy to access GDD is crucial, otherwise people won't refer to and maintain it, which would be detrimental to the whole goal of keeping a GDD. In the end, we learnt to keep some tiny details of out the GDD, without compromising the goals we established for it.
- Versioning a GDD should be as important as versioning game code. It became clear that tracking and discussing feature changes was crucial to the development process. The tool we chose to host the GDD (Google Docs) does provide a change history feature, but tracking changes made to a specific feature usually required a tedious and repetitive process of going back in history change by change, until you found what you were looking for. In addition, it would had been nice to be able to document the reasoning behind a change — but outside the GDD content itself. Next time, I will look for alternatives that offer better history browsing and that offer a way to externally document changes. Let me know in the comments section if you have a suggestion (is git an overkill?).

## Conclusion

Although Game Design Documents are an industry standard, my previous game development experience lacked proper use of them. I took an opportunity I had as the solo developer of a project to experiment with GDDs during the entire game development process. Although writing and maintaining the document required a lot of time and energy, the efforts put into it definitely paid off and I'm confident that using GDDs in my future projects will also be beneficial.