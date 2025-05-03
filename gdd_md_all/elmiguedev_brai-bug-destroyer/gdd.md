## Brai, bug destroyer

Tomamos el control de Brai, quien arriba de su eva debe avanzar durante el desarrollo de la app destruyendo los bugs e inconvenientes que hacen que el proyecto se demore

Si bien es un camino que parece no tener fin, debemos ayudar a Brai a mantener nuestro código limpio e ir subiendo dev-points para subir de categoría.

Podras hacer de brai el mejor developer del mundo?


## Mecánica principal del juego

El juego es un shoot em up horizontal de scroll infinito en el cual deberemos ir matando a los bugs que nos van apareciendo.

Tendremos obstáculos en el camino, además de los bug, que nos harán la vida imposible y tratarán de frenar el avance de brai, así como powerups que nos ayudaran a sortearlos

Para mover a brai usaremos las flechas para movernos por el plano, y la barra espaciadora para disparar.

## Enemigos y obstáculos

**Bugs** 

Son los enemigos más comunes. Estos pueden aparecer solos y de manera aleatoria (en distintas velocidades), así como de distintos tamaños. 

**Tren de bugs**

Son los mismos bugs, pero que vienen en fila y que hacen que sea mas facil que lleguen a nosotros.

**Quejas**

Entes con forma de gritos, que intentan frenar tu desarrollo

**glicth**

Cuadrado enorme que aparece en pantalla, tirando rayitos y haciendo que la pantalla tenga distorciones de manera aleatoria. Para matarlos necesitas de varios disparos


**Meetings**

En cualquier momento puede sonar una llamada (puede ser el sonido de huddle), apareciendo el repsonsable de la call arriba a la derecha (el cuadrito con el avatar como llamando) el cual te frena y evita que dispares por unos segundos (que molestas que son las calls). Al principio son de duración muy corta, pero a medida que pasa el tiempo y subis tu seniority las calls duran mas tiempo, quitando tiempo para matar bugs


**Demo time**

Es una call especial que, mas que quitarte tiempo, lo que hace es llenar de bugs la pantalla como si fuera una raid, volviendo esto un bullet hell por momentos.


**Bosses**

Luego de un tiempo avanzando aparecen grandes bugs que estan para molestar todo el desarrollo. Algunas posibilidades:
- Ultra bug: dispara y lanza minibugs por todos lados
- La complejidad: super ente sin forma, que confunde y daña al mismo timepo
- El server breaker: tiene ataques de timeout que te ralentizan por momentos, asi como ataques de DoS que oscurecen la pantalla por momentos y llenando de quejas y algunos bugs

Demo time es

## Power ups

**Gato negro**

Es la mascota de Brai que siempre aparece de forma random par ayudarlo a matar algunos bugs

**Code Reviews**

Cuando usas un code review, desaparecen los bugs de la pantalla

**Commits** 

Pequeños logos de Git dando vuelta por la pantalla. Cuando juntas los suficiente, tenes como un power up temporal (MR) que hace que dispares mas y pegues mas fuerte

**Uncle bob**

Uncle bob aparece flotando, cuando lo agarras, te da un power up permanente, que mejora tu arma



## Ideas extra 

- bugs de distintos color con distintas capacidades
- para no permitir que haga balas todo el tiempo, hay una barra que cuando se llena, hace burnout y se le quema la pistola por un rato


## Mejoras

- los HUD deberían "observar" a las entidades y mostrar esa info (haciendo uso del update)
