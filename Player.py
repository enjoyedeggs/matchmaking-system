class Player(object):

    def __init__(self, username="null", summonerID="null", MMR=-1, wins=-1, losses=-1, division=-1, divisionPoints=-1, tier=-1, honor=-1):
        self.username = username
        self.summonerID = summonerID
        self.MMR = MMR
        self.wins = wins
        self.losses = losses
        self.division = division
        self.divisionPoints = divisionPoints
        self.tier = tier
        self.honor = honor

    def getMMR(self):
        return self.MMR

    def getDivision(self):
        return self.division
    
    def getTier(self):
        return self.tier

    def getTotalDivision(self):
        return (tier * 4) + division

    def getSummonerID(self):
        return self.summonerID

    def __str__(self):
        return '{' + self.username + ': MMR_' + str(self.MMR) + '}'
