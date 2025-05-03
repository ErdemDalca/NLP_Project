> # GAME DESIGN DOCUMENT
> 
> Creado por: Alba María Álvarez Alonso
>
> Versión del documento: 2.00
>
> ## HISTORIAL DE REVISIONES
>
>
>| Versión      | Fecha        | Comentarios  |
>|--------------|--------------|--------------|
>| 2.0          | 27/11/2024   |  Documento   |
>|              |              |              |
> 
> ## RESUMO
> 
> Nun viaxe audaz máis alá dos confíns coñecidos, unha intrépida astronauta desafía os límites do cosmos, sen percatarse de que o combustible necesario para o seu retorno á Terra, o seu fogar, xa se esgotou. O seu espírito explorador levouna ata os recunchos máis remotos da galaxia, seguindo meticulosos cálculos científicos concibidos durante a era da colonización interestelar.

> A especie humana, no seu afán por expandirse, logrou asentarse en diversos planetas grazas ao auxilio de intelixencias artificiais avanzadas. Non obstante, un acontecemento astrofísico imprevisto devastou as infraestruturas automatizadas, deixando aos colonos á mercede do caos. Os asentamentos dispersos perderon contacto coa civilización central, incapaces de manter o control sobre as máquinas e os territorios conquistados.

> Agora, no medio da vastitude estelar, a astronauta atópase atrapada sen suficiente combustible para regresar. Consciente dos recursos desperdicados nos abandonados enclaves coloniais, comprende que a súa única esperanza reside en atopar unha solución entre os restos da desbandada intergaláctica. Deberá aterrar nestes planetas desolados e buscar o combustible que garanta a súa supervivencia e regreso.

> Non obstante, descoñece que nos planetas nos que necesitará aterrar, robots asasinos acechan sen piedade. A súa misión de "Volta a Casa" vese ameazada por estas máquinas descontroladas, dispostas a impedir o seu regreso con violencia.
> 
> 
> ## Concepto
>
> InterGalax é un xogo de plataformas ambientado no espazo onde o xogador controla a unha astronauta chamada Astro, quen debe chegar ao planeta Terra conseguindo combustible en antigos portos especiais situados en planetas da galaxia. O xogo céntrase na exploración, na recolección de recursos e na superación de obstáculos.
>
> ## Puntos Clave
>
> -**Exploración de planetas únicos e diversos.**
> - **Recolección de combustible para avanzar que se convertira en combustible para a nave espacial.**
> - **Superación de obstáculos e trampas en entornos hostís.**
> - **Sistema de puntuación baseado na recolección de obxectos.**
> - **Enfrentamentos con robots avariados.**
>   
> ## Xénero
>
> * Plataformas de acción e aventura.
>
> ## Público Obxectivo
>
> InterGalax está dirixido a xogadores de tódalas idades que disfruten de xogos de plataformas desafiantes cunha temática espacial. Tamén pode atraer a afeccionados á ciencia ficción e aos xogos de exploración.
>
> ## Experiencia de Xogo
>
> Os xogadores experimentarán unha emocionante aventura espacial mentres controlan a Astro, exploran planetas alieníxenas, recolectan recursos, evitan trampas e enfréntanse a desafíos en cada nivel. A atmósfera do xogo estará inmersa nunha banda sonora cautivadora e efectos de son que realzan a experiencia de xogo.
>
> ## DESEÑO
>
> ### Metas de Deseño
>
> * Crear unha experiencia de xogo que transporte ao xogador a un universo alieníxena.
> * Deseñar niveis desafiantes cunha progresión de dificultade en canto ao acceso aos recursos.
> * Ofrecer mecánicas de xogo intuitivas que manteñan o interese do xogador.
> * Impulsar a exploración e o descubremento con planetas únicos e detallados.
> * Integrar elementos de risco e recompensa para fomentar a estratexia e a toma de decisións do xogador.
>   
> ## MECÁNICAS DE XOGO
>
> ### Núcleo do xogo
>
> **InterGalax** baséase en mecánicas de plataformas clásicas con elementos de exploración e recolección. O xogador controla a **Astro**, quen pode camiñar e saltar para navegar polos niveis. Debe recolectar combustible mentres evita trampas e inimigos.

