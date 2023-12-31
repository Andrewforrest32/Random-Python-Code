import random as R
    
def place_user(board):
    while True:
        row_user = int(input("Which row do you want to place an 'X': "))
        col_user = int(input("Which column do you want to place an 'X': "))
        
        if board[row_user-1][col_user-1] == False:
            board[row_user-1][col_user-1] = 'X'
            break
        else:
            print("Invalid spot, try again.")
    return board
    
def place_bot(board):
    while True:
        row_bot = R.randint(0,2)
        col_bot = R.randint(0,2)
        
        if board[row_bot][col_bot] == False:
            board[row_bot][col_bot] = 'O'
            break
    return board

def check_win(board):
    win_condition = False
    winning_side = ""
    diag1_counter = 0
    diag2_counter = 0
    temp = False
    for x in board: #check rows
        if all(y == x[0] for y in x):
            if x[0] != False:
                win_condition = True
                winning_side = x[0]
    flipped_board = [[],[],[]]
    for x in board: #transpose board
        for i in range(len(x)):
            flipped_board[i].append(x[i])
    for x in flipped_board: #check columns
        if all(y == x[0] for y in x):
            if x[0] != False:
                win_condition = True
                winning_side = x[0]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != False:
        win_condition = True
        winning_side = board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == [2][0] and board[0][2] != False:
        win_condition = True
        winning_side = board[0][2]
    return win_condition, winning_side
    
board = [[False,False,False],[False,False,False],[False,False,False]]
print("Play Tic-Tac-Toe against the compuer, you start with 'X'.")

while True:
    for row in board:
        print(row)
    board = place_user(board)
    board = place_bot(board)
    win_condition, winning_side = check_win(board)
    if win_condition:
        for row in board:
            print(row)
        print(f"Congrats {winning_side}'s, you won!")
        break
