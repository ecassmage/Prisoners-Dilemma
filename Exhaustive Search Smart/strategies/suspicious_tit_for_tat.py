"""

Suspicious tit for tat. The functions of choosing the next character. I know, very complex.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.0.0
Since 1.0.0
"""


def stft(string):
    return 'D' if len(string) == 0 else string[-1]


if __name__ == '__main__':
    print(f"{stft('CC')}")
    print(f"{stft('CD')}")
    print(f"{stft('DC')}")
    print(f"{stft('DD')}")
    print(f"{stft('')}")
    print(f"{stft('C')}")
    print(f"{stft('D')}")
    print(f"{stft('DDD')}")
    print(f"{stft('CCC')}")
    print(f"{stft('CDC')}")
    print(f"{stft('DDC')}")
    print(f"{stft('DCD')}")
    pass
