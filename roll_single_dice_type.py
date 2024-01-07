import random as R

def roll_dice(dice_input):
    dice_input = dice_input.split("d")
    quantity = int(dice_input[0])
    sides = int(dice_input[1])
    dice_sum = 0
    for i in range(quantity):
        roll = R.randint(1,sides)
        print(f"Roll #{i+1}: {roll}")
        dice_sum += roll
    return dice_sum

dice_input = input("Enter dice to roll in the following format 'quantity'd'sides'(ex: 3d10): ")
dice_sum = roll_dice(dice_input)
print(f"The sum of the above rolls is {dice_sum}")