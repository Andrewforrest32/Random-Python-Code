import random as R

rooms = {
    "Kitchen":"Empty","Living Room":"Empty","Dining Room":"Empty",
    "Attic":"Empty","Basement":"Empty"}
    
def user_movement(user_room_choice,rooms,user_found):
    if rooms[user_room_choice] == "Ghost":
        print("Boo! The ghost found you!")
        user_found = True
    elif rooms[user_room_choice] == "Empty":
        rooms[user_room_choice] == "User"
        print("You're safe, for now.")
    return rooms, user_found

def ghost_movement(room_options,rooms,user_found):
    ghost_room_choice = R.choice(room_options)
    if rooms[ghost_room_choice] == "User":
        print("Boo! The ghost found you!")
        user_found = True
    else:
        rooms[ghost_room_choice] = "Ghost"
    return rooms, user_found

print("You find yourself in a haunted house!")
room_options = list(rooms.keys())
print("A ghost is trapped in the house, looking for its next victim!")
user_found = False
print("You start in the living room and have to evade the ghost.")
rooms["Living Room"] = "User"
    
while True:
    print(f"There are the following rooms: {room_options}")
    while True:
        user_room_choice = input("Which room would you like to move to: ")
        if rooms[user_room_choice] == "User":
            print("Invalid option, you're already in that room.")
        else:
            break
    rooms, user_found = ghost_movement(room_options,rooms, user_found)
    if user_found == True:
        break
    rooms, user_found = user_movement(user_room_choice, rooms, user_found)
    if user_found == True:
        break
    