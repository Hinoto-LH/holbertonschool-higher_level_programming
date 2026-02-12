from creature import Creature

class Dragon(Creature):
    """Classe pour les créatures Dragons"""

    def __init__(self, nom, type_dragon, souffle, tresor, age):
        super().__init__()
        self.nom = nom
        self.type_dragon = type_dragon
        self.souffle = souffle
        self.tresor = tresor
        self.age = int(age)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nom': self.nom,
            'type_dragon': self.type_dragon,
            'souffle': self.souffle,
            'tresor': self.tresor,
            'age': self.age
        })
        return data
