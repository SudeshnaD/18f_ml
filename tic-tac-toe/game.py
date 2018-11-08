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
        print "======================="
        print "ROUND {round_n}".format(round_n=len(self.moves) + 1)
        print "{token}'s turn!".format(token=mover.token)

        for row in self.board.positions:
            print row

        move = mover.prompt(self.board)

        print "{token} chooses {position}".format(token=move.token, position=move.flat_position())
        if not self.board.is_valid_move(move):
            mover.learn(self.board, move, -1)
            print "Invalid move! Try again"
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
