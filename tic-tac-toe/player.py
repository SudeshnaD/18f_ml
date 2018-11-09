from move import Move
from board import Board
import numpy as np
import copy

class Player:
    def __init__(self, brain, token):
        self.brain = brain
        self.token = token
        self.brain.token = token

    def prompt(self, board):
        move_position = self.brain.prompt(board, self.token)

        row_coordinate = move_position / 3
        column_coordinate = move_position % 3

        return Move(row_coordinate, column_coordinate, self)

    def receive_invalid_move(self, board, move):
        board_position = np.array(board.positions).flatten()
        board_position = board_position * self.token

        other_values = 1./8.
        valuation = [other_values] * 9
        valuation[move.flat_position()] = 0

        self.brain.learn([board_position], [valuation])

    def receive_result(self, moves, reward):
        board_positions = []
        board = Board()
        valuations = []
        for move in moves:
            if move.mover.token == self.token:
                board_position = np.array(board.positions).flatten()
                board_position = board_position * self.token
                board_positions.append(copy.copy(board_position))

                other_values = (1. - reward) / 8.
                valuation = [other_values] * 9
                valuation[move.flat_position()] = reward
                valuations.append(valuation)
            board.update(move)

        self.brain.learn(board_positions, valuations)
