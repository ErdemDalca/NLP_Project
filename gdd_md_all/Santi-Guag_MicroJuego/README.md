
# Game Design Document (GDD)

## 1. Resumen del Juego
- **Título del Juego**: MicroJuego
- **Género**: Disparos de vista cenital
- **Plataforma(s)**: Windows
- **Descripción General**: El jugador controla una nave espacial y debe disparar para destruir la mayor cantidad de asteroides posibles

## 3. Mecánicas del Juego
- **Objetivos**: Conseguir la mayor cantidad de puntos posibles antes de que se reinicie la partida. Los puntos se consiguen rompiendo asteroides, la partida se reinicia cuando la nave impacta con un enemigo.
- **Mecánicas Principales**: La nave se mueve con movimientos de tanque (adelante, atrás y giro). Los movimientos se controlan con WASD o las flechas. Otra mecánica es la de disparar, que se hace cada vez que se da al espacio.
- **Progresión del Juego**: Los puntos se consiguen cada vez que disparas y destruyes un enemigo, y se reinicia cuando la nave es impactada por un enemigo.

## 4. Diseño de Niveles
- **Número de Niveles/Escenarios**: Solo hay un nivel, el jugador inicia en el centro de la pantalla y los asteroides caen de parte superior de la pantalla de un lugar aleatorio.
- **Dificultad**: El tiempo de *spawn* de los asteroides se va disminuyendo cada vez que destruyes un enemigo.

## 5. Diseño Visual
- **Estilo Artístico**: El estilo visual del juego es píxel-art.
- **Personajes**: El personaje principal es una nave espacial.
- **Entornos**: El juego está ambientado en el espacio.
- **Interfaz de Usuario (UI)**: El sistema de puntos se muestra por pantalla con un texto en la parte inferior central de la pantalla que va aumentando cada vez que se destruye un enemigo.

## 8. Requisitos Técnicos
- **Motor de Juego**: Unity
- **Lenguajes de Programación**: C#
- **Repositorio software**: [MicroJuego GitHub](https://github.com/Santi-Guag/MicroJuego)
- **Método de optimización**: Se utiliza el patrón *Object Pooling* para mejorar el rendimiento en la gestión de balas y asteroides, evitando la creación y destrucción continua de objetos. Esto ayuda a reducir el uso de memoria y mejorar la eficiencia del juego.

## 9. Scripts
- **Player**: Este script controla el comportamiento del jugador en un juego. Gestiona el movimiento de una nave espacial utilizando una fuerza de empuje y rotación basada en la entrada del usuario. También controla la creación de balas usando el *Object Pooling* cuando el jugador dispara, reutilizando las balas previamente disparadas para evitar sobrecargar la memoria.
- **Bullet**: Este script controla el comportamiento de las balas en el juego. Las balas se obtienen de un *pool* predefinido y se mueven en la dirección indicada. Se devuelven al *pool* después de un tiempo o al colisionar con un enemigo, en lugar de ser destruidas.
- **EnemySpawner**: Este script controla la generación de asteroides. Los asteroides se obtienen de un *pool* y, tras ser destruidos o después de un tiempo determinado, se devuelven al *pool* para ser reutilizados en lugar de destruirse.
- **EnemyPool**: Este script gestiona un *Object Pool* para los asteroides en el juego. Crea, activa y desactiva los asteroides a medida que se necesitan, optimizando su reutilización. Cuando un asteroide es tomado del *pool*, se posiciona en un punto aleatorio de la parte superior de la pantalla. Los asteroides se devuelven al *pool* cuando ya no están en uso, desactivándolos en lugar de destruirlos.
- **BulletSpawner**: Este script gestiona un *Object Pool* para las balas del jugador. Crea, activa y desactiva las balas de manera eficiente. Cuando una bala es disparada, se toma del *pool* y se coloca en la posición del arma del jugador. Las balas se devuelven al *pool* cuando ya no están en uso, desactivándolas en lugar de destruirlas.

## 10. Prefabs
- **Bullet**: *Prefab* para las balas que dispara la nave.
- **Meteor**: *Prefab* para los enemigos en forma de asteroide.
