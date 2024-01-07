import random as R
import time as T
        
run_time = 0
wins = 0
flips = 0

start_time = T.time()
while run_time < 5:
    flip = R.randint(1,2)
    guess = R.randint(1,2)
    flips += 1
    if guess == flip:
        wins += 1
    run_time = T.time()-start_time
    
win_rate = int(wins/flips*100)
print(f"The code ran for {run_time} second(s), flipped a coin {flips} times and guessed {wins} times right.")
print(f"That's a win rate of {win_rate}%")