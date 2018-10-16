from human_brain import HumanBrain
from game import Game

brain1 = HumanBrain()
brain2 = HumanBrain()
ttt = Game(brain1, brain2)
ttt.start()
