# ART GALLERY MANAGER

### Documento de Diseño del juego 

Middlederg Software		

## Introducción

Todo despega definitivamente en los años cincuenta. Tras acabar la guerra, y una vez que la vieja Europa vuelve a despertar, los marchantes de arte sienten que es su momento. Los estilos pictóricos se fusionan entre sí, y los cinco artistas predominantes del panorama inundan las colecciones con sus obras. Cada una de sus lienzos logra reinventar el concepto del arte, dándole otra vuelta cuando nadie lo esperaba. Es el verdadero arte moderno.

Coge tus ahorros, tus amplios conocimientos en historia del arte, y pon a tu galería en boca de todos los expertos. A pesar de que no conseguiste ganarte la vida como pintor en tu juventud en el París de entreguerras, la vida te brinda en tu madurez una nueva oportunidad, esta vez, como marchante de arte.

Art Gallery Manager es un juego que te permite gestionar una galería de arte y su entorno. Compraventa de cuadros, subastas, invertir en arte y obtener ganancias, tanto de manera legal como ilegal, y progresar tanto enconomicamente como, sobre todo, a obtener fama y prestigio.

|      Categoría     |                        Información                         |
|-------------------|-----------------------------------------------------------|
| Estudio           | Art Gallery Manager es un juego de Middlederg software.             |
| Género            | Estrategia                                                |
| Plataforma        | Web (Blazor)                                              |
| Licencia          | Basado en el juego de mesa Modern Art de Reiner Knizia.    |
| Mecánica          | El objetivo del juego es ganar dinero, fama y prestigio. Para ello, se realizará la gestión de una o varias galerías de arte y su entorno. |
| Tecnología        | El desarrollo del juego se llevará a cabo mediante la plataforma .NET con el lenguaje C#. Se utilizará el entorno de desarrollo Visual Studio y se realizará una aplicación de Blazor. |

#### Logros

Describir los varios logros o hitos que el jugador obtiene mientras progresa en el juego. Estos pueden otorgar medallas, personajes secretos o puntos extra.

#### Códigos secretos

- Conseguir dinero extra


## Los estilos

Existen cinco corrientes a las que cualquier autor está adscrito desde el comienzo de su carrera. 

El autor solo puede pintar cuadros de su propio estilo, no obstante, puede cambiar de estilo si se lo propone, aunque lleva tiempo.

Cada partida es diferente. Empezando por el año de comienzo de partida, el estilo de moda se irá sucediendo en el tiempo. 

La corriente mayoritaria puede serlo entre 1 y 4 años. Esta duración se puede ver alargada o acortada si el autor tiene mucho o poco éxito durante las subastas del año. Si durante el primer año, más de la mitad de las obras de autores de esa corriente se han vendido por encima de su precio estimado, y más de un 30 por ciento de las obras vendidas son de esa corriente, la corriente mayoritaria se renueva por otro año.


## Los autores

Los cuadros del juego son principalmente de los cinco autores destacados. 
Estos autores están consagrados, pertenecen a uno de los cinco estilos presentes en el juego, y generalmente la gente anhela sus obras. 

Los cinco autores son los siguientes:

###  Julius / Julia Nex 
###### Belga, 1900 - 1964

Excelente exponente del arte moderno, con confictos extrasensoriales y problemas graves que le hicieron crear obras maestras contemporáneas.


### Alf Bahut 
##### Alemán, 1893 – 1952

Ilustre compositor de arte ordenado, parte fundamental del modernismo clásico, fue el primero de los grandes autores del nuevo siglo, del que bebieron los artistas posteriores.


### Stephanie Darmoir 
###### Francesa, 1924 - 1963

Destacada artista conceptual enmarcada en la corriente pop art, con toques dadaistas e influencias knezieanas.

### Arnem Sadland 
###### Noruego, 1912 - 1976

Alumno abanderado de Rodalf Skwark, consiguió hacer creer a toda una generación que el simplismo y el cubismo eran una caja de hacer dinero cuando se combinaban de manera inspiradora.

### Shokido Koriko 
###### Japonesa, 1935 - 1965

