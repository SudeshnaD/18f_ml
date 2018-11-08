from human_brain import HumanBrain
from ai_brain import AIBrain
from game import Game

brain1 = HumanBrain()
brain2 = AIBrain()
ttt = Game(brain1, brain2)
ttt.start()

brain2.learn(ttt)

brain2.save()
