from move import Move
from board import Board

class Player:
    def __init__(self, brain, token):
        self.brain = brain
        self.token = token
        self.brain.token = token

    def prompt(self, board):
        move_position = self.brain.prompt(board)

        row_coordinate = move_position / 3
        column_coordinate = move_position % 3

        return Move(row_coordinate, column_coordinate, self)

    def receive_invalid_move(self, board, move):
        self.brain.learn(board, move, -1)

    def receive_result(self, moves, result):
        board = Board()
        for move in moves:
            if move.mover.token == self.token:
                self.brain.learn(board, move, result)
            board.update(move)
