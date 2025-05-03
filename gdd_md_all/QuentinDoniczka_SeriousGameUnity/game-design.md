# Serious Game Design Document

## Module 1: Titre et Résumé
### 1.1 Titre du Projet
- Nom : "VisuaLogic: Apprentissage par la Visualisation"
- Pourquoi ce titre :
  - "Visual" représente l'aspect visuel et la représentation des concepts
  - "Logic" fait référence aux concepts logiques et mathématiques enseignés
  - La fusion des deux termes crée un nom mémorable qui reflète le concept central du projet
  - Le sous-titre précise directement la fonction principale de l'application

### 1.2 Résumé/Pitch
VisuaLogic est un Serious Game innovant qui transforme l'apprentissage de concepts abstraits (SQL, mathématiques) en expériences visuelles et interactives. Le joueur découvre et maîtrise ces concepts à travers des métaphores concrètes et ludiques, comme des groupes de soldats représentant des commandes SQL ou des balances physiques pour les équations mathématiques. L'objectif est de rendre l'apprentissage plus intuitif et engageant grâce à des représentations visuelles dynamiques.

#### Exemple Type Serious Game
- Contexte : Formation éducative et professionnelle
- Public cible : Étudiants et professionnels souhaitant maîtriser SQL et les mathématiques
- Objectif principal : Transformer l'apprentissage abstrait en expérience visuelle et interactive

### 1.3 Positionnement
- Unicité :
  - Approche unique de visualisation des concepts abstraits
  - Système de progression adaptative permettant de partir de zéro
  - Métaphores originales et mémorables (soldats pour SQL, balances pour mathématiques)
- Impact attendu :
  - Meilleure compréhension des concepts abstraits
  - Développement d'une intuition mathématique et logique
  - Réduction de la barrière d'entrée pour l'apprentissage de SQL et des mathématiques


## Module 2: Objectifs du Serious Game
### 2.1 Objectifs Pédagogiques ou Professionnels
- Apprentissage visé : Transformer l'apprentissage des concepts abstraits en expérience visuelle
  - Comprendre et maîtriser les commandes SQL de base à travers des métaphores visuelles
  - Assimiler les concepts mathématiques grâce à des représentations concrètes
  - Développer une intuition pour la résolution de problèmes logiques
- Exemple concret : Dans une mission SQL, le joueur doit regrouper des soldats par type (SELECT * FROM soldiers GROUP BY type) en visualisant directement l'impact de chaque mot-clé de la requête

### 2.2 Objectifs de Gameplay
- Immersion :
  - Traduire chaque concept abstrait en élément visuel manipulable
  - Créer un lien direct entre les actions du joueur et les résultats visuels
- Engagement :
  - Système de progression par niveau de difficulté
  - Récompenses visuelles immédiates lors de la réussite d'exercices


### 2.3 Mesure de Succès
- Indicateurs clés :
  - Nombre d'exercices résolus correctement
  - Temps passé par concept avant maîtrise
  - Taux de réussite par type de requête SQL
  - Nombre de tentatives avant réussite
  - Temps de réflexion moyen par type d'exercice
  - Utilisation des aides contextuelles
- Impact attendu :
  - Meilleure compréhension des concepts abstraits (mesurable par les tests)
  - Réduction du temps d'apprentissage des concepts SQL
  - Augmentation du taux de rétention des connaissances
  - Amélioration de la confiance dans l'utilisation de SQL
  - Capacité à résoudre des problèmes complexes de manière autonome

#### Exemple Type Serious Game
- Mission typique :
  - Une requête SQL simple comme "SELECT * FROM soldiers WHERE type = 'archer'" est représentée visuellement : les soldats se déplacent et se regroupent selon les critères de la requête
- Objectif : Comprendre l'impact de chaque mot-clé SQL en observant son effet direct sur les groupes de soldats
- Feedback donné au joueur :
  - Visualisation immédiate du résultat de chaque commande
  - Messages d'erreur visuels en cas de syntaxe incorrecte
  - Suggestions visuelles pour corriger les erreurs

## Module 3: Public Cible

### 3.1 Profil des Utilisateurs
- Démographie :
  - Étudiants de tous niveaux souhaitant approfondir leurs connaissances
  - Age : À partir de 12 ans (accessible aux plus jeunes)
  - Expérience : De débutants à confirmés, avec une attention particulière pour les apprenants sans prérequis
