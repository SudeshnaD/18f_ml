class GameRound:
    def __init__(self, mover, waiting_player):
        self.mover = mover
        self.waiting_player = waiting_player

    def start(self, board):
        self.move = self.mover.prompt(board)
