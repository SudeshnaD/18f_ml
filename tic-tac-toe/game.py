from game_state import GameState
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()

        initial_game_state = GameState(self.board)
        self.game_states = [
                initial_game_state
                ]

        self.players = [Player(1), Player(-1)]

    def nth_player(self, player_number):
        self.players[player_number]
