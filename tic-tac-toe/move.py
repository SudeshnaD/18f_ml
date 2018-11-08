class Move:
    def __init__(self, row_coordinate, column_coordinate, mover):
        self.row_coordinate = row_coordinate
        self.column_coordinate = column_coordinate
        self.mover = mover
        self.token = self.mover.token

    def flat_position(self):
        return self.row_coordinate * 3 + self.column_coordinate

    def xy_position(self):
        return (self.row_coordinate, self.column_coordinate)