>
> ### Fluxo de xogo
>
> O xogo desenvólvese en diferentes niveis, cada un situado nun planeta diferente. O xogador debe explorar o nivel, recolectar recursos e alcanzar a nave espacial, unha vez esté a barra de fuel chea, ao final para avanzar ao seguinte planeta. Se perde tódalas súas vidas, e está nas fases 1, 2 ou 3, a partida reiníciase desde cero e volve á fase 1. Se está na fase 4, tamén se reinicia pero volve á fase 2.

> ### Fin de Xogo
>
> * Derrotas: Perder tódalas vidas.
> * Victoria: Alcanzar a nave espacial con suficiente combustible para que poida despegar.
>
> ### Física de Xogo
>
> A física do xogo aplícase aos movementos de Astro, a gravidade nos planetas, plataformas, nave espacial e as interaccións con obxectos e con os raios dos inimigos.
> 
> ### Controis
> 
> * Movemento: Flechas direccionais ou teclas WASD.
> * Barra espaciadora: Saltar.
> * Combinando barra espaciador e teclas WASD (izq y der) o salto é más alto.Sérvese dos "colliders" das plataformas para propulsarse más alto.
> * Tecla "P": Pausar xogo.
> * Tecla "ESC": Sair xogo.
> * Tecla "RET": Reinicia o xogo desde cero.
>
> ## MUNDO DO XOGO
>
> ### Descripción do xogo
>
> O xogo desenvólvese nun universo espacial cheo de planetas alieníxenas, cada un co seu propio estilo e desafíos. Os niveis están deseñados cunha combinación de ambientes naturais e estruturas artificiais.

>
> ### Personaxes
>
> * Xogables: Astro, unha astronauta vestida con un traxe naranxa.
>   
>  <img src="img/Astro.png"/>
>
> 
> * Inimigos: Robots hostís. Se Astro interactúa cos robots ( choque, tocar)  perdería 1 vida, e colisiona tamén cos seus raios láser:
>   
> - Os robots do planeta árido:
>
>
>  <img src="img/Robot8.png"/>
>  <img src="img/Robot12.png"/>
>  <img src="img/Robot7.png"/>
>  <img src="img/Robot9.png"/>
>  <img src="img/Robot10.png"/>
>
>
>
> - Os robots do planeta verde:
>
> 
>  <img src="img/Robot10.png"/>
>  <img src="img/Robot5.png"/>
>  <img src="img/Robot13.png"/>
>  <img src="img/Robot14.png"/>
>  <img src="img/Robot16.png"/>
>  <img src="img/Robot15.png"/>
> 
>
>
> - Os robots do planeta xeado : 
>
>
>  <img src="img/robot1.png"/>
>  <img src="img/Robot2.png"/>
>  <img src="img/Robot4.png"/>
>  <img src="img/Robot6.png"/>
>  
>
>
> - Os robots do planeta desértico : 
> 
>
>  <img src="img/Robot11.png"/>
>  <img src="img/Robot3.png"/>
>  <img src="img/Robot22.png"/>
>  
>
>
> ### Obxectos
>
> * Caixas: Conteñen 70 puntos que son combustible para a nave. Producen un son cando o xogador as recolle
>
> - Caixa con combustible para a escea 1 e 3. : 
>
>  <img src="img/Box_01.png"/>
> 
>
> - Caixa para a escea 2: 
>
>  <img src="img/Box_02.png"/>
>
>
> - Caixa para a escea 4: 
>
>  <img src="img/Box_05.png"/>
>
>
>
> * Diamantes: Conteñen 30 puntos que son combustible para a nave.Producen un son cando o xogador as recolle
> 
>  <img src="img/Crystal_03.png"/>
> 
>
> * Nave: Despegará sempre que Astro acceda a ela coa barra de combustible chea.
>
> <img src="img/SpaceShip.png"/>
>
>
> Situada na parte dereita do terreno de xogo:
>
> <img src="img/Fase1.png"/>
>
> <img src="img/Fase2.png"/>
>
> <img src="img/Fase3.png"/>
>
> <img src="img/Fase4.png"/>
>
>
> * Trampas : Restan puntos se Astro as toca ( 50 puntos). A pérdida de puntos produce un son.

