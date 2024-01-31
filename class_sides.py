class battle_side:
    def __init__(self, hp, energy, mana):
        self.hp = hp    # Health points
        self.energy = energy  # Energy points
        self.mana = mana      # Mana points
        
    def print_stats(self):
        print(f'HP: {self.hp}')
        print(f'Energy: {self.energy}')
        print(f'Mana: {self.mana}')
        
    def recover(self):
        self.hp += 20
        if self.hp > 50:
            self.hp = 50
        self.energy += 20
        if self.energy > 50:
            self.energy = 50
        self.mana += 20
        if self.mana >= 50:
            self.mana = 50
    
    def strike_user(self):
        self.energy -= 20
    def strike_other(self):
        self.hp -= 15
    
    def cast_user(self):
        self.mana -= 20
    def cast_other(self):
        self.hp -= 15    
    

player = battle_side(50,50,50)
print("Player")
player.print_stats()
print("Player recovered")
player.recover()
player.print_stats()

bot = battle_side(50,50,50)
print("\nBot")
bot.print_stats()