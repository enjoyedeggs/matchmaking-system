from tkinter import Tk, Label, Button, LEFT, RIGHT, Scrollbar, Listbox, END, N, S, W, E, Y
import Match as Ma
import Team as Te
import Player as Pl
import MatchListManager as Mlm

print("hi")


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Matchmaking GUI")
        master.geometry("1024x768")

        self.playerQueueLabel = Label(master, text="Player Queue : ", font=("Times New Roman", 30))
        self.playerQueueLabel.grid(columnspan=1, sticky=N + W)
        self.playerQueueLabel.grid(row=0, column=0)

        self.playerQueueScrollBar = Scrollbar()
        self.playerQueueScrollBar.grid(row=1, column=1, sticky=W)

        self.matchQueueScrollBar = Scrollbar()
        self.matchQueueScrollBar.grid(row=1, column=3, rowspan=10, sticky=W)

        self.matchLabel = Label(master, text="Matches :", font=("Times New Roman", 30))

        self.matchLabel.grid(columnspan=1, rowspan=3, row=0, column=3, sticky=N + W)

        self.testButton = Button(master, text="Test", command=self.test)
        self.testButton.grid(columnspan=1, row=2, column=3, sticky=E)

        self.closeButton = Button(master, text="Close", command=master.quit)
        self.closeButton.grid(row=2, column=2)

        listbox = Listbox(root, yscrollcommand = self.playerQueueScrollBar.set)
        listbox.grid(row=1, column=0)

        for i in range(100):
            listbox.insert(END, i)

        listbox.config(yscrollcommand=self.playerQueueScrollBar.set)
        self.playerQueueScrollBar.config(command=listbox.yview)

    def test(self):
        print("hi")


def generateRandomPlayer(self):
    return Pl.Player()


testPlayer1 = Pl.Player(username="BOB", summonerID=120385, division=4, MMR=2000, tier=1)
testPlayer2 = Pl.Player(username="Jeff", summonerID=120386, division=4, MMR=2000, tier=3)
testPlayer3 = Pl.Player(username="dfs", summonerID=120387, division=4, MMR=2000, tier=1)
testPlayer4 = Pl.Player(username="Basdf", summonerID=1123420388, division=4, MMR=2000, tier=1)
testPlayer5 = Pl.Player(username="asvcx", summonerID=120389, division=4, MMR=2000, tier=1)
testPlayer6 = Pl.Player(username="Holland", summonerID=1201245390, division=4, MMR=2000, tier=1)
testPlayer7 = Pl.Player(username="Netherlands", summonerID=120412495, division=4, MMR=2000, tier=1)
testPlayer8 = Pl.Player(username="Eu", summonerID=120134595, division=4, MMR=2000, tier=1)
testPlayer9 = Pl.Player(username="Japan", summonerID=1201235, division=4, MMR=2000, tier=1)
testPlayer10 = Pl.Player(username="Murica", summonerID=120981, division=4, MMR=2000, tier=1)
testPlayer11 = Pl.Player(username="UK", summonerID=120985, division=4, MMR=2000, tier=1)
testPlayer12 = Pl.Player(username="Bread", summonerID=1209823, division=4, MMR=3100, tier=1)


print("\n\n")
testMatchListManager = Mlm.MatchListManager(36, 1000, 4)
testMatchListManager.insertPlayer(testPlayer1)
print(testMatchListManager.divisionToString(4))
testMatchListManager.insertPlayer(testPlayer2)
print(testMatchListManager.divisionToString(8))
print(testMatchListManager.divisionToString(16))
testMatchListManager.insertPlayer(testPlayer3)
testMatchListManager.insertPlayer(testPlayer4)
testMatchListManager.insertPlayer(testPlayer5)
testMatchListManager.insertPlayer(testPlayer6)
testMatchListManager.insertPlayer(testPlayer7)
testMatchListManager.insertPlayer(testPlayer8)
testMatchListManager.insertPlayer(testPlayer9)
testMatchListManager.insertPlayer(testPlayer10)
testMatchListManager.insertPlayer(testPlayer12)
print(testMatchListManager.divisionToString(8))
print(testMatchListManager.divisionToString(16))
testMatchListManager.insertPlayer(testPlayer11)
print(testMatchListManager.divisionToString(8))
print(testMatchListManager.finishedMatchesToString())
print(testMatchListManager.popFinishedMatch())

root = Tk()
gui = GUI(root)
root.mainloop()