- Préférences de jeu :
  - Applications pédagogiques interactives
  - Systèmes de visualisation intuitive
  - Progression graduelle dans la difficulté
- Besoins spécifiques :
  - Apprentissage progressif des concepts
  - Contenu adapté au niveau de chacun
  - Possibilité de réviser et pratiquer à son rythme

### 3.2 Contexte d'Utilisation
- Environnement d'Apprentissage :
  - Usage personnel pour l'auto-formation
  - Complément aux cours traditionnels
  - Support d'apprentissage en formation professionnelle
- Temps Disponibles :
  - Sessions de 5 à 15 minutes par concept
  - Sauvegarde automatique de la progression
  - Exercices courts mais réguliers

### 3.3 Motivations du Public
- Objectifs des utilisateurs :
  - Comprendre visuellement des concepts abstraits
  - Progresser à leur rythme sans pression
  - Valider leur compréhension par la pratique
- Récompenses recherchées :
  - Satisfaction de voir les concepts devenir plus clairs
  - Progression visible dans la maîtrise des concepts
  - Déblocage de niveaux et concepts plus avancés

#### Exemple Type Serious Game
- Profil d'un utilisateur typique :
  - Thomas, 19 ans, étudiant en informatique débutant en SQL. Il a du mal à visualiser mentalement l'impact des requêtes sur les données
  - Il utilise l'application entre ses cours pour renforcer sa compréhension
- Scénario proposé :
  - Une requête SQL avec jointure doit être comprise et appliquée. Thomas doit :
    - Observer les différents groupes de soldats disponibles
    - Comprendre visuellement le concept de jointure
    - Créer la requête appropriée en voyant son effet en temps réel
  - Objectif : Maîtriser le concept de jointure à travers la visualisation

  

## Module 4: Gameplay et Mécaniques

### 4.1 Description du Gameplay
- Type de jeu : Application éducative interactive avec visualisation dynamique
- Rôle du joueur : Apprenant interagissant avec les concepts visuels
  - Objectif principal : Comprendre et maîtriser les concepts abstraits à travers leur représentation visuelle
- Activités principales :
  - Manipulation des éléments visuels représentant les concepts
  - Écriture de commandes SQL avec feedback visuel immédiat
  - Résolution d'équations mathématiques via des représentations concrètes

### 4.2 Mécaniques Principales
- Système de commandes SQL :
  - Éditeur de requêtes avec coloration syntaxique
  - Auto-complétion intelligente des mots-clés SQL
  - Historique des requêtes précédentes
  - Templates de requêtes courantes

- Système de visualisation :
  - Animations fluides des mouvements de troupes
  - Codes couleurs pour différencier les types d'unités
  - Indicateurs visuels pour les conditions (WHERE)
  - Visualisation des jointures par liens physiques

- Système d'aide :
  - Aide contextuelle selon le type de requête
  - Suggestions basées sur les erreurs communes
  - Guide visuel pas à pas pour les nouveaux concepts
  - Détection automatique des erreurs de syntaxe

### 4.3 Progression
- Système de niveaux :
  - Chaque niveau introduit un nouveau concept ou une nouvelle complexité
  - Exemple SQL :
    - Niveau 1 : SELECT simple sur un groupe de soldats
    - Niveau 2 : WHERE avec conditions simples
    - Niveau 3 : GROUP BY avec visualisation des regroupements
  - Exemple Mathématiques :
    - Niveau 1 : Équations simples avec la balance
    - Niveau 2 : Systèmes d'équations
- Difficulté croissante :
  - Introduction progressive de concepts plus complexes
  - Combinaison de plusieurs concepts dans un même exercice

### 4.4 Gamification
- Récompenses :
  - Points d'expérience pour chaque exercice réussi
  - Badges de maîtrise pour chaque concept
- Classements :
  - Comparaison optionnelle avec d'autres apprenants
  - Statistiques personnelles de progression
- Succès :
  - "Maître SQL" pour maîtriser toutes les commandes de base
  - "Expert des Équations" pour résoudre des problèmes complexes

#### Exemple Type Serious Game
- Mission type SQL :
  - Le joueur doit sélectionner tous les archers vétérans parmi les soldats :
    1. Observer les différents types de soldats disponibles
    2. Écrire la requête SQL appropriée
    3. Voir les soldats se regrouper selon la requête