Conocida como la jardinera del sol naciente, por dedicarse a esa actividad antes de alcanzar la fama con la novedosa vuelta de tuerca que le dio al modernismo.


|      Autor        | Estilo         | Visión | Técnica | Prolificidad | Popularidad |
|-------------------|----------------|--------|---------|--------------|-------------|
| Julius Nex        | Tracismo       | 26     | 19      | 2            | 8           |
| Alf Bahut         | Cubismo        | 18     | 27      | 3            | 7           |
| Stephanie Darmoir | Pop art        | 25     | 22      | 2            | 7           |
| Arnem Sadland     | Simplismo      | 25     | 21      | 1            | 7           |
| Shokido Koriko    | Arte abstracto | 28     | 17      | 2            | 7           |

Los autores consagrados tienen una fecha programada de muerte, que si se alcanza durante el juego, hace que fallezcan. Si los cuadros disponibles de ese autor se acaban antes de que llegue esa fecha (debido a su prolificidad, se acaban) el autor fallece en ese año.

### Otros autores

Ademas, durante el juego aparecen jóvenes pintores, de entre 15 y 25 años, cuya carrera puedes apoyar, financiando sus estudios, sus gastos en el taller, su sueldo.
Hay dos opciones de financiación:

- **Con porcentaje**

Puedes financiarlos con un porcentaje en base 5 (3/5, 4/5, etc), pagando esa cantidad de sus gastos. De cada cinco cuadros que pinte, podrás quedarte con ese número de cuadros.

- **Mediante contrato**
 
  - El contrato determina, a grandes rasgos, que el pintor es tu empleado, por tanto debes cubrir sus gastos, estudios, o sueldo. Como contrapartida, podrás quedarte con todas las obras que pinte ese autor, el porcentaje que se indique en el contrato. Cada contrato puede tener una duración de 1, 2 o 3 años.

  - Desde los 15 a los 21 años, los jóvenes autores se encuentran en el liceo, o acedemia de bellas artes, y se deben sufragar sus estudios. Sin embargo, no cobran sueldo, la mantención la provee el propio centro. Cuanto mejor es el liceo al que van, mayor precio, pero la posbilidad de desarrollar mejores características es mayor.
 
  - Cuando el pintor cumple 21 años, si le haces contrato y tienes tu propio taller de pintura, pueden trabajar en él, pagandoles el sueldo negociado. Si no, debes pagarle el porcentaje del alquiler del taller, gastos de consumibles, y el sueldo.

El joven pintor puede abandonar la carrera artistica, y dedicarse a otra cosa, si tú, como mecenas, no estás invirtiendo el suficiente porcentaje en él.

### Características

- **Visión (1 - 30)**
  - Determina la capacidad de interpretar el arte moderno del autor.
  - Se encuadra entre 1 y 30. Determina que nivel de atrevimiento y fuerza tendran las obras creadas. Puede aumentar y disminuir con los años, generalmente será bastante baja cuando el autor sea joven, e irá aumentando a medida que se inviertan recursos económicos en el autor.

- **Tecnica (1 - 30)**
  - Habilidad para crear mejores obras.
  - Se encuadra entre 1 y 30. Determina que nivel de color y fuerza tendrá las obras creadas. Generalmente solo puede aumentar, y lo hace en mayor medida en el periodo formativo. Con mejores maestros aumentará en mayor medida.

- **Prolificidad (2 - 5)**
  -  Es la tasa de obras por año que produce un autor. 
  -  Este valor es fijo para toda la vida del autor, pero se puede ver afectado por cobrar por encima (+1) o por debajo (-1) de la valoración objetiva del autor.

- **Popularidad (1 - 10)**
  - Indica hasta que punto el autor es conocido por la opinión pública
  - Los jóvenes autores siempre tendrán 1.
  - La fama puede verse afectada por los siguientes acontecimientos:
    - +1 - El número de cuadros vendidos el año anterior por encima de su valor es mayor que los vendidos por debajo de su valor
    - +1 – Muerte repentina del autor
    - +1 – Escándalo
    - +2 – El estilo del autor es la corriente mayoritaria

## Los cuadros

