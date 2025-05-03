 <img src="../assets/logointeli.png">


# GDD - Game Design Document - Módulo 1 - Inteli

## BIGODE'S

#### Nomes dos integrantes do grupo
- João de Caprio Agmont
- Paulo Vitor Barros de Almeida
- Isabela Rosati Peçanha
- Reimar Coelho Ferreira Filho
- Cauê Meyer Taddeo
- Thúlio Sallum Bacco Pinto
- Mariana Pereira de Souza 
- Henrique Rodrigues Diniz


## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Jogo](#c2)

[3. Game Design](#c3)

[4. Desenvolvimento do Jogo](#c4)

[5. Casos de Teste](#c5)

[6. Conclusões e trabalhos futuros](#c6)

[7. Referências](#c7)

[Anexos](#c8)

<br>


# <a name="c1"></a>1. Introdução 

## 1.1. Plano Estratégico do Projeto

### 1.1.1. Contexto da indústria 
&nbsp;&nbsp;&nbsp;&nbsp;O mercado de comportamento e adestramento animal tem crescido com a alta demanda por métodos positivos. Os principais players incluem influenciadores, como Dr. Pet, Cesar Millan e Ian Dunbar, além de plataformas educacionais e empresas de produtos para pets. Os modelos de negócio variam entre consultorias, cursos online e assinaturas. Já as tendências no setor de cuidado de pets abrem margens para a gamificação e tecnologia. Alexandre Rossi busca inovação e diferenciação da concorrência ao abranger áreas de atuação como a mídia tradicional e as redes sociais, bem como a possível entrada no mercado de jogos digitais para animais domésticos [8], [9].

#### 1.1.1.1. Modelo de 5 Forças de Porter 

&nbsp;&nbsp;&nbsp;&nbsp;As 5 Forças de Porter são um modelo estratégico desenvolvido por Michael Porter, professor da Harvard Business School, na década de 1970. Este framework é amplamente utilizado para analisar a competitividade em um setor de negócios, identificando as principais forças que influenciam o ambiente competitivo de uma empresa. Ao analisar essas forças, é possível desenvolver estratégias eficazes para melhorar a posição competitiva da empresa no mercado. Sendo assim, a imagem a seguir apresenta a análise da indústria de comportamento e bem-estar de animais, a fim de averiguar como a marca Dr Pet se posiciona nesse setor [3], [6], [10].

<div align="center">
<sub> Figura X - 5 Forças de Porter</sub>
<img src="../assets/cinco_forcas.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>


### 1.1.2. Análise SWOT

&nbsp;&nbsp;&nbsp;&nbsp;A análise SWOT é uma ferramenta estratégica que avalia o cenário interno e externo de uma empresa, identificando forças e fraquezas internas, além de oportunidades e ameaças externas. Isso inclui análises de mercado, concorrentes, fornecedores e contextos políticos, econômicos, sociais e culturais. Na figura 1, apresentamos a análise SWOT centrada na marca Dr Pet [3], [6], [7].

<div align="center">
<sub>Figura 1 - Análise SWOT</sub>
<img src="../assets/analiseSwot.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;A Dr. Pet se posiciona como uma marca consolidada e referência no mercado pet, apoiando-se na credibilidade de Alexandre Rossi e sua forte presença digital. No que tange à concorrência com influenciadores e métodos tradicionais de adestramento, é exigido diferenciação contínua para se destacar. Nesse contexto, sua presença em diferentes ambientes de influência, como redes sociais, mídias tradicionais e literatura educativa, coloca-a em vantagem em relação a seus oponentes. Oportunidades como a crescente demanda por adestramento positivo e a digitalização do setor podem fortalecer sua posição. Contudo, mudanças em algoritmos e regulações representam ameaças que exigem adaptação constante.

### 1.1.3. Missão / Visão / Valores 

&nbsp;&nbsp;&nbsp;&nbsp;A análise de Missão, Visão e Valores é uma ferramenta estratégica fundamental para qualquer empresa, pois ajuda a definir sua identidade e propósito. A Missão descreve o que a empresa faz atualmente, para quem ela trabalha e qual é seu objetivo principal. Ela serve como um guia para as operações diárias e define o papel da empresa no mercado. A Visão, por outro lado, estabelece o objetivo futuro, indicando onde a empresa deseja chegar a longo prazo. Ela inspira e motiva os funcionários a trabalhar em direção a um objetivo comum, ajudando a direcionar as estratégias e decisões da empresa. Os Valores representam os princípios éticos e morais que guiam as ações e decisões da empresa [5]. Eles influenciam a cultura organizacional e são essenciais para construir confiança com clientes, funcionários e parceiros. Essa análise é crucial para que as empresas mantenham uma direção clara e coerente, alinhando suas operações com seus objetivos e princípios. Dessa forma, esses fundamentos podem ser descritos para a marca Dr Pet da seguinte forma:

- Missão: democratizar o acesso aos serviços veterinários e de adestramentos para que os pets desfrutem do direito a uma vida tranquila e saudável;

- Visão: expandir a atuação através de serviços de qualidade que proporcionam uma experiência sempre positiva para os tutores e pets;

- Valores: excelência com simplicidade, credibilidade na transparência, atendimento com respeito e ética, ser sustentável em todos os aspectos.

### 1.1.4. Proposta de Valor 

&nbsp;&nbsp;&nbsp;&nbsp;O Canvas de Proposta de Valor é uma ferramenta estratégica amplamente utilizada para entender as necessidades do público-alvo e alinhar essas necessidades com a oferta de produtos ou serviços. Sua principal função é mapear as "dores", "ganhos" e "tarefas" dos consumidores, proporcionando uma visão clara sobre como uma solução pode resolver problemas ou atender às expectativas. Ao conectar as necessidades dos clientes às ofertas de valor, o canvas facilita a criação de soluções mais eficazes e personalizadas, sendo essencial para o desenvolvimento de produtos e serviços que realmente atendem às demandas do mercado. Aa figura 2 apresenta a análise Canvas Proposta de Valor centrada na solução proposta [11]. 

<div align="center">
<sub>Figura 2 - Canvas Proposta de Valor</sub>
<img src="../assets/canvasPropostadeValor.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;No caso do PawDash, o Canvas de Proposta de Valor é fundamental para identificar as principais "dores" dos tutores de gatos, como a falta de tempo e espaço para interagir com seus pets. O PawDash oferece uma solução interativa que mantém os gatos fisicamente e mentalmente estimulados, evitando problemas como obesidade e estresse, além de fortalecer o vínculo com os tutores, mesmo com rotinas corridas.

&nbsp;&nbsp;&nbsp;&nbsp;Aplicando o Canvas, é possível garantir que o PawDash atenda de forma eficaz às necessidades dos gatos e seus tutores, proporcionando benefícios mútuos: um pet saudável e engajado, e um tutor tranquilo, sabendo que está oferecendo a melhor experiência possível para seu felino.


### 1.1.5. Descrição da Solução Desenvolvida 

&nbsp;&nbsp;&nbsp;&nbsp;A solução desenvolvida consiste em um jogo interativo para gatos no iPad, projetado para estimular seus reflexos e proporcionar uma experiência envolvente tanto para os pets quanto para seus tutores. O jogo utiliza uma mecânica baseada no toque na tela, onde o gato deve acertar patas virtuais para avançar de fase. A cada nível, a dificuldade aumenta, introduzindo elementos como obstáculos e movimentação aleatória, tornando o desafio progressivamente mais complexo e estimulante.  

&nbsp;&nbsp;&nbsp;&nbsp;O diferencial da solução está na sua simplicidade e interatividade, garantindo uma experiência intuitiva para o gato e incentivando a participação ativa do tutor, que reforça o engajamento do pet oferecendo petiscos como recompensa física. O jogo foi pensado para alinhar-se às necessidades do mercado pet, proporcionando uma alternativa inovadora de entretenimento digital para animais de estimação.  

&nbsp;&nbsp;&nbsp;&nbsp;A solução agrega valor ao permitir que tutores ofereçam um estímulo mental e físico aos seus gatos, prevenindo o tédio e reforçando o vínculo entre pet e dono. Além disso, sua abordagem acessível e gamificada atende à crescente demanda por produtos tecnológicos voltados para o bem-estar animal.


### 1.1.6. Matriz de Riscos


&nbsp;&nbsp;&nbsp;A matriz de riscos é uma ferramenta essencial para a gestão de projetos, pois permite identificar, classificar e avaliar os riscos envolvidos em seu desenvolvimento. Seu principal objetivo é mensurar a probabilidade de ocorrência e o impacto que cada risco pode causar, seja positivo ou negativo. Dessa forma, a matriz auxilia na criação de estratégias eficazes para mitigar ameaças e potencializar oportunidades, garantindo maior controle sobre os desafios enfrentados ao longo do projeto. A figura 3 representa a análise de risco do projeto Paw Dash [4].

<div align="center">
<sub>Figura 3 - Matriz de Riscos</sub>
<img src="../assets/matrizderisco.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>


&nbsp;&nbsp;&nbsp;No projeto Paw Dash, foram mapeados os principais riscos que podem afetar sua execução. Cada um foi classificado de acordo com sua probabilidade e impacto, e foram traçadas estratégias para lidar com essas situações. A seguir, são apresentados os riscos identificados, juntamente com seus respectivos planos de ação e resposta:

1. Falta de conhecimento para desenvolver funcionalidades do projeto
- Probabilidade: 70%
- Impacto: Moderado
- Plano de Ação e Resposta: Identificar lacunas no conhecimento; Buscar cursos ou tutoriais; Pedir ajuda em comunidades e fóruns especializados.
  
2. Não cumprir promessas feitas (exemplo: Arduino)
- Probabilidade: 50%
- Impacto: Muito Alto
- Plano de Ação e Resposta: Priorizar tarefas essenciais; Avaliar a viabilidade antes de comprometer recursos; Dividir funcionalidades em MVPs menores para uma implementação mais realista.
  
3. Não conseguir corrigir todos os bugs até o fim da Sprint 5
- Probabilidade: 30%
- Impacto: Alto
- Plano de Ação e Resposta: Implementar testes automatizados e criar um backlog de correção de bugs críticos para priorizar ajustes na Sprint 5.
  
4. Os gatos não interagirem com os elementos do jogo
- Probabilidade: 30%
- Impacto: Muito Alto
- Plano de Ação e Resposta: Ajustar cores, movimentos e sons para tornar o jogo mais atraente; Realizar testes com diferentes gatos; Iterar com base no feedback obtido.
  
5. Impedimentos com ponderada
- Probabilidade: 70%
- Impacto: Alto
- Plano de Ação e Resposta: Criar um planejamento realista, evitando utilizar os horários de dev para realizar atividades ponderadas e utilizar técnicas de produtividade como Pomodoro para otimizar o tempo disponível.
  
6. Queda de internet durante o desenvolvimento
- Probabilidade: 10%
- Impacto: Alto
- Plano de Ação e Resposta:
Baixar documentação e dependências antecipadamente e configurar um ambiente local que minimize os impactos da desconexão.

&nbsp;&nbsp;&nbsp;A aplicação da matriz de riscos no projeto Paw Dash permite uma abordagem estruturada e proativa na identificação e mitigação de desafios. Com a análise detalhada dos riscos e a implementação de medidas preventivas, é possível aumentar a eficiência do desenvolvimento, reduzir imprevistos e aprimorar a tomada de decisões. Além disso, a matriz também possibilita a identificação de oportunidades, auxiliando no direcionamento estratégico do projeto.




### 1.1.7. Objetivos, Metas e Indicadores 

 1.1.7.1. Qual é o objetivo do projeto?  

&nbsp;&nbsp;&nbsp;&nbsp;O objetivo do projeto é desenvolver um jogo interativo para gatos no iPad, que estimule seus reflexos e promova a interação entre os pets e seus tutores. O jogo deve ser intuitivo, engajador e progressivamente desafiador, garantindo uma experiência divertida para os gatos e incentivando o envolvimento dos tutores por meio de um sistema de recompensas físicas como petiscos.  

 1.1.7.2. Quais são as metas do projeto?  

&nbsp;&nbsp;&nbsp;&nbsp;Para garantir o sucesso do jogo, foram estabelecidas metas SMART (Específicas, Mensuráveis, Alcançáveis, Relevantes e Temporais).

1. Finalizar a primeira versão jogável (MVP) com a mecânica de toque e progressão de fases implementadas.  
2. Testar o jogo com pelo menos 10 gatos e seus tutores, avaliando engajamento e interatividade.
3. Otimizar a interface e design gráfico, melhorando a experiência visual e a responsividade do jogo. 
4. Lançar a versão beta para testes públicos, atingindo pelo menos 100 downloads. Prazo: 12 semanas.  
5. Alcançar uma taxa de engajamento de 70%, com gatos interagindo por pelo menos 2 minutos por sessão. 



 1.1.7.3. Como as metas serão medidas?  

&nbsp;&nbsp;&nbsp;&nbsp;As métricas de sucesso serão avaliadas por meio de testes práticos e dados quantitativos, analisando o engajamento dos gatos e a aceitação do jogo pelos tutores.  

- Teste com usuários reais: Observação do comportamento dos gatos e feedbacks quantitativos dos tutores.  
- Tempo médio de interação: Medição do tempo que os gatos passam jogando e a quantidade de toques bem-sucedidos.  
- Número de downloads e avaliações: Indicador do interesse e aceitação do jogo no mercado.  
- Taxa de retenção: Número de jogadores que voltam a utilizar o jogo após a primeira sessão.  



 1.1.7.4. Quais os benefícios da solução proposta?  
 
&nbsp;&nbsp;&nbsp;&nbsp;O jogo trará vantagens tanto para os gatos quanto para seus tutores, além de representar uma inovação no mercado pet.  

- Para os gatos: Estimulação mental e física, redução do tédio e incentivo ao instinto natural de caça.  
- Para os tutores: Uma ferramenta divertida e interativa para entreter seus pets, promovendo maior engajamento e reforço positivo.  
- Para o mercado pet: Introdução de um conceito inovador que pode ser expandido para novas plataformas e funcionalidades futuras.  



 1.1.7.5. Qual será o critério de sucesso e qual medida será utilizada para avaliá-lo?  

&nbsp;&nbsp;&nbsp;&nbsp;O sucesso será determinado pelo engajamento dos gatos, a satisfação dos tutores e a adoção do jogo no mercado.  

- Engajamento dos gatos: Pelo menos 70% dos gatos testados devem interagir com o jogo por 2 minutos ou mais por sessão.  
- Satisfação dos tutores: Feedback positivo de 80% dos tutores que testarem o jogo com seus pets.  
- Adoção do jogo: Alcançar 100 downloads na versão beta e manter uma avaliação média de 4 estrelas ou mais.  
- Aprimoramento contínuo: Implementação de ajustes baseados nos testes para tornar o jogo mais envolvente e eficiente.  



## 1.2. Requisitos do Projeto

&nbsp;&nbsp;&nbsp;&nbsp;Os requisitos do projeto representam as necessidades e expectativas essenciais que orientam seu desenvolvimento e execução. Eles estabelecem o que precisa ser alcançado, de que forma e sob quais condições. O quadro 1 abrange os requisitos funcionais e não funcionais, além dos aspectos técnicos, de qualidade e conformidade. Fundamentais para assegurar os objetivos, esses requisitos servem como base para o planejamento, implementação e avaliação do projeto.

<div align="center">
<sub>Quadro 1 - Requisitos Fundamentais do Jogo</sub>
</div>

\# | Requisitos Fundamentais do Jogo
--- | ---
1 | O jogo deve ser publicável nas principais lojas de aplicativos
2 | O jogo deve funcionar em dispositivos móveis, como celulares e tablets
3 | O dispositivo móvel deve interpretar o toque da pata de gatos
4 | A descrição do jogo deve explicitar que ele é voltado para gatos
5 | O jogo deve apresentar responsividade para ter aparência adequada em diferentes tamanhos de tela
6 | O jogo deve indicar com clareza que o tutor é essencial para a jogabilidade
7 | Os elementos gráficos devem ser esticamente agradáveis ao público-alvo (humanos)
8 | O jogo deve indicar que o tutor deve preparar com antecedência petiscos para recompensar o gato
9 | O jogo deve apresentar diferentes fases que representam diferentes níveis de complexidade
10 | O jogo deve possuir uma interface intuitiva que mostre claramente que o jogo é estruturado em fases
11 | O tutor deve conseguir selecionar a fase que deseja que o gato jogue
12 | Após o tutor selecionar uma fase, deve aparecer uma pequena explicação sobre ela antes do jogo iniciar
13 | A primeira fase deve ser simples e introduzir as principais mecânicas do jogo
14 | O jogo deve apresentar um alvo que se comporte de modo a capturar a atenção do gato
15 | Os elementos gráficos do jogo devem apresentar cores visíveis para gatos
16 | Os alvos devem possuir cores que se destacam na visão dos gatos em relação aos outros elementos
17 | O alvo deve ser capaz de estimular os instintos de caça do gato
18 | O jogo deve apresentar estímulos visuais quando o gato tocar corretamente o alvo
19 | O jogo deve apresentar estímulos de sons de alta frequência quando o gato tocar corretamente o alvo
20 | O background do jogo deve ser simples para não confundir o gato
21 | Os alvos devem ser "destruídos" após uma determinada quantidade pequena de toques 
22 | A quantidade de toques necessária para destruir o alvo deve progredir lentamente de acordo com as fases
23 | O jogo deve apresentar uma mecânica nova para o alvo a cada fase
24 | As novas mecânicas devem desafiar cada vez mais as habilidades de caça do gato
25 | O jogo deve mostrar uma tela que indica que é o momento de recompensar o gato após todos os alvos serem destruídos
26 | O jogo deve fazer o gato associar a destruição dos alvos à recompensa
27 | O jogo deve indicar que o petisco deve ser posicionado na posição do último alvo destruído
28 | O jogo deve possibilitar o dispositivo conectar via Bluetooth com um dispositivo de recompensa automática
29 | O jogo deve ativar o mecanismo de recompensa automática quando o gato acertar o alvo

<div align="center">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

## 1.3. Público-alvo do Projeto

&nbsp;&nbsp;&nbsp;&nbsp;O jogo tem como público-alvo todos os donos de gatos que buscam formas inovadoras de entretenimento e estímulo para seus pets, especialmente aqueles que vivem em ambientes urbanos e utilizam tecnologia no dia a dia. Foi desenvolvido para proporcionar uma experiência interativa entre gatos e seus tutores, promovendo o enriquecimento ambiental e fortalecendo o vínculo entre ambos. Ao abranger esse público, independentemente da idade ou nível de experiência com tecnologia, busca-se garantir que os gatos tenham acesso a um jogo envolvente e adequado ao seu comportamento natural, enquanto os donos desfrutam de uma solução prática e intuitiva para estimular seus animais. O objetivo é incentivar momentos de diversão compartilhada, melhorar o bem-estar dos felinos e oferecer uma alternativa acessível e inovadora dentro do universo digital.

# <a name="c2"></a>2. Visão Geral do Jogo

## 2.1. Objetivos do Jogo 

&nbsp;&nbsp;&nbsp;&nbsp;O jogador (gato) deve tocar no alvo presente na tela, com o objetivo de "destruí-lo" para ser recompensado, conforme o jogador completa as fases, o processo de recompensa fica mais complexo.

## 2.2. Características do Jogo 
&nbsp;&nbsp;&nbsp;&nbsp;O jogo pode ser decrito com cinco características principais que marcam sua jogabilidade:

- O jogo apresenta cinco fases;
- Cada nova fase apresenta alvos com movimentação mais rápida e padrões mais complexos;
- A cada fase, um novo desafio ou elemento é introduzido;
- Há animações ou efeitos especiais que ajudam a manter o jogador imerso;
- O jogador é recompensado pelo tutor após concluir com êxito uma fase.



### 2.2.1. Gênero do Jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Jogo para gato.

### 2.2.2. Plataforma do Jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Quanto ao dispositivo: smartphones e tablets.

&nbsp;&nbsp;&nbsp;&nbsp;Quanto ao sistema: disposítivos móveis que interpretam touch screen.

### 2.2.3. Número de jogadores 

&nbsp;&nbsp;&nbsp;&nbsp;1 ou 2 jogadores.

### 2.2.4. Títulos semelhantes e inspirações 

&nbsp;&nbsp;&nbsp;&nbsp;Temos como títulos semelhantes e inspirações os seguintes jogos: "Cat Toy 2", "Jogos para Gatos", "Meow jogos Para Gatos Filhotes".

### 2.2.5. Tempo estimado de jogo 

*Ex. O jogo pode ser concluído em 3 horas passando por todas as fases.*

*Ex. cada partida dura até 15 minutos*

# <a name="c3"></a>3. Game Design 

## 3.1. Enredo do Jogo 

3.1. Enredo do Jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Nosso jogo é focado em gatos e possui uma mecânica simples de tocar em alvos para ganhar pontos. Apesar de não possuir um enredo tradicional, todo jogo apresenta um contexto, um desafio e um cenário estruturado. Sendo assim, contextualizamos nosso jogo da seguinte forma:

- Contexto: O jogador e seu gato participam de um ambiente interativo projetado para estimular os instintos felinos, oferecendo desafios visuais e de reação;

- Objetivo: O gato deve interagir com os alvos que aparecem na tela para acumular pontos, enquanto o tutor acompanha e incentiva a interação;

- Cenário: O jogo ocorre em um ambiente amigável e estimulante, com variações visuais que criam uma experiência envolvente.

## 3.2. Personagens 

### 3.2.1. Controláveis

&nbsp;&nbsp;&nbsp;&nbsp;Nosso jogo não possui personagens controláveis, pois:

- Não há avatares ou personagens fictícios durante a jogabilidade – o próprio gato interage diretamente com os elementos na tela;

- O jogo é projetado para estimular o instinto de caça do gato, utilizando movimentos e efeitos visuais para incentivar a interação;

- A experiência é intuitiva e baseada no comportamento natural do animal, dispensando personagens jogáveis.

### 3.2.2. Non-Playable Characters (NPC)

&nbsp;&nbsp;&nbsp;&nbsp;NPC (Non-Playable Character, ou Personagem Não Jogável) é qualquer personagem em um jogo que não é controlado diretamente pelos jogadores. Eles geralmente são programados para desempenhar funções específicas, como interagir com os jogadores, fornecer informações, vender itens, ou contribuir para o enredo e a ambientação do jogo.

&nbsp;&nbsp;&nbsp;&nbsp;O jogo Paw Dash não possui NPCs porque sua proposta central é focada exclusivamente na interação entre os jogadores, tutor e gato, e elementos despersonalizados, os alvos. A ausência de NPCs reforça a dinâmica de um ambiente colaborativo e competitivo, promovendo uma experiência mais imersiva e imprevisível. Essa abordagem também simplifica o design do jogo, permitindo que o jogo tenha mais ênfase na jogabilidade e nas mecânicas centradas nos jogadores.

### 3.2.3. Diversidade e Representatividade dos Personagens

&nbsp;&nbsp;&nbsp;&nbsp;O jogo foi projetado para ser acessível tanto para os gatos quanto para os humanos, garantindo que a experiência seja envolvente e inclusiva. Para isso, foram consideradas diversas adaptações para daltônicos e surdos, garantindo que ninguém fique excluído da jogabilidade.

&nbsp;&nbsp;&nbsp;&nbsp;Acessibilidade para Daltônicos:

- Uso de cores contrastantes (ex: amarelo e azul) para facilitar a visualização tanto pelos gatos quanto pelos humanos daltônicos;

- Padrões e texturas distintas para diferenciar elementos visuais sem depender apenas de cores;

- Feedback visual reforçado com animações e efeitos luminosos para indicar interações bem-sucedidas.

&nbsp;&nbsp;&nbsp;&nbsp;Acessibilidade para Surdos:

- Sinais visuais de reforço positivo (brilhos, pequenas vibrações na tela, mudanças de cor ao acertar a pata);

## 3.3. Mundo do jogo 

### 3.3.1. Locações Principais e/ou Mapas 

&nbsp;&nbsp;&nbsp;&nbsp;O jogo se passa em um ambiente virtual projetado para maximizar a interação do gato. As principais locações incluem:
\# | Local | Descrição
--- | --- | ---
1 | Tela Inicial | Área onde o tutor pode acessar o jogo e selecionar os modos de jogo. |
2 | Fases de Caça | Diferentes cenários em que os alvos aparecem, estimulando o gato a caçá-los. |
3 | Menu de Configuração | Permite ajustar elementos como som, cores e níveis de dificuldade. |



### 3.3.2. Navegação pelo mundo 

&nbsp;&nbsp;&nbsp;&nbsp;A navegação no jogo é simples e direta:

- 1. O tutor escolhe o nível e inicia o jogo;
- 2. O gato interage com os alvos na tela, gerando pontuações e efeitos visuais;
- 3. Conforme avança, novas fases e desafios são desbloqueados automaticamente.

### 3.3.3. Concept Art 

&nbsp;&nbsp;&nbsp;&nbsp;Uma concept art é a essência visual de uma ideia, ela explica a atmosfera onde o jogo se passará, os personagens presentes e as fases. Ele será um reflexo de nosso processo criativo, evidenciando que passos tomamos para a criação do design de nosso jogo. O link abaixo apresenta um arquivo que aborda o processo da criação das concepts arts do nosso jogo.

- https://www.figma.com/design/cVbJo00x8BpZQIv578cxQV/Figma-basics?m=dev&t=5ewIVfxGBBk5PlOo-1

### <a name="som"></a>3.3.4. Trilha sonora 

&nbsp;&nbsp;&nbsp;&nbsp;A trilha sonora de um jogo é tão essencial quanto a própria jogabilidade, uma vez que influencia as emoções dos jogadores, fazendo-os criar uma conexão com o jogo. Portanto ao selecionar os áudios e efeitos sonoros, foram tomados cuidados extras, para não prejudicar a concepção do jogo e ornando com a proposta do mesmo.
&nbsp;&nbsp;&nbsp;&nbsp;Ao pensar sobre a trilha sonora, destacou-se a preferência por algo mais chamativo, a fim de "dar a cara" para o jogo através da unicidade da música. Foi decidido também a adição de efeitos sonoros para certas funcionalidades, como: clique dos botôes (configuração, play, etc...), destruição da pata e da pata se movimentando.

\# | titulo | ocorrência | autoria 
--- | --- | --- | ---
1 | "Vacation with my cat" | Trilha principal | <a href = "https://pixabay.com/music/upbeat-vacation-with-my-cat-248359/"> Pixabay (AI generated) </a>
2 | Light Switch | Clique dos botões | <a href = "https://freesound.org/people/GOSFX/sounds/324334/"> freesound </a>
3 | TIN bigode | Clique do botão dos créditos | Autoral
4 | "me dá me dá" - piano cover | Trilha sonora das configurações | Cover da propaganda do 'danoninho' ("me dá me dá")
5 | TIN | Clique na pata | Autoral
6 | Prato de bateria | Clique dos níveis | Autoral
7 | Botão do elevador | Clique dos botões | Autoral
8 | Folhas | Esconderijo da pata na fase 4 | Autoral
9 | "Bink no Sake" - piano cover | Trilha sonora dos créditos | Cover influcenciado pela música "Bink no Sake" (One Piece)
10 | Chocalho | Movimento da pata | Autoral

## 3.4. Inventário e Bestiário 

### 3.4.1. Inventário

&nbsp;&nbsp;&nbsp;&nbsp;Um inventário em jogos é um sistema que permite ao jogador armazenar, organizar e utilizar itens adquiridos ao longo da gameplay. Ele pode conter objetos essenciais para progressão, como armas, recursos, moedas ou equipamentos, dependendo do gênero do jogo. O inventário pode ser acessado a qualquer momento e geralmente envolve mecânicas de gestão de recursos, coleta de itens e uso estratégico de elementos dentro do jogo.

&nbsp;&nbsp;&nbsp;&nbsp;O nosso jogo não possui um sistema de inventário porque sua mecânica central é baseada na interação direta do gato com a tela, sem necessidade de armazenar itens para uso posterior. 

### 3.4.2. Bestiário

&nbsp;&nbsp;&nbsp;&nbsp;Um bestiário em jogos é um compêndio que reúne informações sobre as criaturas encontradas ao longo da gameplay. Ele pode incluir descrições, imagens, fraquezas, habilidades e contexto dentro da história, ajudando o jogador a entender melhor os inimigos ou seres presentes no mundo do jogo. Muitas vezes, o bestiário é desbloqueado progressivamente, conforme o jogador enfrenta ou derrota novas criaturas.  

&nbsp;&nbsp;&nbsp;&nbsp;Nosso jogo não possui um sistema de bestiário porque seu foco está em uma dinâmica simples de interação entre o gato e um elemento despersonalizado na tela, portanto, não utiliza do artifício de introduzir criaturas antogonistas ao jogador para gerar desafio.

## 3.5. Gameflow (Diagrama de cenas) 

&nbsp;&nbsp;&nbsp;&nbsp;Um diagrama de cenas para um jogo representa visualmente a transição entre diferentes telas ou estados, como menus, fases e cutscenes. Ele auxilia no planejamento da navegação, garantindo uma experiência fluida para o jogador e facilitando a organização do desenvolvimento. O link abaixo contém um arquivo que apresenta o diagrama de cenas do nosso jogo.

- https://www.figma.com/design/luhoZeSsvZhyLUqD8fNmj2/Figma-basics?node-id=1669-162202&m=dev&t=ip24dGcWd0Ux4PSl-1*

## 3.6. Regras do jogo 

&nbsp;&nbsp;&nbsp;&nbsp;As regras do jogo definem o início, o progresso dos jogadores, as ações possíveis e o desfecho do jogo, sendo fundamentais para garantir que o usuário entenda com clareza a jogabilidade e, assim, tenha uma boa experiência ao jogar. Desse modo, foram estabelecidas as seguintes regras para o jogo "Paw Dash":

- O usuário deve concluir as fases de modo que, após ter êxito na primeira, poderá jogar a segunda, e assim por diante;

- O usuário (gato) deve tocar corretamente no alvo para ser recompensado;

- O usuário (tutor) deve estar preparado para recompensar o gato quando ele obtiver êxito no jogo;

- O jogo deve usar de cores contrastantes para facilitar a visualização dos elementos por usuários daltônicos e os gatos, contribuindo para uma experiência mais inclusiva.

&nbsp;&nbsp;&nbsp;&nbsp;A partir dessas regras, os usuários (tutor e gato) poderão aproveitar plenamente a experiência oferecida pelo jogo.

## 3.7. Mecânicas do jogo 

&nbsp;&nbsp;&nbsp;&nbsp;As mecânicas de um jogo dizem respeito ao conjunto de interações que possibilitam a realização de ações e a progressão dentro da experiência do jogador. O propósito dessas mecânicas é oferecer desafios, entretenimento e uma experiência imersiva, permitindo que os jogadores explorem o que o jogo oferece, atinjam objetivos e superem obstáculos dentro do contexto definido pelas metas do jogo.

&nbsp;&nbsp;&nbsp;&nbsp;Com isso em mente, para garantir uma mecânica intuitiva, de fácil uso para os gatos e que apresentasse uma progressão de dificuldade, as interações do jogo ocorrem por meio do toque, ação mais adequada para os felinos interagirem com a tela, ou seja, o gato interage com os alvos, elementos principais da jogabilidade, tocando-os. Assim, o desafio ao usuário aumenta à medida que os alvos se movem de forma mais complexa, o que torna mais difícil acertá-los. Ademais, as interações feitas pelo tutor também ocorrem pelo toque, como a seleção de níveis. Outra mecânica do jogo é a responsividade, ou seja, ele se adapta a diferentes tamanhos de tela, garantindo que a experiência seja consistente tanto em tablets quanto em smartphones.

# 3.8. Implementação Matemática de Animação/Movimento

&nbsp;&nbsp;&nbsp;&nbsp;A movimentação dos elementos gráficos no jogo é implementada a partir de uma modelagem matemática que considera o tempo, a aceleração e a velocidade no movimento de um personagem ou objeto. A seguir, detalhamos as funções que descrevem a animação de um elemento gráfico, com base nas equações de Movimento Uniforme (MU) e Movimento Uniformemente Variado (MUV).

## 3.8.1. Parâmetros Iniciais

Antes de definir as funções matemáticas para o movimento, definimos alguns parâmetros iniciais que serão usados em todos os cálculos:

- **t_total**: O tempo total da animação, medido em segundos. Esse parâmetro define a duração do movimento do elemento gráfico, desde o início até a posição final.
- **(x_i, y_i)**: As posições iniciais do elemento gráfico. Este ponto corresponde à posição inicial em que o objeto começa a se mover.
- **(x_f, y_f)**: As posições finais do elemento gráfico. Corresponde ao destino final do movimento.

Esses parâmetros são fundamentais para a modelagem do movimento, pois eles determinam o comportamento do objeto ao longo do tempo.

## 3.8.2. Movimento Uniforme (MU)

O Movimento Uniforme (MU) ocorre quando a velocidade do objeto é constante ao longo de todo o movimento. A fórmula para calcular a velocidade no eixo y e a posição no eixo y, considerando o movimento uniforme, é descrita abaixo.

### 3.8.2.1. Função de Velocidade no eixo y (MU)

A velocidade no movimento uniforme é constante, e pode ser calculada como a diferença das posições final e inicial dividida pelo tempo total t_total:

- **v_y = (y_f - y_i) / t_total**

### 3.8.2.2. Função de Posição no eixo y (MU)

A posição no eixo y em um determinado instante t durante o movimento é dada por:

- **y(t) = y_i + v_y . t**

## 3.8.3. Movimento Uniformemente Variado (MUV)

O Movimento Uniformemente Variado (MUV) ocorre quando a aceleração do objeto é constante ao longo do movimento. A aceleração, neste caso, pode ser positiva ou negativa, resultando em um aumento ou diminuição da velocidade ao longo do tempo. A seguir, apresentamos as fórmulas para calcular a aceleração, a velocidade e a posição no movimento uniformemente variado.

### 3.8.3.1. Função de Aceleração no eixo x (MUV)

A aceleração no eixo x, considerando as posições inicial e final e o tempo total de animação, é dada por:

- **a_x = 2 . (x_f - x_i - vix . t_total) / (t_total^2)**

Se **vix = 0**, temos:

- **a_x = 2 . (x_f - x_i) / (t_total^2)**

### 3.8.3.2. Função de Velocidade no eixo x (MUV)

A velocidade no eixo x em um determinado instante t é dada por:

- **v_x(t) = vix + a_x . t**

### 3.8.3.3. Função de Posição no eixo x (MUV)

A posição no eixo x em um determinado instante t é dada por:

- **x(t) = x_i + vix . t + (a_x . t^2) / 2**

## 3.8.4. Implementação no Jogo

No jogo, a movimentação do bigode até a logo é calculada usando uma combinação de Movimento Uniformemente Variado (MUV) para o eixo x e Movimento Uniforme (MU) para o eixo y.

As equações de movimento para o bigode, conforme implementadas no código do jogo, são as seguintes:

- Posição no eixo x:

  **x(t) = x_i + vix . t + (a_x . t^2) / 2**

- Posição no eixo y:

  **y(t) = y_i + v_y . t**

Essas equações são usadas para calcular as coordenadas x(t) e y(t) a cada quadro, atualizando a posição do bigode de acordo com a animação.

## 3.8.5. Implementação no Código

A implementação do movimento descrito nesta seção está contida no arquivo `menu.js`. Você pode encontrar o código que executa a animação a partir da linha 266 até a 309.

```javascript
// Define a posição final do bigode, ajustada conforme o tamanho da tela do dispositivo
this.bigodeXFinal = this.logo.x - 135 * this.escalaLogo;
this.bigodeYFinal = this.logo.y + 35 * this.escalaLogo;

// Chama a função de deslocamento acelerado horizontal do bigode até que ele esteja na posição final
if (this.bigodeX <= this.bigodeXFinal) {
  // Movimento horizontal progressivo: v * t + (1/2) * a * t²
  this.bigodeX += 2 * this.t + 0.5 * this.t * this.t; 
  // Calcula a velocidade a cada frame
  this.velocidadeX = 2 + 0.5 * this.t;
  // Mostra no console a aceleração, a velocidade em cada frame e a posição no eixo X do bigode
  console.log("Aceleração: " + 0.5, "| Velocidade: " + this.velocidadeX.toFixed(2), "| Posição: " + this.bigodeX.toFixed(2), "(MUV)");
}

// Chama a função de deslocamento uniforme vertical do bigode até que ele esteja na posição final
if (this.bigodeY >= this.bigodeYFinal) {
  this.bigodeY -= 0.8 * this.t; // Movimento vertical regressivo: -v * t
  // Mostra no console a velocidade e a posição no eixo Y do bigode
  console.log("Velocidade: " + (-0.8 * this.t).toFixed(2), "| Posição: " + this.bigodeY.toFixed(2), "(MU)");
}

if (this.bigodeY >= this.bigodeYFinal || this.bigodeX <= this.bigodeXFinal) {
  // Atualiza a posição do bigode conforme as equações de deslocamento enquanto não está na posição final
  this.bigode.setPosition(this.bigodeX, this.bigodeY);
} else {
  // Registra e mostra no console o tempo total que durou o movimento
  if (!this.tFinal) {
    this.tFinal = this.time.now;
    this.tTotal = (this.tFinal - this.inicioMovimento) / 1000;
    console.log("Tempo total: " + this.tTotal.toFixed(2));
  } 
}
```



# <a name="c4"></a>4. Desenvolvimento do Jogo

## 4.1. Desenvolvimento preliminar do jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Para a primeira versão do jogo em termos de código, selecionamos as mecânicas e dinâmicas mais importantes da jogabilidade, bem como alguns elementos cruciais da estética escolhida, como o modelo de uma pata (alvo principal do gato) em pixel art, para desenvolver uma tela que demonstra a essência do nosso projeto. Desse modo, as etapas desenvolvidas preliminarmente, bem como os desafios encontrados e a projeção para o futuro do projeto, podem ser definidos pelos tópicos seguintes.

### **4.1.1. Estética**

&nbsp;&nbsp;&nbsp;&nbsp;Para compor os elementos estéticos iniciais do nosso jogo, desenvolvemos em pixel art a representação de uma pata de gato (figura 4), que atua no jogo como alvo tocável para o gato usuário. Ademais, foi selecionado um background que consiste na representação de uma parede de madeira (figura 5).

<div align="center">
  <sub>Figura 4 - Pata desenvolvida em pixel art</sub>  
  <br>
  <img src="../assets/pata.png" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

<div align="center">
  <sub>Figura 5 - Background de Madeira</sub>  
  <br>
  <img src="../assets/wood2.png" width="30%">
  <br><br>
  <sub>Fonte: Imagem em Domínio Público</sub>
</div>


### **4.1.2. Mecânicas**

&nbsp;&nbsp;&nbsp;&nbsp;As principais mecânicas elaboradas no primeiro estágio de desenvolvimento do jogo foram as seguintes:
- A pata se move verticalmente e horizontalmente através da tela e muda de direção sempre que colide com uma “parede”;
- A pata é clicável, reage diminuindo de tamanho a cada clique e aumenta de velocidade ao atingir um tamanho mínimo pré definido;
- O número de cliques bem sucedidos é contabilizado e mostrado na tela;
- O background se adapta de acordo com o tamanho da tela onde o jogo está sendo jogado.

### **4.1.3 Dificuldades Encontradas**

&nbsp;&nbsp;&nbsp;&nbsp;Os principais desafios encontrados durante o desenvolvimento do jogo foram os seguintes:
- Dificuldade em captar precisamente os cliques na tela, o que pode ser um empecilho, haja vista que os toques dos gatos podem ser suaves e não serem captados adequadamente para uma jogabilidade fluída; 
- Dificuldade em configurar a pata para que ela se divida após um número determinado de cliques, o que é uma das mecânicas principais pensadas para o jogo;
- Desconhecimento sobre a real capacidade de nosso jogo de captar a atenção de felinos, de modo que não temos certeza se nossa abordagem irá ser efetiva em primeira análise.

### 4.1.4 Próximos passos

&nbsp;&nbsp;&nbsp;&nbsp;Pensando nas próximas etapas de desenvolvimento do nosso projeto, os próximos passos planejados para serem executados nos próximos Sprints são os seguintes:
- Otimizar a mecânica de capturar toques na tela e testar seu funcionamento em dispositivos móveis;
- Desenvolver uma tela que instrua o tutor a recompensar o gato de acordo com seu sucesso e de maneira adequada;
- Adicionar sons e efeitos visuais envolventes para otimizar a capacidade de engajar os usuários;
- Testar a jogabilidade com um grupo de gatos para coletar feedback para ajustes;
- Desenvolver a tela inicial do jogo, a tela de seleção de fases, bem como as demais funcionalidades para tornar nosso aplicativo completo;
- Adicionar funcionalidades diferenciais para atender o requisto de proporcionar uma experiência inovadora e cativante entre tutor e animal.

## 4.2. Desenvolvimento básico do jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Para a versão básica do jogo em termos de código, focamos em desenvolver as mecânicas e dinâmicas referentes a primeira fase do jogo, no caso, o tutorial, bem como a interface inicial e a tela de fases. Desse modo, as etapas desenvolvidas nessa sprint, bem como os desafios encontrados e a projeção para o futuro do projeto, podem ser definidos pelos tópicos seguintes.

### **4.2.1. Estética**

&nbsp;&nbsp;&nbsp;&nbsp;Para compor a interface incial, a tela de fases e o fundo do tutorial, desenvolvemos em pixel art backgrounds da tela de níveis e do jogo em si para substituir o fundo de madeira(figuras 7 e 8), botões da tela inicial e para cada fase (figura 6). Ademais, foi desenvolvida uma logo para nosso projeto (figura 9).
<div align="center">
  <sub>Figura 6 - Background da Tela de Fases</sub>  
  <br>
  <img src="../assets/background.jpg" width="30%">
  <br><br>
  <sub>Fonte: Freepik [2]</sub>
</div>

<div align="center">
  <sub>Figura 7 - Background do Nível</sub>  
  <br>
  <img src="../assets/backgroundJogo.jpg" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

<div align="center">
  <sub>Figura 8 - Botões</sub>  
  <br>
  <img src="../assets/botoes.png" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

<div align="center">
  <sub>Figura 9 - Logo</sub>  
  <br>
  <img src="../assets/logo.jpg" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

### **4.2.2. Mecânicas**

&nbsp;&nbsp;&nbsp;&nbsp;As principais mecânicas elaboradas no segundo estágio de desenvolvimento do jogo foram as seguintes:
- A pata se move em uma trajetória circular e lenta na fase de tutorial;
- É possível navegar pelas telas e até mesmo acessar as fases 1 e 2 na tela de níveis;
- Além disso, partes singulares de mecânicas de outras fases foram desenvolvidas indidualmente, mas não são funcionais ainda, como um movimento mais fluído para a fase 2.

### **4.2.3 Dificuldades Encontradas**

&nbsp;&nbsp;&nbsp;&nbsp;Os principais desafios encontrados durante o desenvolvimento do jogo foram os seguintes:
- Dificuldade em estruturar teoricamente e no código o funcionamento da instrução de recompensa; 
- Dificuldade em configurar o jogo para que ele se comporte de maneira adequada em dispositivos móveis, como ele se comporta na web;
- Dificuldade em programar um jogo que possa ser testado de maneira adequada com gatos.

### 4.2.4 Próximos passos

&nbsp;&nbsp;&nbsp;&nbsp;Pensando nas próximas etapas de desenvolvimento do nosso projeto, os próximos passos planejados para serem executados nos próximos Sprints são os seguintes:
- Otimizar as fases já em desenvolvimento avançado para que possam ser testadas;
- Desenvolver uma tela que instrua o tutor a recompensar o gato de acordo com seu sucesso e de maneira adequada;
- Adicionar sons e efeitos visuais envolventes para otimizar a capacidade de engajar os usuários;
- Testar a jogabilidade com um grupo de gatos para coletar feedback para ajustes;
- Planejar como iremos implementar as demais mecânicas propostas para nosso projeto.

## 4.3. Desenvolvimento intermediário do jogo 

&nbsp;&nbsp;&nbsp;&nbsp;Para a versão intermediária do jogo em termos de código, focamos em desenvolver funcionalmente as fases 2 e 3, bem como tornar elas apresentáveis, com os novos assests desenvolvidos ou reformulados, junto do tutorial. Além disso, houve uma grande reformulação na forma como nosso código estava estruturado, de modo que agora nossas fases estão contidas em cenas e a transição entre as telas ocorre de forma mais adequada. Dessa forma, as etapas desenvolvidas nesta sprint, os desafios encontrados e a projeção para o futuro do projeto podem ser descritos nos tópicos seguintes.

### **4.3.1. Estética**

&nbsp;&nbsp;&nbsp;&nbsp;Para compor a interface geral do jogo, foram criados, retrabalhados ou escolhidos backgrounds, sendo alguns definitivos e outros provisórios. As imagens a seguir ilustram os elementos visuais implementados nesta sprint:

<div align="center">
  <sub>Figura 10 - Background Retrabalhado</sub>  
  <br>
  <img src="../assets/backgroundJogo.png" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

<div align="center">
  <sub>Figura 11 - Background Provisório da Tela de Níveis</sub>  
  <br>
  <img src="../assets/backgroundTelaNiveis.png" width="30%">
  <br><br>
  <sub>Fonte: 2D Game Assets (2024) [1]</sub>
</div>

<div align="center">
  <sub>Figura 12 - Background Provisório do Menu</sub>  
  <br>
  <img src="../assets/backgroundMenu.png" width="30%">
  <br><br>
  <sub>Fonte: 2D Game Assets (2024) [1]</sub>
</div>

### **4.3.2. Mecânicas**

&nbsp;&nbsp;&nbsp;&nbsp;As principais mecânicas elaboradas nesta etapa do desenvolvimento do jogo foram as seguintes:
- Em todas as fases já prontas, ao atingir o número pré-determinado de toque necessários para destruir o alvo, o jogo instrui o tutor a colocar a recompensa no local onde a pata foi destruída;
- Na fase 1, o alvo se move circularmente, mas agora com um raio um pouco maior para o gato não tocar apenas no meio da tela;
- Na fase 2, o alvo "rebate" nas bordas e apresenta a mesma dinâmica de recompensa após um toque da primeira fase;
- Na fase 3, o alvo se divide em dois ao ser acertado uma vez, e suas cópias devem ser atingidas mais duas vezes para a recopensa ser dada, contudo, essa fase está em revisão pois é possível que os gatos se confundam muito com dois alvos simultâneos;

&nbsp;&nbsp;&nbsp;&nbsp;A figura 13 ilustra como a instrução de recompensa está implementada no jogo:

<div align="center">
  <sub>Figura 13 - Instrução de Recompensa</sub>  
  <br>
  <img src="../assets/recompensa.png" width="30%">
  <br><br>
  <sub>Fonte: Paw Dash (2025)</sub>
</div>


### **4.3.3. Dificuldades Encontradas**

&nbsp;&nbsp;&nbsp;&nbsp;Os principais desafios encontrados durante o desenvolvimento do jogo nesta sprint foram os seguintes:
- Novamente, desenvolver nosso jogo de modo que ele funcione em diferentes dispositivos foi um desafio;
- A estruturação de nosso jogo em classes foi trabalhosa, pois fizemos primeiro de uma maneira diferente, e a adequação para o novo modelo exigiu tempo e grandes mudanças no código;

### **4.3.4 Próximos passos**

&nbsp;&nbsp;&nbsp;&nbsp;Pensando nas próximas etapas de desenvolvimento do projeto, os próximos passos planejados para as próximas sprints são os seguintes:
- Aumentar o tamanho do alvo, pois, ao testarmos nosso jogo, percebemos que nem sempre o gato conseguia visualizar claramente o alvo;
- Desenvolver o alvo em diferentes cores para testarmos quais são mais efetivas;
- Desenvolver mais uma ou duas fases, conforme nossa capacidade, que diferenciem nosso jogo dos demais;
- Garantir que nosso jogo funcione em dispositivos móveis, a principal plataforma escolhida;
- Implementar a trilha sonora do jogo;
- Retrabalhar alguns designs que não agradaram nossa equipe no geral.



## 4.4. Desenvolvimento final do MVP 

&nbsp;&nbsp;&nbsp;&nbsp;Para a versão final do jogo em termos de código, focamos em refinar e otimizar as funcionalidades que já tinhamos, como a fase de tutorial, com base no que agradou o parceiro, bem como tornar elas responsivas. Nesse sentido, descontinuamos fases que continham mecânicas muito complexas, como a divisão de pata e o controle remoto do alvo pelo tutor, e demos enfâse nas fases simples: tutorial, movimento aleátório e obstáculos. Além disso, de forma adicional, trabalhamos na versão inicial de um dispositivo voltado a automatizar a dinâmica de recompensa. Dessa forma, as etapas desenvolvidas nesta sprint, os desafios encontrados e a projeção para o futuro do projeto podem ser descritos nos tópicos seguintes.

### **4.4.1. Estética**

&nbsp;&nbsp;&nbsp;&nbsp;Para incrementar a experiência do nosso jogo, desenvolvemos efeitos sonoros de modo autoral para uma jogabilidade mais completa (para mais detalhes, veja a [seção 3.3.4](#som)). Além disso, construímos uma animação inicial, conforme a figura 14, para nosso jogo, que acrescenta um detalhe de bigode a logo do projeto na tela de menu, fazendo referência ao nome da equipe "Bigode's".

<div align="center">
  <sub>Figura 14 - Bigode na logo</sub>  
  <br>
  <img src="../assets/bigode.png" width="30%">
  <br><br>
  <sub>Fonte: Material produzido pelos autores (2025)</sub>
</div>

### **4.4.2. Mecânicas**

&nbsp;&nbsp;&nbsp;&nbsp;As principais mecânicas elaboradas nesta etapa do desenvolvimento do jogo foram as seguintes:
- Na fase 1, o alvo se move em formato de "infinito", um pouco mais imprevisível que o movimento definido anteriormente;
- Na fase 3, o alvo não pode ser clicado quando está atrás dos obstáculos e rebate em outros elementos além da borda;
- O jogo se adapta conforme o tamanho da tela do dispostivo e apresenta um visual melhor em dispositivos móveis;
- O jogo indica ao usuário girar a tela do dispositivo para a posição mais adequada para o jogo.

&nbsp;&nbsp;&nbsp;&nbsp;Já as mecânicas retiradas do jogo foram as seguintes:
- O alvo se dividia em dois ao ser acertado uma vez, e suas cópias deviam ser atingidas mais duas vezes para a recopensa ser dada;
- Na fase 1, o alvo se movia de maneira circular e muito previsível.

&nbsp;&nbsp;&nbsp;&nbsp;As figuras 15 e 16 ilustram a fase 3 (obstáculos) e o aviso para rotacionar a tela:

<div align="center">
  <sub>Figura 15 - Fase 3</sub>  
  <br>
  <img src="../assets/fase3.png" width="30%">
  <br><br>
  <sub>Fonte: Paw Dash (2025)</sub>
</div>

<div align="center">
  <sub>Figura 16 - Aviso de Rotação</sub>  
  <br>
  <img src="../assets/rotacao.png" width="30%">
  <br><br>
  <sub>Fonte: Paw Dash (2025)</sub>
</div>


### **4.4.3. Dificuldades Encontradas**

&nbsp;&nbsp;&nbsp;&nbsp;Os principais desafios encontrados durante o desenvolvimento do jogo nesta sprint foram os seguintes:
- Entender quais funcionalidades seriam mais atrativas para os gatos sem testes frequentes;
- Tornar o jogo adaptável a todos os tipos de dispositivos;
- Implementar o desafio proposto pelo artefato voltado à matemática;
- Complexidade do código devido a quantidade de incrementos adicionados.

### **4.4.4 Próximos passos**

&nbsp;&nbsp;&nbsp;&nbsp;Pensando nas próximas etapas de desenvolvimento do projeto, os próximos passos planejados para a próxima sprint são os seguintes:
- Testar o jogo tanto com tutores quanto com gatos, a fim de coletar feedbacks e tratar possíveis erros de execução;
- Caso possível, prosseguir com a dinâmica de recompensa automatizada para torná-la parte do MVP;
- Revisar toda a documentação a fim de alinhá-la com a versão final do nosso jogo.


## 4.5. Revisão do MVP 

*Descreva e ilustre aqui o desenvolvimento dos refinamentos e revisões da versão final do jogo, explicando brevemente o que foi entregue em termos de MVP. Utilize prints de tela para ilustrar.*

# <a name="c5"></a>5. Testes

## 5.1. Casos de Teste

&nbsp;&nbsp;&nbsp;&nbsp;O quadro 2 apresenta os casos de teste que foram elaborados para verificar o funcionamento correto do jogo e a integração de suas partes. Cada teste garante que os requisitos fundamentais sejam atendidos e que a experiência de jogo seja fluida e funcional.

<div align="center">
<sub>Quadro 2 - Casos de Teste</sub>
</div>

\# | Pré-condição | Descrição do teste | Pós-condição 
--- | --- | --- | --- 
1 | O jogo deve estar instalado e aberto na tela inicial | Selecionar uma fase e iniciar o jogo | A fase correspondente deve ser carregada corretamente
2 | O jogo deve estar em execução | O jogador deve tocar no alvo corretamente | O alvo deve apresentar o mesmo tempo de resposta ao toque e suavidade de animação (FPS mínimo de 60) em diferentes dispositivos
3 | O jogo deve estar em execução com os gráficos ajustados | Verificar a estética dos elementos gráficos | O contraste e a saturação das cores devem atender ao padrão X para visibilidade felina, garantindo uma experiência visual agradável para o tutor
4 | O jogo deve estar aberto na tela de início | Apertar o botão "play" | O jogo deve abrir a tela de níveis
5 | O jogo deve estar aberto na tela de níveis | Apertar o botão de um nível específico (ex.: "nível 1", "nível 2", "nível 3", "Nível 4", "Nível 5") | A aba correspondente ao nível deve ser carregada corretamente
6 | O jogo deve estar aberto no nível tutorial | Apertar na pata que gira em torno dela mesma | Um texto explicativo e uma marcação vermelha devem aparecer indicando onde o tutor deve colocar o petisco
7 | O jogo deve estar aberto no nível 2 | Apertar na pata que se movimenta pelo espaço de forma aleatória 3 vezes | Um texto explicativo e uma marcação vermelha devem aparecer indicando onde o tutor deve colocar o petisco
8 | O jogo deve estar aberto no nível 3 | Apertar na pata 5 vezes, a pata se move de forma aleatória pelo espaço | Um texto explicativo e uma marcação vermelhas devem aparecer indicando onde o tutor deve colocar o petisco.
9 | O jogo deve estar aberto no nível 4 | Apertar na pata 5 vezes, a pata que se movimenta de forma aleatória pelo espaço | Um texto explicativo e uma marcação vermelhas devem aparecer indicando onde o tutor deve colocar o petisco.
10 | O jogo deve estar aberto no nível 5 | Apertar na pata 5 vezes, a pata que se movimenta de forma aleatória pelo espaço | Um texto explicativo e uma marcação vermelhas devem aparecer indicando onde o tutor deve colocar o petisco.
11 | As patas devem ter se dividido em duas novas patas menores | Apertar duas vezes em cada pata menor | Um texto explicativo e uma marcação vermelha devem aparecer indicando onde o tutor deve colocar o petisco
12 | A recompensa deve ter sido dada | Apertar o botão de "voltar" localizado no canto inferior direito da tela | O jogo deve retornar à tela de níveis


<div align="center">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;Estes testes garantem que o jogo funcione conforme os requisitos estabelecidos e proporcione uma experiência envolvente tanto para os gatos quanto para seus tutores.

## 5.2. Testes de Jogabilidade (Playtests)

### 5.2.1 Registros de Testes do GDD

#### 5.2.1.1 Registro dos Testes de Guerrilha (Parte 1)

*Descreva nesta seção as sessões de teste/entrevista com diferentes jogadores. Registre cada teste conforme o template a seguir.*

<div align="center">
<sub>Quadro 3 - Testes de Guerrilha</sub>
</div>

| Pergunta | Resposta |
| --- | --- |
| O usuário possui um gato de estimação? | Sim |
| Qual modelo de dispositivo foi utilizado para o teste? | Notebook |
| O jogo apresentou uma responsividade adequada ao dispositivo utilizado? | Sim |
| O usuário já possuía experiência com games? | Experiência com games para gatos |
| Como o usuário navegou pelo jogo? | Navegou com facilidade |
| Conseguiu iniciar o jogo e acessar a tela de níveis? | Sim |
| Conseguiu acessar os níveis e jogá-los? | Sim |
| Como o usuário interagiu com os textos explicativos de cada fase? | Não está lendo |
| Como foi a experiência na fase 1? | Excelente |
| Como foi a experiência na fase 2? | Leu os textos e concluiu |
| Como foi a experiência na fase 3? | Boa |
| Como foi a experiência na fase 4? | Muito boa |
| Como foi a experiência na fase 5? | Achou bonito |
| Apresentou dificuldade em alguma das fases? | Não |
| Caso tenha apresentado dificuldades, quais foram? | Não apresentou |
| O jogo é desafiador ou fácil demais para um gato? | Achou bom |
| Não gostou de alguma das fases? | Fase 3 |
| O que poderia melhorar? | Botão de voltar muito chamativo para o gato |
| Experiência com a mecânica de recompensa | Boa |
| Gostou da trilha sonora e efeitos sonoros? | Gostou muito |
| Gostou do visual do jogo? | Sim, achou fofo |
| O que mais gostou? | Trilha sonora |
| Nota para o jogo | 9 |
| Jogaria com seu gato? | Sim |

| Pergunta | Resposta |
| --- | --- |
| O usuário possui um gato de estimação? | Sim |
| Qual modelo de dispositivo foi utilizado para o teste? | Notebook |
| O jogo apresentou uma responsividade adequada ao dispositivo utilizado? | Sim |
| O usuário já possuía experiência com games? | Experiência com games no geral |
| Como o usuário navegou pelo jogo? | Com facilidade, foi direto para as fases |
| Conseguiu iniciar o jogo e acessar a tela de níveis? | Sim |
| Conseguiu acessar os níveis e jogá-los? | Sim |
| Como o usuário interagiu com os textos explicativos de cada fase? | Não leu |
| Como foi a experiência na fase 1? | Excelente |
| Como foi a experiência na fase 2? | Ótima |
| Como foi a experiência na fase 3? | Repetitiva |
| Como foi a experiência na fase 4? | Leu os textos e concluiu |
| Como foi a experiência na fase 5? | Mais ou menos repetitiva |
| Apresentou dificuldade em alguma das fases? | Não |
| Caso tenha apresentado dificuldades, quais foram? | Não apresentou |
| O jogo é desafiador ou fácil demais para um gato? | Normal |
| Não gostou de alguma das fases? | Fase 4 |
| O que poderia melhorar? | Botão de voltar para o menu. Achou repetitivo |
| Experiência com a mecânica de recompensa | Ok |
| Gostou da trilha sonora e efeitos sonoros? | Gostou |
| Gostou do visual do jogo? | Gostou, mas falta refinamento |
| O que mais gostou? | Do design do jogo |
| Nota para o jogo | 9 |
| Jogaria com seu gato? | Sim |

| Pergunta | Resposta |
| --- | --- |
| O usuário possui um gato de estimação? | Não |
| Qual modelo de dispositivo foi utilizado para o teste? | Notebook |
| O jogo apresentou uma responsividade adequada ao dispositivo utilizado? | Sim |
| O usuário já possuía experiência com games? | Experiência com games no geral |
| Como o usuário navegou pelo jogo? | Foi direto para as fases. Depois abriu o menu |
| Conseguiu iniciar o jogo e acessar a tela de níveis? | Sim |
| Conseguiu acessar os níveis e jogá-los? | Sim |
| Como o usuário interagiu com os textos explicativos de cada fase? | Leu todos |
| Como foi a experiência na fase 1? | Achou muito demorada |
| Como foi a experiência na fase 2? | Amou |
| Como foi a experiência na fase 3? | Som dessincronizado |
| Como foi a experiência na fase 4? | Repetitiva |
| Como foi a experiência na fase 5? | Gostou muito |
| Apresentou dificuldade em alguma das fases? | Não |
| Caso tenha apresentado dificuldades, quais foram? | Não apresentou |
| O jogo é desafiador ou fácil demais para um gato? | Achou fácil |
| Não gostou de alguma das fases? | Fase 4 |
| O que poderia melhorar? | Contador pequeno e escondido, falta tela de fim, som dessincronizado, indicar mudanças nas fases, botão de voltar para o menu |
| Experiência com a mecânica de recompensa | Entendeu |
| Gostou da trilha sonora e efeitos sonoros? | Gostou muito |
| Gostou do visual do jogo? | Gostou, mas muito parecido |
| O que mais gostou? | Trilha sonora |
| Nota para o jogo | 8 |
| Jogaria com seu gato? | Sim |

<div align="center">
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

#### 5.2.1.2 Registro dos Testes com Público-Alvo (Parte 2)

*Conteúdo não disponível. Esta seção deve ser preenchida com registros de sessões de teste realizadas com o público-alvo final do jogo (tutores com gatos).*

#### 5.2.1.3 Análise das Respostas e Principais Conclusões

- Todos os usuários conseguiram navegar com facilidade e acessar os níveis.
- A responsividade foi adequada em todos os dispositivos testados (notebooks).
- A trilha sonora foi um dos elementos mais elogiados pelos participantes.
- O botão de "voltar ao menu" chamou atenção indesejada dos gatos ou causou distração.
- A fase 3 e a fase 4 foram mencionadas como repetitivas por mais de um usuário.
- A mecânica de recompensa foi compreendida e bem aceita.
- Algumas sugestões incluíram melhorias na clareza dos elementos visuais e sincronização de áudio.
- Poucos usuários leram os textos explicativos das fases.

#### 5.2.2 Melhorias

Com base nos testes realizados, foram definidas as seguintes melhorias:

- **Botão de voltar ao menu:** Reduzir o destaque visual ou reposicionar para evitar distrações ao gato.
- **Textos explicativos:** Reformular ou buscar alternativas visuais (como ícones ou tutoriais animados) para maior engajamento.
- **Fases repetitivas:** Introduzir maior variação de padrões de movimento e recompensas para evitar monotonia.
- **Contador e feedback visual:** Aumentar o tamanho e a visibilidade dos elementos informativos na tela.
- **Trilha sonora e efeitos:** Ajustar sincronização do som com as ações nas fases.
- **Tela de encerramento:** Adicionar uma tela final clara ao fim do jogo ou das fases.
- **Responsividade:** Embora o jogo esteja funcional em notebooks, será importante testar e ajustar em tablets, que são o foco do público-alvo.


# <a name="c6"></a>6. Conclusões e trabalhos futuros 

## 6. Conclusões e Trabalhos Futuros

### 6.1. Conclusões

O projeto **Paw Dash** atingiu com sucesso os objetivos definidos na seção 1. A proposta de criar um jogo interativo para gatos foi realizada por meio de um MVP funcional, com foco em estímulo físico/mental dos felinos e interação com seus tutores.

**Pontos fortes:**

- Jogabilidade adaptada à percepção e comportamento dos gatos.
- Interface intuitiva para tutores, com instruções claras.
- Sistema de recompensa bem integrado.
- Design visual e sonoro elogiado nos testes.
- Código organizado, facilitando manutenção e expansão.

**Pontos a melhorar:**

- Algumas fases foram percebidas como repetitivas.
- Textos explicativos ignorados por parte dos usuários.
- Botão de "voltar" atraiu a atenção dos gatos.
- Alguns bugs visuais e sonoros pontuais.
- Ausência de tela de conclusão após a fase.



### 6.2. Trabalhos Futuros

#### Melhorias baseadas em testes

| Problema identificado | Ação sugerida |
|-----------------------|----------------|
| Textos não lidos | Substituir por ícones, sons e animações mais intuitivas |
| Botão "voltar" chamativo | Reposicionar e aplicar menor destaque visual |
| Fases repetitivas | Criar novas dinâmicas que mantenham a simplicidade |
| Sem tela de conclusão | Incluir feedback visual ao fim da fase para guiar a recompensa |
| Falta de progresso visível | Adicionar indicador de progresso ou mapa de níveis |

#### Funcionalidades futuras

- Customização de alvos (cor, forma, tamanho).
- Modo noturno com brilho reduzido.
- Registro de desempenho (tempo de interação, número de toques).
- Sistema simples de conquistas para os tutores.
- Integração com dispositivos de recompensa automática.
- Reexplorar modo controlado pelo tutor.

#### Roadmap sugerido

| Sprint | Objetivo |
|--------|----------|
| Sprint 1 | Refatoração de UI/UX e substituição de instruções por elementos visuais |
| Sprint 2 | Desenvolvimento de novas fases com maior diversidade |
| Sprint 3 | Ampliação dos testes com mais gatos e coleta estruturada de feedback |
| Sprint 4 | Prototipação e testes da recompensa automática |
| Sprint 5 | Publicação em loja de apps para testes beta |


# <a name="c7"></a>7. Referências 

[1] 2D GAME ASSETS. Forest and Trees - Free Pixel Backgrounds. Dribbble, 2024. Disponível em: https://dribbble.com/shots/24653940-Forest-and-Trees-Free-Pixel-Backgrounds. Acesso em: 14 mar. 2025.

[2] BRONWENSTUDIO. Fundo de paisagem rural de pixel art. 2024. Disponível em: https://br.freepik.com/vetores-gratis/fundo-de-paisagem-rural-de-pixel-art_49685499.htm. Acesso em: 23 fev. 2025.

[3] DOOGS PET. Como funciona o mercado de adestramento de cães no Brasil. Disponível em: https://doogspet.com/dicas/como-funciona-o-mercado-de-adestramento-de-caes-no-brasil/. Acesso em: 27 fev. 2025.

[4] FERRAMENTAS DE QUALIDADE. Matriz de Riscos (Matriz de Probabilidade e Impacto). Disponível em: https://ferramentasdaqualidade.org/matriz-de-riscos-matriz-de-probabilidade-e-impacto/. Acesso em: 21 mar. 2025.

[5] MEREO. Missão, visão e valores: o que é, como definir e exemplos. Disponível em: https://mereo.com/blog/missao-visao-e-valores/. Acesso em: 25 fev. 2025.

[6] O GLOBO. Petz compra franquia do Dr. Pet e projeta 50 novas lojas para 2022. Disponível em: https://oglobo.globo.com/economia/negocios/petz-compra-franquia-do-dr-pet-projeta-50-novas-lojas-para-2022-25270397. Acesso em: 27 fev. 2025.

[7] ROCK CONTENT. Como fazer uma análise SWOT. Disponível em: https://rockcontent.com/br/blog/como-fazer-uma-analise-swot/. Acesso em: 27 fev. 2025.

[8] ROSSI, Alexandre. Instagram oficial. Disponível em: https://www.instagram.com/alexandrerossi_oficial/?hl=en. Acesso em: 12 fev. 2025.

[9] ROSSI, Alexandre. Sobre nós. Disponível em: https://doutorpet.com/sobre-nos/. Acesso em: 12 fev. 2025.

[10] SALESFORCE. As 5 forças de Porter: o que são e como usá-las? Disponível em: https://www.salesforce.com/br/blog/5-forcas-de-porter/. Acesso em: 25 fev. 2025.

[11] TERABLOG. Canvas Proposta de Valor: Para que serve e como preencher. Disponível em: https://blog.somostera.com/product-management/canvas-de-proposta-de-valor. Acesso em: 13 mar. 2025.

# <a name="c8"></a>Anexos

*Inclua aqui quaisquer complementos para seu projeto, como diagramas, imagens, Quadros etc. Organize em sub-tópicos utilizando headings menores (use ## ou ### para isso)*
