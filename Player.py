
class Player(object):

    def __init__(self, username="null", summonerID="null", MMR=-1, wins=-1, losses=-1, division=-1, divisionPoints=-1,tier=-1, honor=-1):
        self.username = username
        self.summonerID = summonerID
        self.MMR = MMR
        self.wins = wins
        self.losses = losses
        self.division = division
        self.divisionPoints = divisionPoints
        self.tier = tier
        self.honor = honor