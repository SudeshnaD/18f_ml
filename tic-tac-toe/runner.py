from ai_brain import AIBrain
from static_brain import StaticBrain
from human_brain import HumanBrain
from game import Game
import csv

N_EPOCHS = 100
N_RUNS = 10

experiment_name = "dense"
static_brain = StaticBrain(experiment_name)
learning_brain= AIBrain(experiment_name)
game = Game(static_brain, learning_brain)

with open("{filename}.csv".format(filename=experiment_name), 'ab') as csvfile:
    csv_writer = csv.writer(csvfile)

    for j in range(N_EPOCHS):
        static_brain.load_weights()
        for i in range(N_RUNS):
            print "Game #{num}".format(num=i)
            game = Game(game.player2.brain, game.player1.brain)
            game.start()
            if game.winner:
                csv_writer.writerow([game.winner, game.invalid_moves])
            else:
                csv_writer.writerow(["XXX", game.invalid_moves])

        print "\n\n\n"

        learning_brain.save()
