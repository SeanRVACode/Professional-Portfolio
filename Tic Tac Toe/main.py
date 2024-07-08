
def play_game():
    '''Starts the game,'''
    def board():
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
            
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        return player1,player2


    # Draws current board state
    def draw_board(board):
        for _ in board:
            print(_,sep="\n")

    # Checks winners
    def check_winner(board):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                winner = row[0]
                return (True,winner)
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
                winner = board[0][col]
                return (True,winner)
        
        # Check diagnols
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            winner = board[0][0]
            return (True,winner)
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            winner = board[0][2]
            return (True,winner)
        # Returns a bool and None if a winner wasn't found so program doesn't crash
        return (False,None)
    
    # Not totally necessary, but lets players choose within the game. Maybe in later versions include player names
    player1,player2 = player_selection()
    
    board = board()
    
    draw_board(board)
    
    winner = False
    current_turn = 1
    
    # Keeps the game going while there isnt a winner
    while not winner:
        # Shifts who gets to place a mark based on whose turn it is.
        if current_turn%2 == 0:
            current_player = "O"
        else:
            current_player = "X"
        valid_move = False
        while not valid_move:
            row_move = int(input(f"Player {current_player} which row would you like to put your tic in?\n"))
            col_move = int(input(f"Player {current_player} which col would you like to put your tic in?\n"))
            if board[row_move-1][col_move-1] == " ":
                board[row_move-1][col_move-1] = current_player
                valid_move = True
            else:
                current_tic = board[row_move-1][col_move-1]
                print(f"\nThere is already a {current_tic} there please choose another area.\n")
                draw_board(board)
        current_turn+=1
        draw_board(board)
        winner,player = check_winner(board)
    
    print(f'{player} wins!')

play_game()

