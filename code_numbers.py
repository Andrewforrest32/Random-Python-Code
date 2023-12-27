import random as R

def code_num():
    code = [R.randint(1, 10) for _ in range(4)]
    guesses = 0
    
    while True:
        guess = input("Enter 4 numbers, from 1 to 4, separated by spaces: ")
        guess = guess.split()
        guess = [int(num) for num in guess]
        guesses += 1
        
        correct_places = 0
        correct_wrong_places = 0
        
        if guess == code:
            print("Congrats, that's the secret code!")
            break
        else:
            for i in range(4):
                if guess[i] == code[i]:
                    correct_places += 1
                elif guess[i] in code:
                    correct_wrong_places += 1
            if correct_places == 0 and correct_wrong_places == 0:
                print("Sorry, none of those numbers are in the code.")
            else:
                print(f"You got {correct_places} in the correct spot and {correct_wrong_places} in the wrong spot!")
    
    return(guesses)
    
print("Let's play Code Numbers!")
print("There are four numbers randomnly chosen from 1 to 10 (with potential repeats)")
print("Keep guessing until you got all four in the right spots!")
guesses = code_num()
print(f"It took you {guesses} to get the right code!")
