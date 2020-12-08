import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

# Creating a board of 6*7 cells!
def create_board():
    board = np.zeros((6,7))
    return board

# Add player's input (drop ball)
def drop_piece(board, row, column, piece):
    board[row][column] = piece

# Check whether the location is valid
def is_valid_location(board, column):
    return board[5][column] == 0

# Check if the cell is the last cell of a row, then get the cell from next row
def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 Input 
    if turn == 0:
        column = int(input("Player 1 Make your Selection (0-6): "))
        
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

    # Ask for player 2 Input
    else:
        column = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

    print(board)

    turn = turn + 1
    turn = turn % 2

