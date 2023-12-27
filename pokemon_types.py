import random as R

def type_matchup(type1, type2):
    type_matches = {
    'Normal': [[], ['Rock', 'Steel'], ['Ghost']],
    'Fire': [['Grass', 'Ice', 'Bug', 'Steel'], ['Fire', 'Water', 'Rock', 'Dragon'], []],
    'Water': [['Fire', 'Ground', 'Rock'], ['Water', 'Grass', 'Dragon'], []],
    'Electric': [['Water', 'Flying'], ['Electric', 'Ground'], []],
    'Grass': [['Water', 'Ground', 'Rock'], ['Fire', 'Grass', 'Poison', 'Flying', 'Bug'], []],
    'Ice': [['Grass', 'Ground', 'Flying', 'Dragon'], ['Fire', 'Water', 'Ice', 'Steel'], []],
    'Fighting': [['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy'], []],
    'Poison': [['Grass', 'Fairy'], ['Poison', 'Ground', 'Rock', 'Ghost'], []],
    'Ground': [['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], ['Grass', 'Ice', 'Water'], ['Flying']],
    'Flying': [['Grass', 'Fighting', 'Bug'], ['Electric', 'Rock', 'Steel'], ['Ground']],
    'Psychic': [['Fighting', 'Poison'], ['Psychic', 'Steel'], ['Dark']],
    'Bug': [['Grass', 'Psychic', 'Dark'], ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy'], []],
    'Rock': [['Fire', 'Ice', 'Flying', 'Bug'], ['Fighting', 'Ground', 'Steel'], []],
    'Ghost': [['Psychic', 'Ghost'], ['Dark'], ['Normal']],
    'Dragon': [['Dragon'], ['Steel'], []],
    'Dark': [['Psychic', 'Ghost'], ['Fighting', 'Dark', 'Fairy'], []],
    'Steel': [['Ice', 'Rock', 'Fairy'], ['Fire', 'Water', 'Electric', 'Steel'], []],
    'Fairy': [['Fighting', 'Dragon', 'Dark'], ['Poison', 'Steel'], []]
    }

    attacking_type_matches = type_matches.get(type1)  # Use .get to handle potential KeyError

    if not attacking_type_matches:  # Check for None due to .get
        return 1

    if type2 in attacking_type_matches[0]:
        damage_multiplier = 2
    elif type2 in attacking_type_matches[1]:
        damage_multiplier = 0.5
    elif type2 in attacking_type_matches[2]:
        damage_multiplier = 0  # Immune case
    else:
        damage_multiplier = 1

    return damage_multiplier
    
def read_types():
    
    all_types = [
    'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison',
    'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'
    ]
    print(all_types)
    
    attacking_type = input("Enter the type of your pokemon: ")
    defending_type = input("Enter the type of the opposing pokemon: ")
    
    return attacking_type, defending_type
    
print("Let's calculate some match ups!")

attacking_type, defending_type = read_types()
damage_multiplier = type_matchup(attacking_type, defending_type)
print(f"Your {attacking_type} pokemon will do {damage_multiplier}x damage")