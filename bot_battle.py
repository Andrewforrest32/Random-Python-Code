import random as R
import sys

def user_move(move_options,move_choices,stats):
    while True:
        move_user = input("Pick a move: ")
        if move_user not in move_options:
            print("Invalid choice")
        elif validate_move(move_user, "User", stats) == False:
            print("Not enough mana")
        else:
            move_choices["User Move"] = move_user
            break
    return move_choices
    
def validate_move(move, side, stats):
    current_mana = stats[side]["Mana"]
    if move == "Fireball" and current_mana < 5:
        move_validated = False
    elif move == "Protect" and current_mana < 2:
        move_validated = False
    else:
        move_validated = True
    return move_validated
    
def enact_moves(move_choices,stats, moves):
    if move_choices["Bot Move"] == "Sword Attack":
        if move_choices["User Move"] == "Protect":
            print("You protected against the Bot's Sword Attack!")
            stats["User"]["Mana"] += moves["Protect"]["Mana"]
        else:
            print("The bot hit you with its sword.")
            stats["User"]["HP"] += moves["Sword Attack"]["HP"]
    elif move_choices["Bot Move"] == "Fireball":
        if move_choices["User Move"] == "Protect":
            print("You protected against the Bot's Fireball!")
            stats["User"]["Mana"] += moves["Protect"]["Mana"]
        else:
            print("The bot hit you with a fireball.")
            stats["User"]["HP"] += moves["Fireball"]["HP"]
            stats["Bot"]["Mana"] += moves["Fireball"]["Mana"]
    elif move_choices["Bot Move"] == "Recover":
        print("The bot recovered some health and mana.")
        stats["Bot"]["HP"] += moves["Recover"]["HP"]
        stats["Bot"]["Mana"] += moves["Recover"]["Mana"]

    if move_choices["User Move"] == "Sword Attack":
        if move_choices["Bot Move"] == "Protect":
            print("The bot protected against your Sword Attack!")
            stats["Bot"]["Mana"] += moves["Protect"]["Mana"]
        else:
            print("You hit the bot with your sword.")
            stats["Bot"]["HP"] += moves["Sword Attack"]["HP"]
    elif move_choices["User Move"] == "Fireball":
        if move_choices["Bot Move"] == "Protect":
            print("The bot protected against your Fireball!")
            stats["Bot"]["Mana"] += moves["Protect"]["Mana"]
        else:
            print("You hit the bot with a fireball.")
            stats["Bot"]["HP"] += moves["Fireball"]["HP"]
            stats["User"]["Mana"] += moves["Fireball"]["Mana"]
    elif move_choices["User Move"] == "Recover":
        print("You recovered some health and mana.")
        stats["User"]["HP"] += moves["Recover"]["HP"]
        stats["User"]["Mana"] += moves["Recover"]["Mana"]
        
    if move_choices["User Move"] == "Protect" and move_choices["Bot Move"] == "Protect":
        print("Both sides protected, no change!")
        stats["User"]["Mana"] += moves["Protect"]["Mana"]
        stats["Bot"]["Mana"] += moves["Protect"]["Mana"]
    return stats
    
def check_win(stats):
    side_won = ''
    for side in stats:
        if stats[side]["HP"] <= 0:
            side_won = side
    return side_won

def easy_bot(stats):
    move_options = ["Sword Attack","Sword Attack","Fireball","Protect","Recover"]
    move_bot = R.choice(move_options)
    while validate_move(move_bot,"Bot",stats) == False:
        move_bot = R.choice(move_options)
    return move_bot, stats

def med_bot(stats):
    move_options = ["Sword Attack","Sword Attack","Fireball","Fireball","Protect","Recover"]
    if stats["User"]["HP"] <= 2:
        move_bot = "Sword Attack"
    elif stats["User"]["HP"] <= 5:
        move_bot = "Fireball"
    else:
        move_bot = R.choice(move_options)
    while validate_move(move_bot,"Bot",stats) == False:
        move_bot = R.choice(move_options)
    return move_bot, stats

def hard_bot(stats):
    move_options = ["Sword Attack","Sword Attack","Fireball","Fireball","Protect","Recover"]
    if stats["User"]["HP"] <= 2:
        move_bot = "Sword Attack"
    elif stats["User"]["HP"] <= 5 and stats["Bot"]["Mana"] >= 5:
        move_bot = "Fireball"
    elif stats["Bot"]["Mana"] <= 2 or stats["Bot"]["HP"] <= 2:
        move_bot = "Recover"
    else:
        move_bot = R.choice(move_options)
    while validate_move(move_bot,"Bot",stats) == False:
        move_bot = R.choice(move_options)
    return move_bot, stats

Bot = {"HP":10,"Mana":10}
User = {"HP":10,"Mana":10}
stats = {"Bot":Bot,"User":User}
moves = {
    "Sword Attack":{"HP":-2},"Fireball":{"HP":-4,"Mana":-5},
    "Recover":{"HP":3,"Mana":3}, "Protect":{"Mana":-2}}
move_options = list(moves.keys())
turn_counter = 0

print("Welcome to Bot Battle! Defeat 3 increasingly difficult Bots to win!")
print("Every round starts with both sides at 10 health and 10 mana.")
print(f"The following moves are available: {move_options}")
print("Sword Attack does 2 damage to opposing side.")
print("Fireball does 4 damage to opposide side but uses up 5 mana.")
print("Recover heals the user for 3 health and 3 mana.")
print("Protect negates any incoming damage from the opposing side.")

print("Welcome to Round 1! You have 6 turns to defeat the bot.")
while True:
    if turn_counter == 6:
        print("Sorry, you ran out of turns.")
        sys.exit()
    move_choices = {}
    print(move_options)
    move_choices = user_move(move_options,move_choices,stats)
    move_bot, stats = easy_bot(stats)
    move_choices["Bot Move"] = move_bot
    stats = enact_moves(move_choices,stats,moves)
    print(stats)
    turn_counter += 1
    side_won = check_win(stats)
    if side_won != '':
        print("Sorry, the bot beat you.")
        sys.exit()
        
turn_counter = 0
Bot = {"HP":10,"Mana":10} 
User = {"HP":10,"Mana":10}
stats = {"Bot":Bot,"User":User}
print("Congrats on making it to Round 2! You now have 5 turns to defeat the bot.")
while True:
    if turn_counter == 5:
        print("Sorry, you ran out of turns.")
        sys.exit()
    move_choices = {}
    print(move_options)
    move_choices = user_move(move_options,move_choices,stats)
    move_bot, stats = med_bot_bot(stats, move_options)
    move_choices["Bot Move"] = move_bot
    stats = enact_moves(move_choices,stats,moves)
    print(stats)
    turn_counter += 1
    side_won = check_win(stats)
    if side_won != '':
        print("Sorry, the bot beat you.")
        sys.exit()
    
turn_counter = 0
Bot = {"HP":10,"Mana":10} 
User = {"HP":10,"Mana":10}
stats = {"Bot":Bot,"User":User}
print("Congrats on making it to the final round! You have 5 turns to defeat the bot.")
while True:
    if turn_counter == 5:
        print("Sorry, you ran out of turns.")
        sys.exit()
    move_choices = {}
    print(move_options)
    move_choices = user_move(move_options,move_choices,stats)
    move_bot, stats = hard_bot(stats, move_options)
    move_choices["Bot Move"] = move_bot
    stats = enact_moves(move_choices,stats,moves)
    print(stats)
    turn_counter += 1
    side_won = check_win(stats)
    if side_won != '':
        print("Sorry, the bot beat you.")
        sys.exit()
