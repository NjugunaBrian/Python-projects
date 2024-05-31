def get_opponent(move):
    if move == 'X':
        return 'O'
    elif move == 'O':
        return 'X'
    else:
        raise Exception("Unknown player: " + move)