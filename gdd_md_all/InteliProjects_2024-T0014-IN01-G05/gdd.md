<img src="../assets/logointeli.png">


# GDD - Game Design Document - Módulo 1 - Inteli



## Metamorfose

#### [Davi Abreu da Silveira](https://www.linkedin.com/in/davi-abreu-da-silveira-706323290/)
#### [Fernando Soares de Oliveira](https://www.linkedin.com/in/fernando-soares-de-oliveira-081092292/)
#### [Leonardo Ogata Pedrosa](https://www.linkedin.com/in/leonardo-ogata-983b032b5/)
#### [Mateus Martins Silveira Pretti](https://www.linkedin.com/in/mateus-martins-pretti-03ba952b4/)
#### [Murilo Couto Oliveira](https://www.linkedin.com/in/murilo-couto-oliveira/)
#### [Renan Sabino dos Reis](https://www.linkedin.com/in/renan-reis-483a10289/)
#### [Vinicius Gomes Ibiapina](https://www.linkedin.com/in/vinicius-ibiapina-90407328b/)




## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Jogo](#c2)

[3. Game Design](#c3)

[4. Desenvolvimento do jogo](#c4)

[5. Casos de Teste](#c5)

[6. Conclusões e trabalhos futuros](#c6)

[7. Referências](#c7)

[Anexos](#c8)

<br>


# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto


### 1.1.1. Contexto da indústria

&nbsp;&nbsp;&nbsp;&nbsp; A contextualização da indústria é fundamental para as empresas entenderem o ambiente em que operam, incluindo análise de tendências de mercado, concorrência, avanços tecnológicos e condições econômicas. Para a Meta, anteriormente conhecida como Facebook, essa compreensão é crucial, pois sua operação eficaz e de inovação contínua depende de uma rede diversificada de fornecedores, parceiros e colaboradores.

&nbsp;&nbsp;&nbsp;&nbsp; Os fornecedores desempenham um papel essencial no dia a dia da Meta, fornecendo desde hardware e software até serviços de infraestrutura de data center. Além disso, parcerias com empresas de publicidade, desenvolvedores de aplicativos e organizações sem fins lucrativos contribuem significativamente para a operação e a imagem da marca da Meta.

&nbsp;&nbsp;&nbsp;&nbsp; No entanto, a Meta enfrenta uma concorrência acirrada em diversos mercados globais. Enquanto o WeChat domina o mercado chinês devido a restrições governamentais, o Line é uma força no Japão. Nos Estados Unidos, concorrentes como Snapchat, Telegram, Discord e TikTok desafiam a Meta, demonstrando a dinâmica e competitividade do setor de tecnologia e comunicação digital [1].

&nbsp;&nbsp;&nbsp;&nbsp; A Meta, está atenta às tendências globais que moldam o cenário tecnológico e empresarial. A volatilidade geopolítica, com conflitos regionais e demandas sociais crescentes, define a narrativa de 2024. Além disso, a convergência de realidades virtuais e físicas no metaverso está transformando indústrias e redefinindo interações com a tecnologia. Energias sustentáveis, como as renováveis, ultrapassarão um terço da geração global de energia, marcando um ponto de virada na luta contra as mudanças climáticas. A saúde digital, cidades inteligentes e blockchain também são tendências significativas. Esses fatores moldarão o futuro da Meta e de outras empresas, impulsionando a inovação e a adaptação contínua. Além disso, a empresa está comprometida com a inclusão e a diversidade no mercado de trabalho [2], visando contribuir positivamente para o avanço tecnológico e o bem-estar das pessoas [3]. Essa abordagem reflete a estratégia da Meta em relação à inovação, expansão de mercado e diversidade no local de trabalho.

### 1.1.2. 5 Forças de Porter

&nbsp;&nbsp;&nbsp;&nbsp; No contexto do jogo para a Meta, a análise das 5 forças de Porter revela uma dinâmica complexa e desafiadora. A ameaça de produtos substitutos é alta, dado o vasto leque de opções de entretenimento disponíveis para os consumidores, desde plataformas de vídeos curtos até filmes e séries. A ameaça de entrada de novos concorrentes também é elevada, dada a magnitude do mercado de jogos, onde até mesmo empresas menores podem ganhar espaço com produções indie de qualidade. Por outro lado, o poder de negociação dos clientes é considerado baixo, impulsionado pela mentalidade de exclusividade e pela disposição dos consumidores a pagar por experiências únicas. No entanto, o poder de negociação dos fornecedores é alto devido à limitação de opções e às barreiras significativas à entrada no mercado de hardware. Por fim, a rivalidade entre os concorrentes é intensa, com grandes empresas investindo pesadamente em inovação e tecnologia para se destacarem, o que aumenta a competição e a necessidade de acompanhar o ritmo do mercado (Figura 1).
<br></br>
### Ameaça de produtos substitutos - Alta

O consumidor possui uma gama de possibilidades para escolher seu entretenimento. Por exemplo: plataforma de vídeos curtos (reels, tiktok e shorts), filmes, séries e atividades de lazer em geral.

### Ameaça de entrada de novos concorrentes - Alta

Apesar da existência de grandes empresas estabelecidas e queridas nesse mercado, com rivalidades icônicas, como Sony e Microsoft, o mercado de jogos é tão grandioso que sempre pode abrigar mais uma empresa. Então, muitas produtoras menores "arriscam" o pouco capital que têm em jogos que ficam conhecidos como jogos indie, e muitas vezes, devido ao trabalho bem feito e genial, ganham espaço nesse enorme mercado. São exemplos disso: Celeste, Undertale e Hollow Knight.

### Poder de negociação dos clientes - Baixo

Nos jogos e aplicativos da Meta, o poder de negociação dos clientes, quando baixo, é moldado pela necessidade de funcionalidades específicas, pela busca por integração social e pertencimento, pela estratégia de exclusividade e escassez, e pelo efeito rede e dependência. A dependência dos usuários da plataforma e a oferta de itens exclusivos por tempo limitado diminuem sua capacidade de negociar. 

### Poder de negociação dos fornecedores - Alto

Com um número limitado de empresas que dominam o setor de hardware (como Intel, Microsoft, Nvidea), os fabricantes têm menos opções ao escolher seus fornecedores, o que fortalece a posição destes no processo de negociação, aumentando a barganha. Além disso, as barreiras à entrada para novas empresas nesse mercado são significativas. A complexidade tecnológica, os altos custos de pesquisa e desenvolvimento, bem como a necessidade de infraestrutura especializada, dificultam a entrada de novos concorrentes.  

### Rivalidade entre os concorrentes - Alta

Existem muitas empresas no mercado, tanto na produção de jogos, sendo muitas delas grandes como: EA Esports, Ubisoft, Blizzard, Rockstar Gamer, Valve. Além disso, em um mercado que movimenta cerca de $200 bilhões, os investimentos dessas "baleias" em seus jogos é sempre muito alto, havendo com frequência inovações e descobertas tecnológicas, fazendo com que as outras empresas tenham de correr atrás desse prejuízo.

<div align="center">
<sub>Figura 1 - Análise 5 Forças de Porter</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/5_forças_de_porter.jpg">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### 1.1.3. Análise SWOT

&nbsp;&nbsp;&nbsp;&nbsp; A análise SWOT, também conhecida como matriz FOFA, avalia fatores internos e externos de uma empresa ou projeto. Ela divide-se em quatro componentes: Forças, Fraquezas, Oportunidades e Ameaças. As forças diferenciam a organização, gerando valor, enquanto as fraquezas limitam o potencial. A análise SWOT permite estratégias eficazes e antecipação de desafios no contexto empresarial e tecnológico (Figura 2). No contexto da Meta, conduzimos uma extensa pesquisa, culminando nos seguintes resultados:

## FORÇAS (S): 
### Grande base de usuários

&nbsp;&nbsp;&nbsp;&nbsp; A Meta possui uma enorme base de usuários que usam suas redes sociais. No Brasil, cerca de 93,4% da população com idade entre 16 e 64 anos utilizam o WhatsApp, plataforma adquirida pela Meta em 2014, equivalendo a aproximadamente 169 milhões de usuários. Além disso, o aplicativo contou com mais de 541 milhões de downloads, sendo o quarto 'app' mais baixado do mundo. No final do ano de 2023, a equipe da Meta tornou pública a informação de que o Facebook contava diariamente com cerca de 2,11 bilhões de usuários ativos.

### Grande capacidade de inovação

&nbsp;&nbsp;&nbsp;&nbsp; A Meta, antes mesmo de ser Meta, já conseguiu revolucionar a maneira como enxergávamos as redes sociais. Antes do Facebook, as redes sociais tinham um conceito muito diferente do que imaginamos hoje. Recentemente nos foi apresentado o Metaverso, sem dúvidas a maior inovação da empresa desde então.

### Vantagem competitiva

&nbsp;&nbsp;&nbsp;&nbsp; A Meta oferece uma variedade de serviços integrados que atendem às diferentes necessidades e preferências dos usuários. Uma mesma empresa se tornou capaz de oferecer: redes sociais, mensagens, realidade virtual e aumentada, negócios e publicidade. Alguns desses elementos, como as redes sociais e os negócios e publicidade, são apresentados em conjunto. 

### Forte presença no mercado publicitário

&nbsp;&nbsp;&nbsp;&nbsp; A Meta tem um forte nome no mercado publicitário. Espera-se que o Instagram seja responsável por movimentar cerca de 9,1 bilhões de dólares em anúncios no ano de 2024. Sua acessibilidade e alcance permitem que uma variedade de marcas e personas anuncie em suas plataformas.

## FRAQUEZAS:
### Problemas legais

&nbsp;&nbsp;&nbsp;&nbsp; A Meta enfrenta diversos problemas legais, regulatórios e éticos em diversos países, relacionados à privacidade, segurança, concorrência, conteúdo nocivo, desinformação e manipulação de dados dos usuários. Em dezembro de 2022 a Meta concordou em pagar cerca de US$ 725 milhões para encerrar um processo que acusava a empresa de permitir que a Cambridge Analytica e outras empresas de análise de dados tivessem acesso aos dados privados de seus usuários.

### Má reputação

&nbsp;&nbsp;&nbsp;&nbsp; Para muitos usuários a Meta é uma empresa que abusa de seu poder de mercado. Grande parte dessa má reputação da empresa é proveniente dos problemas legais, citados anteriormente, mas recentemente o seu algoritmo passou a também ser alvo de críticas. A Meta foi acusada de fornecer um algoritmo nocivo para a saúde mental de seus usuários, divulgando de maneira desproporcional a padronização da beleza.

### Desafios na moderação de seus anúncios

&nbsp;&nbsp;&nbsp;&nbsp; Com o sucesso crescente do tráfego pago, as redes sociais se mostraram uma enorme oportunidade para aumentar as vendas. No entanto, essa visibilidade também se mostrou uma grande oportunidade para golpistas. A moderação dos anúncios do Instagram parece não funcionar, e cada vez mais os anúncios maliciosos tomam conta das redes sociais da Meta. Um grande exemplo disso são as casas de apostas virtuais, que, embora ainda sejam contra as leis brasileiras, continuam operando a todo vapor com milhares de promessas falsas.

## AMEAÇAS:
### Maior regulamentação e fiscalização

&nbsp;&nbsp;&nbsp;&nbsp; Os aplicativos da Meta possuem um enorme banco de dados com inúmeras informações de seus usuários. Essas informações são sensíveis e alguns governos podem enxergar isso como uma ameaça aos seus cidadãos. Em caso de qualquer alteração nessas regulamentações, as plataformas da Meta podem sofrer restrições e deixarem de circular em determinadas regiões até que adequem suas diretrizes para a região.

### Forte concorrência

&nbsp;&nbsp;&nbsp;&nbsp; Embora tenha plataformas consolidadas no mercado, a concorrência aumenta a cada dia e novas tendências começam a surgir. É importante mencionar que tudo aquilo que rouba a atenção do usuário pode ser uma concorrente para as redes sociais, em geral, mas algo ainda mais perigoso parece se aproximar: novas tendências de redes sociais. Em 2020, a Meta viu suas plataformas serem deixadas de lado, enquanto milhares de novos usuários passavam a gastar seus tempos de ócio no TikTok.

### Boicotes

&nbsp;&nbsp;&nbsp;&nbsp; Diante desses escândalos de privacidade, a Meta pode virar alvo de boicote e perder grande parte de seus usuários para outras plataformas. Mas há algo ainda mais suscetível a boicotes do que essa questão de privacidade: o Metaverso. Algo muito semelhante vem acontecendo recentemente com as inteligências artificiais de texto e imagens, que foram alvo de diversos protestos importantes.  

## OPORTUNIDADES: 
### Educação online e trabalho remoto

&nbsp;&nbsp;&nbsp;&nbsp; Com o aumento do ensino à distância e do trabalho remoto, a Meta poderia explorar oportunidades para desenvolver ou adquirir plataformas de aprendizado online e ferramentas de colaboração remota, alinhando as mudanças nas tendências de trabalho e educação com suas ofertas de produtos. Vale mencionar que, desde o surto global de COVID-19 em meados de 2020, o mundo passou por uma enorme revolução. Mesmo com as salas de aula presenciais novamente cheias de alunos, muitos professores continuam utilizando plataformas online para a organização de suas tarefas. 

### Mercados emergentes

&nbsp;&nbsp;&nbsp;&nbsp; A Meta pode explorar oportunidades de crescimento em mercados emergentes, onde o acesso à internet ainda está em estágios iniciais e, consequentemente, a adoção das redes sociais está crescendo. Implementar os idiomas desses países pode significar uma disparada à frente dos concorrentes, e captar esses novos usuários pode impulsionar de significativamente a base de usuários da empresa.

### Expandir suas plataformas

&nbsp;&nbsp;&nbsp;&nbsp; Com tantos novos segmentos surgindo, a Meta poderia expandir suas marcas já consolidadas no mercado e integrar alguns desses segmentos dentro de suas plataformas. Por exemplo: o Tinder é um aplicativo muito forte de namoro, por que não, integrar algo semelhante ao Facebook? 

### Parcerias

&nbsp;&nbsp;&nbsp;&nbsp; Com tanta expectativa no futuro do Metaverso, a Meta pode propor parcerias com empresas de diferentes segmentos e trazê-las não apenas para o Metaverso, mas também integrá-las às demais plataformas da Meta. Essas colaborações estratégicas com outras empresas podem abrir novas oportunidades para a Meta. Parcerias em áreas como entretenimento, educação ou saúde digital podem ampliar seu alcance.

<div align="center">
<sub>Figura 2 - Análise SWOT do Projeto</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/SWOT.png">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### 1.1.4. Descrição da Solução Desenvolvida

### Problema a ser resolvido
&nbsp;&nbsp;&nbsp;&nbsp; Há necessidade de criar uma ferramenta que oriente e facilite a compreensão de todos os passos da jornada de contratação de um fornecedor para colaboradores META. Desde o Sourcing (Primeiro Contato) até o Payment (Pagamento). Esse problema a ser resolvido vem por parte da META, e nós G05 da T14 trabalharemos para solução disso por meio de um jogo.

### Dados disponíveis
&nbsp;&nbsp;&nbsp;&nbsp; Como dados disponíveis temos as tecnologias que usamos no desenvolvimento do game: CSS; HTML5; JS; GitHub; VS Code; Phaser. Essas tecnologias são as quais a META e o Inteli definiram para que utilizássemos para a confecção do projeto.

### Macro do game
&nbsp;&nbsp;&nbsp;&nbsp; O jogo é baseado em decisões e também proporciona um senso de progressão rápida à medida que o jogador aumenta seu conhecimento sobre o processo de contratação em cada etapa. Não haverá utilização de banco de dados, e todo o conteúdo estará restrito ao grupo e à Meta. A duração estimada do jogo é entre 20 e 30 minutos. Quanto à compatibilidade, estará disponível para uso em dispositivos móveis e computadores, com versões em inglês e português. Além disso, recorreremos ao uso de recursos da Meta no jogo, como a paleta de cores de suas redes sociais, referências a aplicativos da empresa, pessoas envolvidas no processo de contratação e o local de trabalho dos funcionários (público-alvo), entre outros elementos.

### Solução proposta 
&nbsp;&nbsp;&nbsp;&nbsp; Desenvolver um jogo que simula o processo de seleção e contratação de fornecedores para a Meta, passando por cada etapa do processo, explicando oque e como deve ser feita a busca e a contratação de um parceiro, com base nos valores fundamentais da Meta. O objetivo é orientar os funcionários através desse processo de forma dinâmica, simplificada e ludificada, proporcionando uma experiência imersiva e educativa.

### Como a solução proposta deve ser utilizada?
&nbsp;&nbsp;&nbsp;&nbsp; Os funcionários responsáveis pela contratação de novos fornecedores deverão utilizar o jogo como uma ferramenta de orientação sobre o procedimento de contratação desses parceiros, visando desmistificar a concepção de que se trata de um processo complexo e de difícil  aprendizagem. Durante o jogo, os colaboradores serão conduzidos e fornecidos com dicas sobre como devem lidar com esse processo, proporcionando, assim, aprendizado simples desse processo.

### Benefícios esperados:
&nbsp;&nbsp;&nbsp;&nbsp; Os benefícios esperados são o aumento do engajamento dos funcionários com a empresa e seu funcionamento, além disso, facilitação do entendimento do processo de contratação. Também esperamos que por meio desse jogo aumente as oportunidades de contratação de fornecedores sob o contexto de diversidade. Portanto, o jogo na nossa concepção deve poder ensinar funcionários sobre o processo de contratação de uma forma gamificada e que não deixe dúvidas.

### Qual será o critério de sucesso?
&nbsp;&nbsp;&nbsp;&nbsp; Os critérios para definição de sucesso do nosso projeto será definido a partir dos feedbacks fornecidos pelos representantes da Meta e da equipe de profissionais do INTELI, além disso, atender ao que foi proposto e sanar quaisquer dúvidas dos funcionários a respeito do processo de contratação de fornecedores. Junto a isso gostaríamos de ver a maior promoção de oportunidades a fornecedores diversos dentro da META, o que definiria de fato o sucesso do nosso projeto.

### 1.1.5. Proposta de Valor

&nbsp;&nbsp;&nbsp;&nbsp; O Value Proposition Canvas é uma ferramenta de marketing que ajuda a definir perfis de clientes, propostas de valor e ajustar a oferta de produtos com base nas necessidades dos clientes. O Canvas é dividido em dois blocos: Perfil do Cliente e Proposta de Valor. O bloco de Perfil do Cliente ajuda a identificar os trabalhos que o cliente precisa realizar, as dores que ele enfrenta e os ganhos que ele espera obter. O bloco de Proposta de Valor ajuda a definir os componentes mais importantes da oferta, como aliviar a dor e criar ganhos para os clientes[4].

<div align="center">
<sub>Figura 3 - Canvas da Proposta de Valor do Projeto</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/92562887-e51f-4ab1-82b4-89572ead5159">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### Contextualização:

&nbsp;&nbsp;&nbsp;&nbsp; O Value Proposition Canvas é essencial para orientar o desenvolvimento de produtos e estratégias de negócios, garantindo que atendam às necessidades dos clientes. Seus benefícios incluem:

### Planejamento Focado
&nbsp;&nbsp;&nbsp;&nbsp; Ajuda a manter o foco nos valores essenciais durante o desenvolvimento do produto, evitando que ele não atenda às expectativas do cliente.

### Melhora do Alcance do Marketing
&nbsp;&nbsp;&nbsp;&nbsp; Identifica as necessidades do cliente e desenvolve um plano de ação para atendê-las, facilitando a promoção e a propaganda, aumentando o reconhecimento da marca.

### Forte Envolvimento do Cliente
&nbsp;&nbsp;&nbsp;&nbsp; Concentra-se na identificação e atendimento das necessidades dos clientes, promovendo maior satisfação e engajamento com a marca.

### Praticidade e Simplicidade
&nbsp;&nbsp;&nbsp;&nbsp; Oferece uma visão simplificada da estratégia de negócios e do desempenho do produto, facilitando o entendimento e a análise.
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp; O Canvas é dividido em duas partes principais: o perfil do cliente, representado por um círculo dividido em trabalhos a serem feitos, dores e ganhos; e o mapa da proposta de valor, representado por um quadrado também dividido em três partes, relacionadas às necessidades do cliente (Figura 3).

### 1.1.6. Matriz de Riscos

&nbsp;&nbsp;&nbsp;&nbsp; Uma matriz de riscos é uma ferramenta fundamental utilizada na gestão de projetos e no gerenciamento de riscos. Ela é uma representação visual que ajuda a identificar, classificar e avaliar os riscos que um projeto pode enfrentar. Geralmente, uma matriz de riscos organiza os riscos de acordo com sua probabilidade de ocorrência e seu impacto potencial, criando assim uma visão clara dos principais desafios que podem afetar o sucesso do projeto. Essa ferramenta permite que as equipes de projeto priorizem seus esforços de redução e desenvolvam estratégias para lidar eficazmente com os riscos identificados. Em resumo, a matriz de riscos é uma peça central na tomada de decisões informadas e na garantia de que os projetos estejam preparados para enfrentar e superar obstáculos potenciais (Figura 4).

<div align="center">
<sub>Figura 4 - Matriz de Risco do Projeto</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Matrizrisco.png">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp; Conforme a avaliação dos riscos com a ferramenta da Matriz, segue a análise da vertente e o plano de ação para os mesmos:

### Problemas Técnicos
  
&nbsp;&nbsp;&nbsp;&nbsp; Os problemas técnicos englobam diversos elementos, tais como, queda de energia local, internet de má qualidade, entre outras. Esta problemática com certeza atrasaria os planos do projeto, mas não é de grande ameaça, pois geralmente essas vertentes se resolvem em pouco tempo. A resolução da ameaça seria o foco dos outros membros do grupo no processo onde o outro colaborador do time está incapacitado de agir.


### Tempo não suficiente

&nbsp;&nbsp;&nbsp;&nbsp; Visto que o projeto e o aprendizado dos alunos caminham juntos, é possível notar que o tempo dado pela faculdade deve ser manipulado eficientemente, e que em meio a tensão da entrega do produto, pode ser que ocorra uma falta de tempo para um desenvolvimento melhor do projeto. O passo tomado para que essa problemática seja anulada, deve ser o planejamento prévio do plano de ação do grupo em visa do desenvolvimento do projeto.

### Problemas com saúde

&nbsp;&nbsp;&nbsp;&nbsp; No avanço do tempo é comum o acontecimento de problemas envolvendo a saúde, mas assim como foi classificado, esta vertente se classifica como uma ameaça moderada, pois assim como os problemas técnicos a solução seria o "acobertamento" do membro afetado.

### Desviamento dos Ideais da empresa

&nbsp;&nbsp;&nbsp;&nbsp; Conforme o avanço do desenvolvimento do jogo, é possível ocorrer algum desvio dos ideais da Meta em algum elemento no game. Podemos tomar como exemplo, uma competitividade desnecessária ou, como citado no encontro do dia 09/02, se adicionarmos alguma figura da Meta no jogo e passarmos a ele algum conceito diferente do que a empresa quer. O movimento que podemos tomar quanto a isso, seria a constante comunicação com os colaboradores, para acompanharem as nossas ideias conforme a adição de elementos no jogo.

### Erro na comunicação

&nbsp;&nbsp;&nbsp;&nbsp; Visto que ao separar tarefas aos membros do grupo, deve ser cotidiano que no desenvolvimento e conclusão desses serviços os contribuidores notifiquem a equipe o andamento do trabalho. Nesse sentido, com a falta de comunicação pode gerar diversas vertentes, tais quais como a não conclusão dessas tarefas ou até mesmo a conclusão repetida da mesma. Portanto, é necessário que os contribuidores comuniquem ao grupo o andamento dos afazeres por ferramentas como Slack ou as Dailys no início das aulas.

### Erro no código

&nbsp;&nbsp;&nbsp;&nbsp; Ponderando novamente o ponto de que a equipe está em processo de aprendizado, há chances altas de ocorrer erros nos códigos que podem danificar a jogabilidade e experiência do usuário no jogo. O plano de ação é novamente comunicar aos integrantes quando reportarem erros e o acompanhamento da solução dessa vertente por partes de todos os membros, para os mesmos aprenderem com os erros.

### Erro na Matriz de Risco

&nbsp;&nbsp;&nbsp;&nbsp; Deve ser ponderado a chance da matriz de riscos não considerar perfeitamente todos os riscos do projeto e, dessa forma, não avaliar os riscos de maneira correta. A linha de ação a ser tomada é atualizar sempre que possível a matriz, e tentar entender todas as partes integrantes do grupo com a constante comunicação de possíveis vertentes.

### Acontecimento de Bugs 

&nbsp;&nbsp;&nbsp;&nbsp; Visto o andar do projeto, os acontecimentos de bugs acontecem com muita constância, uma vez que os integrantes estão em processo de aprendizagem. Nessa perspectiva, os bugs influenciam na experiência do usuário e na jogabilidade do jogo, portanto os membros do grupo devem tomar medidas para que isso pare de ocorrer, tais como o teste constante do jogo e o reporte ao se notar um bug.

## 1.2. Requisitos do Projeto

&nbsp;&nbsp;&nbsp;&nbsp; Os requisitos de um projeto são as especificações e condições necessárias para o projeto ser concebido, desenvolvido e implementado com sucesso. Eles formam a base para o entendimento mútuo entre as partes envolvidas no projeto, incluindo clientes, equipe de desenvolvimento e demais stakeholders. Os requisitos são essenciais para guiar todas as fases do ciclo de vida do projeto, desde a sua concepção até a entrega final.

<div align="center">
<sub>Quadro 01 - Requisito Funcional 01</sub>
</div>

Número | Requisito
--- | ---
1 | O jogo deve ser desenvolvido para plataformas mobile
2 | O jogo deve possuir uma tela de pause para o jogador poder acessar as configurações do jogo
3 | O jogo deve apresentar interações fora da história principal para deixar o jogador imerso na história
4 | O jogo possuirá diálogos que guiem o jogador pelo processo de contratação de um novo fornecedor, explicando os valores que a Meta possui
5 | O jogo deve possuir músicas que ambientem o jogador dependendo do cenário e situação
6 | O jogo deve possuir diferentes ferramentas englobem o processo de contratação
7 | O jogo deve possuir uma forma de o player compartilhar suas conquistas no jogo, engajando e incentivando outros colaboradores a jogarem
8 | O jogo deve ter uma mecânica de progressão para mostrar ao jogador sua evolução
9 | O jogo deve ter a tradução para inglês


<div align="center">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## 1.3. Público-alvo do Projeto

&nbsp;&nbsp;&nbsp;&nbsp; O público alvo do projeto se refere a quem ele é destinado, o “target” do projeto. Sendo assim, como nosso atual parceiro é a Meta, pensando macroscopicamente o projeto se dirige aos funcionários de tal empresa, uma vez que a proposta apresentada foi de que ele serviria para auxiliar e engajar os colaboradores a conhecerem mais do processo de contratação de um fornecedor. 

&nbsp;&nbsp;&nbsp;&nbsp; Pensando no público alvo de forma mais detalhada, tomando como base um formulário feito por nossa turma e enviado para os funcionários da Meta responderem, podemos pensar em nossos futuros jogadores como, em primeiro lugar, pessoas que trabalham em diferentes áreas da empresa, desde o financeiro até o time de sourcing, ou seja, uma equipe diversificada no quesito da função que exercem.

&nbsp;&nbsp;&nbsp;&nbsp; Podemos citar também as claras diferenças de forma de analisar dados e maneira de pensar, visto que as respostas ao formulário para questões que tinham como tópico principal as características que eram sublimes para a contratação de um fornecedor e as principais dificuldades enfrentadas para tal foram bem diferentes.

&nbsp;&nbsp;&nbsp;&nbsp; Falando agora sobre a experiência do público alvo com jogos, elas também foram bem diversificadas, englobando desde pessoas que jogam diariamente até pessoas que não entendem/conhecem nada do assunto. Mas apesar disso, os perfis para jogos se repetiram em todas as respostas, sendo os respondentes se identificaram com os perfis: conquistadores, ou seja, gostam de acumular conteúdo e superar as metas que o ambiente proporciona, e versáteis, ou seja, jogam diferentes tipos de jogos.

&nbsp;&nbsp;&nbsp;&nbsp; Em conclusão, é possível perceber que apesar de bem diferentes em alguns aspectos, o perfil dos colaboradores se encontra em pontos extremamente importantes para o desenvolvimento de jogos, como, por exemplo, na questão do perfil de achiever, que pode ser explorado para gerar maior atração pelo game. Sendo assim, as informações coletadas foram de extrema importância e poderão ser fundamentais para um projeto de sucesso.


# <a name="c2"></a>2. Visão Geral do Jogo

## 2.1. Objetivos do Jogo
&nbsp;&nbsp;&nbsp;&nbsp; Em cada etapa, o jogador será introduzido a uma novo minigame que servirá como suporte na avaliação de fornecedores. Por meio dessas mecânicas, espera-se que o jogador seja capaz de discernir as qualidades e os defeitos dos fornecedores. Caso o jogador faça esta distinção corretamente, o jogador poderá avançar para a próxima fase.

<div align="center">
<sub>Figura 5 - Mecânica 1</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/569f4e16-a6ac-4555-beb2-cbf9d943342e">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp; No minigame 1 mostada nas fotos acima (Figura 5), os jogadores devem examinar os dados de uma empresa. Se as estatísticas forem desfavoráveis, devem ser descartadas para a lixeira; caso contrário, devem ser movidas para o sinal de correto. Em caso de acerto, uma mensagem de congratulação é exibida, enquanto em caso de erro, uma mensagem de erro é apresentada aos participantes. Pensamos nessa mecânica como uma maneira simples e divertida de ensinar aos funcionários da Meta como funciona o processo de análise de histórico dos possíveis fornecedores, para assim transmitir ao jogador os valores que a Meta busca em seus fornecedores de uma forma leve de se entender.

<div align="center">
<sub>Figura 6 - Mecânica 2</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/83de6ef6-f192-4516-a629-daa995e1ac96"align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub>Figura 7 - Mecânica 2</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/3dfaf82a-2566-4170-8418-e64f6520c263">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp; No Minigame 2 (Figuras 6 e 7), os jogadores exploram três sites diferentes para analisar questões trabalhistas, financeiras e judiciais das empresas. Nesta etapa, o jogador investiga profundamente para entender a reputação de cada empresa, analisando assuntos como políticas de recursos humanos, relatórios financeiros e casos legais pendentes. Após essa análise minuciosa, os jogadores devem tomar uma decisão, enviando um e-mail para formalizar a contratação da empresa escolhida.

<div align="center">
<sub>Figura 8 - Mecânica 3</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/860a1f7f-e844-40ab-ad00-0a29db9b9199">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub>Figura 9 - Mecânica 3 parte 2</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/ab43eced-4c14-47a7-8a5c-b099707e331a">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp; No Minigame 3 (Figuras 8 e 9), o jogador deve escolher entre quatro funcionários, cada um representando um perfil único, para designar quem será encarregado de manter uma relação positiva entre os fornecedores selecionados e a Meta.

## 2.2. Características do Jogo

### 2.2.1. Gênero do Jogo
&nbsp;&nbsp;&nbsp;&nbsp; Nosso jogo retrata alguns gêneros e como principal deles: 
- Simulação, já que nele almejamos emular o mais próximo possível da realidade, como por exemplo, o cenário onde se passa a maioria do jogo, sendo onde o funcionário trabalha e aplicará o conhecimento adquirido durante o game[5]. 
- Estratégia, já que requer habilidade, planejamento e conhecimento para conclusão das fases do jogo[6]. 
- Aventura, pois o jogador deverá guiar o personagem pelo mapa para realizar as tarefas designadas a ele durante a gameplay[7].
- Educação, devido ao claro intuito de orientar os jogadores (funcionários) a respeito do processo de contratação de fornecedores.

### 2.2.2. Plataforma do Jogo
&nbsp;&nbsp;&nbsp;&nbsp; O jogo estará disponível nas plataformas de desktops, smartphones e tablets, compatível com sistemas Web, Windows, MacOS, Android e iOS. O principal objetivo dessas diversas compatibilidades é tornar o jogo e, consequentemente, o conhecimento o mais acessível possível. 

### 2.2.3. Número de jogadores
&nbsp;&nbsp;&nbsp;&nbsp; O game será jogado por apenas 1 jogador para ser concluído no tempo previsto de jogo e também para poder maximizar o aprendizado a respeito do processo de contratação.

### 2.2.4. Títulos semelhantes e inspirações
&nbsp;&nbsp;&nbsp;&nbsp; Temos como principais fontes de inspiração os jogos: Pokémon Ruby e Sapphire, Papers Please, Undertale e Stardew Valley, a principal aplicação dessas inspirações se dá na parte de design do jogo, mas também engloba inspirações na parte de mecânicas durante a gameplay.

### 2.2.5. Tempo estimado de jogo
&nbsp;&nbsp;&nbsp;&nbsp; O jogo pode ser concluído entre 20 minutos e 30 minutos, passando por todas as fases. Para que, assim, atenda aos objetivos traçados pela META, assim como o tempo estimado pela própria em conjunto com a equipe.

# <a name="c3"></a>3. Game Design

## 3.1. Enredo do Jogo
   
&nbsp;&nbsp;&nbsp;&nbsp; No jogo "Pocket Supplier", os jogadores serão imersos no ambiente do prédio da empresa Meta, onde serão guiados por diversos mentores, incluindo Tata e Fabricinho, durante o processo de contratação. Cada mentor representará uma etapa específica desse processo, como Olga, Cayman, Luna, Barack e Shang. Esses personagens não apenas orientarão os jogadores, mas também oferecerão desafios representados por minigames em diferentes áreas do primeiro andar do prédio.

&nbsp;&nbsp;&nbsp;&nbsp; Cada minigame será projetado para simular uma parte do processo de contratação, oferecendo aos jogadores uma experiência diversificada e envolvente. Esses desafios são concebidos não apenas para entreter, mas também para educar os jogadores sobre os diversos aspectos envolvidos na seleção de fornecedores alinhados aos ideais da empresa Meta.

&nbsp;&nbsp;&nbsp;&nbsp; Ao longo das fases, os jogadores serão instruídos em vários aspectos do processo de contratação, adquirindo conhecimento e habilidades à medida que avançam no jogo. Cada desafio apresentará uma oportunidade para os jogadores aplicarem o que aprenderam, preparando-os para enfrentar desafios mais complexos à medida que progridem.

&nbsp;&nbsp;&nbsp;&nbsp; Na fase final do jogo, os jogadores alcançarão o segundo andar do prédio, onde enfrentarão um grande desafio que sintetiza todo o conhecimento adquirido ao longo dos minigames anteriores. Este desafio final incorporará elementos de todos os aspectos do processo de contratação, exigindo que os jogadores demonstrem um entendimento abrangente e habilidades estratégicas para serem bem-sucedidos.


## 3.2. Personagens

### 3.2.1. Controláveis

&nbsp;&nbsp;&nbsp;&nbsp; Os personagens controláveis, são aqueles que o jogador consegue controlar usando comandos dados pelo próprio usuário, como por exemplo, teclas do teclado, movimento e click do mouse, entre outros.

&nbsp;&nbsp;&nbsp;&nbsp; O Pocket Supplier possui até então dois “personagens controláveis”. Dentre eles estão o protagonista da história e as pastas arrastáveis, que dentro delas possuem os formulários dos fornecedores na fase 1 do jogo.

&nbsp;&nbsp;&nbsp;&nbsp; O protagonista principal da história do Pocket Supplier (Figura 10), inicialmente não possui nome, mas ao decorrer do jogo o usuário terá a oportunidade de colocar seu nome “no personagem”, assim conectando mais o usuário com as mecânicas do “game”. Este personagem será utilizado em todas as cenas principais do jogo e sempre será a representação do colaborador da Meta no escritório da mesma.

<div align="center">
<sub>Figura 10</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/geovane_spritesheet.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; O outro elemento controlável do jogo são as pastas da fase 1 (Figura 11). Esse elemento é utilizado para fazer a dinâmica da etapa, sendo possível arrastá-los para um lixo, recusando os formulários dos fornecedores dentro dessas pastas ou aceitando-os, levando eles para outra pasta na mesa. O formulário foi implementado com o intuito de o jogador conseguir entender,intuitivamente, se o usuário, como um colaborador da Meta, deve sim ou não aceitar os históricos dos fornecedores dentro dessas pastas. 

<div align="center">
<sub>Figura 11</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/pastas.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Consequentemente, podemos concluir que na maioria dos jogos, os personagens e dinâmicas principais são elementos comandáveis, isto é, “personagens controláveis”. Em Pocket Supplier, foram tomados como inspiração os jogos, Pokémon, onde foram usados as ideias de o personagem principal ser controlável e suas oportunidades de escolha, e o “game” Papers Please, em que o personagem (que você não controla os movimentos, apenas o movimento dos itens que ele usa) como um despachante aduaneiro, aceita ou recusa pessoas na fronteira do seu país. 

&nbsp;&nbsp;&nbsp;&nbsp; Portanto, nos jogos atuais, fica muito claro que são poucos os jogos que inovam em mecânica, os “games” não fogem do clichê, mas o diferencial deles são seus roteiros, imagens, sons e a maneira como eles lidam com essas mecânicas.


### 3.2.2. Non-Playable Characters (NPC)

&nbsp;&nbsp;&nbsp;&nbsp; Os personagens não jogáveis, ou em inglês Non-Playable Characters (NPC), são aqueles personagens que o jogador não tem nenhum controle direto sobre eles, isto é, elementos nos quais os comandos passados pelo usuário não influenciam exatamente nos NPC.

&nbsp;&nbsp;&nbsp;&nbsp; No Pocket Supplier os Non-Playable Characters, assim como os personagens controláveis, são apenas dois, sendo eles a “Tatá” e o “Fabrício”.

&nbsp;&nbsp;&nbsp;&nbsp; Nessa perspectiva, a Tatá foi inspirada na representante da Meta no projeto do Módulo 1 da turma 14, a Thaís. Nesse sentido, como uma homenagem a Thaís, a Tatá é a mentora do jogador no roteiro do jogo, oferecendo suporte e assistência ao usuário no decorrer da história. 

<div align="center">
<sub>Figura 12</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/tata.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; O outro personagem não jogável é o Fabricinho. Inspirado no mascote que passa ao usuário dicas de como manter sua privacidade no Facebook, o Fabricinho é um dinossauro azul que apresenta ao jogador o escritório da Meta, introduzindo ele na empresa.

<div align="center">
<sub>Figura 13</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/fabricinho.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Temos também o Barack.

<div align="center">
<sub>Figura 14</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/barack_spritesheet.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; O Cayman.


<div align="center">
<sub>Figura 15</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/cayman_spritesheet.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; A Luna.


<div align="center">
<sub>Figura 16</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/luna_spritesheet2.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; E por último a Olga.

<div align="center">
<sub>Figura 17</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/olga_spritesheet.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Portanto, podemos concluir que, apesar dos personagens não controláveis parecerem não ter utilidade e importância, pelo fato que o jogador não tem influência, eles são muito importantes para a adição de elementos enriquecedores de enredo e implementam uma impressão de imersão do usuário no jogo.

### 3.2.3. Diversidade e Representatividade dos Personagens

&nbsp;&nbsp;&nbsp;&nbsp; A representatividade, no contexto sociocultural, refere-se à inclusão e visibilidade de diferentes grupos sociais, garantindo que suas identidades, experiências e perspectivas sejam reconhecidas e respeitadas. É um conceito fundamental para promover a igualdade e a diversidade, proporcionando um ambiente mais inclusivo e justo para todos.

&nbsp;&nbsp;&nbsp;&nbsp; Ao analisar os personagens do jogo Pocket Supplier, fica evidente a presença de representatividade. Isso demonstra um esforço para incluir a comunidade LGBTQIAPN+ e realce a falta de suporte que essa comunidade muitas vezes enfrenta.

&nbsp;&nbsp;&nbsp;&nbsp; Além disso, a personagem Tatá representa uma figura significativa na área de programação. Como uma mulher negra, ela enfrenta desafios adicionais em um campo que historicamente tem sido dominado por homens brancos. Sua presença no jogo destaca a importância da diversidade no mundo da tecnologia e destaca a necessidade de valorizar talentos diversos.

&nbsp;&nbsp;&nbsp;&nbsp; Em conclusão, a presença de representatividade nos personagens do jogo não apenas enriquece a experiência do jogador, mas também contribui para uma narrativa mais inclusiva e reflexiva. Promover a diversidade e a inclusão é essencial para construir uma sociedade mais justa e igualitária, onde todas as pessoas se sintam representadas e respeitadas.


## 3.3. Mundo do jogo

### 3.3.1. Locações Principais e/ou Mapas

&nbsp;&nbsp;&nbsp;&nbsp; O jogador adentra o prédio e e é recebido pela atmosfera da secretaria. Ao se aproximar, avista Fabricinho, um colaborador entusiasmado e bem-humorado. O qual convida-o a seguir em direção ao elevador que o levará para uma imersão no mundo da empresa.

<div align="center">
<sub>Figura 18</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc1.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; O jogador começa ao lado do elevador, após passar pela secretaria, imergindo em um escritório, inspirado na cultura da Meta. À direita, Tatá está a sua espera para introduzi-lo na empresa.

<div align="center">
<sub>Figura 19</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc6.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; No centro do mapa, encontrasse uma sala de trabalho dos colaboradores, onde a primeira fase será realizada.

<div align="center">
<sub>Figura 20</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc2.jpg" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Abaixo da sala principal, há um nível dedicado às operações cotidianas da empresa. Neste nível, encontram-se duas salas de reunião, destinadas às equipes, onde podem realizar seus encontros para discutir estratégias e resolver questões importantes de trabalho.

<div align="center">
<sub>Figura 21</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc3.jpg" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Neste espaço, encontra-se o depósito da empresa, utilizado para armazenar uma variedade de itens e materiais essenciais para as operações.

<div align="center">
<sub>Figura 22</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc4.jpg" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Por fim, temos a sala do chefe, um ambiente reservado e elegante destinado ao líder da empresa, onde ele pode conduzir reuniões importantes, tomar decisões estratégicas e receber os colaboradores.

<div align="center">
<sub>Figura 23</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/Loc5.png" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>

### 3.3.2. Navegação pelo mundo
&nbsp;&nbsp;&nbsp;&nbsp; A navegação pelo jogo inicia-se na recepção do prédio da Meta, onde o jogador é apresentado a Fabricinho, instrutor responsável por orientá-lo nessa jornada. Fabricinho explica os primeiros passos e acompanha o jogador até o elevador. Após essa cena, o jogador é conduzido ao primeiro andar, onde se encontra com Tata, a primeira de uma série de instrutores nessa área.

&nbsp;&nbsp;&nbsp;&nbsp; Cada mentor do primeiro andar fornece uma instrução sobre uma etapa específica do processo de contratação de fornecedores e apresenta um minigame correspondente. Após interagir com todos os instrutores do primeiro andar, o jogador desbloqueia o acesso ao segundo andar, onde enfrentará o desafio final com o último instrutor.

<div align="center">
  <sub>Quadro 02 - Navegação pelo mundo 01</sub>
</div> 

Número | Requisito
--- | ---
Recepção | Primeira localização do jogo, na qual o jogador poderá sair após receber as instruções de Fabricinho para subir para o primeiro andar do prédio
Primeiro andar | O jogador deve cumprir todos os minigames se movendo e interagindo com os NPC's conforme as instruções desse andar para poder subir para o próximo
Segundo andar | Neste andar o jogador enfrentará o desafio final, onde será testado em relação ao aprendizado de sua jornada

<div align="center">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### 3.3.3. Condições climáticas e temporais

&nbsp;&nbsp;&nbsp;&nbsp; Em nosso jogo, o conceito de tempo é eliminado, permitindo que os jogadores explorem o espaço do personagem e cenários sem restrições temporais. Optamos por criar uma experiência imersiva, onde os jogadores podem mergulhar completamente na narrativa e nas mecânicas do jogo, dedicando-se ao máximo para entender o processo de contratação de um fornecedor, crucial para a Meta. Assim, essa abordagem proporciona uma curva de aprendizagem mais acentuada, uma vez que deixa o jogo com menos elementos, logo, mais fácil de entender, o que essencial e sublime na abordagem que estamos tendo para essa solução gamificada, alcançando também de maneira mais fácil o resultado esperado pelo parceiro, sendo o entendimento do processo de contratação de fornecedores por parte dos funcionários. 

&nbsp;&nbsp;&nbsp;&nbsp; Em síntese, o fato do jogo não ter condições temporais é reflexo do intuito do game, sendo importante para que o objetivo de sua criação seja alcançado com êxito.

### 3.3.4. Concept Art

<div align="center">
<sub>Figura 24 - Mecânica para a etapa de privacy anda security</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/99ccb58f-44d8-4e46-96da-75eef20140fc">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

Nota: Concept demonstrando a dinâmica de análise da privacidade e segurança de uma empresa X, que faz parte do processo de contratação da meta.

<div align="center">
<sub>Figura 25 - Mecânica para avaliar diferentes fornecedores</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/44d76d2f-ede4-497c-8ef4-8bb9818859c9">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

Nota: Concept mostrando a comparação entre dois fornecedores, estilo uma batalha de pokemon.

<div align="center">
<sub>Figura 26 - Mecânica para a etapa de anticorrupção</sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/0b2cf754-72d7-49a8-83a3-9da822a47a42">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

Nota: Concept demonstrando como funcionaria a fase de anti-corrupção do processo de contratação dos fornecedores, exemplificada pela tentativa de suborno de um dos colaboradores da meta por um fornecedor.


### 3.3.5. Trilha sonora

&nbsp;&nbsp;&nbsp;&nbsp; A trilha sonora desempenha um papel fundamental em qualquer obra de entretenimento. Em momentos cruciais, a música tem o poder de transmitir emoções específicas, intensificando sentimentos e complementando a narrativa. No projeto PocketSuppliers, não consideramos a música apenas como um mero complemento, mas sim como um elemento central. Para escolher as trilhas sonoras ideais para cada cena, realizamos testes com nossos integrantes, avaliando suas reações emocionais em relação a cada composição musical em momentos específicos. Como resultado, chegamos à seleção das seguintes músicas:

<div align="center">
  <sub>Quadro 03 - Trilha Sonora</sub>
</div>

 Número | titulo | ocorrência | autoria
--- | --- | --- | ---
1|[Press Play](https://www.youtube.com/watch?v=P54a-u9j4L0) | Tela de Menu | Panda Beats
2 | [Hello It´s Me!](https://www.youtube.com/watch?v=xu7cFtkwz1g)  | Trilha padrão enquanto o jogador estiver no escritório | Pix
3 | [Itty Bitty 8 Bit](https://www.youtube.com/watch?v=XBEz8s-0hnU)  | Primeira mecânica | Kevin MacLeod
OBS | (As demais mecânicas terão suas trilhas sonoras definidas ao decorrer das próximas semanas)

<div align="center">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## 3.4. Inventário e Bestiário

### 3.4.1. Inventário

&nbsp;&nbsp;&nbsp;&nbsp; Decidimos não incluir um sistema de inventário ou itens em nosso jogo, visando proporcionar uma experiência centrada na narrativa e na jogabilidade. Optamos por simplificar a experiência do jogador, evitando distrações que poderiam prejudicar o envolvimento com a história e os desafios do jogo. 

### 3.4.2. Bestiário

&nbsp;&nbsp;&nbsp;&nbsp; Em nosso jogo, adotamos uma abordagem única e inovadora: não possuímos inimigos. Acreditamos que a jornada do jogador pode ser rica e envolvente sem a necessidade de violência. Em vez disso, focamos em desafios, obstáculos e instruções que surgem naturalmente no decorrer da narrativa, proporcionando uma experiência mais imersiva e reflexiva.

## 3.5. Gameflow (Diagrama de cenas)

&nbsp;&nbsp;&nbsp;&nbsp; Um storyboard é uma ferramenta que permite visualizar uma história ou narrativa por uma sequência de ilustrações, ou imagens (Figura 27). É usado para planejar e comunicar como um projeto ou cena se desenvolverá, com uma visão mais detalhada. Um storyboard é importante porque ajuda a organizar as ideias, a identificar problemas, a economizar tempo e recursos, e a criar uma experiência melhor para o público. No contexto de desenvolvimento de jogos, o storyboard é crucial para definir mecânicas, personagens, cenários e desafios. Sua utilização proporciona testes e aprimoramentos conceituais antes da produção, contribuindo para uma experiência mais impactante para o público. Nosso storyboard de programação está disponível em melhor qualidade de imagem em: https://miro.com/app/board/uXjVKbCVi1w=/.

<div align="center">
<sub>Figura 27 - Storyboard </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/storyboard.png">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp; O nosso storyboard é a tradução resumida e completa dos conceitos fundamentais do nosso jogo. Com esta ferramenta, podemos antecipar desafios, configurar níveis e elaborar diálogos envolventes de maneira precisa, proporcionando uma visão detalhada e perspicaz dos aspectos visuais. Consolidamos uma base sólida que não apenas orienta, mas também potencializa a experiência do jogador ao integrar esses elementos. Dessa forma, o storyboard não só visualmente delineia nosso caminho, mas também atua como um guia crucial para garantir que todos os aspectos do jogo sejam planejados e refinados minuciosamente a fim de alcançar um produto final excepcional.

## 3.6. Regras do jogo
&nbsp;&nbsp;&nbsp;&nbsp; No jogo "Pocket Supplier", o jogador é desafiado a compreender o processo de contratação de fornecedores da empresa META. Durante a jornada, os jogadores serão submetidos a minigames que testam sua proficiência sobre o conhecimento em cada etapa do processo e devem ser concluídos para que o jogador possa progredir.

&nbsp;&nbsp;&nbsp;&nbsp; No Minigame 1, o jogador é introduzido à etapa inicial de avaliação, onde é apresentado a uma série de formulários que precisam ser analisados e categorizados corretamente. O objetivo é arrastar os formulários para a prancheta, permitindo que o jogador leia seu conteúdo e tome decisões sobre se deve arquivá-los ou aprová-los. Se um formulário for movido para o local incorreto, uma mensagem de erro alertará o jogador, incentivando-o a reavaliar e realocar o formulário. O desafio é concluído quando todos os formulários são corretamente colocados em seus respectivos lugares.

&nbsp;&nbsp;&nbsp;&nbsp; No Minigame 2, os jogadores enfrentam o desafio de analisar dados financeiros, judiciais e trabalhistas de uma empresa fornecedora em potencial. Para isso, têm acesso a três fontes de informação: "Reclame Aqui" para questões trabalhistas, "Banco Digital" para avaliar a saúde financeira da empresa e fornecer um contexto sobre sua condição, e "JusMETA" para verificar processos judiciais contra a empresa. Após a análise, Olga, a instrutora desta etapa, questiona qual empresa o jogador escolherá aprovar no processo. Caso o jogador selecione a opção errada, Olga fornece uma explicação sobre o motivo da escolha incorreta e indica a opção correta. Se o jogador acertar, Olga o parabeniza e fornece orientações sobre como proceder no jogo.

## 3.7. Mecânicas do jogo
&nbsp;&nbsp;&nbsp;&nbsp; Dentro do framework MDA, a mecânica é entendida como o conjunto de regras bem-definidas que têm a função crucial de caracterizar o jogo e impulsionar sua dinâmica. Em outras palavras, as mecânicas são os elementos essenciais que dão vida ao jogo, determinando como os jogadores interagem com o ambiente virtual e entre si. Essas regras devem ser cuidadosamente planejadas para criar processos que não apenas desencadeiem a diversão esperada pelo jogador, mas também promovam desafios cativantes, recompensas gratificantes e uma experiência envolvente de jogo.

&nbsp;&nbsp;&nbsp;&nbsp; No jogo "Pocket Supplier", as mecânicas incorporadas abrangem a locomoção do jogador por meio das teclas WASD, um padrão amplamente adotado em jogos de computador. Além disso, as interações com NPCs são realizadas de forma intuitiva, utilizando a tecla E para desencadear as falas ou minigames que esses possam apresentar. Uma característica distintiva é a implementação da mecânica "drag and click", na qual o jogador deve clicar e arrastar formulários, decidindo se os arquiva ou os aprova com base em seu julgamento. Essas mecânicas, cuidadosamente integradas, visam proporcionar uma experiência de jogo fluida e envolvente, incentivando os jogadores a explorarem o mundo do jogo de forma interativa e participativa.

# <a name="c4"></a>4. Desenvolvimento do Jogo

## 4.1. Desenvolvimento preliminar do jogo:

&nbsp;&nbsp;&nbsp;&nbsp; Atualmente, a primeira versão do jogo apresenta um cenário inicial situado em um ambiente de escritório, no qual o protagonista possui liberdade de movimento utilizando as teclas direcionais ou os controles WASD. Cada direção de movimento do personagem é acompanhada por uma animação correspondente, e a cena é acompanhada por uma trilha sonora ambiente. Até o momento, nossa equipe enfrentou principalmente desafios relacionados às colisões entre o personagem e os objetos presentes no cenário.

<div align="center">
<sub>Quadro 04 - Próximos passos do desenvolvimento</sub>
</div>

<div align="center">

Número | Próximos passos no desenvolvimento do jogo
--- | ---
1| Solucionar os problemas de colisão entre o personagem e os objetos do cenário.
2| Introduzir novos personagens com os quais o protagonista poderá interagir.
3| Implementar diálogos entre os personagens.
4| Desenvolver um novo cenário para progredir para a próxima fase do jogo.

</div>

<div align="center">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br></br>
Aqui estão alguns screenshots que ilustram a versão inicial do jogo:
<br></br>
<div align="center">
<sub align="top">Figura 28 - Exemplos da versão do jogo </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/exemplo1.jpeg" align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>


<div align="center">
<sub align="top">Figura 29 - Exemplos da versão do jogo </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/exemplo2.jpeg" align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>



<div align="center">
<sub align="top">Figura 30 - Exemplos da versão do jogo </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/exemplo3.jpeg" align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>



<div align="center">
<sub align="top">Figura 31 - Exemplos da versão do jogo </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/exemplo4.jpeg" align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>


## 4.2. Desenvolvimento básico do jogo

&nbsp;&nbsp;&nbsp;&nbsp; Para o desenvolvimento básico do jogo, o grupo concentrou-se em apresentar elementos essenciais para a jogabilidade que possam ser aperfeiçoados posteriormente. Neste pensamento, optamos por criar um menu principal simples, com um botão funcional de "start" (Figura 32), proporcionando aos jogadores uma entrada direta no jogo. Após selecionar "start", uma animação de introdução é exibida, detalhando o personagem principal dirigindo-se ao edifício da Meta. Utilizando um elevador, o personagem chega ao primeiro escritório do jogo (Figura 33), onde a narrativa inicialmente se desenrola.

&nbsp;&nbsp;&nbsp;&nbsp;Dentro deste escritório, o jogador pode explorá-lo utilizando as setas direcionais do teclado para se movimentar e interagir com objetos (Figura 34), criando uma sensação imersiva desde o início do jogo. Esta fase inicial serve como uma introdução ao ambiente e à mecânica do jogo, permitindo aos jogadores familiarizarem-se com os controles e o ambiente que irão explorar.

&nbsp;&nbsp;&nbsp;&nbsp;Uma mecânica essencial do jogo é introduzida nesta fase, que envolve a exibição de formulários com informações sobre potenciais fornecedores. O jogador é desafiado a analisar esses formulários e tomar decisões estratégicas. Formulários com informações favoráveis devem ser movidos para um envelope marcado com o símbolo da Meta, indicando uma escolha positiva (Figura 35). Por outro lado, formulários com informações desfavoráveis devem ser descartados no lixeiro, exigindo discernimento por parte do jogador para diferenciar entre opções vantajosas e desvantajosas.

&nbsp;&nbsp;&nbsp;&nbsp;Esses elementos iniciais do jogo estabelecem uma base sólida para a jogabilidade futura, introduzindo os jogadores ao mundo do jogo, suas mecânicas principais e desafios. Ao focar inicialmente em elementos-chave da jogabilidade, permitimos espaço para o aperfeiçoamento e expansão do jogo ao longo do desenvolvimento, mantendo-nos fiéis à visão inicial do projeto.

<div align="center">
<sub align="center">Figura 32 - Código do menu </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/codigo_menu.jpeg">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 33 - Código da animação introdutória </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/codigo_intro.jpeg">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 34 - Código do movimento do personagem </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/codigo_andar.jpeg">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 35 - Código da mecânica </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/blob/main/assets/codigo_mecanica.jpeg">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## 4.3. Desenvolvimento intermediário do jogo

&nbsp;&nbsp;&nbsp;&nbsp; Para a versão intermediária do jogo, tivemos como meta do grupo entregar um jogo que tivesse uma continuidade, que fosse possível para o jogador avançar até certo ponto sem precisar da ajuda de alguém, ou pular alguma parte durante esse caminho.

&nbsp;&nbsp;&nbsp;&nbsp; Assim, focamos em entregar essa continuidade, implementando cenas e novas informações no código que contribuíssem para isso.

&nbsp;&nbsp;&nbsp;&nbsp; Dessa forma, começamos onde todo jogo começa: pela tela de início (start), que na versão anterior estava com algumas funcionalidades faltando e em versão beta. Para essa sprint, corrigimos e reformulamos tal tela (imagem 36), além de corrigir um pequeno bug no vídeo que roda após o início do jogo.

&nbsp;&nbsp;&nbsp;&nbsp; Seguindo a ordem dos acontecimentos, o próximo item a ser feito da lista eram os balões de fala e interações com NPCs, que permitiriam ao jogo progredir sem dicas externas, enquanto os NPCs ensinariam os jogadores a jogar. Dessa forma, como mostra a imagem 37, para fazer isso utilizamos uma tecla para acionar os balões de fala, deixando-os visíveis, o que foi, de certa forma, simples e deixou o jogo mais completo.

&nbsp;&nbsp;&nbsp;&nbsp; Além disso, a próxima tarefa foi dar alguns toques finais, seguindo a sugestão do parceiro (trocar o lixo por uma caixa de arquivos) na primeira mecânica de "drag and drop". Essa parte foi concluída rapidamente, permitindo que fizéssemos também a segunda mecânica, que consiste em análises mais profundas dos fornecedores, também conhecida como due diligence, onde o jogador analisará fatores como jurisdição e as finanças de tal empresa, por meio de um "site" no jogo (uma parte disso pode ser observado na imagem 38).

&nbsp;&nbsp;&nbsp;&nbsp; Por fim, para ambientar tudo isso da melhor maneira, colocamos música no jogo, fator essencial para imergir e focar mais o jogador no jogo, melhorando sua experiência por completo. A escolha das músicas foi feita baseada na nossa ideia inicial de game, que seria algo mais alegre, com certo tom humorístico, mas também com um cunho de aprendizagem. Elas foram adicionadas de forma simples, sendo apenas carregadas no preload e iniciadas.

<div align="center">
<sub align="center">Figura 36 - Tela inicial reformulada </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/72086996-7581-43ee-bed0-52f3ea5bcff0">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 37 - Código dos balões de fala </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/ad943ec4-b2e3-4979-a6b8-2a12bca09b44">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 38 - Mecânica Due Diligence </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/83de6ef6-f192-4516-a629-daa995e1ac96">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## 4.4. Desenvolvimento final do MVP

&nbsp;&nbsp;&nbsp;&nbsp; Para a sprint em questão, nosso foco para a finalização do MVP, de forma a deixar o jogo com suas principais e mais importantes características, atendendo aos requisitos e necessidades apresentados pelo parceiro, mas que também foram estudados por nosso grupo, focamos em dar detalhes e terminar todas as etapas do processo de contratação.

&nbsp;&nbsp;&nbsp;&nbsp; Nosso principal foco foi em adicionar os pequenos, mas cruciais, ajustes que deixariam o jogo dinâmico e fluído. Dessa forma, recorremos à ajuda e críticas de diversas, pessoas, que contribuíram, e muito, para que o jogo pudesse ter um desenvolvimento mais coerente com o objetivo. Assim, contamos em especial com a opinião da professora Bruna, de UX, e de nosso orientador: Marcelo, para fazer as alterações finais.

&nbsp;&nbsp;&nbsp;&nbsp; Como primeira mudança, colocamos uma secretaria para poder introduzir o jogador aos controles e à aventura que ele está embarcando. Sendo assim, o Fabricinho (dinossauro da imagem 39) é o responsável por ter esse primeiro e sublime contato.

&nbsp;&nbsp;&nbsp;&nbsp; Seguindo as recomendações que recebemos, diminuímos o tamanho da primeira mecânica, que estava muito cansativa e longa, assim como colocamos instruções mais claras e diretas sobre como o player pode jogar aquela fase. 

&nbsp;&nbsp;&nbsp;&nbsp; Foram feitas muitas correções de bugs que afetavam o andamento do jogo como um todo, e aprimorada a mecânica 2, da análise por meio do "browser" de possíveis fornecedores para a meta. Um e-mail para concluir tal mecânica, coisa que não existia antes, também foi adicionado (imagem 40).

&nbsp;&nbsp;&nbsp;&nbsp; Por fim, uma tela para a seleção de fornecedores (imagem 41), ainda em fase de desenvolvimento, mas nos passos finais, foi colocada como a terceira mecânica, dando fechamento à escolha do fornecedor para a meta, processo estudado a fundo por nós para ser reproduzido de forma lúdica, rápida mas eficiente para o aprendizado dos colaboradores de tal empresa.

&nbsp;&nbsp;&nbsp;&nbsp; Essas melhorias refletem nosso compromisso em entregar um produto de alta qualidade, alinhado com as expectativas do parceiro e proporcionando uma experiência de jogo memorável para os usuários.

<div align="center">
<sub align="center">Figura 39 - Secretaria com Fabricinho </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/0b0880b5-28d5-4039-9d78-6147e577341b">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 40 - Complementação da mecânica 2 com emails </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/3dfaf82a-2566-4170-8418-e64f6520c263">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub align="center">Figura 41 - Seleção de fornecedores </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158570773/860a1f7f-e844-40ab-ad00-0a29db9b9199">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## 4.5. Revisão do MVP

&nbsp;&nbsp;&nbsp;&nbsp; Nesta seção, descrevemos o processo de refinamento e revisão da versão final do jogo, enfocando os entregáveis do MVP (Minimum Viable Product). Abaixo está um resumo do que foi alcançado nesta fase, com capturas de tela para ilustrar os principais pontos.

### Desenvolvimento dos Refinamentos e Revisões
&nbsp;&nbsp;&nbsp;&nbsp; Durante a Sprint 5, concentramos nossos esforços na finalização do MVP do jogo, implementando refinamentos com base nos feedbacks das sprints anteriores e nas exigências do escopo inicial. 

### Intuitividade do jogo
&nbsp;&nbsp;&nbsp;&nbsp; Através dos feedbacks recebidos, identificamos uma das principais dificuldades dos jogadores: a falta de intuição no jogo, levando à confusão ou incerteza sobre as próximas etapas. Assim, aprimoramos a experiência, adicionando guias nos mapas e fornecendo explicações durante os minigames, tornando o jogo mais acessível e envolvente para os jogadores.

<div align="center">
<sub>Figura 42 - Seta indicando onde o jogador deve ir </sub>
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/63842f92-032f-4233-87a0-1eb061b2e66e" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
<sub>Figura 43 - Fabricinho explicando minigame
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/ab69fdcc-e99a-4453-a4f4-f34926dfdaf5" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### Adição de elementos sonoros ao jogo
&nbsp;&nbsp;&nbsp;&nbsp; Um feedback frequente dos jogadores foi a monotonia percebida no jogo devido à ausência de trilha sonora e efeitos sonoros. Levando em consideração essa informação crucial, tomamos medidas para aprimorar a experiência do jogo. Selecionamos cuidadosamente músicas específicas para cada cenário e minijogo, visando proporcionar uma experiência mais emocionante durante toda a jogabilidade. Essa iniciativa busca amplificar a atmosfera do jogo, tornando-o mais dinâmico e cativante para os jogadores.

### Adição de Elementos no Escritório
&nbsp;&nbsp;&nbsp;&nbsp; Outro aspecto que contribuía para a monotonia e a sensação de "vazio" no jogo era a ausência de pessoas no escritório, o que tornava a experiência pouco instigante e muitas vezes entediante. Para resolver isso, decidimos adicionar NPCs ao jogo. Esses personagens foram incorporados ao ambiente do escritório para preencher o vazio e proporcionar uma atmosfera mais dinâmica e viva, tornando a interação no jogo mais envolvente e interessante para os jogadores.
//colocar imagens dos NPC's

<div align="center">
<sub>Figura 44 - NPC's espalhados pelo escritório
<img src="https://github.com/Inteli-College/2024-T0014-IN01-G05/assets/158752303/7e9c47ee-3ec6-4dad-a9ac-a305b296817a"align="center" width="100%">
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### Entregáveis do MVP
O MVP revisado agora inclui os seguintes elementos principais:

### Jogabilidade Funcional
&nbsp;&nbsp;&nbsp;&nbsp; Os jogadores são instruídos desde a primeira fase sobre as jogabilidades básicas do jogo, como andar e interagir com objetos, e são constantemente lembrados do que devem fazer e como devem proceder durante os minigames, tornando o jogo funcional e fácil de jogar.

### Mapa mais Intuitivo 
&nbsp;&nbsp;&nbsp;&nbsp; Ao mapa foram adicionados elementos visuais visando simplifica-lo e melhora-lo, assim facilitando a navegação e exploração do jogador e consequentemente tornando o jogo mais fácil.

### Minigames Implementados
&nbsp;&nbsp;&nbsp;&nbsp; Todos os minigames do jogo estão totalmente funcionais, intuitivos e proporcionam aos jogadores uma experiência divertida e simplificada do processo de contratação. 

### Elementos sonoros
&nbsp;&nbsp;&nbsp;&nbsp; Os elementos sonoros essenciais estão cuidadosamente implementados, trazendo vida ao jogo e conferindo uma sensação única a cada etapa do processo. Os sons complementam de forma envolvente a experiência do jogador, tornando cada momento mais imersivo e cativante.

# <a name="c5"></a>5. Testes

## 5.1. Casos de Teste

&nbsp;&nbsp;&nbsp;&nbsp; Os casos de teste são conjuntos de condições, dados e passos específicos elaborados para verificar se um determinado software ou sistema atende aos requisitos estabelecidos. Eles são uma parte essencial do processo de teste de software, desempenhando um papel crucial na identificação de possíveis falhas e na garantia da qualidade do produto final.

&nbsp;&nbsp;&nbsp;&nbsp; Dessa forma, eles nos ajudarão a entregar o projeto bem-feito e completo, evitando erros na execução e no código, garantindo uma maior satisfação do nosso parceiro, a Meta.

<div align="center">
<sub>Quadro 05 - Requisito Funcional 01</sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
1 | Usuário conectado com a internet | iniciar o jogo desde seu início | o jogo deve iniciar do menu inicial
2 | Menu inicial aberto | Verificar se as opções de conção do jogo são exibidas | Os botões devem aparecer
3 | O jogador deve clicar no ponto de interrogação | A cena dos créditos deve abrir | A cena dos créditos deve acabar
4 | A tela  do menu inicial deve abrir | Clicar no botão start | O botão start aciona outra tela 
5 | Animação em vídeo deve aparecer | A animação deve aparecer completa | A animação deve chegar até o final
6 | A cena da secretaria deve aparecer após o vídeo | Os comandos andar direita, esquerda, cima e baixo devem funcionar | O player deve andar
7| O jogador deve ir até o Fabricinho | O jogador deve apertar o E | O balão de fala deve abrir
8 | O jogador deve ler todas as instruções e escrever seu nome | O balão de fala deve desaparecer | O jogador deve andar até o elevador
9 | O jogador deve apertar o E | O vídeo do elevador deve começar | O vídeo do elevador deve acabar
10 | A cena do escritório deve aparecer após o vídeo | Os comandos andar direita, esquerda, cima e baixo devem funcionar | O player deve andar
11 | Um botão com a letra E deve estar piscando | O player deve clicar no botão | O botão deve abrir os balões de fala
12| O balão de fala deve abrir | O jogador deve apertar o botão com a letra E novamente | O diálogo antigo deve ser substituído
13| O jogador ter lido todo o texto | O jogador entendeu o texto e está preparado para a nova mecânica | O jogador deve seguir para a próxima mecânica
14| Um botão deve aparecer no escritório | O player deve clicar no botão | O botão deve abrir outra cena
15| A nova cena deve aparecer | As pastas devem ser arrastadas até a prancheta | A pasta se transformará em textos
16| O jogador deve arrastar o texto da prancheta | A pasta deve aparecer novamente | O texto deve desaparecer
17| O jogador deve arrastar o papel até o lixo ou a pasta | A resposta aparecerá como 'error' em caso de erro e "congratulations" em caso de acerto | A pasta deverá sumir 
18| O jogador deve arrastar todas as pastas | O jogador deve voltar para o escritório | O jogador deve iniciar a próxima mecânica
19| A nova cena do escritório deve aparecer | O jogador deve andar até a Olga | O jogador deve apertar o E
20| O jogador deve ler todos os diálogos | O jogador deve andar até o computador | O jogador deve apertar o E
21| A nova cena deve abrir | Deve aparecer uma aba para o jogador digitar | O jogador deve apertar na seta 
22| O jogador deverá ler as instruções que aparecerão | O jogador deve digitar as instruções | Deve abrir uma página com três sites
23| O jogador deve escolher um site para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
24| O jogador deve apertar o botão sair | A cena com os três sites deve voltar | O jogador deve apertar em outro site
25| O site deve abrir com uma página | O jogador deverá ler todas as instruções | O jogador deve apertar no botão sair
26| O jogador deve escolher o site ainda não escolhido para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
27| O jogador deve apertar o site ainda não escolhido | A cena com os três sites deve voltar | O jogador deve apertar o botão sair
28| Uma nova cena deve abrir | Deve aparecer uma aba para o jogador digitar | O jogador deve apertar na seta 
29| O jogador deverá ler as instruções que aparecerão | O jogador deve digitar as instruções | Deve abrir uma página com três sites
30| O jogador deve escolher um site para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
31| O jogador deve apertar o botão sair | A cena com os três sites deve voltar | O jogador deve apertar em outro site
32| O site deve abrir com uma página | O jogador deverá ler todas as instruções | O jogador deve apertar no botão sair
33| O jogador deve escolher o site ainda não escolhido para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
34| O jogador deve apertar o botão sair | A cena com os três sites deve voltar | O jogador deve apertar o botão sair
35| Uma nova cena deve abrir | O jogador deve escolher qual das três empresas que ele analisou deve ser contratada | O jogador deve apertar em qual empresa ele quer contratar
36| Se a resposta for correta deve aparecer Parabéns você conseguiu | A cena do escritório deve voltar | Se a resposta for a errada deve aparecer Tente novamente
37| O jogador deve escolher novamente a empresa | Se a resposta for correta deve aparecer: Parabéns! Você conseguiu. | A cena do escritório deve voltar
38| No escritório o jogador deve apertar o E | O balão de fala da Olga deve abrir | O jogador deve ler todas as instruções
39| As instruções devem sumir | O jogador deve ir até o computador | No computador o jogador deve apertar o E
40| Uma nova cena deve abrir | O jogador deve clicar no personagem e analisá-los | O jogador deve escolher o melhor funcionário
41| Se a resposta for correta deve aparecer: Parabéns você conseguiu | A cena do escritório deve voltar | Se a resposta for a errada deve aparecer Tente novamente
42| O jogador deve escolher novamente um funcionário | Se a resposta for correta deve aparecer: Parabéns! Você conseguiu. | A cena do escritório deve voltar
43| No escritório o jogador deve apertar o botão E | Deve abrir uma cena do elevador | A cena do elevador deve acabar
44| Uma cena com botões deve abrir | O jogador deve escolher o botão due diligence | A cena deve começar
45| O jogador deverá ler as instruções que aparecerão | O jogador deve digitar as instruções | Deve abrir uma página com três sites
46| O jogador deve escolher um site para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
47| O jogador deve apertar o botão sair | A cena com os três sites deve voltar | O jogador deve apertar em outro site
48| O site deve abrir com uma página | O jogador deverá ler todas as instruções | O jogador deve apertar no botão sair
49| O jogador deve escolher o site ainda não escolhido para clicar | O site deve abrir com uma página | O jogador deverá ler todas as instruções
50| O jogador deve apertar o botão sair | A cena com os três sites deve voltar | O jogador deve apertar o botão sair
51| O jogador deve digitar metamail | Uma nova cena deve abrir | O jogador deve escolher se a empresa deve ser contratada ou não |
52| Se a resposta for correta deve aparecer Parabéns você conseguiu | A cena do escritório deve voltar | Se a resposta for a errada deve aparecer Tente novamente
53| O jogador deve escolher novamente a empresa | Se a resposta for correta deve aparecer: Parabéns! Você conseguiu. | A cena com os botões deve voltar
54| O jogador deve escolher o botão onboarding | Uma nova cena deve abrir | O jogador deve clicar no personagem e analisá-los
55| O jogador deve escolher o melhor funcionário | Se a resposta for correta deve aparecer: Parabéns você conseguiu | A cena do escritório deve voltar
56| Se a resposta for a errada deve aparecer Tente novamente | O jogador deve escolher novamente um funcionário | Se a resposta for correta deve aparecer: Parabéns! Você conseguiu.
57| A cena com os botões deve voltar | O jogador deve escolher Seleção de fornecedores | A cena com as pastas deve abrir
58| A nova cena deve aparecer | As pastas devem ser arrastadas até a prancheta | A pasta se transformará em textos
59| O jogador deve arrastar o texto da prancheta | A pasta deve aparecer novamente | O texto deve desaparecer
60| O jogador deve arrastar o papel até o lixo ou a pasta | A resposta aparecerá como 'error' em caso de erro e "congratulations" em caso de acerto | A pasta deverá sumir 
61| O jogador deve arrastar todas as pastas | O jogador deve voltar para a cena dos botões | O jogador deve escolher o botão terminar


<div align="center">
<sub>Material produzido pelos autores (2024)<sub>
</div>

## 5.2. Testes de jogabilidade (playtests)

### 5.2.1 Registros de testes 

&nbsp;&nbsp;&nbsp;&nbsp; Os casos de teste são essenciais para garantir a qualidade do jogo, descrevendo condições de entrada, passos e resultados esperados. Este conjunto abrange vários cenários para validar funcionalidade, desempenho e robustez, visando identificar falhas e entregar o melhor do nosso jogo ao parceiro. Os respectivos testes foram realizados por alunos do Atêlie 03, no Atêlie 04 durante a intrução de UX. Na data de 5 de março de 2024, a partir das 11h da manhã até 12h, tendo duração de 10 minutos por teste. O teste 01 foi realizado no dispositivo de Fernando Soares de Oliveira, o teste 02 foi realizado no dispositivo de Leonardo Ogata Pedrosa e os testes 03, 04 e 05 foram realizados no dispotivo de Davi Abreu da Silveira.

<div align="center">
<sub>Quadro 06 - Caso de teste 01</sub>
</div>

Nome | Felipe Campos
--- | ---
Já possuía experiência prévia com games? | Sim, jogador casual
Conseguiu iniciar o jogo? | Sim
Entendeu as regras e mecânicas do jogo? | As mecânicas não ficaram claras
Conseguiu progredir no jogo? | Sim, mas com dificuldades
Apresentou dificuldades? | Sim, principalmente com as colisões e as faltas de instruções (O jogador não localizou com facilidade o "aviso", mas a fase 1 foi entendida completamente).
Que nota deu ao jogo? | 8,0
O que gostou no jogo? | A fase 1, onde é possível ler os formulários
O que poderia melhorar no jogo? | Instruções básicas nas mecânicas e jornada da onde o jogador deve ir

<div align="center">
<sub>Quadro 07 - Caso de teste 02</sub>
</div>

Nome | Marina Oliveira
--- | ---
Já possuía experiência prévia com games? | Sim, jogava
Conseguiu iniciar o jogo? | Sim
Entendeu as regras e mecânicas do jogo? | Conseguiu compreender as mecânicas, mas com dificuldades                                                          
Conseguiu progredir no jogo? | Mais ou menos
Apresentou dificuldades? | Sim, teve problemas por ser pouco intuitivo
Que nota deu ao jogo? | 8,5
O que gostou no jogo? | Gostou das animações. Achou o personagem ótimo
O que poderia melhorar no jogo? | Jogo mais intuitivo, poderiam ter instruções indicando como iniciar os minigames, além de não entender onde deveria ir

<div align="center">
<sub>Quadro 08 - Caso de teste 03</sub>
</div>

Nome | Lucas Mendes
--- | ---
Já possuía experiência prévia com games? | Sim, jogava casualmente
Conseguiu iniciar o jogo? | Sim
Entendeu as regras e mecânicas do jogo? | Não conseguiu compreender completamente as mecânicas, por terem poucas instruções visuais. As regras foram entendidas facilmente
Conseguiu progredir no jogo? | Sim
Apresentou dificuldades? | Sim, apresentou dificuldades para se movimentar pelo mapa
Que nota deu ao jogo? | 8,0
O que gostou no jogo? | Achou o jogo bonito com um ótimo mapa
O que poderia melhorar no jogo? | A instrução para utilizar os controles do personagem, além de melhorar o zoom da câmera

<div align="center">
<sub>Quadro 09 - Caso de teste 04</sub>
</div>

Nome | Amanda Santos
--- | ---
Já possuía experiência prévia com games? | Sim, jogava casualmente
Conseguiu iniciar o jogo? | Sim
Entendeu as regras e mecânicas do jogo? | Não compreendeu as instruções. Porém, entendeu as mecânicas
Conseguiu progredir no jogo? | Sim
Apresentou dificuldades? | Sim, apresentou dificuldades para se encontrar pelo cenário
Que nota deu ao jogo? | 7,0
O que gostou no jogo? | Achou a cutscene do início muito boa
O que poderia melhorar no jogo? | A velocidade do nosso personagem, estava muito rápido, dificultando a movimentação pelo mapa                              

<div align="center">
<sub>Quadro 10 - Caso de teste 05</sub>
</div>

Nome | Gabriel Costa
--- | ---
Já possuía experiência prévia com games? | Sim, jogava casualmente
Conseguiu iniciar o jogo? | Sim
Entendeu as regras e mecânicas do jogo? | Conseguiu compreender as mecânicas e as regras
Conseguiu progredir no jogo? | Sim
Apresentou dificuldades? | Sim, encontrou problemas com bugs no mapa
Que nota deu ao jogo? | 8,0
O que gostou no jogo? | Gostou da movimentação, e da proposta apresentada no jogo. Achou muito bom os assets usados
O que poderia melhorar no jogo? | Deixar o jogo mais intuitivo. Mostrando instruções na tela de como jogar o primeiro minigame                                      

<div align="center">
<sub>Material produzido pelos autores (2024)<sub>
</div>

### 5.2.2 Melhorias

&nbsp;&nbsp;&nbsp;&nbsp; Com base nos resultados dos testes de jogabilidade, podemos identificar algumas áreas que precisam de expansões no jogo. Ao analisar o feedback dos jogadores e observar seu comportamento durante as sessões de testes, fica evidente que algumas características precisam ser aprimoradas para proporcionar uma experiência mais envolvente e imersiva.

<div align="center">
<sub>Quadro 11 - Expansões</sub>
</div>

Expansão | Motivo
--- | ---
Clareza das mecânicas e instruções | Os testadores apresentaram dificuldades em entender as mecânicas do jogo e as instruções fornecidas não foram claras o suficiente. Podemos melhorar isso, a partir de tutoriais mais abrangentes e instruções visuais mais detalhadas, especialmente nas fases iniciais do jogo.
Intuitividade do jogo | Os jogadores tiveram dificuldades devido à falta de intuição no jogo. Isso pode ser resolvido mostrando ao jogador os controles na tela, tornando as interações mais intuitivas e oferecendo dicas contextuais ao desenvolver das mecânicas.
Navegação no mapa | Algumas pessoas enfrentaram problemas para se movimentar pelo mapa. Melhorar a navegabilidade do mapa e fornecer indicadores de direção mais claros pode auxiliar os jogadores a se orientarem melhor no ambiente do jogo.
Correção de bugs | Alguns jogadores relataram problemas com bugs no mapa, o que pode prejudicar a experiência. É importante corrigir esses bugs para garantir uma jogabilidade suave e livre de problemas técnicos.
Melhorias visuais | Embora os aspectos visuais foram elogiados, ainda há espaço para melhorias, como aumentar o zoom da câmera, melhorar a velocidade do personagem e tornar o jogo esteticamente mais atraente.

<div align="center">
<sub>Material produzido pelos autores (2024)<sub>
</div>

# <a name="c6"></a>6. Conclusões e trabalhos futuros 

&nbsp;&nbsp;&nbsp;&nbsp; O jogo contextualiza o processo de contratação de fornecedores diversos na Meta, fornecendo uma visão detalhada dos valores fundamentais da empresa. Ele permite que os jogadores entendam o ambiente em que operam e como as decisões de contratação se encaixam nesse contexto. O jogo proporciona uma experiência imersiva e educativa, simplificando o processo de contratação de fornecedores e alinhando-o aos valores da Meta. Isso ajuda a aumentar o engajamento dos funcionários e a facilitar o entendimento do processo.
<br></br>

<div align="center">
<sub>Quadro 12 - Pontos fortes da solução do jogo</sub>
</div>

Pontos fortes | Explicação
--- | ---
Abordagem educativa e imersiva | O jogo oferece uma maneira envolvente de aprender sobre o processo de contratação de fornecedores, tornando-o mais acessível e compreensível para os funcionários.
Integração de valores da empresa | O jogo incorpora os valores fundamentais da Meta em todo o processo de contratação, garantindo que os jogadores estejam alinhados com a missão e visão da empresa.
Adaptação aos diferentes perfis dos jogadores | O jogo leva em consideração a diversidade de experiências e habilidades dos funcionários da Meta, oferecendo uma experiência personalizada para cada jogador.
<div align="center">
<sub>Material produzido pelos autores (2024)<sub>
</div>
<br></br>
<div align="center">
<sub>Quadro 13 - Pontos a expandir</sub>
</div>

Pontos a se aprofundar | Explicação
--- | ---
Detalhação da interatividade | O jogo poderia incluir mais interações e ramificações na história, proporcionando uma experiência mais dinâmica e intuitiva.
Melhoria da jogabilidade | Algumas partes do jogo podem ser refinadas para tornar a experiência mais fluida para os jogadores.
<div align="center">
<sub>Material produzido pelos autores (2024)<sub>
</div>

<br></br>

&nbsp;&nbsp;&nbsp;&nbsp; Para aprimorar o jogo, estamos planejando implementar uma série de medidas. Primeiramente, pretendemos adicionar mais opções de interação e tomada de decisões ao longo do jogo. Acreditamos que isso aumentará significativamente o envolvimento dos jogadores, proporcionando uma experiência mais dinâmica e personalizada. Outra área que estamos focando é a promoção da diversidade na seleção de fornecedores dentro do jogo. Pretendemos incorporar elementos que destaquem a importância da inclusão e equidade, incentivando os jogadores a considerarem uma variedade de fornecedores em suas decisões. Isso não só reflete os valores da Meta, mas também enriquece a experiência do jogo ao apresentar uma gama mais ampla de perspectivas e oportunidades. 

&nbsp;&nbsp;&nbsp;&nbsp; Por fim, estamos comprometidos em manter o jogo atualizado e relevante ao longo do tempo. Isso significa que estaremos atentos ao feedback dos jogadores e às mudanças no ambiente de negócios da Meta. Planejamos realizar atualizações regulares com base nessas informações, garantindo que o jogo continue a fornecer uma experiência educativa e envolvente para os funcionários da Meta.

&nbsp;&nbsp;&nbsp;&nbsp; Pensando em futuras expansões, estamos considerando várias ideias para enriquecer ainda mais o jogo. Uma delas é a introdução de elementos de realidade aumentada, proporcionando uma experiência ainda mais imersiva aos jogadores. Essa adição pode tornar o jogo mais envolvente, a partir da integração ao Meta Quest 3. Isso inclui abordar questões legais, éticas ou de sustentabilidade relacionadas à seleção de fornecedores. Essa diversificação permitirá uma cobertura mais abrangente, oferecendo oportunidades de aprendizado mais especializadas e direcionadas. 

&nbsp;&nbsp;&nbsp;&nbsp; Por último, estamos considerando parcerias com desenvolvedores de jogos e especialistas em educação. Essas parcerias poderiam ajudar a aprimorar a qualidade e eficácia do jogo, garantindo que ele atenda aos mais altos padrões de engajamento e educação. Visando tornar o jogo uma ferramenta ainda mais valiosa para a equipe da Meta, contribuindo para seu desenvolvimento profissional e sucesso organizacional.

# <a name="c7"></a>7. Referências

[1] DAS, Priona. The 10 Biggest Competitors Of Facebook. 11 de agosto de 2023. Disponível em: https://www.feedough.com/facebook-competitors/. Acesso em: 1 mar. 2024 <br>

[2] META, Facebook. Transforming supplier diversity. Disponível em: https://www.facebook.com/suppliers/diversity/mission-and-values/. Acesso em: 1 mar 2024 <br>

[3] META, Facebook. Responsible Supply Chain. Disponível em: https://sustainability.fb.com/responsible-supply-chain/. Acesso em: 1 mar 2024 <br>

[4] Gushiken, Amanda. Value Proposition Canvas: o que é e como funciona essa metodologia?. 26 de julho de 2023. Disponível em: https://g4educacao.com/portal/value-proposition-canvas. Acesso em: 29 fev 2024 <br>

[5] Werneck, Vivi. 10 jogos de simulação para PS4, Xbox One, Switch e PC. Disponível em: https://rb.gy/aolqan. Acesso em: 1 mar 2024 <br>

[6] CARDOSO, Bruna. Jogos de estratégia? Saiba o significado desse tipo de game. Disponível em: https://seugame.com/o-que-sao-jogos-de-estrategia/. Acesso em: 1 mar 2024 <br>

[7] Cafagne, Tomás. O que são Adventure Games?. Disponível em: http://www.larp.mae.usp.br/o-ultimo-banquete-em-herculano/o-que-sao-adventure-games/. Acesso em: 1 mar 2024 <br>

# <a name="c8"></a>Anexos

Não se aplica.
