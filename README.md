# Mini-Paint en Python (Pygame)

Ce projet est un logiciel de dessin minimaliste et performant réalisé avec **Pygame**. Il permet de dessiner à main levée, de gérer des palettes de couleurs via des raccourcis clavier et d'exporter ses créations.

##  Fonctionnalités implémentées

- **Dessin dynamique** : Utilisation des coordonnées de la souris pour générer des tracés fluides.
- **Raccourcis clavier intelligents** : 
  - Changement de couleur instantané (`N` pour Noir, `R` pour Rouge, `V` pour Vert, `B` pour Bleu, `J` pour Jaune).
  - Gestion de l'épaisseur du trait (`P` pour augmenter, `M` pour diminuer).
- **Exportation** : Sauvegarde de la création au format `.png` à la racine du projet avec la touche `S` ainsi qu'une entrée console pour le nom.
- **Contrôles de sécurité** : Empêche l'épaisseur du trait de descendre en dessous de 1.

##  Concepts techniques utilisés

En analysant le code, j'ai mis en pratique plusieurs notions clés de programmation :
- **Structures de données** : Utilisation d'un dictionnaire pour mapper les noms des couleurs aux objets `pygame.Color`.
- **Gestion des événements** : Capture et traitement des événements `MOUSEMOTION` et `KEYDOWN`.
- **Interpolation de tracé** : Calcul de lignes entre deux positions successives (`debut_ligne` et `fin_ligne`) pour assurer un dessin continu même lors de mouvements rapides de la souris.
- **Interaction avec le système de fichiers** : Utilisation de `pygame.image.save` pour la persistance des données.

##  Utilisation

1. Installez Pygame : `pip install pygame`
2. Lancez le script : `python logiciel.py`
3. Utilisez les touches clavier pour changer de style et la souris pour dessiner !
