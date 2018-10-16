from board import Board
from player import Player
from game_round import GameRound
from invalid_move_game_result import InvalidMoveGameResult
from winning_game_result import WinningGameResult
from tied_game_result import TiedGameResult

class Game:
    def __init__(self, player1_brain, player2_brain):
        self.board = Board()
        self.rounds = []
        self.player1 = Player(player1_brain, 1)
        self.player2 = Player(player2_brain, -1)

    def start(self):
        self.start_new_round(self.player1, self.player2)

    def start_new_round(self, mover, waiting_player):
        new_round = GameRound(mover, waiting_player)
        self.rounds.append(new_round)
        self.current_round = new_round
        self.current_round.start(self.board)
        self.move(self.current_round.move)

    def move(self, move):
        if not self.board.is_valid_move(move):
            self.result = InvalidMoveGameResult(self.current_round.mover)
            return

        self.board.update(move)

        if self.board.has_winner():
            self.result = WinningGameResult(self.current_round.mover, self.current_round.waiting_player)
        elif self.board.is_tied():
            self.result = TiedGameResult(self.current_round.next_mover)
        else:
            self.start_new_round(self.current_round.waiting_player, self.current_round.mover)
