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
        move_recommendations = self.brain.prompt(board, self.token)
        print move_recommendations
        return Move(move_recommendations, self)

    def receive_invalid_move(self, board, move):
        board_position = np.array(board.positions).flatten()
        board_position = board_position * self.token

        other_values = np.array(move.recommendations)
        probability_residual = move.recommendations[move.flat_position] / 8.
        other_values = other_values + probability_residual
        valuation = other_values
        valuation[move.flat_position] = 0

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

                if reward == 1:
                    valuation = [0] * 9
                else:
                    probability_residual = move.recommendations[move.flat_position] / 8.
                    valuation = np.array(move.recommendations)
                    valuation = valuation + probability_residual
                valuation[move.flat_position] = reward
                valuations.append(valuation)
            board.update(move)

        self.brain.learn(board_positions, valuations)
