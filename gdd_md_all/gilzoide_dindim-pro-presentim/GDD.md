# (nome a definir)
**Conceito**: Você anda e pula pelas páginas de um gibi para pegar as moedas e conseguir comprar um presente maneiro para o amigo oculto de natal.

**Referências**:
- [Jetpack](https://www.dosgames.com/game/jetpack): pegar as moedas para passar da fase, comportamentos de inimigos
- [Comix zone](https://en.wikipedia.org/wiki/Comix_Zone): jogo se passa num gibi
- Zeldas 2D com item de pulo (Oracles, Minish Cap): gameplay topdown com pulo

**Gênero**: Aventura

**Plataforma**: PC/Linux/OSX/Web


## Game Flow
- Menu com logo e botões iniciar, créditos
- Iniciar:
  - Entrar na historinha
  - Apertar o botão de ação para começar o jogo
  - Andar pelo mapa, pular entre os quadrinhos, desviar de obstáculos, pegar as moedas
  - Ir até o final da página para passar para a próxima
  - (?) Após a última fase, loja de presentes para escolher o que comprar
  - Placar da run, com tempo gasto, moedas conseguidas (?) e presente escolhido
  - Clica no botão de Menu para voltar ao menu principal
- Créditos:
  - Abre um popup (ou janela fullscreen que volta) com os créditos de assets usados
  - Clica no botão de voltar para voltar ao menu principal


## Estilo estético
- Estilo cartoon nas ilustras 2D, com balões ou caixas de diálogo
- Toon shading nos objetos 3D
- Filtros de quadrinhos antigos (aquelas bolinhas, não sei o nome)
- Fonte de gibi
- Cores saturadas
- Música felizinha de aventura


## Personagens
- Jogador:
  - Uma cabeça com googly eyes em 3D presa a uma mola
  - Animação simples: olhos animam com física, mola anima com escala
- Inimigos:
  - **TODO**


## Narrativa
- É véspera de natal e você ainda não comprou seu presente de amigo oculto
- Você vai em busca de moedas para comprar o presente
- Após sua aventura, você cola na loja para comprar um presente maneiro e volta feliz para casa
- Narrativa é contada em quadrinhos estáticos


## Mecânicas
- Direcional faz a personagem se movimentar
- Botão de ação faz a personagem pular
- Personagem tromba nas paredes do quadro em que está
- Personagem pode pular para um novo quadro. Cair na parede faz a personagem cair em algum dos quadros adjacentes
- Encostar em moedas as coleta
- Encostar em obstáculos inimigos faz personagem recomeçar na borda do quadro atual, (?) perdendo uma vida
- Para sair da borda, apertar o botão de ação e pular para onde quiser
- Inimigo que anda em percurso fixo
- Inimigo que anda random
- Inimigo que te segue se no mesmo quadro e anda random se não


## Controles
- WASD/←↓↑→/joystick esquerdo/gamepad D-pad para direcionais
- Espaço/Return/Qualquer botão do mouse ou gamepad para ação e pulo
- Nos menus, tap com mouse ou navegação de botões pelo direcional e botão submit padrão


## UI
- Geral
  - Fonte com cara de gibi
- Menu principal
  - Título, botões Iniciar e Créditos
- Créditos
  - Nome dos assets e link clicável para a página
  - Lista de assets em scroll, se necessário
- Gameplay
  - Timer com tempo gasto até agora (para speed run) no topo da tela ou canto superior esquerdo
  - Pontuação de moedas em um dos cantos superiores
  - (?) Vida restante em um dos cantos superiores
  - (?) Indicação de onde está a saída


## Artes

## Animações

## SFX

## Músicas
