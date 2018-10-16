from board import Board
from player import Player
from game_round import GameRound

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.rounds = []

        self.player1 = player1
        self.player1.token = 1

        self.player2 = player2
        self.player2.token = -1

        self.players = [player1, player2]

    def start(self):
        self.start_new_round()

    def start_new_round(self):
        new_round = GameRound(self.board, self.next_mover(), self.waiting_player())
        self.rounds.append(new_round)
        new_round.start()

    def next_mover(self):
        self.players[len(self.rounds) % 2]

    def waiting_player(self):
        self.players[(len(self.rounds) - 1) % 2]

    def current_round(self):
        self.rounds[-1]

    def move(self, move):
        self.current_round().move = move

        if not self.board.is_valid_move(move):
            self.result = InvalidMoveGameResult(self.next_mover(), self.waiting_player())
            return

        self.board.update(move)

        if self.board.has_winner():
            self.result = WinningGameResult(self.next_mover(), self.waiting_player())
        else if self.board.is_tied():
            self.result = TiedGameResult(self.next_mover(), self.waiting_player())
        else:
            self.start_new_round()
