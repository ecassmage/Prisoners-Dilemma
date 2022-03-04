import copy


class Strategy:
    def __init__(self, *args, **kwargs):
        self.nameOfStrategy = kwargs.get('name', None)

        self.config = kwargs.get('config', None)

        self.target = kwargs.get('target', None)

        self.args = args        # Store the  args  for later
        self.kwargs = kwargs    # Store the kwargs for later
        self.memory = []
        self.allMoves = []
        self.OtherPrisoners = []

    def run(self, *args):
        return self.target(self=self, CalledFromRun=True, *args, *self.args, **self.kwargs)

    def addPrisoner(self, other):
        self.OtherPrisoners.append(other)
        other.OtherPrisoners.append(self)

    def newMemory(self, newMove, cleanup_behind=True):
        self.memory.append(newMove)

        if cleanup_behind:
            if len(self.memory) > self.config['memory'] > -1:
                self.memory.pop(0)
            self.allMoves.append(newMove)

    def SetupMemorySet(self):
        pass

    def getMemory(self):
        return self.memory

    def getCopyOfMemory(self):
        return copy.copy(self.memory)

    def getAllMemories(self):
        return tuple(memory.getMemory() for memory in self.OtherPrisoners)  # apparently python is ludicrously bad with memory, a lot worse then I thought at least so lets use tuples instead of lists.

    def setMemory(self, memory):
        self.memory = copy.copy(memory)

    def __len__(self):
        return len(self.memory)
