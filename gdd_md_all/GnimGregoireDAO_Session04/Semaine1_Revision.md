# Fiche de Révision - Semaine 1

## 1. Notion de conception de jeu (Game Design)

### 1.1 Éléments fondamentaux

- **Gameplay** : Ensemble des interactions entre le joueur et le jeu
- **Game Loop** : Boucle principale du jeu (Input → Update → Render)
- **Game Mechanics** : Règles et systèmes qui définissent l'interaction
- **Level Design** : Conception des niveaux et de l'environnement de jeu

### 1.2 Documents de conception

- **GDD (Game Design Document)** : Document détaillant tous les aspects du jeu
- **One Page Design** : Résumé concis du concept du jeu
- **Technical Design Document** : Spécifications techniques
- **Art Bible** : Guide du style visuel

## 2. Prise en main de Unity

### 2.1 Interface principale
- **Scene View** : Fenêtre de manipulation des objets
- **Game View** : Aperçu du jeu en cours d'exécution
- **Hierarchy Window** : Liste des objets dans la scène
- **Project Window** : Ressources du projet
- **Inspector** : Propriétés des objets sélectionnés

### 2.2 Navigation de base
- **Pan** : Alt + Clic gauche
- **Zoom** : Molette souris
- **Orbit** : Alt + Clic droit
- **Frame Select** : F (centre la vue sur l'objet)

## 3. Types de jeux vidéo

### 3.1 Genres principaux
- **Action**
  - Beat'em up
  - FPS (First Person Shooter)
  - TPS (Third Person Shooter)
  - Plateforme
  
- **Aventure**
  - Point & Click
  - Visual Novel
  - Action-Aventure
  
- **RPG (Role Playing Game)**
  - JRPG
  - Action RPG
  - MMORPG
  
- **Stratégie**
  - RTS (Real Time Strategy)
  - 4X
  - Tower Defense

### 3.2 Sous-genres et hybrides
- Roguelike/Roguelite
- Metroidvania
- Survival Horror
- Battle Royale

## 4. Concepts de base Unity

### 4.1 Scènes
- Unité de base d'organisation
- Contient l'environnement, les personnages, l'UI
- Gestion des transitions entre scènes
- Optimisation par scène

### 4.2 GameObjects
- Conteneur d'éléments de base
- Hiérarchie parent-enfant
- Transform (position, rotation, échelle)
- Tags et Layers pour l'organisation

### 4.3 Scripts
- Composants personnalisés en C#
- MonoBehaviour comme classe de base
- Méthodes de cycle de vie:
  ```csharp
  void Start() { } // Initialisation
  void Update() { } // Mise à jour par frame
  void FixedUpdate() { } // Physique
  ```

## 5. Patron de conception Composante

### 5.1 Principes
- Composition plutôt qu'héritage
- Réutilisation du code
- Flexibilité et modularité

### 5.2 Implémentation dans Unity
- Components comme blocs de construction
- Combinaison de comportements
- Communication entre composants
- Découplage des fonctionnalités

### 5.3 Exemples de composants
- Transform
- Rigidbody
- Collider
- Renderer
- Audio Source
- Custom Scripts

## 6. Physique 2D

### 6.1 Composants de base
- **Rigidbody2D**
  - Dynamic
  - Kinematic
  - Static
  
- **Collider2D**
  - BoxCollider2D
  - CircleCollider2D
  - PolygonCollider2D
  
### 6.2 Forces et mouvements
- AddForce()
- velocity
- gravité
- friction

### 6.3 Détection de collisions
```csharp
void OnCollisionEnter2D(Collision2D collision)
void OnCollisionStay2D(Collision2D collision)
void OnCollisionExit2D(Collision2D collision)
```

### 6.4 Triggers
```csharp
void OnTriggerEnter2D(Collider2D other)
void OnTriggerStay2D(Collider2D other)
void OnTriggerExit2D(Collider2D other)
```

### 6.5 Layers et Matrix de collision
- Configuration des interactions
- Optimisation des performances
- Filtrage des collisions

## Points clés à retenir
1. La conception de jeu est un processus itératif
2. Unity utilise une approche basée sur les composants
3. La physique 2D requiert une bonne compréhension des forces
4. Les scènes sont les conteneurs principaux dans Unity
5. Les scripts permettent de personnaliser les comportements
6. La documentation est votre meilleure amie

## Exercices pratiques suggérés
1. Créer une scène simple avec des objets basiques
2. Implémenter un mouvement de personnage en 2D
3. Gérer des collisions simples
4. Créer un système de points avec triggers
5. Organiser une hiérarchie d'objets cohérente
