class HumanBrain:
    def prompt(self, board):
        move_position = input("Which slot? (0-8) ")
        row_coordinate = move_position / 3
        column_coordinate = move_position % 3

        return (row_coordinate, column_coordinate)

    def receive_result(self, result):
        print "You are playing: {token}".format(token=self.token)
        print "Game over! You scored: {result}".format(result=result)

    def learn(self, game):
        pass

    def save(self):
        pass
