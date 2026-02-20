#!/usr/bin/python3
from warrior import Warrior
from mage import Mage
from enemy import Enemy

arthur = Warrior("Arthur", 100, 10)
merlin = Mage("Merlin", 80, 30)
goblin = Enemy("Goblin", 50, 8)

characters = [arthur, merlin, goblin]

# Test du polymorphisme
for char in characters:
    print(f"{char._name} attacks with {char.attack()} damage")

print("----- Combat -----")

# Arthur attaque le Goblin
damage = arthur.attack()
goblin.take_damage(damage)

# Goblin contre-attaque
damage = goblin.attack()
arthur.take_damage(damage)

print(f"Arthur alive: {arthur.is_alive()}")
print(f"Goblin alive: {goblin.is_alive()}")
