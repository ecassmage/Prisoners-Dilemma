"""

Runs the program. Already setup to do the task.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.0.1
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


def printScore(exhaustiveSearch, config):
    if config['debug']:
        print("       " + '_' * (exhaustiveSearch.waterTesting if type(exhaustiveSearch.waterTesting) is int else len(exhaustiveSearch.waterTesting)) + " <- practice length")
        print(f"ES:    {exhaustiveSearch}\nother: {''.join(exhaustiveSearch.others_allMemory)}")

    es_score = exhaustiveSearch.calculate_score(exhaustiveSearch.allMemory, exhaustiveSearch.others_allMemory)
    other_score = exhaustiveSearch.calculate_score(exhaustiveSearch.others_allMemory, exhaustiveSearch.allMemory)
    length = len('Exhaustive Search Average: ')
    print()
    print(f"Score For {'Exhaustive Search: '.ljust(length, ' ')} {es_score}")
    print(f"Score For {f'{exhaustiveSearch.name}: '.ljust(length, ' ')} {other_score}")
    print(f"Score For {'Exhaustive Search Average: '.ljust(length, ' ')} {es_score / config['iterations']}")

    print(f"Score For {f'{exhaustiveSearch.name} Average: '.ljust(length, ' ')} {other_score / config['iterations']}")


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
    printScore(exhaustiveSearch, config)


if __name__ == '__main__':
    print("Start")
    main()
