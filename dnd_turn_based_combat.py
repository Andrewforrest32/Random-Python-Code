import random as R

def bot_spell_choice(stats, spells):
    spell_options = list(spells.keys())
    if stats["Bot"]["HP"] <= 2:
        spell_options.remove("Sacrifice Health")
    for spell in spell_options:
        if check_spell_validity(spell, "Bot", stats, spells) == False:
            spell_options.remove(spell)
    bot_spell = R.choice(spell_options)
    return bot_spell
    
def check_spell_validity(spell_choice, side, stats, spells):
    if spell_choice == "Fireball" or spell_choice == "Firebolt" or spell_choice == "Cure Wounds":
        if stats[side]["Mana"] >= -1*spells[spell_choice]["Mana"]:
            validity = True
        else:
            validity = False
    else:
        validity = True
    return validity

def stats_change(side, HP_change, Mana_change, stats):
    stats[side]["HP"] = stats[side]["HP"]+HP_change
    if stats[side]["HP"] > 10:
        stats[side]["HP"] = 10
    stats[side]["Mana"] = stats[side]["Mana"]+Mana_change
    if stats[side]["Mana"] > 10:
        stats[side]["Mana"] = 10
    return stats
    
def use_spell(spell_choice, side, spells, stats):
    if check_spell_validity(spell_choice, side, stats, spells):
        HP_change = spells[spell_choice]["HP"]
        Mana_change = spells[spell_choice]["Mana"]
    
        if spell_choice == "Fireball" or spell_choice == "Firebolt":
            stats = stats_change(side, 0, Mana_change, stats)
            if side == "User":
                stats = stats_change("Bot",HP_change, 0, stats)
            else:
                stats = stats_change("User",HP_change, 0, stats)
        else:
            stats = stats_change(side, HP_change, Mana_change, stats)
        
        print(f"{side} used the spell {spell_choice}")
    else:
        print(f"Sorry {side}, invalid move.")
    
    return stats
    
def check_win(stats):
    if stats["Bot"]["HP"] <= 0:
        return True
    elif stats["User"]["HP"] <= 0:
        return True
    else:
        return False

stats = {
    "Bot":{"HP":10,"Mana":10},
    "User":{"HP":10,"Mana":10}}
    
spells = {
    "Fireball": {"HP": -4,"Mana": -4},
    "Firebolt": {"HP": -2,"Mana":-2},
    "Cure Wounds": {"HP": 3,"Mana": -2},
    "Sacrifice Health": {"HP": -2,"Mana": 3},
    "Recover": {"HP": 1, "Mana": 1}}
    
while True:
    
    for spell in spells:
        print(f"{spell}: {spells[spell]}")
        if spell == "Fireball" or spell == "Firebolt":
            print("This damages the opposing side.")
        else:
            print("This only affects the casting side.")

    bot_spell = bot_spell_choice(stats, spells)
    stats = use_spell(bot_spell, "Bot", spells, stats)
    print(stats)
    if check_win(stats):
        print("Sorry, you lost.")
        break
    
    user_spell = input("Pick a spell to use: ")
    stats = use_spell(user_spell, "User", spells, stats)
    print(stats)
    if check_win(stats):
        print("Congratulations, you win!")
        break
