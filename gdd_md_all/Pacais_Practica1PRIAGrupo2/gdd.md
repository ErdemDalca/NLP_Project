# Introducción
Dragon Run trátase dunha experiencia corta para windows e móviles Android. O xogador controla a un dragonciño que debe escapar dunha cova na que se caeu intentando aprender a voar. Para iso deberá evitar os monstros e obstáculos que se crucen no seu camiño. 

## Descripción
O xogo tratarase dun "autorunner", é dicir, un xogo no que o xogador avanzará nunha dirección automáticamente. O xogador terá que evitar obstáculos que se aproximarán a él saltando ou agachándose. O público obxectivo será calquera persona que teña 5 minutos libres para gastar nunha experiencia simple pero divertida. O rango de idade serán personas de 3 a 99 anos.

## Trasfondo
Este xogo estaría inspirado por xogos como Geometry Dash ou o Dinosaur Game (o xogo que aparece cando te quedas sin conexión a internet en google chrome).

## Características clave
- <ins>Autorunner</ins>: O xogo está planteado de forma na que o movemento é automático e só precisa dúas teclas para levar a cabo as mecánicas do xogo, inspirándose en cláiscos arcade e xogos pioneiros para dispositivos móviles
- <ins>Obstáculos</ins>: Utilízase un sistema de niveles para xestionar os distintos obstáculos que o xogador debe evitar. O primeiro nivel, a ras de suelo, obligará ao xogador a saltar. No segundo nivel de altura, o obstáculo poderá evitarse saltando sobre él ou agachándose. Os obstáculos de terceiro teñen o obxectivo de castigar un mal uso dos saltos do xogador
- <ins>Gráficos</ins>: Os gráficos terán un estilo retro pixel-art colorido reminiscente á época da sexta xeración de consolas.
- <ins>Dificultade</ins>: O obxectivo do xogo e chegar a obter a maior puntuación posible, e debido ás mecánicas de aceleración, a dificultade escalará con gran rapidez mentras dure a partida.

## Plataformas 
O xogo estará dispoñible de salida para windows, e no futuro próximo planease transportalo a sistemas móviles android.

## Xénero
Dragon Run igual que os xogos nos que se inspira cae na categoría de xogo de plataformas en 2D, concretamente no xénero de autorunner, posto que o xogador deverá moverse polo entorno para evitar obstáculos mentres avanza hacia adiante de forma automática.

## Fluxo de xogo
Ao ser unha experiencia arcade corta o fluxo e moi simple. Ao iniciar o xogo o dragón comenzará a correr, e diversos obstáculos comenzarán a aparecer. A frecuencia coa que aparezcan e a cantidad de tipos de obstáculos que apareceran irán aumentando co tempo. Ao impactar con un obstáculo o xogador perderá unha vida. Ao perder tres vidas, o xogo pasará a estado de Game Over, desde o que se poderá reiniciar a partida.

## Mecánicas
- Xogador
  + Salto: O xogador podrá saltar para evitar verticalmente os obstáculos. O salto ten unha alta velocidade e unha altura fixa.
  + Agacharse: O xogador poderá agacharse para reducir a súa altura e evitar obstáculos que se dirixan á parte alta do xogador
- Obstáculos: Implementase un sistema de obstáculos por nivel de altura:
    + Primeiro nivel: Haberá osbstáculos que aparecerán á mesma altura co personaxe xogador, que se evitarán saltando por encima deles.
    + Segundo nivel: Haberá obstáculos que se dirixirán á parte superior do xogador, polo que este deberá agacharse ou saltar sobre eles.
    + Terceiro nivel: Estes obstáculos aparecerán encima do xogador, castigandoo no caso no que saltase nun mal momento.
    + Durante o xogo aparecerán obstáculos individuales de cada un de estes niveis ou poderán aparecer combinacións de dous niveises
- Nivel
  + En cuestión de programación, o xogador non se desplaza horizontalmente, senon que o escenario se move en dirección do xogador. O nivel repetirase indifinidamente ata que o xogador perda todas as súas vidas.
  + A velocidade de desplazamento aumentará cada 200 puntos, e con ela a dificultade do xogo.
- Puntuación
  + O xogador acumulará puntos durante o tempo que se manteña con vida.
  + Canto máis aumente a velocidade do xogo máis puntos se ganarán por segundo.
- Vidas
  + O xogador comenza a partida con tres vidas. Ao chocar con un obstáculo perderá unha de elas. Ao perder as tres vidas o xogo chega a súa fin.
  + Cada 1000 puntos obtidos, o xogador recuperará unha vida.

## Obstáculos
### Obstáculos individuales
- Cristales: Na cova encontranse agrupacións de cristales afiados a ras do chan. O dragón deberá saltalos para non perder unha vida ao chocar con eles. Este obxeto ten a función de obrigar o xogador ao saltar.
- Morcegos: Unha gran cantidade de morcegos habitan na cova. Estos saldrán volando hacia o dragón a unha altura a cal impactarán na súa cabeza. Para evitar isto, o dragón pode saltar por encima de eles ou agacharse para pasar por debaixo. Os morcegos teñen o obxectivo a nivel mecánico de ofrecer liberdade ao xogador para afrontar un obstáculo de dúas formas distintas. Dependendo de que obstáculos aparecezcan despois, pode ser máis beneficioso saltar que agacharse e viceversa.
- Arañas: Nesta cova habitan tamén arañas de cristal, as cales colgarán do teito a gran altura. Individualmente non son tan perigrosas pero ao combinarse con outros obstáculos limitará a altura ata a que se pode saltar para sortealos.
### Combinacións posíbles
- Cristal + Morcego: Cando aparece un cristal e un morcego ao mesmo tempo ao dragón non lle quedará máis remedio que sortear ambos obstáculos 
- Cristal + Araña: Esta combinación de obstáculos obligará ao dragón a medir un só salto para pasar entre ambo-los dous obxectos.
- Araña + Morcego: Cando estas criaturas se unen o dragón verase obrigado a agacharse para non perder unha vida.

## Físicas
En canto a movemento o dragón pode facer un salto de lonxitude fixa desde o suelo, e logo outro salto máis mentres esté no aire. Estes dous saltos son os que lle permitirá esquivar casi todos os obstáculos.
Por outra parte a velocidade do xogo aumenta lentamente pero de forma exponencial ao subir a puntuación. Como a nivel de programación o que está en movemento e o escenario e os obstáculos e non o dragón, este movemento non interfire coas físicas.
Por outro lado o dragón pódese agachar, o que reducirá a súa hitbox verticalmente e será capaz de evitar os morcegos e as arañas coas que se atope.

## Controles
Solo se usan dúas teclas:
  - Espacio: Salto e doble salto
  - Shift: Agacharse