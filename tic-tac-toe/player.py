class Player:
    def __init__(self, token, brain):
        self.token = token
        self.brain = brain

    def prompt(self, board):
        print board.positions

        return Move(1,2, self)


