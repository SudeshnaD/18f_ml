from human_brain import HumanBrain
from ai_brain import AIBrain
from game import Game

brain = AIBrain()
ttt = Game(brain, brain)
ttt.start()

brain.save()
