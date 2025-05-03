# Game Design Document: Constructor Defense

## 1. Conceito Central

### Visão Geral
Constructor Defense é um tower defense de perspectiva top-down onde o jogador controla um personagem construtor que deve posicionar defesas fisicamente no campo de batalha. Diferente dos tower defense tradicionais, onde o jogador coloca estruturas clicando em locais do mapa, neste jogo o construtor precisa estar presente para construir, criando uma dinâmica única de movimento estratégico e gerenciamento de tempo.

### Proposta Única
A principal inovação é a fusão entre tower defense e ação-movimento. O jogador constantemente toma decisões sobre:
- Onde estar fisicamente no mapa
- O que construir em cada momento
- Para onde se mover em seguida
- Quando reparar estruturas existentes vs. construir novas

## 2. Especificações Visuais

### Estilo Artístico
- **Perspectiva**: Top-down 2D com elementos isométricos sutis (15° de inclinação)
- **Arte**: Estilo cartoon com contornos definidos e cores vibrantes
- **Dimensões Base**: Grid de 64x64 pixels por célula
- **Animações**: Fluidas, com 8 frames para movimentos básicos
- **Paleta**: Cores contrastantes para facilitar identificação:
  - Construtor: Azul e verde
  - Estruturas: Variações de cinza, azul e amarelo
  - Inimigos: Tons de vermelho e roxo
  - Recursos: Cristais brilhantes em amarelo/dourado
  - Terreno base: Tons neutros terrosos

### Renderização Técnica
- Sistema de camadas:
  1. **Camada de fundo**: Terreno e decoração (estático)
  2. **Camada de estruturas**: Muros, torres, armadilhas
  3. **Camada de entidades**: Personagem e inimigos
  4. **Camada de efeitos**: Partículas, projéteis, UI
- Todas as animações são baseadas em sprites
- Sistema de iluminação simples: luz global + halos de luz local para estruturas

## 3. Física e Regras de Movimento

### Sistema de Movimentação do Construtor
- **Velocidade base**: 5 unidades/segundo
- **Aceleração**: 0-100% em 0.2 segundos
- **Desaceleração**: 100%-0 em 0.1 segundos
- **Colisão**: Círculo com raio de 20px
- **Movimento**: 8 direções (WASD/setas)

### Habilidade Dash
- **Distância**: 3 células (192px)
- **Velocidade**: 15 unidades/segundo
- **Duração**: 0.2 segundos
- **Cooldown**: 3 segundos
- **Invulnerabilidade**: Durante o dash (0.2s)
- **Efeito visual**: Rastro de partículas azuis

### Detecção de Colisão
- Sistema baseado em círculos para entidades
- Sistema baseado em caixas para estruturas
- Grid de navegação para pathfinding de inimigos
- Implementação técnica:
  ```
  function checkCollision(entity1, entity2) {
    return distance(entity1.position, entity2.position) < 
           (entity1.radius + entity2.radius);
  }
  ```

## 4. Sistema de Construção

### Mecânica de Construção
- O construtor deve estar fisicamente em uma célula para construir nela
- Grid virtual de 64x64 pixels por célula
- Todas as construções ocupam exatamente uma célula
- Sistemas de cooldown por tipo de construção
- Feedback visual: célula atual destacada (verde se disponível, vermelha se ocupada)

### Tipos de Estruturas

#### 1. Muros Defensivos
- **Função**: Bloquear caminho de inimigos
- **HP**: 80 (nível 1), aumenta +100% por nível
- **Custo**: 30 recursos
- **Cooldown**: 1 segundo
- **Resistência**: Alta a dano físico, baixa a explosivos
- **Visual**: Estrutura sólida que se deteriora com o dano
- **Upgrades**:
  - Nível 2: +100% HP, aspecto reforçado, custo 100
  - Nível 3: +100% HP, espinhos (dano passivo), custo 200

#### 2. Torres de Ataque
- **Função**: Atacar inimigos à distância
- **HP**: 50 (nível 1), aumenta +50% por nível
- **Custo**: 75 recursos
- **Cooldown**: 3 segundos
- **Ataque base**:
  - Dano: 3 pontos
  - Alcance: 3 células (192px)
  - Cadência: 1.5 por segundo
  - Projétil: Velocidade 10 células/segundo
- **Visual**: Base com canhão giratório que aponta para o alvo
- **Upgrades**:
  - Nível 2: +25% alcance, +66% dano, +33% cadência
  - Nível 3: +25% alcance, +33% dano, +25% cadência, projétil perfurante

