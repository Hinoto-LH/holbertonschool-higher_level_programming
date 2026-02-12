import csv
import json

# Import des classes
from centaure import Centaure
from acromentule import Acromentule
from detraqueur import Detraqueur
from dragon import Dragon
from elfedemaison import ElfeDeMaison


def lire_csv(nom_fichier):
    """Lit le fichier CSV et retourne les données"""
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            return list(lecteur)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []


def creer_creature(type_creature, donnees):
    """Crée une instance de créature selon son type"""
    try:
        if type_creature == "Centaure":
            return Centaure(
                nom=donnees['nom'],
                force=donnees['attribut1'],
                agilite=donnees['attribut2'],
                age=donnees['attribut4']
            )
        elif type_creature == "Acromentule":
            return Acromentule(
                nom=donnees['nom'],
                taille=donnees['attribut1'],
                venin=donnees['attribut2'],
                nombre_pattes=donnees['attribut3'],
                territoire=donnees['attribut4']
            )
        elif type_creature == "Détraqueur":
            return Detraqueur(
                nom=donnees['nom'],
                puissance_aspiration=donnees['attribut1'],
                lieu_garde=donnees['attribut2'],
                dangerosite=donnees['attribut3']
            )
        elif type_creature == "Dragon":
            return Dragon(
                nom=donnees['nom'],
                type_dragon=donnees['attribut1'],
                souffle=donnees['attribut2'],
                tresor=donnees['attribut3'],
                age=donnees['attribut4']
            )
        elif type_creature == "Elfe de maison":
            return ElfeDeMaison(
                nom=donnees['nom'],
                maitre=donnees['attribut1'],
                loyaute=donnees['attribut2'],
                magie_domestique=donnees['attribut3']
            )
        else:
            print(f"Type de créature inconnu : {type_creature}")
            return None
    except Exception as e:
        print(
            f"Erreur lors de la création de la créature {type_creature} : {e}")
        return None


def sauvegarder_json(creatures, nom_fichier):
    """Sauvegarde les créatures dans un fichier JSON"""
    try:
        # Convertir les objets en dictionnaire avec l'ID comme clé
        donnees_json = {}
        for creature in creatures:
            if creature is not None:
                creature_dict = creature.to_dict()
                donnees_json[creature.id] = creature_dict

        # Sauvegarder dans le fichier JSON
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees_json, fichier, indent=2, ensure_ascii=False)

        print(f"Données sauvegardées avec succès dans {nom_fichier}")
        print(f"Nombre de créatures sauvegardées : {len(donnees_json)}")

    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def main():
    """Fonction principale"""
    print("=== Gestionnaire de Créatures Magiques ===")

    # 1. Lire le fichier CSV
    print("Lecture du fichier creatures.csv...")
    donnees_csv = lire_csv('creatures.csv')
    print(donnees_csv)

    if not donnees_csv:
        print("Aucune donnée à traiter.")
        return

    # 2. Créer les objets créatures
    print("Création des objets créatures...")
    creatures = []

    for ligne in donnees_csv:
        type_creature = ligne['type']
        creature = creer_creature(type_creature, ligne)
        if creature:
            creatures.append(creature)
            print(f"✓ {type_creature} '{ligne['nom']}' créé avec l'ID : {creature.id}")

    # 3. Sauvegarder en JSON
    print("\nSauvegarde dans data.json...")
    sauvegarder_json(creatures, 'data.json')

    print("\n=== Traitement terminé ===")


if __name__ == "__main__":
    main()
