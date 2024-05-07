
def new_Board():
    return [[None for _ in range(3)] for _ in range(3)]


board = new_Board()

def render(playBoard):
    #print row headers
    print("  0   1   2")
    print(" +---+---+---+")
    #print each column with column numbers
    for i in range(3):
        row_str = f"{i}| " + " | ".join([" " if playBoard[j][i] is None else str(playBoard[j][i] ) for j  in range(3)]) + " |"
        print(row_str)
        print(" +---+---+---+")
    #print(playBoard); 

def get_move():
    print("What is your move's X co-ordinate?")
    while True:
        X_move = input('=> ')
        if not X_move.isdecimal():
              print("Please enter a number")
        else:
            X_move = int(X_move)
            break      
    print("What is your move's Y co-ordinate?")
    while True:
        Y_move = input('=> ')
        if not Y_move.isdecimal():
            print("Please enter a number")
        else:
            Y_move = int(Y_move)  
            break

    move_coords = (X_move, Y_move)
    print(move_coords)


#board[0][1] = 'X'
#board[1][1] = 'O' 

render(board)
print(get_move())
    