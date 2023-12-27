import random as R

def populate_list(end_range):
    numbers_list = list(range(1, end_range + 1))
    numbers_list_copy = numbers_list.copy()
    death_number = R.choice(numbers_list_copy)
    numbers_list_copy.remove(death_number)
    coin_num1 = R.choice(numbers_list_copy)
    numbers_list_copy.remove(coin_num1)
    coin_num2 = R.choice(numbers_list_copy)
    numbers_list_copy.remove(coin_num2)
    coin_num3 = R.choice(numbers_list_copy)
    numbers_list_copy.remove(coin_num3)
    return numbers_list,death_number,coin_num1,coin_num2,coin_num3
    
def guess_numbers(numbers_list,death_number,coin_num1,coin_num2,coin_num3,end_range):
    score = ""
    coins = 3
    while True:
        print(numbers_list)
        guess = int(input(f"Guess a number from the list: "))
        if guess not in numbers_list:
            print("Invalid guess!")
        elif guess == death_number:
            score = "You got the death number, sorry!"
            break
        elif guess == coin_num1 or guess == coin_num2 or guess == coin_num3:
            coins -= 1
            print(f"You got a coin! Only {coins} coin(s) left!")
            numbers_list.remove(guess)
        else:
            print("Guess again!")
            numbers_list.remove(guess)
        
        if coins == 0:
            score("Congratulations! You found all 3 coins and avoided the death number!")
    return score
    
print("Let's play a game!")
end_range = int(input("Starting at 1, enter an ending number: "))
print("The goal of the game is to find the three secret coins hidden within the numbers!")
print("However, be careful of finding the death coin, which immediately ends the game!")
numbers_list,death_number,coin_num1,coin_num2,coin_num3 = populate_list(end_range)
score = guess_numbers(numbers_list,death_number,coin_num1,coin_num2,coin_num3,end_range)
print(score)
print(f"The death coin was: {death_number} and the 3 coins were at: {coin_num1}, {coin_num2}, and {coin_num3} ")