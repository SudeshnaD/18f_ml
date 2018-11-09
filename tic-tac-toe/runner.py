from ai_brain import AIBrain
from game import Game

brain = AIBrain("dense")

for i in range(100):
    print "{num}\r".format(num=i)
    ttt = Game(brain, brain)
    ttt.start()

brain.save()