Los cuadros tienen un valor estimado, que cambia con respecto a cada vez que el cuadro es vendido. Tienen las siguientes características fijas:

- **Fuerza (1 – 10)** Viene determinada por la técnica y la visión de su autor
- **Color (1 – 10)** Viene determinado por la técnica de su autor
- **Atrevimiento (1 – 10)** Viene determinado por la visión de su autor

Estas características no cambian nunca, una vez que se ha pintado el cuadro. Los cuadros que pinten los autores, tendrán unas características acordes a las habilidades de su autor.

**Características variables:**

- Valor añadido: +1 o -1 cada vez que el cuadro sea vendido por encima o por debajo de su precio estimado.
- Prestigio: Suma de las tres características fijas + la popularidad del autor + valor añadido
- Precio estimado: Precio dependiente del prestigio.
- Interes: Nivel de apetencia que genera en la gente para ir a ver una galería. Media entre (FCA / 3) y popularidad del autor.


## Transacciones

Se organizan cuatro subastas o mercados al año, una por cada estación.

####  1° Subasta de primavera

El frío nos da un respiro, y los coleccionistas de arte salen de sus mansiones para pujar por las obras que darán un aire fresco a sus galerías.

#### 2° Exposición de verano

Con el calor sofocante del verano a las puertas, los coleccionistas y autores exponen las obras de las que quieren deshacerse. Ocasion inmejorable para encontrar gangas.

#### 3° Subasta de otoño

Terminan las vacaciones de verano, y las galerías compiten por hacerse con las obras que echan en falta en sus colecciones. Debes administrar bien tu dinero para conseguir las novedades más codiciadas.

#### 4° Exposición de invierno

La desesperada opulencia del otoño da paso a la fria desilusion invernal, donde se pone a la venta aquello que se sobrevaloró en la anterior subasta.

## Subastas

Las subastas son el medio por excelencia para conseguir obras u obtener ingresos. Puedes llevar las obras que te sobren en tu colección y que no quieras (máximo 4). También puedes decidir, en el momento de entregarlas, si quieres donar el importe de las obras, o si prefieres quedarte con el dinero. La casa de subastas se queda el 10 por ciento si lo donas, o el 20 si te lo quedas.

También puedes pujar por las obras que hayan llevado otros coleccionistas. Siempre se establece un tipo de puja y un precio de salida. La casa te sugerirá un precio, pero puedes modificarlo.

Las pujas duran 7 días, es decir, tienes 7 turnos para pujar o pasar. Los tipos de pujas son los siguientes:

- **Abierta**: Cada postor en cada turno hace, si quiere, una puja por el cuadro. Se entrega como fianza el 20% de la apuesta realizada.

- **A ciegas**: Cada postor hace su apuesta en secreto, entregando la cantidad ofertada. La apuesta más alta, después de los siete días, se llevará el cuadro, y los demás postores recuperarán su dinero. Aunque no se sepa la cantidad puesta por cada entidad que puja, el número de postores si que es público.

## Exposiciones

Las exposiciones contienen muestras de arte que, tanto los autores como otras galerías, tratan de vender a un precio fijo. Tienen una duración únicamente de tres días, de viernes a domingo. Tú puedes poner a la venta hasta 4 obras. La galería que primero ofrezca el precio establecido de salida, conseguirá el cuadro.

Tipos de entradas:
- Reducida. Entrada para un día. La entrada de día para el domingo es la más barata, ya que las mejores obras ya se habrán acabado.
- Completa. Entrada para los tres días de exposición.
- Preferente: Tienes derecho a ofrecer un precio por una obra antes que nadie.
- Tarifa plana: Con un descuento fijo del 15% sobre todas las obras.

¡No hay que olvidarse de los impuestos! Cada transacción de compraventa estará grabada con un 8% de impuestos estatales. Este valor podra variar dependiendo del lugar de origen de la galería del jugador.

Los impuestos se pueden evitar desarrollando la habilidad ingeniería fiscal, pero hay que tener en cuenta que hacienda puede descubrir el pufo, lo que acarrearía importantes multas.

## Objetivo

