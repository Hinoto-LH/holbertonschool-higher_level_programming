#!/usr/bin/python3
# La ligne ci-dessus indique quel interpréteur Python utiliser (utile sous Linux)

def read_file(filename=""):
    """
    Cette fonction lit le contenu d'un fichier texte
    et affiche son contenu à l'écran.
    """

    # Ouverture du fichier en mode lecture ("r")
    # Le fichier sera automatiquement fermé à la fin du bloc 'with'
    with open("python-input_output/tests/my_file_0.txt", "r") as f:

        # Lecture de tout le contenu du fichier
        filename = f.read()

        # Affichage du contenu du fichier
        print(filename)
