def is_valid_sudoku(board):
    def is_valid_group(group):
        return sorted(group) == list(range(1, 10))

    for row in board:
        if not is_valid_group(row):
            return False

    for col in range(9):
        if not is_valid_group([board[row][col] for row in range(9)]):
            return False

    for box_row in range(3):
        for box_col in range(3):
            if not is_valid_group([board[row][col] for row in range(box_row * 3, (box_row + 1) * 3) for col in range(box_col * 3, (box_col + 1) * 3)]):
                return False

    return True

board = []
print("Enter the Sudoku board row by row (each row should be 9 digits):")
for i in range(9):
    while True:
        row = input(f"Row {i + 1}: ").strip()
        if len(row) == 9 and row.isdigit():
            board.append([int(char) for char in row])
            break
        else:
            print("Invalid input. Please enter exactly 9 digits.")

if is_valid_sudoku(board):
    print("Yes")
else:
    print("No")

    