# Game design document voor Catastrophic Catastrophy

## Concept en mechanics
Het concept van ons spel is een competitie tussen verschillende huisdieren. De speler kiest, of krijgt, een huisdier toegewezen waarmee de speler het spel speelt. Dit huisdier zal in een top-down bullet hell game vechten tegen horden van enemies die proberen de speler aan te vallen. Na een aantal waves van deze enemies spawnt er een boss. Dit is een ander huisdier waartegen het huisdier van de speler moet vechten, om te bewijzen dat het huisdier van de speler superieur is. Als de speler een boss verslaat, dan krijgt hij/zij de kans om het wapen van deze boss op te pakken en te gebruiken in het vervolg van het spel. Ook verdient de speler na het verslaan van enemies/bosses in-game currency, die gebruikt kunnen worden voor stat/weapon upgrades.

## Formal elements
- Players: Single player vs enemies
- Objectives: Het verslaan van waves van enemies en bosses om verder te komen in het spel
- Procedures: Lopen, schieten, dashen
- Rules: Als de speler al zijn/haar levens verliest, dan stopt het spel (speler is dood)
- Resources: HP, schiet-cooldown, invulnerability-cooldown
- Conflict: Enemies proberen de speler te raken, met hun body of met hun kogels. De speler moet deze zien te ontwijken
- Outcome: De speler verslaat alle enemies en voltooid een wave/verslaat een boss. Hierna wordt de speler beloond met in-game currency of het wapen van een boss
- Boundaries: De speler kan niet van het scherm af lopen, en kan ook geen enemies raken buiten het scherm.

## Inspiratie analyse
### Vampire Survivors
Voor de mechanics van ons spel hebben wij ons laten inspireren door vampire survivors. Vampire survivors is een bullet hell game waarbij er waves aan enemies het beeld in lopen en de speler achtervolgen. Tevens spawnt er af en toe een boss in die (betere) loot dropt. In onze game wordt de speler achtervolgt door waves van 'normale' enemies. Eens in de zoveel tijd spawnt er een boss met een wapen die schiet op de speler. 

Als de speler de boss verslaat kan de speler het wapen van de boss oppakken en gebruiken om de enemies te verslaan.  
In vampire survivors krijg je na een bepaalde hoeveelheid xp te hebben verdiend de mogelijkheid om een wapen te upgraden. Wij willen dit concept in een iets andere vorm toepassen. Namelijk in de vorm van een shop.

### Stardew Valley
Voor het uiterlijk van de game hebben we inspiratie opgedaan van de populaire game Stardew Valley. In onze game willen wij gebruik maken van 'vrolijke' felle kleuren en pixel art. Deze aspecten zijn ook terug te zien in het design van Stardew Valley. 

In Stardew Valley is het ook mogelijk om allerlei verschillende soorten (huis)dieren te houden. Huisdieren is een belangrijk thema binnen onze game.

### Enter The Gungeon
Wij hebben inspriratie gehaald uit Enter The Gungeon. Dit spel is een bullet hell waar je in een dungeon verschilde enemies en bosses tegenkom. Verder is er ook een top-down point of view, deze sprak ons erg aan en willen wij deze ook implementeren in onze game


### Animal Restaurant

In Animal Restaurant run je een restaurant waar verschillende dieren komen. Deze dieren hebben allemaal hun eigen karakters. Zoals: een struisvogel die een papieren zak draagt omdat hij verlegen is, een stinkdier die niet te veel bonen mag eten omdat hij anders scheten laat en een flamingo die een influencer is. 

Al deze dieren hebben hun eigen originele persoonlijkheid, wij willen ook onze eigen karakters hun eigen persoonlijkheid geven.

## Game design theory
### Flow state
Flow state
Een speler bereikt flow state als er een balans is tussen de moeilijkheidsgraad van het spel en de stress die een speler ervaart.

![Flow state diagram](/docs/Groepje/Images/flowState.png)

Een game kan op 2 verschillende manieren flow state verstoren:

1. De moeilijkheid van de game is relatief te hoog ten opzichte van de vaardigheden van de speler. Dit zorgt voor stress/spanning, waardoor de speler een spel niet voor langere tijd kan spelen.

2. De moeilijkheid van de game is relatief te laag ten opzichte van de vaardigheden van de speler. Dit zorgt voor verveeldheid, waardoor de speler geen interesse heeft om een spel te spelen.