El objetivo del juego es conseguir la máxima puntuación posible antes de que finalicen los años que dura el juego (15 / Dificultad). La puntuación depende tanto del patrimonio económico como del prestigio.

Al comenzar el último año del juego, el jugador cae enfermo, y tiene ese último año para poner en orden sus asuntos. Al finalizar el año, la partida termina.

## Jugador

Cuando comienza una nueva partida, el jugador selecciona:
- Año de comienzo (Entre 1955 y 1965)
- Sus datos personales como mecenas virtual (nombre, apellidos, y fecha de nacimiento)
- Predilección por un estilo
- Ciudad de origen
- Dificultad (1. Aprendiz – 2. Aspirante – 3. Maestro)

Además, el jugador comienza con:
- Un avatar
- Una edad (20 + (Dificultad - 1) * 10) +- 3
- Una galería situada en la ciudad inicial escogida, con capacidad para exponer 4 obras.
- Algunos miles de dólares en su cuenta, dependiendo de la dificultad. (15000 / Dificultad)
- Un cuadro inicial, del autor consagrado perteneciente al estilo por el que se ha seleccionado predilección, y regalo personal del autor a la familia del jugador. En modo aprendiz puedes elegir el cuadro, en modo aspirante es al azar, y en modo maestro es uno de características más bajas


## Caracteristicas

Las siguientes caracteristicas definen al jugador y se ven alteradas por eventos que ocurren durante la partida:

#### Patrimonio

El patrimonio ecónomico define la riqueza del jugador se compone de:

  - **Dinero en efectivo**
  
Líquido con el que se cuenta y que se puede gastar de manera inmediata.
  
  - **Activos**

Valor de los edificios que albergan las galerías de arte y almacenes, así como el valor estimado de todas las obras que posee el jugador

#### Prestigio

El prestigio es la ponderación de varios factores:

- La media del prestigio de cada cuadro que posee el jugador (50%)
- El prestigio que aportan las galerías del jugador (20%)
- 1% por cada autor promocionado (Máximo 10%)
- Efectividad en subastas (Si los cuadros que sacas a subasta se venden o no) (5%)
- Popularidad en exposiciones (Si los cuadros que expones se venden o no) (5%)
- Donaciones de dinero realizadas en subastas (5%)
- Donaciones de obras al museo nacional (5%)

## Gastos anuales

Es necesario incluir en la partida presupuestaria anual varios gastos que afectan a toda la sociedad del jugador. Estos contratos duran un año, y al comienzo del año siguiente se renueva el contrato o se cambia de compañía.

- Mantenimiento. Es necesario contar con un servicio de mantenimiento. Este se establece con una empresa de mantenimiento, y sirve para todos los almacenes y galerías. Trasladan obras, reparan averias, etc. 
  - Coste anual: Superficie total x media de visitantes mensuales x modificador

- Seguros. Es necesario contratar un seguro anual, que por lo menos cubra la responsabilidad civil. También se pueden contratar seguros más amplios, que cubran inundaciones, incendios, o incluso asegurar las obras expuestas. Pueden ocurrir desastres, por medio de eventos, que afecten a las galerías, por lo que un buen seguro puede dar lugar a una buena compensación económica.

## Galerías de arte

Las galerías de arte son pequeños museos privados en los que los propietarios exponen obras. 

La gente puede visitarlas a cambio de pagar una entrada. Además, el jugador puede contratar a empleados para varias tareas, los cuales pueden contar con habilidades. 

Cada empleado tendra un nivel en cada habilidad, que influirá en mayor o menor medida en el entorno. Cuanto más se invierta en sueldos, más prosperará el negocio.


|   Ubicación   |  Encarece o abarata el precio del alquiler  |
|--------------|--------------------------------------------|
| Distrito bohemio | +25%                                       |
| Centro de la ciudad | +10%                                |
| Barrio residencial | -40%                                    |
| Arrabales | -60%                                        |

En ocasiones, con el devenir de los años y los planes para la reconversión del las ciudades, el tipo de ubicación puede llegar a cambiar, afectando

**Coste de la entrada**

