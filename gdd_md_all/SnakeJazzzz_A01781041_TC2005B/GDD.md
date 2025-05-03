# **Tower Siege**

## _Documento de Diseño de Juego_

---

##### **Aviso de derechos de autor**

Pedro Mauri Mtz - A01029143
Michael Andrew Devlyn - A01781041
Tomás Molina Pérez Diez - A01784116

## _Índice_

---

1. [Índice](#índice)
2. [Diseño de Juego](#diseño-de-juego)
    1. [Resumen](#resumen)
    2. [Jugabilidad](#jugabilidad)
    3. [Mentalidad](#mentalidad)
3. [Técnico](#técnico)
    1. [Pantallas](#pantallas)
    2. [Controles](#controles)
    3. [Mecánicas](#mecánicas)
4. [Diseño de Niveles](#diseño-de-niveles)
    1. [Temas](#temas)
    2. [Flujo de Juego](#flujo-de-juego)
5. [Desarrollo](#desarrollo)
6. [Gráficos](#gráficos)
7. [Sonidos/Música](#sonidosmúsica)
8. [Cronograma](#cronograma)

## _Diseño de Juego_

---

### **Resumen**

En "Tower Siege", dos jugadores se enfrentan en una batalla estratégica, seleccionando mazos de cartas que representan varias unidades para atacar las torres del oponente mientras defienden las propias. El dominio del posicionamiento de unidades y la gestión de recursos es clave para la victoria en este competitivo juego 2D.

### **Jugabilidad**

El juego empieza al enseñarle a los jugadores en que tablero (mapa) va a ser la partida. Los jugadores después seleccionan cinco cartas de un conjunto de veinte, incluyendo soldados, caballeros, arqueros, catapultas entre otros. El jugador no sabe que baraja escogió su contrincante.
Al usar una carta en el tablero, esto hará que aparezca el personaje de la carta en el lugar colocado. Cada carta tiene un costo de recursos para desplegar y un cooldown después de que ha sido usada. El juego desafía a los jugadores a gestionar estos recursos, desplegar unidades estratégicamente, y conquistar las torres centrales para obtener una ventaja. 
Al conquistar las torres centrales, estas amplían el espacio donde un jugador puede colocar sus cartas.
La victoria se logra destruyendo las torres del oponente o si nadie ha ganado al terminar el tiempo de partida el jugador que ha hecho más daño al oponente gana..

### **Mentalidad**

El juego busca invocar una mentalidad de planificación estratégica y adaptabilidad. Los jugadores deberían sentir la tensión de la gestión de recursos, la emoción de romper las defensas exitosamente, y la necesidad de adaptarse constantemente al campo de batalla en evolución.

## _Técnico_

---

### **Pantallas**

1. Pantalla de Título
    - Iniciar Juego
    - Opciones
    - Salir
2. Selección de Mazo
3. Pantalla de Batalla
    - Menú de Pausa
4. Pantalla de Victoria/Derrota
5. Créditos

### **Controles**

- **Ratón**: Navegar por los menús, seleccionar cartas, colocar unidades.
- **Teclado**: Atajos para la selección de cartas, manejo de tropas.

### **Mecánicas**

- **Generación de Recursos**: Los jugadores reciben recursos con el tiempo, utilizados para jugar cartas.
- **Despliegue de Unidades**: Interfaz de arrastrar y soltar para colocar unidades en el campo de batalla.
- **Interacción con el Terreno**: Las unidades interactúan con el terreno, afectando el movimiento y la estrategia.
-**Manejo de unidades desplegadas**: Las unidades toman la dirección que los jugadores 
indiquen. 
## _Diseño de Niveles_

---

### **Temas**

#### **Campo de Batalla**
- **Ambiente**: Competitivo, intenso
- **Objetos**
    - _Interactivos_: Árboles (cobertura), lagos(obstáculo)

### **Flujo de Juego**

1. Cada jugador selecciona su mazo.
2. Comienza la batalla, los jugadores generan recursos.
3. Los jugadores despliegan unidades, con el objetivo de destruir las torres del oponente.
4. La victoria se logra cuando todas las torres de un jugador son destruidas.

## _Desarrollo_

---

### **Clases Abstractas / Componentes**

1. **Carta**
    - Atributos: Costo, Tipo (Ataque/Defensa), Alcance
2. **Unidad**
    - Derivado de Carta: Soldado, Caballero, Arquero
3. **Torre**
    - Salud, Valor de Defensa

### **Clases Derivadas / Composiciones de Componentes**

- **Unidades**
    - **Soldado**: Bajo costo, unidad básica
    - **Caballero**: Alta salud, rapido
    - **Arquero**: Largo alcance, baja salud
- **Obstáculos**
    - **Árbol**: Proporciona cobertura a ciertas tropas.
    - **lago**No cruzable por la mayoría, potencia ciertas las unidades.

## _Gráficos_

---

### **Atributos de Estilo**

- **Colores**: Vibrantes, colores de equipo distintos para claridad
- **Estilo**: Semi-realista con elementos estilizados, asegurando que las unidades y el terreno sean fácilmente distinguibles.
- **Retroalimentación**: Explosiones para unidades destruidas, contornos brillantes para unidades seleccionables.

### **Gráficos Necesarios**

1. **Unidades**: Sprites animados para cada tipo de unidad.
2. **Terreno**: Texturas variadas para diferentes terrenos (césped, agua, arbol).
3. **Efectos**: Efectos visuales para ataques, recolección de recursos.

## _Sonidos/Música_

---

### **Atributos de Estilo**

- **Instrumentos**: Partituras orquestales con un ritmo dinámico que refleja la intensidad del juego.
- **Efectos de Sonido**: Choque de espadas, pasos de marcha y ruidos de construcción para una jugabilidad inmersiva.

### **Sonidos Necesarios**

1. **Movimientos de Unidades**: Cada tipo de unidad tiene sonidos de pasos distintos.
2. **Combate**: Diferentes sonidos para ataques cuerpo a cuerpo, a distancia y de asedio.
3. **Ambientales**: Ambiente de fondo que refleja el terreno actual.

### **Música Necesaria**

1. **Tema Principal**: Una pieza orquestal heroica que establece el tono épico del juego.
2. **Música de Batalla**: Música rápida e intensa que se reproduce durante el combate, con variaciones dependiendo de la etapa de la batalla.
3. **Temas de Victoria/Derrota**: Temas distintos que se reproducen al ganar o perder una partida, capturando el ambiente de triunfo o pérdida.
4. **Música de Menú**: Música de fondo sutil y atmosférica para los menús del juego y la pantalla de selección de mazo.

## _Cronograma_

---

1. **Fase de Concepto y Diseño** (sem 1-2)
    - Finalizar concepto de juego, mecánicas y documento de diseño.
    - Comenzar arte preliminar y bocetos conceptuales.

2. **Fase de Desarrollo** (sem  3-5)
    - Desarrollar mecánicas de juego principales e implementar jugabilidad básica.
    - Crear niveles iniciales y probar equilibrio.
    - Implementar elementos básicos de UI y controles.

3. **Producción de Arte y Sonido** (sem 6-8)
    - Finalizar todos los activos gráficos incluyendo personajes, entornos y UI.
    - Grabar e integrar efectos de sonido y pistas musicales.

4. **Pruebas y Refinamiento** (sem 9-10)
    - Realizar sesiones de prueba para recopilar comentarios.
    - Refinar jugabilidad, equilibrar unidades y pulir gráficos/sonido.

5. **Preparación para el Lanzamiento** (sem 11)
    - Lanzar el juego.

6. **Soporte Post-Lanzamiento** (Continuo)
    - Monitorear comentarios de los jugadores y abordar cualquier problema con actualizaciones.
    - Lanzar contenido adicional (p.ej., nuevas unidades, mapas) basado en la demanda de los jugadores.

---



