from game_state import GameState
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()

        initial_game_state = GameState(self.board)
        self.game_states = [initial_game_state]

        self.players = [Player(1), Player(-1)]

        self.next_mover().prompt()

    def next_mover(self):
        self.players[len(self.game_states) - 1]

    def move(self, mover, row_coordinate, column_coordinate):
        if self.is_valid_move(row_coordinate, column_coordinate):
        else:
            invalid_move_result(mover, row_coordinate, column_coordinate)

    def is_valid_move(row_coordinate, column_coordinate):
        return self.board.positions[row_coordinate][column_coordinate] == 0

    def update(self, row_coordinate, column_coordinate, token):
        self.board.update(row_coordinate, column_coordinate, token)
        latest_game_state = GameState(self.board)
        latest_game_state.last_move = (row_coordinate, column_coordinate, token)
        self.game_states.append(latest_game_state)

        self.check_game_ended()
