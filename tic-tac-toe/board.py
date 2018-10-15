class Board:
    def __init__(self):
        self.positions = [
                [ 0, 0, 0],
                [ 0, 0, 0],
                [ 0, 0, 0],
                ]

    def update(self, move):
        self.positions[move.row_coordinate][move.column_coordinate] = move.token
