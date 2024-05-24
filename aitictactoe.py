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

    points = [(row, col) for row in range(3) for col in range(3)]

        
    (row, col) = random.choice(points)
    if board[row][col] is not None:
        raise Exception("Illegal move!")

    new_board = [row[:] for row in board]
    

    new_board[row][col] = move

    return new_board


def get_winning_move(board, move):
    get_all_lines = get_all_line_coords()

    for line in get_all_lines:
        n_me = 0
        n_them = 0
        n_new = 0
        last_new_coords  = None

        for (x, y) in line:
            value = board[x][y]
            if value == move:
                n_me += 1
            elif value is None:
                n_new += 1
                last_new_coords = (x, y)
            else:
                n_them += 1

        if n_me == 2 and n_new == 1:
            return last_new_coords            
        
        last_new_coords = move
     
    return move

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
        board = random_ai(board, current_player_id)
        render(board)
        get_winning_move(board, current_player_id)
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


#find_winning_moves_ai will need to use the current_player argument,
#because it needs to know whose winning moves it should be trying to find

#the winning move is supposed to complete a gap where the the current player can win
#arguments are board and move in my case
#if in a row, column or diagonal where two spots match our current player, we want to play there so that we can win.


    
    
    
    












