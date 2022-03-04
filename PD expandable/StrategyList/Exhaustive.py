import Strategy
import math
from exhaustive_search import __exhaustive_search as exhaustion


class Exhaustive(Strategy.Strategy):
    """
    Time to waste as much memory as possible to do stuff like predicting the other persons next move.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.memoryChoices = []
        self.defectWeight = kwargs['config']['exhaustive settings'].get('defect weight', 0)        # my desire for the weights is so that it won't just look at the fact that if the others defecting is possible,
        self.cooperateWeight = kwargs['config']['exhaustive settings'].get('cooperate weight', 0)  # they will always do it.
        self.patternWeights = {}

    def minimax(self):
        for combination in exhaustion(depth=self.config['depth'], returnType=list):
            pass
        pass

    def collectPatterns(self):

        joinedMem = ''.join(self.getMemory())
        for pos in range(2, len(self)+1):
            self.patternWeights[f"{joinedMem[len(self) - pos:]}_{joinedMem[-1]}"] = self.patternWeights.get(f"{joinedMem[len(self) - pos:]}_{joinedMem[-1]}", 0) + 1
        pass

    def likelyHoodOfUsage(self):
        pass

    def __calculate_score(self, *args):
        arg = [list(element) for element in args]
        value = 0

        for charPos in range(min([len(x) for x in args])):

            defection = 0
            for stringPos in range(len(arg)):
                if arg[stringPos][charPos] == 'D':
                    defection += 1

            value += self.config[f'{defection} defect'].get('cooperation', -1) * self.cooperateWeight if arg[0][charPos] == 'C' \
                else self.config[f'{defection} defect'].get('defection', -1) * self.defectWeight

        return value


def sigmoid(number):
    return 1 / (1 + math.e**(3 - number))


def randomTest(ee):
    import random
    for i in range(100):
        ee.newMemory(random.choice(['C', 'D']))
        ee.collectPatterns()


if __name__ == '__main__':
    import FileOpener
    e = Exhaustive(config=FileOpener.getConfig(), target=None, name='name')
    randomTest(e)
    pass
    # print(sigmoid(5))
    pass
