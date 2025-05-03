# "Orcfall: Descent into Darkness" Game Design Dokument 

## Koncept gry
"Orcfall: Descent into Darkness" to gra roguelike, w której gracz wciela się w wojownika przybywającego do wioski nękanej przez orki zamieszkujące mroczne lochy. Głównym zadaniem jest przedarcie się przez niebezpieczne, losowo generowane poziomy i pokonanie potężnego Króla Orków, który rządzi na ich dnie. Po drodze gracz odkryje sekrety lochów, zdobywając potężne bronie i artefakty oraz rozwijając swoją postać.


## Bohater
Wojownik (@), posiada następujące cechy:
- HP - poziom życia 
    - Reprezentuje zdolność bohatera do przetrwania obrażeń zadawanych przez przeciwników.
    - Domyślna wartość: 25 HP.
    - Zwiększa się w miarę zdobywania doświadczenia lub po znalezieniu specjalnych przedmiotów (np. mikstur leczenia, artefaktów zwiększających maksymalne życie).
    - Spada w wyniku otrzymania obrażeń. Jeśli spadnie do 0, bohater ginie.
- XP - poziom doświadczenia
    - Reprezentuje postęp bohatera w grze, zdobywany poprzez pokonywanie przeciwników, wykonywanie zadań lub znajdowanie skarbów.
    - Wzrost poziomu doświadczenia może:
        - Zwiększyć maksymalny poziom HP.
        - Zwiększyć wartości ATK i DEF.
        - Otworzyć dostęp do unikalnych zdolności lub bonusów.
    - System XP działa w oparciu o progi poziomów (np. osiągnięcie 100 XP podnosi bohatera na wyższy poziom).
- GD - ilość golda 
    - Złoto można zdobywać poprzez eksplorację lochów, grabienie przeciwników.
    - Wykorzystywane do zakupu przedmiotów, potężniejszych broni lub usług (np. leczenia).
- LU - poziom szczęścia 
    - Wartość wyrażona w procentach, w przedziale od -100% do 100%.
- ATK - aktualna wartość ataku
    - Określa obrażenia zadawane przeciwnikom podczas walki.
    - Zwiększana za pomocą broni, artefaktów, buffów lub osiągania kolejnych poziomów XP.
- DEF - aktualna wartość obrony
    - Określa zdolność bohatera do redukcji obrażeń otrzymywanych od przeciwników.
    - Wartość obrony rośnie dzięki noszeniu zbroi i innych przedmiotów defensywnych.
    - Wpływa również na szanse unikania obrażeń (w połączeniu ze szczęściem).
- EQ - ilość przedmiotów które gracz może unieść
    - Maksymalna liczba przedmiotów, które bohater może unieść.
    - Przekroczenie limitu EQ uniemożliwia podniesienie nowych przedmiotów.

### Ekwipunek Bohatera
Ekwipunek bohatera składa się ze specjalnych slotów przeznaczonych na konkretne typy przedmiotów oraz przestrzeni na przedmioty zwykłe. 
Każdy slot pozwala na przypisanie jednego unikalnego przedmiotu, który modyfikuje statystyki bohatera.

#### Główne Sloty Ekwipunku
- Zbroja (Body Armor):
    - Opis: Chroni ciało bohatera, zwiększając wartość obrony (DEF).
    - Przykłady przedmiotów:
        - Skórzana Zbroja (+2 DEF).
        - Kolczuga (+4 DEF).
        - Magiczna Zbroja (+6 DEF, +5 LU).
- Hełm (Helmet):
    - Opis: Chroni głowę bohatera, zwiększając DEF lub wpływając na inne statystyki.
    - Przykłady przedmiotów:
        - Żelazny Hełm (+1 DEF).
        - Hełm z Rogami (+2 DEF, +1 ATK).
        - Hełm Mędrca (+3 DEF, +10 LU).
- Broń Główna (Main Weapon):
    - Opis: Podstawowe narzędzie walki, które bezpośrednio wpływa na wartość ataku (ATK).
    - Przykłady przedmiotów:
        - Miecz (+5 ATK).
        - Topór Dwuręczny (+8 ATK, -1 DEF).
        - Magiczna Różdżka (+3 ATK, +10 LU).
- Artefakt (Artifact):
    - Gracz może używać jednocześnie dwóch artefaktów
    - Opis: Rzadki przedmiot zapewniający unikalne efekty i bonusy.
    - Przykłady przedmiotów:
        - Pierścień Szczęścia (+20 LU).
        - Amulet Życia (+10 HP).
        - Kamień Mocy (+3 ATK, +3 DEF).
    - Efekt specjalny: Artefakty mogą wpływać na wiele statystyk naraz, a ich efekty są często trudne do zdobycia.