- Objectif de gameplay : Comprendre visuellement l'impact de chaque mot-clé SQL
- Feedback :
  - Visualisation immédiate du résultat
  - Messages d'aide en cas d'erreur
  - Suggestions d'amélioration pour optimiser la requête
  - 

## Module 5: Narration et Contexte

### 5.1 Synopsis
- Contexte général :
  - Le joueur entre dans une académie d'apprentissage où les concepts abstraits prennent vie visuellement
  - Mission : Maîtriser progressivement les concepts en interagissant avec leurs représentations visuelles
- Contexte spécifique :
  - Pour SQL : Une armée où chaque soldat représente une donnée à manipuler
  - Pour les mathématiques : Un laboratoire où les équations sont des balances à équilibrer

### 5.2 Personnages
- Éléments visuels principaux :
  - SQL : Différents types de soldats (archers, vétérans, etc.) représentant les données
  - Mathématiques : Objets physiques représentant les variables et constantes
- Éléments d'interface :
  - Assistant visuel : Guide les utilisateurs dans la compréhension des concepts
  - Indicateurs de réussite : Montrent la progression et la validation des exercices

### 5.3 Univers
- Ambiance visuelle :
  - Style graphique : 2D avec animations fluides
  - Interface divisée en deux zones principales :
    - Zone supérieure : visualisation des soldats et leurs mouvements
    - Zone inférieure : saisie des commandes SQL
  - Représentations visuelles des commandes SQL :
    - GROUP BY : Regroupement physique des soldats par type
    - INSERT : Arrivée de nouvelles recrues dans l'armée
    - DELETE : Départ des soldats retraités
    - UPDATE : Changement d'équipement ou de rang des soldats
  - Animations spécifiques pour chaque type d'opération
- Retours sonores :
  - Sons de validation pour les commandes réussies
  - Indications sonores pour les erreurs de syntaxe
  - Effets sonores légers pour les mouvements de troupes

### 5.4 Progression Narrationnelle
- Introduction :
  - Tutoriel présentant les bases de chaque domaine (SQL ou mathématiques)
  - Premiers exercices guidés pour familiariser l'utilisateur
- Progression par thèmes :
  - SQL : Des requêtes simples aux jointures complexes
  - Mathématiques : Des équations basiques aux systèmes d'équations
- Accomplissements :
  - Déblocage progressif de nouveaux concepts
  - Validation des compétences acquises

#### Exemple Type Serious Game
- Scénario SQL :
  - Début : Introduction aux commandes SELECT simples avec un petit groupe de soldats
  - Progression : Ajout de conditions WHERE, GROUP BY avec des groupes plus larges
  - Maîtrise : Manipulation de plusieurs groupes avec des jointures
- Objectif : Comprendre visuellement l'impact de chaque commande SQL
- Feedback :
  - Visualisation immédiate des résultats
  - Suggestions d'optimisation des requêtes


## Module 6: Contenus et Ressources

### 6.1 Compétences à Mobiliser
- Compétences techniques :
  - Compréhension des concepts SQL de base
  - Maîtrise de la syntaxe des requêtes
  - Capacité à visualiser les opérations sur les données
- Compétences cognitives :
  - Logique et raisonnement
  - Capacité d'abstraction
  - Résolution de problèmes

### 6.2 Contenus Pédagogiques
- Supports intégrés :
  - Fiches explicatives pour chaque commande SQL
  - Exemples animés montrant l'effet des requêtes
  - Guide des meilleures pratiques SQL
- Exercices interactifs :
  - Challenges progressifs par niveau de difficulté
  - Quiz sur la syntaxe et l'utilisation des commandes
- Documentation accessible :
  - Aide contextuelle pendant les exercices
  - Bibliothèque de requêtes types avec explications

### 6.3 Assets Nécessaires
- Graphismes 2D :
  - Sprites des différents types de soldats
  - Éléments d'interface utilisateur
  - Animations pour les mouvements et regroupements
- Sons (minimalistes, non essentiels au gameplay) :
  - Simple retour sonore désactivable pour les validations/erreurs
  - Aucun son d'ambiance
  - Application parfaitement utilisable sans son
- Animations :
  - Mouvements des soldats (marche, regroupement)
  - Effets visuels pour les opérations SQL
  - Transitions entre les états de données

