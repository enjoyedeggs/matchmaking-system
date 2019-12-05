
class PlayerQueueManager(object):
    PlayerQueue = []

    def __init__(self):
        self.PlayerQueue = []


    def insertPlayer(self, player):
        self.PlayerQueue.insert(0, player)

    def removePlayer(self):
        return self.PlayerQueue.pop()

    def insertPlayerPriority(self, priorityPercentage, player):
        self.PlayerQueue.insert((len(self.PlayerQueue)/(priorityPercentage/100)), player)