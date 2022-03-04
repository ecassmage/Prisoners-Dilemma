"""

tit for tat. The functions of choosing the next character. I know, very complex.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.0.0
Since 1.0.0
"""


def tft(string):
    return 'C' if len(string) == 0 else string[-1]


if __name__ == '__main__':
    print(f"{tft('CC')}")
    print(f"{tft('CD')}")
    print(f"{tft('DC')}")
    print(f"{tft('DD')}")
    print(f"{tft('')}")
    print(f"{tft('C')}")
    print(f"{tft('D')}")
    print(f"{tft('DDD')}")
    print(f"{tft('CCC')}")
    print(f"{tft('CDC')}")
    print(f"{tft('DDC')}")
    print(f"{tft('DCD')}")
    pass
