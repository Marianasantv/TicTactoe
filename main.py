def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, position, player):
   board[position[0]][position[1]]= player
   return board
    
print(' ')
print(' ')


def check_for_winner(board, player):
    if (board[0][0] == player and board[0][1] == player and board[0][2]== player):
        return True
        print(print_board)
    elif (board[1][0] == player and board[1][1] == player and board[1][2]== player):
        return True
        print(print_board)
    elif (board[2][0] == player and board[2][1] == player and board[2][2]== player):
        return True
        print(print_board)
    elif (board[0][0] == player and board[1][0] == player and board[2][0]== player):
        return True
        print(print_board)
    elif (board[0][1] == player and board[1][1] == player and board[2][1]== player):
        return True
        print(print_board)
    elif (board[0][2] == player and board[1][2] == player and board[2][2]== player):
        return True
        print(print_board)
    elif (board[0][0] == player and board[1][1] == player and board[2][2]== player):
        return True
        print(print_board)
    elif (board[0][2] == player and board[1][1] == player and board[2][0]== player):
        return True
        print(print_board)
    else:
        return False


##Testing:

board = create_empty_board()
print_board(board)

print(' ')
print(' ')

update_board(board,[1,2],"X")
update_board(board,[1,1],"O")
update_board(board,[2,2],"X")
update_board(board,[0,2],"O")
update_board(board,[2,0],"X")
update_board(board,[2,1],"O")
update_board(board,[0,0],"X")
update_board(board,[0,1],"O")
print_board(board)
print(' ')
print(' ')
print(check_for_winner(board,"X"))
print(' ')
