from ai_brain import AIBrain
from static_brain import StaticBrain
from human_brain import HumanBrain
from game import Game
import csv

N_EPOCHS = 10000
N_RUNS = 10

experiment_name = "dense"
static_brain = StaticBrain(experiment_name)
learning_brain= AIBrain(experiment_name)
brains = [static_brain, learning_brain]

with open("{filename}.csv".format(filename=experiment_name), 'ab') as csvfile:
    csv_writer = csv.writer(csvfile)

    for j in xrange(N_EPOCHS):
        static_brain.load_weights()
        brain1 = brains[j % 2]
        brain2 = brains[((j + 1) % 2)]
        for i in xrange(N_RUNS):
            print "Game #{num}".format(num=i)
            print brain1.__class__.__name__
            print brain2.__class__.__name__
            game = Game(brain1, brain2)
            game.start()
            if game.winner is not None:
                ai_did_win = game.winner
                if game.player1.brain == static_brain:
                    ai_did_win = ai_did_win * -1
                csv_writer.writerow([ai_did_win, game.invalid_moves])
            else:
                csv_writer.writerow(["XXX", game.invalid_moves])

        print "\n\n\n"

        learning_brain.save()
