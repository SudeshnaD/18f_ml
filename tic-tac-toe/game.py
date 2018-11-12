from board import Board
from player import Player

class Game:
    def __init__(self, player1_brain, player2_brain):
        self.board = Board()
        self.moves = []
        self.player1 = Player(player1_brain, 1)
        self.player2 = Player(player2_brain, -1)
        self.winner = None
        self.invalid_moves = 0

    def start(self):
        self.start_new_round(self.player1, self.player2)

    def start_new_round(self, mover, waiter):
        print "======================="
        for row in self.board.positions:
            print row

        print "{token}'s turn!".format(token=mover.token)
        move = mover.prompt(self.board)

        print "{token} selects {move_position}".format(token=mover.token, move_position=move.flat_position)

        if not self.board.is_valid_move(move):
            print "invalid! Try again!"
            self.invalid_moves += 1
            mover.receive_invalid_move(self.board, move)
            if self.invalid_moves < 20: # Prevent stack overflow
                self.start_new_round(mover, waiter)
            return

        self.moves.append(move)
        self.board.update(move)

        if self.board.has_winner():
            print "{winner_token} wins!".format(winner_token=mover.token)
            self.winner = mover.token
            print "{winner_token} learning:".format(winner_token=mover.token)
            mover.receive_result(self.moves, 1.)
            print "{loser_token} learning:".format(loser_token=waiter.token)
            waiter.receive_result(self.moves, 0.)
        elif self.board.is_tied():
            print "tie!"
            self.winner = 0
            # mover.receive_result(self.moves, 0.5)
            # waiter.receive_result(self.moves, 0.5)
        else:
            self.start_new_round(waiter, mover)
