#!/usr/bin/python3
"""
Module qui définit la classe VerboseList,
une liste qui affiche un message à chaque modification.
"""


class VerboseList(list):
    """
    Liste qui affiche des messages lorsqu'elle est modifiée.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste
        et affiche un message.

        Args:
            item: élément à ajouter
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste avec un itérable et affiche un message
        indiquant le nombre d'éléments ajoutés.

        Args:
            iterable: itérable d'éléments à ajouter
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Supprime un élément de la liste et affiche un message.

        Args:
            item: élément à supprimer
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne un élément à l'index donné
        et affiche un message.

        Args:
            index (int): index de l'élément à retirer (par défaut -1)

        Returns:
            l'élément retiré
        """
        value = super().pop(index)
        print(f"Popped [{value}] from the list.")
        return value
