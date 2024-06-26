def new_Board():
    return [[None for _ in range(3)] for _ in range(3)]

def render(playBoard):
    #print row headers
    print("  0   1   2")
    print(" +---+---+---+")
    #print each column with column numbers
    for i in range(3):
        row_str = f"{i}| " + " | ".join([" " if playBoard[j][i] is None else str(playBoard[j][i] ) for j  in range(3)]) + " |"
        print(row_str)
        print(" +---+---+---+")
    print(playBoard); 

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
    return(move_coords)
 

def make_move(board, move_coords, move):   
    
    X, Y = move_coords

    new_board = [row[:] for row in board]
    new_board[X][Y] = move
    
    if 0 <= X < len(new_board) and 0 <= Y < len(new_board[0]):
        if new_board[X][Y] is None:
            return new_board[X][Y]
    else:
        print(f"Exception: 'Can't make move {(X, Y)}, square already taken!'")

    return new_board
    
def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is None:
                return False
            
    return True


def get_all_line_coords():
    cols = []
    for x in range(3):
        col = []
        for y in range(3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for x in range(3):
        row = []
        for y in range(3):
            row.append((x, y))
        rows.append(row)

    diagonals = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

    return cols + rows + diagonals
           
def get_winner(board):
    get_all_lines = get_all_line_coords()
     
    for line in get_all_lines:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0] 
   

    return None

def main():
    board = new_Board()
    render(board)
    players = ['X', 'O']

    current_player_index = 0
    while True:
        current_player_id = players[current_player_index % 2]
        move_coords = get_move()
        board = make_move(board, move_coords, current_player_id)
        render(board)
        current_player_index += 1

        winner = get_winner(board)

        if winner is not None:
            render(board)
            print(f"The winner is {winner}")
            break
        if is_board_full(board):
            render(board)
            print("It's a DRAW!")
            break       
        
    
if __name__ == '__main__':
    main()





