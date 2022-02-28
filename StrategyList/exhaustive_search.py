try:
    import score_calculate
except ModuleNotFoundError:
    from StrategyList import score_calculate


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


def __exhaustive_search(*args, **kwargs):
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


def exhaustive_search(*args, CalledFromRun=False, **kwargs):
    """
    exhaustive_search will calculate the optimal strategy to defeat its opponents and would fail horribly if it didn't know what strategy its opponent was using.
    It does not know when the simulation will end so it will not be able to predict the end.
    (This will descend into chaos if too many are added the simulation
    :param args:
    :param CalledFromRun:
    :param kwargs:
    :return:
    """
    if not CalledFromRun:
        return 'C'
    OtherPrisoners = kwargs['self'].OtherPrisoners
    depth = kwargs['config']['depth']
    CopyMemoryForAllPrisoners = [kwargs['self'].getCopyOfMemory()] + [prisoner.getCopyOfMemory() for prisoner in OtherPrisoners]
    bestScored = []
    for ES_Combination in __exhaustive_search(depth=depth, *args, **kwargs, returnType=list):
        pass
        for character in ES_Combination:
            for num, prisoner in enumerate(OtherPrisoners):
                prisoner.newMemory(prisoner.target(config=kwargs['config'], self=prisoner, *prisoner.OtherPrisoners), False)
            kwargs['self'].newMemory(character, False)

        score = score_calculate.calculateValues(kwargs['self'].getMemory(), *[prisoner.getMemory() for prisoner in OtherPrisoners], config=kwargs['config'], singleVal=True)
        if len(bestScored) == 0 or score > bestScored[0]:
            bestScored = [score, [char for char in ES_Combination]]
            pass
        for num, copyOfMemory in enumerate(CopyMemoryForAllPrisoners):
            kwargs['self'].setMemory(copyOfMemory) if num == 0 else OtherPrisoners[num-1].setMemory(copyOfMemory)
    return bestScored[1][0]


"""
Deprecated Stuff


def exhaustive_search_dep(*args, **kwargs):
    OthersMemory = kwargs['memory']
    config = kwargs['config']
    memory = [a.memory for a in OthersMemory]
    bestChoice = None
    for element in __exhaustive_search(depth=len(args[0].getMemory()), *args, **kwargs, returnType=list):
        val = score_calculate.calculateValues(element, *memory, config=config, singleVal=True)
        if bestChoice is None or val > bestChoice[0]:
            bestChoice = [val, ''.join(element)]
    return bestChoice[-1][0] if bestChoice[-1] != '' else 'D'


def override(depth, returnType=None):
    returnType = str if returnType is None else returnType
    return __exhaustive_search(depth=depth, returnType=returnType)
"""


def main():
    pass


if __name__ == '__main__':
    main()
