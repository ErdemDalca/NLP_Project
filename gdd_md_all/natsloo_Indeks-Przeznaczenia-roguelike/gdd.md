# "Indeks Przeznaczenia" Game Design Document - wersja 2.6.1

### Tabela zmian
| **Wersja** |   **Data**    |  **Komentarz**   |
| :--------: | :-----------: | :--------------: |
|    1.0     | 12-15/10/2024 | Wersja startowa. |
|    1.1     | 18/10/2024    | Rework mechanik i kilka nowych elementów. |
|    1.1.1   | 14/11/2024    | Małe poprawki.   |
|    1.3     | 21/11/2024    | Mechanizm walki. |
|    2.0     | 22-23/11/2024 | Duży rework pomysłu na grę. |
| 	 2.0.1   | 28/11/2024    | Reorganizacja sekcji "Mechaniki w grze". |
|    2.1     | 28/11-03/12/2024 | Poprawki do walki. |
|    2.1.1   | 05/12/2024 	 | Drobne poprawki do sekcji "Przeciwnicy". |
|    2.3	 | 11/01/2025    | Rozwinięcie lub utworzenie opisów cech, ekwipunku, przedmiotów, rozwoju bohatera, map w grze. |
|	 2.5	 | 15/01/2025    | Przepisanie sekcji "Przedmioty i inne poprawki. |
|	 2.5.1	 | 15/01/2025    | Dodanie opisu jednego pominiętego bossa. |
| 	 2.5.2	 | 19/01/2025	 | Drobne poprawki i jeden dodatkowy przedmiot. |
|    2.6	 | 30/01/2025    | Finalizacja. |
|	 2.6.1   | 30/01/2025    | Dodanie opisu ruchu przeciwników. |

# Wprowadzenie
Dokument ten określa aspekty projektowe gry komputerowej pod roboczym tytułem "Indeks Przeznaczenia" autorstwa Natalii Kuśmierczyk, tworzonej w semestrze zimowym 2024/2025 II roku Informatyki na potrzeby przedmiotu "Programowanie gier łotropodobnych".

### Cel dokumentu
Dokument ten powstaje jako swego rodzaju encyklopedia projektowa pomocna w całym procesie powstawania gry "Indeks Przeznaczenia" - projektowaniu, kodowaniu, testowaniu programu.

### Konwencja dokumentu
Elementy pewne, konieczne i/lub już dokonane będą zapisywane pismem prostym.
_Pomysły, elementy niepewne lub luki w kreatywności będą zaznaczane kursywą i/lub znakami zapytania_.

---
# Opis
### Koncept gry
"Indeks Przeznaczenia" to gra roguelike (łotropodobna) dla pojedynczego gracza na PC. Jej główny bohater to student informatyki, starający się pogodzić swoje życie prywatne i naukowe, tak by zdać wszystkie egzaminy, obronić pracę i skończyć studia, a przy tym nie oszaleć i dobrze się bawić.

### Bohater
Student informatyki.

##### Cechy i stany bohatera:
- poziom wiedzy:
	- startowa wartość: 0;
	- wpływ:
		- to podstawowy wyznacznik rozwoju bohatera;
		- za każde 10 PW bohater dostaje bonus do szczęścia i humoru oraz redukcję stresu;
		- od PW zależy, czy bohater atakuje pierwszy w walkach;
		- zdobywane przede wszystkim poprzez pokonywanie przeciwników - po każdej wygranej walce wzrasta o 1/3 poziomu oświecenia (PS, czyli punktów życia) przeciwnika; 
- szczęście:
	- startowa wartość: 1, wartości +/- w przedziale <0,2>;
	- wpływ:
		- stanowi mnożnik PW, stresu i humoru;
- stan konta:
	- startowa wartość: 500 zł;
	- wpływ:
		- brak pieniędzy = brak możliwości zakupu jedzenia = głód;
		- brak pieniędzy = brak możliwości dokupienia lepszych broni = bronie podstawowe = trudniejsze walki = większa szansa na przegraną;
		- pieniądze pochodzą ze znajdowanych przedmiotów;
