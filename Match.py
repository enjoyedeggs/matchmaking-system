import Team as Te


class Match(object):
    teams = {'team1': Te.Team(), 'team2': Te.Team()}
    idCounter = 0

    def __init__(self, team1=-1, team2=-1):
        teams = {team1, team2}
        Match.idCounter += 1
        self.id = Match.idCounter

    def getMatchMMR(self):
        return self.teams['team1'].getTeamMMR() + self.teams['team2'].getTeamMMR()

    def __str__(self):
        print("test")
