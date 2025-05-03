# GDD CVs please
GDD con todo el diseño de videojuego reunido.
Algunos temas de diseño todavia no aplicados es necesario consultarlos en el GDD del notion, pero esto busca ser util para consultar dudas a la hora de trabajar en tareas de desarrollo.



# Applicant (el candidato):
- Waiting (esperando a ser entrevistado)
  - *Permite*: llamar al candidato. 
- Reviewing (en la entrevista)
  - *Dispara*: CV y Oferta en estado Idle.
  - *Permite*: interactuar con el CV y la Oferta. Evaluar al candidato como apto o no.
- Evaluated (ya ha sido evaluado)
  - *Permite*: contabilizarlo para el resumen diario.

# Curriculum:
- Idle (esperando a ser revisado)
  - *Permite*: visualizar el CV para interactuar con su contenido.
- Active (siendo revisado)
  - *Permite*: seleccionar las habilidades para preguntar por ellas.
- Approved (aprobado como válido)
  - *Permite*: contabilizarlo como que ha pasado el proceso.
- Rejected (rechazado como válido)
  - *Permite*: contabilizarlo como que no ha pasado el proceso.

# Job Offer (Oferta de trabajo):
- Idle (esperando a ser revisado)
  - *Permite*: visualizar la oferta para interactuar con su contenido. Preguntar si el candidato es capaz de suplir la oferta o no.
- Not Matched (sin emparejar con ninguna actitud)
  - *Permite*: contar como que la oferta no ha sido satisfecha.
- Matched (emparejada con actitud de CV)
  - *Permite*: sumar la puntuación propia de la oferta a tu puntuación diaria (comisión por suplir demanda).

