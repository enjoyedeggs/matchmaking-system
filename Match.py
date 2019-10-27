import Team as Te


class Match(object):
    teams = {'team1': Te.Team(), 'team2': Te.Team()}

    def __init__(self, team1=-1, team2=-1):
        teams = {team1, team2}

    def __str__(self):
        print("test")
