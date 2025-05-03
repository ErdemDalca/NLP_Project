## Game Design Document: "Beggars and Bakers"

### Estória

O jogador assume o papel de um cavaleiro leal que recebe uma missão aparentemente simples: buscar o café da manhã para o rei na padaria favorita do monarca. No entanto, o caminho até lá está repleto de perigos e personagens peculiares que querem tirar seu dinheiro de todas as formas possíveis. Desde mendigos espertalhões até vendedores insistentes e bruxas maliciosas, o cavaleiro precisará usar sua astúcia e habilidades para manter suas moedas seguras e completar sua missão com sucesso.

O rei é exigente: ele só aceita os itens específicos de uma padaria distante, e a satisfação dele depende da quantidade e qualidade dos itens entregues. Se o cavaleiro falhar, o cavaleiro pode morrer.

---

### Estrutura do Jogo

- **Gênero:** Plataforma 2D de ação/aventura com elementos de estratégia e humor.
- **Objetivo:** Levar uma quantidade X de itens da padaria para o rei, gerenciando o dinheiro e evitando perder todas as moedas no caminho.
- **Progressão:** O jogo é dividido em fases, cada uma com um caminho mais longo e desafiador até a padaria.
- **Fim do Jogo:** O jogador perde se ficar sem dinheiro. O jogo termina com sucesso ao entregar os itens ao rei, com diferentes finais baseados na satisfação do monarca.

---

### Mecânicas do Jogo

#### Mecânicas do Jogador
- **Movimentação:** O cavaleiro pode se mover livremente pelo mapa, evitando inimigos e coletando moedas.
- **Combate:** O jogador pode atacar inimigos para derrotá-los e ganhar moedas.
- **Interação com NPCs:**
  - **Mendigos:** Se o cavaleiro encostar neles, perde moedas (esmola ou roubo).
  - **Vendedores:** Quando próximos, o cavaleiro compra automaticamente itens (úteis ou inúteis). Uma música paraguaia toca quando um vendedor está por perto.
  - **Bruxa:** Transforma moedas em itens inúteis se o cavaleiro encostar nela.
- **Coleta de Moedas:** Moedas são obtidas derrotando inimigos ou coletando-as no mapa.
- **Gerenciamento de Dinheiro:** O jogador deve equilibrar gastos e ganhos para garantir que tenha dinheiro suficiente para comprar os itens necessários na padaria.

#### Itens e Compras
- **Padaria:** No final de cada fase, o jogador pode comprar itens específicos para o rei. Os itens variam em preço e qualidade.
- **Itens Especiais:** Alguns vendedores oferecem itens úteis, como poções de velocidade ou escudos temporários, mas podem ser caros.

---

### Inimigos e NPCs

#### Mendigos

- **Comportamento:** Andam lentamente pelo mapa.
- **Mecânica:** Se o cavaleiro encostar neles, perde moedas (esmola ou roubo).
- **Dica:** Evite contato ou use ataques para mantê-los longe.

#### Vendedores

- **Comportamento:** Andam pelo mapa e se aproximam do jogador, são rápidos.
- **Mecânica:** Quando próximos, o cavaleiro compra automaticamente o item que estão vendendo.
- **Características:** Falam em espanhol ou guarani. Uma música paraguaia toca quando estão por perto.

#### Bruxa

- **Comportamento:** Fica parada em áreas específicas do mapa.
- **Mecânica:** Transforma moedas do jogador em sapos se ele encostar nela ou se estiver em seu campo de visão e for atacado.
- **Dica:** Desvie ou ataque-a rapidamente.

#### Outros Possíveis Inimigos

- **Padeiros:** Atacam o cavaleiro com pães duros.
- **Donos de Tavernas:** Tentam empurrar bebidas caras.
- **Vendedores de Poção:** Oferecem poções úteis, mas a preços altos.

---

### Progressão de Dificuldade

- A cada fase, o número de inimigos e a quantidade de moedas que eles roubam aumentam.
- Novos tipos de inimigos são introduzidos, como vendedores mais agressivos e bruxas mais rápidas.
- O caminho até a padaria fica mais longo e cheio de obstáculos.

---

### Sistema de Satisfação do Rei

- O rei avalia a entrega com base na quantidade e qualidade dos itens:
  - **5 Estrelas:** Três itens de alta qualidade. O rei fica extremamente satisfeito.
  - **3 Estrelas:** Dois itens de qualidade média. O rei fica satisfeito, mas não impressionado.
  - **1 Estrela:** Um ou nenhum item entregue. O rei manda o cavaleiro para a guilhotina.

---

### Finais

O jogo tem múltiplos finais baseados na satisfação do rei:

1. **Final Perfeito (5 Estrelas):** O rei fica encantado com o café da manhã e recompensa o cavaleiro com honras e riquezas.
2. **Final Regular (3 Estrelas):** O rei aceita o café da manhã, mas o cavaleiro não recebe recompensas extras.
3. **Final Ruim (1 Estrela):** O rei manda o cavaleiro para a guilhotina.

---

### Gráficos e Estilo Visual

- **Estilo:** Pixel art.
- **Cenários:** Ambientes medievais com toques humorísticos, por exemplo: padarias com placas de "Melhor Padaria do Reino".
- **Animação:** Movimentos fluidos e efeitos cômicos.

---

### Trilha Sonora e Efeitos Sonoros

- **Trilha Principal:** Música medieval com toques humorísticos.
- **Efeitos Sonoros:**
  - Moedas tilintando ao serem coletadas.
  - Risadas de mendigos ao roubarem moedas.
  - Música paraguaia tocando quando vendedores estão por perto.
  - Som de sapos crocitando quando a bruxa age.

---

### Menu e Opções

- **Iniciar Jogo**
- **Configurações:** Ajustar volume de som e gráficos.
- **Tutorial:** Explicação das mecânicas básicas.
- **Ranking:** Ver pontuações mais altas (baseadas na quantidade de moedas restantes ao final do jogo).
- **Sair**
