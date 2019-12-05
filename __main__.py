from tkinter import *
from tkinter import ttk
import Match as Ma
import Team as Te
import Player as Pl
import PlayerQueueManager as Pqm
import MatchListManager as Mlm
import PlayerRandomizer as Pr

print("hi, this is Marissa :)")

class GUI:

    def __init__(self, master): #-- magic funtion that builds GUI
        self.master = master
        master.title("Matchmaking GUI")

        # -------------------------------------------------- FRAMES -------------------------------------------------
        self.button_frame = Frame(master)  # - Frame BOTTOM
        self.button_frame.pack(side=BOTTOM, fill=X, padx=15)

        self.col0_frame = Frame(master)  # - Frame 0
        self.col0_frame.pack(side=LEFT)

        self.playerq_frame = Frame(master)  # - Frame 1
        self.playerq_frame.pack(side=LEFT)
        self.playerq_frame['borderwidth'] = 3
        self.playerq_frame['relief'] = 'sunken'

        self.col2_frame = Frame(master)  # - Frame 2
        self.col2_frame.pack(side=LEFT)

        self.matchmaking_pr_frame = Frame(master)  # - Frame 3
        self.matchmaking_pr_frame.pack(side=LEFT)
        self.matchmaking_pr_frame['borderwidth'] = 3
        self.matchmaking_pr_frame['relief'] = 'sunken'

        self.col4_frame = Frame(master)  # - Frame 4
        self.col4_frame.pack(side=LEFT)

        self.finishmatch_frame = Frame(master)  # - Frame 5
        self.finishmatch_frame.pack(side=LEFT)
        self.finishmatch_frame['borderwidth'] = 3
        self.finishmatch_frame['relief'] = 'sunken'

        self.col6_frame = Frame(master)  # - Frame 6
        self.col6_frame.pack(side=LEFT)

        # -------------------------------------------------- FRAME 0 --------------------------------------------------
        self.spacing_col0 = Label(self.col0_frame, text="   ")  # - 3 spaces
        self.spacing_col0.config(height=2)
        self.spacing_col0.grid(row=0, column=0, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME 1 --------------------------------------------------
        self.playerq_title = Label(self.playerq_frame, text="Player Queue")
        self.playerq_title.grid(row=1, column=1, sticky=W)

        self.spacing_col1 = Label(self.playerq_frame, text="\t")
        self.spacing_col1.grid(row=2, column=1, sticky=W)  # -- for spacing purposes

        self.playerq_box = Text(self.playerq_frame)
        self.playerq_box.config(height=36, width=25)  # - this should have 'state="disabled"'
        self.playerq_box.grid(row=3, column=1, sticky=W)
        # -------------------------------------------------- FRAME 2 --------------------------------------------------
        self.spacing_col2 = Label(self.col2_frame, text="  ")  # - 2 spaces
        self.spacing_col2.grid(row=0, column=2, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME 3 --------------------------------------------------
        self.matchmaking_pr_title = Label(self.matchmaking_pr_frame, text="Matchmaking Process")
        self.matchmaking_pr_title.grid(row=1, column=3, sticky=W)

        self.matches_option = ttk.Combobox(self.matchmaking_pr_frame, values=[
                                                                    "Division1",
                                                                    "Division2",
                                                                    "Division3",
                                                                    "Division4"])
        self.matches_option.grid(row=1, column=3, sticky=E)
        self.matches_option.current(0)

        self.spacing_col3 = Label(self.matchmaking_pr_frame, text="\t")
        self.spacing_col3.grid(row=2, column=3, sticky=W)  # -- for spacing purposes

        self.matches_box = Text(self.matchmaking_pr_frame)
        self.matches_box.config(height=36, width=55)
        self.matches_box.grid(row=3, column=3, sticky=N)
        # -------------------------------------------------- FRAME 4 --------------------------------------------------
        self.spacing_col4 = Label(self.col4_frame, text="  ")  # - 2 spaces
        self.spacing_col4.grid(row=0, column=4, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME 5 --------------------------------------------------
        self.finishmatches_title = Label(self.finishmatch_frame, text="Finished Matches")
        self.finishmatches_title.grid(row=1, column=5, sticky=W)

        self.finishmatches_option = ttk.Combobox(self.finishmatch_frame, values=[
                                                                        "Division1",
                                                                        "Division2",
                                                                        "Division3",
                                                                        "Division4"])
        self.finishmatches_option.grid(row=1, column=5, sticky=E)
        self.finishmatches_option.current(0)

        self.spacing_col5 = Label(self.finishmatch_frame, text="\t")
        self.spacing_col5.grid(row=2, column=5, sticky=W)  # -- for spacing purposes

        self.finmatches_box = Text(self.finishmatch_frame)
        self.finmatches_box.config(height=36, width=45)
        self.finmatches_box.grid(row=3, column=5, sticky=N)
        # -------------------------------------------------- FRAME 6 --------------------------------------------------
        self.spacing_col4 = Label(self.col6_frame, text="  ")  # - 2 spaces
        self.spacing_col4.grid(row=0, column=6, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME BOTTOM --------------------------------------------------
        self.accept_p_button = Button(self.button_frame, text="   ACCEPT PLAYERS   ", command=self.acceptPlayer)
        self.accept_p_button.grid(row=4, column=1, sticky=W)

        self.accept_p_button = Button(self.button_frame, text="   INSERT PLAYER INTO MATCH MANAGER   ", command=self.popPlayerToMatchManager)
        self.accept_p_button.grid(row=4, column=2, sticky=W)

        self.stop_p_button = Button(self.button_frame, text="   STOP   ")
        self.stop_p_button.grid(row=4, column=3, sticky=E, padx=80)

        self.stop_p_button = Button(self.button_frame, text="   Cycle 100   ", command=self.cycle100)
        self.stop_p_button.grid(row=4, column=4, sticky=E, padx=80)

        self.matchListManager = Mlm.MatchListManager(36, 1000, 4)
        self.playerQueueManager = Pqm.PlayerQueueManager()
        self.matches_box.insert(END, "spamsdgf" + "\n")
        self.playerq_box.insert(END, "spamsdgf" + "\n")


    def acceptPlayer(self):
        tPlayer = Pr.generateRandomPlayer()
        self.playerQueueManager.insertPlayer(tPlayer)
        self.updatePlayerQueue()

    def updatePlayerQueue(self):
        self.playerq_box.delete(1.0, END)
        for player in self.playerQueueManager.PlayerQueue:
            self.playerq_box.insert(END, player.username + " - " + str(player.MMR) + "\n")

    def updateMatchList(self):
        self.matches_box.delete(1.0, END)
        for division in range(self.matchListManager.divisions):
            self.matches_box.insert(END, self.matchListManager.divisionToString(division) + "\n")

    def updateFinishedMatchList(self):
        self.finmatches_box.delete(1.0, END)
        for match in self.matchListManager.finishedMatchArray:
            self.finmatches_box.insert(match.__str__() + "\n")

    def updateAll(self):
        self.updatePlayerQueue()
        self.updateMatchList()
        self.updateFinishedMatchList()

    def popPlayerToMatchManager(self):
        self.matchListManager.insertPlayer(self.playerQueueManager.removePlayer())
        self.updateAll()

    def cycle100(self):
        for i in range(100):
            self.acceptPlayer()
            self.popPlayerToMatchManager()

    def test(self):  # - ?
        print("hi")

root = Tk()
gui = GUI(root)
root.mainloop()


def generateRandomPlayer(self):
    return Pl.Player();

testPlayer1 = Pl.Player(username="BOB", summonerID=120385, division=4, MMR=2000, tier=1)
testPlayer2 = Pl.Player(username="Jeff", summonerID=120386, division=4, MMR=2000, tier=3)
testPlayer3 = Pl.Player(username="dfs", summonerID=120387, division=4, MMR=2000, tier=1)
testPlayer4 = Pl.Player(username="Basdf", summonerID=1123420388, division=4, MMR=2000, tier=1)
testPlayer5 = Pl.Player(username="asvcx", summonerID=120389, division=4, MMR=2000, tier=1)
testPlayer6 = Pl.Player(username="Holland", summonerID=1201245390, division=4, MMR=2000, tier=1)
testPlayer7 = Pl.Player(username="Netherlands", summonerID=120412495, division=4, MMR=2000, tier=1)
testPlayer8 = Pl.Player(username="Eu", summonerID=120134595, division=4, MMR=2000, tier=1)
testPlayer9 = Pl.Player(username="Japan", summonerID=1201235, division=4, MMR=2000, tier=1)
testPlayer10 = Pl.Player(username="America", summonerID=120981, division=4, MMR=2000, tier=1)
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
