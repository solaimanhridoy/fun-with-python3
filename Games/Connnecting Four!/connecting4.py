import numpy as np 

# Creating a board of 6*7 cells!
def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 Input 
    if turn == 0:
        selection = int(input("Player 1 Make your Selection (0-6): "))

    # Ask for player 2 Input
    else:
        selection = int(input("Player 2 Make your Selection (0-6): "))

    turn = turn + 1
    turn = turn % 2

