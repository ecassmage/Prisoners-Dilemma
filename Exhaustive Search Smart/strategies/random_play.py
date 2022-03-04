"""

random play. chooses a random play.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.1.0
Since 1.1.0
"""

import random


def rand_play(string):
    """
    Returns a random choice, no rhyme or reason to it.

    :param string: Takes a string, but only because the others need a string.
    :return: returns character of choice.
    """
    return random.choice(['C', 'D'])
