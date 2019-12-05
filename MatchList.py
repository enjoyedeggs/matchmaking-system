import Match as Ma
import Player as Pl
import MatchListManager as Mlm

class MatchList(object):

    def __init__(self, matchListManager, maxMMRDifference = 1000, maxDivisionDifference = 4):
        self.matchList = []
        self.maxMMRDifference = maxMMRDifference
        self.maxDivisionDifference = maxDivisionDifference
        self.matchListManager = matchListManager

    def insertPlayer(self,  player: Pl.Player):
        for match in self.matchList:
            if(abs(match.getMinimumMatchMMR() - player.getMMR()) <= self.maxMMRDifference and abs(match.getMaximumMatchMMR() - player.getMMR()) <= self.maxMMRDifference):
                if(abs(match.getMinimumMatchDivision() - player.getDivision()) <= self.maxDivisionDifference and abs(match.getMaximumMatchDivision() - player.getDivision()) <= self.maxDivisionDifference):
                    if(match.insertPlayer(player)):
                        if(match.isMatchFull()):
                            match.evenTeamMMR()
                            self.matchListManager.addFinishedMatch(match)
                            self.matchList.remove(match)
                        return True
        return False
    
    def createMatch(self,  player: Pl.Player):
        newMatch = Ma.Match()
        newMatch.insertPlayer(player=player)
        self.matchList.append(newMatch)

    def __str__(self):
        returnString = ""
        for match in self.matchList:
            returnString += match.__str__()
            returnString += "\n"
        return returnString
      