### 6.4 Intégration Pédagogique
- Tutoriels progressifs :
  - Introduction aux concepts de base
  - Guide pas à pas pour les premières requêtes
  - Exercices guidés avec feedback immédiat
- Suivi des progrès :
  - Tableau de bord des compétences acquises
  - Historique des requêtes réalisées
  - Statistiques de progression

#### Exemple Type Serious Game
- Mission Exemple :
  - Situation : Gestion d'une nouvelle recrue dans l'armée
  - Tâches :
    1. Écrire une requête INSERT pour ajouter le soldat
    2. Utiliser SELECT pour vérifier l'ajout
    3. Modifier ses caractéristiques avec UPDATE
  - Ressources nécessaires :
    - Éditeur de requêtes SQL
    - Visualisation en temps réel des changements
    - Aide contextuelle sur la syntaxe
- Feedback donné :
  - Visualisation immédiate des modifications
  - Messages d'erreur explicatifs
  - Suggestions d'optimisation

### 6.5 Technologies Utilisées
- Moteur de jeu : Unity 2D pour une performance optimale sur mobile
- Outils principaux :
  - Interface de développement Visual Studio/VSCode
  - Système de gestion de versions Git
- Outils tiers :
  - Bibliothèque d'animations 2D pour Unity
  - Sons minimalistes pré-enregistrés (optionnels)
  - Système de feedback visuel en temps réel
- Technologies potentielles futures :
  - IA pour la génération procédurale de niveaux et exercices
  - Système d'analyse des requêtes SQL pour adaptation du contenu
  - Générateur automatique de variations d'exercices


## Module 7: Technologie et Plateformes

### 7.1 Moteur de Jeu
- Choix : Unity 2D
  - Raison :
    - Performance optimale pour les animations 2D
    - Excellente compatibilité multiplateforme
    - Outils adaptés pour l'interface utilisateur et les animations
    - Gestion efficace des entrées tactiles

### 7.2 Plateformes Cibles
- Mobile (iOS et Android) :
  - Plateforme principale pour l'apprentissage en mobilité
  - Interface optimisée pour écrans tactiles
  - Application légère et performante
- Web (via WebGL) :
  - Version accessible depuis n'importe quel navigateur
  - Pas d'installation requise
  - Synchronisation de la progression entre plateformes
- PC/Mac :
  - Version desktop complète
  - Support clavier/souris
  - Idéal pour les sessions longues

### 7.3 Langages et Frameworks
- Langage principal : C# (Unity)
- Frameworks supplémentaires :
  - DOTween : Pour des animations fluides
  - TextMeshPro : Pour le rendu optimal du texte
  - SQLite : Pour la gestion locale des données

### 7.4 Intégrations Spécifiques
- API :
  - Système de sauvegarde cloud pour la progression
  - Synchronisation entre appareils
- Modules d'IA (futurs) :
  - Génération procédurale d'exercices
  - Adaptation du niveau de difficulté
  - Système de suggestions personnalisées

### 7.5 Performance et Optimisation
- Optimisation mobile :
  - Atlas de sprites optimisés
  - Gestion efficace de la mémoire
  - Temps de chargement minimaux
- Multiplateforme :
  - Interface adaptative selon la taille d'écran
  - Tests sur différents appareils et navigateurs
  - Support offline complet

### 7.6 Outils Supplémentaires
- Gestion de projet :
  - GitHub pour le versioning
  - Trello pour le suivi des tâches
- Design :
  - Adobe Illustrator pour les assets 2D
  - Aseprite pour les animations
  - Figma pour le design d'interface

#### Exemple Type Serious Game
- Scénario Technique :
  - Un étudiant pratique des requêtes SQL sur son téléphone pendant son trajet. L'application fonctionne hors-ligne et synchronise sa progression quand la connexion est rétablie
  - Plateforme cible : Application mobile native
  - Performance : Interface réactive et temps de réponse immédiat pour le feedback visuel des requêtes

  
## Module 8: Système de Feedback

### 8.1 Feedback Immédiat
- Indicateurs Visuels :
  - Animations des soldats réagissant aux commandes SQL
  - Surbrillance des éléments affectés par la requête
  - Indicateurs de syntaxe (vert pour correct, rouge pour erreur)
- Retours Sonores (optionnels) :
  - Son minimal de validation pour les requêtes correctes
  - Son d'erreur discret pour les syntaxes incorrectes
