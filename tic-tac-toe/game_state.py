from board import Board

class GameState:
    def __init__(self, board):
        self.board_state = Board()
        self.board_state.copy(board)
