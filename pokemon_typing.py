import random as R

def type_matchup(attacking_types, defending_types):
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

    damage_multiplier = 1

    for type1 in attacking_types:
        for type2 in defending_types:
            attacking_type_matches = type_matches.get(type1)  # Use .get to handle potential KeyError

            if attacking_type_matches:
                if type2 in attacking_type_matches[0]:
                    damage_multiplier *= 2
                elif type2 in attacking_type_matches[1]:
                    damage_multiplier *= 0.5
                elif type2 in attacking_type_matches[2]:
                    damage_multiplier *= 0  # Immune case

    return damage_multiplier

def read_types():
    all_types = [
    'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison',
    'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'
    ]
    print(all_types)
    
    attacking_types = input("Enter the types of your pokemon (comma-separated): ").split(',')
    defending_types = input("Enter the types of the opposing pokemon (comma-separated): ").split(',')
    
    return attacking_types, defending_types
    
print("Let's calculate some match ups!")

attacking_types, defending_types = read_types()
damage_multiplier = type_matchup(attacking_types, defending_types)
print(f"Your {', '.join(attacking_types)} pokemon will do {damage_multiplier}x damage")
