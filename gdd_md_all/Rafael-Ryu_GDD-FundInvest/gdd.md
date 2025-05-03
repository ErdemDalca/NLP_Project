

# GDD - Game Design Document - Módulo 1 - Inteli

**_Os trechos em itálico servem apenas como guia para o preenchimento da seção. Por esse motivo, não devem fazer parte da documentação final_**

## Fund Invest

## 👨‍🎓 Integrantes: 
- <a href="http://www.linkedin.com/in/clara-benito">Clara Benito</a>
- <a href="https://www.linkedin.com/in/gabriel-mutter-de-souza-9a0131351">Gabriel Souza</a> 
- <a href="https://www.linkedin.com/in/victorbarq/">Luisa Mangini</a> 
- <a href="www.linkedin.com/in/pietro-alkmin">Pietro Alkmin</a>
- <a href="https://www.linkedin.com/in/rafael-nakahara-bb5100351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Rafael Ryu Tati Nakahara</a> 
- <a href="https://www.linkedin.com/in/sara-maria-farencena-sbardelotto-3b8154275?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Sara Sbardelotto</a>
- <a href="https://www.linkedin.com/in/yudi-omaki">Yudi Omaki</a>



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

## 1.1. Plano Estratégico do Projeto

&emsp; Esta seção apresenta o plano estratégico do projeto, que tem como objetivo estabelecer as diretrizes fundamentais para orientar sua execução e garantir o alcance dos objetivos definidos. O planejamento estratégico é essencial para alinhar as ações às metas estabelecidas, promovendo o crescimento sustentável e o sucesso do projeto.

### 1.1.1. Contexto da Indústria

#### Segmento de Atuação

&emsp; O **BTG Pactual** atua predominantemente na área de investment banking, expandindo suas operações para outros segmentos. Essa diversificação o posiciona como um dos maiores bancos de investimento da América Latina, desempenhando um papel fundamental no mercado financeiro brasileiro e global.


#### Contexto da Indústria/Mercado

&emsp; O mercado financeiro tem passado por profundas transformações, impulsionadas pelo crescente desenvolvimento tecnológico, pela digitalização dos serviços e pelo aumento da competitividade. Os bancos de investimento enfrentam o desafio de se adaptarem rapidamente a esse cenário, inovando para atender às crescentes demandas dos clientes, especialmente diante da ascensão das fintechs.

#### Atividades Principais

&emsp; O BTG Pactual é um banco de investimento com atuação em diversas áreas do mercado financeiro. Suas principais atividades incluem:

