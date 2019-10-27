from tkinter import Tk, Label, Button, LEFT, RIGHT, Scrollbar, N, S, W, E
import Match as Ma
import Team as Te
import Player as Pl

print("hi")


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Matchmaking GUI")

        self.PlayerQueueLabel = Label(master, text="Player Queue : ")
        self.PlayerQueueLabel.grid(columnspan=1, sticky=W)
        self.PlayerQueueLabel.grid(row=1, column=1)

        self.playerQueueScrollBar = Scrollbar()
        self.playerQueueScrollBar.grid(rowspan=10, sticky=W)
        self.playerQueueScrollBar.grid(row=2, column=1)

        self.matchLabel = Label(master, text="Matches : ")
        self.matchLabel.grid(columnspan=1, sticky=E)
        self.matchLabel.grid(row=1, column=3)

        self.greet_button = Button(master, text="Test", command=self.test)
        self.greet_button.grid(row=3, column=3)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, column=2)

    def test(self):
        print("hi")

testPlayer = Pl.Player(username="BOB", summonerID=120385)
print(testPlayer.username)

testTeam = Te.Team()
testTeam.players['player1'] = testPlayer
print(testTeam.players['player1'])
print(testTeam.players['player1'].summonerID)

testMatch = Ma.Match()
print(testMatch.teams)
print(testMatch.teams['team1'])

root = Tk()
gui = GUI(root)
root.mainloop()
