# Les Créatures Magiques de Poudlard - Exercice Python sur l'Héritage et les Fichiers

## Présentation de l'exercice

Cet exercice pratique vous permet d'explorer et de maîtriser les concepts avancés de la programmation orientée objet en Python à travers la création d'un système de gestion de créatures magiques inspirées de l'univers de Harry Potter. Vous allez concevoir un système complet utilisant l'héritage, la lecture de fichiers CSV et la sérialisation JSON pour créer une base de données de créatures fantastiques.

## Structure de l'exercice

L'exercice est organisé autour de la création d'un système hiérarchique de classes avec les éléments suivants:

1. **Classe mère `Creature`**
   - Attributs communs (ID unique, timestamps de création et modification)
   - Utilisation des modules `uuid` et `datetime` pour la gestion des identifiants
   - Méthode de sérialisation `to_dict()` pour la conversion JSON

2. **Classes filles spécialisées**
   - **Centaure** : Attributs de force, agilité, nom et âge
   - **Acromentule** : Caractéristiques de taille, type de venin, nombre de pattes et territoire
   - **Détraqueur** : Puissance d'aspiration, lieu de garde et niveau de dangerosité
   - **Dragon** : Type de dragon, type de souffle, trésor gardé et âge
   - **Elfe de maison** : Maître servi, niveau de loyauté et capacités magiques domestiques

3. **Traitement de données**
   - Lecture et parsing de fichier CSV avec le module `csv`
   - Instanciation dynamique d'objets selon le type de créature
   - Gestion d'erreurs pour la robustesse du programme

4. **Sérialisation et persistance**
   - Conversion des objets en format JSON
   - Sauvegarde avec les IDs comme clés principales
   - Structure de données optimisée pour la recherche

## Concepts de programmation abordés

- **Héritage en Python** : Classe mère et classes filles
- **Polymorphisme** : Méthodes communes avec implémentations spécifiques
- **Encapsulation** : Organisation des données et méthodes
- **Modules Python** : `csv`, `json`, `uuid`, `datetime`
- **Gestion de fichiers** : Lecture CSV et écriture JSON
- **Traitement d'erreurs** : `try`/`except` pour la robustesse
- **Sérialisation de données** : Conversion objet vers JSON
- **Identifiants uniques** : Génération d'UUID pour les clés primaires

## Architecture du projet

```
projet/
├── creatures.csv          # Données source des créatures
├── creature.py          # Définition de la classe parente
├── dragon.py            # Définition de la classe dragon
├── centaure.py          # Définition de la classe centaure
├── acromentule.py       # Définition de la classe acromentule
├── detraqueur.py        # Définition de la classe detraqueur
├── elfedemaison.py      # Définition de la classe elfedemaison
├── main.py              # Programme principal
└── data.json           # Fichier de sortie généré
```

## Exemple d'utilisation

Le programme lit automatiquement le fichier `creatures.csv`, crée les objets appropriés (Centaures, Dragons, etc.) et génère un fichier `data.json` structuré avec des identifiants uniques comme clés. Chaque créature conserve ses attributs spécifiques tout en héritant des propriétés communes de la classe `Creature`.

## Données fournies

Le fichier CSV inclut 10 créatures variées :
- 2 Centaures (Firenze et Bane)
- 2 Acromentules (Aragog et Mosag)
- 2 Détraqueurs (gardiens d'Azkaban)
- 2 Dragons (Norbert et Horntail)
- 2 Elfes de maison (Dobby et Kreattur)

## Ressources supplémentaires

- [Documentation Python officielle sur l'héritage](https://docs.python.org/fr/3/tutorial/classes.html#inheritance)
- [Guide sur le module CSV](https://docs.python.org/fr/3/library/csv.html)
- [Documentation du module JSON](https://docs.python.org/fr/3/library/json.html)
- [Real Python - Héritage et composition](https://realpython.com/inheritance-composition-python/)
- [Module UUID pour les identifiants uniques](https://docs.python.org/fr/3/library/uuid.html)
- [Module datetime pour la gestion du temps](https://docs.python.org/fr/3/library/datetime.html)
- [Bonnes pratiques pour la sérialisation JSON](https://realpython.com/working-with-json-data-in-python/)
