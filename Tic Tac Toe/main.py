
def draw_board():
    size = 3
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board


# Ask Player if they want to be X or O
def player_selection():
    valid_choice = False
    while not valid_choice:
        player1 = input("Player 1 do you want to be X or O?\n").upper()
        if player1.upper() == "X" or player1.upper() == "O":
            valid_choice = True
        else:
            print(f"Sorry {player1} is not a valid selection.\n")
    return player1



