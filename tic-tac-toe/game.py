from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.moves = []
        self.players = [Player(self, 1), Player(self, -1)]

    def start(self):
        self.move(self.next_mover().prompt())

    def next_mover(self):
        self.players[len(self.moves) % 2]

    def move(self, move):
        if self.is_valid_move(move):
        else:
            invalid_move_result(move)

    def is_valid_move(move):
        return self.board.positions[row_coordinate][column_coordinate] == 0

    def update(self, move):
        self.board.update(move)
        self.moves.append(move)