- Contextualisation :
  - Messages explicatifs des erreurs de syntaxe
  - Suggestions de correction en temps réel
  - Visualisation des effets de chaque clause SQL

### 8.2 Feedback Différé
- Rapports d'Exercices :
  - Résumé des concepts pratiqués :
    - Types de requêtes utilisées
    - Taux de réussite par type de commande
    - Temps moyen par exercice
  - Statistiques de progression
- Analyse des Erreurs :
  - Compilation des erreurs fréquentes
  - Suggestions de révision des concepts mal maîtrisés
  - Exemple : "Le GROUP BY est souvent mal placé dans vos requêtes"

### 8.3 Système de Progression
- Scores Cumulés :
  - Niveaux de maîtrise par concept SQL :
  - Niveau 1 : SELECT simple et WHERE basique
    - Sélectionner tous les archers
    - Filtrer les soldats par type
  - Niveau 2 : GROUP BY et fonctions d'agrégation
    - Compter le nombre de soldats par type
    - Calculer la moyenne d'âge par unité
  - Niveau 3 : JOIN et sous-requêtes simples
    - Associer les soldats à leurs équipements
    - Trouver les vétérans dans chaque unité
  - Niveau 4 : Requêtes complexes
    - Jointures multiples entre armées
    - Sous-requêtes corrélées
  - Niveau 5 : Optimisation et cas avancés
    - Optimisation des requêtes
    - Gestion des cas particuliers (NULL, etc.)

- Badges de Progression :
  - "Recruteur Junior" : Maîtrise des INSERT basiques
  - "Maître du SELECT" : Expert en requêtes de sélection
  - "Stratège des JOIN" : Excellence dans les jointures
  - "Guru du GROUP BY" : Maîtrise des regroupements
  - "Commandant des Requêtes" : Maîtrise des requêtes complexes
  - "Oracle de l'Optimisation" : Excellence en optimisation
  - "Légendaire du SQL" : Tous les concepts maîtrisés
- Système de Suivi :
  - Progression personnelle visible
  - Comparaison optionnelle avec la moyenne des utilisateurs

### 8.4 Outils de Suivi et d'Évaluation
- Tableaux de Bord :
  - Vue d'ensemble des concepts maîtrisés
  - Statistiques détaillées :
    - Temps passé par concept
    - Taux de réussite par type de requête
    - Points de blocage identifiés
- Exports :
  - Export des requêtes créées
  - Historique d'apprentissage téléchargeable

### 8.5 Feedback Adaptatif
- Système d'Adaptation :
  - Ajustement de la difficulté selon les performances
  - Génération d'exercices ciblant les faiblesses
- Révision Intelligente :
  - Rappel des concepts prérequis si nécessaire
  - Suggestions d'exercices de renforcement

#### Exemples Types Serious Game
- Mission Niveau 1 : "Les Recrues"
  - Objectif : SELECT et WHERE simples
  - Tâche : Sélectionner tous les archers avec plus de 5 ans d'expérience
  - Feedback : Visualisation des soldats sélectionnés se mettant en avant

- Mission Niveau 2 : "L'Organisation"
  - Objectif : GROUP BY et agrégations
  - Tâche : Regrouper les soldats par type et calculer la force moyenne de chaque groupe
  - Feedback : Formations de groupes avec affichage des statistiques

- Mission Niveau 3 : "L'Équipement"
  - Objectif : JOIN simple
  - Tâche : Associer chaque soldat à son équipement
  - Feedback : Visualisation des liens entre soldats et équipements

- Mission Niveau 4 : "Le Commandement"
  - Objectif : Jointures multiples et sous-requêtes
  - Tâche : Trouver les capitaines dont tous les soldats sont des vétérans
  - Feedback : Mise en évidence des hiérarchies et relations complexes

- Mission Niveau 5 : "L'Élite"
  - Objectif : Optimisation et cas complexes
  - Tâche : Requête optimisée pour trouver les meilleures unités selon plusieurs critères
  - Feedback : Comparaison des performances entre différentes approches

# Serious Game Design Document

## Module 9: Contraintes et Faisabilité

