import numpy as np

class Move:
    def __init__(self, move_recommendations, mover):
        self.recommendations = move_recommendations
        self.flat_position = np.random.choice(np.arange(9), p=move_recommendations)

        self.row_coordinate = self.flat_position / 3
        self.column_coordinate = self.flat_position % 3
        self.xy_position = (self.row_coordinate, self.column_coordinate)

        self.mover = mover
        self.token = self.mover.token
