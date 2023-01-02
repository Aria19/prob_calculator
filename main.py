# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(
    hat=hat, 
    expected_balls={"yellow":2,
                    "blue":3,
                    "test":1}, 
    num_balls_drawn=20, 
    num_experiments=100)
actual = probability
expected = 1.0
print("actual", actual)
print("expected", expected)
