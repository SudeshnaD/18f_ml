class Move:
    def __init__(self, row_coordinate, column_coordinate, token):
        self.row_coordinate = row_coordinate
        self.column_coordinate = column_coordinate
        self.token = token

    def flat_position(self):
        return self.row_coordinate * 3 + self.column_coordinate

    def xy_position(self):
        return (self.row_coordinate, self.column_coordinate)
