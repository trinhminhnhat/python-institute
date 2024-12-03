#4.7.2.1 PROJECT: Tic-Tac-Toe
from random import randrange

def display_board(board):
    # Display the board in the console
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   " . join(str(cell) for cell in row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    # Accept and validate the user's move
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = 'O'
                    return
        print("Square already occupied. Choose another.")

def make_list_of_free_fields(board):
    # Create a list of free squares
    free_fields = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check if a player has won
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Row 1
        [(1, 0), (1, 1), (1, 2)],  # Row 2
        [(2, 0), (2, 1), (2, 2)],  # Row 3
        [(0, 0), (1, 0), (2, 0)],  # Column 1
        [(0, 1), (1, 1), (2, 1)],  # Column 2
        [(0, 2), (1, 2), (2, 2)],  # Column 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    # Make a random move for the computer
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

# Initialize the board
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

# Game loop
while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You win!")
        break
    draw_move(board)
    if not make_list_of_free_fields(board):
        display_board(board)
        print("It's a tie!")
        break
