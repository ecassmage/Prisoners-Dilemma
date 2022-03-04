"""

tit for two tat. The functions of choosing the next character. I know, very complex.

Name: Prisoners Dilemma, Exhaustive Search w/ basic neural network
Developer: Evan Morrison
Version 1.1.0
Since 1.0.0
"""


def tf2t(string):
    return 'C' if len(string) < 2 else 'D' if string[-2:] == 'DD' else 'C'


if __name__ == '__main__':
    print(f"{tf2t('CC')}")
    print(f"{tf2t('CD')}")
    print(f"{tf2t('DC')}")
    print(f"{tf2t('DD')}")
    print(f"{tf2t('')}")
    print(f"{tf2t('C')}")
    print(f"{tf2t('D')}")
    print(f"{tf2t('DDD')}")
    print(f"{tf2t('CCC')}")
    print(f"{tf2t('CDC')}")
    print(f"{tf2t('DDC')}")
    print(f"{tf2t('DCD')}")
    pass
