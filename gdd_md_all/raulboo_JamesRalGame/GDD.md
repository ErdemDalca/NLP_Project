---
Title: 
Creator:
---

# [Working Title]

- [\[Working Title\]](#working-title)
- [0. Ideias](#0-ideias)
- [1. Dev Roadmap - 3 meses](#1-dev-roadmap---3-meses)
- [2. Theme and Concept](#2-theme-and-concept)
- [3. Story, Setting and Locations](#3-story-setting-and-locations)
- [4. Gameplay](#4-gameplay)
    - [a. Verbos Padrão (de todos os personagens)](#a-verbos-padrão-de-todos-os-personagens)
    - [b. Efeitos Padrão](#b-efeitos-padrão)
    - [c. Cartas Modificadoras](#c-cartas-modificadoras)
    - [d. Powerups](#d-powerups)
- [5. Characters](#5-characters)
- [6. Level Design](#6-level-design)
- [7. Menu Design](#7-menu-design)
- [8. Assets Needed](#8-assets-needed)
    - [a. Animated Sprites](#a-animated-sprites)
    - [b. Graphical Effects](#b-graphical-effects)
    - [c. Props](#c-props)
    - [d. Tilesets](#d-tilesets)
    - [e. Sound Effects](#e-sound-effects)
    - [f. Music](#f-music)
    - [g. UI Assets](#g-ui-assets)
    - [h. Text/Dialogue](#h-textdialogue)
- [9. Game Walkthrough / Full Script](#9-game-walkthrough--full-script)


# 0. Ideias

a gente poderia começar algum projeto juntos eu tava querendo ajudar na programação tb. daria pra assim se quiser ambos ajudar em programar e pixelart assim nos ganhariamos experiencia ajudando um ao outro no que cada um ja tem mais experiencia tb
nao tenho ainda nenhuma ideia especifica poderia ser algo pequeno de treino
eu tava hj e ontem olhando sobre como desenhar tiles isometricos mas nao precisava ter haver com isso so tava olhando curioso pq acho legal jogos com essa aparencia tb XD
mas poderia ser algo mais convensional de tiles quadrados ou outra coisa. a gente poderia escolher um tipo de joguinho pra o projeto

Nao sei se isso é mt complexo mas vc sabe se é facil fazer suporte pra sockets e netplay no love?
Mas a ideia era fazer um jogo tipo animal crossing, que vc constroi seu mundo, e as outras pessoas podem visitar

Mas a gente podia fazer um jogo multiplayer :3
Tipo aqueles joguinhos que da pra jogar com amigo e ficar horas ajhsjahdjs
Tipo smash bros e mario kart
Pensei em multiplayer local

E dava pra fazer um jogo de luta tipo smash, vc gosta?
Ou um jogo de corrida, ate um jogo de corrida de avioes

bom ate o moment temos idea de:
- coisas isometrica
- multiplayer local
- jogo de luta
- corrida de avioes

Tive algumas outras ideias, ve se vc gosta delas:
talvez aproveitar a flexibilidade do love e experimentar uma pixelart em uma resoluçao maior. Tipo estilo Changed, que fica menos vibes snes e mais vibes "Flash"
jogo de 2 players com uma competição de mini games bem rapidos, um atras do outro (tipo cooking mama, run or die, etc.)
tema steampunk
tema com arvores, tipo os personagens tem poderes de planta, conseguem modificar a fase fazendo crescer troncos e galhos, criando plataformas etc.

Inclusive podia ser um jogo de luta com um estágio dinamico, que vai mudando com os movimentos dos jogadores e com o tempo; dai reduzia a complexidade de criar outros modos de jogo, da ideia dos minigames
E no caso, o mvp seria mais simples: um jogo de luta normal kkkk

bom a ideia de jogo de luta parece legal coisinhas inspiradas pelo classico kung fu ou o mais reference roof rage XD

so o problema que vejo que as fases são faceis pq são miudas quase uma tela ou duas as maiores umas 3 ou 4 so mas animar povo vai ser sofrido XD
a nao ser que as animações sejam bem simples como o primeiro de cima XD
tb se tiver plataformas como segundo exemplo o AI pode ser dificil se resolver ter um AI singleplayer =x
mas AI do primeiro parece super facil ja q ele nao tem que navegar por um mapa é um terreno flat
bom essa uma das possibilidades
outra que pensei poderia ser se aquela ideia do tank que uma vez eu tava fazendo no godot poderia ser refeita mais como se fosse um bullet heaven (tipo vampiro survival e outros asism) que q um tank que ia recebendo upgrades e tb poderia se tornar multiplayer facil
a minha versao o tana era um pouco mais realista o momevimeno com curvas e aceleração 

se um dia eu refizesse ele tava pensando em talvez fazer mais arcade com movimento de oito direções mais rigido pq fica mais facil configurr inimigos e outras coisas e so a torre de tiro atirar mais livre

Gostei dessa ideia, tipo fazer um jogo competitivo em que tem 1 milhao de balas atirando um contra o outro ia ser legal ajshajsbhwjnsjs
E podia ter avioes :3

Acho que jogo de luta tava pensando mais em smash, que vc tenta derrubar seu oponente do estagio :p

Queria um que desse pro player modular ate ficar ridiculo, tipo quando eu jogo smash eu queria muito que tivesse uma opção que aumentasse o knockback do soco a ponto de ser one-punch-man ahdhahjdhejd

Tipo no smash, tem um monte de powerups
Pode ter personagens diferentes dai, alguns podem atirar bullet patterns diferentes tbm em momentos diferentes
Bora fazer furries ne? owo

bem como disse se parecer muito trabalho tem a ideia do tank/ou aviao etc naquele estilo mais bullet heaven que são mais faceis de programar XD

Temas: steampunk, avioes, plantas, árvores,


# 1. Dev Roadmap - 3 meses

- 1º mês ALPHA = Lógica geral, movimento em 2d, multiplayer local, placeholder tiles e sprites, poderes e habilidades principais implementadas, 2 jogadores, efeitos sonoros placeholder 
  - [x] Implementação dos verbos básicos
  - [ ] Socos, Camera centrada, Morte e Respawn, Modificadores de Gameplay (mvp)
  - [ ] Demais verbos básicos 

- 2º mês BETA = Gameplay com rounds completos, mecanicas de cartas completas, 3 personagens jogáveis, 1 arena jogável, MVP, já é jogável e divertido, ciclos de animação completos para os 3 personagens, efeitos sonoros plenos, powerups
- 3º mês RELEASE = Menus funcionais, música de fundo, polish, bug fixes, balanceamento, margem de erro pra completar o que falta

# 2. Theme and Concept

Conceito: Um jogo de luta, multiplayer local de 2-4 jogadores, inspirado em Smash, cujo objetivo é derrubar o adversário para fora do estágio. Ao fazê-lo, o derrubador pode modificar uma regra do jogo, igual para todos.

Tema: Steampunk

Estilo de Arte: SNES, resolução ~480x270, furry owo

# 3. Story, Setting and Locations

# 4. Gameplay

### a. Verbos Padrão (de todos os personagens)
- Correr         (→)             - walk, walk.accel, walk.max_speed
- Dash           (←→)            - walk, walk.is_dashing, walk.dash_accel, walk.dash_max
- Pulo           (↑ >5 frames)   - jump, grounded, jump.coyote_time_left, jump.frames, jump.speed
- Hop            (↑ <5 frames)   - jump, grounded, jump.coyote_time_left, jump.frames, jump.hop_speed
- Pulo duplo     (↑↑)            - jump, jump.doubles_left
- Fast fall      (↓↑)            - fastfall, fastfall.speed
- Golpe normal   (Z) 
- Golpe especial (X)

### b. Efeitos Padrão
- Gravity 
- Falling speed   (max +vely) - move.max has to change if we're gonna implement fast fall
- Ground friction
- Air friction
- Knockback
- Hitstun


### c. Cartas Modificadoras
Ideias para cartas modificadores de gameplay:
- Todos os jogadores trocam de personagem
- Controles invertidos
- Pulo absurdo
- Golpe especial += bumerangue
- Golpe especial += rajadas de balas (ou outros padrões de balas)
- Todos podem voar
- Todos ficam gigantes (3x tamanho)
- O chão é lava (ficar no chão causa dano)
- Fase no escuro (apenas players e entities emitem uma luz de curto alcance)

### d. Powerups 

# 5. Characters

# 6. Level Design

# 7. Menu Design

# 8. Assets Needed

### a. Animated Sprites
### b. Graphical Effects
### c. Props
### d. Tilesets
### e. Sound Effects
### f. Music
### g. UI Assets
### h. Text/Dialogue

# 9. Game Walkthrough / Full Script