"""
Deprecated Code.

def tft_dep(*args, **kwargs):
    OthersMemory = kwargs['memory']
    config = kwargs['config']
    dirtyBetrayal = 0
    for playerMemory in OthersMemory:
        if len(playerMemory.memory) > 0 and playerMemory.memory[-1] == 'D':
            dirtyBetrayal += 1
    return 'D' if dirtyBetrayal >= config['number of defections'] else 'C'

"""
def getChars(*args):
    return [''.join(arg.memory[-1:]) for arg in args]


def tft(*args, config, CalledFromRun=False, **kwargs):
    if CalledFromRun:
        return 'D' if getChars(*kwargs['self'].OtherPrisoners).count('D') >= config['number of defections'] else 'C'
    return 'D' if getChars(*args).count('D') >= config['number of defections'] else 'C'


if __name__ == '__main__':
    exit()  # won't work how intended since I changed some stuff, may fix later.
    string1 = ['CDDCDCDCDCCC', 'CDDCDCDCDCCD', 'CDDCDCDCDCDC', 'CDDCDCDCDCDD']
    string2 = ['CC', 'CD', 'DC', 'DD']
    string3 = ['C', 'D']
    string4 = []
    string5 = ['CDDCDCDCDCCC', 'CDDCDCDCDCCD', 'CDDCDCDCDCDC', 'CDDCDCDCDCCD']

    print(tft(config={'number of defections': 1}, *string1))
    print(tft(config={'number of defections': 1}, *string2))
    print(tft(config={'number of defections': 1}, *string3))
    print(tft(config={'number of defections': 1}, *string4))
    print(tft(config={'number of defections': 1}, *string5))