#### 3. Armadilhas
- **Função**: Dano em área, uso único
- **HP**: 40
- **Custo**: 50 recursos
- **Cooldown**: 2 segundos
- **Efeito base**:
  - Dano: 10 instantâneo
  - Raio: 0.7 células
  - Ativação: Quando inimigo passa por cima
- **Visual**: Semi-oculto no chão com brilho sutil
- **Upgrades**:
  - Nível 2: +50% dano, efeito slow 30% por 3s
  - Nível 3: +33% dano, efeito slow 50% por 3s, efeito burn 5 dano/s por 3s

#### 4. Ferramenta de Reparo
- **Função**: Restaurar HP de estruturas
- **Custo por uso**: 15 recursos
- **Cooldown**: 0.5 segundos
- **Efeito**: +20 HP na estrutura
- **Visual**: Marteladas com partículas de luz
- **Limitações**: Só funciona em estruturas danificadas

### Sistema de Upgrades
- **Tempo de upgrade**: 3 segundos de construção
- **Custo**: Nível 2 (100), Nível 3 (200)
- **Mecânica**: Construtor deve selecionar estrutura e iniciar upgrade
- **Visual**: Barra de progresso e partículas durante upgrade
- **Implementação técnica**:
  ```
  function upgradeStructure(structure) {
    if (structure.level < 3 && resources >= UPGRADE_COSTS[structure.level + 1]) {
      structure.isUpgrading = true;
      structure.upgradeProgress = 0;
      decreaseResources(UPGRADE_COSTS[structure.level + 1]);
      
      // Concluído quando upgradeProgress >= UPGRADE_TIME (3s)
    }
  }
  ```

## 5. Entidades Inimigas

### IA e Comportamento
- **Pathfinding**: Algoritmo A* simplificado
- **Atualização de rota**: A cada 0.5 segundos
- **Comportamentos base**:
  1. **Direto**: Linha mais curta até o objetivo
  2. **Inteligente**: Evita muros contornando-os
  3. **Enxame**: Agrupa-se com outros inimigos

### Tipos de Inimigos

#### 1. Inimigos Básicos
- **Velocidade**: 2 células/segundo
- **HP**: 15-25
- **Dano**: 5/segundo contra estruturas, 10 contra casa
- **Comportamento**: Segue rota direta
- **Valor**: 20 recursos ao morrer

#### 2. Inimigos Velozes
- **Velocidade**: 3 células/segundo
- **HP**: 10-15
- **Dano**: 3/segundo
- **Comportamento**: Movimento errático, prioriza rotas alternativas
- **Valor**: 15 recursos
- **Característica especial**: Pode ocasionalmente "dashar" 1 célula

#### 3. Inimigos Tanques
- **Velocidade**: 1 célula/segundo
- **HP**: 40-80
- **Dano**: 10/segundo ou 20/golpe
- **Comportamento**: Ataca estruturas preferencialmente
- **Valor**: 30 recursos
- **Característica especial**: Fica furioso (25% mais rápido) abaixo de 30% HP

#### 4. Inimigos Voadores
- **Velocidade**: 2 células/segundo
- **HP**: 12-20
- **Dano**: 8/segundo
- **Comportamento**: Ignora muros, ataca diretamente a casa
- **Valor**: 25 recursos
- **Requisito**: Só pode ser atacado por torres

### Sistema de Ondas
- **Tempo entre ondas**: 30 segundos
- **Escala de dificuldade**: Crescente
  - Onda 1-3: Apenas inimigos básicos
  - Onda 4-7: Introduz tipos especializados
  - Onda 8-10: Inclui combinações táticas (tanques + velozes)
- **Spawn**: Pontos específicos nas bordas do mapa
- **Contagem regressiva**: Timer visível entre ondas

## 6. Sistema de Recursos

### Economia do Jogo
- **Recurso base**: Cristais mágicos (contador único)
- **Recursos iniciais**: 200
- **Fontes de recursos**:
  1. **Inimigos derrotados**: 15-30 por inimigo
  2. **Resource piles**: Spawnam no mapa (30-80 cada)
  3. **Bônus de combo**: Multiplicador de recursos baseado em tempo

