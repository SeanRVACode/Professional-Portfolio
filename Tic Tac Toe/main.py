
def play_game():
    '''Starts the game,'''
    def board():
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
            
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        return player1,player2



    def draw_board(board):
        for _ in board:
            print(_,sep="\n")
    
    def check_winner(board,players=('X','O')):
        for player in players:
            
            # Check rows
            for row in board:
                if all(cell == player for cell in row):
                    return player
            
            # Check columns
            for col in zip(*board):
                if all(cell == player for cell in col):
                    return player
            # Check diags
            if all(cell == player for cell in board[::4]):
                return player
            if all(cell == player for cell in board[2:-1:2]):
                return player
                
    
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
        
        row_move = int(input(f"Player {current_player} which row would you like to put your tic in?\n"))
        col_move = int(input(f"Player {current_player} which col would you like to put your tic in?\n"))
        board[row_move-1][col_move-1] = current_player
        current_turn+=1
        draw_board(board)

    
    
    
        
    # board = board()        
    # a = board
    # choice_row = input("Which row do you want to put your piece in? (1-3)\n")
    # choice_column = input("Which colum ndo you want to put your piece in? (1-3)\n")
    # board[int(choice_row)-1][int(choice_column)-1] = "X" 
    # draw_board(board)
    # draw_board(a)
    
play_game()

