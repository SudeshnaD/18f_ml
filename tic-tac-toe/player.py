class Player:
    def __init__(self, token):
        self.token = token
        self.brain = HumanBrain()

    def prompt(self, board):
        print board.positions

        return Move(1,2, self)


