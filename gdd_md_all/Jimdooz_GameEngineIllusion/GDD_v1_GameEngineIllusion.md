# GameEngine Illusion : Game Design Document

## Genre

Plateformer 3D, puzzle

## Camera

3ème personne derrière le character, suit la tête. Discuter de la position de la caméra par rapport au personnage pour voir les objets devant lui. 

## Controls 

* Zqsd mouvement personnage
* Souris mouvement caméra
* Clic gauche attraper/activer un objet
* Clic droit lâcher un objet en direction de là où pointe la caméra
* Space pour sauter

## Character

Au mieux, bipède. 

## Histoire / But

Le bâtiment s'est en partie effondré, il faut sortir de là. 

## Ambiance

Sombre, nuances de gris, flèches bleu en effet "gloom" (néon), objets interactifs avec une surbrillance colorée (orange par exemple), son ? (si moteur de son).

## HUD

Rien.

## Game World

Dans un bâtiment sans vie. Une suite de salles qui jouent sur la verticalité, où on a l'impression qu'il y a de la vie alors qu'en fait non, créant des zones de gouffre où le personnage peut tomber.

## Gameplay

* Sauter par dessus une plateforme
* Sauter par dessus un obstacle
* Grimper/escalader
* Pousser des objets
* Récupérer un objet
* Inventaire virtuel non accessible pour le joueur (un booléen : clé ? ok)
* Activer/Désactiver des éléments
* Pas de lampe que le personnage pourrait tenir

## Mécaniques

* Quand un objet, se trouvant près du personnage, peut avoir une interaction (pousser, récupérer, activer), il se mets alors en surbrillance.

## Puzzles

* Deux plateformes éloignées, le vide entre les deux (mort si chute), pour voir le labyrinthe de planches il faut regarder vers le bas
* Trouver une clé pour ouvrir une porte
* Pousser un objet pour libérer le passage/sur des activateurs
* Escalader une succession de plateformes gauche-droite pour aller à un niveau au dessus
* Si on regarde sur le chemin normal on voit pas une flèche qui indique un escalier ou une plateforme, il faut se mettre dans l'autre sens 

## Inspirations

Resident Evil
Superluminal
Inside
Limbo
White Night