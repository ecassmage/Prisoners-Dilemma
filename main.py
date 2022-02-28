"""
This runs mainly like this.
main.py (will use fileOpener.py here to read and modify the config.json file)
PrisonersDilemma.py
Strategy.py
StrategyList (will be whatever is injected into Strategy)
score_calculate.py

It should be modifiable to an extent though considering how much I was messing around with this, I wouldn't be surprised if there were plenty of bugs hidden away.

Name Prisoners Dilemma
Developer: Evan Morrison
Version: 1.0.1
Since: 1.0.0

"""


from StrategyList import exhaustive_search, tit_for_tat, tit_for_two_tat, suspicious_tit_for_tat, score_calculate
import PrisonersDilemma
import Strategy
import fileOpener


def getFunctionCall(string: str):
    functions = {'es': exhaustive_search.exhaustive_search, 'tft': tit_for_tat.tft, 'tf2t': tit_for_two_tat.tf2t, 'stft': suspicious_tit_for_tat.stft}
    return functions[string]


def setup_game(config):
    prisonersDilemma = PrisonersDilemma.PrisonersDilemma(config=config)
    for player in config['players']:
        temp = Strategy.Strategy(target=getFunctionCall(config['players'][player]), config=config, name=config['players'][player])
        for prisoner in prisonersDilemma.prisoners:
            prisoner.addPrisoner(temp)  # should add all others to each others OtherPrisoners variable
        prisonersDilemma.addPrisoner(temp)  # should neatly store them all in a box.
    return prisonersDilemma


def calculateAverages(PD, config):
    values = score_calculate.calculateValues(*[prisoner.allMoves for prisoner in PD.prisoners], config=config)
    for number, prisoner in enumerate(PD.prisoners):
        print(f"prison {number} \tUsing Strategy: {prisoner.nameOfStrategy.ljust(6, ' ')} \thad average of: {round(values[number] / len(prisoner.allMoves), 3)}")
    pass


def main():
    config = fileOpener.getConfig()
    PD = setup_game(config)
    PD.run()
    for prisoner in PD.prisoners:
        print(f"{prisoner.nameOfStrategy}: \t{prisoner.allMoves}")
    calculateAverages(PD, config)


if __name__ == "__main__":
    main()
    pass
