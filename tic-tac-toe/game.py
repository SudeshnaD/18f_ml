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

    def update(self, row_coordinate, column_coordinate, token):
        self.board.update(row_coordinate, column_coordinate, token)
        latest_game_state = GameState(self.board)
        latest_game_state.last_move = (row_coordinate, column_coordinate, token)
        self.game_states.append(latest_game_state)
