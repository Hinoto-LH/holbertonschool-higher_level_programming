1️⃣ Superclass / base class / parent class

👉 C’est la classe “mère”, celle dont une autre classe hérite.

class Animal:
    def speak(self):
        print("Je fais un bruit")


Ici, Animal est :

une superclass

une base class

une parent class

👉 Ces trois termes veulent dire exactement la même chose.

2️⃣ Subclass (classe enfant)

👉 C’est la classe qui hérite d’une autre

class Dog(Animal):
    pass

Dog est une subclass

Elle hérite de Animal

3️⃣ Lister tous les attributs et méthodes d’une classe ou instance
🔹 dir()
dir(Animal)
dir(my_dog)


➡️ Liste tout (y compris ce qui est hérité ou interne)

🔹 __dict__
Animal.__dict__
my_dog.__dict__


➡️ Montre seulement ce qui est défini directement

4️⃣ Quand une instance peut avoir de nouveaux attributs

👉 À tout moment, tant que la classe n’utilise pas __slots__

dog = Dog()
dog.name = "Rex"
dog.age = 3


➡️ Ces attributs n’existent que pour cette instance

⚠️ Mauvaise pratique en général (ça rend le code moins clair)

5️⃣ Hériter d’une classe

Syntaxe :

class Child(Parent):
    pass


Exemple :

class Cat(Animal):
    def speak(self):
        print("Miaou")

6️⃣ Classe avec plusieurs classes de base (héritage multiple)
class Flyable:
    def fly(self):
        print("Je vole")

class Bird(Animal, Flyable):
    pass


➡️ Bird hérite de Animal ET Flyable

⚠️ À utiliser avec modération (peut devenir complexe)

7️⃣ Classe par défaut dont toutes les classes héritent

👉 object

class MyClass:
    pass


Équivaut à :

class MyClass(object):
    pass


➡️ Toutes les classes Python héritent de object

8️⃣ Redéfinir (override) une méthode ou un attribut
🔹 Override d’une méthode
class Dog(Animal):
    def speak(self):
        print("Wouf")


➡️ La méthode de Animal est remplacée

🔹 Appeler la version du parent
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Wouf")

9️⃣ Ce qui est hérité par les subclasses

Une subclass hérite :

✅ méthodes

✅ attributs de classe

✅ méthodes spéciales (__str__, __init__, etc.)

❌ Pas :

attributs d’instance créés dans __init__ si le parent n’est pas appelé

class Animal:
    def __init__(self):
        self.alive = True

class Dog(Animal):
    def __init__(self):
        pass  # alive n'existe pas !


✔️ Correct :

class Dog(Animal):
    def __init__(self):
        super().__init__()

🔟 À quoi sert l’héritage

👉 Réutiliser du code
👉 Organiser les concepts
👉 Polymorphisme (même méthode, comportement différent)

animals = [Dog(), Cat()]
for a in animals:
    a.speak()

🔟 À quoi sert l’héritage

👉 Réutiliser du code
👉 Organiser les concepts
👉 Polymorphisme (même méthode, comportement différent)

animals = [Dog(), Cat()]
for a in animals:
    a.speak()

1️⃣1️⃣ Fonctions built-in importantes
🔹 isinstance(obj, Class)

➡️ Vérifie si un objet est une instance ou d’une sous-classe

isinstance(dog, Dog)      # True
isinstance(dog, Animal)   # True


✅ À utiliser très souvent

1️⃣1️⃣ Fonctions built-in importantes
🔹 isinstance(obj, Class)

➡️ Vérifie si un objet est une instance ou d’une sous-classe

isinstance(dog, Dog)      # True
isinstance(dog, Animal)   # True


✅ À utiliser très souvent

🔹 issubclass(A, B)

➡️ Vérifie si A hérite de B

issubclass(Dog, Animal)   # True

🔹 type()

➡️ Donne la classe exacte

type(dog) == Dog


⚠️ Moins flexible que isinstance

🔹 super()

➡️ Accéder à la classe parente

super().method()


Utilisé surtout dans :

__init__

override de méthodes

| Concept    | À retenir           |
| ---------- | ------------------- |
| superclass | classe parent       |
| subclass   | classe enfant       |
| héritage   | partage de code     |
| object     | parent de tout      |
| override   | remplacer           |
| super()    | appeler le parent   |
| isinstance | vérifier un objet   |
| issubclass | vérifier une classe |
