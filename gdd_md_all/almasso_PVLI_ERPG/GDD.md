
# ÑRPG: GAME DESIGN DOCUMENT

## ÍNDICE

1. [Ficha Técnica](#ficha-técnica)
2. [Descripción](#descripción)
3. [Jugabilidad](#jugabilidad)
    1. [Movimiento](#movimiento)
    2. [Cámara](#cámara)
    3. [Exploración](#exploración)
    4. [Combate](#combate)
        1. [Puntos de vida](#puntos-de-vida)
        2. [Flujo de combate](#flujo-de-combate)
        3. [Ataques](#ataques)
        4. [Aliados](#aliados)
        5. [~~Puntos de experiencia y qué significa subir de nivel~~](#puntos-de-experiencia-y-qué-significa-subir-de-nivel)
4. [Diseño de Nivel](#diseño-de-nivel)
    1. [Tipos de Zonas](#tipos-de-zonas)
        1. [Plaza](#plaza)
        2. [Parque](#parque)
        3. [~~Puerto~~](#puerto)
        4. [~~Catedral~~](#catedral)
        5. [~~Cementerio~~](#cementerio)
        6. [Acantilado](#acantilado)
        7. [Manín Interactive](#manin-interactive)
        8. [~~Catacumbas~~](#catacumbas)
5. [HUD](#hud)
    1. [Exploración](#hud-exploración)
    2. [Combate](#hud-combate)
    3. [Diálogos](#diálogos)
6. [Contenido](#contenido)
    1. [Historia](#historia)
    2. [Objetos](#objetos)
        1. [Consumibles](#consumibles)
7. [Menús y Flujo de Juego](#menús-y-flujo-de-juego)
9. [Referencias](#referencias)


### Ficha Técnica

+ **Título:** España: Rondando por Galicia
+ **Género:** J-RPG
+ **Target:** Adolescente o Joven Adulto con gusto por la estrategia en el combate, pequeños gags y por una historia simple.
+ **Rating:** +16 años
+ **Plataforma:** Web
+ **Modo de Juego:** Un jugador, historia cuasilineal

### Descripción

ÑRPG es un JRPG ubicado en Galicia, donde en una de las grandes plazas de Vigo se encuentra el *Dinoseto* vandalizado, podado y destrozado. Nuestro protagonista, ***Manín***, que es el jardinero encargado del seto, se verá envuelto en una aventura por toda Galicia para recuperar los diferentes trozos del *Dinoseto*. Durante esta aventura atravesará diversas zonas como: _La Plaza, El Cementerio, La Catedral de Santiago, El Parque, El Puerto y Las Catacumbas_, haciendo amigos (icónicos personajes de España) para reclutar en su _Party_, luchando contra diversos enemigos y Jefes.

### Jugabilidad

Conservamos una jugabilidad muy parecido a los clásicos JRPGs (Primeras entregas de Final Fantasy y Dragon Quest), en la que llevamos a un protagonista que se aventurará al mundo tratando de cumplir una misión, generalmente a gran escala, mientras completa otras misiones secundarias. Todo esto lo hace acompañado de una ***Party***: una serie de aliados que el _héroe_ acaba por encontrarse en su camino y decide incorporar a su equipo. Generalmente consigue más aliados de la capacidad de su grupo de combate (4 contando al protagonista) y puede escoger quienes se enfrentan a la batalla junto a él. 

#### Movimiento

A la hora de viajar por el mundo nuestro personaje va a moverse en 4 direcciones (arriba, abajo, izquierda, derecha) y en la combinación de las mismas, permitiendo movimiento diagonal. Cada vez que Manín avance un paso, se moverá 1 casilla en la dirección deseada, pues el _mapa_ por el que controlamos al personaje está dividido en _Tiles_ de 32x16 píxeles. El movimiento se para cuando el juego pase a fase de combate.

#### Cámara

+ **Exploración:** Nos muestra una vista _top-down_ de la escena, con el protagonista en el centro. La cámara estará fijada en él todo el rato.
+ **Combate:** La escena se muestra con una vista horizontal estática de la escena (ver HUD).

#### Exploración

Gran parte de la aventura se basa en la exploración de un entorno. Esta consiste en andar por las diferentes zonas del mapa hablando con NPCs, abastecerse el inventario para próximas batallas en las diferentes tiendas y completar la misión de esa zona concreta. 

En las zonas consideradas "_hostiles_", Manín tendrá posibilidades de empezar un combate junto a sus aliados (si el jugador ha decidido incorporar alguno a su equipo) en el estado en el que estos se encuentren. 

Durante este modo también se podrán usar objetos sobre los aliados, como, por ejemplo, las curaciones o reabastecimientos de maná (NO IMPLEMENTADO -> SE USA EL SERGAS PARA ESTO).

#### Combate

Manín pasará a la fase de combate cuando esté explorando algún suelo hostil (definir cuáles son hostiles y cuáles no) de forma aleatoria. Cada paso que dé en una de estas zonas aumentará la probabilidad de combate hasta que este se produzca.

[Ver HUD de combate](#hud-combate)

##### Puntos de Vida

Son la estadística que mantendrá a un personaje en pie. Cuando este reciba un ataque, perderá X Puntos de Vida(PVs) dependiendo de la fuerza y tipo del ataque. Si un personaje llega a 0 PVs, muere: no podrá ser utilizado de ninguna manera hasta que sea curado de las siguientes formas: en un **SERGAS**, con un objeto que permita a un aliado volver a la vida (NO IMPLEMENTADO) o con algún '_ataque_' aliado que permita revivir a un objetivo (NO IMPLEMENTADO).

En caso de que toda la _party_ muera, se cargará un anterior punto de guardado, manteniendo el estado del inventario y de los aliados iguales a los del momento del guardado.

Al igual que los aliados, los enemigos también '_mueren_', y una vez lo hacen no pueden volver al campo de batalla.

##### Flujo de Combate:

Al empezar un combate se calcula un orden de turnos en función de la velocidad de cada participante. Esto entra en juego una vez se hayan decidido las acciones de los personajes. Todas las acciones de los aliados se definen antes de que estas se empiecen a ejecutar: Primero se muestra el menú de combate de cada personaje y una vez se haya escogido su acción, se hace lo mismo para el siguiente. Cuando todos los personajes tengan una acción asignada, se resuelven siguiendo el orden comentado anteriormente. 

##### Ataques:
1. Tipos de Ataque
2. Daño
3. Estado Alterado (Precisión)
4. Puntos de Maná
5. Objetivo(s)

Los ataques tienen 3 estadísticas. Daño, Efectos de Estado y Puntos de Maná. Los ataques también se diferencian en 3 tipos: Normal, Especial y Ulti (ULTI NO IMPLEMENTADA).

**Tipos de Ataque:** Cada personaje tiene 1 ataque Normal: no gasta Puntos de Maná; 2 Especiales: gastan Puntos de Maná; y 1 Ulti: Tarda X turnos en poder usarse, solo puede usarse una vez y gasta al menos la mitad de los PM de cada personaje. Los del primer tipo son los ataques más débiles, pues no consumen nada al personaje que los usa, los del segundo tipo son más fuertes y pueden tener daño elemental y efectos de estado, mientras que la Ulti es el más fuerte de todos y también puede provocar estados alterados con mayor probabilidad.

**Daño:** El daño es la cantidad de Puntos de Vida que un ataque quitaría a un objetivo si tuviera 0 Resistencia al Tipo de Daño que el ataque haga. Los Tipos de Daño son los siguientes: Meleé, Rango, Fuego, Eléctrico, Tóxico y Apoyo. Los ataques de tipo 'Apoyo' no hacen daño, sino al contrario: pueden curar al objetivo, subir su precisión, ataque, resistencias, etc.

**Estados Alterados:** Son efectos que puede sufrir un personaje de forma pasiva por haber consumido un objeto o haber recibido un ataque. Duran X turnos en función de cada estado. Se conservan entre combates: se mantienen los turnos que se han pasado sufriendo el estado concreto. También se pueden acumular varios estados a la vez. un ataque que pueda causar un Estado Alterado tiene una probabilidad de que este entre en efecto.

Listado:
1. **Borracho:** La precisión del personaje baja y su velocidad de turno es menor (implementación de movimiento de HUD?). (NO IMPLEMENTADO)
2. **Quemado:** Los PVs bajan gradualmente y las resistencias a daño Físico, Rango y a Fuego, siendo esta última la más afectada.
3. **Paralizado:** El personaje pierde su turno mientras esté paralizado. También baja la resistencia a daño Eléctrico.
4. **Envenenado:** Bajan los PVs gradualmente. Baja resistencia al Tóxico.
5. **Confuso:** Hay un 60% de probabildades de que el personaje confuso sea objetivo de sus propios ataques. Los objetos están desordenados y aparecen con interrogaciones. (NO IMPLEMENTADO)

**Puntos de maná:** Los ataques Especiales y de Ulti consumen X PM dependiendo de cada ataque. Si no se tiene suficiente PM para realizarlos, no se pueden hacer.

**Objetivo(s):** Un ataque puede hacer objetivo a una o varios personajes dependiendo del ataque.

##### Aliados

Tipos de PJs:
    Manin: DPS (mixed)
    Melendi: DPS-Support (ranged)
    Jarfaiter: DPS (Physic)
    Pedro Sánchez & cmpy: Tank (Ranged)
    Abel Caballero: Tank (Physic) (NO IMPLEMENTADO)
    Niño Fumón: Full-Support (NO IMPLEMENTADO)

##### ~~Puntos de Experiencia y qué significa subir de nivel~~

~~El sistema de niveles es el típico que podemos encontrar el cualquier RPG: al acabar un combate toda la party consigue X puntos de experiencia dependiendo del tipo de enemigo que haya derrotado; cuando se consiga acumular suficiente experiencia, el nivel de la party sube automáticamente haciendo que se aumenten las estadísticas de: Daño, HP, MP y Velocidad. La cantidad que se mejora en cada uno de estos depende completamente del personaje. A pesar de seguir este esquema clásico, en ÑRPG el nivel se comparte entre toda la party, de tal fomrma que no existe nivel de personaje, o si queremos considerar que existe, este sería el mismo para todos. De esta forma, al unirse un personaje a la party, este entra con el nivel de la party.~~

##### _Loot_

Al acabar un combate es posible recibir dinero por cada enemigo al que nos hayamos enfrentado. Esta es una de las recompensas del juego, ya que nos permitirá adquirir objetos consumibles en la tienda disponible en la plaza. Estos objetos pueden servirnos para mejorar nuestro estado en una batalla y dar una vuelta al combate a nuestro favor.

### Diseño de Nivel

#### Tipos de Zonas

Todas las zonas son accesibles desde el inicio.

##### Plaza

<img src="https://user-images.githubusercontent.com/99798297/208027202-98c6ab98-4ea5-45ae-bb8e-1872b25208a2.png" style="width:75%;height:75%;">

Es la zona principal del mapa. Conecta con todos los caminos hacia las demás zonas y es donde comenzará la trama. En el centro de la plaza se encuentra el Dinoseto, la estatua principal del juego. 

El juego comienza con una descripción de tu objetivo y lo que ha pasado: una banda de ladrones ha robado piezas del Dinoseto y Manín piensa detenerlos. Manín ve a los 3 maleantes irse cada uno por un lado diferente: Al Norte: las oficinas de Manín Interactive. Al Oeste: El Acantilado. Al Este: El Parque.

Podemos encontrar diferentes NPCs distrubuidos con los que podemos interactuar. Se encuentran también una de las sedes del SERGAS: Servizo Galego de Superebriedade, que cura todas las afecciones que pueda tener la party del jugador. Al lado contrario encontramos a Apu, de la famosa serie de los Simpson, vendiéndonos todos los objetos disponibles actualmente en el juego.

**Estatua:** Dinoseto.

![image](https://user-images.githubusercontent.com/91317502/198385399-70b2aaf2-7134-4bba-870e-40f0f94f993d.png)


##### Parque

<img src="https://user-images.githubusercontent.com/99798297/208027360-a11c4a57-74f8-4b54-a043-ed8b48a2e755.png" style="width:75%;height:75%;">

Podremos acceder a esta zona desde el este de la plaza. Se encontrarán una serie de NPCs en el parque y 2 personajes aliados que podremos añadir a nuestra Party: ***Jarfaiter*** (comenzarás una quest en la que debes comprar un porro y dárselo para que se una a ti) y ***Melendi*** (pedirá a Manín que encuentre su guitarra para unirse a él). En la parte superior derecha hay un pequeño lago, donde encontraremos la Main Quest hablando con un pescador. Nos pedirá encontrar su caña a cambio de copartir parte de su caza. Al recuperarla y devolvérsela al pescador, este pescará una estatua malvada con la que tendremos que pelear para recuperar una de las 3 piezas del Dinoseto.


**Estatua:** Ángel Caído

<img src="https://images.squarespace-cdn.com/content/v1/5bf1e2c19d5abbac28975277/1572290734770-C423BDERL56EOU0DHOQE/Fuente-A%CC%81ngel-Cai%CC%81do_Madrid.jpg?format=1000w" style="width:50%; height:50%;">

**Tipos de enemigos:** Artistas y Culturistas.

**Misión:** Nuestra misión en este parque es ayudar a un pescador del gran lago a recuperar su caña, pues los culturistas se la han robado porque consideran que el parque es "suyo". El pobre hombre da direcciones hacia el bosque, donde cree que se han llevado su preciado objeto. Al conseguir recuperar la caña volvemos al gran lago para entregársela al pescador. Él lo agradece y comparte unas _frías_ con nosotros (ver Contenido - Objetos). Poco después se pone a pescar, pero se ve que ha picado algo muy grande y pide ayuda a Manín. Él le ayuda de buen grado y consiguen sacar del agua la estatua del cuchillero de Albacete, que alberga en su interior una pieza del Dinoseto. Comienza la batalla tras un pequeño diálogo.

##### ~~Puerto~~ 

~~El puerto es la segunda zona del juego. Es una zona más larga que ancha. En toda la parte izquierda hay almacenes y fábricas donde los pescadores llevan sus capturas, y en la zona derecha se encuentra un puerto con barcos atracados, los cuales algunos estarán abiertos. En la zona central del nivel hay un suelo asfaltado con basura, y en el centro ***Abel Caballero***, que te pedirá que recojas la basura que han dejado los fiesteros a cambio de que se pueda unir a tu party. En todo el puerto te puedes encontrar a narcotraficantes que se enfrentarán a ti.~~

~~**Estatua:** Bicha de Balazote.~~

<img src="https://user-images.githubusercontent.com/91317502/198385020-6b7672d1-0920-49a6-b671-245be2b18a45.png" style="width:50%;height:50%;">

~~**Tipos de enemigos:** Narcos, británicos.~~

~~**Misión:** Te encontarás nada más entrar a una anciana que te dirá que ha visto a unos hombres meter una caja pesada de, casualmente, el tamaño de una pequeña estatua en el barco del fondo. Cuando llegas a ese barco se verá que es un barco británico, propiedad del **British Museum**, en el que habrá un guardia que no te dejará entrar. Para poder pasar habrá _dos opciones_: Enfrentarte al guardia y entrar a la fuerza o buscar a un trabajador del barco por el puerto y robarle la llave. Si te enfrentas al guardia saltarán las alarmas del barco y saltarán combates aleatorios mientras estás dentro de él buscando la estatua. Si por el contrario le has robado la tarjeta al trabajador, tendrás que pasar sin que te detecten por el barco para recuperar la estatua. De cualquiera de las formas que entres la estatua estará al final del todo, y cuando llegues los ingleses revivirán a la Bicha de Balazote para que se enfrente a ti.~~

##### ~~Catedral~~

~~La catedral es la tercera zona del juego. Es un edificio más largo que ancho que consta de dos plantas. En la primera planta es parecida a una catedral común: dos retablos religiosos a cada lado, filas de bancos y una tarima donde hay un cura dando misa. Detrás de la tarima hay dos habitaciones que están cerradas inicialmente. En la entrada hay un banco de alimentos que sirve para curar a la _party_. La zona de arriba solo tiene los palcos, donde puedes moverte por los lados debido a que el centro está hueco. En esta zona se encontrará ***Pedro Sánchez***, a quien puedes reclutar para la party.~~

~~**Estatua:** El Lazo - en Benavente (replanteada como un ángel bíblicamente correcto).~~

<img src="https://user-images.githubusercontent.com/91317502/198385190-4fdf290d-475b-47a7-b540-6a1d57a80d1b.png" style="width:50%;height:50%;">

~~**Tipos de enemigos:** Abuelas ultrarreligiosas, curas.~~

~~**Misión:** Al entrar te encontrarás a una mujer que te pedirá ayuda para buscar a su hijo que no había vuelto de catequesis. El niño estará en la sala que está detrás de la tarima donde el cura está dando misa, pero no podrás entrar debido a la homilía. Para poder entrar tendrás que sabotear la misa de distintos modos: romper algún retablo, tirar la lámpara colgante, etc. Cuando se acabe la misa podrás entrar en la primera sala, donde estará el cura que estaba dando misa y te enfrentarás a él. Cuando le derrotes podrás entrar a la siguiente sala donde estará el niño que buscas y la estatua del Ángel Bíblico, la cual el cura revivirá para que te enfrentes a ella. En esta misma sala estará también la entrada a las catacumbas (ver 4.1.6), pero no se podrá acceder todavía.~~

##### ~~Cementerio~~

~~El cementerio será la cuarta y penúltima zona del juego. Es una zona más ancha que alta. En cuanto entras hay un camino de tierra que lleva al norte, donde hay una especie de plaza con la estatua del Ángel Caído; y a los lados lleva a una fila de tumbas. Encima de la fila de tumbas se encuentra un panteón a cada lado, los cuales estarán vallados y en sus entradas hay un jardín antes de poder entrar a la propia estructura. En el fondo norte del cementerio hay un restaurante donde puedes curar a tu party. En los caminos te encontrarás a la Santa Compaña~~

~~**Estatua:** Ángel caído.~~

~~**Tipos de enemigos:** Satánicos y Santa Compaña.~~

~~**Misión:** En cuanto llegas a la plaza central del cementerio habrá un grupo de satánicos que querrán hacer un sacrificio contigo para revivir al Ángel Caído. En cuanto los derrotas te dirán que hay tres grupos más haciendo sacrificios: uno en cada panteón y otro en algún sitio de las tumbas. Uno de los que intentan sacrificar será el ***Niño fumón***, que cuando lo rescatas te ofrecerá su ayuda para la party. En cuanto frustras sus sacrificios te dirán que ya es demasiado tarde, y la estatua habrá revivido, por lo que te tendrás que enfrentar al Ángel Caído.~~

##### Acantilado

<img src="https://user-images.githubusercontent.com/99798297/208027905-5440e2e4-7e66-43eb-9d84-04976fa0b62c.png" style="width:75%;height:75%;">

Una de las 3 zonas donde se recibirá una parte del Dinoseto. Para conseguir, hablaremos con _Kratos_, de la saga God of War y veremos cómo se lanza al vacío con la canción 'Dream On' de fondo, haciendo alusión a un meme reciente. Cuando _Kratos_ acabe de caer al vacío, aparecerá la pieza.

##### Manin Interactive

<img src="https://user-images.githubusercontent.com/99798297/208028038-b8868a1b-295f-4422-9b74-3f210dcb1742.png" style="width:75%;height:75%;">

Aquí podremos encontrar a los 5 desarrolladores del juego dispuestos a matar a Manín por haber atormentado sus vidas durante los últimos meses. Si Manín vence a los furiosos desarrolladores, aparecerá una pieza del Dinoseto para poder continuar la aventura.

##### ~~Catacumbas~~

~~Es la zona final. Nada más entrar en ella por la Catedral habrá un pasillo que desemboque en un laberinto, donde te encontrarás con todos los enemigos principales que estaban en cada zona. Al final de este laberinto habrá una sala donde estará el Dinoseto, al cual te tendrás que enfrentar, y cuando le ganes se acabará el juego~~

~~**Tipos de enemigos:** Todos los anteriormente mencionados.~~

### HUD

#### HUD-Exploración

En la esquina inferior izquierda se muestran las caras de los combatientes de la party con su barra de Vida y Maná
<img src="https://user-images.githubusercontent.com/99798297/208024401-d7a0035f-f1ea-4f49-9040-6a13d0e99541.png" style="width:50%;height:50%">

Al presionar la Q podemos acceder 4 menús distintos:
- PARTY: Podremos ver todas las estadísticas de cada personaje perteneciente a la Party en más detalle. <img src="https://user-images.githubusercontent.com/99798297/208024702-5c934243-aa6e-4ef6-bd9d-7caaa4c710c8.png" style="width:50%;height:50%;">
- ORDER: Podremos cambiar el orden de la party al hacer click en 2 imágenes diferentes. <img src="https://user-images.githubusercontent.com/99798297/208025102-1212e5f5-6b38-441b-a9f6-c5c909e03e34.png" style="width:50%;height:50%;">
- ITEM: Se muestra el inventario con todos los objetos que posee el jugador. <img src="https://user-images.githubusercontent.com/99798297/208024738-6b5a9ee4-0375-431d-aad5-ee91943bc162.png" style="width:50%;height:50%;">
- QUESTs: Se muestran las quests que tenga el jugador en ese momento. <img src="https://user-images.githubusercontent.com/99798297/208024810-a6e2ef91-f191-440c-b5a5-62abd9fb3b49.png" style="width:50%;height:50%;">

#### HUD-Combate

Los enemigos aparacen en la parte central de la pantalla con una barra de vida cada uno, alternando su posición entre encima y debajo del enemigo para que no se superponga con los enemigos adyacentes. En la zona contraria a la barra de vida se mostrarán los iconos de estados alterados (si sufre alguno). Se muestra una vista completa del sprite del enemigo. 
Arriba en el centro se muestra el estado de la _party_: X recuadros (siendo X el número de combatientes aliados) donde se ve el sprite de nuestro aliado y (si tuviera alguno) los iconos de estados alterados que sufra al lado de la cabeza. En la parte inferior se muestra su **barra de vida** y de **maná** con números dentro de las mismas indicando el valor actual y el máximo. Si alguno de los aliados llega a 0 PV su sprite se enrojece y una 'x' lo tapa parcialmente. 
Cuando toque escoger la acción de un aliado, su sprite se anima y gana un borde blanquecino. A la hora de escoger un ataque de uno de los aliados, se despliega una ventana desde la parte de abajo de su recuadro. Este desplegable muestra los ataques y sus estadísticas: Tipo de daño, Usos restantes, Usos totales y Daño. 
Cuando un aliado ataque, se hará una pequeña animación sobre el personaje objetivo. 
En la esquina inferior izquierda se muestran 2 botones: 'Ataque', para que el desplegable mencionado anteriormente aparezca en pantalla y se pueda escoger un ataque, y 'Objeto', para acceder al menú de objetos usables en combate a través de un menú desplegado desde la esquina inferior derecha.

#### Diálogos

<img src="https://user-images.githubusercontent.com/99798297/208026430-f7764e2b-1158-44b7-bba8-1e21c5a990bc.png" style="width:100%;height:100%;">

Todos aquellos NPC interactuables muestran una caja de diálogo al hablar con ellos. La caja tiene 3 zonas:
- El nombre del personaje, blanco sobre un fondo amarillento
- El texto del personaje, blanco sobre un fondo grisáceo semitransparente
- Una etiqueta opcional, que bien puede ser de **Verificado**, azul sobre un fondo blanco semitransparente; o la de **Desarrollador**, verde sobre un fondo blanco semitransparente.

Al interactuar con un NPC, se muestra el texto progresivamente con una pequeña animación. Si el jugador vuelve a interactuar, el texto se mostrará totalmente, quitando toda animación. Si se deja mostrar el texto totalmente, o bien se "cancela" la animación, al volver a interactuar pasaremos al siguiente diálogo o se cerrará la caja de texto si no hay más.

### Contenido

##### Historia

Después de haber sido limpiador de piscinas en verano y haberse adentrado en una _Dungeon_ para recuperar su Patito perdido en la primera entrega de su historia: ***Chill Out***, Manín se muda a Vigo para comenzar su carrera como jardinero. Pasadas unas cuantas semanas se descubre que varias estatuas han sido robadas, todas con un mismo patrón, hasta que el *Dinoseto*, una de las obras más preciadas de la ciudad, ha sido podada y vandalizada de la misma forma que las demás obras de arte. Manín, tan valiente como es, trata de resolver el misterio a causa de la inutilidad de las autoridades locales.

<img src="https://user-images.githubusercontent.com/99798297/208026748-681a6be5-f63d-4eff-b194-00266d7deba2.png" style="width:50%;height:50%;">

##### Objetos

###### LEYENDA:

    - (+) "algo" -> se recupera un poco de "algo". En caso de ser un estado alterado, el objetivo gana el estado alterado "algo".
    - (-) "algo" -> se pierde un poco de "algo". En caso de ser un estado alterado, el objetivo pierde el estado alterado "algo".
    - (++) "algo" -> igual que (+), pero aumenta "algo" en mayor cantidad.
    - (--) "algo" -> igual que (-), pero disminuye "algo" en mayor cantidad.
    - En caso de no especificar objetivos, el objeto solo puede usarse sobre uno a la vez.

###### Consumibles

- **Cigarro**: +maná -vida
- **Kebab**: +vida -maná
- **Fría**: ++vida -maná +borracho
- **Porro**: ++maná -vida +confuso
- **Tarta de Santiago**: ++vida ++maná (toda la party) - Solo existe uno en la partida. (NO IMPLEMENTADA)
- **Dalsy Naranja**: +vida
- **Dalsy Fresa**: +maná
- **Ibuprofeno**:
    · 200mg: +vida
    · 600mg: ++vida
    · 1g: +++vida
- ~~**Grageas**~~:
    · ~~49%: +vida~~
    · ~~49.5%: -vida~~
    · ~~1.5%: el objetivo muere~~

###### Objetos de boss 

- **Trozo de Dinoseto**: Se necesitan tener todos para desbloquear las catacumbas. Solo se pueden usar una vez se tengan todos. 
- **Objeto Único** (NO IMPLEMENTADO): Cada _boss_ tendrá un objeto único que podrá revivir a toda la _party_ dentro y fuera de combate.

### Menús y Flujo de Juego

Desde una pantalla de Inicio podremos comenzar el juego en la plaza (NO HAY GUARDADO). Caminando por las _zonas hostiles_ eventualmente el jugador se enzarzará en un combate. Si el jugador gana el combate se muestran menús de victoria, subida de experiencia y reparto de objetos si los enemigos han _droppeado_ alguno. En el caso contrario, se muestra una escena de _Game Over_ que lleva a la pantalla de título para volver a empezar de 0.

###### PANTALLA DE TÍTULO:

<img src="https://user-images.githubusercontent.com/99798297/208014988-2ed1913d-478c-48ce-9d67-5fa2dd822d3a.png" style="width:100%;height:100%">

###### GAME OVER:

<img src="https://user-images.githubusercontent.com/99798297/208024096-bf8a24f3-641b-4727-943c-eef824c530b4.png" style="width:100%;height:100%">

### Referencias
Nos hemos basado en RPGs clásicos como el Dragon Quest, Final Fantasy o Lisa: the Painful. También gran parte del combate está basado en Pokémon, al igual que las ideas que se tienen sobre los menús.
