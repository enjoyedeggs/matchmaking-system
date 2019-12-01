import Player as Pl


class Team(object):
    players = {'player1': Pl.Player(), 'player2': Pl.Player(), 'player3': Pl.Player(), 'player4': Pl.Player(),
               'player5': Pl.Player()}

    def getTeamMMR(self):
        return self.players['player1'].getMMR() + self.players['player2'].getMMR() + self.players['player3'].getMMR() + \
               self.players['player4'].getMMR() + self.players['player5'].getMMR()

    def __str__(self):
        return '{' + str(self.players['player1']) + ', ' + str(self.players['player2']) + ', ' + str(
            self.players['player3']) + ', ' + str(self.players['player4']) + ', ' + str(self.players['player5']) + '}'
