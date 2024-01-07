import random as R

def spell_damage(spell_choice, spells):
    max_damage = spells[spell_choice]["Damage Amount"]["Dice Sides"]
    damage = R.randint(1,max_damage)
    return damage

def print_spells(spells):
    for spell in spells:
        spell_damage_type = spells[spell]["Damage Type"]
        spell_damage_amount = spells[spell]["Damage Amount"]["Quantity"]
        spell_damage_dice = spells[spell]["Damage Amount"]["Dice Sides"]
        print(f"{spell}'s damage is {spell_damage_amount}d{spell_damage_dice} {spell_damage_type}")

Firebolt = {"Damage Amount":{"Quantity":1,"Dice Sides":10},"Damage Type":"Fire"}
RayOfFrost = {"Damage Amount":{"Quantity":1,"Dice Sides":8},"Damage Type":"Cold"}
EldritchBlast = {"Damage Amount":{"Quantity":1,"Dice Sides":10},"Damage Type":"Force"}
ChillTouch = {"Damage Amount":{"Quantity":1,"Dice Sides":8},"Damage Type":"Necrotic"}
LightningLure = {"Damage Amount":{"Quantity":1,"Dice Sides":8},"Damage Type":"Lightning"}
MindSliver = {"Damage Amount":{"Quantity":1,"Dice Sides":6},"Damage Type":"Psychic"}
SacredFlame = {"Damage Amount":{"Quantity":1,"Dice Sides":8},"Damage Type":"Radiant"}
Infestation = {"Damage Amount":{"Quantity":1,"Dice Sides":6},"Damage Type":"Poison"}

spells = {
    "Firebolt":Firebolt,
    "Ray of Frost":RayOfFrost,
    "Eldritch Blast":EldritchBlast,
    "Chill Touch":ChillTouch,
    "Lightning Lure":LightningLure,
    "Mind Sliver":MindSliver,
    "Sacred Flame":SacredFlame,
    "Infestation":Infestation}
    
print_spells(spells)
spell_names = list(spells.keys())
while True:
    print(spell_names)
    spell_choice = input("Which spell do you want to cast: ")
    damage_done = spell_damage(spell_choice, spells)
    spell_choice_damage_type = spells[spell_choice]["Damage Type"]
    print(f"You casted {spell_choice} which did {damage_done} {spell_choice_damage_type} damage.")