>   - No planeta árido son picas situadas en puntos estratéxicos de paso ou debaixo de plataformas e consumen enerxía ao tocalas 
>
> <img src="img/Spike_01.png"/>
>
>  - No planeta frondoso as trampas son a propia vexetación, que debido á radiación consumen enerxía: 
>
> <img src="img/flores.png"/>
>
> <img src="img/grass.png"/>
>
>  - No planeta xeado as trampas son uns lásers situados en zonas de paso ou debaixo de platadormas.
>
> <img src="img/trapsLaser.png"/>
> 
>  - No planeta desértico mineiro, as trampas son os cristáis que están en forma de estalactitas e estalacmitas, ademáis dos cogumelos azuis.
>
>  <img src="img/traps4.png"/>
>  <img src="img/trapsEstalacM.png"/>
>  
>
>
> ## INTERFACE
>
> ### Fluxo de Pantallas
>
> O xogo conta con 2 pantallas de inicio , 4 pantallas que corresponden con cada fase e 1 pantalla final.
> 
> 0. ### Pantalla inicio:
>
> Pantalla inicial selección idioma :
> 
>   <img src="img/pantallaIdiomas.png"/>
>   
>
> * Fondo: Unha pantalla apaisada cun fondo estelar en movemento descendente, creando a sensación de desprazamento. Cinco planetas destacan sobre este fondo: o máis cercano é un planeta árido, seguido por un frondoso,o xeado, o desértico e na distancia, a Terra.
>
> * Nave: Unha nave xurde desde a parte inferior da pantalla, desprazándose cara o norte e desaparecendo pola parte superior da pantalla.
> 
> * Efecto sonoro : A música de fondo, reminiscente de máquinas avariadas.
>
> * Mensaxe na pantalla: Mesaxe estática que indica a selección dunha botón bandeira para seleccionar o idioma elexido: "SELECT".
>
> * Obxectos : 2 bandeiras a cada lado da mensaxe indican que se deben seleccionar para continuar o xogo.
>
> * Transición : sexa a selección que sexa, as bandeiras desaparecen, a mensaxe "SELECT" desaparece e comeza a escribirse a mensaxe no idioma seleccionado.
> 
> Pantalla inicio en inglés : 
> 
>  <img src="img/pantalla0.png"/>
>
> Pantalla inicio en galego : 
>
>   <img src="img/IntroGalego.png"/>
>   <img src="img/Intro2Galego.png"/>
> 
> 
> * Fondo: Unha pantalla apaisada cun fondo estelar en movemento descendente, creando a sensación de desprazamento. Cinco planetas destacan sobre este fondo: o máis cercano é un planeta árido, seguido por un frondoso,o xeado, o desértico e na distancia, a Terra.
>
> * Nave: Unha nave xurde desde a parte inferior da pantalla, desprazándose cara o norte e desaparecendo pola parte superior da pantalla. Aparece a mesma nave saindo da parte superior dereita desprazándose en línea recta ata a parte inferior esquerda. Por último reaparece a nave saindo dende a parte central esquerda e desprazándose en línea recta ata a parte centar dereita.
> A música de fondo, reminiscente de máquinas avariadas, acompaña o movemento, mentres un son de "typing" resoa xunto coa aparición de caracteres na pantalla que narran a mensaxe: "Astro necesita volver á casa, pero antes debe obter combustible para a súa nave. Para iso, terá que deterse en 4 planetas estraños, antigos portos espaciais dos humanos".
>
> * Mensaxe na pantalla: Despois de 1.5 segundos, a mensaxe desaparece e en letras grandes aparece: "PREME UNA TECLA PARA COMEZAR" e máis pequeno "PREME ESPAZO PARA VER 'COMO XOGAR'" e "PREME ESC PARA SAÍR".
>
> * Transición: Ao premer calquera tecla (excepto "esc" ou "espazo"), as mensaxes desaparecen e, despois de 2 segundos, a escena avanza á seguinte pantalla onde comeza o xogo.
>
>
> 1. ### Pantalla 1 - "How to play"
>
>  Pantalla en inglés : 
> 
>    
>    <img src="img/pantalla1.png"/>
>
>  Pantalla en galego : 
>
>   <img src="img/hpGalego.png"/>
> 
>
> * Fondo: Unha pantalla apaisada cun fondo estelar en movemento descendente, creando a sensación de desprazamento. Cinco planetas destacan sobre este fondo: o máis cercano é un planeta árido, seguido por un frondoso,o xeado, o desértico e na distancia, a Terra.
>
>
> * PLAYER: Icono de Astro onde se especifica que fai e que debe facer no xogo: 
>   "Ela camiña e salta para subir obstáculos e utiliza os 'colliders' das plataformas para gañar impulso nalgúns dos seus saltos. 
> Debe recoller combustible para poder despegar a nave espacial (os puntos representan combustible). A nave espacial só depegará se a barra de combustible está chea (500 puntos ou máis)."
>
> * FUEL: Icono das caixas contando que conteñen:
>   "As caixas aparecerán na escena, cada unha contén 70 puntos de combustible."
>
>
> * ENEMIES: Icono dos robots ( inimigos) onde se indica tamén que fan e que dano poden causar:
>   "Eles disparan sen parar cando o xogador está preto deles porque están estropeados. Se un dos disparos acerta en Astro, ela perderá unha vida.
> Se Astro toca a un robot, perderá 1 vida. Se Astro perde tres vidas, é 'game over'."
>
>
> * TRAPS : Icono das trampas, indicando que dano farán:
>   "Se Astro toca calquera destas trampas, perderá unha certa cantidade de combustible (50 puntos), sempre que teña acumulados 50 puntos ou máis. Se ten menos, non perderá ningún combustible."
>
>
> * GAME OVER : Icono dunha serras indicando "Game Over": 
>   "Se Astro as toca, acabaríase o xogo".
>    
>  
> * No medio da pantalla sairá un mensaxe que di que se pulsas calquera tecla comezas a xogar, e ao fondo da pantalla o mensaxe para saír do xogo coa tecla 'esc'.
> 
>
>
>  2. ### Pantalla 2 - Planeta árido/vermello ( FASE 1):
>      
>      <img src="img/pantalla2.png"/>
>
> * Ambiente: Unha paisaxe desértica con montañas puntiagudas de area no fondo. Inspirado no planeta dos Insectívoros (película "El juego de Ender").
>
> * Porto Espacial: O porto conta cun almacén subterráneo metálico. Astro debe descender varios niveis a través de plataformas fixas e en canto teña a barra de combustible chea acceder á nave a través das plataformas flotantes.
> * As plataformas flotantes non se atravesan de abaixo cara arriba, xa que éstas utilízanse para situar as trampas xusto debaixo, por se non se calcula ben o salto ou se cae das plataformas, e así favorecer a perda de puntuación.
>
> * Obxectivo: Astro debe acumular combustible atopando caixas metalizadas e diamantes dispersos polo almacén.
>
> * Caixas e Diamantes: As caixas simulan unha explosión de po ao ser tocadas por Astro, outorgando 70 puntos en combustible, mentres que os diamantes outorgan 30 puntos de combustible sen explosión.
>
> * Trampas: Picas no chan e no teito causan a perda de combustible se Astro as activa. A perda de de combustible produce un son.
>
> * Robots Averiados: Seis robots defectuosos móvense de maneira errática dun lado ao outro do almacén, cambiando de dirección cada vez que chocan cunha parede, e disparando raios de plasma segundio a dirección hacia donde se dirixa. Ser alcanzado por 1 raio custa unha vida.
>
> * Vidas: Representadas por tres figuras de Astro na parte superior esquerda. A perda de vida xera un son, aparece a mensaxe de GameOver , Astro desaparece da escea e a partida reiniciaríase na mesma fase se o xogador pulsa a tecla "RET".
>
> * Barra de fuel: barra horizontal que aparece valeira e a medida que Astro vai conseguindo combustible coas caixas e cristáis, ésta baise enchendo. Así que teña o suficiente combustible para despegar produciráse un son de aviso. Se pola contra, baixa de ese límite, producirase outro son de aviso.
>
> * Despegue: Astro debe conseguir encher totalmente a barra de fuel para activar o despegue da nave. Ao tocar a nave, ésta despega activándose o son de propulsión e o rastro do lume das tobeiras de propulsión do cohete. Astro desaparece (como se entrase na nave) e nave sae verticalmente da escea.
>
> * Transición: A nave despega e desaparece da escena, pasando á fase 2 dous segundos despois.
>
> * Dificultade de nivel : Dificultade moderada xa que aparecen bastantes localizacións con caixas con combustible ( 16 localizacións) e cristáis con puntos extra ( 20 localizacións), aportando 120 puntos nas plataformas flotantes exteriores.. Non hai demasiadas trampas, acesos fáciles e plataformas flotantes de escape dos raios os robots dentro do almacén.
>
>
> 3. ### Pantalla 3 - Planeta frondoso/verde ( FASE 2):
>       
>       <img src="img/pantalla3.png"/>
>
> * Ambiente: Un entorno selvático con unha vexetación única que se alimenta de enerxía, distinta á da Terra. Astro atópase na parte superior do terreo, con árbores de troncos visibles no fondo. Inspirado na lúa de Endor, "planeta" onde viven os Ewoks.
>
> * Porto Espacial: A nave está situada na parte dereita do mapa, accesible desde plataformas flotantes. As plataformas non se atravesan de abaixo cara arriba, xa que estas utilízanse para situar as trampas xusto debaixo, por se non se calcula ben o salto ou se cae das plataformas, e así favorecer a perda de puntuación.
>
> * Sistema de Covas: Na parte inferior da pantalla, hai un complexo sistema de covas. Astro debe descender por pozos estreitos con plataformas escalonadas. A vexetación dentro das covas é perigosa: tocala consume combustible.
>
> * Obxectivo: O xogador debe recolectar caixas dispersas en varias localizacións dentro das covas. Cada caixa outorga 70 puntos. Tamén diamantes dentro e fóra das covas que aportan 30 puntos.
>
> * Trampas: A vexetación perigosa restan combustible acumulado ao xogador se son activados.
>
> * Robots Averiados: Seis robots defectuosos disparan raios láser continuamente, movéndose de maneira errática. Ser alcanzado por 1 raio resta unha vida.
>
> * Pérdida de Puntos e Vidas: Xéranse sons específicos para indicar a perda de puntos ou vidas. Se o xogador perde tódalas vidas, sae na pantalla o mensaxe de "Game Over", Astro desaparece e a partida reiniciaríase na fase 1 se o xogador pulsa a tecla "RET".
>
> * Despegue da Nave: A nave despega con son de explosión e lume nas tobeiras de propulsión cando a barra de vida está totalmente chea e Astro toca a nave.
>
> * Transición: Se a nave despega, despois de 2 segundos cárgase a fase 3.
>
> * Dificultade de nivel : Dificultade moderada-media xa que aparecen bastantes puntos con caixas con combustible (14 localizacións )e cristáis con puntos extra ( 20 localizacións ), pero nesta fase so se conseguirían 30 puntos nas plataformas flotantes exteriores.. Non hai demasiadas trampas e os accesos ós pasadizos entre cova e cova son sinxelos de sortear con saltos. Línea íntegra con robots no fondo da cova donde se encontran moitas das caixas e cristais necesarios para recolectar combustible.
>
>
>
> 4. ### Pantalla 4 - Planeta xeado/branco ( FASE 3):
>       
>       <img src="img/pantalla4.png"/>
>
> * Ambiente: Un entorno nevado con unhas montañas xeadas. Astro atópase na parte superior do terreo. Inspirado no planeta Mann, da película Interestelar.
>
> * Porto Espacial: A nave está situada na parte dereita do mapa, accesible desde plataformas flotantes. As plataformas non se atravesan de abaixo cara arriba, xa que estas utilízanse para situar as trampas xusto debaixo, por se non se calcula ben o salto ou se cae das plataformas, e así favorecer a perda de puntuación.
>
> * Laboratorio: Na parte inferior da pantalla, hai un complexo e perigoso laboratorio. Astro debe descender polos corredores do mesmo , intentando evitar os láseres ubicados tanto no teito como no solo do laboratorio,os bidóns radiactivos, así como non caer nos pozos coas serras, xa que remataría o xogo.
>
> * Obxectivo: O xogador debe recolectar caixas dispersas en varias localizacións dentro do laboratorio. Cada caixa outorga 70 puntos de combustible. Tamén diamantes dentro e fóra do laboratorio que aportan 30 puntos de combustible.
>
> * Trampas: Os lasers en forma de picas e os bidóns radiactivos restan combustible acumulado ao xogador se son activados.
>
> * Robots Averiados: Catro robots defectuosos disparan raios láser continuamente, movéndose de maneira errática. Ser alcanzado por 1 raio resta unha vida.
>
> * Pérdida de Puntos e Vidas: Xéranse sons específicos para indicar a perda de puntos ou vidas. Se o xogador perde tódalas vidas,ou cae nas serras, sae na pantalla a mensaxe de "Game Over", Astro desaparece e a partida reiniciaríase na fase 1 se o xogador pulsa a tecla "RET". Perderanse tódalas vidas se a personaxe toca algunhas das serras.
>
> * Despegue da Nave: A nave despega con son de explosión e lume nas tobeiras de propulsión cando a barra de vida está totalmente chea e Astro toca a nave.
>
> * Transición: Se a nave despega, despois de 2 segundos cárgase a fase 4.
>
> * Dificultade de nivel : Dificultade medio_alta. Moitas trampas situadas ao largo e fondo do laboratorio, así como serras situadas en zonas de salto donde é moi doado caer, finalizando instantáneamente o xogo. Contén 20 localizacións de cristais, donde se poderán conseguir 60 puntos nas plataformas flotantes exteriores, e 16 localizacións de caixas de combustible dentro do laboratorio.
>
> 5. ### Pantalla 5 - Planeta mineiro/amarelo ( FASE 4): 
>       
>       <img src="img/pantalla5.png"/>
>
> * Ambiente: Un entorno polvorento e totalmente desértico. Astro atópase na parte superior do terreo xusto detrás dunhas formacións rocosas. Inspirado no planeta Tatooine, Star Wars.
>
> * Porto Espacial: A nave está situada na parte dereita do mapa, accesible desde plataformas flotantes. As plataformas non se atravesan de abaixo cara arriba, xa que estas utilízanse para situar as trampas xusto debaixo, por se non se calcula ben o salto ou se cae das plataformas, e así favorecer a perda de puntuación.
>
> * Mina: Na parte inferior da pantalla, hai un sistema de grutas, antigo xacemento mineiro. Astro debe descender polas grutas do mesmo, intentando evitar as estalactitas ubicadas no teito como as estalacmitas ubicadas sobre o terreo, así como os cogumelos azúis no solo da cova.
>
> * Obxectivo: O xogador debe recolectar caixas dispersas en varias localizacións dentro da mina. Cada caixa outorga 70 puntos de combustible. Tamén diamantes dentro e fóra das covas que aportan 30 puntos de combustible.
>
> * Trampas: Os cogumelos azuis e as estalacmitas e estalactitas restan combustible acumulado ao xogador se son tocados.
>
> * Robots Averiados: Tres robots defectuosos disparan raios láser continuamente, movéndose de maneira errática. Ser alcanzado por 1 raio resta unha vida.
>
> * Pérdida de Puntos e Vidas: Xéranse sons específicos para indicar a perda de puntos ou vidas. Se o xogador perde tódalas vidas, sae na pantalla a mensaxe de "Game Over", Astro desaparece e a partida reiniciaríase na fase 2 se o xogador pulsa a tecla "RET".
>
> * Despegue da Nave: A nave despega con son de explosión e lume nas tobeiras de propulsión cando a barra de vida está totalmente chea e Astro toca a nave.
>
> * Transición: Se a nave despega, despois de 2 segundos cárgase a escea final.
>
>
> * Dificultade de nivel : Dificultade medio_alta. Moitas trampas situadas ao largo e fondo da mina. Accesos difíciles onde algúns supoñen a pérda de combustible. Outros accesos son insalvables se non usas os colliders coa combinación de teclas WASD para poder acceder. Contén 20 localizacións de cristais , onde nas plataformas exteriores so se conseguirían 30 puntos, e 16 localizacións de caixas de combustible dentro da mina.
>
>
> 6. ### Pantalla 6 - Escea final
>
> Pantalla final en inglés : 
> 
> <img src="img/pantalla6.png"/>
>
> Pantalla final en galego : 
>
> <img src="img/finGalego.png"/>
>
>
> * Fondo: Unha pantalla apaisada cun fondo estelar en movemento descendente, creando a sensación de desprazamento. Un planeta destaca sobre este fondo: a Terra.
>
> * A música de fondo, reminiscente de máquinas avariadas, acompaña o movemento, mentres parpadea no centro da pantalla a mensaxe: "Astro voltou á casa!! Gustaríalle volver a repetir a misión ?"
>
> * Nave: Unha nave xurde desde a parte inferior da pantalla, desprazándose cara o norte e desaparecendo pola parte superior da pantalla. Aparece a mesma nave saindo da parte superior dereita desprazándose en línea recta ata a parte inferior esquerda. Por último reaparece a nave saindo dende a parte central esquerda e desprazándose en línea recta ata a parte centar dereita.
>
> * Mensaxe na pantalla:"PREMA CALQUER TECLA PARA COMEZAR" e máis pequeno "PREME ESC PARA SAÍR".
>
> * Transición: Ao premer calquera tecla (excepto "esc"), a escena avanza á pantalla de inicio.
>
>
>  ### HUD
>
> O HUD mostra unha barra de combustible na esquina superior dereita e as vidas restantes na esquina superior esquerda.
> 
>
>   <img src="img/hud.png"/> 
>
> Se se preme a tecla P, pausase o xogo. 
> 
>  <img src="img/pauseIngles.png"/>
>
>  <img src="img/pausaGalego.png"/>
> 
>
>  Se o xogo termina, sae unha mensaxe indicando Game Over :  
>
>  <img src="img/goGalego.png"/>
> 
>  <img src="img/goIngles.png"/>
> 
> ### ARTE
>
> ### Metas de Arte
>
> Crear un estilo visual único que combine elementos espaciais cun deseño retro de píxeles. O arte debe transmitir a atmósfera do xogo e a diversidade dos planetas.
> 
> ### Assets de Arte
> 
> * Imaxes: Sprites de personaxes (astronauta e robots), fondos de niveis, sprites de caixas, nave espacial, planetas, 4 tileMaps para crear as escenas xogables.
>
> * Animacións: Movementos de personaxes, despegue de nave, lume de propulsión da nave, movemento dos robots, disparos dos robots, explosións das caixas, movemento flotante dos diamantes, movemento flotante dos planetas na escena inicial,movemento das serras e trampas de láser na fase 3, parallax nas pantallas 2,3,4 e 5, efecto movemento do fondo estrellado na pantalla 0,1 e 6.

