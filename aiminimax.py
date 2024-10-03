import copy

import aitictactoe as engine
import aiutils as utils


def _minimax_score(board, player_to_move, player_to_optimize):
    winner  = engine.get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif engine.is_board_full(board):
        return 0

    legal_moves = utils.get_available_moves(board)

    scores = []

    for move in legal_moves:
        new_board = copy.deepcopy(board)
        engine.make_move(new_board, move, player_to_move)

        opp = utils.get_opponent(player_to_move)
        opp_best_response_score = _minimax_score(new_board, opp, player_to_optimize)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)    

def minimax_ai(board, who_am_i):
    best_move = None
    best_score = None

    for move in utils.get_available_moves(board):
        new_board = copy.deepcopy(board)
        engine.make_move(new_board, who_am_i, move)

        opp = utils.get_opponent(who_am_i)
        score = _minimax_score(new_board, opp, who_am_i)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score

        return best_move        