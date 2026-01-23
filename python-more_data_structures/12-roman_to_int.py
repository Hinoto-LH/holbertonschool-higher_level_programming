#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    # isinstance permet de verifier un type
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev = 0

    for char in roman_string:
        value = rom[char]  # conversion de symbole en entier
        if value > prev:
            total += value - 2 * prev
        else:
            total += value
        prev = value

    return total
