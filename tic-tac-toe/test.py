from ai_brain import AIBrain
from board import Board

experiment_name = "dense"
brain = AIBrain(experiment_name)
board = Board()

brain.prompt(board, 1)
