from tkinter import Tk, Label, Button, LEFT, RIGHT, Scrollbar, Listbox, END, N, S, W, E, Y
import Match as Ma
import Team as Te
import Player as Pl

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


testPlayer = Pl.Player(username="BOB", summonerID=120385)
print(testPlayer.username)

testTeam = Te.Team()
testTeam.players['player1'] = testPlayer
print(testTeam.players['player1'])
print(testTeam.players['player1'].summonerID)

testMatch = Ma.Match()
print(testMatch.teams)
print(testMatch.teams['team1'])
testMatch = Ma.Match(testTeam, testTeam)
print(testMatch.teams['team1'])

root = Tk()
gui = GUI(root)
root.mainloop()
