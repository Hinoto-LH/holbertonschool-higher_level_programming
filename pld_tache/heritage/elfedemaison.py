from creature import Creature

class ElfeDeMaison(Creature):
    """Classe pour les créatures Elfes de maison"""

    def __init__(self, nom, maitre, loyaute, magie_domestique):
        super().__init__()
        self.nom = nom
        self.maitre = maitre
        self.loyaute = loyaute
        self.magie_domestique = magie_domestique

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nom': self.nom,
            'maitre': self.maitre,
            'loyaute': self.loyaute,
            'magie_domestique': self.magie_domestique
        })
        return data
