> # GAME DESIGN DOCUMENT
> 
> Creado por: Alba María Álvarez Alonso
>
> Versión del documento: 1.00
>
> ## HISTORIAL DE REVISIONES
>
>
>| Versión      | Fecha        | Comentarios  |
>|--------------|--------------|--------------|
>| 1.0          | 23/05/2024   |  Documento   |
>|              |              |              |
> 
> ## RESUMEN
> 
> En un viaje audaz más allá de los confines conocidos, una intrépida astronauta ha desafiado los límites del cosmos, sin percatarse de que el combustible necesario para su retorno a la Tierra, su hogar, se ha agotado. Su espíritu explorador la ha llevado hasta los rincones más remotos de la galaxia, siguiendo meticulosos cálculos científicos concebidos durante la era de la colonización interestelar.
> 
> La especie humana, en su afán por expandirse, logró establecerse en diversos planetas gracias al auxilio de inteligencias artificiales avanzadas. Sin embargo, un acontecimiento astrofísico imprevisto devastó las infraestructuras automatizadas, dejando a los colonos a merced del caos. Los asentamientos dispersos perdieron contacto con la civilización central, incapaces de mantener el control sobre las máquinas y los territorios conquistados.
>
> Ahora, en medio de la vastedad estelar, la astronauta se encuentra atrapada sin suficiente combustible para retornar. Consciente de los recursos desperdiciados en los abandonados enclaves coloniales, comprende que su única esperanza reside en hallar una solución entre los restos de la desbandada intergaláctica. Deberá aterrizar en estos planetas desolados y buscar el combustible que garantice su supervivencia y retorno.
>
> Sin embargo, desconoce que en el planeta árido dos robots averiados, Tars y Case, y en un mundo selvático otros dos, Abbott y Costello, acechan sin piedad. Su misión de "Vuelta a Casa" se ve amenazada por estas máquinas descontroladas, dispuestas a impedir su regreso con violencia.
> 
> ## Concepto
>
> Intergalaxies es un juego de plataformas ambientado en el espacio donde el jugador controla a una astronauta llamada Astro, quien debe llegar al planeta Tierra  consiguiendo combustible en antiguos puertos especiales situados en planetas de la galaxia. El juego se enfoca en la exploración, la recolección de recursos y la superación de obstáculos.
>
> ## Puntos Clave
>
> * Exploración de planetas únicos y diversos.
> * Recolección de combustible para avanzar.
> * Superación de obstáculos y trampas en entornos hostiles.
> * Sistema de puntuación basado en la recolección de objetos.
> * Enfrentamientos con robots averiados.
>   
> ## Género
>
> * Plataformas de acción y aventura.
>
> ## Público Objetivo
>
> Intergalaxies está dirigido a jugadores de todas las edades que disfruten de juegos de plataformas desafiantes con una temática 
> espacial. También puede atraer a aficionados a la ciencia ficción y a los juegos de exploración.
>
> ## Experiencia de Juego
>
> Los jugadores experimentarán una emocionante aventura espacial mientras controlan a Astro, exploran planetas alienígenas, recolectan 
recursos, evitan trampas y enfrentan desafíos en cada nivel. La atmósfera del juego estará inmersa en una banda sonora cautivadora y efectos de sonido que realzan la experiencia de juego.
>
> ## DISEÑO
>
> ### Metas de Diseño
>
> * Crear una experiencia de juego que transporte al jugador a un universo alienígena.
> * Diseñar niveles desafiantes con una progresión de dificultad en cuanto al acceso a los recursos.
> * Ofrecer mecánicas de juego intuitivas que mantengan el interés del jugador.
> * Impulsar la exploración y el descubrimiento con planetas únicos y detallados.
> * Integrar elementos de riesgo y recompensa para fomentar la estrategia y la toma de decisiones del jugador.
>   
> ## MECÁNICAS DE JUEGO
>
> ### Núcleo de Juego
>
>Intergalaxies se basa en mecánicas de plataformas clásicas con elementos de exploración y recolección. El jugador controla a Astro, quien puede caminar y saltar para navegar por los niveles. Debe recolectar combustible mientras evita trampas y enemigos.
>
> ### Flujo de Juego
>
> El juego se desarrolla en niveles lineales, cada uno ubicado en un planeta diferente. El jugador debe explorar el nivel, recolectar recursos y alcanzar la nave espacial al final para avanzar al siguiente planeta. Si pierde todas sus vidas, la partida se reinicia desde cero y vuelve a la escena 2.
>
> ### Fin de Juego
>
> * Derrotas: Perder todas las vidas.
> * Victoria: Alcanzar la nave espacial con suficiente combustible.
>
> ### Física de Juego
>
> La física del juego se aplica a los movimientos de Astro, la gravedad en los planetas, plataformas, nave espacial y las interacciones con objetos y con los rayos de los enemigos.
> 
> ### Controles
> 
> * Movimiento: Flechas direccionales o teclas WASD.
> * Barra espaciadora: Saltar.
> * Combinando barra espaciador y teclas WASD (izq y der) el salto es más alto.Se sirve del collider de las plataformas para propulsarse más alto.
> * Tecla "P": Pausar el juego.
> * Tecla "ESC": Salir del juego.
> * Tecla "RET": Reinicia el juego desde cero en la misma fase.
>
> ## MUNDO DEL JUEGO
>
> ### Descripción General
>
> El juego se desarrolla en un universo espacial lleno de planetas alienígenas, cada uno con su propia estética y desafíos. Los niveles están diseñados con una combinación de entornos naturales y estructuras artificiales.
>
> ### Personajes
>
> * Jugables: Astro, una astronauta vestida con un traje naranja.
>   
>  <img src="Imágenes/Captura de pantalla 2024-04-12 141251.png"/>
>
> 
> * Enemigos: Robots hostiles. Astro no interactúa con los robots ( ambos se traspasan).Solo colisiona con sus rayos láser:
>   
> Los robots del planeta árido fueron bautizados por los colonos como Tars y Case. (Película "Interestelar")
>
>  <img src="Imágenes/Captura de pantalla 2024-04-12 141355.png"/>
>
> 
> Los robots del planeta frondoso como Abbot y Costello (Película "La llegada")
>
>  <img src="Imágenes/Captura de pantalla 2024-04-12 141031.png"/>
>
> 
> ### Objetos
>
> * Cajas: Contienen puntos que son el combustible para la nave.
> * Diamantes: Contienen más puntos que son el conbustible para la nave.
> * Nave: Despegará siempre que Astro acceda a ella con al menos 500 puntos de combustible.
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 141212.png"/>
>
> Situada en la parte derecha del terreno de juego:
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 164202.png"/>
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 140952.png"/>
>
> 
> * Trampas : Restan puntos si Astro las toca.La pérdida de puntos produce un sonido
>   En el planeta árido son picas situadas en puntos estratégicos de paso o debajo de plataformas y consumen energía al tocarlas
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 141329.png"/>
>
>  En el planeta frondoso las trampas son la propia vegetación, que debido a la radiación consumen energía: 
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 141103.png"/>
>
> <img src="Imágenes/Captura de pantalla 2024-04-12 141139.png"/>
>
> 
> ## INTERFAZ
>
> ### Flujo de Pantallas
>
> El juego cuenta con 2 pantallas de inicio y 2 escenas que corresponden con cada fase.
> 
> 0. ### Pantalla inicio:
>   
>  <img src="Imágenes/Captura de pantalla 2024-04-12 140613.png"/>
>
> 
> * Fondo: Una pantalla apaisada con un fondo estelar en movimiento descendente, creando la sensación de desplazamiento. Tres planetas se destacan sobre este fondo: el más cercano es un planeta árido, seguido por uno frondoso, y en la distancia, la Tierra.
>
> * Nave: Una nave emerge desde la parte inferior de la pantalla, moviéndose hacia el centro y deteniéndose. La música de fondo, reminiscente de máquinas averiadas, acompaña el movimiento, mientras un sonido de typing resuena junto con la aparición de caracteres en la pantalla que narran el mensaje: "Astro necesita volver a casa, pero antes debe obtener combustible para su nave. Para ello, tendrá que detenerse en dos planetas extraños, antiguos puertos espaciales de los humanos".
>
> * Mensaje en pantalla: Después de 1.5 segundos, el mensaje desaparece y en letras grandes aparece: "PRESS KEY TO START" y  más pequeño  "PRESS SPACE TO HOW TO PLAY" y "PRESS ESC TO QUIT".
>
> * Transición: Al presionar cualquier tecla ( excepto "esc" o "espace"), los mensajes desaparecen y, después de 2 segundos, la escena avanza a la siguiente pantalla donde se inicia el juego.
>
> 
> 1. ### Escena 1 - How to play
>    
>    <img src="Imágenes/Escena1.png"/>
> 
>
>      * Fondo: Una pantalla apaisada con un fondo estelar en movimiento descendente, creando la sensación de desplazamiento. Tres planetas se destacan sobre este fondo: el más cercano es un planeta árido, seguido por uno frondoso, y en la distancia, la Tierra.
>      * Icono de Astro donde se especifica qué hace y qué debe hacer en el juego :
>      "She walks and jumps to climb platforms and must collect points to launch the spaceship ( where points reoresent fuel).The spaceship will only launch if Astro gathers 500 points or more"
>      * Icono de Tars y Case (representando a todos los robots) donde se indica también qué hacen y que daño pueden causar:
>        "They shoot in the same direction without stopping because they are damaged. If one of the shots hits Astro, she will lose one life. if she loses 3 lives, it´s game over".
>      * Icono de una de las cajas contando qué contienen:
>        "Boxes will randomly appear in the scene, each containing points".
>      * Icono de las trampas, indicando qué daño harán :
>      " If Astro touches traps, she will loose 50 points".
>
>       * En medio de la pantalla saldrá un mensaje que dice que si pulsas cualquier tecla empiezas a jugar, y al fondo de la pantalla el mensaje para salir del juego con la tecla "esc"
>
> 
>  3. ### Escena 2 - Planeta árido:
>      
>      <img src="Imágenes/Captura de pantalla 2024-04-12 140852.png"/>
>
> * Ambiente: Un paisaje desértico con montañas de arena picudas en el fondo.Inspirado en el planeta de los Insectívoros ( Película "El juego de Ender")
>
> * Puerto Espacial: El puerto cuenta con un almacén subterráneo metálico. Astro debe descender varios niveles a través de plataformas flotantes y fijas.
> * Las plataformas no se atraviesan de abajo hacia arriba, ya que éstas se utilizan para situar las trampas justo debajo, por si no se calcula bien el salto o se cae de la plataformas, y así favorecer la pérdida de puntuación.
>
> * Objetivo: Astro debe acumular puntos encontrando cajas metalizadas y diamantes dispersos por el almacén.
>
> * Cajas y Diamantes: Las cajas simulan una explosión de polvo en la escena 1 y una explosión de luz en la escena 2 al ser tocadas por Astro, otorgando 50 puntos, mientras que los diamantes otorgan 60 puntos sin explosión. Ambos aparecen aleatoriamente en localizaciones fijas.
>   
> * Trampas: Picas en el suelo y en el techo causan la pérdida de puntos si Astro las activa. La pérdida de puntos produce un sonido.
>
> * Robots Averiados: Dos robots defectuosos ( Tars y Case) se mueven de manera errática, disparando rayos de plasma con diferentes velocidades y patrones. Ser alcanzado por 1 rayo cuesta una vida.
> 
> * Vidas: Representadas por tres figuras de Astro en la parte superior izquierda. La pérdida de vida genera un sonido, aparece el mensaje de GameOver y Astro desaparece de la escena.
>
> * Despegue: Astro debe acumular al menos 500 puntos para activar el despegue de la nave. Al tocar la nave, ésta despega activándose el sonido propulsión y el rastro del fuego de las toberas de propulsión del cohete. Astro desaparece ( como si entrerar en la nave)
> 
> * Transición: La nave despega y desaparece de la escena, pasando a la escena 2 dos segundos después.
>
>  
> 3. ### Escena 3 - Planeta frondoso:
>       
>      <img src="Imágenes/Captura de pantalla 2024-04-12 140919.png"/>
>
> * Ambiente: Un entorno selvático con una vegetación única que se alimenta de energía, distinta a la de la Tierra. Astro se encuentra en la parte superior del terreno, con árboles de troncos visibles en el fondo. Inspirado en la luna de Endor, "planeta" donde viven los Ewoks
>
> * Puerto Espacial: La nave está ubicada en la parte derecha del mapa, accesible desde plataformas flotantes. Las plataformas no se atraviesan de abajo hacia arriba, ya que éstas se utilizan para situar las trampas justo debajo, por si no se calcula bien el salto o se cae de la plataformas, y así favorecer la pérdida de puntuación.
>
> * Sistema de Cuevas: En la parte inferior de la pantalla, hay un complejo sistema de cuevas. Astro debe descender por pozos estrechso con plataformas escalonadas. La vegetación dentro de las cuevas es peligrosa: tocarla resta puntos del Score.
>
> * Objetivo: El jugador debe recolectar cajas dispersas en tres localizaciones dentro de las cuevas. Cada caja otorga 50 puntos. También diamantes dentro y fuera de las cuevas que aportan 60 puntos.
>
> * Trampas: La vegetación peligrosa y los láseres de los robots pueden restar puntos o vidas al jugador si son activados.
>
> * Robots Averiados: Dos robots defectuosos ( Abbott y Costello ) disparan rayos láser continuamente, moviéndose de manera errática. Ser alcanzado por 1 rayo resta una vida.
>
> * Pérdida de Puntos y Vidas: Se generan sonidos específicos para indicar la pérdida de puntos o vidas. Si el jugador pierde todas las vidas,sale en pantalla el mensaje dde "Game Over", Astro desaparece y la partida se reiniciaría si el jugador pulsa tecla "RET".
>
> * Despegue de la Nave: La nave despega con sonido de explosión y fuego en las toberas de propulsión cuando el Score alcanza los 500 puntos y Astro toca la nave. 
> 
> * Transición: Si la nave despega, después de 2 segundos se carga la pantalla de la escena 0.
>    
>  ### HUD
>
> El HUD muestra el marcador de puntos en la esquina superior derecha y las vidas restantes en la esquina superior izquierda.
>
>  <img src="Imágenes/Captura de pantalla 2024-04-12 140736.png"/> 
> 
> ### ARTE
>
> ### Metas de Arte
>
> Crear un estilo visual único que combine elementos espaciales con un diseño retro de píxeles. El arte debe transmitir la atmósfera del juego y la diversidad de los planetas.
> 
> ### Assets de Arte
> 
> * Imágenes: Sprites de personajes (astronauta y robots), fondos de niveles,sprites de cajas, nave espacial, planetas, 2 tileMaps para crear las cuevas de las escenas jugables
> * Animaciones: Movimientos de personajes, depegue de nave, fuego de propulsión de la nave, movimiento de los robots, disparos de los robots, explosiones de las cajas, movimiento flotante de los diamantes, movimiento flotante de los planetas en la escena inicial, parallax en la escena 1 y 2, efecto movimiento del fondo estrellado en la escena 0.
> ## AUDIO
>
> ### Metas de Audio
>
> Proporcionar una experiencia auditiva envolvente que complemente la acción del juego y mejore la inmersión del jugador en el universo espacial.
>
> ### Assets de Audio
>
> * Música: Banda sonora atmosférica para la escena 1 y 2, sonido istriónico de máquina averiada en la pantalla incial, con sonido de teclado al escribirse en pantalla la misión de Astro
> * Sonidos: Recolección de objetos, explosiones y disparos. Sonido para la pérdida de puntos (caída trampas), recogida de puntos, pérdida de vidas, y despegue de la nave, cambio de la pantalla de inicio a la escena 1 al presionar cualquier tecla excepto "esc" y Game Over
>   
> ## DETALLES TÉCNICOS
>
> ### Plataformas Objetivo
>
> El juego se desarrollará inicialmente para PC y se adaptará a otras plataformas según sea necesario.
> 
> ### Herramientas de Desarrollo
>
> * Motor del juego: Unity.
> * Arte: Asset Store, imágenes en internet
> * Música y sonido: Asset Store.
>
>   
