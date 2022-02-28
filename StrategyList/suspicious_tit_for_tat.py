"""
Deprecated Code.

def stft_dep(*args, **kwargs):
    OthersMemory = kwargs['memory']
    config = kwargs['config']
    dirtyBetrayal = 0
    for playerMemory in OthersMemory:
        if len(playerMemory.memory) == 0:
            return 'D'
        if len(playerMemory.memory) > 0 and playerMemory.memory[-1] == 'D':
            dirtyBetrayal += 1

    return 'D' if dirtyBetrayal >= config['number of defections'] else 'C'

"""
def getChars(*args):
    return [''.join(arg.memory[-1:]) for arg in args]


def stft(*args, config, CalledFromRun=False, **kwargs):

    if CalledFromRun:
        storage = getChars(*kwargs['self'].OtherPrisoners)
        return 'D' if storage.count('D') >= config['number of defections'] else 'D' if storage.count('') == len(storage) else 'C'
    storage = getChars(*args)
    return 'D' if storage.count('D') >= config['number of defections'] else 'D' if storage.count('') == len(storage) else 'C'  # good ol' single line if else if else line


if __name__ == '__main__':
    exit()  # won't work how intended since I changed some stuff, may fix later.
    string1 = ['CDDCDCDCDCCC', 'CDDCDCDCDCCD', 'CDDCDCDCDCDC', 'CDDCDCDCDCDD']
    string2 = ['CC', 'CD', 'DC', 'DD']
    string3 = ['C', 'D']
    string4 = []
    string5 = ['CDDCDCDCDCCC', 'CDDCDCDCDCCD', 'CDDCDCDCDCDC', 'CDDCDCDCDCCD']
    string6 = ['CDDCDCDCDCCC', 'CDDCDCDCDCCC', 'CDDCDCDCDCDC', 'CDDCDCDCDCCC']
    string7 = ['CC', 'CC', 'DC', 'DC']
    string8 = ['C', 'C', 'D', 'C']
    string9 = ['C', 'D', 'D', 'C']

    print(stft(config={'number of defections': 1}, *string1))
    print(stft(config={'number of defections': 1}, *string2))
    print(stft(config={'number of defections': 1}, *string3))
    print(stft(config={'number of defections': 1}, *string4))
    print(stft(config={'number of defections': 1}, *string5))
    print(stft(config={'number of defections': 1}, *string6))
    print(stft(config={'number of defections': 1}, *string7))
    print(stft(config={'number of defections': 2}, *string8))
    print(stft(config={'number of defections': 2}, *string9))
