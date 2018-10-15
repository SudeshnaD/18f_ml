class Board:
    def __init__(self):
        self.positions = [
                [ 0, 0, 0],
                [ 0, 0, 0],
                [ 0, 0, 0],
                ]

    def copy(self, board):
        for row_coordinate, row in enumerate(board.positions):
            for column_coordinate, val in enumerate(row):
                self.update(row_coordinate, column_coordinate, val)

    def update(self, row_coordinate, column_coordinate, value):
        self.positions[row_coordinate][column_coordinate] = value
