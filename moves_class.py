import random as R

class Move:
    def __init__(self,damage,accuracy,stab_type,move_type):
        self.damage = damage
        self.accuracy = accuracy
        self.stab_type = stab_type
        self.move_type = move_type
    
    def print_info(self):
        print(f"{stab_type}-type {move_type} move")
        print(f"Damage: {damage}")
        print(f"Accuracy: {accuracy}")
        
    def check_accuracy(self):
        roll = R.randint(1,100)
        if roll <= self.accuracy:
            move_success = True
        else:
            move_success = False
        return move_success