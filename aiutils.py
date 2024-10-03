def get_opponent(who_am_i):
    if who_am_i == 'X':
        return 'O'
    elif who_am_i == 'O':
        return 'X'
    else:
        raise Exception("Unknown player: " + who_am_i)
    

def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] is None]    