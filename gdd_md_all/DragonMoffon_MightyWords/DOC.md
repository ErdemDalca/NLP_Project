# Rap God Game DESIGN DOCUMENT
##### By DigiDuncan, DragonMoffon, and Stirupp for the Jan 2025 Pirate Software Game Jam


### Introduction
#### Prompt
You are the weapon. 
Concept
The pen is mightier than the sword.
#### Game Summary Pitch
A single player card game where you face off in a rhyme rap battle. Put together a string of rhymes, rack up combos, crush egos, become a rap GOD.
#### Inspiration
##### Reigns
Reigns is what got us into making a card game. In it you have to make yes or no decisions which affect 4 properties differently. Instead of 4 properties we have multiple forms of lyricism such as Rhyme, Alliteration, Assonance etc. 

##### Mad Verse City
Mad Verse City is a Jackbox Party Pack game in which two opponents take turns writing diss bars at each other. The first line is a fill-in-the-blank, the next is a fully custom-written line, and then this repeats. Scores are based on audience participation, but we wouldn’t adopt this part.

##### Balatro
Balatro is a Poker-like rogue-like gambling-like. In it, you make poker hands, and those poker hands (plus some modifiers) score the player points. They must get a certain amount of points per match, within a certain amount of turns. Originally we were just talking about poker hands matching rhyming schemes, but as Balatro is the premier poker-like it has helped give us ideas for how to do the scoring.

##### Other
Sushi-Go, Mad libs, and scrabble are other games that helped us get to our final game idea.

#### Player Experience
The player creates a deck from a randomised list of ‘fill in the blank’ cards and ‘word’ cards. They then face off with opponents and randomly draw from their deck. Fill in ‘fill in the blank’ cards with ‘word’ cards, attempting to string together rhyming ‘word’ cards. The player must take risks in play and deck building to set up combos, and crush the combatants. Verbally.

#### Platform
The game will be developed to be released on the web.
	
#### Development Software
Godot 4.3 (game development)

Photoshop, Illustrator (Art creation)

Audacity (Audio design [SFX])

FL studio for editing songs (Audio design [Music])

#### Genre
Singleplayer, card game

#### Target Audience
With limited design exploration and time, this game needs to be largely simple and toyetic. The simple card mechanics and novel concept should market towards casual game players who want a short puzzle experience. 

### Concept

#### Gameplay overview

There are two phases: deck building and play.

When deck building, the player is presented with a series of randomized cards. They then chose a limited number of ‘fill in the blank’ cards and ‘word’ cards.

Then they begin the play phase. They face a rap opponent who has a specific score to match, and special requirements to beat them, such as a verse of 100% alliteration. (stretch goal) the player also has a set of achievements of increasing stupidity which unlock new words and phrases.


On their turn they create 4 (maybe variable) bars by selecting a phrase card and then word cards for each blank. Each bar is scored by itself and then the whole verse is scored based on various categories. (Ideally) a text-to-speech voice then reads out their verse and the hype crew shout out various things based on how well the player did. 

The Ai will throw together semi-random verses based on their unique challenge deck. They also have a hype crew, but their call-outs are based on how close to completing the challenge the player is. 

If the player runs out of verses then they lose the match, but if they beat the challenge then they get to finish early (and maybe) they get bonus cards to choose from or special achievements.

#### Theme Interpretation (You are the Weapon)
In this game, you control the most powerful weapon of all -- words. The pen is mightier than the sword after all. Your words have power, and you can take your opponents down with the cutting wit of rhyme.

#### Mechanics

##### Decks
The player has two decks. One for filling in the blank cards, and One for words to go in the blanks. Inbetween rounds the player gets a few new options they can swap out.

##### Cards
The cards have two roles and when combined together make sick rap phrases which get scored as part of the verse.

##### Rhyming
When the player creates a verse the player gets scored on how well they rhymed. With different rhyming schemes having different bonuses e.g. AABB, ABAB, AAAB, etc.

##### Alliteration
The verses also get scored on alliteration, this is both  internal so if the fill-in and words both provide alliteration, and if there is alliteration across the lines.

##### Assonance
Similar to alliteration if the vowel sounds inside the words work together then they also get bonus points

##### Syllables
The length of the fill in words also has an impact on flow. So there is a bonus for getting the right blank length


### Art
#### Theme Interpretation
To enhance the ‘pen is mightier than the sword’ interpretation, we chose rap battles as a theme. To match this theme this project draws from post, post, post, japanese inspired, y2k revival hip hop fashion and streetwear. The colors will be bright, the outfit y2k, and the visuals stank. This matches the fun novelty aspect of the game.

#### Design
The design of the game is maximalist, y2k and pop. Inspired by games like Jet Set Radio and Bomb Rush Cyberfunk. A graphic style with bold colors and shapes creates a daring, youthful, sharp, stupid style.

### Audio
THE FIRST OPTION IN GAME SHOULD BE TO CONTROL AUDIO VOLUME

#### Music
The music will be very simple as a backing track to the tts rapping the verses. It will be funk and hip hop inspired fills and breaks. 

#### Sound Effects
There should be heavy folly on the cards and interactions with lots of interjections to add to the brazen rap frenzy. 

### Game Experience
#### UI
The GUI will be as bombastic as the character design and concept. Bright geometric shapes that lead the eye to the buttons. 

In a round the player’s verse will take center stage along with the character and opponent. The cards run along the bottom of the screen with their score details in the center. 

Ideally the audio would bounce to the bpm of the song to make it feel dynamic.
#### Controls
Since the game is mostly GUI based it should be navigable using arrow keys, gamepad, and mouse.







