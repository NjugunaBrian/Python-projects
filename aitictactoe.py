import random

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



def random_ai(board, move):
    
    move_coords = []
    for row in range(3):
        for col in range(3):
            if board[row][col] in ('','_'):
                move_coords.append((row, col))
                return move_coords
    
    if move_coords:
        move = random.choice(move_coords)
        X, Y  = move
        new_board = [row[:] for row in board]
        new_board[X][Y] = move
    
        if 0 <= X < len(new_board) and 0 <= Y < len(new_board[0]):
            if new_board[X][Y] is None:
                return new_board[X][Y]
    else:
        return None
    
    return new_board



board = new_Board()
render(board)
print(random_ai(board, "X"))






