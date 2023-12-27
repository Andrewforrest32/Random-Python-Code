import random as R

def correct_list(names_list):
    while True:
        print(names_list)
        name_index = int(input("Which name is wrong, enter the number (starting at 1 or 0 when done): "))
        if name_index == 0:
            break
        name_choice = input("Do you wanna correct the name or remove it? (correct/remove): ")
        if name_choice == 'correct':
            new_name = input("Enter the corrected name: ")
            names_list[name_index-1] = new_name
        elif name_choice == 'remove':
            names_list.pop(name_index-1)
    return names_list

def declare_limitations(names_list):
    limit_list = {}
    choice = input("Are there any limitations (besides people not getting themselves)? (y/n): ")
    if choice == 'y':
        while True:
            name1 = input("Enter the first name with a restriction (or stop when done): ")
            if name1 == 'stop':
                break
            else:
                name2 = input("Enter the second associated name: ")
                # Check if name1 is already in the limit_list
                if name1 not in limit_list:
                    limit_list[name1] = []
                limit_list[name1].append(name2)
                # Check if name2 is already in the limit_list
                if name2 not in limit_list:
                    limit_list[name2] = []
                limit_list[name2].append(name1)
    return limit_list

def draw_names(names_list, limit_list):
    names_drawn = {}
    while names_list:
        name1 = R.choice(names_list)
        while True:
            name2 = R.choice(names_list)
            if name2 not in limit_list.get(name1, []) and name2 != name1:
                names_list.remove(name2)
                names_drawn[name1] = name2
                names_drawn[name2] = name1
                break
    return names_drawn

print("Let's help you plan a gift exchange!")
names_list = []
while True:
    print(names_list)
    name = input("Enter a name (or stop when done): ")
    if name == 'stop':
        print(names_list)
        is_correct = input("Is the above list of names correct? (y/n): ")
        if is_correct == 'y':
            break
        else:
            names_list = correct_list(names_list)
    else:
        names_list.append(name)
        
limit_list = declare_limitations(names_list)
names_drawn = draw_names(names_list.copy(), limit_list)  # Pass a copy of names_list to draw_names
print(names_drawn)
