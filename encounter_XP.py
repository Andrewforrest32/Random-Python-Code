def calculate_xp(party_level, party_size, difficulty):
    character_xp = [
        [25,50,75,100],[50,100,150,200],[75,150,224,400],[125,250,375,500],
        [250,500,750,1100],[300,600,900,1400],[350,750,1100,1700],[450,900,1400,2100],
        [550,1100,1600,2400],[600,1200,1900,2800],[800,1600,2400,3600],[1000,2000,3000,4500],
        [1100,2200,3400,5100],[1250,2500,3800,5700],[1400,2800,4300,6400],
        [1600,3200,4800,7200],[2000,3900,5900,8800],[2100,4200,6300,9500],
        [2400,4900,7300,10900],[2800,5700,8500,12700]]
    difficulty_xp = {"easy":0,"medium":1,"hard":2,"deadly":3}
    difficulty_index = difficulty_xp[difficulty]
    per_character_XP = character_xp[party_level][difficulty_index]
    return per_character_XP*party_size
    
party_level = int(input("Enter the level of the party: "))
party_size = int(input("Enter the size of the party: "))
difficulty = input("What difficulty level (easy, medium, hard, deadly): ")
encounter_xp = calculate_xp(party_level, party_size, difficulty)
print(f"Your {party_size} players of level {party_level} encounters a {difficulty} encounter of {encounter_xp}XP.")