### Resource Piles
- **Aparência**: Cristais brilhantes
- **Tamanho**: 32x32 pixels
- **Coleta**: Automática ao passar próximo
- **Spawn**: Aleatório no mapa + garantido após certos inimigos
- **Tipos**:
  - Normal: 30-50 recursos (80% chance)
  - Raro: 60-80 recursos (20% chance)

### Sistema de Combos
- **Mecânica**: Matar inimigos em rápida sucessão (2 segundos)
- **Multiplicador**: +10% por inimigo no combo
- **Reset**: Quando não mata nada por 2 segundos
- **Bônus**: Aplicado a recursos e pontuação
- **Implementação**:
  ```
  function enemyDefeated(enemy) {
    const now = Date.now();
    if (now - lastKillTime < 2000) {
      combo++;
    } else {
      combo = 1;
    }
    lastKillTime = now;
    
    gainResources(enemy.value * (1 + (combo * 0.1)));
  }
  ```

## 7. Feedback Visual e Efeitos

### Sistema de Partículas
- **Construção**: 12 partículas amarelas em explosão (duração 0.8s)
- **Destruição**: 15 partículas da cor do objeto (duração 1s)
- **Dano**: 3-5 partículas vermelhas + número do dano
- **Coleta de recursos**: Espiral de 8 partículas douradas
- **Dash**: Trilha de 5 partículas azuis por frame

### Feedback de Interface
- **Seleção**: Contorno brilhante ao redor de estruturas selecionadas
- **Alcance**: Círculo semi-transparente mostrando alcance de torres
- **Estado de construção**: Destacar célula atual (verde/vermelho)
- **Cooldowns**: Indicadores visuais com temporizador
- **Saúde**: Barras de vida que mudam de cor (verde → vermelho)

### Efeitos de Status
- **Congelamento**: Inimigo com brilho azul e movimento 50% mais lento
- **Queimadura**: Inimigo com partículas de fogo e dano por tempo
- **Atordoamento**: Inimigo com estrelas girando sobre a cabeça

## 8. Fluxo de Jogo e Progressão

### Estrutura de Campanha
- **Total de níveis**: 20 níveis em 5 ambientes
- **Curva de dificuldade**: Introdução gradual de mecânicas
- **Objetivo por nível**: Sobreviver todas as ondas com a casa intacta

### Sistema de Progressão
- **Desbloqueio de ferramentas**:
  - Nível 1: Muros, torres básicas
  - Nível 3: Armadilhas
  - Nível 5: Reparo
  - Nível 8: Sistema de upgrade
  - Nível 12: Dash

### Sistema de Pontuação
- **Base**: Recursos coletados + inimigos derrotados
- **Multiplicadores**:
  - Vida da casa restante: até 2x
  - Combo máximo: até 1.5x
  - Estruturas preservadas: até 1.3x
- **Recompensas**: Desbloqueia novos tipos de estruturas e habilidades

## 9. Parâmetros Técnicos de Implementação

### Performance e Otimização
- **Entidades máximas**: 50-100 simultâneas
- **Objetivos de frame rate**: 60 FPS
- **Culling**: Entidades fora da tela não são atualizadas
- **Pooling**: Sistema de reuso de objetos para inimigos e projéteis

### Estruturas de Dados
- **Grid de navegação**: Matriz 2D representando células ocupáveis
- **Quad-tree**: Para detecção de colisão eficiente
- **Listas de entidades**: Inimigos, estruturas, projéteis, partículas

### Ciclo de Atualização
```
function gameLoop(timestamp) {
  const deltaTime = (timestamp - lastTime) / 1000;
  lastTime = timestamp;
  
  updatePlayer(deltaTime);
  updateStructures(deltaTime);
  updateEnemies(deltaTime);
  updateProjectiles(deltaTime);
  updateParticles(deltaTime);
  checkCollisions();
  renderAll();
  
  requestAnimationFrame(gameLoop);
}
```

### Parâmetros Balanceáveis
- **Velocidade global**: Multiplicador (0.8-1.2)
- **Dificuldade de inimigos**: Multiplicador de HP e dano (0.8-1.5)
- **Economia**: Multiplicador de custo e ganho (0.8-1.2)
- **Progressão**: Multiplicador de requisitos de upgrade (0.9-1.1)

Este documento fornece uma visão abrangente do design do Constructor Defense, detalhando todas as mecânicas, sistemas e parâmetros necessários para implementação. As especificações técnicas são suficientemente detalhadas para permitir a criação do jogo conforme concebido, mantendo a inovação de um construtor ativo no campo de batalha.