"""

average d. chooses next move based on averages with D being the tie breaker

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.1.0
Since 1.1.0
"""


def avgd(string):
    """
    Average d will find which character is used most and play that one, it will play D if they are equal

    :param string: takes a string of the Exhaustive searches moves
    :return: returns character it will play
    """
    return 'C' if list(string).count('C') >= int(len(string) / 2) else 'D'
