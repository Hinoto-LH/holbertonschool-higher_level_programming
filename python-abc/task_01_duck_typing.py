#!/usr/bin/env python3
"""
Script qui crée des instances de Circle et Rectangle
et affiche leur aire et périmètre en utilisant shape_info.
"""

from task_01_duck_typing import Circle, Rectangle, shape_info

# Création des instances
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

# Affichage des informations sur les formes
shape_info(circle)
shape_info(rectangle)
