class PlayerQueueManager(object):

    def __init__(self):
        self.PlayerQueue = []

    def insertPlayer(self, player):
        self.PlayerQueue.insert(0, player)

    def removePlayer(self):
        if (self.PlayerQueue):
            return self.PlayerQueue.pop()

    def insertPlayerPriority(self, priorityPercentage, player):
        self.PlayerQueue.insert((len(self.PlayerQueue) / (priorityPercentage / 100)), player)

    def isEmpty(self):
        return len(self.PlayerQueue) == 0