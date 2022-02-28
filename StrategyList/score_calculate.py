def getJsonFile(FileInfo):
    if FileInfo is None:
        import fileOpener
        return fileOpener.getConfig()
    return FileInfo


def calculateValues(*args, config=None, singleVal=False) -> list:
    """
    This can be used for 1 or more prisoners, 1 prisoner is dumb though. I have made it so it can take in n prisoners strategies and output
    the value of them each [prisoner_1, prisoner_2, prisoner_3, ..., prisoner_n]
    This will give the ability to more easily test different things without changing much.

    :param args: takes all of the prisoners strategies, can be hardcoded in or given as a list/tuple/equivalent, but needs a * left of variableName
    :param config: takes the config file, not necessary and will retrieve it if not passed up, but will take some extra space up for a bit so I thought it
           best to give option to pass it up, especially if there are modifications to it
    :param singleVal: just a thing, no need to worry about it.
    :return: returns all of the values the prisoners received like this -> [prisoner_1, prisoner_2, prisoner_3, ..., prisoner_n]. will always return a list
    """

    config = getJsonFile(config)['rewards']
    arg = [list(element) for element in args]
    values = [0] * len(arg)

    for charPos in range(min([len(x) for x in args])):

        defection = 0
        for stringPos in range(len(arg)):
            if arg[stringPos][charPos] == 'D':
                defection += 1

        for stringPos in range(len(arg)):
            values[stringPos] += config[f'{defection} defect'].get('cooperation', -1) if arg[stringPos][charPos] == 'C' else config[f'{defection} defect'].get('defection', -1)

    return values[0] if singleVal else values
