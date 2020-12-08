import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

# Creating a board of 6*7 cells!
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
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
# print cell of the board from bottom to up 
def print_board(board):
    print(np.flip(board, 0))

# Check the winning moves!
def wining_move(board, piece):
    # Check the horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check the vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonnals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonnals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 Input 
    if turn == 0:
        column = int(input("Player 1 Make your Selection (0-6): "))
        
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

            if wining_move(board, 1):
                print("Player 1 Win! Congrats.")
                game_over = True
                break

    # Ask for player 2 Input
    else:
        column = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

            if wining_move(board, 2):
                print("Player 2 Win! Congrats.")
                game_over = True
                break

    print_board(board)

    turn = turn + 1
    turn = turn % 2

