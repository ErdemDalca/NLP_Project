**Game Design Document (GDD) - "Labyrinth of Echoes"**

---

**1. Visão Geral**

**Título:** Labyrinth of Echoes\
**Gênero:** Roguelike de visão aérea (top-down)\
**Plataforma:** PC, Web, Mobile\
**Público-alvo:** Jogadores casuais e entusiastas de roguelikes que buscam uma experiência viciante, de curta duração por sessão, com progressão satisfatória.

**Resumo:**
"Labyrinth of Echoes" é um roguelike minimalista em que o jogador assume o papel de uma alma presa em um labirinto gerado proceduralmente, com outras almas. O objetivo é escapar do labirinto enquanto coleta "Fragmentos de Eco" para desbloquear poderes e desvendar segredos sobre sua origem. O jogo foca em movimentação estratégica, habilidades simples e uma progressão recompensadora.

---

**2. Gameplay**

**Loop Principal:**

1. **Explorar:** Navegue pelo labirinto em busca de saídas e Fragmentos de Eco.
2. **Combater:** Derrote inimigos que patrulham o labirinto.
3. **Coletar:** Pegue Fragmentos de Eco para desbloquear habilidades ou aprimorar atributos.
4. **Avançar:** Complete um nível do labirinto e avance para um mais difícil.

**Mecânicas Chave:**

- **Movimentação:** Controle simples com WASD ou toques (mobile).
- **Ataque:** Clique/pressione para atirar um projétil de energia (sem animação complexa, apenas uma partícula).
- **Habilidades:** Ative poderes com cooldown (por exemplo, teletransporte, escudo temporário, explosão em área).
- **Progressão:** Acumule Fragmentos de Eco para upgrades permanentes.
- **Perma-Death:** A morte reinicia o jogo, mas os upgrades desbloqueados permanecem.

**Estilo de Progressão:**

- Fragmentos de Eco são usados para desbloquear habilidades no menu principal (meta-progression).
- Cada "run" oferece upgrades temporários aleatórios que variam o estilo de jogo.
- Labirintos mais avançados apresentam novos inimigos e desafios ambientais (como áreas que reduzem sua visão ou armadilhas).

**Árvore de Habilidades e Classes:**

- O jogador pode evoluir por meio de uma árvore de habilidades com três caminhos principais: **Purificação**, **Destruição** e **Conjuração**.
- Cada caminho representa um estilo único de jogo:
  - **Purificação:** Técnicas pacifistas que libertam as almas(curam o usuário), mas dropam menos Fragmentos de Eco. Favorece aumento de **Vida**.
  - **Destruição:** Técnicas poderosas e explosivas que infligem alto dano. Favorece aumento de **Poder**.
  - **Conjuração:** Técnicas baseadas em controle, como paralisação e conjurações. Favorece aumento de **Controle de Ecos**.
- O jogador pode combinar dois caminhos (primário e secundário), criando combinações como:
  - **Purificador Destruidor:** Vida alta com habilidades explosivas.
  - **Destruidor Conjurador:** Poder elevado e controle estratégico.
  - **Conjurador Purificador:** Foco em controle e resistência.

**Checkpoints na Árvore:**
A cada estágio da árvore, certos poderes tornam-se permanentes, não sendo reinicializados mesmo após a morte, garantindo uma sensação de progressão contínua.

---

**3. Arte e Estética**

**Estilo Visual:**

- **Minimalista:** Texturas simples, com paleta de cores reduzida (por exemplo, preto, branco e uma cor destacada para os Fragmentos de Eco).
- **Vista Aérea:** Personagens e inimigos vistos de cima, sem necessidade de sprites laterais ou frontais.
- **Animações:** Apenas movimentos de translado, pequenas rotações para projéteis e efeitos de partículas para ataques.

**Ferramentas de IA:**

- Use geradores de pixel art ou ilustrações simplificadas para criar tilesets do labirinto (paredes, pisos, armadilhas).
- Inimigos podem ser representados por formas geométricas abstratas (ex.: círculos, triângulos) com cores diferentes para indicar tipos.