- Es el coste de la entrada para cada visitante, únicamente para ese día. Puede ser gratuita o llegar a costar un máximo de 2 dólares por obra expuesta.

- Día gratuito: Puedes establecer un día gratuito, o una tarde gratuita. Esto ayuda al prestigio.

**Superficie** 

Metros cuadrados de la galería. Suele oscilar entre 30 y 60 metros cuadrados. Por cada ocho metros cuadrados se puede albergar una obra. La galeria se puede ampliar de tamaño, para que quepan mas obras. Hay cinco niveles de ampliación incrementales:

| Metros    | Huecos |
|-----------|--------|
| + 16 metros |   2    |
| + 16 metros |   2    |
| + 24 metros |   3    |
| + 32 metros |   4    |
| + 40 metros |   5    |

**Estado de Suministros**

|         | Luz                 | Agua               | Calefacción                    | Teléfono           |
|---------|---------------------|--------------------|--------------------------------|----------------------|
| -       | Sin instalación     | Tuberías de plomo  | Sin calefacción                | Sin instalación     |
| Básico  | Instalación simple  | Tuberías de cobre  | Calefacción a carbón           | Un teléfono          |
| Moderno | Instalación moderna | Tuberías de PVC    | Calefacción gas                | Centralita           |
| Lujo    |                     |                    | Calefacción eléctrica          |                      |


**Cuartos de baño**

Normalente se requiere uno por cada 90 metros. Dependiente de la legislación de cada pais.

Gestión de las galerías
De manera global a todas las galerías, se gestionan los siguentes gastos:

**Gastos suministros** Hay que pagar luz, agua, calefacción, telefono, internet. Si una galería nueva no tiene un suministro instalado, se puede pagar el coste de instalacion. El cálculo de los suministros se realiza de la siguiente manera:
- Luz -> superficie x visitantes x modificadorLuz + coste basico de luz
- Agua -> numero cuartos baño x visitantes x modificadorAgua + coste basico de agua
- Calefaccion -> igual que luz de octubre a marzo, dependiendo de la latitud de la ciudad.
- Teléfono -> Número empleados x modificador telefono

**Seguridad**

Se debe elegir si contratar una empresa de seguridad. Se puede cambiar de proveedor para el año siguiente. Cada empresa ofrecerá una serie de cosas en el pack, pertenecientes a estas tres categorías

- Circuito de vigilancia: Sin vigilancia - Con circuito cerrado de televisión
- Alarma: Sin alarma – Perros guardianes – Alarma electrónica
- Número de vigilantes: Numero de guardias de seguridad contratados. Cada guardia cubre 20 horas semanales de vigilancia efectiva
  
Cada opcion tiene una efectividad, y un precio anual. 

**Empleados**

- Personal limpieza. Necesitarás 1 limpiador por cada 50 metros que tengas de galería
  - Sin limpieza
    - Perdida de prestigio
    - Facilidad de que las obras se corrompan
  - Sencilla
    - 1 limpiador por cada 50 metros
  - Reluciente
    - 2 limpiadores por cada 50 metros
- Personal taquilla. Necesarios 2 taquilleros para abrir la galería
- Cuidadores.
  - Se ocupan de mantener vigilados los cuadros durante las visitas.
  - Necesario 1 cuidador por cada 10 obras
- Guías. Añade prestigio a la galería
- Prevención de riesgos (Solo disponible a partir de 1950)
  - Impide que las inundaciones y los incendios afecten a las galerías

**Prestigio**

El prestigio se calcula:

- Ubicación (10%)
- Instalaciones
  - 
  - Cuartos de baños
- Servicios (10%)
  - Limpieza
  - Taquilla
  - Cuidadores
  - Guías

### Almacén

El almacen es un edifico anexo a la galería de arte que aloja las obras no expuestas.

Dependiendo de la calidad del sitio, las obras necesitaran cierta restauración. Llegado un punto de no retorno, la obra se estropeará y perderá todo su valor.

Puede albergar hasta 4 obras, y se pueden hacer dos ampliaciones de +2 obras cada una.

### Alquilar una nueva galería

Si cuentas con patrimonio suficiente, puedes abrir una nueva galería.

### Dejar una de tus galerías

