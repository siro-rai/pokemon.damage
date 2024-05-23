# damage_calculator.py_ver2

def calculate_damage(level, power, attack, defense, stab, type_effectiveness, critical):
    """
    Calculate the damage dealt by a Pokémon move.

    Parameters:
    level (int): Level of the attacking Pokémon
    power (int): Base power of the move
    attack (int): Attack stat of the attacking Pokémon
    defense (int): Defense stat of the defending Pokémon
    stab (float): Same-Type Attack Bonus (1.5 if same type, 1 otherwise)
    type_effectiveness (float): Effectiveness of the move (2.0 for super effective, 0.5 for not very effective, etc.)
    critical (float): Critical hit modifier (1.5 if critical hit, 1 otherwise)

    Returns:
    int: Damage dealt
    """
    modifier = stab * type_effectiveness * critical
    damage = (((2 * level / 5 + 2) * power * attack / defense) / 50 + 2) * modifier
    return int(damage)

# Example usage
if __name__ == "__main__":
    level = int(input("Enter attacking Pokémon's level: "))
    power = int(input("Enter move's base power: "))
    attack = int(input("Enter attacking Pokémon's attack stat: "))
    defense = int(input("Enter defending Pokémon's defense stat: "))
    stab = float(input("Enter STAB (1.5 if same type, otherwise 1): "))
    type_effectiveness = float(input("Enter type effectiveness (2.0 for super effective, 0.5 for not very effective, etc.): "))
    critical = float(input("Enter critical hit modifier (1.5 if critical hit, otherwise 1): "))

    damage = calculate_damage(level, power, attack, defense, stab, type_effectiveness, critical)
    print(f"Damage dealt: {damage}")

