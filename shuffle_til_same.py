import random as R
import time as T

def compare_lists(list1):
    list1_rand = list1.copy()
    R.shuffle(list1_rand)
    print(f"The starting list is {list1} and the initial shuffled version is {list1_rand}")
    iterations = 0
    start_time = T.time()
    while True:
        if list1_rand == list1:
            end_time = T.time()
            break
        else:
            R.shuffle(list1_rand)
            print(f"The new shuffled list is {list1_rand}")
            iterations += 1
    run_time = end_time - start_time
    return run_time, iterations

initial_list = [1,2,3]
run_time, iterations = compare_lists(initial_list)
print(f"It took {run_time} seconds and {iterations} iterations to shuffle the list back to {initial_list}.")