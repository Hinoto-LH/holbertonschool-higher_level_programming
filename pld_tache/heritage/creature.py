from datetime import datetime
import uuid


class Creature:
    """Classe mère pour toutes les créatures magiques"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            'type': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
