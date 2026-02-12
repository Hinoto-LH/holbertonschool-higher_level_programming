from creature import Creature

class Centaure(Creature):
    """Classe pour les créatures Centaures"""

    def __init__(self, nom, force, agilite, age):
        super().__init__()
        self.nom = nom
        self.force = int(force)
        self.agilite = int(agilite)
        self.age = int(age)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nom': self.nom,
            'force': self.force,
            'agilite': self.agilite,
            'age': self.age
        })
        return data