#### Zarządzanie Ekwipunkiem
Limit miejsc w ekwipunku: Bohater może nosić ograniczoną liczbę przedmiotów (określoną przez statystykę EQ). Jeśli limit zostanie przekroczony, bohater nie może podnieść nowych przedmiotów.

Przedmioty w slotach: Wymiana przedmiotu w jednym ze slotów (np. zmiana zbroi) automatycznie przenosi poprzedni przedmiot do ekwipunku ogólnego lub na ziemię.

Efekty kumulacji: Tylko efekty aktywne z aktualnie wyposażonych przedmiotów są brane pod uwagę w statystykach bohatera.

W sklepie, który jest w jaskini można kupić lub sprzedać przedmioty.

### Drzewko umiejętności i wbijanie poziomów
- Umiejetności:
    - "Zdrowy jak Ryba" zwiększa maksymalne HP
    - "Trening obsługi miecza" zwiększa ATK
    - "Gruba skóra" zwiększa DEF
    - "Szczęśliwy traf" zwiększa LU
    - "Zawsze miałem łeb do interesów" zwiększa mnożnik zdobywanego Golda
- Poziomy:
    - pierwszy poziom jest za 100XP
    - każdy kolejny wymaga 40% więcej XP niż poprzedni
    - kazdy poziom daje jeden punkt umiejętności, który można przeznaczyć na jedną z powyższych umiejętności
    - każda umiejętność zwiększa daną statystykę o 3 jednostki
    - zdobywanie doświadczenia:
        - małe ilości za zbiernie przedmiotów
        - troszkę więcej za pokonywanie przeciwników



## Przeciwnicy 
- Posiadają podobne cechy co główny bohater (HP, XP, GD, LU, ATK, DEF, EQ)
- Są coraz mocniejsi na każdym kolejnym poziomie, żeby walka nie robiła się zbyt łatwa, gdy gracz zdobędzie lepsze przedmioty
- Podczas walki mogą użyć mikstur, żeby się uleczyć
- Lista przeciwników: 
    - Szczur (s) - bardzo łatwy do pokonania, występuje tylko w jaskiniach
    - Zwykły Ork (O) - najłatwiejszy do pokonania
    - Ork Wojownik (W) - posiada zwiększony atak, w porównaniu do Zwykłego Orka, ale ma też mniejszą obronę
    - Ork Berserker (B) - Dziki wojownik, który wpada w szał bitewny, atakując z brutalną siłą. Średnie HP, bardzo wysoki ATK, ale niska DEF
    - Ork Obrońca Króla (G) - dobrze doposażone jednostki, widać że nie żałowali golda na wyposażenie, dzięki temu posiadają zwiększony ATK i DEF
    - Król Orków (K) - Największy ze wszystkich orków, przez co ma najwięcej życia, posiada dużo HP oraz ma zwiększony ATK, jedynym jego słabym punktem jest to że przez swoje rozmiary nie mieści się w żadną zbroję więc ma DEF na średnim poziomie

### Ruch przeciwników
- Jeśli są w pobliżu gracza to
    - idą w jego kierunku 
    - uciekają od niego jeśli gracz ma dużo lepsze statystyki
- Jeśli gracza nie ma w pobliżu to ruszają się w sposób losowy

## Walka 
Walka w grze opiera się na statystykach ATK, DEF i LU oraz rzutach kośćmi, co wprowadza element losowości i strategicznego wykorzystania szczęścia.

### Podstawowe Zasady
1. Obliczanie Ataku i Obrony:
- Atakujący: ATK + wynik z K6
- Broniący się: DEF + wynik z K6
2.  Porównanie Wyników:
- Jeśli wartość ataku przewyższa wartość obrony, przeciwnik otrzymuje obrażenia równe: Atak-Obrona.
- W przeciwnym razie atak zadaje obrażenia równe 1 (ma to na celu uniknięcie sytuacji gdy w której 2 Istoty mające duży DEF i mały ATK biły by się bez konca)

### Wpływ Szczęścia (LU)
Statystyka LU (Szczęście) może wywołać efekty specjalne zarówno podczas ataku, jak i obrony. Każda walcząca postać rzuca dodatkową kością K100, aby określić, czy szczęście wpływa na wynik.

Podczas Ataku:
- Szczęście Pozytywne (LU > 0):
    - Jeśli wynik K100 <= LU, atak jest krytyczny
    - Wartość Ataku = ATK + wynik z 2x K6
  
- Szczęście Negatywne (LU < 0):
    - Jeśli wynik K100 <= ∣LU∣, atak jest fatalny
    - Wartość Ataku = ATK − wynik z K6.

Podczas Obrony:
- Szczęście Pozytywne (LU > 0):
    - Jeśli wynik K100 < LU, obrona jest wzmocniona
    - Wartość Obrony = DEF + wynik z 2x K6.
