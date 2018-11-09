from board import Board
from player import Player

class Game:
    def __init__(self, player1_brain, player2_brain):
        self.board = Board()
        self.moves = []
        self.player1 = Player(player1_brain, 1)
        self.player2 = Player(player2_brain, -1)

    def start(self):
        self.start_new_round(self.player1, self.player2)

    def start_new_round(self, mover, waiter):
        move = mover.prompt(self.board)

        if not self.board.is_valid_move(move):
            mover.receive_invalid_move(self.board, move)
            self.start_new_round(mover, waiter)
            return

        self.moves.append(move)
        self.board.update(move)

        if self.board.has_winner():
            mover.receive_result(self.moves, 1)
            waiter.receive_result(self.moves, -1)
        elif self.board.is_tied():
            mover.receive_result(self.moves, 0)
            waiter.receive_result(self.moves, 0)
        else:
            self.start_new_round(waiter, mover)
