# 2.5.1.11 LAB: Sudoku
def is_valid_sudoku(board):
    # Helper function to check if a list contains all digits from 1 to 9
    def is_valid_group(group):
        return sorted(group) == list("123456789")

    # Check all rows
    for row in board:
        if not is_valid_group(row):
            return "No"

    # Check all columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return "No"

    # Check all 3x3 sub-squares
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            sub_square = [
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
            ]
            if not is_valid_group(sub_square):
                return "No"

    return "Yes"

# Input 9 rows of the Sudoku
board = []
for _ in range(9):
    row = input("Enter a row of 9 digits: ").strip()
    if len(row) != 9 or not row.isdigit():
        print("Invalid input. Each row must contain exactly 9 digits.")
        exit()
    board.append(row)

# Output the result
print(is_valid_sudoku(board))
