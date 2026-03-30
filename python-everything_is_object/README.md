# Concepts Fondamentaux : Objets et Gestion de la Memoire en Python

Ce document regroupe les notions essentielles pour comprendre comment Python manipule les donnees, les objets et les variables.

## 1. Objets et Classes

* **Qu'est-ce qu'un objet ?**
  En Python, tout est objet. Un objet est une entitée qui contient des donnees (attributs) et des fonctionnalites (methodes). Chaque objet a trois caracteristiques : une identite (son adresse memoire), un type et une valeur.

* **Classe vs Objet (ou Instance)**
  - La **Classe** est le plan de construction (le moule). Par exemple, la classe "Chien".
  - L'**Objet** (ou Instance) est la realisation concrete. Par exemple, "Rex" est une instance specifique de la classe "Chien".

## 2. Mutabilite : Mutable vs Immutable

* **Definition**
  - **Mutable** : Un objet dont on peut modifier le contenu apres sa creation sans changer son identite (adresse memoire).
  - **Immutable** : Un objet dont le contenu ne peut pas etre change. Toute modification entraine la creation d'un nouvel objet.

* **Types Intregres Immutables**
  - Nombres (int, float, complex)
  - Chaines de caracteres (str)
  - Tuples (tuple)
  - Booleens (bool)
  - Gel de zones memoire (frozenset)

* **Types Integres Mutables**
  - Listes (list)
  - Dictionnaires (dict)
  - Ensembles (set)
  - Tableaux d'octets (bytearray)

## 3. Variables et References

* **Qu'est-ce qu'une reference ?**
  Une reference est l'adresse memoire d'un objet. En Python, une variable n'est pas une "boite" qui contient la valeur, mais une "etiquette" (un nom) qui pointe vers un objet en memoire.

* **Qu'est-ce qu'une affectation (Assignment) ?**
  C'est l'action de lier un nom (variable) a un objet. Exemple : `a = [1, 2]` lie le nom `a` a l'objet liste cree en memoire.

* **Qu'est-ce qu'un alias ?**
  Un alias survient lorsque deux variables pointent vers le meme objet. Exemple : `b = a`. Toute modification d'un objet mutable via `a` sera visible via `b`.

## 4. Identite et Comparaison

* **Savoir si deux variables sont identiques (Lien vers le meme objet)**
  On utilise l'operateur `is`. Il compare les adresses memoire (l'identite).
  ```python
  a is b  # True si a et b pointent vers le meme objet
  ```
