from creature import Creature


class Acromentule(Creature):
    """Classe pour les créatures Acromentules"""

    def __init__(self, nom, taille, venin, nombre_pattes, territoire):
        super().__init__()
        self.nom = nom
        self.taille = taille
        self.venin = venin
        self.nombre_pattes = int(nombre_pattes)
        self.territoire = territoire

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nom': self.nom,
            'taille': self.taille,
            'venin': self.venin,
            'nombre_pattes': self.nombre_pattes,
            'territoire': self.territoire
        })
        return data
