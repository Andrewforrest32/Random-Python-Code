import random as R

def groups_five(people):
    groups_made = {}
    num_groups = len(people)//5
    for i in range(num_groups):
        group_name = f"Group #{i+1}"
        temp_group = R.sample(people,5)
        groups_made[group_name] = temp_group
        for person in temp_group:
            people.remove(person)
    return groups_made

def groups_four(people):
    groups_made = {}
    num_groups = len(people)//4
    for i in range(num_groups):
        group_name = f"Group #{i+1}"
        temp_group = R.sample(people,4)
        groups_made[group_name] = temp_group
        for person in temp_group:
            people.remove(person)
    return groups_made

def groups_three(people):
    groups_made = {}
    num_groups = len(people)//3
    for i in range(num_groups):
        group_name = f"Group #{i+1}"
        temp_group = R.sample(people,3)
        groups_made[group_name] = temp_group
        for person in temp_group:
            people.remove(person)
    return groups_made

def groups_two(people):
    groups_made = {}
    num_groups = len(people)//2
    for i in range(num_groups):
        group_name = f"Group #{i+1}"
        temp_group = R.sample(people,2)
        groups_made[group_name] = temp_group
        for person in temp_group:
            people.remove(person)
    return groups_made
    
def groups_uneven(people):
    groups_made = {}
    group0 = R.sample(people, 3)
    for person in group0:
        people.remove(person)
    groups_made = groups_two(people)
    num_groups = len(groups_made.keys())
    groups_made[f"Group #{num_groups+1}"] = group0
    return groups_made

people = []
while True:
    name = input("Enter name (or 'stop' when done): ")
    if name == 'stop':
        break
    else:
        people.append(name)
        
num_people = len(people)
if num_people%5 == 0:
    groups_made = groups_five(people)
elif num_people%4 == 0:
    groups_made = groups_four(people)
elif num_people%3 == 0:
    groups_made = groups_three(people)
elif num_people%2 == 0:
    groups_made = groups_two(people)
else:
    groups_made = groups_uneven(people)
    
print(groups_made)