### 9.1 Durée de Développement
- Estimation globale : 2 mois minimum
- Approche DevOps :
  1. Sprint initial (2 semaines) :
  - Setup du projet Unity
  - Mise en place CI/CD
  - Tests unitaires framework
  2. MVP (3 semaines) :
  - Fonctionnalités SQL de base (SELECT, WHERE)
  - Interface basique
  - Assets graphiques simples depuis Unity Asset Store
  3. Itérations (3 semaines) :
  - Tests utilisateurs
  - Ajout fonctionnalités SQL avancées
  - Optimisation mobile
- Développement continu post-lancement :
  - Nouvelles fonctionnalités
  - Contenu additionnel
  - Optimisations basées sur les retours

### 9.2 Budget Estimé
- Coûts principaux :
  - Développement :
    - 1 développeur Unity/C#
    - Assets Unity Store
    - Estimation : 10 000 à 15 000 €
  - Outils et licences :
    - Unity Personal (gratuit initialement)
    - Assets graphiques prêts à l'emploi
    - Estimation : 1 000 €
  - Tests :
    - Tests automatisés
    - Beta testing
    - Estimation : 500 €
- Budget total initial : 11 500 à 16 500 €

### 9.3 Ressources Nécessaires
- Équipe minimale :
  - 1 développeur Unity/C#
  - Support ponctuel expert SQL
- Matériel :
  - PC développement
  - Devices test basiques
- Tests :
  - Framework tests unitaires
  - Pipeline CI/CD
  - Tests automatisés

### 9.4 Contraintes Techniques
- Base de données :
  - SQLite pour stockage local
  - Système de synchronisation simple
- Assets :
  - Utilisation d'assets préfabriqués
  - Animations simples et optimisées
- Tests :
  - Tests unitaires pour chaque fonctionnalité
  - Tests d'intégration automatisés
  - Tests de performance mobile

### 9.5 Risques Identifiés
- Techniques :
  - Complexité des animations pour certaines requêtes SQL
  - Performance sur anciens appareils
- Pédagogiques :
  - Clarté des visualisations
  - Courbe d'apprentissage
- Solutions :
  - Tests précoces des concepts clés
  - Feedback utilisateur régulier

### 9.6 Opportunités de Partenariats
- Établissements d'enseignement :
  - Écoles d'informatique
  - Centres de formation professionnelle
- Entreprises :
  - Départements formation
  - Services IT

## Module 10: Plan de Lancement et Évaluation

### 10.1 Stratégie de Lancement
- Phase Pilote :
  - Test avec 2-3 établissements partenaires
  - Retours des professeurs et étudiants
  - Ajustements avant lancement commercial
- Lancement Commercial :
  - Démarchage établissements d'enseignement
  - Présence sur les stores (iOS/Android)
  - Communication ciblée réseaux enseignement

### 10.2 Support Utilisateur
- Documentation Pédagogique :
  - Guide pour enseignants
  - Tutoriels intégrés pour étudiants
  - Exercices types et corrections
- Support Technique :
  - Email support prioritaire écoles
  - FAQ et guides de dépannage
  - Documentation technique

### 10.3 Évaluation
- Métriques Techniques :
  - Stabilité de l'application
  - Performance sur différents devices
  - Taux de bugs critiques
- Métriques Pédagogiques :
  - Progression des étudiants
  - Taux de réussite par concept
  - Temps moyen d'apprentissage

### 10.4 Évolution
- Phase 1 (MVP) :
  - Concepts SQL fondamentaux
  - Interface intuitive
  - Système de suivi basique
- Phase 2 :
  - SQL avancé
  - Statistiques pour enseignants
  - Plus d'exercices pratiques
- Phase 3 :
  - Générateur d'exercices
  - Outils de suivi avancés
  - Nouveaux domaines potentiels

### 10.5 Modèle Économique
- Tarification :
  - Application : 4.99€ (prix unique)
  - Licence établissement :
    - 20 étudiants : 79€/an
    - 50 étudiants : 149€/an
    - 100+ étudiants : sur devis
- Avantages Licence :
  - Suivi des étudiants
  - Support prioritaire
  - Mises à jour gratuites
  - Outils enseignants

#### Scénario Type
- Lancement Initial :
  - Phase 1 : Test gratuit 2 mois avec 3 écoles partenaires
  - Phase 2 : Lancement stores à 4.99€
  - Phase 3 : Introduction licences établissements
- Objectifs Année 1 :
  - 2000 utilisateurs individuels
  - 10 établissements sous licence
  - Note stores > 4.5/5