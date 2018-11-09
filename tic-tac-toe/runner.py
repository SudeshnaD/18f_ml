from ai_brain import AIBrain
from human_brain import HumanBrain
from game import Game
import csv

N_RUNS = 2

experiment_name = "dense"
brain = AIBrain(experiment_name)
brain2 = HumanBrain()

with open("{filename}.csv".format(filename=experiment_name), 'ab') as csvfile:
    csv_writer = csv.writer(csvfile)

    for i in range(N_RUNS):
        print "Game #{num}".format(num=i)
        game = Game(brain, brain)
        game.start()
        if game.winner:
            csv_writer.writerow([game.winner, game.invalid_moves])
        else:
            csv_writer.writerow(["XXX", game.invalid_moves])

    print "\n\n\n"

brain.save()
