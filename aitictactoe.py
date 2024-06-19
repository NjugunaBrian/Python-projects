import random
import sys
from symbol import eval_input
import aiutils as utils

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


def random_move(board):
  points = [(row, col) for row in range(3) for col in range(3)]

  while True:
    (row, col) = random.choice(points)
    if board[row][col] is None:
      return (row, col)
    
def random_ai(board, move):
    return random_move(board)
    


def find_my_winning_move(board, move):
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
     
    return random_ai(board, move)

def blocking_their_winning_move(board, move):
    their_winning_move = find_my_winning_move(board, utils.get_opponent(move))
    if their_winning_move:
        return their_winning_move

def find_all_winning_moves(board, move):
    my_winning_move = find_my_winning_move(board, move)
    if my_winning_move:
        return my_winning_move
    
    their_winning_move = blocking_their_winning_move(board, move)
    if their_winning_move:
        return their_winning_move
    
    return random_ai(board, move)

def human_player(board, move):
    x = int(eval_input("X?: "))
    y = int(eval_input("X?: "))
    return (x, y)


def get_move(board, move, algorithm_name):
    if algorithm_name == 'random_ai':
        return random_ai(board, move)    
    elif algorithm_name == 'find_my_winning_move':
        return find_my_winning_move(board, move)
    elif algorithm_name == 'find_all_winning_moves':
        return find_all_winning_moves(board, move)
    elif algorithm_name == 'human_player':
        return human_player(board, move)
    else:
        raise Exception("Unknown algorithm name: " + algorithm_name) 
    
def make_move(board, move, move_coords):

    x, y = move_coords

    new_board = [row[:] for row in board]
    
    new_board[x][y] = move

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
   

    

def main(p1_name, p2_name):
    board = new_Board()
    render(board)
    players = [('X', p1_name), ('O', p2_name)]


    current_player_index = 0
    while True:
        current_player_id, current_player_name = players[current_player_index % 2]
        
        move_coords = get_move(board, current_player_id, current_player_name)
        if move_coords is None:
            print("No more moves available. Game over.")
            break
        board = make_move(board, current_player_id, move_coords)
        render(board)

        current_player_index += 1

        winner = get_winner(board)
        return winner
        '''
        if winner is not None:
            render(board)
            print(f"The winner is {winner}")
            if winner == 'X':
                return 1
            else:
                return 2
            
            
        if is_board_full(board):
            render(board)
            print("It's a DRAW!")
            return 0       
        '''

def repeated_battles(p1_name, p2_name):
    drawWin = 0
    Xwin = 0
    Owin = 0
    #we have to tally the amount of times a score becomes 0, 1 or 2 so as to establish
    winner = main(p1_name, p2_name)
    winner = main(p1_name, p2_name)
    winner = main(p1_name, p2_name)

    if winner == 'X':
        Xwin += 1
    elif winner == 'O':
        Owin += 1
    else:
        drawWin += 1

    print(Xwin)        
        
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python tictactoe.py <player1_name> <player2_name>")
        exit(1) 

    p1_name = sys.argv[1]
    p2_name = sys.argv[2]

    repeated_battles(p1_name, p2_name)
