"""

Runs the program. Already setup to do the task.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.0.0
Since 1.0.0
"""


import FileOpener
from strategies import tit_for_tat, tit_for_two_tat, suspicious_tit_for_tat
import Exhaustive


def getFunction(string):
    """
    Stores the different strategy functions for use in the program.
    :param string: takes a string which identifies which strategy will be needed.
    :return: returns the function requested.
    """
    return {'tft': tit_for_tat.tft, 'tf2t': tit_for_two_tat.tf2t, 'stft': suspicious_tit_for_tat.stft}[string]


def main():
    """
    Does those things only a main function can do because all other functions and methods are too scared.
    :return: returns nothing.
    """
    config = FileOpener.getConfig()
    exhaustiveSearch = Exhaustive.Exhaustive(config=config, target=getFunction(config['player 2']), name=config['player 2'])
    for _ in range(config['iterations']):
        charForES = exhaustiveSearch.run()
        charForTFT = exhaustiveSearch.target(''.join(exhaustiveSearch.memory))
        exhaustiveSearch.addRoundMemory(charForES, charForTFT)
        if config['debug'] and _ % 100 == 0:
            print(f"Iteration: {_}")
    print("       " + '_' * config['es settings']['testing the water'])
    print(f"ES:    {exhaustiveSearch}\nother: {''.join(exhaustiveSearch.others_allMemory)}")


if __name__ == '__main__':
    print("Start")
    main()