- odpoczynek:
	- startowa wartość: 100/100;
	- wpływ:
		- jeśli wyniesie 0, gra się kończy z powodu wycieńczenia bohatera;
		- każde 25 punktów stresu powyżej wartości bazowej odejmuje 10 punktów odpoczynku;
- stres:
	- startowa wartość: 50/200
	- wpływ:
		- ataki wroga zwiększają poziom stresu;
		- gdy stres osiąga 200, bohater rzuca studia i gra się kończy;
- humor:
	- wartości:
		- 0/100 - Depresja;
		- 25/100 - Smutny;
		- 50/100 - Neutralny;
		- 75/100 - Szczęśliwy;
		- 100/100 - Euforia;
	- startowa wartość: Neutralny;
	- wpływ:
		- ataki wroga zmniejszają poziom humoru;
		- gdy humor spada do 0, bohater wpada w depresję i rzuca studia, więc gra się kończy;
		- pokonywanie przeciwników daje + do humoru;
- pełny brzuszek:
	- startowa wartość: 100/100;
	- wpływ:
		- każda walka zabiera -PS przeciwnika punktów głodu;
		- jedzenie kupione w sklepie i jadalne przedmioty znalezione na planszach zmniejszają głód;
		- jeśli wyniesie 0/100 - rodzice bohatera zabierają go do domu z powodu zagłodzenia, gra się kończy;
 
### Miejsce akcji
Gra ma miejsce w Lublinie. Lokacjami w grze są:
- niesprecyzowana uczelnia studenta - odbywają się tam wykłady, ćwiczenia, konsultacje, rozmowy z promotorem i wszystkie walki z bossami (egzaminami, kolokwiami, wejściówkami...);
- miasto, a w nim:
	- miejsce zamieszkania bohatera: dom studencki - może się w nim uczyć, odpoczywać, spotykać ze znajomymi;
	- klub - miejsce imprez ze znajomymi;
	- biblioteka - miejsce na spokojną naukę w ciszy;
	- park - czasem trzeba dotknąć trawy;
	- mieszkania znajomych - można się razem uczyć albo zrobić domówkę;
	- sklepy - miejsce zakupu broni;
	- stołówka - miejsce obiadów.

### Mechaniki w grze
##### Plansze poziomów
Gra zaczyna się w akademiku bohatera. Po wejściu na drzwi bohater może wyjść do miasta i odwiedzać lokacje w grze. Plansza miasta oraz jest stała i zawsze wygląda tak samo, plansze innych miejsc generują się za każdym razem, gdy gracz je odwiedza. Generują się w nich również przedmioty i istoty. Sklep i stołówka to osobne interfejsy.

##### Generacja plansz losowych
Do tworzenia plansz losowych używane są trzy algorytmy/sposoby generacji.
Plansze uczelni są generowane za pomocą algorytmu używającego losowej liczby pivotów losowo ustawianych na mapie o podanych wymiarach. Każdy pivot stanowi lewy górny róg pomieszczenia, którego rozmiar jest generowany losowo z podanego zakresu <min, max>. Pivoty są potem łączone korytarzami, aby wszystkie pomieszczenia były dostępne. Na mapie wstawiane są obiekty i istoty, a na końcu para drzwi: do przechodzenia na poprzedni i następny poziom.

![przykładowa plansza uczelni](image.png "przykładowa plansza uczelni")

Plansze akademika, biblioteki i innych pomieszczeń poza parkiem są generowane prostym algorytmem typu BSP (binary space partitioning), który tworzy najpierw jedno duże pomieszczenie, a potem próbuje je podzielić podaną ilością poziomych i pionowych linii na mniejsze pomieszczenia o podanym rozmiarze. Każde pomieszenie ma drzwi stanowiące przejścia do sąsiednich pomieszczeń. Na mapie wstawiane są obiekty i istoty, a na końcu para drzwi: do przechodzenia na poprzedni i następny poziom.

![przykładowa plansza innych miejsc](image-1.png "przykładowa plansza innych miejsc")

