class HumanBrain:
    def prompt(self, board):
        for row in board.positions:
            print row

        return input("Which slot? (0-8) ")

    def learn(self, board_positions, valuations):
        pass

    def save(self):
        pass
