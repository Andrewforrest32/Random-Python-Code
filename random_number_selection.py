import random as R
import time as T

def choose_num(start_num, end_num):
    numbers = list(range(start_num, end_num+1))
    selected_num = R.randint(start_num, end_num)
    start_time = T.time()
    while True:
        temp = R.choice(numbers)
        if temp == selected_num:
            break
        else:
            numbers.remove(temp)
    
    end_time = T.time()
    return (end_time-start_time)
    
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
run_time = choose_num(start_num, end_num)
print(f"It took {run_time} seconds to find a specific random number between the range you entered.")