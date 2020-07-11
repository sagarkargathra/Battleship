"""
Author : Sagar Kargathra
"""

from random import randint
board = []
for i in range(6):
    board.append(["0"] * 6)

def print_board(board):
    for row in board:
        print("   ".join(row))
print("Let's play battleship")
print_board(board)

def random_row(board):
    return randint(0,len(board) - 1)

def random_column(board):
    return randint(0,len(board) - 1)

ship_row = random_row(board)
ship_column = random_column(board)

for turn in range(10):
    print("Turn: ",turn)
    guess_row = int(input("Guess Row: "))
    guess_column = int(input("Guess Column: "))
    if guess_row == ship_row and guess_column == ship_column:
        print("CONGRATULATIONS! You have sunk the ship")
        break

    else:
        if (guess_row < 0 or guess_row > 5) or (guess_column < 0 or guess_column > 5):
            print("OOPS! That is not even in the ocean, please enter number b/w 0 and 5.")
        elif board[guess_row][guess_column] == "X":
            print("You guessed that one already")
        else:
            print("You missed the battleship")
            board[guess_row][guess_column] = "X"
    if turn == 9:
        print("GAME OVER!")
    print_board(board)









