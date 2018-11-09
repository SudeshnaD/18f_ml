from ai_brain import AIBrain
from game import Game

brain = AIBrain("dense")

for i in range(100):
    game = Game(brain, brain)
    game.start()
    print "{num}, {winner}, {invalid_moves}".format(num=i, winner=game.winner, invalid_moves=game.invalid_moves)

brain.save()