Plansze parku są generowanie algorytmem typu automat komórkowy, który najpierw wypełnia mapę polami drzew lub trawy na podstawie zadanego prawdopodobieństwa, a później liczy ilość sąsiadów typu drzewo dla każdego pola. Jeśli ta ilość jest równa lub przekracza zadany próg, pole staje się lub pozostaje drzewem, jeśli ilość jest poniżej tego progu, pole staje się lub pozostaje trawą. Potem wstawiana jest pozioma rzeka, która ma losowaną z przedziału <3,5> szerokość, a także losowe małe przesunięcia. Następnie wstawiana jest pionowa ścieżka, a jeśli napotkane pole mapy było wcześniej rzeką - most. Ścieżka też ma losowe delikatne przesunięcia. Potem dodawane są dodatkowe mosty losowane z przedziału <0,5>, istoty i przedmioty, a także para drzwi: do przechodzenia na poprzedni i następny poziom, jedne drzwi na początku ścieżki, drugie na końcu.

![przykładowa plansza parku](image-2.png "przykładowa plansza parku")


##### Ekwipunek
Podstawowym ekwipunkiem są kieszenie bohatera - 5 miejsc. Ekwipunek może być rozszerzony poprzez znalezienie przedmiotu "nowy plecak", który dodaje za każdym razem po znalezieniu dodatkowe 3 miejsca do ekwipunku. Miejsca dodatkowe można też stracić, poprzez znalezienie przedmiotu "huligani z Dziesiątej". Przedmioty z ekwipunku mogą być użyte w walce.

##### Przedmioty
Bohater napotyka w różnych miejscach w grze różne przedmioty lub obiekty. Część z nich to bronie specjalne oraz jedzenie, które zajmują miejsce w ekwipunku. Są też obiekty, które mają różnorakie efekty, ale nie zajmują miejsca. Przedmioty są na mapach oznaczane `*` w kolorze jasnoniebieskim.
W poszczególnych miejscach można znaleźć efekty, bronie i jedzenie:
- uczelnia:
	- stypendium rektora - mityczny boost, po każdej wygranej walce dodaje do stanu konta 100zł;
	- zepsuty laptop;
	- niezapisana praca;
	- bronie specjalne (patrz sekcja "Bronie i przedmioty, z których można korzystać w walce");
	- darmowe ksero;
	- przedawkowanie kofeiny;
	- wspólna nauka;
	- stare notatki;
	- koszulka uczelni;
	- tuptup;
	- członkostwo koła naukowego;
	- dociekliwość;
- miasto:
	- pieniądze na ulicy;
	- zgubiony portfel;
	- nowy plecak (rzadki przedmiot, zwiększenie ilości miejsc w ekwipunku o 3 miejsca);
	- chuligani z Dziesiątej (zmniejszenie ilości miejsc w ekwipunku do wartości bazowej);
	- kupon rabatowy do sklepu;
	- darmowe ksero;
	- kanary;
	- spotkanie starego znajomego;
- park:
	- pieniądze na ulicy;
	- zgubiony portfel;
	- nowy plecak (rzadki przedmiot, zwiększenie ilości miejsc w ekwipunku o 3 miejsca);
	- chuligani z Dziesiątej (zmniejszenie ilości miejsc w ekwipunku do wartości bazowej);
	- spotkanie starego znajomego;
	- bezpłatny koncert;
	- spotkanie starego znajomego;
- dom studencki:
	- przelew od rodziców;
	- chrapiący wspólokator;
	- niespodziewana kontrola czystości pokoju;
	- nowa poduszka;
	- bronie specjalne;
	- zepsuty laptop;
	- niezapisana praca;
	- przedawkowanie kofeiny;
	- wspólna nauka;
	- dociekliwość;
- biblioteka:
	- stare notatki;
	- pusta biblioteka;
	- kara za przetrzymanie;
	- nowa ulubiona książka;
	- zepsuty laptop;
	- niezapisana praca;
	- spotkanie starego znajomego;
	- wspólna nauka;
	- dociekliwość;
- klub:
	- darmowy drink;
	- przedawkowanie kofeiny;
	- dzwonienie w uszach;
	- zgubione klucze;
	- zgubiona ładowarka;
	- impreza;
	- spotkanie starego znajomego;
	- koncert jazzowy;