---

**4. Design de Níveis**

**Labirintos Procedurais:**

- Gerados automaticamente a cada sessão, com caminhos, salas escondidas e segredos.
- **Objetos Gerados:** Fragmentos de Eco, armadilhas, inimigos, altares de poder (permitem upgrades temporários).
- **Escala de Dificuldade:**
  - Níveis iniciais: caminhos mais simples, poucos inimigos.
  - Níveis avançados: mais bifurcações, inimigos rápidos ou com habilidades especiais, armadilhas frequentes.

---

**5. Inimigos**

**Tipos de Inimigos:**

1. **Aventureiros Perdidos:** Humanos que tentaram explorar o labirinto e se perderam. Fracos, mas em grupo podem ser perigosos.
   - **Ataques:** Golpes rápidos com armas simples.
   - **Design:** Figuras humanoides com roupas esfarrapadas, olhos brilhando em azul pálido.

2. **Ecos Sedentos:** Seres que consumiram muitos Fragmentos e se corromperam.
   - **Ataques:** Investidas rápidas e explosões ao morrer.
   - **Design:** Formas amorfas, como sombras com olhos vermelhos pulsantes.

3. **Conjuradores Sombrios:** Outros jogadores que dominaram técnicas de conjuração.
   - **Ataques:** Lançam magias de paralisação e invocam aliados temporários.
   - **Design:** Figuras encapuzadas com fragmentos flutuando ao redor.

4. **Purificadores Eternos:** Almas que se dedicaram à purificação.
   - **Ataques:** Nenhum (não atacam jogadores purificadores).
   - **Design:** Figuras etéreas, envoltas em luz dourada.

5. **Guardião dos Ecos:** Mini-boss que aparece em níveis avançados.
   - **Ataques:** Poderosos ataques em área e invocação de "Ecos Sedentos".
   - **Design:** Figura imponente, parcialmente mecânica, com fragmentos de eco incrustados no corpo.

**Desafios Ambientais:**

- **Áreas Escuras:** Limita a visão do jogador.
- **Campos de Corrupção:** Drenam vida lentamente ao atravessar.
- **Armadilhas Ativadas por Peso:** Disparam projéteis ao serem pisadas.

---

**6. Audio Design**

Em breve.

---

**7. Monetização (Opcional)**

**Versão Mobile:**

- Versão gratuita com anúncios entre as runs (removíveis por uma pequena taxa).
- Compra de Fragmentos de Eco para acelerar a progressão (sem pay-to-win).

---

**8. Lore**

No centro do multiverso existe um lugar chamado Labirinto de Ecos, uma dimensão onde memórias esquecidas e almas perdidas são aprisionadas. Você é uma dessas almas, um fragmento de algo maior, condenado a vagar por corredores sem fim. A cada passo, o Labirinto sussurra fragmentos de sua própria história: um ser todo-poderoso, conhecido como o Guardião dos Ecos, manipula o labirinto para testar aqueles que entram. Dizem que quem conseguir escapar se tornará mais do que uma alma perdida — ganhará a capacidade de moldar a realidade.

**Fragmentos de Eco:**
Os Fragmentos de Eco são resíduos de memórias e poder armazenados no labirinto. Coletá-los permite que você acesse habilidades antigas esquecidas ou desbloqueie novos talentos. Cada fragmento é uma parte da história do Guardião, revelando sua própria corrupção e o motivo por trás do labirinto.


**Finalidade do Labirinto:**
Os sussurros dizem que o Guardião busca um sucessor digno. No entanto, sua verdadeira intenção é se libertar de sua própria prisão. Cada jogador é mais uma tentativa do labirinto de criar o guerreiro perfeito para essa tarefa.

---

**10. Conclusão**

"Labyrinth of Echoes" é projetado para ser um jogo viciante, acessível e de baixa complexidade no desenvolvimento, focando em uma progressão satisfatória e gameplay que premia a habilidade do jogador. Com mecânicas simples e arte minimalista, ele é ideal para um projeto independente que

