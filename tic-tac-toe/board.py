class Board:
    def __init__(self):
        self.positions = [
                [ 0, 0, 0],
                [ 0, 0, 0],
                [ 0, 0, 0],
                ]

    def update(self, move):
        self.positions[move.row_coordinate][move.column_coordinate] = move.token

    def is_valid_move(self, move):
        return self.is_occupied(move.row_coordinate, move.column_coordinate)

    def is_occupied(row_coordinate, column_coordinate):
        return self.positions[row_coordinate][column_coordinate] == 0
