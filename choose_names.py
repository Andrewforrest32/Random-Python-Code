import random as R

def choose_name(names, amount):
    if amount == 1:
        names_chosen = R.choice(names)
    elif amount > 1:
        names_chosen = R.sample(names, amount)
    return names_chosen

default_names = ['Ewan', 'Catherine', 'Nick', 'Amanda', 'Chloe', 'Kendra', 'Julie']
print(f"Default names are {default_names}")

choice = input("Choose an option (1 for default names, 2 to input your own): ")

if choice == "1":
    names = default_names
else:
    inputted_names = input("Enter the names of everyone, separated by commas: ")
    names = inputted_names.split(',')
    names = [name.strip() for name in names]

amount = int(input("How many people are being chosen: "))
names_chosen = choose_name(names, amount)
print(f"The name(s) chosen are {names_chosen}")