- Szczęście Negatywne (LU < 0):
    - Jeśli wynik  K100<∣LU∣, obrona jest fatalna:
    - Wartość Obrony = DEF − wynik z K6.

### Dodatkowe Akcje w Walce
#### Korzystanie z Mikstur i Eliksirów
Podczas walki gracz może skorzystać z mikstur znajdujących się w ekwipunku. 
 
Mikstury:
- Przywracać punkty życia (HP).
- Uwaga: Skorzystanie z mikstury zajmuje jedną turę, podczas której przeciwnik ma okazję zaatakować.
 
Eliksiry:
- Tymczasowo zwiększać statystyki ATK, DEF lub LU.
- Ich efekt działa tylko przez określoną ilość walki
- Muszą być użyte przed walką

#### Ucieczka z Walki
Gracz może spróbować uciec z walki. Jednak zanim ucieczka się powiedzie:
- Przeciwnik wykonuje jeszcze jeden atak, który należy odeprzeć.
- Po udanej obronie gracz opuszcza walkę i wraca do bezpiecznego obszaru.
- Wskazówka: Decyzja o ucieczce może być kluczowa, szczególnie przy niskim poziomie HP lub w przypadku trudniejszych przeciwników.
 
## Mapa - jaskinie i lochy

Lochy w "Orcfall: Descent into Darkness" to losowo generowane poziomy, wypełnione przeciwnikami, pułapkami oraz skarbami. Każdy poziom staje się coraz bardziej wymagający w miarę zagłębiania się w grę, co odzwierciedla rosnący poziom trudności przeciwników i skomplikowanie układu lochów. Kluczowym elementem rozgrywki jest eksploracja i pokonywanie przeszkód w losowo generowanym świecie.

### Metody generowania lochów i jaskiń:

- #### Metoda 1: Dynamiczne łączenie pomieszczeń

Pierwsza metoda polega na losowym rozmieszczaniu pomieszczeń i dynamicznym łączeniu ich za pomocą korytarzy. Proces rozpoczyna się od wybrania dwóch pomieszczeń, między którymi tworzony jest korytarz. Aby uniknąć powstawania prostych, liniowych połączeń, na mapie generowane są tymczasowe przeszkody, zmuszając algorytm do tworzenia bardziej skomplikowanych ścieżek. Następnie do powstałej struktury dołączane są kolejne pomieszczenia, które są łączone z poprzednimi w podobny sposób.

Metoda ta generuje mapy o nieregularnym układzie, z wieloma alternatywnymi ścieżkami oraz rozległymi korytarzami, co zachęca gracza do eksploracji i odkrywania całej mapy.

<img src="image-1.png" width="800" height="800">

- #### Metoda 2: Sortowanie pomieszczeń

Druga metoda rozpoczyna się od losowego rozmieszczenia pomieszczeń, które następnie są sortowane, aby tworzyły układ mniej chaotyczny, zazwyczaj przebiegający od góry do dołu. Algorytm stara się minimalizować liczbę połączeń między korytarzami, co utrudnia omijanie pomieszczeń. W rezultacie powstaje mapa, na której gracz musi eksplorować kolejne pomieszczenia w bardziej logicznym porządku.

Ten rodzaj generacji tworzy bardziej uporządkowane lochy z mniejszą liczbą korytarzy, co sprawia, że eksploracja staje się bardziej wymuszona i systematyczna. Pomaga to graczowi skupić się na pokonywaniu wyzwań w każdym pomieszczeniu.

<img src="image-2.png" width="800" height="800">

- #### Metoda 3: Generowanie jaskiń

Jaskinie stanowią alternatywę dla lochów, oferując bardziej otwarte przestrzenie z nieregularnymi korytarzami. Generowanie jaskiń opiera się na automatach komórkowych. Proces rozpoczyna się od losowego rozmieszczenia ścian na mapie, a następnie zastosowania iteracyjnych reguł, które określają, czy dany obszar pozostaje ścianą czy zamienia się w przestrzeń otwartą, w zależności od liczby sąsiadujących ścian.

Po kilku iteracjach mapa zyskuje organiczny układ przypominający naturalne jaskinie. Kolejny krok to zapewnienie odpowiedniej grywalności - algorytm sprawdza, czy istnieje wystarczająco duży, połączony obszar otwarty, w którym można umieścić 'drzwi' powrotne do poprzedniego poziomu.

Jaskinie pełnią rolę poziomów dodatkowych, w których gracz może znaleźć rzadkie przedmioty oraz rozwijać swojego bohatera. Eksploracja tych poziomów jest opcjonalna, ale zapewnia unikalne wyzwania i możliwości rozwoju, które mogą okazać się kluczowe w dalszej części gry.

<img src="image.png" width="800" height="800">