Flow state wordt in onze game veroorzaakt door de kracht van de enemies zo te laten scalen, dat deze op elk moment haalbaar zouden kunnen zijn, mits de speler de juiste upgrades kiest en de juiste wapens per wave/boss. Dit vereist kennis van de speler met betrekking tot de updates. Hierom geven we de speler een baseline skill niveau om vanaf verder te werken, door een tutorial/guides toe te voegen op bepaalde momenten waar nieuwe features worden geintroduceerd.

### Internal Economy
Een internal economy van een game is een economisch systeem wat zich enkel en alleen in de game bevindt (met uitzonderingen op micro-transactions). Een economie binnen een spel gaat over de flow van resources tussen entities/de game. Binnen het spel zijn er meestal 4 componenten die bepalend zijn voor de economische flow: bronnen, vernietigingen, omvormers en ruilmogelijkheden. Bronnen zorgen voor een toegankelijkheid aan een resource, vernietigingen zorgen ervoor dat de resource niet in overvloed aanwezig is door het te verwijderen van het spel (zorgt tot op zekere hoogte tot schaarste). Omvormers zorgen dat een bepaalde resource omgevormd kan worden tot een andere resource. Deze actie is meestal irreversibel. Ruilmogelijkheden zorgen dat de speler resources kan in ruilen voor (meestal) niet-ruilbare items/resources.

![In game currencies](/docs/Groepje/Images/inGameCurrency.png)

Wij gaan een internal economy in onze game voegen aan de hand van een in-game currency. Deze wordt verkregen door waves/bosses te verslaan. De speler kan ook (een deel van) deze currency verliezen door dood te gaan. Wij hebben nog geen plan om een omvormer specifiek toe te voegen, maar wel een ruilmogelijkheid die een belangrijke rol vervult; de shop. Deze zorgt er namelijk voor dat de in-game currency nuttig is voor de speler. Hier kan de speler zijn/haar karakter sterker maken door de currency in te ruilen voor stat/weapon upgrades.

### Feedback Loops
Feedback loops zijn de manier hoe de speler feedback krijgt van het spel, op basis van hoe goed/slecht de speler speelt. De positieve feedback loop geeft positieve feedback als de speler goeie acties uitvoert. Het geeft de speler een overwinningsgevoel als hij/zij iets goeds doet. Denk hierbij bijvoorbeeld aan Monopoly. Als een speler veel straten in zijn bezit heeft, dan krijgt hij/zij meer geld van de anderen, waarmee deze speler weer meer straten kan kopen, enz. Een positieve feedback loop zorgt er meestal voor dat de spelers die niet zo goed gaan, nog verder achter komen te liggen. Een negatieve feedback loop geeft de speler die het beste bezig is, een (kleine) hindernis zodat het geen 'smooth sailing' is als een speler aan kop loopt. Dit geeft andere spelers nog mogelijkheden om een comeback te maken, als het om een multiplayer game gaat. Denk hierbij bijvoorbeeld aan Mario Kart. De spelers voorop krijgen slechtere items dan de spelers achterop. Dit geeft de spelers achterin meer kans om anderen in te halen. Als het om een single player game gaat, worden negatieve feedback loops veroorzaakt door bijvoorbeeld diminishing returns. Dit houdt in dat een herhaalde actie, steeds minder oplevert voor de speler.

In onze game gaan wij verschillende feedback loops verwerken. Allereerst een positieve feedback loop. Hoe sterker de speler wordt, hoe meer enemies hij/zij kan vermoorden, hoe meer in-game currency de speler krijgt, waardoor de speler weer sterker kan worden aan de hand van upgrades. Onze negatieve feedback loop zijn de diminishing returns op de prijs van de upgrades. Deze schaalt exponentieel, waardoor het steeds langer duurt om upgrades te kopen.

### Design Goal
Design goal is het doel wat bereikt moet worden als het ontwerpdoel, de mechanics en de motivatie op elkaar af zijn gestemt en elkaar complementeren. Hierin is het ontwerpdoel hetgeen wat je wilt bereiken met het spel, de mechanics zijn de verhoudingen tussen speler en spel om het ontwerpdoel te bereiken en de motivatie is de reden waarom een speler het spel zou willen spelen.

