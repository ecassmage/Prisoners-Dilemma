"""
Deprecated Code.

def tf2t_dep(*args, **kwargs):
    OthersMemory = kwargs['memory']
    config = kwargs['config']
    dirtyBetrayal = 0
    for playerMemory in OthersMemory:
        if len(playerMemory.memory) > 1 and playerMemory.memory[-2] == 'D' == playerMemory.memory[-1]:
            dirtyBetrayal += 1
    return 'D' if dirtyBetrayal >= config['number of defections'] else 'C'
"""


def getChars(*args):
    return [''.join(arg.memory[-2:]) for arg in args]


def tf2t(*args, config, CalledFromRun=False, **kwargs):
    if CalledFromRun:
        return 'D' if getChars(*kwargs['self'].OtherPrisoners).count('DD') >= config['number of defections'] else 'C'
    return 'D' if getChars(*args).count('DD') >= config['number of defections'] else 'C'


class A:
    def __init__(self, string):
        self.memory = string


if __name__ == '__main__':
    # exit()  # won't work how intended since I changed some stuff, may fix later.
    string1 = [A('CDDCDCDCDCCC'), A('CDDCDCDCDCCD'), A('CDDCDCDCDCDC'), A('CDDCDCDCDCDD')]
    string2 = [A('CC'), A('CD'), A('DC'), A('DD')]
    string3 = [A('C'), A('D')]
    string4 = []
    string5 = [A('CDDCDCDCDCCC'), A('CDDCDCDCDCCD'), A('CDDCDCDCDCDC'), A('CDDCDCDCDCCD')]

    print(tf2t(config={'number of defections': 1}, *string1))
    print(tf2t(config={'number of defections': 1}, *string2))
    print(tf2t(config={'number of defections': 1}, *string3))
    print(tf2t(config={'number of defections': 1}, *string4))
    print(tf2t(config={'number of defections': 1}, *string5))
