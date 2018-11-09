from ai_brain import AIBrain
from game import Game
import csv

experiment_name = "dense"
brain = AIBrain(experiment_name)

with open("{filename}.csv".format(filename=experiment_name), 'ab') as csvfile:
    csv_writer = csv.writer(csvfile)

    for i in range(10):
        # print "Game #{num}".format(num=i)
        game = Game(brain, brain)
        game.start()
        if game.winner:
            print "{num}, {winner}, {invalid_moves}".format(num=i, winner=game.winner, invalid_moves=game.invalid_moves)
            csv_writer.writerow([game.winner, game.invalid_moves])
        else:
            print "{num}, XXX, {invalid_moves}".format(num=i, invalid_moves=game.invalid_moves)

brain.save()
