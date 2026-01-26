1️⃣ What is OOP (Programmation Orientée Objet)

La POO est une manière de programmer en organisant le code autour d’objets plutôt que de simples fonctions.
Un objet regroupe :

des données (attributs)

des comportements (méthodes)

Objectifs principaux :

mieux structurer le code

le rendre réutilisable

plus facile à maintenir
-------------------------------------------

2️⃣ “first-class everything”

En Python, tout est un objet :

fonctions

classes

modules

types de base (int, str, list…)

👉 Cela signifie qu’on peut :

les stocker dans des variables

les passer en paramètres

les retourner depuis une fonction
-------------------------------------------

3️⃣ Une classe est un modèle (plan) qui définit :

les attributs

les méthodes

Elle décrit comment créer des objets.

class Person:
    pass
-------------------------------------------

4️⃣ What is an object and an instance

Un objet (ou instance) est une création concrète d’une classe.

p1 = Person()


👉 p1 est une instance de la classe Person
-------------------------------------------

5️⃣ Difference between a class and an object/instance
| Classe     | Objet                |
| ---------- | -------------------- |
| Modèle     | Réalisation concrète |
| Définition | Utilisation          |
| Une seule  | Plusieurs possibles  |
-------------------------------------------

6️⃣ What is an attribute

Un attribut est une variable appartenant à un objet ou à une classe.

p1.name = "Alice"


Ici, name est un attribut de l’objet p1.
-------------------------------------------

7️⃣ Public, protected et private attributes

En Python, c’est une convention, pas une vraie restriction.

| Type      | Syntaxe  | Signification           |
| --------- | -------- | ----------------------- |
| Public    | `name`   | Accessible partout      |
| Protected | `_name`  | Usage interne conseillé |
| Private   | `__name` | Name mangling           |

-------------------------------------------

8️⃣ What is self

self représente l’instance courante de la classe.

class Person:
    def say_hi(self):
        print("Hi")


👉 self permet d’accéder aux attributs et méthodes de l’objet.
-------------------------------------------

9️⃣ What is a method

Une méthode est une fonction définie dans une classe.

def greet(self):
    print("Hello")


Elle agit sur l’objet via self.
-------------------------------------------

🔟 The special __init__ method

__init__ est appelé automatiquement lors de la création d’un objet.

class Person:
    def __init__(self, name):
        self.name = name


👉 Il sert à initialiser les attributs.
-------------------------------------------

1️⃣1️⃣ Data Abstraction, Encapsulation & Information Hiding

Abstraction : montrer l’essentiel, cacher la complexité

Encapsulation : regrouper données + méthodes

Information Hiding : empêcher l’accès direct à certaines données

👉 Objectif : sécurité et lisibilité du code
-------------------------------------------

1️⃣2️⃣ What is a property

Une property permet d’accéder à une méthode comme si c’était un attribut.

@property
def age(self):
    return self._age
-------------------------------------------

1️⃣3️⃣ Attribute vs Property
| Attribut        | Property                    |
| --------------- | --------------------------- |
| Variable simple | Méthode déguisée            |
| Accès direct    | Peut contenir de la logique |
| Pas de contrôle | Validation possible         |
-------------------------------------------

1️⃣4️⃣ Pythonic way to write getters and setters

👉 Ne PAS écrire get_x() / set_x()

Utiliser @property :

@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value < 0:
        raise ValueError
    self._age = value
-------------------------------------------

1️⃣5️⃣ Dynamically create new attributes

En Python, on peut ajouter un attribut à la volée :

p1.city = "Paris"


👉 Cet attribut n’existe que pour p1.
-------------------------------------------

1️⃣6️⃣ Bind attributes to objects and classes

Attribut d’objet → spécifique à une instance

Attribut de classe → partagé

class A:
    x = 10  # attribut de classe

a = A()
a.y = 5   # attribut d’instance
-------------------------------------------

1️⃣7️⃣ What is __dict__

__dict__ est un dictionnaire interne qui contient les attributs.

p1.__dict__


👉 Montre toutes les données stockées dans l’objet ou la classe.
-------------------------------------------

1️⃣8️⃣ How Python finds attributes (ordre de recherche)

Python cherche dans cet ordre :

Instance (obj.__dict__)

Classe

Classes parentes (MRO)

👉 C’est le Method Resolution Order (MRO).
-------------------------------------------

1️⃣9️⃣ How to use getattr

getattr permet d’accéder dynamiquement à un attribut.

getattr(p1, "name")


Avec valeur par défaut :

getattr(p1, "age", 0)