1. **Assessoria Financeira:** O banco oferece consultoria especializada para operações complexas, como fusões, aquisições, reestruturação de empresas e captação de recursos, atendendo tanto empresas quanto governos.
2. **Gestão de Investimentos:** Administra fundos e carteiras personalizadas, ajustando estratégias conforme o perfil de risco e os objetivos dos clientes. Seu foco principal está em clientes de alta renda.
3. **Operações de Crédito:**  Disponibiliza diversas opções de financiamento e produtos de crédito, tanto para empresas quanto para pessoas físicas, expandindo sua base de clientes.
4. **Corretagem:** Atua como intermediário na negociação de ativos financeiros, garantindo eficiência na compra e venda de ações, títulos de renda fixa e outros investimentos[4](#ref4)

#### Abrangência das Atividades (Âmbito Internacional, Nacional e Regional)

&emsp; Embora tenha iniciado suas operações no Brasil, o BTG Pactual expandiu sua atuação internacionalmente, estabelecendo escritórios em diversos países da América Latina e em importantes centros financeiros globais. Essa expansão oferece vantagens estratégicas, como a diversificação das fontes de receita e o acesso a novas oportunidades de negócios em diferentes mercados. Com isso, a instituição fortalece sua competitividade tanto no cenário nacional quanto no internacional.

&emsp; O setor de investment banking é altamente competitivo, com empresas disputando espaço por meio da oferta de serviços financeiros personalizados, assessoria para fusões e aquisições, crédito estruturado e intermediação de ativos financeiros. Além disso, as fintechs têm ganhado relevância ao oferecer soluções inovadoras, menores custos operacionais e experiências digitais simplificadas. Esse movimento tem atraído um público crescente para investimentos e assessoria financeira.[2](#ref2)

&emsp; O segmento de gestão de investimentos (Asset Management) também está em expansão, impulsionado pelo aumento da procura por fundos ESG (Environmental, Social and Governance), ativos alternativos e estratégias sustentáveis. A concorrência entre bancos tradicionais e plataformas digitais exige inovação constante para atender a diferentes perfis de investidores.

&emsp; Por fim, a chegada de novos entrantes no setor financeiro, como fintechs e bancos digitais, representa uma ameaça aos modelos tradicionais. Esses novos players apostam em estruturas ágeis, eliminação de tarifas e acessibilidade digital para captar clientes que antes dependiam exclusivamente das grandes instituições. Esse cenário pressiona os bancos tradicionais a modernizarem seus serviços e adotarem tecnologias como blockchain e Big Data para manterem sua competitividade.[1](#ref1).

#### Principais Tendências do Mercado

&emsp; O setor financeiro está em constante evolução, impulsionado por novas tecnologias e mudanças regulatórias. Uma das principais tendências é a expansão do Open Finance, regulamentado pelo Banco Central, que permite o compartilhamento seguro de informações financeiras entre instituições. Essa iniciativa promove maior concorrência e personalização dos serviços oferecidos aos clientes.

&emsp; Outro destaque é o crescimento dos investimentos sustentáveis. A demanda por fundos ESG (Environmental, Social and Governance) tem aumentado significativamente, impulsionada por investidores que buscam rentabilidade alinhada a critérios ambientais, sociais e de governança. Esse movimento reflete uma mudança no comportamento dos investidores em busca de impacto positivo.

&emsp; Além disso, a adoção de inteligência artificial e Big Data tem transformado o setor financeiro. Bancos utilizam essas tecnologias para otimizar a tomada de decisões, personalizar serviços financeiros e reduzir riscos operacionais. Ferramentas como análise preditiva têm permitido maior eficiência na gestão de dados e na mitigação de fraudes.

&emsp; A digitalização do mercado financeiro também tem ganhado força com o avanço dos bancos digitais e corretoras 100% online. Esse cenário tem acelerado a transformação digital, levando as instituições tradicionais a investirem em experiências mais ágeis e intuitivas para os consumidores.

&emsp; Por fim, a tokenização de ativos e o uso da tecnologia blockchain estão revolucionando setores como crédito, investimentos e pagamentos internacionais. Contratos inteligentes baseados em blockchain têm ampliado a eficiência operacional e reduzido custos, tornando essas tecnologias fundamentais para o futuro do mercado financeiro.[3](#ref3)

#### 1.1.1.1. Modelo de 5 Forças de Porter

&emsp; O modelo das **Cinco Forças de Porter**, desenvolvido por Michael Porter na década de 1970, é uma ferramenta clássica da administração estratégica que tem como objetivo analisar o grau de atratividade e competitividade de um setor. Ao examinar cinco dimensões centrais do ambiente externo, o modelo permite compreender como se estruturam as relações de poder entre empresas, fornecedores, clientes, concorrentes e possíveis substitutos.

&emsp; As forças avaliadas pelo modelo são: **rivalidade entre concorrentes existentes**, **ameaça de novos entrantes**, **poder de barganha dos fornecedores**, **poder de barganha dos clientes** e **ameaça de produtos substitutos**. Por meio dessa análise, é possível identificar os fatores que influenciam a intensidade da concorrência e a rentabilidade do setor.

&emsp; Ao compreender essas dinâmicas, as empresas podem formular estratégias mais eficazes para se posicionarem no mercado. Isso inclui buscar diferenciação, obter vantagem competitiva e garantir sustentabilidade no longo prazo.



<div align="center">

*FIGURA 1 - As 5 Forças de Porter (BTG Pactual).*

![imagem forcas porter](/assets/imagens_GDD/5forcasdeporter.png) 


<sub>Fonte: exmerare.com. | Fonte: Template disponível em Canva, adaptado por Bold & Thrive, 2025.</sub>

</div>

&emsp; No contexto do projeto, esse modelo será aplicado para compreender os desafios e oportunidades do setor de jogos digitais com foco em educação financeira no mercado brasileiro, revelando onde estão os riscos e quais fatores podem ser explorados para ampliar o impacto e a relevância do jogo BTG. Realizamos uma análise utilizando o modelo de Porter (**figura 1**).

### Rivalidade entre Concorrentes

&emsp; O setor bancário brasileiro é altamente competitivo, especialmente no segmento de bancos de investimento. O BTG Pactual disputa espaço com instituições tradicionais, como **Itaú BBA**, **Bradesco BBI** e **Santander CIB**, além de players internacionais, como **Goldman Sachs** e **J.P. Morgan**. Esses concorrentes buscam constantemente oferecer produtos financeiros sofisticados, atendimento personalizado e soluções digitais que atendam às demandas de empresas e investidores.

&emsp; No campo da capacitação interna, a disputa também se manifesta por meio de metodologias inovadoras de treinamento corporativo. Empresas concorrentes investem em universidades corporativas, plataformas digitais exclusivas e consultorias especializadas, o que exige do BTG soluções que aliem eficiência e cultura institucional. Para se destacar, é fundamental que o banco invista em abordagens que combinem tecnologia, personalização e engajamento contínuo.

### Ameaça de Novos Entrantes

&emsp; Embora o setor financeiro tenha **barreiras de entrada elevadas**, como regulamentações rígidas, necessidade de capital robusto e exigência de confiança institucional, a digitalização tem reduzido parte dessas barreiras. O surgimento de **fintechs** e **bancos digitais**, com modelos mais ágeis e centrados na experiência do usuário, representa uma ameaça crescente, especialmente em nichos de atuação específicos.

&emsp; No contexto da capacitação de novos analistas, a ameaça também está presente: startups e plataformas de **treinamento corporativo digital** vêm oferecendo soluções escaláveis, modulares e mais acessíveis, que podem atrair instituições em busca de otimização de tempo e custo. O BTG, portanto, precisa se antecipar a esses movimentos, oferecendo experiências formativas que valorizem a cultura da empresa e promovam diferenciação estratégica.

### Ameaça de Produtos Substitutos

&emsp; Existem diversas alternativas aos treinamentos internos tradicionais, como cursos online (Coursera, Alura, Udemy for Business), **plataformas de e-learning white label**, **treinamentos presenciais** e até **mentorias personalizadas**. Essas soluções competem com qualquer proposta de capacitação interna — inclusive com o jogo desenvolvido pelos estudantes.

&emsp; Por isso, é essencial que o BTG, ao adotar uma solução como o jogo, garanta que ela tenha **diferenciais claros**, como alta interatividade, adaptação ao contexto da empresa, aplicação prática dos conceitos e engajamento gamificado. Somente assim será possível justificar sua escolha frente aos substitutos mais tradicionais ou generalistas.

### Poder de Barganha dos Clientes

&emsp; No mercado financeiro, os **clientes institucionais** do BTG (empresas, investidores e grandes corporações) possuem um alto grau de exigência e grande poder de escolha. A fidelização depende da performance, credibilidade e atendimento personalizado. Isso exige do banco diferenciais contínuos — inclusive no investimento em talentos internos.

&emsp; Já no contexto do projeto do jogo, o **cliente interno** é o próprio BTG. A empresa possui total poder de decisão sobre a adoção, continuidade ou descarte da solução. Se o produto não corresponder às expectativas de qualidade, aplicabilidade e alinhamento à cultura institucional, pode ser facilmente substituído. Por isso, o projeto precisa ser construído com foco claro nas necessidades reais do banco, garantindo aderência aos seus valores e padrões de excelência.

### Poder de Barganha dos Fornecedores

&emsp; Para o BTG, os fornecedores incluem sistemas bancários, provedores de tecnologia, infraestrutura de TI, serviços terceirizados e parceiros educacionais. O grau de poder de barganha varia de acordo com a especialização dos serviços e a disponibilidade de alternativas no mercado.

&emsp; - **Alta barganha:** tecnologias específicas e consultorias de alto nível

&emsp; - **Média:** plataformas de treinamento licenciadas ou customizadas

&emsp; - **Baixa:** serviços operacionais ou genéricos, com ampla concorrência

&emsp; No caso do jogo desenvolvido por estudantes, o BTG atua como patrocinador e não depende diretamente de fornecedores críticos, o que diminui a vulnerabilidade. Ainda assim, a entrega final precisa atender aos padrões esperados para que seja considerada competitiva frente a fornecedores profissionais.

### Considerações Finais

&emsp; A análise das Cinco Forças de Porter evidenciou os principais fatores que impactam o posicionamento do BTG Pactual no setor financeiro. O cenário competitivo exige inovação constante e atenção às novas soluções digitais. Nesse contexto, iniciativas como o jogo desenvolvido podem representar uma estratégia relevante ao oferecer uma experiência de capacitação alinhada à cultura do banco, reforçando seu diferencial diante dos concorrentes e substitutos.

### 1.1.2. Análise SWOT

&emsp; A matriz SWOT é um método de planejamento estratégico que auxilia empresas na tomada de decisões. Essa ferramenta analisa fatores internos e externos, organizando-os em quatro categorias: Strengths (Forças) e Weaknesses (Fraquezas), que pertencem ao ambiente interno, e Opportunities (Oportunidades) e Threats (Ameaças), que se referem ao ambiente externo. O objetivo da análise é identificar os principais pontos que influenciam o projeto, compreendendo quais fatores estão sob seu controle direto (internos) e quais escapam ao seu alcance (externos).

&emsp; O ambiente externo envolve fatores que não estão sob o controle direto do projeto, como dinâmicas de mercado, inovações tecnológicas, mudanças sociais e decisões políticas. Esses elementos influenciam diretamente as oportunidades — cenários favoráveis que podem ser aproveitados — e as ameaças, que representam riscos potenciais ao desempenho do projeto. Embora não sejam controláveis, esses fatores devem ser constantemente monitorados para que o projeto possa se adaptar com eficiência e manter um posicionamento estratégico diante das transformações do contexto.

&emsp; Por outro lado, os aspectos internos dizem respeito a fatores que estão sob o controle direto do projeto, como estrutura organizacional, recursos disponíveis, competências técnicas e processos internos. As forças correspondem a elementos que oferecem vantagens competitivas e diferenciam o projeto no mercado, enquanto as fraquezas representam limitações que podem comprometer seu desempenho ou dificultar sua consolidação. Reconhecer esses pontos permite à equipe agir de forma estratégica, potencializando aquilo que já é positivo e corrigindo fragilidades antes que se tornem entraves ao desenvolvimento.



<div align="center">

*FIGURA 2 - Análise SWOT (BTG Pactual).*

![imagem swot](/assets/imagens_GDD/SWOT.png) 


<sub>Fonte: Template disponível em Canva, adaptado por Bold & Thrive, 2025.</sub>

</div>

### 1.1.3. Missão / Visão / Valores (sprint 2)

&emsp; A partir dessa leitura estratégica, a matriz SWOT se mostra fundamental para o posicionamento do projeto, justamente por evidenciar a interdependência entre os elementos analisados. Uma alteração em qualquer um dos fatores, sejam internos ou externos, pode influenciar diretamente os demais, o que reforça a importância de uma abordagem integrada. Uma estratégia eficaz, portanto, depende da capacidade de potencializar os pontos fortes, corrigir as fragilidades, aproveitar as oportunidades e minimizar os riscos. Ao aplicar essa lógica ao jogo BTG, é possível direcionar os recursos, que são naturalmente limitados, de forma mais inteligente, garantindo que o projeto avance com consistência e esteja preparado para se adaptar às mudanças do ambiente.

&emsp; Diante da análise SWOT, foi possível identificar características essenciais do projeto, como a credibilidade da marca BTG e sua forte expertise no mercado financeiro, além de limitações como a ausência de uma estrutura física e a total dependência do meio digital. Entre as oportunidades destacam-se o crescente interesse por educação financeira e a ampla aceitação de soluções gamificadas. Diante desse cenário, o jogo foi concebido como uma resposta estratégica: uma ferramenta interativa que potencializa os pontos fortes, busca superar as fragilidades e explora as oportunidades para promover uma experiência educativa eficaz e envolvente.


### 1.1.3. Missão / Visão / Valores

&emsp; A missão, visão e valores do BTG Pactual refletem seu compromisso com a inovação no setor financeiro, a busca pela excelência e a construção de um mercado mais eficiente. Esses princípios orientam tanto a atuação da empresa quanto o desenvolvimento de novas soluções, como o jogo de onboarding para analistas.

### Missão
&emsp; Oferecer soluções financeiras inovadoras e de alta performance, auxiliando clientes e investidores a alcançar seus objetivos estratégicos. No contexto do projeto, essa missão se traduz na criação de um jogo interativo que agiliza o processo de onboarding de novos analistas, tornando-o mais eficiente e acessível.

### Visão
&emsp; Ser referência global em serviços financeiros, combinando tecnologia e expertise para transformar o mercado de investimentos. A visão do projeto está alinhada a essa meta, ao propor um treinamento inovador que capacita os novos analistas com uma abordagem prática e dinâmica.

### Valores
&emsp; **Foco no Cliente:** Desenvolver soluções que atendam às necessidades e expectativas dos clientes com excelência.


&emsp; **Inovação:** Utilizar tecnologia e conhecimento para criar soluções financeiras diferenciadas.


&emsp; **Ética e Transparência:** Atuar com integridade, responsabilidade e compromisso com o mercado.
Compromisso com a Melhoria Contínua: Buscar constantemente evolução e excelência nos processos e resultados.


&emsp; **Empreendedorismo:** Incentivar a proatividade e a busca por oportunidades de crescimento e desenvolvimento.


### 1.1.4. Proposta de Valor

&emsp; O Canvas Proposta de Valor é uma ferramenta de planejamento estratégico que auxilia empresas na análise e compreensão de seu público-alvo, considerando suas dores, necessidades e desejos (SOMOS TERA, 2025). Essa metodologia permite a tomada de decisões assertivas no desenvolvimento de produtos ou serviços, garantindo maior alinhamento às expectativas dos clientes. <br>

&emsp; Composto por uma representação gráfica cujo objetivo é conectar o cliente à solução, o Canvas facilita a visualização e comparação das principais questões dos clientes (lado direito) em relação à proposta de valor da empresa (lado esquerdo). <br>

&emsp; Nos segmentos de clientes, são analisados três aspectos principais: dores, ganhos e tarefas. As dores representam os problemas enfrentados pelos clientes que os impedem de alcançar seus objetivos, sendo os motivos para que eles busquem um produto ou serviço. Os ganhos correspondem aos benefícios que os clientes obtêm ao adquirir a solução correta, superando suas expectativas tanto em quantidade quanto em qualidade. Já as tarefas dizem respeito às atividades que os clientes realizam ou tentam executar no dia a dia, gerando demandas por novos produtos ou serviços. Esses três elementos são avaliados em conjunto para criar uma solução eficaz e personalizada. <br>

&emsp; Na proposta de valor, são trabalhadas as soluções para as questões identificadas nos segmentos de clientes. Os analgésicos visam aliviar as dores dos clientes, oferecendo soluções específicas para cada problema identificado. Para isso, é essencial considerar a relação custo-benefício da entrega do produto ou serviço e garantir que ele realmente atenda às necessidades avaliadas. Os criadores de ganho consistem em desenvolver produtos ou serviços que agreguem valor aos clientes, atendendo aos desejos e necessidades previamente analisados. Por fim, os produtos e serviços conectam diretamente a solução proposta aos segmentos de clientes, consolidando tudo o que foi desenvolvido. <br>

&emsp; Dessa forma, ao aplicar o Canvas Proposta de Valor ao projeto FundInvest, detalhamos a seguir como cada elemento do modelo foi relacionado à proposta do jogo:
Tarefas dos clientes: aprender sobre a área de fundos de investimento e a cultura do BTG, além de completar o processo de onboarding de forma eficaz.


&emsp;**Dores**: o processo de onboarding tradicional era considerado cansativo e pouco envolvente, gerando uma integração lenta e ineficiente.

&emsp;**Ganhos esperados**: os novos analistas desejam uma integração mais rápida, interativa e que proporcione aprendizado dinâmico dos conceitos da área.

&emsp;**Produtos e serviços**: o FundInvest oferece ensino sobre fundos de investimento e cultura BTG por meio de minigames intuitivos e envolventes.

&emsp;**Analgésicos**: o jogo torna o onboarding mais leve e atrativo, minimizando a sensação de sobrecarga e tornando o processo mais eficiente.

&emsp;**Criadores de ganho**: a gamificação acelera a inserção dos analistas na área, ao mesmo tempo em que promove maior engajamento e retenção de conhecimento.


&emsp; A figura 3 apresenta o Canvas Proposta de Valor do FundInvest, evidenciando a conexão entre os segmentos de clientes e a proposta de valor desenvolvida.

<div align="center">
    
*FIGURA 3- Canvas Proposta de Valor.* 

![imagem canvas](/assets/imagens_GDD/canvas.png)

<sub>Fonte: Template disponível em Canva, adaptado por Bold & Thrive, 2025</sub>
</div>

&emsp; A partir do Canvas Proposta de Valor apresentado acima, determinamos como a solução proposta pelo jogo FundInvest se conecta diretamente ao segmento de clientes. Por meio dessa análise, identificamos que a principal dor do cliente era enfrentar um processo de onboarding cansativo, que resultava em uma integração lenta e ineficiente. Como resposta, desenvolvemos um jogo com um sistema de minigames intuitivos, tornando a experiência do cliente interativa e dinâmica, além de acelerar e otimizar o processo de integração.

### 1.1.5. Descrição da Solução Desenvolvida

&emsp; O banco BTG Pactual relatou um problema durante o processo de onboarding de seus novos analistas de fundos de investimento. Atualmente, o processo é cansativo e ineficiente, pois exige elevada capacitação técnica e compreensão de negócios por parte do novo analista.

&emsp; Para solucionar essa adversidade, a Bold & Thrive desenvolveu um jogo web com perspectiva top-down, com o objetivo de tornar o processo de onboarding mais dinâmico, intuitivo e eficiente. O jogo utiliza conteúdos e minigames que abordam conceitos técnicos e de negócios de forma interativa, divertida e eficaz.

&emsp; No "FundInvest", o usuário vivencia a experiência de um novo analista de fundos de investimento do banco. Durante o jogo, o analista passará por três andares, onde cada andar representa uma fase composta por quatro minigames distintos. Os objetos e NPCs interativos são sinalizados por meio de um ponto de exclamação na tela, facilitando a experiência do usuário. Para avançar para a próxima fase, é necessário que a taxa de acerto em cada minigame supere 50%.

&emsp; Espera-se que, ao final do jogo, o analista em onboarding tenha absorvido todas as informações do "FundInvest" por meio das perguntas e conteúdos oferecidos ao longo da experiência. Dessa forma, sua integração à área de fundos de investimento e à cultura BTG será mais acelerada e eficiente.

### 1.1.6. Matriz de Riscos

&emsp; A Matriz de Riscos é uma ferramenta visual que facilita o gerenciamento e a classificação de riscos, resultantes da relação entre a probabilidade de ocorrência e a gravidade do impacto caso aconteçam (FERRAMENTAS DA QUALIDADE, 2025). Por meio dela, é possível identificar se os riscos representam ameaças, que podem gerar prejuízos, ou oportunidades, que têm o potencial de melhorar os resultados. Além disso, a matriz auxilia na tomada de decisões e na implementação de medidas preventivas para mitigação dos riscos.Ao analisar as ameaças e oportunidades dos riscos do projeto FundInvest a partir da matriz apresentada, foi possível compreender os desafios enfrentados e as possibilidades de crescimento. As ameaças identificadas, como dificuldades técnicas, desalinhamento com a cultura do BTG e falhas em UI/UX, possuem planos estratégicos de mitigação para minimizar impactos negativos e garantir uma experiência completa ao usuário. 

&emsp; Além disso, as oportunidades destacadas enfatizam a capacidade interativa do projeto, que permite ajustes estratégicos conforme necessário. Acompanhando de perto esses riscos e adotando medidas preventivas intencionais, a equipe está preparada para transformar ameaças em oportunidades, garantindo a entrega de um jogo que proporcione um processo de onboarding interativo e dinâmico.


&emsp; A seguir encontra-se o quadro de probabilidades dos riscos analisados acontecerem:

#### Probabilidade
<div align="center">
    <sub>Quadro 1 - Probabilidade</sub>
</div>

<table border="1" align="center">
    <tr>
        <th>Probabilidade Numérica</th>
        <th>Descrição dos critérios de probabilidade</th>
    </tr>
    <tr>
        <td>10%</td>
        <td>Não é provável que aconteça</td>
    </tr>
    <tr>
        <td>30%</td>
        <td>Pode ser que ocorra uma vez dentro de um ano</td>
    </tr>
    <tr>
        <td>50%</td>
        <td>Pode ser que ocorra mais de uma vez dentro de um ano</td>
    </tr>
    <tr>
        <td>70%</td>
        <td>Pode ser que ocorra mensalmente</td>
    </tr>
    <tr>
        <td>90%</td>
        <td>Pode ser que ocorra semanalmente</td>
    </tr>
</table>

<div align="center">
    <sub>Fonte: Bianca Minetto Napoleão (2019)</sub>
</div>
<br>

&emsp; Veja abaixo o quadro que mostra o impacto das consequências dos possíveis riscos a serem analisados:

#### Impacto
<div align="center">
    <sub>Quadro 2 - Probabilidade</sub>
</div>

<table border="1" align="center">
    <tr>
        <th>Impacto</th>
        <th>Descrição dos critérios de impacto</th>
    </tr>
    <tr>
        <td>Muito baixo</td>
        <td>Os riscos possuem consequências pouco significativas</td>
    </tr>
    <tr>
        <td>Baixo</td>
        <td>Os riscos possuem consequências reversíveis em curto e médio prazo com custos pouco significativos</td>
    </tr>
    <tr>
        <td>Moderado</td>
        <td>Os riscos possuem consequências reversíveis em curto e médio prazo com custos baixos</td>
    </tr>
    <tr>
        <td>Alto</td>
        <td>	Os riscos possuem consequências reversíveis em curto e médio prazo com custos altos</td>
    </tr>
    <tr>
        <td>Muito alto</td>
        <td>Os riscos possuem consequências irreversíveis ou com custos inviáveis</td>
    </tr>
</table>

<div align="center">
    <sub>Fonte: Bianca Minetto Napoleão (2019)</sub>
</div>
<br>

&emsp; A partir do conceito de Matriz de Riscos, considerando fatores internos  externos, a equipe mapeou os riscos do projeto FundInvest e suas potenciais ameaças e oportunidades, que estão representados na imagem a seguir:

<div align="center">

*FIGURA 4 - Matriz de Riscos*

![imagem matriz riscos](/assets/imagens_GDD/matrizRiscos.png)

<sub>Fonte: autoria própria (2025) | Template: Bianca Minetto Napoleão (2019)</sub>

</div>

### Plano de ação contra ameaças:
**Risco 1 - Dificuldade na implementação de mecânicas**
<br> Probabilidade: 70%
<br> Impacto: muito alto
<br> Mitigação: testes contínuos e uso de bibliotecas prontas.

**Risco 2 - Baixa retenção do conteúdo**
<br> Probabilidade: 30%
<br> Impacto: muito alto
<br> Mitigação: testes contínuos para ajustes na experiência do usuário.

**Risco 3 - Baixo engajamento dos analistas**
<br> Probabilidade: 50%
<br> Impacto: alto
<br> Mitigação: ajuste na curva de dificuldade e inclusão de mecânicas de progresso ou recompensas.

**Risco 4 - Desalinhamento com a cultura do BTG**
<br> Probabilidade: 10%
<br> Impacto: muito alto
<br> Mitigação: validação contínua com parceiro.

**Risco 5 - Falha em UI/UX**
<br> Probabilidade: 50%
<br> Impacto: muito alto
<br> Mitigação: HUDs intuitivas e tutoriais claros.

### **Oportunidades encontradas:**
**Oportunidade 1 - Sistema de progressão**
<br> Probabilidade: 70%
<br> Impacto: alto
<br> Aproveitamento: curva de aprendizagem de incentiva os usuários a continuarem engajados e concluírem o onboarding com qualidade.

**Oportunidade 2 - Modelo diversificado**
<br> Probabilidade: 90%
<br> Impacto: muito alto
<br> Aproveitamento: implementação de minigames variados para um onboarding mais interativo e dinâmico.

**Oportunidade 3 - Validação do jogo como ferramenta de treinamento**
<br> Probabilidade: 30%
<br> Impacto: Muito alto
<br> Aproveitamento: onboarding intuitivo e integração acelerada ou, inclusive, expansão para outras áreas da empresa.

**Oportunidade 4 - Produto alinhado à cultura BTG**
<br> Probabilidade: 50%
<br> Impacto: muito alto
<br> Aproveitamento: estudo de casos e testes de novas soluções.

**Oportunidade 5 - Otimização da experiência do usuário (UX)**
<br> Probabilidade: 50%
<br> Impacto: muito alto
<br> Aproveitamento: testes iterativos para coleta de feedback e aprimoramento do jogo.

&emsp; Ao analisar as ameaças e oportunidades dos riscos do projeto FundInvest a partir da matriz acima, foi possível entender os desafios enfrentados e as possibilidades de crescimento. As ameaças identificadas, como dificuldades técnicas, desalinhamento com a cultura BTG e falha em UI/UX, possuem planos de mitigação estratégicos para minimizar impactos negativos e garantir uma experiência completa ao usuário. Também, as oportunidades destacadas enfatizam a capacidade iterativa do projeto, que permite ajustes estratégicos. Acompanhando de perto tais riscos e adotando medidas preventivas intencionais, a equipe está preparada para transformar ameaças em oportunidades, garantindo a entrega de um jogo que contemple um onboarding interativo e dinâmico.

### 1.1.7. Objetivos, Metas e Indicadores

&emsp; O uso da metodologia SMART foi essencial para estruturar os objetivos do projeto de forma clara e estratégica. Por meio de critérios bem definidos, foi possível garantir foco, organização e eficiência no desenvolvimento do onboarding gamificado para os analistas do BTG Pactual, alinhando o planejamento às metas estabelecidas.

<div align="center">
    
*FIGURA 5 - Metas SMART*

</div>

![imagem metas smart](/assets/imagens_GDD/SMART.png)

<div align="center">
<sup>Fonte: Template disponível em Canva, adaptado por Bold & Thrive, 2025.</sup>
</div>

**Definição** <br>
&emsp; A metodologia SMART analisa cinco critérios: específicos, mensuráveis, atribuíveis, realistas e temporais. As metas são utilizadas para que os objetivos sejam definidos de forma clara e eficaz, permitindo que sejam alcançados de maneira mais eficiente.

**Específicas** <br>
&emsp; Tornar o processo de onboarding dos analistas de fundos de investimento do banco BTG Pactual mais interativo e eficiente por meio de um jogo “top-down” com progressão de níveis e desafios ao longo do jogo, abordando conteúdos relacionados à área de fundos e à cultura BTG.

**Mensuráveis** <br>
&emsp; Reduzir o tempo de integração dos novos analistas. Os resultados serão monitorados por meio da progressão nas fases e do desempenho dos jogadores.

**Atribuível** <br>
&emsp; A equipe **Bold & Thrive** é responsável pelo desenvolvimento do projeto.

**Realista** <br> 
&emsp; Criar, em 10 semanas, o MVP de um jogo gamificado e interativo que torne eficaz e acelere o processo de onboarding.

**Temporal** <br>
&emsp; O MVP deve ser entregue dentro do prazo de 10 semanas. A metodologia SCRUM foi utilizada para administrar o tempo de forma eficiente, juntamente com o acompanhamento quinzenal do BTG Pactual para aprovação e feedback do projeto.

&emsp; A utilização da metodologia SMART foi essencial para o alinhamento dos objetivos e a identificação de prioridades dentro dos prazos estabelecidos, garantindo que o objetivo fosse atingido conforme o cronograma. A especificidade tornou os objetivos individuais claros para todos os membros da equipe, além de permitir o acompanhamento do progresso individual, possibilitando ajustes precisos para que a equipe alcance o resultado esperado.

## 1.2. Requisitos do Projeto

&emsp; O projeto **FundInvest** tem como proposta solucionar a problemática apresentada pelo BTG Pactual.

&emsp; O problema envolve o processo de onboarding dos novos analistas de desenvolvimento na área de sistemas de fundos de investimento no BTG Pactual é complexo e lento, o que causa atrasos na adaptação e falhas na integração.

&emsp; Atualmente, o maior desafio para desenvolver esse projeto está em utilizar ferramentas de programação, como Phaser, HTML e JavaScript, além de implementar conceitos de negócios, como análise SWOT e as 5 Forças de Porter, no desenvolvimento do projeto.

&emsp; Este projeto tem como objetivo auxiliar os novos analistas de fundos de investimento no BTG Pactual a vivenciarem um processo de onboarding mais rápido e dinâmico, incorporando quizzes, jogos de conexão de palavras, entre outros.

&emsp; A seguir, são apresentados os requisitos e restrições que a solução deve seguir para garantir um desenvolvimento com qualidade e que atenda às necessidades do stakeholder:

<div align="center">

<sub>Quadro 3 - Requisitos </sub>

</div>
 
\# | Requisito  
--- | ---  
1 | O jogo deve proporcionar, de forma dinâmica e rápida, uma visão introdutória ao mercado de fundos de investimento e um direcionamento a cultura do BTG.
2 | A tela inicial do jogo deve conter as funções de configuração e os botões de start e continuar (ação possível por meio do uso de Cookies).
3 | Para a movimentação do personagem deve-se usar as teclas W, A, S e D, e o modelo de visão top-down.
4 | A versão preliminar de desenvolvimento do jogo deve conter quatro telas (tela inicial, tela de personalização, tela de primeira cena do jogo e tela de configuração).
5 | O foco principal do jogo deve ser a visão geral de fundos de investimento, sem aprofundar totalmente em outros tópicos mais específicos de finanças, garantindo um aprendizado mais focado e completo no tópico escolhido.
6 | O jogo deve rodar na infraestrutura do banco, onde o analista poderá acessar o jogo apenas quando estiver conectado à rede do banco.


## 1.3. Público-alvo do Projeto

&emsp; O público-alvo do jogo são analistas técnicos do BTG Pactual, em processo de onboarding no banco, sendo introduzidos ao setor de fundos de investimento. Esse público é majoritariamente composto por jovens adultos, com formação acadêmica em Ciência da Computação, Engenharia de Software, Sistemas de Informação e áreas correlatas ([5](#ref5)). Muitos estão ingressando no mercado de trabalho ou possuem pouca experiência no setor financeiro, necessitando de uma introdução clara e objetiva aos conceitos de fundos de investimento e aos desafios técnicos da área ([6](#ref6)).

&emsp; Em termos demográficos, embora o setor de tecnologia seja tradicionalmente dominado por homens, o BTG Pactual tem implementado iniciativas para promover a diversidade, como o programa #ElaFazTech, que visa aumentar a representatividade feminina na área de desenvolvimento. Quanto à raça/cor, não há dados específicos disponíveis sobre a composição racial dos analistas técnicos no BTG Pactual. No entanto, o banco afirma valorizar a diversidade e, em seus processos seletivos, não faz distinção de raça, cor, religião, identidade de gênero, orientação sexual, nacionalidade, deficiência ou idade.

&emsp; Em termos de preferências, apuramos que esse público apresenta forte inclinação para tecnologia, inovação e aprendizado interativo. Por serem desenvolvedores, valorizam desafios técnicos, resolução de problemas lógicos e experiências práticas de aprendizado, sendo altamente responsivos à gamificação e metodologias hands-on.([7](#ref7))

&emsp; Os analistas e estagiários dessa geração são nativos digitais, acostumados a interações dinâmicas e recompensadoras, aprendendo melhor por meio de experiências gamificadas, simulações e desafios progressivos. Estudos indicam que 85% dos jovens profissionais se engajam mais quando os treinamentos incluem gamificação e interação([8](#ref8)). Eles respondem bem à mecânicas como sistemas de pontos, conquistas, missões e placares de liderança, que estimulam a competição saudável e incentivam a progressã([9](#ref9)). Além disso, esperam feedback instantâneo, aprendizado ágil e autonomia, tornando essencial que o onboarding seja rápido, eficiente e objetivo.([10](#ref10))

# <a name="c2"></a>2. Visão Geral do Jogo 

&emsp; Este jogo corporativo foi desenvolvido para transformar o processo de onboarding em uma experiência interativa e envolvente. Utilizando elementos de gamificação, ele torna o aprendizado mais dinâmico, permitindo que os novos funcionários assimilem informações essenciais de forma prática e motivadora.

## 2.1. Objetivos do Jogo 

&emsp; No desenvolvimento do jogo corporativo para onboarding, o principal objetivo é acelerar a integração dos novos funcionários, tornando o processo mais dinâmico e interativo. A ideia é transformar o aprendizado em uma experiência envolvente, permitindo que os colaboradores compreendam a cultura, os processos e a estrutura da empresa de forma prática e eficiente. Além disso, o jogo contribui para fortalecer os laços entre os funcionários, ajudando-os a se relacionar melhor com diferentes perfis e a desenvolver habilidades sociais importantes no ambiente de trabalho.

&emsp; Para tornar o onboarding mais eficiente, o jogo substitui treinamentos tradicionais demorados por desafios interativos. Sua estrutura foi pensada para reforçar o conhecimento por meio de minigames que incentivam a participação ativa, tornando o aprendizado mais leve e prático. As informações essenciais são apresentadas de forma intuitiva, facilitando sua aplicação no dia a dia. O progresso dentro do jogo acontece por meio de andares, que representam diferentes níveis de dificuldade. Cada andar possui quatro salas, e em cada sala o jogador responde a três perguntas. Para avançar, é necessário acertar pelo menos nove das doze perguntas disponíveis, com a dificuldade aumentando gradualmente a cada fase.

&emsp; Caso o jogador não alcance o desempenho esperado em um desafio, ele pode assistir a um vídeo explicativo para reforçar o conteúdo. No final de cada módulo, um teste ajuda a revisar os principais pontos aprendidos. Além disso, o jogo foi desenvolvido para garantir a privacidade dos usuários: em vez de armazenar dados em servidores externos, ele utiliza cookies que registram as informações diretamente no console do navegador. Assim, cada jogador pode acompanhar seu próprio progresso sem que a empresa tenha acesso aos resultados, possibilitando revisões sempre que necessário, sem preocupações com monitoramento.

&emsp; Mais do que apenas transmitir conhecimento técnico e processual, o jogo também fortalece as relações interpessoais dentro da empresa. Ele inclui dinâmicas que incentivam a colaboração, o trabalho em equipe e a comunicação eficaz, criando um ambiente mais integrado e participativo. Ao unir aprendizado, interação e gamificação, o jogo transforma o onboarding em um processo mais eficiente e envolvente, garantindo que os novos colaboradores se sintam preparados para suas funções e promovendo um ambiente corporativo mais colaborativo e acolhedor.

## 2.2. Características do Jogo 

&emsp; O FundInvest é um jogo educativo que simula a experiência de um analista de fundos de investimento dentro de um banco, oferecendo desafios progressivos que combinam estratégia e raciocínio lógico. Ele se destaca por proporcionar uma abordagem imersiva e dinâmica ao aprendizado sobre o mercado financeiro, tornando-o mais acessível e envolvente para os jogadores. Inspirado em grandes títulos do gênero, o FundInvest busca engajar os participantes enquanto ensina conceitos financeiros importantes de forma prática e divertida.

### 2.2.1. Gênero do Jogo 

&emsp; É um jogo de puzzles com uma grande variedade de desafios relacionados a fundos de investimento. O jogo se passa dentro de um banco, simulando a experiência de um funcionário do BTG. A dificuldade dos problemas aumenta com o passar das fases e, ao final de cada nível, haverá um Boss Level.

### 2.2.2. Plataforma do Jogo

&emsp; O Fund Invest foi desenvolvido usando a linguagem JavaScript, portanto é um jogo web pensado para usuários desktop.

### 2.2.3. Número de jogadores 

&emsp; É um jogo singleplayer (1 jogador), em que o jogador vivencia a experiência de um analista de fundos de investimento, resolvendo diversas situações do seu dia a dia dentro do banco.

### 2.2.4. Títulos semelhantes e inspirações 

&emsp; O nosso foi inspirado por dois títulos principais: Celeste e The Legend of Zelda.

&emsp; De *Celeste*, fomos inspirados pela seleção de background e estilo de arte que o jogo procura transmitir, transformando nossa forma de imaginar o design do nosso game. Essa inspiração se manifesta na escolha de nossos assets e personagens, sempre buscando provocar uma atmosfera única e agradável.

&emsp; *The Legend of Zelda* nos inspirou na escolha do tipo de câmera que usaríamos. Enquanto a maioria dos jogos 2D utiliza uma movimentação que limita a ação ao plano horizontal, *The Legend of Zelda* adota o estilo top-down. Essa escolha nos permitiu criar ambientes mais amplos e imersivos, aproximando a experiência de um jogo 3D.

### 2.2.5. Tempo estimado de jogo 

&emsp; O tempo estimado para concluir o jogo é de cerca de duas horas, considerando que o jogador não tenha um conhecimento prévio sobre jogos e precise aprender os comandos. No entanto, esse tempo pode variar dependendo da agilidade do jogador.

# <a name="c3"></a>3. Game Design 

&emsp; O design do jogo foi estruturado para proporcionar uma experiência de aprendizado dinâmica e acessível, utilizando mecânicas interativas para facilitar a assimilação dos conteúdos. Nesta seção, são apresentados os principais elementos que compõem o jogo, incluindo sua ambientação, personagens e representatividade.

## 3.1. Enredo do Jogo (sprints 2 e 3)

&emsp; O jogador assume o papel de um analista recém-contratado no Banco BTG, pronto para iniciar sua jornada profissional. No entanto, logo ao chegar, ele descobre que o banco está sob uma ameaça secreta: espiões infiltrados disfarçaram-se de gestores, diretores e até do próprio CEO, tentando roubar informações confidenciais e comprometer a segurança da instituição. Para impedir esse ataque, o jogador precisa utilizar seu conhecimento sobre mercado financeiro, compliance e estratégias de investimento para identificar e eliminar os infiltrados.

&emsp; Cada fase do jogo representa um andar do banco, onde ele deve resolver desafios financeiros para coletar pistas e desmascarar os impostores. A missão começa no primeiro andar, onde o jogador aprende conceitos fundamentais e enfrenta seu primeiro espião, um gestor disfarçado. Conforme avança para os andares superiores, os desafios tornam-se mais difíceis e os espiões mais astutos, exigindo do jogador raciocínio estratégico e domínio das finanças para derrotá-los.

&emsp; No terceiro e último andar, o jogador chega ao confronto final contra o líder dos espiões, que está fingindo ser o CEO do banco. Se conseguir resolver os desafios e identificá-lo, o jogador garante a segurança das informações estratégicas e recebe o reconhecimento de toda a equipe do BTG, sendo oficialmente integrado ao banco.

&emsp; O jogo combina aprendizado e narrativa investigativa, mantendo o jogador engajado ao longo da experiência. Cada decisão, cada resposta e cada desafio vencido aproximam o jogador da verdade, tornando a jornada não apenas educativa, mas também envolvente e estratégica.

## 3.1.3.3 Curva de Dificuldade

&emsp; O balanceamento do jogo é essencial para garantir uma experiência justa, engajante e alinhada aos objetivos do onboarding. O sistema de pontuação foi estruturado para recompensar o acerto imediato e incentivar a progressão do jogador sem penalizações severas. O jogador ganha 100 pontos ao acertar uma pergunta na primeira tentativa, 50 pontos na segunda tentativa e 25 pontos na terceira tentativa. Caso acerte três ou mais questões seguidas, receberá um bônus de 50 pontos. Não há penalidades para erros, mas, caso não atinja o número mínimo de acertos necessários para avançar, precisará assistir a conteúdos explicativos e refazer a fase.

&emsp; A progressão do jogo ocorre de maneira gradual, com fases que evoluem em dificuldade conforme o jogador avança. Não há limite de tempo para responder às perguntas, e o jogador só passa de fase se acertar pelo menos metade delas. Caso contrário, deverá refazer a fase e revisar o conteúdo antes de tentar novamente. Cada fase contém quatro perguntas e não há restrições quanto ao número de erros, o que permite que o jogador aprenda no próprio ritmo, sem frustrações excessivas.

&emsp; Para manter a motivação e o engajamento do jogador, o jogo possui uma música tema de fundo, e uma nova trilha sonora é tocada ao concluir uma fase. O feedback do aprendizado ocorre por meio de vídeos explicativos antes do início das questões e também ao final, caso o jogador tenha um desempenho abaixo do esperado. No entanto, não há dicas durante as perguntas, garantindo que o desafio esteja alinhado ao aprendizado autônomo. Esse balanceamento foi projetado para tornar a experiência de onboarding dinâmica e interativa, permitindo que os novos analistas adquiram conhecimentos essenciais de forma envolvente e eficiente.

&emsp; Na sala 1, serão feitas perguntas introdutórias sobre o assunto, necessárias para responder às perguntas das fases seguintes, como termos básicos e palavras-chave. As perguntas são apresentadas por meio de um minigame baseado na conexão de palavras com seus respectivos significados.

&emsp; Na sala 2, os assuntos abordados na primeira sala são aprofundados e revisados para que o jogador fixe e defina bem os fundamentos. O objetivo do segundo minigame é selecionar a alternativa correta entre as quatro disponíveis para a pergunta, no formato de múltipla escolha.

&emsp; Na sala 3, são abordadas perguntas mais técnicas e complexas sobre fundos de investimento. As perguntas são respondidas no formato de múltipla escolha.

&emsp; Na sala 4, há um Boss level, no qual os temas abordados nas fases anteriores serão integrados em uma pergunta de desafio. O minigame fornece um banco de palavras que deve ser utilizado para o preenchimento das lacunas em branco conforme o contexto da frase.

## 3.2. Personagens 
&emsp; Os personagens do FundInvest foram cuidadosamente desenvolvidos para refletir o ambiente corporativo de um banco e criar conexões significativas com os novos analistas. Cada personagem possui características e funções específicas dentro do jogo, desde o protagonista, controlado pelo jogador, até os NPCs que representam funcionários dentro da empresa. Essa diversidade de personagens enriquece a experiência de aprendizado.

### 3.2.1. Controláveis

&emsp; O jogador assume o papel de um analista recém-contratado no Banco BTG, que precisa investigar e eliminar espiões infiltrados na empresa. O personagem é controlado em uma perspectiva top-down, podendo se movimentar pelo ambiente utilizando as teclas W, A, S e D ou as setas direcionais do teclado. O analista não possui um nome fixo, permitindo que o jogador personalize sua identidade ao iniciar o jogo. Sua aparência também pode ser ajustada dentro de algumas opções predefinidas, garantindo um nível básico de personalização.

&emsp; Durante a jornada, o personagem interage com NPCs (funcionários, gestores e espiões disfarçados), coletando informações e participando de desafios que testam seus conhecimentos sobre finanças, compliance e estratégias de mercado. Cada desafio bem-sucedido aproxima o jogador da identificação dos espiões, sendo essencial para avançar pelos andares do banco.

&emsp; Além da movimentação, o personagem pode interagir com objetos e NPCs ao pressionar a tecla E, acionando diálogos e mecânicas específicas dos minigames presentes nas salas do jogo. Conforme avança na história, o analista recebe recompensas financeiras simbólicas, representadas por bônus em dinheiro fictício, que servem como indicadores de progresso e aprendizado. O controle do personagem é fluido e responsivo, garantindo que a experiência do jogador seja dinâmica e intuitiva ao longo da investigação.

### 3.2.2. Non-Playable Characters (NPC)

&emsp; Os NPCs desempenham um papel fundamental no jogo, contribuindo para a ambientação e o realismo do cenário corporativo do Banco BTG. Embora não haja interações diretas entre o jogador e esses personagens por meio de diálogos, eles estão presentes de forma passiva, representando funcionários e gestores do banco. Dessa forma, reforçam a atmosfera do ambiente profissional e o contexto narrativo do jogo.

<div align="center">
<sub>Quadro 4 - Requisitos </sub>
</div>

| #  | Nome            | Imagem                 | objetivo              |
|----|-----------------|------------------------|-----------------------|
| 1  | Funcionário     | ![imagem funcionario](/assets/imagens_GDD/funcionario.png) | Este NPC está localizado na sala 2 e está no jogo apenas como cenário, portanto não tem interação com ele|
| 2  | Boss final      | ![imagem boss](/assets/imagens_GDD/boss.png)|Este NPC está localizado na sala 4 e é o Boss do jogo que vai desafiar as habilidades do jogador |

### 3.2.3. Diversidade e Representatividade dos Personagens

&emsp; A sociedade brasileira atual apresenta uma crescente diversidade em diferentes setores, especialmente no mercado profissional. Dados do IBGE mostram que a participação de negros e pardos no mercado formal aumentou de 32,2% para 40,9% entre 2021 e 2024. O número de mulheres em cargos gerenciais e burocráticos também cresceu 5,3%, embora ainda seja inferior à ocupação masculina. Esses avanços refletem uma inclusão gradual que serve como base para a abordagem do jogo.

&emsp; A personagem principal foi criada para representar essa diversidade crescente no Brasil, promovendo identificação com o jogador por meio de elementos familiares ao público-alvo. O jogo incentiva a exploração e a busca por conhecimento, características alinhadas aos valores do BTG Pactual. Além disso, a diversidade da equipe de desenvolvimento foi incorporada nos detalhes do jogo, reforçando sua identidade inclusiva.

&emsp; O público-alvo do jogo é composto por analistas técnicos do BTG Pactual em processo de onboarding. Esse grupo valoriza aprendizado ágil e feedback instantâneo, aspectos que foram integrados à experiência gamificada. A abordagem diversificada busca engajar os jogadores enquanto promove equidade e representatividade.

&emsp; A gamificação é usada como ferramenta para facilitar o onboarding técnico e reforçar uma cultura organizacional mais inclusiva. O jogo reflete iniciativas como o programa #ElaFazTech do BTG Pactual, evidenciando o compromisso com a diversidade no setor de tecnologia. O projeto não apenas cumpre seu papel funcional no onboarding, mas também promove valores de colaboração e inclusão. Alinhado às tendências sociais e corporativas previstas para 2025, o jogo contribui para um ambiente mais equitativo e inovador.

## 3.3. Mundo do jogo (sprints 2 e 3)
&emsp; O mundo do FundInvest é inspirado no ambiente do BTG, com salas que simulam diferentes departamentos. Com cenários projetados detalhadamente, pensando desde a arquitetura da mesa de operações até os escritórios, oferecendo um espaço virtual onde os novos analistas se familiarizem não só com a área de fundos de investimentos e a cultura do banco, mas também com sua estrutura física e organizacional. Nele, cada ambiente serve como palco para desafios específicos relacionados ao processo de onboarding, criando uma curva de aprendizagem que acompanha o desenvolvimento das habilidades do usuário.

### 3.3.1. Locações Principais e/ou Mapas (sprints 2 e 3)

&emsp; O jogo FundInvest se passa dentro do Banco BTG, onde o jogador assume o papel de um analista recém-contratado. O ambiente foi projetado para simular um banco de investimentos de forma realista, sendo dividido em diferentes andares que representam as etapas da investigação sobre espiões infiltrados na empresa.

&emsp; A jornada começa na Tela Inicial, onde o jogador pode ajustar configurações e iniciar sua missão. Ao entrar no jogo, ele é levado ao prédio do banco, marcando o início da experiência. O primeiro local explorável é o corredor principal, que funciona como um hub central de navegação. Nesse espaço interativo, o jogador pode conversar com NPCs que oferecem dicas e instruções sobre os desafios.

&emsp; Cada andar do banco representa um nível e conta com quatro salas temáticas. Nessas salas, ocorrem minigames educativos relacionados ao mercado financeiro e às tarefas diárias de um analista. Os ambientes possuem uma estética corporativa moderna e incluem elementos como mesas, computadores, gráficos e painéis informativos para reforçar a ambientação profissional.

&emsp; Após completar todas as salas de um andar, o jogador recebe uma chave especial que desbloqueia o elevador localizado no corredor principal. Esse elevador é fundamental para avançar no jogo, transportando o jogador ao próximo nível da investigação. À medida que progride pelos andares, os desafios se tornam mais complexos e os espiões mais difíceis de identificar.

&emsp; Os locais explorados incluem áreas como salas de reuniões, escritórios dos diretores, setores de compliance e até mesmo a sala do CEO. O confronto final ocorre neste último ambiente, onde o jogador enfrenta o último espião.

&emsp; Ao concluir a missão, o jogador chega à Cena de Fim, que simboliza sua vitória sobre os infiltrados e sua aceitação definitiva como parte do banco. Por fim, há uma Cena de Créditos, dedicada aos desenvolvedores e às fontes utilizadas no projeto.

&emsp; Todos os ambientes foram cuidadosamente projetados para oferecer uma experiência imersiva. As transições entre as áreas são suaves, enquanto as interações intuitivas ajudam a guiar o jogador ao longo da narrativa.

### 3.3.2. Navegação pelo mundo (sprints 2 e 3)

&emsp; A navegação do jogo FundInvest ocorre por meio de um sistema estruturado de salas interligadas, permitindo ao jogador transitar entre diferentes ambientes de forma intuitiva. A movimentação segue o padrão top-down, com o jogador podendo se deslocar utilizando as teclas W, A, S e D ou as setas direcionais do teclado.

&emsp; O jogo começa na Tela de Boas-Vindas, onde o jogador pode escolher entre iniciar uma nova partida ou continuar de onde parou. O menu inicial também oferece opções de configuração e ajustes de volume. Ao clicar no botão "Jogar", o jogador é levado à primeira fase, onde descobre que o banco está sendo infiltrado por espiões disfarçados.

&emsp; Após essa introdução, o jogador é transportado para o corredor principal, que funciona como um hub de conexão entre as salas do andar atual. Nesse corredor, ele pode interagir com NPCs que fornecem informações sobre a mecânica do jogo e os desafios que enfrentará.

&emsp; Cada andar representa um novo nível de investigação. O jogador deve resolver desafios deter os espiões infiltrados. As salas contêm minigames educativos que precisam ser concluídos antes que o jogador possa avançar. O acesso às salas é feito ao interagir com as portas e pressionar a tecla E.

&emsp; Ao final de cada andar, o jogador enfrenta um espião disfarçado, boss. Para desmascara-lo, é necessário responder corretamente os desafio proposto. Após derrotar o espião, o jogador recebe uma chave especial, que desbloqueia o elevador e permite a transição para o próximo nível da investigação.

&emsp; Conforme avança pelos andares, os desafios se tornam mais complexos, exigindo maior domínio dos conceitos abordados. Essa progressão continua até que todas as fases sejam concluídas. No final do jogo, o jogador chega à Cena de Fim, onde recebe uma mensagem de parabéns por ter eliminado todos os espiões e garantido a segurança do banco. Nessa etapa, ele pode optar por revisar os conteúdos ou encerrar sua experiência.

&emsp; O sistema de navegação foi projetado para ser fluido e intuitivo. Quando o jogador se aproxima de uma porta ou ponto de transição, um indicador visual aparece para reforçar a interatividade. Além disso, todas as transições entre telas e cenas utilizam efeitos visuais suaves para garantir uma experiência imersiva.

&emsp; O progresso do jogador é salvo automaticamente através de cookies, permitindo que ele continue do ponto onde parou mesmo após fechar e reabrir o jogo.

### 3.3.3. Condições climáticas e temporais 

*Não se aplica*

### 3.3.4. Concept Art 

&emsp; A concept art é uma etapa fundamental no desenvolvimento visual do FundInvest, pois estabelece a identidade estética e traduz, de forma visual, os conceitos centrais do jogo. Por meio de ilustrações representativas das salas e personagens, é possível alinhar a ambientação, os elementos interativos e o tom narrativo com a proposta geral do projeto, além de auxiliar a equipe a entender como colocar em prática aquilo que inicialmente foi idealizado.
A seguir, apresentamos as artes conceituais das salas do primeiro andar, acompanhadas de suas respectivas descrições e funções no gameplay.

<div align="center">
    
*FIGURA 6 – Concept art da Sala 1*

</div>

![imagem concept sala 1](/assets/imagens_GDD/00677010-3b1e-4301-ab19-15a6f824d46f.png)

&emsp; Figura 6: A Sala 1 representa a primeira fase do andar, sendo o primeiro contato do jogador com o jogo em si. O espaço é ambientado em um escritório corporativo, levemente arborizado e minimalista. O elemento interativo principal é uma lousa branca, que apresenta um minigame introdutório simples.

<div align="center">
    
*FIGURA 7 – Concept art da Sala 2*
    
</div>

![imagem concept sala 2](/assets/imagens_GDD/acf4c649-f5d0-4e28-bfbf-b18bbdef32b5.png)

&emsp; Figura 7: A Sala 2 mantém a ambientação da anterior, mas apresenta um desafio mais complexo. O destaque é um cofre interativo que contém um minigame de associação de conceitos. Sua resolução é essencial para que o jogador avance à próxima fase.

<div align="center">
    
*FIGURA 8 – Concept art da Sala 3*

</div>

![imagem concept sala 3](/assets/imagens_GDD/bcc11d34-6677-4a01-a1ac-e0f16d42ad0c.png)

&emsp; Figura 8: A Sala 3 segue a mesma linha estética das anteriores. Nela, o progresso depende da interação com uma máquina de café, que abriga um minigame decisivo para acessar a próxima etapa.

<div align="center">
    
*FIGURA 9 – Concept art da Sala 4*

</div>

![imagem concept sala 4](/assets/imagens_GDD/f781d8ce-9ad9-4144-9363-123aec5be5bc.png)

&emsp; Figura 9: A Sala 4 é o desafio final do andar. O jogador deve confrontar o Big Boss — um espião disfarçado infiltrado na empresa — em uma batalha que representa o clímax da narrativa do level e desbloqueia o acesso ao próximo andar.

&emsp; O estilo visual do FundInvest adota uma abordagem em pixel art, inspirada em jogos clássicos como Celeste e na estética de ambientes corporativos. A proposta é construir um universo visual que remeta a um banco de investimentos, com design limpo e funcional, sem abrir mão da identidade lúdica e interativa que define a experiência do jogo.

 &emsp; Os cenários retratam escritórios modernos, corredores corporativos e salas de reunião, seguindo uma estética minimalista e organizada. Os personagens foram desenhados para representar diferentes perfis do ambiente financeiro — como analistas, gestores e espiões infiltrados —, cada um com um visual único que comunica seu papel na narrativa.

 &emsp; A interface gráfica prioriza a usabilidade e clareza, utilizando ícones padronizados, fontes limpas e elementos de alto contraste. A paleta de cores combina tons neutros para os ambientes e cores vibrantes para personagens e objetos interativos, facilitando a leitura visual durante o gameplay.

 &emsp; Todo o material visual foi desenvolvido internamente, respeitando diretrizes de acessibilidade e coesão estética. Elementos complementares, como os sprites do pacote ModernOffice by Limezu, foram utilizados de forma pontual, com os devidos créditos e licenças reconhecidos.

 &emsp; A avaliação contínua das concept arts durante o desenvolvimento permitiu à equipe alinhar a direção artística com os objetivos narrativos e funcionais do jogo. A análise crítica desses elementos visuais, possibilitou identificar ajustes necessários para manter a consistência estética e fortalecer a imersão do jogador. Esse processo de iteração visual contribuiu diretamente para a construção de uma identidade gráfica coerente, reforçando o papel do visual como ferramenta de narrativa, ambientação e gameplay.


Estilo artístico inspirado em: Celeste

Fontes de imagens externas:  ModernOficce byLimezu

### 3.3.5. Trilha sonora 

<div align="center">
<sub>Quadro 4 - Sons </sub>
</div>

\# | Título | Descrição da ocorrência  | Justificativa | Autoria
--- | --- | --- | --- | --- | 
1 | efeitoSonoroAmbiente.wav | tela inicial do jogo | O som ambiente ajuda a trazer uma atmosfera ao jogo, fazendo com que o jogador se sinta imerso | [bangcorrupt](https://freesound.org/people/bangcorrupt/sounds/552809/)
2 | som de clique | Ao interagir com qualquer botão do jogo o som de clique de mouse é emitido| Emite som de clique de mouse, confirmando a realização da interação com o botão | [Weak_Hero](https://freesound.org/people/Weak_Hero/sounds/790532/)
3 | som de elevador | ao interagir com o elevador no térreo | O som do elevador indica a chegada dentro do banco para o começo da sua jornada de missões e aprendizagem | [Splushionsindasky](https://freesound.org/people/Splushionsindasky/sounds/397339/)
4 | efeitoSonoroPassos.wav | som de passos sempre que o personagem está em movimento | O som do personagem andando ajuda a dinamizar a experiência do jogador, trazendo um ar mais realista ao jogo | [Vrymaa](https://freesound.org/people/Vrymaa/sounds/753292/)
5 | efeitoSonoroCorreto.wav | Ao acertar a resposta correta do minigame este som é emitido | Retorna um feedback informando que a resposta está correta | [JapanYoshiTheGamer](https://freesound.org/people/JapanYoshiTheGamer/sounds/361263/)
6 | efeitoSonoroIncorreto.wav | Ao selecionar a resposta incorreta no minigame este som é emitido | Retorna um feedback informando que a resposta está incorreta | [JapanYoshiTheGamero](https://freesound.org/people/JapanYoshiTheGamer/sounds/361260/)
7 | som de coletar a chave | ao passar de fase ou coletar uma chave | som de recompensa quando o personagem completa um minigame e ganha a chave para ir para o próximo, dando a sensação de conquista | [LittleRobotSoundFactory](https://freesound.org/people/LittleRobotSoundFactory/sounds/274183/)
8 | desbloqueio | ocorre ao desbloqueio das salas | som para sinalizar o desbloqueio da sala | [soundfx6482](https://www.youtube.com/watch?v=oh9aCj3V7cg)
9 | som de virar a página | durante a transição de diálogos, papel ou livro | som para quando o personagem está falando com alguém e passa o diálogo, criar uma imersão maior com o jogo | [florian_reinke](https://freesound.org/people/florian_reinke/sounds/63514/)
10 | tema de tensão | Ao entrar na quarta sala(boss level) a musica é iniciada | Torna a experiência imersiva e eleva o grau de tensão | [awrmacd](https://freesound.org/people/awrmacd/sounds/387222/)

acesse o teste de sons no link abaixo:
https://drive.google.com/file/d/1jIGqagDd6SBmjH_456FfUlw9Ww25dwv4/view?usp=sharing

## 3.4. Inventário e Bestiário 

&emsp; Nesta seção, exploramos dois elementos essenciais para a mecânica do jogo: o Inventário e o Bestiário. Ambos desempenham papéis importantes na organização e no aprofundamento da experiência do jogador, oferecendo recursos para gerenciar itens coletados e informações sobre os desafios encontrados ao longo da jornada.

### 3.4.1. Inventário

&emsp; O sistema de Inventário foi projetado para armazenar e organizar os itens adquiridos pelo jogador durante o progresso no jogo. Ele permite que o jogador acesse, utilize ou gerencie esses recursos de forma prática, contribuindo para a estratégia e a continuidade da narrativa.

## 3.5. Gameflow (Diagrama de cenas) 

&emsp; Nesta seção apresentamos o Gameflow, um diagrama de cena que descreve o fluxo do jogo de forma visual e estruturada. Cada cena representa um momento na jornada do jogador, desde a Tela Inicial até a última parte desenvolvida.

<div align="center">
    
*FIGURA 10 - Gameflow.* 

![imagem gameflow](/assets/imagens_GDD/gameflow2.png)

<sub>Fonte: autoria própria (2025)</sub>
</div>


&emsp; O gameflow do FundInvest segue uma estrutura modular, onde cada cena representa um estado do jogo e funciona como uma classe separada na programação. O jogo começa na Tela Inicial, onde o jogador pode optar por iniciar uma nova partida ou acessar as configurações. Ao selecionar "Jogar", o jogador é transportado para o Corredor Principal, que serve como um hub conectando todas as salas de desafios.

&emsp; No Corredor Principal, o jogador pode se movimentar livremente e interagir com NPCs que fornecem informações e orientações sobre os desafios. Para acessar uma sala, basta se aproximar da porta e pressionar a tecla E, ativando a transição para o ambiente correspondente. Cada sala apresenta um desafio financeiro que deve ser resolvido para que o jogador possa avançar.

&emsp; Após completar uma sala, o jogador retorna ao corredor e pode seguir para a próxima. Quando todas as salas de um andar forem concluídas, o jogador recebe uma chave especial que desbloqueia o elevador. Esse elevador permite a transição para o próximo andar, onde novos desafios mais complexos são apresentados.

&emsp; A progressão do jogo é linear e exige que todas as tarefas de um nível sejam finalizadas antes que o jogador possa avançar. Conforme os andares se sucedem, os desafios aumentam em complexidade, exigindo maior domínio dos conceitos financeiros abordados.

&emsp; No último andar, ocorre o confronto final contra o líder dos espiões, responsável pela ameaça ao banco. Após vencer esse desafio, o jogador é levado à Cena Final, onde recebe uma mensagem de reconhecimento e um resumo de sua jornada. Essa cena marca a conclusão do jogo, oferecendo a opção de revisar os conteúdos ou reiniciar a partida.

&emsp; A navegação entre os ambientes segue uma estrutura fluida e lógica, garantindo que as interações levem o jogador a novos estados dentro do jogo. O sistema modular das salas permite que os desafios sejam organizados de maneira independente, facilitando ajustes e expansões futuras.

## 3.6. Regras do jogo 

&emsp; As regras do jogo são um conjunto de instruções que ajudam os usuários a entenderem como determinado jogo funciona e os auxilia sobre como jogá-lo (KHAN ACADEMY, 2025).

&emsp; Nessa seção, serão abordadas as regras do jogo FundInvest, assim como os objetivos que o usuário deverá alcançar, os desafios que irá enfrentar, as recompensas a receber e a sequência que deverá seguir para passar por cada etapa e completar o jogo.

&emsp; O FundInvest é ambientado inspirado no prédio do BTG e é composto por 1 fase, representada por um andar com 4 salas e 4 minigames distintos em cada uma. A seguir, estão as regras que o usuário deve seguir:

<div align="center">
<sub>Quadro 5 - Regras </sub>
</div>

 
\# | Regras do jogo FundInvest 
--- | ---  
1 | O usuário deve seguir a sequência de salas indicadas pelas HUDs na tela.
2 | Dentro de cada sala, o usuário deve interagir com um NPC ou objeto para iniciar o minigame.
3 | O usuário não pode prosseguir para a sala seguinte caso não atinja a pontuação mínima na sala atual (mais de 50%), ficando preso nela até cumprir o requisito mínimo para avançar.
4 | Ao concluir com êxito o minigame de cada sala, o usuário recebe uma chave, que será usada para desbloquear o cadeado da sala seguinte e liberar sua entrada.
5 | Ao concluir o último minigame (sala 4) o usuário conclui a fase 1.
6 | Minigame 1: conecte conceitos às definições corretas.
7 | Minigame 2: escolha a alternativa correta dentre 4 opções.
8 | Minigame 3: preencha a lacuna da frase arrastando a opção correta.
9 | Minigame 4: preencha as lacunas do texto arrastando as opções corretas.

<div align="center">
<sub>Fonte: autoria própria (2025) </sub>
</div>


## 3.7. Mecânicas do jogo 

# Mecânicas do Jogo

&emsp; As mecânicas do jogo são elementos fundamentais que definem como o jogador interage com o ambiente virtual. No contexto do onboarding do BTG Pactual, essas mecânicas foram projetadas para serem intuitivas, garantindo que o jogador possa se concentrar na experiência de aprendizado enquanto resolve os desafios propostos. (ARRIVABENE, 2020)

## Mecânicas Gerais

&emsp; As mecânicas de um jogo são os sistemas de regras e métodos de interação que compõem a experiência fundamental de um jogo. Elas definem como o jogador interage com o ambiente virtual, quais ações podem ser realizadas e como essas ações afetam o mundo do jogo.

<div align="center">
<sub>Quadro 6 - Mecânicas </sub>
</div>

| # | Mecânica | Funcionamento |
|---|----------|---------------|
| 1 | Clique para transição de ambiente | Quando certos objetos são clicados, o ambiente do jogo se altera |
| 2 | Rolagem de páginas | Dentro do computador, o jogador pode rolar certas páginas web utilizando o scroll do mouse ou arrastando dois dedos no touchpad |
| 3 | Clique para interagir | O jogador utiliza o botão esquerdo do mouse ou toque na tela para interagir com elementos do jogo |

## Mecânicas do Login na Plataforma

</div>
<div align="center">
<sub>Quadro 7 - Mecânicas </sub>
</div>
 
\# | Mecânica | Funcionalidade
--- | --- | --- 
1 | Clique para transição de telas | O usuário deve utilizar o botão esquerdo do mouse ou clicar levemente sobre o touchpad para interagir com botões e transicionar entre telas.
2 | Preenchimento do campo nome | Ao cliclar com o botão esquerdo do mouse ou levemente sobre o touchpad no campo nome pode-se preencher o nome de usuário.
3 | Movimento do personagem | Para mover o player, o usuário deve usar as teclas WASD ou "up", "left", "down" e "right", para mecânicas de andar para cima, esquerda, baixo e direita, respectivamente.
4 | Tecla E | O usuário deve utilizar a tecla E para qualquer tipo de interação com NPCs ou objetos.
5 | Sistema de Caderno | O jogador pode acessar um caderno interativo que contém informações importantes. O caderno possui navegação entre as páginas através dos botões "Anterior" e "Próxima".
6 | Sistema de Desbloqueio de Salas | As salas são desbloqueadas progressivamente conforme o jogador completa os desafios anteriores.
7 | Minigames Interativos | Cada sala possui minigames únicos com mecânicas específicas, como conexão de conceitos, interação com objetos e resolução de puzzles.
8 | Sistema de Diálogo | Interface para exibição de diálogos e mensagens importantes ao jogador.
9 | Sistema de Salvamento | Capacidade de salvar o progresso do jogo.
10 | Setas Indicadoras | Sistema de setas que guiam o jogador para objetivos importantes como minigames e saídas.
11 | Cutscenes | Sistema de cutscenes com diálogos sequenciais para momentos narrativos importantes.
12 | Seleção de Personagem | Sistema de seleção de personagem com a visualização do personagem escolhido.

<div align="center">
<sub>Fonte: autoria própria (2025) </sub>
</div>

## 3.8. Implementação Matemática de Animação/Movimento

### 3.8.1. Contextualização

&emsp; Este projeto implementa um sistema de movimento bidimensional para as notas de dinheiro que flutuam no background das telas de nome e de seleção de personagem. Foi aplicada de forma que:

- Um eixo (horizontal/X) utiliza o Movimento Uniforme (MU) - velocidade constante
- Outro eixo (vertical/Y) utiliza o Movimento Uniformemente Variado (MUV) - com velocidade inicial nula e aceleração constante

&emsp; Esta implementação demonstra a aplicação prática de conceitos de física cinemática adaptados para um ambiente de jogo digital, proporcionando um efeito visual de notas de dinheiro sendo carregadas pelo vento de forma realista.

### 3.8.2. Modelagem Matemática

#### 3.8.2.1. Parâmetros iniciais

&emsp; Para qualquer objeto que siga este tipo de movimento, precisamos definir:

- **Posição inicial**: coordenadas `(xi, yi)` 
- **Posição final**: coordenadas `(xf, yf)`
- **Tempo total**: duração `T` da animação (em segundos)

#### 3.8.2.2. Movimento Uniforme (MU) - Eixo X

&emsp; No movimento uniforme, a velocidade permanece constante durante toda a trajetória. A velocidade é calculada a partir do deslocamento total e do tempo total:

**Velocidade no eixo X (constante):**
```
vx = (xf - xi) / T
```

Onde:
- `vx` é a velocidade no eixo X (em pixels por segundo)
- `xf` é a posição final no eixo X (em pixels)
- `xi` é a posição inicial no eixo X (em pixels)
- `T` é o tempo total da animação (em segundos)

**Posição no eixo X a cada instante:**
```
x(t) = xi + vx * t
```

Onde:
- `x(t)` é a posição no eixo X no instante `t`
- `t` é o tempo decorrido desde o início da animação (em segundos)

#### 3.8.2.3. Movimento Uniformemente Variado (MUV) - Eixo Y

&emsp; No movimento uniformemente variado com velocidade inicial nula, temos uma aceleração constante desde o início. Isso significa que a velocidade aumenta linearmente com o tempo, partindo de zero.

**Aceleração no eixo Y (constante):**

Para calcular a aceleração necessária para que o objeto se desloque de `yi` até `yf` em um tempo `T` (partindo do repouso), usamos a fórmula:

```
ay = 2 * (yf - yi) / T²
```

Esta fórmula é derivada da equação geral do MUV:
```
yf = yi + vi * T + (1/2) * ay * T²
```

Como a velocidade inicial (vi) é zero, temos:
```
yf = yi + (1/2) * ay * T²
```

Isolando `ay`, chegamos a:
```
ay = 2 * (yf - yi) / T²
```

**Velocidade no eixo Y a cada instante:**
```
vy(t) = ay * t
```

Onde:
- `vy(t)` é a velocidade no eixo Y no instante `t`
- `ay` é a aceleração constante no eixo Y (em pixels por segundo ao quadrado)
- `t` é o tempo decorrido desde o início da animação (em segundos)

**Posição no eixo Y a cada instante:**
```
y(t) = yi + (1/2) * ay * t²
```

Onde:
- `y(t)` é a posição no eixo Y no instante `t`
- `yi` é a posição inicial no eixo Y (em pixels)
- `ay` é a aceleração constante (em pixels por segundo ao quadrado)
- `t` é o tempo decorrido desde o início da animação (em segundos)


# <a name="c4"></a>4. Desenvolvimento do Jogo
&emsp; O FundInvest foi desenvolvido seguindo uma metodologia ágil com sprints quinzenais em um período de 10 semanas, permitindo entregas e ajustes baseados em feedback contínuo. Desse modo, foi possível equilibrar entre uma abordagem técnica do conteúdo e interativa para sua aplicação. No geral, o processo de desenvolvimento do jogo incluiu fases de prototipagem, implementação de mecânicas, desenvolvimento de conteúdo educacional e refinamento da experiência final, sempre com foco em um onboarding com integração interativa e eficaz.

## 4.1. Desenvolvimento preliminar do jogo 

&emsp; Na versão preliminar do jogo foram entregues a movimentação do personagem e duas cenas:

&emsp; **Movimentação do Personagem:** Para o movimento do personagem, foram implementadas como padrão as teclas WASD.

&emsp; **Tela inicial:** foram implementados três botões interativos, "Start", que direcionava para a tela inicial, "Continue", permitindo ao jogador retomar o progresso, e a engrenagem para acessar as configurações do jogo.

&emsp; **Tela de identificação:** caixa implementada para registrar o nome do usuário, mas que apesar de operante, não possuía uma indicação intuitiva para a função de digitação. Após a identificação, o usuário clicava no botão "enter" do teclado para avançar para a tela da primeira fase.

## 4.2. Desenvolvimento básico do jogo

&emsp; Durante o desenvolvimento básico do jogo, foram entregues:

&emsp; **Protótipo do Mapa:** Implementado o primeiro protótipo de mapa para a fase 1.

&emsp; **Configurações:** Implementação do controle de volume do som do jogo e instruções sobre o uso das teclas para movimentação do personagem, bem como a opção de voltar ao menu inicial.

&emsp; **Cookies:** Implementação do sistema completo de cookies para salvar:
- Nome do jogador;
- Configurações de volume;
- Mapeamento personalizado de teclas;
- Posição do jogador no cenário;
- Progresso nas fases.

&emsp; Além disso, foi implementada a funcionalidade de exportar o save como arquivo JSON e o sistema de importação de saves, permitindo que o jogador continue seu progresso em outro dispositivo.

&emsp; **Sprite Temporário:** Implementação de sprite temporário para testes de movimentação.

&emsp; **Atualização na Movimentação do Personagem:** Implementada a movimentação do personagem por setas, além da opção de alterar a função das teclas de movimento no menu de configurações.

&emsp; **Atualização na Tela de Identificação:** Implementado indicador de digitação na caixa de identificação do usuário.

## 4.3. Desenvolvimento intermediário do jogo 

&emsp; Na versão intermediária do jogo, foram entregues:

* **Corredor Principal Fase 1:** Implementação do mapa oficial do corredor principal do jogo (recepção).

* **Salas Fase 1:** Implementação das 4 salas que compõem a primeira fase do jogo.

* **Protótipo Cena Elevador:** Implementação da cena teste do elevador que conecta o usuário à cena do corredor principal.

* **Interaçaão para Transição entre Cenas:** Implementados pontos de interação no corredor principal, nos quais, conforme o personagem se aproxima, aparece um indicador visual explicando como interagir para que determinada transição seja feita. Por exemplo, ao pressionar a tecla E próximo a um ponto de transição, é exibido um diálogo de confirmação, que ao ser confirmado, inicia a transição de cena. 

* **Sistema de Colisão:** Implementação de colisões invisíveis para áreas em que o Tiled não foi usado, mas a colisão é necessária.

&emsp; Durante o desenvolvimento intermediário, o foco principal das alterações realizadas foram voltadas ao Level Design, com a reestruturação do corredor principal e o desenvolvimento de todas as 4 salas, visando tornar o jogo mais intuitivo e agradável ao jogador. Ao longo da Sprint 3, foram entregues os designs de todas as fases propostas, incluindo os minigames, apesar de apenas uma fase ter sido finalizada, adição de novas músicas de fundo e indicadores de interatividade para o jogador.

## 4.4. Desenvolvimento final do MVP 

* **Protótipo Seleção de Personagens:** Antes de iniciar o jogo, o jogador é apresentado à variação de personagens, podendo escolher o personagem que o representará durante o jogo. Essa diversidade de personagens contribui para a diversificação e imersão do usuário dentro do jogo.

* **Recepção com interação, enredo e tutorial do jogo:** O jogador inicia sua jornada interagindo com elementos que o introduzem a história e aos desafios do jogo. Além de um breve tutorial, para que o jogador compreenda as principais mecânicas do jogo.

* **Conteúdos para os Minigames:** Antes de cada minigame, o jogador recebe uma introdução com conteúdos essenciais sobre o mercado financeiro, para garantir que o jogador tenha a base necessária para responder corretamente às perguntas e avançar no jogo.

* **Salas 1 e 2:** Nelas ocorre ocorre o contato entre o usuário e os objetos interativos que o leva aos conteúdos das salas e aos minigames.

* **Minigames 1 e 2:** Minigames de conectar conceitos e definnições (sala 1) e de alternativas (sala 2), com nível de dificuldade progressivo para estimular e garantir a curva de aprendizagem.

## 4.5. Revisão do MVP 

&emsp; O MVP inclui as principais mecânicas de progressão, interação e aprendizado, garantindo que o objetivo do jogo (ensinar conceitos financeiros de forma gamificada) seja atingido. Todas as funcionalidades essenciais foram implementadas, permitindo uma experiência fluida do início ao fim da jornada do jogador.

### Tela inicial e logo
&emsp; A tela inicial apresenta um layout intuitivo e convidativo, introduzindo a temática do jogo com elementos visuais alinhados ao ambiente corporativo de um banco. Além disso, botões interativos permitem o acesso às configurações, ao início do jogo e a outras opções, garantindo que o usuário tenha controle antes de começar a experiência.

<div align="center">

*FIGURA 11 - Tela inicial*

![imagem tela inicial](/assets/imagens_GDD/telaInicial.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Tela de configuração

&emsp; O menu de configurações teve um redesign completo, assim como na tela inicial, o idioma foi substituído para o português, o background foi alterado para que se tornasse condizente a ambientação do jogo e a interface dos botões foi alterada.

<div align="center">

*FIGURA 12 - Tela de configuração*

![imagem tela configurações](/assets/imagens_GDD/configuracoes.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Seleção do nome
&emsp; A tela de seleção de nome teve o background alterado, teve a implementação matemática de animação/movimento adicionada(o) por meio da nota de dinheiro no background, o local de inserir o nome e o botão de “confirmar” foram alterados.

<div align="center">

*FIGURA 13 - Tela de Seleção de nome*

![imagem tela de seleção de nome](/assets/imagens_GDD/Tela_nome.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Tela de seleção de personagens
&emsp; A tela de seleção de personagens foi adicionada com 4 opções de personagens para serem utilizados.

<div align="center">

*FIGURA 14 - Tela de seleção de personagem*

![imagem seleção personagem](/assets/imagens_GDD/personagem.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Elevador
&emsp; A cena interativa do elevador foi substituída pela cutscene do elevador abrindo antes do início do jogo. 

<div align="center">

*FIGURA 15 - Tela do elevador*

![imagem tela conteúdo](/assets/imagens_GDD/elevador.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Recepção 
&emsp; Ao iniciar o jogo, ocorre uma interação entre o jogador e o computador da recepção, que explica o contexto em que o jogo se passa e qual objetivo deve ser alcançado, além de fornecer instruções de como se movimentar no jogo. Todas as salas foram separadas em diferentes cenas.

<div align="center">

*FIGURA 16 - Tela de recepção*

![imagem tela recepção](/assets/imagens_GDD/recepcao.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>


### Conteúdos apresentados antes dos minigames

&emsp; Ao entrar nas salas, o jogador tem acesso a conteúdos que irão ser utilizados durante a realização do minigame. Cada sala possui conteúdos exclusivos, visando o aprendizado e entendimento por parte do analista.

<div align="center">

*FIGURA 17 - Tela de conteúdo*

![imagem tela conteúdo](/assets/imagens_GDD/conteudo.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Sala 1
&emsp; Ao entrar na sala 1, o jogador tem acesso ao conteúdo e deve interagir com o minigame, sinalizado por meio do ponto de exclamação vermelho presente na HUD.

<div align="center">

*FIGURA 18 - Tela Sala 1*

![imagem tela sala 1](/assets/imagens_GDD/sala2.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Minigame 1
&emsp; Ao interagir com o ponto de exclamação, o jogador é direcionado ao minigame 1. O objetivo do minigame é conectar as palavras aos seus respectivos significados. Após conectar as caixas de palavras, o jogador deve clicar em “verificar”. Caso tenha acertado, a fase foi concluída, caso contrário, ele deve refazer o minigame.

<div align="center">

*FIGURA 19 - Tela Minigame 1*

![imagem tela minigame 1](/assets/imagens_GDD/minigame1.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Sala 2
&emsp; Ao entrar na sala 2, o jogador tem acesso ao conteúdo e deve interagir com a lousa, sinalizada por meio do ponto de exclamação vermelho presente na HUD.

<div align="center">

*FIGURA 20 - Tela Sala 2*

![imagem tela sala 2](/assets/imagens_GDD/sala1.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Minigame 2
&emsp; O minigame 2 consiste em 3 perguntas de múltipla escolha. Caso o jogador acerte duas questões ou mais, a fase foi concluída, caso contrário, deverá refazer o minigame.

<div align="center">

*FIGURA 21- Tela Minigame 2*

![imagem tela minigame 2](/assets/imagens_GDD/minigame2.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>


### Sala 3
&emsp; Ao entrar na sala 3, o jogador tem acesso ao conteúdo e deve interagir com a máquina de café, sinalizada por meio do ponto de exclamação vermelho presente na HUD.

<div align="center">

*FIGURA 22 - Tela Sala 3*

![imagem tela sala 3](/assets/imagens_GDD/Sala3.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Minigame 3
&emsp; O minigame 3 consiste em completar frases com a palavra correta, baseando-se no contexto da frase. Todas as três questões devem ser respondidas corretamente para que o jogador prossiga.

<div align="center">

*FIGURA 23 - Tela Minigame 3* 

![imagem tela minigame 3](/assets/imagens_GDD/minigame3.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>


### Sala 4
&emsp; A sala 4 apresenta um **boss level**. Esta é a fase final do jogo, o jogador deve interagir com o chefe se aproximando de sua mesa.

<div align="center">

*FIGURA 24 - Tela Sala 4* 

![imagem tela sala 4](/assets/imagens_GDD/sala4.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>

### Minigame 4
&emsp; O minigame 4 é uma fase desafiadora. Todos os conteúdos abordados durante as salas anteriores serão utilizados em uma só pergunta, para garantir que o aprendizado do analista tenha sido eficiente.

<div align="center">

*FIGURA 25 - Tela Minigame 4*

![imagem tela minigame 4](/assets/imagens_GDD/minigame4.png)

<sub>Fonte: autoria própria (2025)</sub>

</div>


# <a name="c5"></a>5. Testes

&emsp; Nesta seção, detalhamos os testes realizados para garantir o funcionamento correto do jogo e a consistência da experiência do usuário. Os casos de teste foram elaborados para cobrir diferentes aspectos do jogo, incluindo menus, transições, controles e elementos interativos, com o objetivo de identificar e corrigir possíveis falhas. 

## 5.1. Casos de Teste 

&emsp; Os casos de teste descritos a seguir abrangem as funcionalidades desenvolvidas durante as sprints 2 a 4. Eles foram organizados por áreas do jogo, como Menu Inicial, Menu de Opções, Menu de Nome de Personagem, Primeira Fase e Corredor Principal. Cada caso apresenta uma pré-condição, a descrição do teste e a pós-condição esperada para validar o comportamento correto do sistema.

### Menu Inicial

<div align="center">
<sub>Quadro 8 - Casos de Teste </sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
1 | Jogo recém-iniciado | Verificar se todos os elementos do menu inicial são carregados corretamente | Background, título e botões "Start" e "Opções(Engrenagem)" são exibidos na tela
2 | No menu inicial | Clicar no botão "Start" | O jogador é levado para a tela de "Nome do Personagem"
3 | No menu inicial | Clicar no botão "Opções" | O jogador é levado para a tela de "Configurações"
4 | Jogo recém-iniciado sem 'save' existente | Verificar a exibição do botão "Continuar" | O botão "Continuar" não aparece no menu
5 | Jogo recém-iniciado com 'save' existente | Verificar a exibição do botão "Continuar" | O botão "Continuar" aparece no menu
6 | No menu inicial com 'save' existente | Clicar no botão "Continuar" | O jogo carrega a fase onde o jogador parou anteriormente
7 | Jogo recém-iniciado | Verificar reprodução da música de fundo | A música do jogo é reproduzida no volume padrão e caso exista um save anterior, a música é reproduzida no volume salvo anteriormente
8 | No menu inicial | Redimensionar a janela do navegador | Os elementos do menu se reposicionam adequadamente
9 | No menu inicial | Passar o mouse sobre os botões | Os botões reagem de forma interativa

### Menu de Opções

<div align="center">
<sub>Quadro 9 - Casos de Teste </sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
10 | No menu inicial | Acessar o menu de opções através do botão "Opções" | O menu deve possuir, o título "CONFIGURAÇÕES", controle de volume e configurações
11 | No menu de opções | Ajustar o controle de volume | O volume da música muda em tempo real conforme a barra deslizante é movida
12 | Volume ajustado no menu de opções | Sair do menu e retornar às opções | O controle de volume mantém a posição definida anteriormente
13 | No menu de opções | Clicar no botão da tecla para cima e pressionar uma nova tecla | A tecla pressionada é configurada e aparece no botão
14 | No menu de opções | Clicar no botão da tecla para baixo e pressionar uma nova tecla | A tecla pressionada é configurada e aparece no botão
15 | No menu de opções | Clicar no botão da tecla para esquerda e pressionar uma nova tecla | A tecla pressionada é configurada e aparece no botão
16 | No menu de opções | Clicar no botão da tecla para direita e pressionar uma nova tecla | A tecla pressionada é configurada e aparece no botão
17 | No menu de opções | Tentar configurar uma tecla já utilizada: 1. Clicar no botão da tecla para cima 2. Pressionar a tecla D (que já está configurada para direita) | O jogo deve mostrar a mensagem de erro "A tecla D já está sendo utilizada!" e manter o botão da tecla selecionado sem alterar sua configuração
18 | Teclas personalizadas configuradas | Sair do menu e retornar às opções | As teclas configuradas permanecem salvas
19 | No menu de opções | Clicar no botão "Exportar Save" | Um arquivo JSON é baixado com os dados do jogo
20 | No menu de opções | Clicar em "Importar Save" e selecionar um arquivo de save válido | Mensagem de sucesso é exibida e configurações são atualizadas
21 | No menu de opções | Clicar em "Importar Save" e selecionar um arquivo inválido | Mensagem de erro é exibida
22 | No menu de opções | Clicar no botão "Voltar ao Menu" | O jogador é levado para o menu principal
23 | No menu de opções | Redimensionar a janela do navegador | Os elementos do menu se reposicionam adequadamente

### Menu de Nome de Personagem

<div align="center">
<sub>Quadro 10 - Casos de Teste </sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
24 | Menu inicial com botão "Start" clicado | Verificar carregamento da tela de nome | O menu deve ter título "DIGITE SEU NOME:" e a caixa de texto deve estar visível
25 | Tela de nome do personagem carregada | Digitar caracteres usando o teclado | Os caracteres digitados aparecem na caixa de texto
26 | Tela de nome do personagem carregada | Observar o cursor na caixa de texto | O cursor pisca com intervalo regular na caixa de texto
27 | Tela de nome com 32 caracteres inseridos | Tentar digitar mais caracteres | O campo só aceita até 32 caracteres
28 | Tela de nome com caracteres inseridos | Pressionar a tecla Backspace | O último caractere é removido da caixa de texto
29 | Tela de nome com nome válido inserido | Pressionar a tecla Enter | O jogo avança para a primeira fase
30 | Tela de nome com campo vazio | Pressionar a tecla Enter | O jogo não avança e permanece na tela de nome
31 | Nome salvo em jogo anterior | Iniciar novo jogo, confirmar nome e voltar ao menu e clicar em "Continuar" | O nome digitado é mantido
32 | Tela de nome do personagem carregada | Redimensionar a janela | Os elementos do menu se reposicionam adequadamente

### Primeira Fase

<div align="center">
<sub>Quadro 11 - Casos de Teste </sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
33 | Nome do personagem definido e confirmado | Iniciar primeira fase do jogo | A primeira fase carrega com o cenário, personagem e elementos de jogo
34 | Personagem na primeira fase | Pressionar tecla configurada para cima | O personagem se move para cima
35 | Personagem na primeira fase | Pressionar tecla configurada para baixo | O personagem se move para baixo
36 | Personagem na primeira fase | Pressionar tecla configurada para esquerda | O personagem se move para a esquerda
37 | Personagem na primeira fase | Pressionar tecla configurada para direita | O personagem se move para a direita
38 | Personagem na primeira fase | Pressionar duas teclas de movimento simultaneamente | O personagem se move na diagonal
39 | Personagem na primeira fase | Usar teclas de seta em vez das configuradas | O personagem se move normalmente respondendo às setas
40 | Personagem em movimento | Soltar a tecla de movimento | O personagem para de se mover
41 | Progresso salvo na primeira fase | Fechar e reabrir o jogo, clicando em "Continuar" | O jogador inicia na mesma posição onde parou anteriormente
42 | Na primeira fase | Redimensionar a janela do navegador | Os elementos do menu se reposicionam adequadamente

### Corredor Principal

<div align="center">
<sub>Quadro 12 - Casos de Teste </sub>
</div>

\# | pré-condição | descrição do teste | pós-condição 
--- | --- | --- | --- 
43 | Personagem no corredor principal | Tentar atravessar uma parede usando a tecla de movimento | O personagem é bloqueado pela colisão e não atravessa a parede
44 | Personagem no corredor principal | Tentar atravessar um objeto (vasos) | O personagem é bloqueado pela colisão e não atravessa o objeto
45 | Personagem no corredor principal | Caminhar na direção do ponto de transição para a Sala 1 | Quando próximo o suficiente, um indicador visual deve aparecer mostrando que é possível interagir
46 | Personagem próximo ao ponto de transição da Sala 1 | Pressionar a tecla E | Um diálogo de confirmação deve aparecer perguntando se deseja entrar na Sala 1
47 | Diálogo de confirmação aberto para Sala 1 | Confirmar a transição | O jogo deve iniciar a transição e carregar a cena da Sala 1
48 | Diálogo de confirmação aberto para Sala 1 | Cancelar a transição | O diálogo fecha e o personagem permanece no corredor
49 | Personagem no corredor principal | Caminhar na direção do ponto de transição para a Sala 2 | Quando próximo o suficiente, um indicador visual deve aparecer mostrando que é possível interagir
50 | Personagem próximo ao ponto de transição da Sala 2 | Pressionar a tecla E | Um diálogo de confirmação deve aparecer perguntando se deseja entrar na Sala 2
51 | Diálogo de confirmação aberto para Sala 2 | Confirmar a transição | O jogo deve iniciar a transição e carregar a cena da Sala 2 
52 | Personagem no corredor principal | Tentar interagir com um ponto de transição estando fora do alcance | Nenhum indicador visual deve aparecer e a tecla E não deve produzir efeito
53 | Personagem no corredor principal | Tentar colidir simultaneamente com duas paredes (ex: em um canto) | O personagem é bloqueado em ambas as direções

&emsp; Os testes complementares avaliaram as interações com NPCs, a pontuação, o salvamento, a acessibilidade e o desempenho do jogo. A funcionalidade dos diálogos foi verificada para garantir que a tecla E inicie corretamente as conversas, permitindo que o texto avance conforme esperado e encerrando automaticamente caso o jogador se afaste antes do término.

&emsp; O sistema de pontuação foi testado para confirmar a atribuição correta de pontos por acertos e a aplicação do bônus para respostas consecutivas. Também foi validado se a progressão ocorre apenas após o jogador atingir a pontuação mínima exigida, garantindo que, em caso de falhas repetidas, a opção de revisão do conteúdo seja oferecida.

&emsp; O salvamento automático foi analisado para assegurar que o progresso seja mantido ao fechar e reabrir o jogo. As funções de importação e exportação de saves foram testadas, garantindo que arquivos válidos sejam carregados corretamente e que arquivos corrompidos sejam bloqueados com uma mensagem de erro.

&emsp; A acessibilidade foi validada para garantir que todas as ações possam ser realizadas apenas pelo teclado. As mudanças na resolução da tela foram testadas para confirmar que os elementos da interface permanecem ajustados e legíveis.

&emsp; O desempenho geral foi analisado para assegurar estabilidade na taxa de quadros por segundo (FPS) e respostas imediatas dos elementos interativos, como botões e NPCs. As transições entre cenas foram testadas para verificar se ocorrem sem atrasos ou travamentos.

## 5.2. Testes de jogabilidade (playtests) 

&emsp; Os testes de jogabilidade realizados durante a Sprint 4 tiveram como objetivo avaliar a experiência dos jogadores com o jogo, identificando pontos positivos, dificuldades encontradas e aspectos a serem aprimorados. Para isso, foram conduzidas sessões de teste com diferentes perfis de jogadores, incluindo tanto jogadores casuais quanto mais experientes. As observações foram registradas para embasar melhorias no design, na mecânica e na acessibilidade do jogo.

### 5.2.1 Registros de testes

&emsp; Nesta seção, são descritas as sessões de teste realizadas com os jogadores, utilizando um template padronizado para registrar as informações relevantes. Os testes foram conduzidos por meio de entrevistas e observação direta, permitindo uma análise detalhada da interação dos jogadores com o jogo.

<div align="center">
<sub>Quadro 13 - Registros de testes </sub>
</div>

Nome | Daniel 
--- | ---
Já possuía experiência prévia com games? | sim, mas não joga com frequência há algum tempo
Conseguiu iniciar o jogo? | sim
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim  
Apresentou dificuldades? | não, mas se confundiu na ordem das salas
Que nota deu ao jogo? | 9.0
O que gostou no jogo? | Gostou da variedade de minigames e da chave após concluir os minigames
O que poderia melhorar no jogo? | A intuitividade, pois falta HUDs indicando para onde ir, e a opção dos minigames 3 e 4 aceitarem respostas erradas

<div align="center">
<sub>Quadro 14 - Registros de testes </sub>
</div>

Nome | Leonardo 
--- | ---
Já possuía experiência prévia com games? | sim, atualmente joga 2x por semana
Conseguiu iniciar o jogo? | sim
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | sim, teve dificuldade em identificar o objeto de interação na sala 3
Que nota deu ao jogo? | 9.0
O que gostou no jogo? | Gostou da variedade de minigames, dos controles e da seleção de personagens
O que poderia melhorar no jogo? | As colisões, estão mais largas que os objetos, o design das HUDs, alguns estão difíceis de visualizar, e o sistema de pontos dos minigames, a contagem não reseta ao sair do minigame

<div align="center">
<sub>Quadro 15 - Registros de testes </sub>
</div>

Nome | Vitória 
--- | ---
Já possuía experiência prévia com games? | sim, jogava diariamanete antes de começar o estágio regular, inclusive já desenvolveu um jogo e trabalhou em uma startup de games
Conseguiu iniciar o jogo? | sim
Entendeu as regras e mecânicas do jogo? | sim, mas teve problemas pois indicava-se o uso das teclas AWSD, porém não funcionavam, devido a escolha de um tester anterior pelo uso das setas para movimentação do personagem
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | sim, teve dificuldade em identificar os objetos de interação
Que nota deu ao jogo? | 9.0
O que gostou no jogo? | Gostou da elaboração dos minigames
O que poderia melhorar no jogo? | A linearidade do jogo, manter as salas 2, 3 e bloqueadas e só permitir acesso a elas após atingir 50%+ de acerto na sala anterior, além da opção de escolher entre masculino e feminino antes de acessar as opções de personagens, e um botão dentro da primeira fase para retornar a tela inicial

<div align="center">
<sub>Quadro 16 - Registros de testes </sub>
</div>

Nome | Joseph
--- | ---
Já possuía experiência prévia com games? | sim, joga duas vezes por semana
Conseguiu iniciar o jogo? | sim
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | sim, teve dificuldade em entender a disposição das salas
Que nota deu ao jogo? | 9.0
O que gostou no jogo? | Variedade de minigames
O que poderia melhorar no jogo? | Sinalização das salas

<div align="center">
<sub>Quadro 17 - Registros de testes </sub>
</div>

Nome | Nicholas
--- | ---
Já possuía experiência prévia com games? | sim, joga todos os dias
Conseguiu iniciar o jogo? | sim
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | sim, teve dificuldades durante a sala 4
Que nota deu ao jogo? | 10
O que gostou no jogo? | Diferentes tipos de minigames
O que poderia melhorar no jogo? | A progressão do jogo poderia ser mais intuitiva

<div align="center">
<sub>Quadro 18 - Registros de testes </sub>
</div>

Nome | Alice
--- | ---
Já possuía experiência prévia com games? | sim, jogava com baixa frequência
Conseguiu iniciar o jogo? | sim 
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | não sabia o que fazer após concluir o minigame 1
Que nota deu ao jogo? | 8
O que gostou no jogo? | Gostou dos minigames
O que poderia melhorar no jogo? | Sinalizar o que deve ser feito após concluir os minigames

<div align="center">
<sub>Quadro 19 - Registros de testes </sub>
</div>

Nome | Davi
--- | ---
Já possuía experiência prévia com games? | sim, joga várias vezes por semana
Conseguiu iniciar o jogo? | sim 
Entendeu as regras e mecânicas do jogo? | sim
Conseguiu progredir no jogo? | sim
Apresentou dificuldades? | não
Que nota deu ao jogo? | 8
O que gostou no jogo? | Gostou do minigame 3
O que poderia melhorar no jogo? | As exclamações poderiam estar em mais evidência e o personagem poderia andar mais rapido

### 5.2.2 Melhorias

&emsp; Após recebermos os feedbacks dos testadores durante o teste de guerrilha, foram identificadas as principais funcionalidades que necessitam de aprimoramento, com o objetivo de minimizar ou sanar as dificuldades apresentadas durante o teste de jogabilidade.

### Melhorias feitas
* Sinalizações para as salas.
* Indicadores de objetos interativos.
* Bloqueio de salas.
* Aprimoramento da interface e jogabilidade do minigame 1.

### Melhorias futuras
* Sistema de progresso.
* Feedbacks após respostas.
* Expansão o conteúdo.

# <a name="c6"></a>6. Conclusões e trabalhos futuros

&emsp;Após a conclusão do FundInvest, é notório que o projeto atingiu seu objetivo central: apresentar uma opção inovadora ao método convencional de integração, combinando conhecimento técnico com a interatividade e o envolvimento proporcionados pela linguagem dos jogos.

&emsp;A solução elaborada atende diretamente à dificuldade identificada pelo parceiro, transformando um processo complexo e pouco interessante em um percurso acessível, gamificado e produtivo. Através de jogos curtos, história envolvente e desafios progressivos, o jogador assimila conteúdos cruciais sobre fundos de investimento enquanto se adapta à cultura do BTG Pactual.

&emsp;O processo de criação também ofereceu aprendizados valiosos para a equipe, tanto no âmbito técnico quanto colaborativo. A união de diversas áreas do saber (programação, design, negócios e educação) foi fundamental para a entrega de um produto funcional, consistente e em sintonia com as expectativas do parceiro.

&emsp;O projeto, embora finalizado em sua etapa de MVP, ainda demonstra diversas oportunidades de aprimoramento. Dentre as ideias para trabalhos futuros, destacam-se a criação de um modo multiplayer, que estimule a cooperação entre novos analistas; o desenvolvimento de um sistema de feedback adaptável, apto a oferecer reforços personalizados com base no desempenho individual de cada jogador; e a ampliação do conteúdo com novos temas e desafios práticos relacionados ao mundo financeiro. Adicionalmente, a criação de uma versão móvel do jogo pode expandir consideravelmente seu alcance e acessibilidade, assim como a futura integração com plataformas internas do BTG possibilitaria um acompanhamento mais abrangente da trajetória de cada usuário.


# <a name="c7"></a>7. Referências

<a name="ref1"></a>[1] MASSARI, Bianca Brandt. Trabalho acadêmico. PUC-Rio, maio 2017. Disponível em: <https://www.econ.puc-rio.br/uploads/adm/trabalhos/files/Bianca_Brandt_Massari.pdf>. Acesso em: 25 fev. 2025.

<a name="ref2"></a>[2] BTG PACTUAL. Setor de atuação. [S.l.: s.n.], [s.d.]. Disponível em: <https://ri.btgpactual.com/sobre-o-banco/setor-de-atuacao/>. Acesso em: 25 fev. 2025.

<a name="ref3"></a>[3] OS MAIORES BANCOS DO BRASIL. Valor Econômico, 8 nov. 2024. Disponível em: <https://valor.globo.com/financas/noticia/2024/11/08/os-maiores-bancos-do-brasil.ghtml>. Acesso em: 25 fev. 2025.

<a name="ref4"></a>[4] BTG PACTUAL. Quem somos. [S.l.: s.n.], [s.d.]. Disponível em: <https://investimentos.btgpactual.com/quem-somos>. Acesso em: 25 fev. 2025.

<a name="ref5"></a>[5] SIQUEIRA, Luan. Desenvolvedor de software: concepção, resolução, problemas. PD Soluções, 30 out. 2023. Disponível em: <https://blog.pdsolucoes.com.br/desenvolvedor-de-software-concepcao-resolucao-problemas/>. Acesso em: 26 fev. 2025.

<a name="ref6"></a>[6] FASTERCAPITAL. Desafios técnicos: como enfrentar e superar desafios técnicos e aprender com seus fracassos e sucessos. Atualizado em: 17 jun. 2024. Disponível em: <https://fastercapital.com/pt/contente/Desafios-tecnicos--como-enfrentar-e-superar-desafios-tecnicos-e-aprender-com-seus-fracassos-e-sucessos.html?>. Acesso em: 26 fev. 2025.

<a name="ref7"></a>[7] SCIELO. Artigo publicado na revista Cadernos EBAPE.BR. Publicação nesta coleção: 18 dez. 2020. Data do fascículo: nov. 2020. Disponível em: <https://www.scielo.br/j/cebape/a/RbdpN7vpVLvbqPLgszzH5Rr/>. Acesso em: 26 fev. 2025.

<a name="ref8"></a>[8] INSTITUTO DI. Estudos de caso: sucesso no engajamento em treinamentos corporativos. Instituto DI, 21 jul. 2024. Disponível em: <https://www.idi.com.br/post/estudos-de-caso-sucesso-no-engajamento-em-treinamentos-corporativos>. Acesso em: 26 fev. 2025.

<a name="ref9"></a>[9] PUC-SP. Artigo publicado na Revista de Carreiras e Pessoas (ReCaPe). Publicado em: 6 maio 2022. Disponível em: <https://revistas.pucsp.br/ReCaPe/article/view/50127>. Acesso em: 26 fev. 2025.

<a name="ref10"></a>[10] EY GLOBAL. How banking on Gen Z talent will make or break the future of banking. Ernst & Young Global Ltd., 10 jul. 2023. Disponível em: <https://www.ey.com/pt_br/insights/banking-capital-markets/how-banking-on-gen-z-talent-will-make-or-break-the-future-of-banking>. Acesso em: 26 fev. 2025.


# <a name="c8"></a>Anexos

**Trello**

&emsp;Utilizamos o Trello para organizar as etapas do trabalho em nosso projeto, aplicando a metodologia Kanban. Essa metodologia busca otimizar processos por meio da visualização do fluxo de tarefas. No Trello, as tarefas foram organizadas em colunas específicas: Backlog, Sprint Backlog, Em desenvolvimento, Aguardando Review, Em review e Concluído. Cada cartão representava uma tarefa e era movido entre as colunas conforme seu progresso.

**Benefícios:** A metodologia Kanban permite identificar pontos de melhoria no processo e aprimorar a produtividade geral do trabalho. O Trello facilitou a implementação dessa abordagem de forma visual e colaborativa, garantindo que todos os membros da equipe estivessem alinhados com o andamento do projeto.

**Aseprite**

&emsp;O Aseprite foi utilizado exclusivamente para a criação das sprite sheets do jogo. Essa ferramenta permitiu o desenvolvimento de imagens pixeladas com precisão.

**Benefícios:** Com o Aseprite, foi possível criar sprites detalhados e organizados, essenciais para a animação e integração dos elementos visuais no jogo.

**Canva**

&emsp;O Canva foi empregado tanto para a criação de logos e designs quanto para a elaboração de tabelas e imagens relacionadas ao projeto. Sua interface intuitiva facilitou o desenvolvimento de materiais variados.

**Benefícios:** A ferramenta ofereceu facilidade para criar representações visuais profissionais e atrativas, otimizando o tempo da equipe e garantindo qualidade nos resultados.

**Tiled**

&emsp;O Tiled foi utilizado para a montagem dos mapas do jogo, integrando elementos como pisos, paredes e objetos decorativos.

**Benefícios:** A flexibilidade do Tiled nos permitiu organizar os níveis de maneira eficiente, facilitando ajustes e testes durante o desenvolvimento.

**Figma**

&emsp;O Figma foi utilizado exclusivamente para criar diagramas de cenas do jogo. Ele permitiu mapear graficamente o fluxo das cenas, ajudando na definição da jogabilidade.

**Benefícios:** A ferramenta possibilitou uma visualização clara e colaborativa das cenas do jogo, garantindo alinhamento entre os membros da equipe durante o processo de design.
