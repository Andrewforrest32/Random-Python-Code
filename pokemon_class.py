class Pokemon:
    def __init__(self,hp,attack,special_attack,defence,special_defence,speed,types,level):
        self.hp = hp
        self.attack = attack
        self.special_attack = special_attack
        self.defence = defence
        self.special_defence = special_defence
        self.speed = speed
        self.types = types
        self.level = level
    
    def print_stats(self):
        print(f"Type(s): {self.types}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Special Attack: {self.special_attack}")
        print(f"Defence: {self.defence}")
        print(f"Special Defence: {self.special_defence}")
        print(f"Speed: {self.speed}")
        
pikachu = Pokemon(35,55,50,40,50,90,["Electric"],50)
print("Pikachu")
pikachu.print_stats()

print("")

bulbasaur = Pokemon(45,49,65,49,65,45,["Grass"],50)
print("Bulbasaur")
bulbasaur.print_stats()

print("")

charmander = Pokemon(39,52,60,43,50,65,["Fire"],50)
print("Charmander")
charmander.print_stats()

print("")

squirtle = Pokemon(44,48,50,65,64,43,["Water"],50)
print("Squirtle")
squirtle.print_stats()

print("")

starly = Pokemon(40,55,30,30,30,60,["Flying"],50)
print("Starly")
starly.print_stats()

print("")

goomy = Pokemon(45,50,55,35,75,40,["Poison"],50)
print("Goomy")
goomy.print_stats()