class HumanBrain:
    def prompt(self, board):
        print "======================="
        print "{token}'s turn!".format(token=mover.token)

        for row in self.board.positions:
            print row

        return input("Which slot? (0-8) ")

    def learn(self, board, move, result):
        pass

    def save(self):
        pass
