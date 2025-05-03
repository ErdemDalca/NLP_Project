# Docummento de Diseño de "The Wall"
---

## Concepto  

## Historia:
El juego comienza con un diálogo interno de John, diciendo que Bran (su hermano el tullido) había partido hacia el muro con el fin de alejar a los caminantes de la zona, ya que el rey de la noche va tras él. Además algunos de los personajes (Daenerys y Aria) están atrapados en algunas zonas por las que tenemos que pasar para llegar al muro y, por lo tanto, tendremos que rescatarlos para que nos ayuden a salvar a Bran. Tras haber avanzado y rescatado a los dos compañeros, llegamos a la última fase, en el muro, donde encontramos a Bran cara a cara con el rey de la noche. Allí Bran revela su verdadera identidad, diciendo que el rey de la noche es un simple títere y que es él quien controla todo. John se da cuenta de que ha caído en la trampa, ya que al estar ahi John y Daenerys, podrá acabar con los herederos al trono de una vez y ser rey él. Finalmente comienza una pelea final donde habrá una gran cantidad de caminantes que matar y también un caminante gigante. Todos estos enemigos controlados por Bran.  

## Descripción  
Ahora que conocemos un poco la historia, para ganar deberemos detener a Bran y haber rescatado al resto de personajes. Sin embargo, tambien podremos perder, y esta situación se dará cuando mueran todos los personajes que tenemos. En el mapa habrá zonas por las que nos podremos caer, lo que provocará la muerte directa de los personajes y tendremos que volver a empezar. Si se nos muere un personaje, tendremos opción de revivirlo si encontramos una poción de salud, o directamente no revivirlo y curar la vida del personaje que estemos usando. En cualquier momento del juego, podremos cambiar de personaje.

## Mecánicas: 
 
**Andar**  
**Atacar con espada**  
**Lanzar fuego**  
**Lanzar lanza (enemigo)**  
**Embestida enemiga**  
**Saltar**  
**Recoger objetos**   
**Empujar**  
**Aturdir**  

## Dinámicas:  
- Si atacamos a un enemigo y de ese golpe no le matamos, habrá un empuje hacia atrás, lo que permitirá poder empujarlo por un hueco o tirarlo de una altura (en el caso de que se encuente cerca del borde). A su vez, si nosotros recibimos un ataque y no nos mata de ese golpe, podrá pasarnos lo mismo y caer por un hueco tambien, muriendo directamente.
- Si recogemos una poción de salud, tendremos opción de curarnos o de revivir a un personaje.
- Si estamos con el personaje de Daenerys y quemamos a un enemigo, éste tendrá el estado quemado (sufriendo x daño por segundo durante z segundos) y en el caso de tocarnos sufriríamos la quemadura también.
- Si estamos contra el último enemigo (el gigante) y nos golpea, el personaje quedará aturdido durante un tiempo, por lo que deberemos cambiar a otro personaje para poder seguir (en el caso de no querer estar aturdidos todo el rato.)

## Controles:  
**D:** Andar hacia la derecha.  
**A:** Andar hacia la izquierda.  
**W:** Saltar.  
**K:** Atacar.  
**P:** Pausa.  
**Números:** Cambiar de personajes.  


## Personajes:  
Los valores de vida y daño de los personajes y enemigos están sujetos a posibles cambios en un futuro, ya que para establecerlos bien habrá que hacer pruebas con diferentes valores.

- **Nombre del personaje:**  John  
![John](assets/GDD/john.png)  

  - **Vida:** 21  
  - **Daño:** 8  
  - **Ataque:** Cuerpo a cuerpo con una espada de acero valirio.
  - **Armas:** Espada de acero valirio.
  - **Velocidad de movimiento:** 1.  

- **Nombre del personaje:**  Daenerys  
![Daenerys](assets/GDD/daenerys.png)
  - **Vida:** 15  
  - **Daño:** 9  
  - **Ataque:** Ataque a distancia con fuego de los dragones.  
  - **Armas:** Dragones.  
  - **Velocidad de movimiento:** 1.  

