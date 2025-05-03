## Game Design Document Simmac Prototyoe

#### Douwe Westerdijk & Nolan Bijmholt </br> Alfa College - 2024/2025

Versie 2.1.8

### Inhoud

  - [Inhoud](#inhoud)
  - [Game Vision](#game-vision)
  - [Technische Details](#technische-details)
  - [Gameplay overzicht](#gameplay-overzicht)
    - [Camera](#camera)
    - [Speler](#speler)
    - [Producten](#producten)
    - [Bestellingen](#bestellingen)
    - [Order Assembly Table](#order-assembly-table)
    - [Klanten](#klanten)
    - [Tussendaagse menu](#tussendaagse-menu)
  - [Minigames](#minigames)
    - [Burger Minigame - Burger Stack](#burger-minigame---burger-stack)
    - [Fries Minigame - Put the Fries In the Bag](#fries-minigame---put-the-fries-in-the-bag)
    - [Drinks Minigame - Shake Shifter](#drinks-minigame---shake-shifter)
    - [Dessert Minigame - Sniper Showdown / Pop the Cherry](#dessert-minigame---sniper-showdown--pop-the-cherry)
  - [UI](#ui)
  - [Game Manager](#game-manager)
  - [Save States](#save-states)


---

### **Game Vision**

*Simmac is een restaurant tycoon/simulator. Jij neemt de rol aan van restaurantmanager. Het is jouw taak om alles in orde te houden en het restaurant zo waardevol mogelijk te maken. Dit doe je door bestellingen te plaatsen, werknemers aan te nemen en te managen. Daarnaast moet je effectief complicaties binnen en buiten het restaurant behandelen om het restaurant draaiende te houden.
Dit doe je in een systeem dat elke dag bijna onmerkbaar lastiger wordt, waardoor de stress nooit weggaat. Kun jij een nieuwe hoge score behalen?*

Wij gaan een prototype maken van Simmac om te onderzoeken hoe de gameloop van het bestellingen plaatsen in herhalende minigames wordt ervaren. In dit GDD zijn alle features van dit prototype uitgewerkt, en deze zullen op basis van feedback verder worden uitgewerkt tijdens de ontwikkeling van het uiteindelijke spel.

---

### **Technische Details**

- **Engine:** *Unity 6000.0.40f1*
- **Platform:** *PC*
- **Besturing:** *Toetsenbord en muis*

---

### **Gameplay overzicht**

Jij speelt als restaurantmanager van Simmac. Je kan rondlopen binnen het
restaurant, de benodigde keuken- en servicefuncties bedienen door op de
stations te klikken, en hun minigames te spelen om bestellingen te maken.

Aan het einde van de dag krijg je een overzicht van de boekhoudgegevens
van het restaurant. Hier kun je kiezen om personeel aan te nemen.

#### **Camera**

Simmac is een 2D-spel met een camera die de speler volgt. Als je de
camera maximaal uitzoomt, krijg je het hele restaurant van boven te zien.

#### **Speler**

De speler kan vrij rondlopen in het restaurant en interacteren met de wereld. De
speler beweegt met het toetsenbord en gebruikt de muis voor interacties.

De speler moet dichtbij een station staan om hier op te kunnen klikken.

#### **Producten**

Producten worden bereid en geserveerd – dit is de taak van de speler.
Het kost geld om een product te maken, het is aan de speler om te zorgen dat je de
juiste producten maakt om geen onnodig geld uit te geven.

Producten hebben vier verschillende types: standaard, rood, groen en blauw. Deze types zijn als vervanger voor hoe je in het echt verschillende soorten burgers en drankjes kan bestellen. Deze types kosten de speler geen extra geld.

Verder beschikken de producten over een kwaliteitsmeter, die varieert van 0 tot 100. De kwaliteit van de bestelling wordt bepaald door het gemiddelde van de verschillende kwaliteiten, wat invloed heeft op de tevredenheid van de klant.

Het spel bevat vier producten: milkshakes, burgers, friet en desserts.

#### **Bestellingen**

Een bestelling wordt geplaats wanneer een klant naar de kassa voorin het restaurant
loopt. De klant wacht voor de kassa totdat de speler hier heen loopt en op de klant klikt

Wanneer een klant een bestelling plaatst, wordt deze opgeslagen in de Game Manager
en weergegeven in de UI.

De speler moet de juiste stations gebruiken om de bestelling te maken. Als een
product is gemaakt, wordt het op de Order Assembly Table (OAT) geplaatst.

Zodra alle producten voor een bestelling op de OAT liggen, wordt de bestelling
automatisch afgegeven.

#### **Order Assembly Table**

De OAT is een centrale verzamelplaats voor alle gemaakte consumpties in de keuken. Alles wat in de keuken gemaakt wordt eindigt in de OAT voordat het naar een klant gaat.

Des te langer een product in de OAT ligt, des te slechter de kwaliteit zal worden.
Het is niet aan te raden om producten te maken zonder bestelling.

Oudere bestellingen krijgen prioriteit naar de klant. De speler kan producten uit de OAT weggooien als ze te oud zijn. Als je dit niet doet kan een verouderd product aan de klant gegeven worden, waardoor de klant ontevreden zal zijn.

#### **Klanten**

Klanten bestellen bij de kassa. De bestelling wordt in de UI weergegeven.

Klanten hebben een tevredenheidsmeter.
Terwijl ze wachten, daalt hun tevredenheid. Deze timer bepaald de tevredenheid die
een klant kan hebben. Stel een klant wacht te lang en heeft een tevredenheid van 90%, dan is de beste tevredenheid voor deze klant dus 90%, ongeacht van hoe goed het eten is.

De tevredenheid van de klant is ook gebonden aan hoe goed het eten gemaakt is, en
hoe oud dit eten is. Als je de minigames goed speelt resulteert dit in eten van 100%
kwaliteit. Hoe langer eten in de OAT ligt, hoe lager de kwaliteit zal worden. De kwaliteit van het eten daalt lineair met de tijd.

Nadat ze hun bestelling krijgen, stijgt of daalt hun tevredenheid afhankelijk van
de kwaliteit van het eten. Daarna verlaten ze het restaurant.

#### **Tussendaagse menu**

Aan het einde van de dag krijgt de speler het tussendaagse menu. Hier wordt eerst een overzicht gepresenteerd voor alle inkomsten en uitgaves.

En daarna een menu gepresenteerd waar wat algemene statistieken staan (de huidige dag, hoeveel geld, etc.). De speler kan hier naar de volgende dag gaan.

---

### **Minigames**

Je start een minigame door op een station te klikken. Elk station waar je eten / drinken maakt heeft een unieke minigame. Je kan alleen op de stations klikken als je er naast staat. Na het spelen van de minigame, verschijnt de consumptie die je hebt gemaakt in de OAT

#### **Burger Minigame - Burger Stack**

In de Burger Stack moet je proberen een perfecte burger te maken. Dit doe je door alle ingrediënten perfect te stapelen.
Je begint met het onderste broodje die je links en rechts kan bewegen terwijl ingrediënten uit de lucht vallen. Probeer deze zo recht mogelijk op de burger op te vangen om een hogere score te krijgen.

#### **Fries Minigame - Put the Fries In the Bag**

In PFIB beweegt een frietzak onderaan het scherm. De speler beweegt de zak heen en weer om zoveel mogelijk frietjes op te vangen.

De uiteindelijke score van de speler wordt berekend door te kijken naar hoeveel frietjes de speler gevangen heeft van de totale hoeveelheid gevallen frietjes.

In het begin van het spel krijg je een frietzak van willekeurige grootte, deze
zijn small, medium & large. Grotere frietzakken maken het spel makkelijker.

#### **Drinks Minigame - Shake Shifter**

De speler ziet een transparante milkshakebeker met een percentage bovenaan. Een
kleur beweegt op en neer over de beker heen.

De speler moet klikken wanneer de vulling exact overeenkomt met het percentage.

Des te dichter bij de correcte waarde de speler klikt, des te beter de score is.

#### **Dessert Minigame - Sniper Showdown / Pop the Cherry**

De speler staat op een schietbaan en moet een kers op een ijsje schieten. Dit doet de speler met behulp van instrumenten zoals zijn afstandsmeter, windmeter en geweer.
Ook kan de speler zijn geweer calibreren voor hele verre schoten.

De speler krijgt vier pogingen om het kersje er goed op te schieten.
Bij elke misser gaat de kwaliteit met een vaste hoeveelheid omlaag en als de speler alles mist wordt de kwaliteit een vaste lage waarde.

---

### **UI**

Links boven in het scherm staan alle bestellingen, hier kun je de volgorde en de producten zien, ook staat hier welke producten al gereed zijn.

Recht boven staat hoeveel geld het restaurant heeft, dit is om de speler te motiveren om door te gaan. Ook staat hier hoe laat het is in een 24 uur's klok. Hierdoor weet de speler hoe lang de dag nog duurt.

---

### **Game Manager**

De GameManager is het centrale punt van het spel en regelt alle verbindingen van de klanten, de stations, de minigames, en de speler.

De GameManager beheert ook de savefiles en autosaves.
Deze worden opgeslagen in de persistentDataPath als een `savegame.simmac` bestand.

De tijdsdoorloop van het spel wordt ook geregeld vanuit de GameManager.

Funcies te Simmac als geheel overkoepelen en doorgegeven moeten worden aan delen van Simmac die niet geschikken over onderlinge communicatie staan ook in de GameManager om er voor te zorgen dat er een centrale plaats is waar informatie bestaat.

---

### **Save States**

De gebruiker krijgt één actieve save om mee te spelen. Deze save laadt de GameManager in, die alle benodigde informatie bevat om het spel correct op te starten.

Het spel wordt automatisch opgeslagen in het tussendaagse menu aan het einde van de dag. Hierdoor kan de speler halverwege de dag stoppen en later opnieuw proberen.

Bij het laden van het spel verschijnt één van de volgende schermen, afhankelijk van wanneer de vorige sessie eindigde:

- Het begin van de dag – Als de speler halverwege de dag is gestopt.

- Het tussendaagse menu – Als de vorige sessie aan het einde van de dag eindigde.

- Het failliet-scherm – Als de speler aan het einde van de dag failliet ging en stopte.
