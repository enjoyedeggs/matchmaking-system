from tkinter import *
from tkinter import ttk
import zmq
import time
import zlib
import pickle
from threading import Thread
import Match as Ma
import Team as Te
import Player as Pl
import PlayerQueueManager as Pqm
import MatchListManager as Mlm
import PlayerRandomizer as Pr

class GUI:

    def __init__(self, master):  # -- magic funtion that builds GUI
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
        self.playerq_box.config(height=36, width=25)
        self.playerq_box.grid(row=3, column=1, sticky=W)
        # -------------------------------------------------- FRAME 2 --------------------------------------------------
        self.spacing_col2 = Label(self.col2_frame, text="  ")  # - 2 spaces
        self.spacing_col2.grid(row=0, column=2, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME 3 --------------------------------------------------
        self.matchmaking_pr_title = Label(self.matchmaking_pr_frame, text="Matchmaking Process")
        self.matchmaking_pr_title.grid(row=1, column=3, sticky=W)

        divisions = []
        for i in range(27):
            divisions.append("Division-" + str(i + 1))
        divisions.append("All")

        self.matches_option = ttk.Combobox(self.matchmaking_pr_frame, values=divisions)
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

        self.finishmatches_option = ttk.Combobox(self.finishmatch_frame, values=divisions)
        self.finishmatches_option.grid(row=1, column=5, sticky=E)
        self.finishmatches_option.current(0)

        self.spacing_col5 = Label(self.finishmatch_frame, text="\t")
        self.spacing_col5.grid(row=2, column=5, sticky=W)  # -- for spacing purposes

        self.finmatches_box = Text(self.finishmatch_frame)
        self.finmatches_box.config(height=36, width=60)
        self.finmatches_box.grid(row=3, column=5, sticky=N)
        # -------------------------------------------------- FRAME 6 --------------------------------------------------
        self.spacing_col4 = Label(self.col6_frame, text="  ")  # - 2 spaces
        self.spacing_col4.grid(row=0, column=6, sticky=W)  # -- for spacing purposes
        # -------------------------------------------------- FRAME BOTTOM ----------------------------------------------
        self.accept_p_button = Button(self.button_frame, text="   Accept Players   ", command=self.acceptPlayers)
        self.accept_p_button.grid(row=4, column=1, sticky=W)

        self.accept_p_button = Button(self.button_frame, text="   Start Match Manager   ",
                                      command=self.startMatchManager)
        self.accept_p_button.grid(row=4, column=2, sticky=W)

        self.accept_p_button = Button(self.button_frame, text="   Send Matches   ", command=self.startMatchSender)
        self.accept_p_button.grid(row=4, column=3, sticky=W)

        self.stop_p_button = Button(self.button_frame, text="   STOP   ",command=quit)
        self.stop_p_button.grid(row=4, column=4, sticky=E, padx=80)

        self.startTestButton = Button(self.button_frame, text="   Start Test Script   ", command=self.startTestScript)
        self.startTestButton.grid(row=4, column=5, sticky=E, padx=80)

        self.matchListManager = Mlm.MatchListManager(28, 500, 4)
        self.playerQueueManager = Pqm.PlayerQueueManager()
        self.playerRandomizer = Pr.PlayerRandomizer()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.context2 = zmq.Context()
        self.socket2 = self.context2.socket(zmq.PAIR)

    def acceptPlayers(self):
        self.openQueueToOutside()

    def updatePlayerQueue(self):
        self.playerq_box.delete(1.0, END)
        for player in self.playerQueueManager.PlayerQueue:
            self.playerq_box.insert(END, player.username + " - " + str(player.MMR) + "\n")

    def updateMatchList(self):
        self.matches_box.delete(1.0, END)
        if (self.matches_option.current() == 27):
            for division in range(self.matchListManager.divisions):
                self.matches_box.insert(END, self.matchListManager.divisionToString(division) + "\n")
        else:
            self.matches_box.insert(END, self.matchListManager.divisionToString(int(self.matches_option.current())) + "\n")

    def updateFinishedMatchList(self):
        self.finmatches_box.delete(1.0, END)
        if (self.finishmatches_option.current() == 27):
            for match in self.matchListManager.finishedMatchArray:
                self.finmatches_box.insert(END, match.__str__() + "\n")
        else:
            for match in self.matchListManager.finishedMatchArray:
                if (match.getMaximumMatchDivision() == int(self.finishmatches_option.current())):
                    self.finmatches_box.insert(END, match.__str__() + "\n")

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

    def recievePlayers(self):
        while(1==1):
            player = self.socket.recv()
            player = zlib.decompress(player)
            player = pickle.loads(player)
            self.playerQueueManager.insertPlayer(player)
            self.updatePlayerQueue()

    def openQueueToOutside(self):
        self.socket.bind("tcp://*:1111")
        thread = Thread(target=self.recievePlayers, args=())
        thread.start()
        #thread.join()

    def startTestScript(self):
        self.playerRandomizer.automaticRandomizedMain()

    def runMatchManager(self):
        while(1==1):
            if(not self.playerQueueManager.isEmpty()):
                self.popPlayerToMatchManager()
                self.updateAll()

    def startMatchManager(self):
        thread = Thread(target=self.runMatchManager, args=())
        thread.start()

    def runMatchSender(self):
        while(1==1):
            match = self.matchListManager.popFinishedMatch()
            pickleObj = pickle.dumps(match, protocol=-1)
            self.socket.send(zlib.compress(pickleObj))
            self.updateFinishedMatchList()

    def startMatchSender(self):
        self.socket2.connect("tcp://localhost:1112")
        thread = Thread(target=self.runMatchSender, args=())
        thread.start()



root = Tk()
gui = GUI(root)
root.mainloop()
