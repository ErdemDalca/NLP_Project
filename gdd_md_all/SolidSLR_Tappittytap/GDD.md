# TIPPITYTAP

## Datos xerales

- Nome: Tippitytap
- Desenvolvedor: Santiago López Rey (SolidSLR)


## Información xeral do xogo

- Tippitytap é un xogo de ritmo, "puzles", e axilidade casual orientado a dispositivos móviles. O xogador deberá ir pulsando na pantalla os íconos adecuados cando aparezan na pantalla para gañar puntos. Estará composto por diversas fases, cada unha delas más difícil que a anterior. Ó fin de cada fase, o xogador verá a súa puntuación e unha táboa que compara o resultado co doutros xogadores. 

## Características principáis

- Xogo de fácil acceso.
- Curva de aprendizaxe sinxela.
- Compoñente "competitivo" (Ranking de puntuacións).

## Xogabilidade

- O xogo irá sacando botóns na pantalla do xogador, uns deberán ser pulsados e outros non. A cantidade de botóns que se crean dependerá do nivel.
- Cada nivel ten que ser completado nun tempo limitado. Se o xogador non completa o nivel cando acabe o tempo, gárdase a puntuación obtida ó chegar o contador a cero.
- Os botóns que deben ser pulsados serán representados cunha cor verde clara e aumentan a puntuación do xogador.
- Os botóns que non deben ser pulsados serán representados cun roxo chamativo e restán puntuación ó xogador.
- O xogador ten que pulsar ditos botóns o máis rápido posible. Canto máis rápido pulse os botóns correctos, máis puntos gaña. Se pulsa un botón roxo, perde unha cantidade fixa de puntos.
- Os nivéis rematarán cando o xogador pulse tódolos botóns que se poden xerar ou cando o contador de tempo chegue a cero.

## Redes

- As puntuacións de cada xogador son rexistradas no ranking global unha vez que se remata un nivel.
- Integramos un sistema que permite engadir a xogadores como "ámigos".
- Ó rematar un nivel, o xogador verá un ranking cá súa puntuación. Pode escoller entre o ranking global e o ranking de amigos.

## Interfaz

1. Pantalla de inicio:
   - Esquina superior esquerda -> Menú de opcións.
   - Esquina superior dereita -> Menú social.
   - Centro -> Logo animado de Tippitytap.
   - Centro inferior -> Botóns "Xogar"(seguinte nivel) e "Seleccionar nivel".

2. Menú de opcións:
   - Activar/Desactivar son.
   - Selección de tema (Fondo de pantalla e estilo dos botóns).
  
3. Menú social:
   - Arriba -> Etiquetas "Amigos" e "Ranking global".
   - Centro -> Placeholder que amosa o ranking seleccionado. 

4. Selección de nivel
   - Centro superior -> Nome do nivel e mellor puntuación propia (en caso de existir).
   - Centro -> Imaxen representativa do nivel.
   - Centro inferior -> Botón "Xogar".

5. Pantalla de xogo:
   - Cámara fixa ocupando toda a pantalla do dispositivo.
   - Esquina superior esquerda -> Cronómetro con tempo restante.
   - Esquina superior dereita -> Puntuación actual do nivel.
   - Resto da pantalla -> Zona de xogo.

6. Fin de xogo:
   - Centro superior -> Nickname do xogador.
   - Centro -> Ranking global/Ranking amigos
   - Centro inferior esquerda -> Botón "Repetir".
   - Centro inferior dereita -> Botón "Seguinte".
   - Esquina superior esquerda -> Botón "Inicio" (representado cún ícono).

## Niveis

1. Nivel tutorial
   - Carga a pantalla de xogo.
   - Destaca o contador de tempo e explica a súa función.
   - Empeza a correr o contador de tempo.
   - Aparece un botón para pulsar.
   - Para o xogo, destaca o botón e explica a función.
   - Súmanse puntos no contador de puntos.
   - Para o xogo, destaca o contador de puntos e explica cómo obter maior puntuación.
   - Aparece un botón para non pulsar.
   - Para o xogo, destaca o botón e explica a súa función.
   - Desaparece o botón.
   - Mostra mensaxe "Listo? 3, 2, 1. GO!"
   - Comeza o nivel 1

2. Resto de niveis
   - Mostra menxase "Listo? 3, 2, 1. GO!"
   - Aparecen botóns para pulsar e non pulsar de forma aleatoria por calquera parte da pantalla.
   - Límite de tempo diferente en cada nivel.

## Comercialización
- F2P
- App Store (Apple), Play Store (Android)
- Adds in-game
- Opción premium (sen anuncios) a disposición de compra dentro do propio xogo (2.49€).
- Clasificación PEGI 3 con compras In-Game.

## Datos técnicos

1. Hardware obxectivo
   - Dispositivos Android.
   - Dispoisitivos iOS.

2. Software de desenvolvemento
   - Unity