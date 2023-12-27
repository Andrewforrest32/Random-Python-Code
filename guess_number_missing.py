import random as R

def populate_list(end_range, size):
    list_random = [R.randint(1, end_range) for _ in range(size)]
    return list_random
    
def remove_item(end_range, size):
    while True:
        list_random = populate_list(end_range, size)
        print(list_random)
        list_copy = list_random.copy()
        R.shuffle(list_copy)
        removed_item = R.choice(list_copy)
        list_copy.remove(removed_item)
        print(list_copy)
        answer = input("Enter the missing number from the original list or 'stop' when done: ")
        if answer == 'stop':
            break
        elif int(answer) == removed_item:
            print("Congrats, you found the missing number!")
        else:
            print(f"Sorry, that wasn't the missing number, {removed_item} was.")

print("Let's play Find the Missing Number!")
end_range = int(input("Starting at 1, pick an ending number: "))
size = int(input("Enter the length of the list: "))
print(f"Starting the game with a list of {size} numbers from 1 to {end_range}...")
remove_item(end_range, size)