# StackOverflow GDD
## Název hry
Stack Overflow
## Autoři hry
Anna Skorobogatova, Aleš Calábek, Ondřej Lomič
## Popis cílové skupiny
Hru může hrát kdokoliv se znalostí základů programování a syntaxe jazyka Python.
## Chtěný herní zážitek
Vycházíme z předpokladu, že hráče baví počítání - ať už z hlavy nebo na papíře.
Méně zkušení hráči si mohou osvěžit/naučit se některé prvky jazyka Python,
zkušenější hráči se mohou předhánět, kdo se nejrychleji dopočítá k výsledku,
a kdo si z hlavy poradí i s vysokými čísly.
## Počet hráčů
2+
## Délka herní instance
30 minut
## Herní pravidla

### Obsah:
1. Karty programů - karty obsahující jednoduché programy v jazyce Python; každý
program přijímá jednu vstupní hodnotu, kterou tranformuje na jednu hodnotu výstupní.
2. Karty hodnot - karty obsahující kladná i záporná, celá i desetinná čísla,
sloužící jako vstupní hodnoty pro programy a jako výstupní hodnota.

### Cíl hry:
Zbavit se všech karet.

### Příprava:
Zamíchejte karty programů a rozdejte každému hráči 4 karty.
Zamíchejte karty hodnot, jednu kartu vylosujte a umístěte ji na stůl tak, aby
na ní každý hráč viděl. Tato karta představuje výstupní hodnotu a bude stejná
po celou hru.
Balíčky programů a hodnot položte doprostřed stolu jako lízací balíčky.

### Herní kolo:
Na začátku každého herního kola je z balíčku hodnot vytažena jedna karta, která
slouží jako vstupní hodnota programů. Úkolem všech hráčů je vybrat z karet, které
mají v ruce, jeden či více programů tak, aby se výsledek jimi vybrané sekvence
programů co nejvíce blížil hodnotě na kartě s výstupní hodnotou. Vítězem kola
se stává hráč, jehož výsledek se nejvíce blíží výstupní hodnotě,
tedy že absolutní hodnota rozdílu jeho výsledku a výstupní hodnoty má nejmenší
hodnotu mezi všemi hráči. Všechny použité karty programů se odhodí. Až na vítěze
si všichni hráči si doberou z balíčku tolik karet, aby měli stejný počet karet
jako na začátku kola, vítěz si bere o jednu kartu méně. V případě remízy
(stejného rozdílu výsledku a výstupní hodnoty) je více vítězů kola a tito
si dobírají snížený počet karet. Na konec se odklidí karta se vstupní hodnotou
a hra pokračuje novým herním kolem.

### Řetězení programů:
K transformaci vstupní hodnoty na výstupní mohou hráči použít více než jeden
program. V takovém případě je výstupní hodnota prvního programu použita jako
vstupní hodnota druhého programu, výstupní hodnota druhého programu je použita
jako vstupní hodnota třetího programu a tak dále. Výsledkem pro dané herní kolo
je výstupní hodnota posledního programu z použité sekvence programů. Hráč musí
jasně stanovit pořadí použitých programů.

### Speciální efekty karet:
Pro některé vstupní hodnoty může v programu dojít k chybě:
1. Type Error - použití hodnoty nesprávného typu
    + efekt: hráč automaticky prohrává a na konci kola si bere o jednu kartu navíc
1. Recursion Error ala Stack Overflow - nekončící rekurzivní program
    + efekt: hráč automaticky prohrává a VŠICHNI hráči si na konci kola vezmou jednu kartu 
1. Value Error - použití hodnoty mimo očekávaný rozsah
    + efekt: hráč automaticky prohrává, nicméně před vyhodnocením ostatních hráčů se vylosuje
    nová VSTUPNÍ hodnota
    + jakékoli chyby způsobené nekonečnem či NaN (Not a Number, např. 0 * inf), se považují
    za Value Errors 
1. Zero Division Error - modulo nebo dělení nulou
    + efekt: hráč automaticky prohrává, nicméně před vyhodnocením ostatních hráčů se vylosuje
    nová VÝSTUPNÍ hodnota

### Konec hry:
Hra končí ve chvíli, kdy se jeden z hráčů zbaví všech karet a tento se stává
vítězem.

## Mechaniky
herní kola, hrací karty, lízání karet, držení karet v ruce, ztráta karet
při prohraném kole, speciální efekty (viz Herní pravidla), řetězení programů,
výběr programů na základě vstupní a výstupní hodnoty

## Smyčky
1. počítání výsledku pro danou vstupní hodnotu a sekvenci programů
2. jedno herní kolo - vylosuje se vstupní hodnota, každý hráč vybere sekvenci
programů, vyhodnocení
3. jedna celá hra - opakování herních kol zatímco mají alespoň dva hráči karty v ruce

## Identifikované problémy/neznámé návrhu hry
1. jak často bude docházet ke speciálním efektům a jejich balancování
2. jak přístupná je hra pro neprogramátory

## Co kdo dělal
+ Anna Skorobogatova: karty
+ Aleš Calábek: herní pravidla, GDD
+ Ondřej Lomič: Gitlab projekt, programy
