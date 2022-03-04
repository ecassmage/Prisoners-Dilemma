"""

This will when setup and run (setup already through main.py), it will attempt to make the most optimal choices based on a neural network.
Will utilize the config.json file to set some things up and can be modified.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.1.0
Since 1.0.0
"""


import random


class Exhaustive:
    """
    Will likely build biases that screw it over, however it should be able to predict predictable strategies like tft and while maybe not beat them, it will be able to start playing smarter by the end.
    """
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', None)

        self.config = kwargs['config']
        self.memory = []
        self.allMemory = []
        self.patternWeights = {}
        self.verificationOfCorrectness = None  # [this set of moves, expected move]

        self.others_memory = []
        self.others_allMemory = []
        self.target = kwargs['target']

        self.nextMove = ''
        self.other_nextMove = ''

        self.waterTesting = self.config['es settings']['testing the water']

    def run(self):
        """
        This runs the entire iteration.
        Will first check if program is still in the testing phase and will then move on to if it will just pick randomly or if it will attempt to predict the opponents next move.
        :return: returns the chosen character whether it be C or D
        """
        scores = []
        if len(self) < (self.waterTesting if type(self.waterTesting) is int else len(self.waterTesting)):
            if type(self.waterTesting) is int:
                return random.choice(['C', 'D'])
            else:
                return self.waterTesting[len(self)]

        for combination in exhaustive_search(depth=self.config['depth'], returnType=str):
            scoreReceived, expectedNextMove = self.likelyHoodOfUsage(combination)
            scores.append([scoreReceived, combination, expectedNextMove])

        bestTemp = max(scores, key=lambda x: x[0])
        self.verificationOfCorrectness = bestTemp[2]
        return bestTemp[1][0]

    def addRoundMemory(self, self_choice, others_choice):
        """
        adds the rounds choices to the memory, will also change the weights based on the accuracy of the predictions.
        :param self_choice: the choice which the Exhaustive search chose upon.
        :param others_choice: the choice which the opponent chose upon.
        :return: returns nothing.
        """
        self.__changeWeights()
        self.newMemory(self_choice)
        self.others_newMemory(others_choice)

    def newMemory(self, newMove, cleanup_behind=True):
        """
        sets the new memory for the Exhaustive search
        :param newMove: the current iterations chosen move.
        :param cleanup_behind: boolean variable for if memory is finite and should be wiped if too large.
        :return: returns nothing.
        """
        self.memory.append(newMove)
        self.allMemory.append(newMove)
        if cleanup_behind and len(self.memory) > self.config['memory'] > -1:
            self.memory.pop(0)

    def others_newMemory(self, newMove, cleanup_behind=True):
        """
        sets the new memory for the opponent.
        :param newMove: the current iterations chosen move.
        :param cleanup_behind: boolean variable for if memory is finite and should be wiped if too large.
        :return: returns nothing.
        """
        self.others_memory.append(newMove)
        self.others_allMemory.append(newMove)
        if cleanup_behind and len(self.others_memory) > self.config['memory'] > -1:
            self.others_memory.pop(0)

    def __changeWeights(self):
        """
        an internal method which will run other methods to determine weight changes.
        will call lowerWeights(self) should it predict incorrectly.
        :return: returns nothing.
        """
        # and len(self) >= self.config['es settings']['testing the water']
        if len(self.others_memory) > 0 and (self.waterTesting > len(self) if type(self.waterTesting) is int else len(self.waterTesting) > len(self)) and self.verificationOfCorrectness != self.others_memory[-1]:
            self.lowerWeights()
        self.collectPatterns()

    def lowerWeights(self):
        """
        Lowers the Exhaustive search' weights given that if it gets here, then it predicted incorrectly.
        :return: returns nothing.
        """
        # if self.verificationOfCorrectness is None:
        #      return
        joinedMem = ''.join(self.memory)
        for pos in range(2, len(self.memory) + 1):
            self.patternWeights[f"{joinedMem[len(self.memory) - pos:]}_{self.verificationOfCorrectness}"] = self.patternWeights.get(f"{joinedMem[len(self.memory) - pos:]}_{self.verificationOfCorrectness}", 0) - 1

    def collectPatterns(self):
        """
        Collects patterns found from the memory. Will only find patters as far back as it can remember but will remember these patterns forever. (or until the program closes, I am not writing this all to file)
        :return: returns nothing.
        """
        joinedMem = ''.join(self.memory)
        for pos in range(2, len(self.memory) + 1):
            self.patternWeights[f"{joinedMem[len(self.memory) - pos:]}_{self.others_allMemory[-1]}"] = self.patternWeights.get(f"{joinedMem[len(self.memory) - pos:]}_{self.others_allMemory[-1]}", 0) + 1

    # def getPatternsSetOfString(self, string):
    #     stringMem = ''.join(self.memory) + string
    #     setOfData = {}
    #     for position in range(len(self.memory), len(stringMem)):
    #         for numberOffSet in range(1, 1 + len(self.memory)):
    #             stringLookUp = stringMem[position - numberOffSet:position]

    def likelyHoodOfUsage(self, string):
        """
        calculates and then generates the most likely counter the opponent will make.
        Uses sigmoid!!!

        :param string: contains a set of moves of length=(depth in config.json file).
        :return: returns the score that this pairing will receive and the opponent move set.
        """
        string_generated_likely_hood_value = 0
        stringGenerated = ''
        stringMem = ''.join(self.memory) + string

        for position in range(len(self.memory), len(stringMem)):

            likely_hood_of_choosing_character = 0
            likely_hood_of_choosing_character_value = 0

            for numberOffSet in range(1, 1 + len(self.memory)):
                stringLookUp = stringMem[position - numberOffSet:position]
                likely_hood_of_choosing_character += self.patternWeights.get(f"{stringLookUp}_C", 0) - self.patternWeights.get(f"{stringLookUp}_D", 0)  # positive means to choose cooperate, negative means to defect.
                likely_hood_of_choosing_character_value += (sigmoid(abs(likely_hood_of_choosing_character)) * sigmoid(1 + len(self.memory) - numberOffSet))

            stringGenerated += 'C' if likely_hood_of_choosing_character > 0 else self.config['es settings']["default state"] if likely_hood_of_choosing_character == 0 else 'D'
            string_generated_likely_hood_value += sigmoid(abs(likely_hood_of_choosing_character)) * likely_hood_of_choosing_character_value
        score = self.calculate_score(string, stringGenerated)
        return score, stringGenerated[0]

    def calculate_score(self, selfString: str, otherString: str):
        """
        calculates the score of this pairing of moves.
        Score is based on weights from config.json

        :param selfString: the Exhaustive search move set.
        :param otherString: the opponents predicted move set.
        :return: returns the score generated.
        """
        score = 0
        for index in range(len(min([selfString, otherString], key=len))):  # why find the smallest despite them supposed to be the same size, Dunno.
            score += self.config['rewards'][f"{(selfString[index], otherString[index]).count('D')} defect"]['cooperation' if selfString[index] == 'C' else 'defection']
        return score

    def __len__(self):
        return len(self.allMemory)

    def __str__(self):
        return ''.join(self.allMemory)


