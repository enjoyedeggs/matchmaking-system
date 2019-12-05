import MatchList as Ml

class MatchListManager(object):
    
    def __init__(self, divisions, maxMMRDifference, maxDivisionDifference):
        self.matchListArray = []
        self.finishedMatchArray = []
        self.divisions = divisions
        self.maxMMRDifference = maxMMRDifference
        self.maxDivisionDifference = maxDivisionDifference
        
        for i in range(0, divisions):
            self.matchListArray.append(Ml.MatchList(self, maxMMRDifference, maxDivisionDifference))
            
    def insertPlayer(self, player: Ml.Pl.Player):
        playerCurrentDivision = ((player.getTier() * 4) + (player.getDivision()))
        currentLinkedList = playerCurrentDivision - 1
        divisionDeviation = 0
        
        while(divisionDeviation <= self.maxDivisionDifference):
            if(not((currentLinkedList + divisionDeviation) >= self.divisions)):
                if(self.matchListArray[currentLinkedList + divisionDeviation].insertPlayer(player)):
                    return True
                    
            if(not((currentLinkedList - divisionDeviation) < 0) and not(divisionDeviation == 0)):
               if(self.matchListArray[currentLinkedList - divisionDeviation].insertPlayer(player)):
                   return True
               
            divisionDeviation += 1
            
        self.matchListArray[currentLinkedList].createMatch(player)
        return True
    
    def addFinishedMatch(self, match):
        self.finishedMatchArray.append(match)

    def popFinishedMatch(self):
        return self.finishedMatchArray.pop()

    def divisionToString(self, division):
        return "Division: " + str(division) + "\n\n" + self.matchListArray[division - 1].__str__()

    def finishedMatchesToString(self):
        returnString = "FinishedMatches: \n"
        for match in self.finishedMatchArray:
            returnString += match.__str__() + "\n"
        return returnString

    def __str__(self):
        returnString = ""
        for i in range(self.divisions):
            returnString += self.divisionToString(i+1)
        return returnString

        
        
        
        
    