Wij willen een competitie tussen verschillende huisdieren met onze game bereiken, aan de hand van een top-down bullet hell game. De mechanics die wij hiervoor gebruiken, zijn boss fights tussen de speler en andere huisdieren, waves bij deze bossfights en upgrades die je kan kopen om je eigen huisdier sterker te maken. De motivatie in onze game is het feit dat de bosses hun wapens droppen wanneer ze zijn geelimineerd. Het meesteren van deze nieuwe wapens is iets waar de speler aan moet wennen. Ook hebben wij een shop waar je stat buffs kan kopen (en misschien nog andere zaken later). Dit geeft de speler het gevoel dat ze altijd sterker kunnen worden, waardoor ze blijven spelen.

### Core mechanics & secondary mechanics
Core mechanics zijn de acties die een speler moet uitvoeren om verder te komen in het spel. Deze worden veel gebruikt door de speler. Secondary mechanics zijn mechanics die inwerken op de core mechanics. Secondary mechanics zijn (meestal) optioneel om verder te komen in het spel of het spel uit te spelen.

In onze game zijn de core mechanics rondlopen en het schieten van een geweer. De secondary mechanics die hieruit voortvloeien zijn een player dash, een in-game currency en verschillende wapentypes.

![Movement mechanic diagram](/docs/Groepje/Images/mechanicDiagramMovement.png)
![Shooting mechanic diagram](/docs/Groepje/Images/mechanicDiagramShooting.png)

### Level structure
Level structure houdt zich bezig met de wijze waarop de speler aan mechanics wordt blootgesteld. Een goede level structure introduceert stapsgewijs de mechanics, en het hoofddoel hierbij is het ontwikkelen van de vaardigheden van de speler. Met een level wordt een afgebakend deel van een spel bedoeld. Denk hierbij aan een level in mario, maar ook een wave van een zombie survival game bijvoorbeeld. De basismechanics die nodig zijn om het spel te spelen (core mechanics) worden meestal aan het begin geintroduceerd en zijn niet heel lastig om te begrijpen op laag niveau. Optionele mechanics die leuk zijn voor het spel (secondary mechanics) worden vaak later in het spel vrijgegeven. Hieronder is een voorbeeld te zien van simpele level structure in een 3-match game. Bij elk level worden nieuwe mechanics uitgelegd of worden deze geadvanceerder toegepast.

![Level structure](/docs/Groepje/Images/levelStructure.png)

In onze game krijgt de speler op het beginscherm te zien welke knoppen gebruikt worden voor welke basisacties. Hierin leggen wij uit hoe de speler loopt, schiet en een eventuele dash doet. Er wordt pas later in de levels iets gedaan met betrekking tot wapens oppakken en upgrades kopen, maar deze mechanics heeft de speler niet per se nodig om het spel te spelen. Ook kan het overweldigend zijn om alle mechanics aan het begin te proppen. Hierom spreiden wij het uit. Wij zijn op dit moment bezig met het implementeren van waves en boss fights. Dit zou de level structure moeten verbeteren zodra het werkt.

### Polish
Met polish wordt bedoeld dat effecten in het spel op een positieve manier overgedragen worden aan de speler. Dit wordt gedaan aan de hand van UI-elementen of geluidseffecten. Denk hierbij aan elementen als damage indicators als de speler of enemies geraakt worden, een pick-up sound effect of een visueel effect bij het oppakken van een extraordinair item. Polish is heel belangrijk voor het informeren van de speler wat er gaande is in een spel. Het geeft feedback op de speler wanneer deze positieve/negatieve acties uitvoert. Zonder polish voelt een spel heel eenzijdig; het spel communiceert niet terug naar de speler wanneer de speler iets naar het spel communiceerd.

In ons spel hanteren wij polish door enemies die geraakt zijn van het spel te verwijderen. Als de speler geraakt is, dan flasht hij/zij in een bloedrode kleur, zodat te zien is dat de speler HP is verloren. Naast onze speler staat een health counter en een dash cooldown indicator. Deze helpen de speler met het correct weergeven van de resources die hij/zij op elk moment bezit. Hierdoor kan de speler beter geinfomeerd keuzes maken.



## Bronnenlijst
[Internal economy how-to design](https://www.peachpit.com/articles/article.aspx?p=1925649)
