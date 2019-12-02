from tkinter import *
from tkinter import ttk
import Match as Ma
import Team as Te
import Player as Pl

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
        self.matches_box.config(height=36, width=45, state="disabled")
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
        self.finmatches_box.config(height=36, width=45, state="disabled")
        self.finmatches_box.grid(row=3, column=5, sticky=N)
        # -------------------------------------------------- FRAME 6 --------------------------------------------------
        self.spacing_col4 = Label(self.col6_frame, text="  ")  # - 2 spaces
        self.spacing_col4.grid(row=0, column=6, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME BOTTOM --------------------------------------------------
        self.accept_p_button = Button(self.button_frame, text="   ACCEPT PLAYERS   ", command=self.accept_players())
        self.accept_p_button.grid(row=4, column=1, sticky=W)

        self.stop_p_button = Button(self.button_frame, text="   STOP   ")
        self.stop_p_button.grid(row=4, column=3, sticky=E, padx=80)


    def accept_players(self):
        tPlayer = Pl.Player(username="BOB", summonerID=120385)
        print(tPlayer.username)

        self.playerq_box.insert(END, tPlayer.username + " - " + str(tPlayer.summonerID) + "\n")


    def test(self):  # - ?
        print("hi")

root = Tk()
gui = GUI(root)
root.mainloop()

'''
def generateRandomPlayer(self):
    return Pl.Player();


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
'''