> ## AUDIO
>
> ### Metas de Audio
>
> Proporcionar unha experiencia auditiva envolvente que complemente a acción do xogo e mellore a inmersión do xogador no universo espacial.
>
> ### Assets de Audio
>
> * Música: Banda sonora atmosférica para as fases 1,2,3,4 e 5, son estridente de máquina avariada na pantalla inicial, con son de teclado ao escribirse na pantalla a misión de Astro. Mesmo son estridente de máquina estropeada para a pantalla de "Como xogar" e na pantalla final.
>
> * Sons: Recolección de obxectos, explosións e disparos. Son para a perda de puntos (caída nas trampas), recollida de puntos, perda de vidas,superación do límite mínimo de combustible na barra de fuel, baixar por debaixo do umbral mínimo de combustible necesario para o despegue e despegue da nave, cambio da pantalla de inicio á escena 1 ao presionar calquera tecla excepto "esc".cambio entre pantalla "how to play" e fase 1, cambio de pantalla final á pantalla de inicio e son específico para Game Over.
>   
> ## DETALLES TÉCNICOS
>
> ### Plataformas Obxectivo
>
> O xogo desenvolverase inicialmente para PC e adaptarase a outras plataformas segundo sexa necesario.
> 
> ### Ferramentas de Desenvolvemento
>
> * Motor do xogo: Unity.
> * Arte: Asset Store, imaxes en internet, itch.io.
> * Música e son: Asset Store.
> * Código : Visual Studio Code.
>
>   
