class PrisonersDilemma:
    def __init__(self, *args, **kwargs):
        self.config = kwargs['config']
        self.prisoners = [arg for arg in args]

    def addPrisoner(self, strategy):
        self.prisoners.append(strategy)

    def run(self, numberOfIterations=1, *args):
        if self.config['iterations'] != -1:
            for _ in range(self.config['iterations']):
                moves = []
                for prisoner in self.prisoners:
                    moves.append(prisoner.run(*args))

                for num, prisoner in enumerate(self.prisoners):
                    prisoner.newMemory(moves[num])
                    print(f"{prisoner.nameOfStrategy}: \t{prisoner.allMoves}")
        else:
            while True:
                moves = []
                for prisoner in self.prisoners:
                    moves.append(prisoner.run(*args))

                for num, prisoner in enumerate(self.prisoners):
                    prisoner.newMemory(moves[num])
                    print(f"{prisoner.nameOfStrategy}: \t{prisoner.allMoves}")