- **Nombre del personaje:**  Aria  
![Aria](assets/GDD/aria.png)
  - **Vida:** 19  
  - **Daño:** 9  
  - **Ataque:** Cuerpo a cuerpo con su pequeña pero letal espada.
  - **Armas:** Espada fina.  
  - **Velocidad de movimiento:** 1,5.  

## Enemigos  

- **Nombre:** Caminante lancero  
![Lancero](assets/GDD/lancero.png)
  - **Vida:** 12  
  - **Daño:** 6  
  - **Armas:** Lanza  
  - **Puntos:** 120  
  - **Movilidad:**  Estático

- **Nombre:** Caminante soldado  
Aún sin imagen.
  - **Vida:** 9  
  - **Daño:** 8  
  - **Armas:** Espada.  
  - **Puntos:** 100
  - **Movilidad:**  Lateral
  - **Velocidad de movimiento:** 1,5

- **Nombre:**  Gigante  
Aún sin imagen.
  - **Vida:** 100  
  - **Daño:** 10  
  - **Armas:** Ninguna. Embiste y golpea. 
  - **Puntos:** 1000   
  - **Movilidad**: Lateral
  - **Velocidad de movimiento:** 2

(Está por decidir si poner cuervos que ataquen tambien, en la fase final).

## Items:  
**Poción de escudo:** Protege del daño de un golpe de cualquier enemigo.  
**Poción de salud:** Cura 10 puntos de salud, en el caso de tener un personaje muerto, se dará la opción de revivirlo con 10 puntos de salud.  
**Poción de salto:** Permite saltar el doble de altura durante 30 segundos (por ejemplo).  

## Interfaces:  

- **Nombre de la pantalla:** Titulo.  
  - **Descripción de la pantalla:** pantalla que aparece al principio con la opción de iniciar el juego.  
- **Nombre de la pantalla:** Menu.  
  - **Descripción de la pantalla:** pantalla que aparece cuando pulsamos la tecla P, el cual nos da las opciones de mutear la música o los efectos y volver a la pantalla del título o a la partida actual.
- **Nombre de la pantalla:** Barra de juego.  
  - **Descripción de la pantalla:** zona que aparace en la parte inferior con la vida del personaje, los personajes, la puntuación y las pociones.
- **Nombre de la pantalla:** Niveles.  
  - **Descripción de la pantalla:** Se trata de las pantallas con los diferentes mapas que componen el juego.
- **Nombre de la pantalla:** Game Over.  
  - **Descripción de la pantalla:** Pantalla que aparece cuando muere el último personaje disponible.
- **Nombre de la pantalla:** Win.  
  - **Descripción de la pantalla:** Pantalla final del juego que felicita al jugador por haber completado el juego.

## Niveles/Mapas:  
En principio, habrá 3 niveles. El primero donde podremos rescatar a Daenerys, el segun donde podremos rescatar a Aria y en el tercero tendremos el enfrentamiento final. Aún no tenemos decidido el número de enemigos por nivel ni la distribución que habrá de los objetos.


## Visión general del juego:  

- **Cámara:** Visión 2d con scroll lateral.   
- **Puntuación:** Habrá un  sistema de puntuación que irá aummentando en función de los enemigos que derrotemos y del tiempo que tardemos en completar el juego.   
- **Público:** Estimado a partir de 7 años.  

## Música y sonidos:    

En el menú de pausa podrás realizar dos operaciones sobre el audio del juego: parar la música de fondo o parar los efectos de los personajes.

- **Jugadores:** Los distintos personajes que se pueden utilizar tienen efectos de sonido para sus animaciones: ataque, salto y recibir daño.
- **Banda sonora:**: Es el sonido que acompaña a los distintos niveles. También se escuchará en el menú de pausa.
- **Victoria:** Sonará una canción alegre advirtiendo de que te has pasado el juego.
- **Game over:** Sonará la campana de vergüenza para advertir de que has perdido.

## Miembros del equipo:  
Jorge María Martín y Borja Aday Guadalupe Luis.
