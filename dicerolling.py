import random

def dice_rolls(dice_types, dice_amounts, modifier):
    dice_values = []
    dice_total = 0
    
    for i in range(0,len(dice_types)):
        dice_type = int(dice_types[i][1:])
        for j in range(0,dice_amounts[i]):
            temp_roll = random.randint(1,dice_type)
            dice_values.append(temp_roll)
            dice_total += temp_roll
    
    dice_total += modifier
    
    return dice_values, dice_total
    
print("This program lets you roll dice!")
dice_types = []
dice_amounts = []
modifier = 0
modifier_choice = False

while True:
    print("What type of dice do you want to roll: d4, d6, d8, d10, d12, d20, d100")
    
    while True:
        dice_type = input("Enter dice type (or stop to calculate total): ")
        if dice_type == "stop":
            dice_values, dice_total = dice_rolls(dice_types, dice_amounts, modifier)
            print(f"The dice rolled {dice_values} with modifier {modifier} is equal to {dice_total}")
            continue_inputting = False
            break
        elif dice_type not in {"d4","d6","d8","d10","d12","d20","d100"}:
            print("Invalid dice type")
        else:
            dice_types.append(dice_type)
            break
        
    if dice_type == "stop":
        break
    
    while True:
        dice_amount = int(input(f"Enter how many {dice_type}'s do you want to roll: "))
        if dice_amount <= 0:
            print("Invalid amount, please enter an integer bigger than 0")
        else:
            dice_amounts.append(dice_amount)
            break
    
    while modifier_choice == False:    
        modifier_choice = input("Is there any modifier to the roll (y/n): ")
        if modifier_choice not in {"y","n"}:
            print("Invalid choice")
        elif modifier_choice == "y":
            modifier = int(input("Enter the modifier (positive/negative): "))
            modifier_choice == True
            break
        else: 
            break
        
    print(f"So far, you're rolling {dice_amounts}{dice_types} with modifier of {modifier}")
