from random import randint

board =[]

for x in range(5):
    board.append(["O"]*5)

def print_board(board_in):
    for i in range(len(board_in)):
        print(" ".join(board_in[i]))

print_board(board)

ship_row = randint(0,len(board)-1)
ship_col = randint(0,len(board)-1)

print(ship_row)
print(ship_col)
for turn in range(4):
    guess_row = int(input("Enter guess row: "))
    guess_col = int(input("Enter guess col: "))

    print("Turn", turn + 1)

    if ship_row == guess_row and ship_col == guess_col:
        print("You found the battleship")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("That's not even in the ocean")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed the battleship")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")