- mieszkania znajomych:
	- zgubiona ładowarka;
	- zgubione klucze;
	- wspólna nauka;
	- impreza;
	- bronie specjalne;
	- zepsuty laptop;
	- niezapisana praca;
	- przedawkowanie kofeiny;
	- stare notatki;
	- spotkanie starego znajomego.

##### Walka
Każda walka to naprzemienne ataki bohatera i bossa. Kolejność walki zależy od punktów PS (boss) i PW (bohater), kto ma więcej, ten atakuje pierwszy. Bossowie możliwi do spotkania są wybierani losowo i umieszczani na mapie. Walka zaczyna się poprzez wejście bohatera na pole przeciwnika. Przeciwnicy będą oznaczeni `!` w kolorze fioletowym. Ataki przeciwników będą wybierane losowo: wartości FS i NN są przy każdym ataku przeciwnika losowane z przedziału <min, max>, gdzie liczby w przedziale ∈ ℕ. Również typ (nazwa) ataku jest losowany za każdym razem. Ataki bohatera będą zależały od gracza i jego ekwipunku. 

Po pokonaniu przeciwnika, ilość PW bohatera wzrasta o 1/3 PS pokonanego przeciwnika, humor bohatera wzrasta o 1/3 max_NN przeciwnika. Do tych wartości będzie stosowana funkcja `floor()`. Po przegraniu walki gra się kończy. Walkę można przegrać poprzez osiągnięcie przez bohatera poziomu stresu = 200 i/lub poziomu humoru = 0.

##### Przeciwnicy 
Przeciwnicy charakteryzują się:
- poziomem oświecenia (PS) - to punkty życia bossa, muszą zostać zmniejszone do zera, aby boss został pokonany;
- faktorem stresu (FS) - maksymalna ilość stresu, która może zostać dodana w wyniku jednego ataku przeciwnika do poziomu stresu bohatera;
- neurodegradacją nastroju (NN) - maksymalna ilość humoru, która może zostać odjęta w wyniku jednego ataku do poziomu humoru bohatera.

Co 50 ms następuje losowanie ruchu przeciwnika w jednym z czerech kierunków albo spoczynku. Jeśli bohater jest w promieniu 10 kratek, to przeciwnicy będą się kierować w jego stronę, jeśli nie - będą wykonywać losowe ruchy.

Przeciwnicy bohatera to: 
- wejściówki, od początku gry;
	- PS: <1,5>;
	- FS: <1,4>;
	- NN: <1,4>;
	- ataki:
		- pytania otwarte;
		- mało czasu;
		-
- praca domowa, od początku gry;
	- PS: <1,5>;
	- FS: <1,3>;
	- NN: <1,3>;
	- ataki:
		- od kiedy Ty się Sebastian Tyda nazywasz?;
		- plagiat;
		- krótki termin;
		- crash edytora tekstowego;
		- działa tylko na emulatorze (na DSM-51 już nie);
		- zapomniało się zrobić;
		- koszmar;
		- można taniej;
		-
- referaty, mogą się pojawiać po 5 wygranych walkach:
	- PS: <4,8>;
	- FS: <1,5>;
	- NN: <1,4>;
	- ataki:
		- głupi temat;
		- krótki czas;
		- crash edytora tekstowego;
		-
- projekty, po 10 walkach:
	- PS: <7,10>;
	- FS: <2,8>;
	- NN: <4,6>;
	- ataki:
		- beznadziejna grupa projektowa;
		- głupi temat;
		- konflikty;
		- 
- kolokwia, po 16 walkach:
	- PS: <11,17>;
	- FS: <3,10>;
	- NN: <3,10>;
	- pisemne - ataki:
		- pytania otwarte;
		- pytania zamknięte;
		- mało czasu;
		- słabo widoczne polecenia;
		- baza nie siadła;
		-
	- programistyczne - ataki:
		- mało czasu;
		- null pointer exception;
		- memory leak;
		- 

- sesja egzaminacyjna, po 20 walkach:
	- PS: <14,25>;
	- FS: <6,15>;
	- NN: <4,12>;
	- ustne - ataki:
		- upierdliwy egzaminator;
		- zaskakujące pytania;
		- trema;
		- 
	- pisemne - ataki:
		- pytania otwarte;
		- pytania zamknięte;
		- mało czasu;
		- baza nie siadła;
		- egzamin miał być na komputerze, ale nie ma internetu, więc piszesz na kartce;
		- 
	- programistyczne - ataki:
		- mało czasu;
		- null pointer exception;
		- memory leak;
		- stack overflow;
		- 
