from game_state import GameState
from board import Board

class Game:
    def __init__(self):
        self.board = Board()

        initial_game_state = GameState(self.board)
        self.game_states = [
                initial_game_state
                ]