def __addChange(string: list, breakIfAllD):
    """
    switches the 'bits' of the combination to go to the next set.
    :param string: takes the currently built combination
    :param breakIfAllD: a breaker for differentiating between going another bit deep or stopping at this point
    :return: returns True or False, depending on need. True for if break is required, False if not required
    """
    for num, char in enumerate(reversed(string)):
        if char == 'C':
            string[len(string)-1-num] = 'D'
            return False
        else:
            string[len(string) - 1 - num] = 'C'
    if breakIfAllD < 0 or breakIfAllD > len(string):
        string.append('C')
        return False
    return True


def __chooseYield(string, returnType):
    """
    This is for formatting purposes, not really important
    """
    if returnType == str:
        return ''.join(string)
    elif returnType == list:
        return string


def exhaustive_search(*args, **kwargs):
    """
    Generator which will build every combination that match certain specification, for exhaustive search.

    :param args: NOTHING, just here for the ride
    :param kwargs: key word arguments like the config file and stuff like depth length and if it needs to go From combination C to D...D or just CCC to DDD
    :return: returns / yields the next combination in the iteration loop.
    """
    returnType = kwargs.get('returnType', str)
    depth = kwargs.get('depth', kwargs.get('config', {'depth': 0})['depth'])  # this roundabout way is because I am avoiding exceptions so as to not use try: except: for some reason.

    if depth <= -1:
        string = ['C']
        yield __chooseYield(string, returnType)
        while True:
            __addChange(string, depth)
            yield __chooseYield(string, returnType)
    else:
        string = ['C'] * depth
        yield __chooseYield(string, returnType)
        while True:
            if __addChange(string, depth):
                return __chooseYield(string, returnType)
            yield __chooseYield(string, returnType)


def sigmoid(number):
    """
    Sigmoids!!!
    :param number: takes a number for input x in the sigmoid
    :return: returns the calculated sigmoid.
    """
    import math
    return 1 / (1 + math.e**(4 - (abs(number)/2)))


def randomTest(e):
    """Tests"""
    import random
    for i in range(100):
        e.newMemory(random.choice(['C', 'D']))
        e.others_newMemory(random.choice(['C', 'D']))
        e.collectPatterns()


def test():
    """More Tests"""
    import FileOpener
    e = Exhaustive(config=FileOpener.getConfig(), target=None, name='name')
    randomTest(e)
    e.run()
    # for line in e.patternWeights:
    #     print(f"{line}: {e.patternWeights[line]}")
    pass


if __name__ == '__main__':
    test()
