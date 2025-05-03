About:
Silesian Undergrounds is game written in C# with help of Monogame framework. Project was created in order to pass university laboratories from subject "Basics of programming of 2d games" in group of 4 people(all authors mentioned in "Autorzy" section).
All assets downloaded from internet and used in game are listed in "Spis użytych grafik" and "Spis użytych ścieżek dzwiękowych" sections of this file.

# Game Design Document

## Tytuł: Silesian undergrounds

## Autorzy:
- Bartłomiej Bukowiecki (me)
- Kamil Klyta (https://github.com/gonuit)
- Tomasz Kot (https://github.com/TomaszKot11)
- Bartłomiej Wloczyk (https://github.com/Paxon96)

## High concept

Gracz wciela się w górnika imieniem Janusz. Janusz podczas codziennej, ciężkiej pracy w kopalni, wpadł w wyniku niefortunnego wypadku do głębokiej szczeliny i tak znalazł się w nieznanym podziemnym świecie. Gra należy do gatunku roguelike, a skupia się na przetrwaniu w nieznanym świecie i wydostaniu się z na powierzchnię. Głównym zadaniem gracza jest, poprzez pokonywanie kolejnych poziomów, wydostanie się na powierzchnię.

## Game flow

Podczas swojej wędrówki gracz będzie musiał walczyć z różnymi przeciwnikami oraz zbierać znajdźki i przedmioty, które będą zmieniały jego statystyki. Gra nastawiona jest na wielokrotne jej przechodzenie.

## Mechaniki:
- Generowana mapa, złożona z predefiniowanych jaskiń
- Pasek głodu, którego wartość zmniejsza się wraz z upływem czasu. Przy dojściu do 0 – gracz umiera
- Możliwość zbierania węgla oraz innych surowców służących jako waluta
- Sklep co poziom, możliwość zakupu jedzenia oraz ekwipunku
- Losowe generowanie znajdziek
- System walki, mechanika hack and slash
- Pokoje w kórych można znaleźć przedmioty specjalne

## Tilemapa i warstwy

- Warstwa 1 (Walls):
	bloki z którymi gracz koliduje

- Warstwa 2 (Background):
	bloki tła

- Warstwa 3 (Pickables):
	poprzez umieszczenie testury X (czerwony) z Tileset2 oznaczamy miejsca, w których mogą pojawić się przedmioty do podniesienia

- Warstwa 4 (Traps):
	poprzez umieszczenie testury X (zielony) z Tileset2 oznaczamy miejsca, w których mogą pojawić się płapki (kolce) zadające graczowi obrażenia

- Warstwa 5 (Transitions):
	służy do oznaczenia miejsca po wejściu na które użytkownik zostanie przeniesiony na następny poziom

- Warstwa 6 (Enemies):
	warstwa służąca do oznaczania miejsc, w których mogą pojawiać się przeciwnicy

- Warstwa 7 (SpecialItems):
	warstwa służąca do oznaczania miejsc, w których mogą pojawiać się przedmioty specjalne - mikstury zmieniające statystyki użytkownika

- Warstwa 8 (PlayerSpawn):
	warstwa służąca do oznaczania miejsca, w których spawnuje się gracz - celem uniknięcia ewentualnych kolizji z losowo
	generowanymi przedmiotami
- Warswta 9 (ShopPickables):
	warstwa służąca do generowania przedmiotów możliwych do zakupu przez użytkownika

- Warstwa 10 (RandomRooms):
	warstwa do oznaczania miejsc gdzie generują się losowe pokoje dla gracza


### Spis użytych grafik:

| Nazwa pliku w folderze Content  | Autor/Źródło | Licencja |
| ------------- | ------------- | ------------- |
| background.png  | [opengameart](https://opengameart.org/content/pixelart-menu-naturery-hand-shooting-some-green-stuff) | CC0 |
| bottom-left.png  | Kamil Klyta  | N/A |
| bottom-right.png  | Kamil Klyta  | N/A |
| bottom.png  | Kamil Klyta | N/A |
| bottom-left.png  | Kamil Klyta | N/A |
| box.png | [opengameart](https://opengameart.org/content/pixelart-menu-naturery-hand-shooting-some-green-stuff) | CC0 |
| box_lit.png | [opengameart](https://opengameart.org/content/pixelart-menu-naturery-hand-shooting-some-green-stuff) | CC0 |
| debug_box.png | Bartosz Bukowiecki | N/A |
| debug_circle.png | Bartosz Bukowiecki | N/A |
| default.png | Bartosz Bukowiecki | N/A |
| kolejne.png | Bartłomiej Wloczyk | N/A |
| ledder.png | Kamil Klyta | N/A |
| left-entry-bottom.png | Kamil Klyta | N/A |
| left-entry-top.png | Kamil Klyta | N/A |
| left.png | Kamil Klyta | N/A |
| minerCharacter.png | [opengameart](https://opengameart.org/content/dwarves) | GPL 2.0 [Andrettin](https://opengameart.org/users/andrettin) |
| rays_map.png | Tomasz Kot | N/A |
| right-entry-bottom.png | Kamil Klyta | N/A |
| right-entry-top.png | Kamil Klyta | N/A |
| right.png | Kamil Klyta | N/A |
| test.png | Bartłomiej Bukowiecki | N/A |
| top-left.png | Kamil Klyta | N/A |
| top-right.png | Kamil Klyta | N/A |
| top.png | Kamil Klyta | N/A |
| x-blue.png | Tomasz Kot | N/A |
| x-green.png | Tomasz Kot | N/A |
| x.png | Bartłomiej Wloczyk | N/A |
| zielone.png | Bartłomiej Bukowiecki | N/A |
| chest_1.png | Kamil Klyta | N/A |
| chest_2.png | Kamil Klyta | N/A |
| chest_3.png | Kamil Klyta | N/A |
| chest_4.png | Kamil Klyta | N/A |
| meat_with_label.png | Tomasz Kot | N/A |
| meat.png | Kamil Klyta | N/A |
| steak.png | Kamil Klyta | N/A |
| grounds_[1..24].png | Kamil Klyta | N/A |
| wood_*.png | Kamil Klyta | N/A |
| heart.png | Kamil Klyta | N/A |
| heart_shop_1.png | Tomasz Kot | N/A |
| heart_1.png | Kamil Klyta | N/A |
| key_1.png | Kamil Klyta | N/A |
| key_2.png | Kamil Klyta | N/A |
| key_3.png | Kamil Klyta | N/A |
| key_4.png | Kamil Klyta | N/A |
| key_1_label.png | Tomasz Kot | N/A |
| coal.png | Kamil Klyta | N/A |
| gold_1.png | Kamil Klyta | N/A |
| gold_2.png | Kamil Klyta | N/A |
| gold_3.png | Kamil Klyta | N/A |
| silver_1.png | Kamil Klyta | N/A |
| silver_2.png | Kamil Klyta | N/A |
| silver_3.png | Kamil Klyta | N/A |
| atack-booster.png | Kamil Klyta | N/A |
| chest-drop-booster.png | Kamil Klyta | N/A |
| hunger-booster.png | Kamil Klyta | N/A |
| hunger-immunite-booster.png | Kamil Klyta | N/A |
| libe-booster.png | Kamil Klyta | N/A |
| movement-booster.png | Kamil Klyta | N/A |
| pickup-double-booster.png | Kamil Klyta | N/A |
| temporary_spike_1.png | Bartłomiej Wloczyk | N/A |
| temporary_spike_2.png | [opengameart](https://opengameart.org/content/bevouliin-free-game-obstacle-spikes) | CC0 |
| temporary_spike_3.png | [opengameart](https://opengameart.org/content/bevouliin-free-game-obstacle-spikes) | CC0 |
| temporary_spike_4.png | [opengameart](https://opengameart.org/content/bevouliin-free-game-obstacle-spikes) | CC0 |
| temporary_spike_5.png | [opengameart](https://opengameart.org/content/bevouliin-free-game-obstacle-spikes) | CC0 |
| bricks-bottom.png | Kamil Klyta | N/A |
| bricks-ledder.png | Kamil Klyta | N/A |
| bricks-left.png | Kamil Klyta | N/A |
| bricks-left-bottom.png | Kamil Klyta | N/A |
| bricks-left.png | Kamil Klyta | N/A |
| bricks-left-transparent.png | Kamil Klyta | N/A |
| bricks-right.png | Kamil Klyta | N/A |
| bricks-right-bottom.png | Kamil Klyta | N/A |
| bricks-right.png | Kamil Klyta | N/A |
| bricks-top.png | Kamil Klyta | N/A |
| 48x48Worm_FullSheet.png | 8bit games assets from Humble Bumble | N/A |
| ghost.png | 8bit games assets from Humble Bumble | N/A |
| rat.png | 8bit games assets from Humble Bumble | N/A |
| worm_obrocony.png | 8bit games assets from Humble Bumble | N/A |
| minotaur_obrocony.png | 8bit games assets from Humble Bumble | N/A |

### Spis użytych ścieżek dzwiękowych:
| Nazwa pliku w folderze Content  | Autor/Źródło | Licencja |
| ------------- | ------------- | ------------- |
| background_game.mp3 | [opengameart](https://opengameart.org/content/enchanted-tiki-86) | CC0 |
| chest_opening.wav | [opengameart](https://opengameart.org/content/open-chest) | CC3 [spookymodem](https://opengameart.org/users/spookymodem) |
| eating_sound.mp3 | [FreeSound](https://freesound.org/people/Ondruska/sounds/360686/) | CC0 |
| item_picking.mp3 | [FreeSound](https://freesound.org/people/niamhd00145229/sounds/422709/) | CC0 |
| damage_sound.mp3 | [FreeSound](https://freesound.org/people/Raclure/sounds/458867/) | CC0 |
| menu_theme.mp3 | [opengameart](https://opengameart.org/content/cave-theme) | CC0 |
| mouse_click.wav | [FreeSound](https://freesound.org/people/Agaxly/sounds/213004/) | CC0 |
