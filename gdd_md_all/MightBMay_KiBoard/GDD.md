Game Design Document
==========================================

## Concept<a id="concept"></a>
<div style= "margin-left: 40px;">
Kiboard is a rhythm game designed to be played with an actual piano through a MIDI cable connected to your computer. 
</div>

## Game Structure, Loop & Objective<a id="game-structure-loop--objective"></a>

<div style= "margin-left: 40px;">
Players will first select a song to play, then notes of that song will begin to fall on a Piano Roll- a visual representation of a piano- in front of them.<br><br>

There will be a variety of songs you can listen to and learn to play through the piano roll-like display. Players will be able to slow down the speed of these songs to learn them slowly over time.<br><br>

The objective is for players to press the correctly indicated note at the correct timing of the note to earn points.<br><br>

The goal of the game is to make learning songs on the piano a more entertaining experience for the player, as well as providing tools to help them in learning songs.<br><br>
</div>

## Players<a id="players"></a>
<div style= "margin-left: 40px;">
Players will be able to play the game on Windows PC’s using an 88 key Midi Piano, OR using 8/12 Keys on their computer Keyboard.
</div>

## Graphics & Display<a id="graphics--display"></a>
   <div style= "margin-left: 40px;">
   KiBoard is split into two main scenes:
   

      ### <b><ins>Song Selection</ins></b><a id="song-selection"></a>
	    <div style= "margin-left: 40px;">
         The song selection screen will be the main UI menu for the game, consisting of 4 panels, and some buttons.
         </div>
         <div style= "margin-left: 40px;">
            #### Song Selector<a id="song-selector"></a>
            </div><div style= "margin-left: 80px;">
            The center will be the song selector, Allowing for the player to select from a list of songs. Clicking on one of these songs will open the other 3 panels. 
            </div>
         <div style= "margin-left: 40px;">
            #### High Score<a id="high-score"></a>
            </div><div style= "margin-left: 80px;">
               The high score panel will appear to the top left, displaying your previously achieved best score.<br><br>
               It will show the date and time it was done, the achieved total score, the amount of “Perfect, good, Okay, Missed,” and “Extra” notes played, as well as show the ratio of notes correctly played to the total number of notes.
               </div>
         <div style= "margin-left: 40px;">
            #### Song Version<a id="song-version"></a>
            </div><div style= "margin-left: 80px;">
               Song Version relates to how the File system for the game is structured. An example would be if you wanted to add different difficulties to the same song, and is elaborated on in  **FINISH LATER: INSERT LINK TO CUSTOM SONGS SECTION EXPLAINING VERSIONS**<br><br>

               This panel will be a list of all the versions of a song listed in that songs folder, allowing you to select from them before hitting play.
               </div>
         <div style= "margin-left: 40px;">
            #### Song Settings & Preview<a id="song-settings--preview"></a>
            </div><div style= "margin-left: 80px;">
               The song setting window will allow you to set song-specific settings before you hit play.

               Some examples of these settings are:

               - Whether the player is using a Midi Piano or a computer keyboard.
               - Whether or not the player wants to use a sustain Pedal.
               - The BPM they want to play the song at (left blank will default to the Midi Files bpm).
               - Beats Before Drop (how long in advance notes should spawn before they cross the Hit Indicator Bar. Changing this can drastically increase/decrease the amount of time you have to react to a note, as well as modifying the scale of notes).

               The song preview window shows the player a scaled-down exact copy of what the selected song looks like to play before clicking play.
               </div>
         
	  ### <b><ins>In Game</ins></b><a id="in-game"></a>
	     <div style= "margin-left: 40px;">
	        The In Game Scenes ( split into GameScene88 and GameScene12) are where players go after selecting a song, and is where the game loop is played.
		     </div>
	     <div style= "margin-left: 40px;">
		     #### Piano Roll<a id="piano-roll"></a>
				<div style= "margin-left: 40px;">
			    ##### Piano <a id="piano"></a>
			    <div style= "margin-left: 40px;">
		        The Piano is laid out like an 88 key piano in the bottom of the screen. It displays what notes the player is currently pressing.
		        </div>
		
		        ##### Key Lane<a id="key-lane"></a>
		        <div style= "margin-left: 40px;">
		        Light and dark gray strips extend vertically from each key in the Piano. These are the Key Lanes that notes can fall on. They are coloured differently to help differentiate between two nearby notes.  
		        </div>
		
		        ##### Hit Indicator Bar<a id="hit-indicator-bar"></a>
		        <div style= "margin-left: 40px;">
		        A coloured bar slightly above the Piano acts as a visual indicator for when you should play a note. When the bottom of the note touches the hit indicator bar, it is the ideal time.
		        </div>
		
		        ##### Note<a id="note"></a>
		        <div style= "margin-left: 40px;">
		        Notes display what notes the player must react and play in sync to the song with.
		        </div>
		
		        ##### Beat Indicators<a id="beat-indicators"></a>
		        <div style= "margin-left: 40px;">
		        Horizontally across the key lanes are beat indicators. These are a visual representation of how far away a note is from the correct timing to hit it. One beat indicator represents the note being 
		
		        one beat away.
    </div>
</div>
#### Combo bar<a id="combo-bar"></a>
	<div style= "margin-left: 40px;">
		On the left of the Piano Roll is the Combo bar. The bar extends vertically, parallel to the piano roll.<br><br>
		
		The score gained by each correct note hit is multiplied by the combo multiplier, ranging from 1-3x the base value, and increasing based on the amount of correct notes the player plays.<br><br>
		
		This multiplier's value is shown slightly to the left of the combo bar.
	</div>

#### Score<a id="score"></a>
	<div style= "margin-left: 40px;">
		##### Total Score<a id="total-score"></a>
		<div style= "margin-left: 40px;">
		To the right of the piano roll, your total score is shown.
		</div>
	
		##### Score Text<a id="score-text"></a>
		<div style= "margin-left: 40px;">
		Each time you play a note, the value of it is displayed in a stacking history of score changes. These are also coloured according to the timing of the note, pink being perfect, green good, blue okay, and red incorrect.
		</div>
	
		#### Progress Bar<a id="progress-bar"></a>
		<div style= "margin-left: 40px;">
		Along the top of the screen is a green bar. Going from left to right, this bar displays how far the player is into the song's duration.
		</div>
	
	</div>
</div>
	

