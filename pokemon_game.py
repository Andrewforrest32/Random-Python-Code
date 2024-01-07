import random as R

def select_move_user(user_choice, stats, counter_user):
    if stats["Growth_user"] == True:
        counter_user +=1
    if counter_user == 3:
        stats["Growth_user"] = False
        counter_user = 0
            
    if user_choice == 1 or user_choice == 2:
        if user_choice == 1:
            if accuracy_check(80) == False:
                print("Your move failed.")
            else:
                stats = attack_user(user_choice, stats)
        elif user_choice == 2:
            if accuracy_check(95) == False:
                print("Your move failed.")
            else:
                stats = attack_user(user_choice, stats)
        stats["Defend_user"] = False
    elif user_choice == 3:
        stats["Defend_user"] = False
        stats = growth_user(stats)
    return stats, counter_user

def select_move_bot(user_choice, stats, counter_bot):
    if user_choice == 4:
        stats = defend_user(stats)
        
    if stats["Growth_bot"] == True:
        counter_bot +=1
    if counter_bot == 3:
        stats["Growth_bot"] = False
        counter_bot = 0
        
    if stats["HP_user"] == 1:
        action_bot = 2
    elif stats["HP_user"] == 2:
        action_bot = 1
    elif stats["Defend_bot"] == True:
        action_bot = R.randint(1,3)
        stats["Defend_bot"] = False
    elif stats["Growth_bot"] == True:
        action_bot = R.choice([1,2,4])
        stats["Defend_bot"] = False
    else:
        action_bot = R.randint(1,4)
        stats["Defend_bot"] = False
        
    if action_bot == 1 or action_bot == 2:
        stats = attack_bot(action_bot, stats)
    elif action_bot == 3:
        stats = growth_bot(stats)
    else:
        stats = defend_bot(stats)
    return action_bot, stats, counter_bot

def turn_order(action_bot, action_user):
    order = []
    if (action_user == 2 and action_bot == 2) or (action_user != 2 and action_bot != 2):
        temp = R.randint(1,2)
        if temp == 1:
            order.append("User")
            order.append("Bot")
        else:
            order.append("Bot")
            order.append("User")
    elif action_user == 2:
        order.append("User")
        order.append("Bot")
    elif action_bot == 2:
        order.append("Bot")
        order.append("User")
    return order

def defend_user(stats):
    if stats["Defend_user"] == True:
        print("Protect failed!")
        stats["Defend_user"] = False
    else:
        stats["Defend_user"] = True
        print("You chose to protect!")
    return stats

def defend_bot(stats):
    print("Bot chose to defend.")
    stats["Defend_bot"] = True
    return stats

def growth_user(stats):
    print("You grew stronger for two turns!")
    stats["Growth_user"] = True
    return stats

def growth_bot(stats):
    print("Bot grew stronger for two turns")
    stats["Growth_bot"] = True
    return stats
    
def accuracy_check(move_accuracy):
    chance = R.randint(1,100)
    if chance < move_accuracy:
        return True
    else:
        return False

def attack_user(user_choice, stats):
    if stats["Defend_bot"] == True:
            print("The bot defended against your attack!")
    elif user_choice == 1 and stats["Growth_user"] == True:
        stats["HP_bot"] = stats["HP_bot"] - 3
        print("You did 3 damage!")
    elif user_choice == 1:
        print("You did 2 damage!")
        stats["HP_bot"] = stats["HP_bot"] - 2
    elif user_choice == 2 and stats["Growth_user"] == True:
        print("You did 2 damage!")
        stats["HP_bot"] = stats["HP_bot"] - 2
    else:
        print("You did 1 damage!")
        stats["HP_bot"] = stats["HP_bot"] - 1
    return stats

def attack_bot(bot_choice, stats):
    if stats["Defend_user"] == True:
        print("The user defended against your attack!")
    elif bot_choice == 1:
        if stats["Growth_bot"] == True:
            print("Bot did 3 damage")
            stats["HP_user"] = stats["HP_user"] - 3
        else:
            print("Bot did 2 damage")
            stats["HP_user"] = stats["HP_user"] - 2
    elif bot_choice == 2:
        if stats["Growth_bot"] == True:
            print("Bot did 2 damage")
            stats["HP_user"] = stats["HP_user"] - 2
        else:
            print("Bot did 1 damage")
            stats["HP_user"] = stats["HP_user"] - 1
    return stats

def check_winner(order, stats):
    current_HP_bot = stats["HP_bot"]
    current_HP_user = stats["HP_user"]
    winner_found = False
    
    if current_HP_bot <= 0:
        if current_HP_user <= 0:
            if order[0] == "User":
                print("You win!")
                winner_found = True
            else:
                print("Sorry, you lost.")
                winner_found = True
        else:
            print("You win!")
            winner_found = True
    elif current_HP_user <= 0:
        print("Sorry, you lost.")
        winner_found = True
    else:
        print(f"Bot's HP: {current_HP_bot} User's HP: {current_HP_user}")
    return winner_found

print("Let's play a basic turn-based attacking game!")
print("We both start off with 10 HP and have the same four moves.")
print("Who goes first is chosen at random, except if only one side picks Quick Attack.")
print("Using Growth last for two turns and can only be used once.")
print("You can't use defend two turns in a row.")

stats = {
    "HP_bot":10,"HP_user":10,
    "Growth_bot":False,"Growth_user":False,
    "Defend_bot":False,"Defend_user":False}

moves_options = {
        1:"Scratch: Do two damage (Accuracy: 80%)",
        2:"Quick Attack: Do one damage (priority +1, Accuracy: 95%)",
        3:"Growth: Raise attack by 1",
        4:"Defend: Prevent the next instant of damage"}
        
counter_user = 0
counter_bot = 0
        
while True:
    print(moves_options)
    while True:
        action_user = int(input("Pick a move (based on the number): "))
        if action_user not in [1,2,3,4]:
            print("Invalid move choice, pick again.")
        else:
            break
    
    action_bot, stats, counter_bot = select_move_bot(action_user, stats, counter_bot)
    stats, counter_user = select_move_user(action_user, stats, counter_user)
    order = turn_order(action_bot, action_user)
        
    winner_found = check_winner(order, stats)
    if winner_found == True:
        break