Una vez que, tanto el almacén como la galería no contengan cuadros, puedes abandonar la galería, para ahorrar los costes de alquiler. Nunca puedes dejar tu última galería

### Finanzas

Está disponible un informe por año, con los ingresos y gastos que genera cada galería.

## TII / Tecnologías, innovaciones e inversiones

Para optimizar tu emporio, se puede invertir dinero en diferentes tipos de mejoras. A corto plazo supone una inversión, pero a largo plazo permite obtener beneficios.

El funcionamiento de estas tecnologías es sencillo: Cada año, permite elegir tres de ellas.

**Crisis en el sector**

La crisis hace mella en los sueldos, y hay que apretarse el cinturón.
- Disminuye los sueldos de empleados un 25%.
- Disminuye el prestigio de la galería
- Activable solo si hubiera crisis.

**Pequeño desconocido**

Debido a fallos burocráticos, algunos recibos se han traspapelado, y, ¿Quienes somos nosotros para dar centa de ello? 
 
- Activable dependiendo del prestigio del jugador (Solo con prestigio bajo)
- Ahorra costes en los suministros, disminuyendo los gastos de agua, luz y gas.
  
**Contactos con empresas suministradoras**

Una vez que somos una gran empresa, las comercializadores nos ofrecerán mejores condiciones

- Activable dependiendo del prestigio del jugador  (Solo con prestigio alto)
- Ahorra costes en los suministros, disminuyendo los gastos de agua, luz y gas.

**Ingeniería fiscal**

- Coste: Contratar los servicios de abogados para que analicen la situación de la compañía
- Permite evitar el pago de los impuestos derivados de la venta de obras.

**Falsificador**

¿Quién no soñó alguna vez con resucitar obras perdidas? Tan sencillo con contratar al profesional adecuado: Un imitador discreto y eficiente.

- Activable cuando tengas algúna obra deshechada
- Recrea una de las obras que hayas tenido que desechar por falta de mantenimiento.
- Coste: Pagar los servicios del falsificador
- Si se descubre la falsificación, tu prestigio descenderá

**Donar obras al museo de arte nacional**

Puedes elegir entre 1 y 3 obras, y donarlas para siempre al museo de arte nacional estatal. Gracias a esa acción, ganarás prestigio, dependiendo de las obras que hayas donado.

A medida que pasa el tiempo, la acción queda en el olvido (Ingratos...) Cada año transucurrido desde la donación, desciende el prestigio obtenido (10% por cada año). al de 10 años, nadie se acuerdará de la donación realizada.

**Visita al mercado negro**

Puedes intentar comprar obras robadas que se encuentren en el mercado negro. 

# EVENTOS

### Crisis económica

Puede ocurrir que, al inicio del año, ese año resulte ser una año de crisis. Esto afectará de manera directa o indirecta a otros aspectos del juego.

- Si el año pasado no hubo crisis, 20% de que el año actual haya crisis.
- Si en los últimos 10 años se ha sufrido una crisis, bajan un 18% las posibilidades de crisis para el año actual
- Para cada año de crisis, la probabilidad de que el siguiente año continue la crisis es:
    - 2º año -> 75%
    - 3º año -> 60%
    - 4º año -> 50%
    - 5º año -> 40%
    - 6º año -> 25%
    - 7º año -> 18%
    - 8º año -> 12%
    - 9º año -> 5%

### Desastre natural

Puede ocurrir un incendio o inundación en una galería, pero es muy poco probable. Si esto ocurre, la galería es destruida. Si la galería cuenta con un seguro, el jugador será compensado.

 Si la galería cuenta con un departamento de prevención de riesgos, el desastre no afectará a la galería.

 ### Robos

¡Los ladrones codician las obras que albergan las galerías! Si la galería cuenta con buena seguridad, los ladrones pueden ser detenidos. Si son muy habilidosos, o la galería no cuenta con medidas de seguridad adecuadas, se pueden perder cuadros de la propia galería.

### Escándalo

Un escándalo afecta a uno de los 5 autores principales. Puede ser un divorcio, una pelea, etc

Hace que suba la popularidad del autor