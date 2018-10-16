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

    def is_tied(self):
        count = 0
        for row in self.positions:
            for value in row:
                count = count + abs(value)

        return count == 9

    def rows(self):
        self.positions

    def columns(self):
        first_column = []
        second_column = []
        third_column = []

        for row in self.positions:
            first_column.append(row[0])
            second_column.append(row[1])
            third_column.append(row[2])

        [first_column, second_column, third_column]

    def has_winner(self):
        has_winner = False

        # Check rows
        for row in self.rows():
            if abs(sum(row)) == 3: has_winner = True

        # Check columns
        for column in self.columns():
            if abs(sum(column)) == 3: has_winner = True

        # Check diagonals
        negative_diagonal = []
        positive_diagonal = []
        for i, row in enumerate(self.rows()):
            negative_diagonal.append(row[i])
            positive_diagonal.append(row[2 - i])
        if abs(sum(negative_diagonal)) == 3: has_winner = True
        if abs(sum(positive_diagonal)) == 3: has_winner = True

        return has_winner
