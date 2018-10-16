from move import Move

class Player:
    def __init__(self, brain, token):
        self.brain = brain
        self.token = token
        self.brain.token = token

    def prompt(self, board):
        (row_coordinate, column_coordinate) = self.brain.prompt(board)

        return Move(row_coordinate, column_coordinate, self.token)

    def receive_result(self, result):
        self.brain.receive_result(result)