- final boss: obrona pracy; ostatni przeciwnik, po 50 walkach:
	- PS: <35,45>;
	- FS max: <9,20>;
	- NN max: <7,15>;
	- ataki:
		- złożone pytania;
		- nieodpisujący promotor;
		- ciężka komisja;
		- trema;
		-	

##### Bronie i przedmioty, z których można korzystać w walce:
- podstawowe: 
	- można używać bez ograniczeń;
	- zadają nieduże obrażenia, <1-3 PS>; 
	- dwie losowe bohater ma w ekwipunku na początku gry, resztę może dokupić:
		- długopisy - "Czarne czy niebieskie?", 2 PS;
		- papier kancelaryjny - "Pożyczysz kartkę?", 1 PS;
		- kalkulator prosty - "2 + 2 = 5", 2 PS;
		- dokumentacja - "en.cppreference.com", 1 PS;
		- dobre IDE - "Wszystko, tylko nie Qt Creator!", 3 PS;
		- przypomnienia na grupie - "Grunt to dobry starosta.", 2 PS;
		- skrypt - "PDF to mój ulubiony typ pliku.", 3 PS;
		- 
- limitowane:
	- można użyć x razy na walkę;
	- zadają większe obrażenia, <3-7 PS>
	- trzeba kupić:
		- własne notatki - "Slowa spisane podczas wykladu to skarb, o ile da sie je odczytac.", 4 PS, można użyć 2 razy;
		- zadania z poprzednich lat - "Oby dal to samo.", 6 PS, można użyć 1 raz;
		- zagadnienia od prowadzącego - "Jakos im nie ufam.", 3 PS, można użyć 3 razy;
		- kalendarz akademicki - "Kiedy sesja poprawkowa?", zmiejsza stres o 10;
		- prezentacja od prowadzącego - "500 slajdow do zakucia.", 3 PS, można użyć 3 razy;
		- karta wzorów - "Jak na maturze.", 5 PS, można użyć 2 razy;
		- zwolnienie lekarskie - "Nie chce wiedziec, ile musze nadrobic.", poprawia humor o 10, zmniejsza stres o 20;
		- 
- specjalne:
	- nie można ich kupić, można tylko znaleźć:
	- można użyć tylko raz:
		- nowe przyciski klawiatury - "Ciche switche sa dla frajerow.", 9 PS;
		- wysoko latające długopisy - "Nic tak nie motywuje jak grawitacja i rozpacz.", 9 PS;
		- ściąga - "Sprytne, co?", zabiera przeciwnikowi 1/4 PS;
		- kalkulator naukowy - "Ratuje, gdy liczby zaczynaja mowic w dziwnych jezykach.", poprawia humor o 20, zmniejsza stres o 20;
		- baza pytań - "Przyda sie na pewnym przedmiocie na litere A.", pokonuje od razu przeciwnika, redukuje stres do 0 i poprawia humor na 100;
		- zdjęcie zadań wcześniejszej grupy - "Nie wszyscy bohaterowie nosza peleryny.", poprawia humor o 20 i zmniejsza stres o 20;
		- przepisanie oceny - "Darmowe ECTSy to skarb.", zabiera przeciwnikowi połowę PS;

##### Zwycięstwo
Sposobem na wygranie gry jest ukończenie studiów i obronienie pracy, czyli pokonaniem wszystkich przeciwników na swojej drodze.

---
# Technikalia
### Systemy operacyjne
Systemy, na których gra działa, to Windows i Linux. 
### Języki
Gra jest programowana w prostym C++, bez użycia dodatkowych, zewnętrznych bibliotek. 
Elementy tekstowe w interfejsie użytkownika są w języku polskim.
### Grafika
Gra działa w terminalu wybranego systemu operacyjnego, jej grafika jest zatem prosta, oparta o znaki ASCII oraz kolory konsolowe.
