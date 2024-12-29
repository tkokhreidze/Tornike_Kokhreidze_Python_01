import random

def display_board(board):
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print("|   " + board[row][col] + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("This field is already occupied. Try again.")
        else:
            print("Invalid move. Enter a number between 1 and 9.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    board[move[0]][move[1]] = 'X'

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    board[1][1] = 'X'
    while True:
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break
        draw_move(board)

tic_tac_toe()
