from random import randint
# variables
board = ['-' , '-' , '-' ,
         '-' , '-' , '-' ,
         '-' , '-' , '-']
current_player = 'x'
winner = ''
game_running = True

# game board
def print_board(board):
    print(board[0] + '|' + board[1] + '|' +  board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' +  board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' +  board[8])


# take player input
def player_input(board):
    inp = int(input('Select a spot between 1 - 9 : '))
    if board[inp - 1] == '-':
        board[inp - 1] = current_player
    else:
        print('oooooh dadach dari eshtebah mizani in khone pore!!!!')


# check for win
def check_horizontale(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    
def check_if_win(board):
    global game_running
    if check_horizontale(board):
        print_board(board)
        print(f'The winner is {winner}')
        game_running = False
    elif check_row(board):
        print_board(board)
        print(f'The winner is {winner}')
        game_running = False
    elif check_diagonal(board):
        print_board(board)
        print(f'The winner is {winner}')
        game_running = False





# check for tie
def check_if_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('It\'s a tie')
        game_running = False

# switch player
def switch_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    else :
        current_player = 'x'

# computer choice
def computer(board):
    while current_player == 'o':
        position = randint(0 , 8)
        if board[position] == '-':
            board[position] = 'o'
            switch_player()



# functionality
while game_running:
    print_board(board)
    player_input(board)
    check_if_win(board)
    check_if_tie(board)
    switch_player()
    computer(board)
    check_if_win(board)
    check_if_tie(board)