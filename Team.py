import Player as Pl

class Team(object):

    def __init__(self):
        self.players = {'player1': Pl.Player(), 'player2': Pl.Player(), 'player3': Pl.Player(), 'player4': Pl.Player(),
               'player5': Pl.Player()}

    def insertPlayer(self, player):
        for p in self.players:
            if(self.players[p].getSummonerID() == "null"):
                self.players[p] = player
                return True
        return False

    def removePlayerByID(self, id):
        for p in self.players:
            if(self.players[p].getSummonerID() == id):
                self.players[p] = Pl.Player()
                return True
        return False
    
    def isTeamFull(self):
        for player in self.players:
            if(self.players[player].getSummonerID() == 'null'):
                return False
        return True

    def getAverageTeamMMR(self):
        return (self.players['player1'].getMMR() + self.players['player2'].getMMR() + self.players['player3'].getMMR() +
                self.players['player4'].getMMR() + self.players['player5'].getMMR()) / 5

    def getMinimumMMR(self):
        minimumMMR = self.players['player1'].getMMR()
        for player in self.players:
            if(self.players[player].getMMR() > 0 and self.players[player].getMMR() < minimumMMR):
                minimumMMR = self.players[player].getMMR()
        return minimumMMR

    def getMaximumMMR(self):
        maximumMMR = self.players['player1'].getMMR()
        for player in self.players:
            if(self.players[player].getMMR() > 0 and self.players[player].getMMR() > maximumMMR):
                maximumMMR = self.players[player].getMMR()
        return maximumMMR

    def getMinimumDivision(self):
        minimumDivision = self.players['player1'].getDivision()
        for player in self.players:
            if(self.players[player].getDivision() > 0 and self.players[player].getDivision() < minimumDivision):
                minimumDivision = self.players[player].getDivision()
        return minimumDivision

    def getMaximumDivision(self):
        maximumDivision = self.players['player1'].getDivision()
        for player in self.players:
            if(self.players[player].getDivision() > 0 and self.players[player].getDivision() > maximumDivision):
                maximumDivision = self.players[player].getDivision()
        return maximumDivision

    def __str__(self):
        return '{' + str(self.players['player1']) + ', ' + str(self.players['player2']) + ', ' + str(
            self.players['player3']) + ', ' + str(self.players['player4']) + ', ' + str(self.players['player5']) + '}'
