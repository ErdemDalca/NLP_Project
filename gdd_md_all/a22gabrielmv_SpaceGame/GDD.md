# **Game Design Document (GDD)**

## **1\. PRESENTACIÓN/RESUMEN**

### **Título:**

**SpaceGame**

### **Concepto:**

Un **shoot em up en 3D** ambientado en el universo de **Mass Effect**, donde el jugador controla una nave de la Alianza enfrentándose a oleadas de **Reapers y Geth**. Con mecánicas de **combate y oleadas**, el jugador deberá resistir y derrotar a enemigos cada vez más numerosos.

### **Género:**

* Shooter espacial  
* Acción y supervivencia

### **Público:**

* Fans de Mass Effect y shooters espaciales

### **Plataforma:**

* **PC (Windows)**  
* Posible versión para **Web** en el futuro

---

## **2\. GAMEPLAY**

### **Objetivos:**

* **Principal:** Sobrevivir a oleadas de enemigos y acumular la mayor cantidad de puntos posible.

### **Jugabilidad:**

* El jugador controla una **nave de combate** con un arma de proyectiles.  
* Se enfrenta a oleadas de enemigos (Geth y Reapers) que atacan tanto de lejos como a distancias cortas.  
* **Dificultad progresiva**: Mayor cantidad de enemigos con el tiempo.

### **Progresión:**

* Oleadas de enemigos cada vez más difíciles.  
* El jugador **gana puntos** por cada enemigo destruido.

### **GUI (Interfaz Gráfica):**

* **HUD:**  
  * Barra de vida.  
  * Puntuación del jugador.  
* **Pantalla de Inicio** con opciones de control.  
* **Pantalla de Game Over** con botón para volver al inicio.

---

## **3\. MECÁNICAS**

### **Reglas:**

* El jugador **pierde si su nave es destruida**.  
* Puede esquivar y disparar.

### **Interacción:**

* **Controles:**  
  * Movimiento con el click izquierdo (la nave irá hacia el cursor).  
  * Disparo con la tecla F.  
* **Interacción con enemigos y objetos:**  
  * Disparar y destruir enemigos.

### **Puntaje:**

* \+100 puntos por Geth destruido.  
* \+300 puntos por Reaper destruido.

### **Dificultad:**

* **Cada 30 segundos:**  
  * Más cantidad de enemigos en pantalla.

---

## **4\. ELEMENTOS DEL VIDEOJUEGO**

### **Worldbuilding:**

* **Ambientación:** Espacio profundo, en una batalla entre la Alianza y los invasores Geth y Reapers.  
* **Historia (Opcional):**  
  * El jugador es un **piloto de la Alianza** resistiendo la invasión.  
  * Debe sobrevivir el mayor tiempo posible para cubrir la retirada.

### **Personajes:**

* **Nave del jugador:**  
  * **Modelo basado en la Normandía de Mass Effect**.  
  * Habilidades: Disparo, esquiva.  
* **Enemigos:**  
  * **Geth:** Disparan proyectiles y atacan en grupos.  
  * **Reapers:** Más resistentes, aceleran con el tiempo y atacan a corta distancia, drenando la vida del jugador.

### **Niveles:**

* **Mapa infinito en el espacio**, con estrellas y planetas de fondo.

---

## **5\. ASSETS**

### **Música:**

* Banda sonora épica y futurista, inspirada en Mass Effect, libre de licencia.

### **Efectos de sonido:**

* Disparos de la nave y los enemigos.  
* Explosiones cuando un enemigo es destruido.  
* Alertas de daño.

### **Modelos 2D/3D:**

* **Nave del jugador:** Modelo en 3D con animaciones de propulsores.  
* **Enemigos:** Modelos 3D de Geth y Reapers.  
* **Efectos:** Explosiones, partículas de disparos y animaciones de los planetas.

