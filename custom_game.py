import random as R

def print_moves(moves):
    for move in moves:
        print(move)
        for side in moves[move]:
            print(f"{side}: {moves[move][side]}")

def move_validation(stats,side,move):
    move_valid = True
    if move == "Strike":
        if stats[side]["Energy"] < 15:
            move_valid = False
    elif move == "Cast":
        if stats[side]["Mana"] < 15:
            move_valid = False
    elif move == "Recover":
        if stats[side]["HP"] == 100 and stats[side]["Mana"] == 50 and stats[side]["Energy"] == 50:
            move_valid = False
    return move_valid

def move_selector(stats,side,move):
    if move == "Recover":
        stats = recover_move(stats,side)
    elif move == "Strike":
        stats = strike_move(stats,side)
    else:
        stats = cast_move(stats,side)
    print(f"{side} used {move}")
    return stats

def bot_move_selector(stats,moves):
    while True:
        bot_move = R.choice(moves)
        if move_validation(stats,"Bot",bot_move):
            stats = move_selector(stats,"Bot",bot_move)
            break
    return stats
    
def check_win(stats):
    game_won = False
    if stats["Player"]["HP"] <= 0:
        print("Sorry, you lost.")
        game_won = True
    elif stats["Bot"]["HP"] <= 0:
        print("Congrats, you won!")
        game_won = True
    return game_won

def recover_move(stats,side):
    stats[side]["HP"] += 20
    if stats[side]["HP"] > 100:
        stats[side]["HP"] = 100
    stats[side]["Mana"] += 15
    if stats[side]["Mana"] > 50:
        stats[side]["Mana"] = 50
    stats[side]["Energy"] += 15
    if stats[side]["Energy"] > 50:
        stats[side]["Energy"] = 50
    return stats

def strike_move(stats,side):
    stats[side]["Energy"] -= 15
    other_side = "Player" if side=="Bot" else "Bot"
    stats[other_side]["HP"] -= 20
    return stats

def cast_move(stats,side):
    stats[side]["Mana"] -= 15
    other_side = "Player" if side=="Bot" else "Bot" 
    stats[other_side]["HP"] -= 20
    return stats
    
def end_turn_regen(stats):
    sides = ["Player","Bot"]
    for side in sides:
        if stats[side]["Mana"] < 50:
            stats[side]["Mana"] += 5
            print(f"{side} recovered 5 Mana")
        if stats[side]["Energy"] < 50:
            stats[side]["Energy"] += 5
            print(f"{side} recovered 5 Energy")
    return stats

player = {"HP":100,"Mana":50,"Energy":50}
bot = {"HP":100,"Mana":50,"Energy":50}
stats = {"Player":player,"Bot":bot}

recover = {"User":{"HP":20,"Mana":15,"Energy":15}}
strike = {"User":{"Energy":-15},"Other Side":{"HP":-20}}
cast = {"User":{"Mana":-15},"Other Side":{"HP":-20}}

moves = {"Recover":recover,"Strike":strike,"Cast":cast}
moves_names = list(moves.keys())

print_moves(moves)

while True:
    while True:
        print(moves_names)
        move_choice = input("Pick a move: ")
        if move_choice not in moves_names or move_validation(stats,"Player",move_choice) == False:
            print("Invalid move choice")
        else:
            break
        
    stats = move_selector(stats,"Player",move_choice)
    print(stats)
    if check_win(stats):
        break
    
    stats = bot_move_selector(stats,moves_names)
    print(stats)
    if check_win(stats):
        break
    
    stats = end_turn_regen(stats)