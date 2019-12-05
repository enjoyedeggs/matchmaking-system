import Team as Te


class Match(object):
    idCounter = 0

    def __init__(self):
        team1 = Te.Team()
        team2 = Te.Team()
        self.teams = {'team1': team1, 'team2': team2}
        Match.idCounter += 1
        self.id = Match.idCounter

    def insertPlayer(self, player):
        if(self.teams['team1'].insertPlayer(player)):
            return True
        elif(self.teams['team2'].insertPlayer(player)):
            return True
        return False
    
    def removePlayerByID(self, id):
        if(self.teams['team1'].removePlayerByID(id)):
            return True
        elif(self.teams['team2'].removePlayerByID(id)):
            return True
        return False
    
    def evenTeamMMR(self):
        return #placeholder to be finished later

    def getAverageMatchMMR(self):
        return (self.teams['team1'].getAverageTeamMMR() + self.teams['team2'].getAverageTeamMMR()) / 2

    def getMaximumMatchMMR(self):
        if(self.teams['team2'].getMaximumMMR() == -1):
            return self.teams['team1'].getMaximumMMR()
        return self.teams['team1'].getMaximumMMR() if (self.teams['team1'].getMaximumMMR() < self.teams['team2'].getMaximumMMR()) else self.teams['team2'].getMaximumMMR()

    def getMinimumMatchMMR(self):
        if (self.teams['team2'].getMinimumMMR() == -1):
            return self.teams['team1'].getMinimumMMR()
        return self.teams['team1'].getMinimumMMR() if (self.teams['team1'].getMinimumMMR() > self.teams['team2'].getMinimumMMR()) else self.teams['team2'].getMinimumMMR()

    def getMaximumMatchDivision(self):
        if (self.teams['team2'].getMaximumDivision() == -1):
            return self.teams['team1'].getMaximumDivision()
        return self.teams['team1'].getMaximumDivision() if (
                    self.teams['team1'].getMaximumDivision() < self.teams['team2'].getMaximumDivision()) else self.teams[
            'team2'].getMaximumDivision()

    def getMinimumMatchDivision(self):
        if (self.teams['team2'].getMinimumDivision() == -1):
            return self.teams['team1'].getMinimumDivision()
        return self.teams['team1'].getMinimumDivision() if (
                    self.teams['team1'].getMinimumDivision() > self.teams['team2'].getMinimumDivision()) else self.teams[
            'team2'].getMinimumDivision()

    def isMatchFull(self):
        return (self.teams['team1'].isTeamFull() and self.teams['team2'].isTeamFull())

    def __str__(self):
        return "Match ID: " + str(self.id) + "\n" + self.teams['team1'].__str__() + "\n" + self.teams['team2'].__str__() + "\n"
