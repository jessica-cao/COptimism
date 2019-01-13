import eval_board_state
from chess import *
import check_valid_moves

def minimax(board, depth, color, is_max_player):
    """Minimax algorithm. Uses white as the reference color"""
    if depth == 0 or is_game_over(board):
        return eval_board_state.eval_board_state(board)
    if is_max_player:
        best_value = -100000000
        for child in all_valid_boards(board, color):
            best_value = max(best_value, minimax(board, depth - 1, color.other(), not is_max_player))
        return best_value
    else:
        best_value = 100000000
        for child in all_valid_boards(board, color):
            best_value = min(best_value, minimax(board, depth - 1, color.other(), not is_max_player))
        return best_value




def is_game_over(board):
    return len(check_valid_moves.moves_while_in_check(board)) == 0

def all_valid_boards(board, color):
    all_valid_boards = []
    if not check_valid_moves.is_in_check(board, color):
        for x in range(8):
            for y in range(8):
                if board.get(x, y) is not None and board.get(x, y).color == color:
                    for move in check_valid_moves.valid_moves(x, y, board):
                        child = board.copy()
                        child.move_piece(x, y, *move)
                        all_valid_boards.append(child)
    else:
        all_valid_boards.append(check_valid_moves.boards_while_in_check(board, color))
    return all_valid_boards

board = eval_board_state.is_in_check()
for board in all_valid_boards(board, Color.WHITE):
    print(board)




