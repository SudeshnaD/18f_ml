class HumanBrain:
    def prompt(self, board):
        print "You are playing: {token}".format(token=self.token)

        for row in board.positions:
            print row
        row_coordinate = input("Which row? (0-2) ")
        column_coordinate = input("Which column? (0-2) ")

        return (row_coordinate, column_coordinate)

    def receive_result(self, result):
        print "You are playing: {token}".format(token=self.token)
        print "Game over! You scored: {result}".format(result=result)
