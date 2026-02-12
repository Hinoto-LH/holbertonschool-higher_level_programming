from creature import Creature

class Detraqueur(Creature):
    """Classe pour les créatures Détraqueurs"""

    def __init__(self, nom, puissance_aspiration, lieu_garde, dangerosite):
        super().__init__()
        self.nom = nom
        self.puissance_aspiration = puissance_aspiration
        self.lieu_garde = lieu_garde
        self.dangerosite = dangerosite

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nom': self.nom,
            'puissance_aspiration': self.puissance_aspiration,
            'lieu_garde': self.lieu_garde,
            'dangerosite': self.dangerosite
        })
        return data
