**Game Design Document (GDD)**

**Título:** AION

**Gênero:** Aventura narrativa interativa, drama urbano

**Plataforma:** Web (Typescript + Three.js)

**Perspectiva:** 2D (com elementos 2.5D ou de profundidade para atmosferas)

---

### 1. Visão Geral

**Resumo:**
"AION" é um jogo narrativo sobre escolhas, percepção e arte. O jogador começa como João, um trabalhador urbano, preso na rotina. Ao acessar uma rede social, ele encontra Nyx, um(a) artista misterioso(a) que o convida a visitar uma exposição em uma galeria alternativa chamada Lux. A partir dessa decisão, o jogador mergulha em uma experiência sensorial, alternando entre os mundos de João e Nyx.

**Estilo visual:** Minimalista, com foco em atmosfera, sombra, chuva, paleta fria (tons de azul, cinza, lilás). Estética de cadernos, redes sociais alternativas e galeria de arte.

**Inspirações:** Disco Elysium, Kentucky Route Zero, Night in the Woods.

---

### 2. Mecânicas

**Exploração:**
- Cenas estáticas com transições animadas.
- Jogador clica/interage com elementos do cenário (ex: objetos, pessoas, celulares).

**Escolhas:**
- Diálogos com opções.
- Decisões bifurcadas que influenciam o rumo da narrativa.

**Rede Social (AION):**
- Interface diegética (como se o jogador estivesse vendo a tela do celular).
- Postagens, curtidas, comentários (alguns simulados).
- Jogador escolhe legenda de fotos.

**Transição de Personagem:**
- De João para Nyx (com efeito visual e sonoro sutil).

**Narrativa Visual:**
- Câmeras fixas com efeitos de profundidade.
- Texto escrito à mão e elementos desenhados para parecerem notas pessoais.

---

### 3. Estrutura

**Ato 1:** Rotina de João
- Cidade chuvosa
- Jazz no fone
- Caminho do trabalho
- Acesso à AION e descoberta de Nyx

**Decisão:** seguir Nyx ou ignorar

**Ato 2:** A exposição na galeria Lux
- Jogador é Nyx
- Exploração das obras
- Escolha de legenda
- Repercussão na rede

**Ato 3:** Comentários, reflexão, novo ciclo
- Introdução de Kairos e outros personagens
- Possível nova decisão: quem assumir a seguir

---

### 4. Interface

**Geral:**
- Mouse: point-and-click
- UI minimalista
- Tipografia manuscrita para falas internas e legendas
- Layout de rede social estilizado como um feed

**Cenas:**
- Chuva animada em camadas
- Sons diegéticos (passos, chuva, música ambiente)

---

### 5. Estilo Sonoro

- Jazz, ambient, lo-fi
- Sons urbanos (chave do apartamento, buzina ao fundo, chuva constante)
- Mudanças de som conforme mudança de personagem (João = mais realista, Nyx = mais etéreo)

---

### 6. Tecnologias

- **Frontend:** Typescript, Three.js (usado para criar efeitos de câmera, profundidade e chuva)
- **Assets:** SVGs e PNGs 2D desenhados à mão ou vetoriais
- **Audio:** Web Audio API para controle dinâmico de sons

---

### 7. Roadmap

1. Protótipo com cena inicial (João + chuva + feed da AION)
2. Implementação de decisões e transição para Nyx
3. Exposição interativa + postagem
4. Final com escolha do próximo personagem ou fechamento

---

### 8. Considerações Finais

- O jogo deve manter uma atmosfera contemplativa.
- A narrativa é o centro; não há combate nem puzzles complexos.
- Ideal para jogadores que gostam de experiências poéticas e subjetivas.

---

