import random as R

def rock_paper_scissors():
    wins = 0
    bot_wins = 0
    options = ['Rock', 'Paper', 'Scissors']
    winning_combinations = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

    while True:
        print("Score: You:", wins, "Bot:", bot_wins)  # Display current scores

        bot = R.choice(options)

        while True:  # Loop for input validation
            user = input(f"{options} or 'stop' when done: ").capitalize()
            if user in options or user == 'Stop':
                break
            else:
                print("Invalid choice. Please choose from Rock, Paper, or Scissors.")

        if user == 'Stop':
            break

        if user == bot:
            print(f"{bot} vs {user} = draw")
        elif winning_combinations[user] == bot:  # Use dictionary for winning logic
            print(f"{bot} vs {user} = win")
            wins += 1
        else:
            print(f"{bot} vs {user} = lose")
            bot_wins += 1

    return wins, bot_wins  # Return scores for final display

print("Let's play Rock-Paper-Scissors!")
player_wins, bot_wins = rock_paper_scissors()
print(f"Your final score: {player_wins}\nBot's final score: {bot_wins}")