from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.moves = []
        self.players = [Player(self, 1), Player(self, -1)]

    def start(self):
        self.move(self.players[0].prompt(self.board))

    def next_mover(self):
        self.players[len(self.moves) % 2]

    def move(self, move):
        self.moves.append(move)

        if not self.board.is_valid_move(move):
            self.result = GameResult(GameResult.INVALID_MOVE)
            move.mover.receive_result(self.result)
            return

        self.board.update(move)

        if self.board.game_finished():
            if self.board.is_tied():
                self.result = GameResult(GameResult.TIED)
            else if self.board.
        else:
            self.next_mover().prompt(self.board)
