from board import Board
from player import Player
from invalid_move_game_result import InvalidMoveGameResult
from winning_game_result import WinningGameResult
from tied_game_result import TiedGameResult

class Game:
    def __init__(self, player1_brain, player2_brain):
        self.board = Board()
        self.moves = []
        self.player1 = Player(player1_brain, 1)
        self.player2 = Player(player2_brain, -1)

    def start(self):
        self.start_new_round(self.player1, self.player2)

    def start_new_round(self, mover, waiting_player):
        print "======================="
        print "ROUND {round_n}".format(round_n=len(self.moves) + 1)
        print "{token}'s turn!".format(token=mover.token)

        for row in self.board.positions:
            print row

        move = mover.prompt(self.board)

        print "{token} chooses {position}".format(token=move.token, position=move.flat_position())
        if not self.board.is_valid_move(move):
            self.result = InvalidMoveGameResult(mover)
            self.start_new_round(mover, waiting_player)
            return

        self.moves.append(move)
        self.board.update(move)

        if self.board.has_winner():
            self.result = WinningGameResult(mover, waiting_player)
        elif self.board.is_tied():
            self.result = TiedGameResult(mover, waiting_player)
        else:
            self.start_new_round(waiting_player, mover)
