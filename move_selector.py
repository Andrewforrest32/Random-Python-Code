import random as R

def calculate_dmg(pokemon_level,attack_stat,defence_stat,move,move_dmg):
    dmg_max = int((2*pokemon_level/5+2)*attack_stat/defence_stat*move_dmg/50+2)
    dmg_min = int(dmg_max*0.85)
    dmg = R.randint(dmg_min,dmg_max)
    return dmg
    
def move_selector(hp,damages,moves):
    lethal_dmg_indices = []
    for dmg in damages:
        if dmg >= hp:
            lethal_dmg_indices.append(damages.index(dmg))
            
    lethal_moves = []
    for lethal_index in lethal_dmg_indices:
        lethal_moves.append(moves[lethal_index])
        
    if len(lethal_moves) != 0:
        move_chosen = R.choice(lethal_moves)
    else:
        move_chosen = moves[damages.index(max(damages))]
    return move_chosen

moves_dmg = {"Lick":30,"Bite":60,"Psychic":90}
moves = list(moves_dmg.keys())
pokemon_level = 5
attack_stat = 10
defence_stat = 10
hp = 10

damages = []

for move in moves:
    dmg = calculate_dmg(pokemon_level,attack_stat,defence_stat,move,moves_dmg[move])
    damages.append(dmg)
    
move_chosen = move_selector(hp,damages,moves)
print(f"Chosen move: {move_chosen}")