# Flujo cambio de estados
Flujo general para cualquiera de las entidades, puede surgir algun caso a especificar segun avancemos.
![Image](https://github.com/ansousa/CV-Please/assets/4136363/7c73660e-4deb-4183-bbc0-ec18f826c5a6)

# Flujo acciones jugador
**El flujo gira tanto a nivel de diseño como interno de logica del codigo, alrededor de los candidatos.**
Hay **una pila de candidatos**, a los que vas dando paso.
Cada **candidato tiene ya asociado una oferta y su CV, y toda la narrativa sobre el caso concreto**, para hacer mas sencillo y concreto el diseño de las historias.
El flujo de juego se basa en **saber si el candidato dice la verdad o no sobre su validez**, y cuanto estamos nosotros como jugadores dispuestos **a sacrificar nuestro bienestar por ayudar a los demás, o mirar solo nuestro beneficio**.
Para eso puedes **clicar en los distintos apartados y habilidades**, generando una pregunta por el jugador y una respuesta del aplicante.
**Mas adelante se incluiran mas mecanicas** como las preguntas cruzadas, negociacion de salario, o minijuegos especificos para cierto tipo de trabajos, tambien que para medir el tiempo que tienes en el dia, cuenta las acciones que haces, y te limita a cuanta gente puedes ver.
**Algunas ideas adicionales**: para ayudar a las empresas, opcion de espiar a los candidatos por redes sociales(aceptar un informe de ellos que sean como pistas?)
El **saber si el candidato es valido o no**, es algo que se hace por diseño del puzzle, fuera de la logica interna del juego, nos apoyaremos en unas tablas de dificultad segun si el trabajo pide mas experiencia , hacer que sea necesario que cumplan mas requisitos, pero siempre planteado desde la narrativa y no desde calculo interno del juego.

![Image](https://github.com/ansousa/CV-Please/assets/4136363/bf8ced77-4cc7-46af-bb46-4a425626f4e7)


# Diseño paneles
Diseño para mostrar campos en los contenedores:


![Image](https://github.com/ansousa/CV-Please/assets/4136363/926241ff-6d5d-4450-91b6-7900abe09bd2)


# Diseño pantalla principal de juego

En esta primera version se busca solo sustituir lo que existe ahora en la actual versión de la escena de juego principal:

- [ ] Añadir el fondo de pantalla ya generado.
- [ ] Sustituir los elementos interactuables actuales de botones y paneles por elementos integrados en la UI del juego:
1. Abrir paneles del candidato actual.
2. Llamar a candidato actual.
3. Seleccionar pregunta.
4. Realizar preguntar( devolver respuesta)
5. Validar candidato OK/NOK
6. Terminar dia se mantiene de momento como un boton debug, al final lo quitaremos y será un proceso automatico.

- [ ] Editar paneles de CV oferta, chat y log para verse con vista " digital" ( ver diseño debajo).




![Image](https://github.com/ansousa/CV-Please/assets/4136363/10551962-1d3e-4ebd-87b4-7c42075b4b98)
![Image](https://github.com/ansousa/CV-Please/assets/4136363/13ded397-3347-42c1-83c6-20bbb73a6431)
![Image](https://github.com/ansousa/CV-Please/assets/4136363/5e17205d-e039-41cd-9af2-98aa143adb06)


# Diseño flujo pantalla principal PENDIENTE

Esta pendiente repasar y rediseñar el flujo en la pantalla con los nuevos elementos, adaptarlos a maquina de estados y mover ciertas funciones de unos elementos a los nuevos( ejemplo clicar en el candidato no es el control para ver los paneles, el candidato será la forma de ir llamando nuevos candidatos al finalizar un trabajo).








# Diseño pantallas resumen y pagos
<html>
<body>
<!--StartFragment--><h2>Calculo de recompensas</h2>
Definimos el dinero necesario para ese dia/mes , que necesitas para cubrir todos los gastos, con las tablas definidas mas abajo( en principio dificultad base, segun avance la historia y el criterio del jugador, pasar a las tabla dificil o facil)

Para ese dia de trabajo, repartimos ese dinero base, entre los casos indicados( en principio en partes iguales, pero los casos importantes podrían llevar más)
    Contamos con que el jugador no va a acertar el 100% de los casos, ni en condiciones buenas, asi que le faltará dinero, o lo compensará haciendo en buen tiempo o con las condiciones especiales.
     El tiempo penaliza o no en cada candidato

Al final se calcula y se le entrega ese dinero.
Debe elegir en que categorias gasta el dinero, y guardará el dinero que le sobre.
Si no gastas en algun area, se anota para aplicar posibles penalizadores en la siguiente pantalla de resumen
Aceptar estos pagos continua al siguiente dia


<h2>Que mostrar en pantalla</h2>

- Lista resumen de trabajo hecho
    - Ir uno a uno con los casos
    - Definir si acertó o fallo , bonos y penalizadores
    - Definir texto de acierto o fallo en la clase puzzle y pasarlo al validationResult??
- Siguiente escena
- Los gastos del mes
    - Mostrar dinero total en cuenta
    - Eventos especiales
- Intro texto para meter temas de historias o dialogos por sucesos/eventos como no pagar algo y sus consecuencias
- Aceptar los pagos y continuar al siguiente dia

<h2>Valores a tener en cuenta en esta pantalla</h2>

- Contador dias sin pagar un area especifica
- Array con los vailidationResult LISTA RESUMEN DEL DIA HECHO
    - Aqui habra que añadir en el puzzle y al validationResult, el valor asignado base, con bono y con penalizador
    - Mostrar lo que gana con cada caso ysi tuvo bonos o no
    - Penalizadores por falla
- Dinero en la cuenta
- Areas a pagar y dinero a pagar ( por partes y total)
- Diario de pagos en cada area ( array con bool)
- Estado del jugador ( avisar de penalizadores)
- Eventos especiales
- Campo para notificar cambios o temas de la historia que se deban indicar al jugador( que secretamente indican cambios en dificultad o pagos)


<h2>Estructura de datos </h2>
Cargar lista de "ValidationResult" enviado de la escena de juego. 

Gestionar variables en global sobre eventos del nivel o eventos independientes( se implementará mas adelante). 

Cargar al menu los gastos y aplicar los cambios al saldo y a las condiciones de impagos en global. 

<h2>Flujo de trabajo de la escena </h2>
Cargar y mostrar uno a uno los candidatos y sus resultados, aplicar paga, bonos y penalizaciones al saldo actual.

Al terminar, mostrar la pantalla de pagos mensuales para que el jugador elija como gastar sus recursos disponibles

Notificar y aplicar las consecuencias de impagos previos.

<h2>tablas de dificultad y dinero</h2>
<p>Se cambia el tier de dificultad en funcion de que habra ciertos puzzles marcados como “ayuda a empresa” o “ayuda a persona” e iremos contando hasta llegar a un baremo.
Esto se guarda en el global y cada dia se calcula si se cumple el requisito.</p>

DIFICULTAD NORMAL( ni cumplir con la empresa ni ayudar a la gente) |  
-- | --
  |  
  | sueldo necesario para pasar el mes
enero | 1000
febrero | 1200
marzo | 1400
abril | 1600
mayo | 1800
junio | 2000


DIFICULTAD FACIL ( ayudas a la empresa todo el rato) | Se rebaja por que te dan comisiones
-- | --
  |  
  | sueldo necesario para pasar el mes
enero | 1000
febrero | 1050
marzo | 1100
abril | 1150
mayo | 1200
junio | 1250




DIFICULTAD DIFICIL ( ayudas a la gente todo el rato) | Te penalizan en la empresa
-- | --
  |  
  | sueldo necesario para pasar el mes
enero | 1000
febrero | 1200
marzo | 1400
abril | 1600
mayo | 1800
junio | 2000



<h2>Areas a cubrir de pagar</h2>
<p>Areas a cubrir de pagar: (mensuales)alquiler , comida, transporte, (ocasionales)medico, ropa, reparaciones hogar/coche</p>
<p>No cubrir pagos mensuales: alguiler( retrasos y comisiones), comida (enfermar), transporte(penalizaciones trabajo sueldo)</p>
<p>No cubrir gatos ocasionales: medico( enfermar mas, game over), ropa ( penalizacion trabajo sueldo), reparaciones hogar/coche ( enfermar o llegar tarde trabajo, penalizacion sueldo.</p>
<!-- notionvc: 11974aef-9394-46fc-bc7a-e0fe42220d7f --><!--EndFragment-->
</body>
</html>


#Detalles de validaciones( copipasteado de la tarea, revisar y exponer como funciona y estructura mejor)

Hay un flujo que queremos completar, el que cada trabajo tiene unas valoraciones al acabarse( tanto basicas como el candidato es correcto, como la de tiempo o las condiciones especiales añadidas) que cuando se hace el resumen de final de dia, se tiene que mostrar un resultado de OK/NOK y recompensa o finalizacion con un mensaje acorde.

Para esto creamos un nuevo resource detail_validation, que añadimos a cada puzzle, con estos resultados.
La logica de validacion va por el tipo de condicion, aqui mezclamos las basicas de tiempo y candidato correcto a las adicionales, y toda esta carga de prueba va al game manager, para el puzzle y la pantalla de resumen, solo es logica de mostrar resultado.

Siguiente paso entender donde cargar mejor esta info del puzzle en el objeto Applicant en la escena principal.
Una vez cargado generar metodo procesar condiciones de validacion.
Dentro de esto, se añade este resultado en el aplicant result, para cargarlo posteriormente en la escena de resumen.

Repasar bien de desmontar la logica de carga no dinamica en el boton de decision_made y montar lo dinamico y que necesitas para mandar a la pantalla de resumen.

Edit1: tienes ya los detail validation cargados y calculados en applicant, falta añadirlo a la clase ApplicantResult con solo el resultado, es el applicant.validation que se quedó cargando en el otro boton , quitar eso y meter lo calculado antes.

Añadida informacion en los puzzles creados de compañia y categoria de trabajo.
Se añade esta info al applicant, y a la estructura del aplicant result.
Correccion de enums para igualar el valor en las condiciones.
Eliminamos carga no dinamica en la pantalla de resumen de resultados de candidatos.
Quitamos la carga no dinamica de applicant result en evento de validar o no validar los candidatos, aqui ahora solo se envia el enum, y se genera el result en el applicant.process_aplicant


<h2>Diseño pantallas</h2>

<h3>Pantalla de resumen resultado candidatos</h3>
1 - Foto del candidato.

2 - Nombre completo, puesto y empresa a la optaba.

3- Respuesta narrativa de si el candidato fue apto o no.

4 - Bonos o penalizaciones( en distinto color) respecto al caso revisado.

5 - Continuar al siguiente candidato 



![Image](https://github.com/ansousa/CV-Please/assets/4136363/65faa39a-2df6-401d-b135-49a24528d2d6)




<h3>Pantalla de pago</h3>

1- cuadro de dialogo para contar temas de la historia de ese nivel en funciones de acciones del jugador(esto puede meterse directo al global o crearemos otra estructura de datos para los niveles, donde calibramos sus acciones con los candidatos " de historia")
2- Cuadro de gastos: los gastos del mes, sueldo y dinero ahorrado, el jugador elige que gastos hace y cuales no, con consecuencias en los dias posteriores.
3- Cuadro de dialogo para mostrar las consecuencias de no pagar algo.
4- Aceptar y continuar al nivel siguiente.

![Image](https://github.com/ansousa/CV-Please/assets/4136363/26574b4b-f48b-4c34-9de9-97609f77e973)







### **Borrador de tareas**
Plantear estructura de datos para los parametros que queremos medir por nivel: eventos de historia, la brujula moral del jugador, los gastos, los impagos, los eventos NO asociados a candidatos( puede ser a dias concretos o eventos que medimos a lo largo del tiempo como la brujula moral).
   -> Una buena solucion sería, tener clases "Evento" que tienen como propiedades el evento que las define, los parametros para que salten y las respuestas necesarias, y en una clase Manager, tener todo cargado y listo para consultar y comprobar?

Ver como funciona el cambio de escena.

Pendiente analisis en reunion y sacar tareas para esta epica

Se crea una pagina en notion para cuando afrontemos esto.
De momento ya se gestionaron los detalles de validaciones de los candidatos, que es lo minimo con lo que queremos ir ahora.
Si hace falta gestionar mas adelante eventos especiales para X dia, volveremos mas adelante para desarrollarlo.



#Como hemos ajustado y cambiado los paneles para que se ajusten a la resolucion

Hemos cambiado la resolucion y ajustado los paneles dejando sus "anchors" en las esquinas.Con esto y manteniendo el cambio de resolucion en el proyecto a "viewport" y mantener aspect ratio , se puede cambiar la resolucion y nada se descuadra.
https://www.youtube.com/watch?v=blPqie3Z_F0 <--guia seguida y explica como setear resolucion por codigo.



Para jugar con que las lineas de los paneles ocupen solo el espacio que necesitan, hay que setear un minimo de tamaño, dejar el vertical en expand y poner strech ratio a 0:
Hay que ver si se puede calcular  en caliente, cuanto texto ocupa la info que lleva para setear el tamaño minimo.

![Image](https://github.com/ansousa/CV-Please/assets/4136363/3a8dac22-1e89-4838-a6d1-d6175542f859)



![Image](https://github.com/ansousa/CV-Please/assets/4136363/69413b73-842b-464b-88f4-3583bc64c9dd)



## Explicación flujo cargar escenas
Godot permite gestionar clases singleton con "Autoload" una opcion de añadir scripts/nodos a todas las escenas y ser accesibles.
Los scripts habilitados como Autoload aparecen en la raiz de todas las escenas, ademas de lo definido para esa escena.
Usando esto, podemos gestionar la transicion de la escena actual a otra, y de mientras mantener una pantalla de carga ocultando esta transición.

Toda la info en este video:
https://www.youtube.com/watch?v=5aV_GSAE1kM
Documentacion sobre autoload:
https://docs.godotengine.org/en/3.5/tutorials/scripting/singletons_autoload.html

## Pasos para crear el load manager
Definir una escena de carga, para la transicion.
Crear un script load manager con autoload.
Tener dos escenas entre las que transicionar.

## Load manager script
Asignamos una propiedad que sea la escena de carga.
Un metodo que como parametros tendrá la escena actual y la escena a cargar.
Instanciamos la escena de carga y llamamos a object.call_defferred(), que nos asegura que no se cargará la escena de carga, hasta que termine de ejecutarse todo el codigo de la actual.
Con ResourceLoader.load_interactive() cargamos la siguiente escena, esta se irá cargando poco a poco segun le indiquemos en las siguientes lineas con el metodo object.pool().
Con object.queue_free() en la escena actual liberamos la escena.
Añadimos un delay para que se vea un tiempo la escena de carga.
Hacemos un bucle en el que en cada vuelta ejecutamos .poll() sobre la carga de la siguiente escena
    Aqui puede irse actualizando una posible barra de % de carga.
Cuando se cargue completamente , finalizamos el bucle, instanciamos la nueva escena y eliminamos la de carga.








