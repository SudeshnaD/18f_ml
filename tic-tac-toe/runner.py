from human_brain import HumanBrain
from ai_brain import AIBrain
from game import Game

brain = AIBrain("dense")
ttt = Game(brain, brain)
ttt.start()

brain.save()
