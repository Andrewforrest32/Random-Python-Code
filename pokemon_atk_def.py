import random as R

def print_pokemons(pokemons):
    for pokemon in pokemons:
        print(pokemon)
        hp = pokemons[pokemon]["HP"]
        print(f"HP: {hp}")
        attack = pokemons[pokemon]["Attack"]
        print(f"Attack: {attack}")
        defence = pokemons[pokemon]["Defence"]
        print(f"Defence: {defence}")
        print("Moves")
        for move in pokemons[pokemon]["Moves"]:
            move_dmg = pokemons[pokemon]["Moves"][move]
            print(f"{move} has {move_dmg} attack power.")
    print("Explosion also KO's the pokemon that uses it.")

def display_hp(sides,bot_pokemon,user_pokemon):
    bot_hp = sides["Bot"][bot_pokemon]["HP"]
    print(f"The bot's {bot_pokemon}'s HP: {bot_hp}")
    user_hp = sides["User"][user_pokemon]["HP"]
    print(f"Your {user_pokemon}'s HP: {user_hp}")

def check_explosion(sides,pokemon):
    choose_explosion = False
    if sides["Bot"][pokemon]["HP"] <= 5 and sides["Bot"]["Single pokemon"] == False:
        choose_explosion = True
    return choose_explosion

def pokemon_selector(pokemons):
    names = pokemons.keys()
    pokemon_bot = R.sample(names,2)
    pokemon_user = R.sample(names,2)
    return pokemon_bot, pokemon_user
    
def get_pokemon(name):
    if pokemon == "Squirtle":
        return squirtle
    elif pokemon == "Bidoof":
        return bidoof
    else:
        return starly
        
def calculate_dmg(sides,attacking_side,defending_side,attacking_pokemon,defending_pokemon,move):
    pokemon_level = 5
    attack_stat = sides[attacking_side][attacking_pokemon]["Attack"]
    defence_stat = sides[defending_side][defending_pokemon]["Defence"]
    move_dmg = sides[attacking_side][attacking_pokemon]["Moves"][move]
    dmg_max = int((2*pokemon_level/5+2)*attack_stat/defence_stat*move_dmg/50+2)
    dmg_min = int(dmg_max*0.85)
    dmg = R.randint(dmg_min,dmg_max)
    print(f"{move} did {dmg} damage")
    return dmg

def update_hp(sides,defending_side,defending_pokemon,dmg,bot_pokemon):
    pokemon_died = False
    bot_pokemon_chosen = defending_pokemon
    sides[defending_side][defending_pokemon]["HP"] = sides[defending_side][defending_pokemon]["HP"] - dmg
    if sides[defending_side][defending_pokemon]["HP"] < 0:
        sides[defending_side][defending_pokemon]["HP"] = 0
        pokemon_died = True
        if bot_pokemon_chosen == bot_pokemon[1]:
            sides[defending_side]["Both down"] = True
            return sides, bot_pokemon_chosen
        else:
            bot_pokemon_chosen = bot_pokemon[1]
        sides[defending_side]["Single pokemon"] = pokemon_died
    return sides, bot_pokemon_chosen
    
def bot_move_selector(sides,bot_current_pokemon,bot_current_moves):
    if check_explosion(sides,bot_current_pokemon):
        move_chosen = "Explosion"
    else:
        move_chosen = bot_current_moves[0]
    return move_chosen
    
squirtle = {"HP":20,"Attack":10,"Defence":10,"Moves":{"Bubble":45,"Explosion":70}}
bidoof = {"HP":18,"Attack":10,"Defence":12,"Moves":{"Tackle":35,"Explosion":70}}
starly = {"HP":18,"Attack":12,"Defence":10,"Moves":{"Peck":40,"Explosion":70}}
pokemons = {"Squirtle":squirtle,"Bidoof":bidoof,"Starly":starly}

bot_pokemon_chosen, user_pokemon_chosen = pokemon_selector(pokemons)
bot = {"Single pokemon":False,"Both down":False}
user = {"Single pokemon":False,"Both down":False}

for pokemon in bot_pokemon_chosen:
    bot[pokemon] = get_pokemon(pokemon)
for pokemon in user_pokemon_chosen:
    user[pokemon] = get_pokemon(pokemon)

sides = {"Bot":bot,"User":user}

#Introduction
print("Welcome to pokemon showdon!")
print(f"2 of the following pokemon are randomly chosen for both sides: {list(pokemons.keys())}")

print(f"The bot will be starting with {bot_pokemon_chosen[0]} and {bot_pokemon_chosen[1]}")
print(f"You will be starting with {user_pokemon_chosen[0]} and {user_pokemon_chosen[1]}")

#Display pokemon stats and moves
print_pokemons(pokemons)

#Start game
print("You will be starting!")
user_current_pokemon = user_pokemon_chosen[0]
bot_current_pokemon = bot_pokemon_chosen[0]
print(f"You send out {user_current_pokemon}")
print(f"The bot sends out {bot_current_pokemon}")
user_current_pokemon_moves = list(pokemons[user_current_pokemon]["Moves"])
bot_current_pokemon_moves = list(pokemons[bot_current_pokemon]["Moves"])

while True:
    display_hp(sides,bot_current_pokemon,user_current_pokemon)
    print("Your turn!")
    while True:
        print(f"Your available moves are {user_current_pokemon_moves}")
        user_move_choice = input("Pick a move: ")
        if user_move_choice not in user_current_pokemon_moves:
            print("Invalid move choice")
        else:
            break
    user_move_dmg = pokemons[user_current_pokemon]["Moves"][user_move_choice]
    user_move_actual_dmg = calculate_dmg(sides,"User","Bot",user_current_pokemon,bot_current_pokemon,user_move_choice)
    sides,bot_current_pokemon = update_hp(sides,"Bot",bot_current_pokemon,user_move_actual_dmg,bot_pokemon_chosen)
    if sides["Bot"]["Both down"] == True:
        print("You win!")
        break
    print("Bot's turn!")
    bot_move_choice = bot_move_selector(sides,bot_current_pokemon,bot_current_pokemon_moves)
    bot_move_actual_dmg = calculate_dmg(sides,"Bot","User",bot_current_pokemon,user_current_pokemon,bot_move_choice)
    sides,user_current_pokemon = update_hp(sides,"User",user_current_pokemon,bot_move_actual_dmg,user_pokemon_chosen)
    if sides["User"]["Both down"] == True:
        print("Sorry, you lost.")
        break