import Player as Pl
import time
import random
import zmq
import zlib
import pickle
from threading import Thread
from random import seed
from random import randint


class PlayerRandomizer:
    seed(time.process_time_ns())

    def __init__(self):
        self.adj = ["Youthful", "Hurt", "Beautiful", "Plausible", "Simple", "Educated", "Gentle", "Jumpy", "Defeated",
                    "Impolite",
                    "Volatile", "Real", "Visible", "Graceful", "Ordinary", "Strong", "Accidental", "Chubby", "Melted",
                    "Embarrassed",
                    "Chunky",
                    "Snotty", "Magenta", "Awesome", "Swanky", "Automatic", "Blushing", "Jittery", "Brash",
                    "Kindhearted", "Tense",
                    "Conscious",
                    "Alleged", "Large", "Bright", "Heavenly", "Symptomatic", "Windy", "Ignorant"]

        self.noun = ["Bread", "Paper", "Diamond", "Queen", "Pizza", "Hat", "Law", "Chocolate", "King", "City", "Heart",
                     "Worker", "Unit", "Player", "Entry", "Bath", "Power", "Meal", "Sir", "Farmer", "Photo", "Hair",
                     "Apple",
                     "Death", "Data", "Storage", "Lady", "Stranger", "Union", "Chest", "Orange", "Actor", "Week",
                     "Knowledge",
                     "Dirt", "Success"]

        self.tier = [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
                     0]

        self.weights = [0.012, 0.027, 0.04, 0.1, 0.18, 0.12, 0.35, 1.18, 1.3, 1.4, 1.6, 5.2, 4.5, 6.1, 4.8, 12, 9.5,
                        9.5, 5, 9.1, 9.4, 6.1, 2.9, 3.7, 2.5, 1.3, .52, 0.079]

        self.userValue = 10000000

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)

    def generateRandomPlayer(self):
        player = Pl.Player()
        player.username = self.adj[randint(0, len(self.adj) - 1)] + self.noun[randint(0, len(self.noun) - 1)]
        player.summonerID = self.userValue
        placement = random.choices(self.tier, self.weights, k=1)
        player.division = int(placement[0] % 4)
        player.tier = placement[0] / 4
        player.honor = randint(1, 15)
        player.wins = randint(50, 500)
        player.losses = player.wins + randint(-50, 100)
        player.MMR = 500 + (placement[0] * 250) + randint(-400, 600)
        self.userValue += 1
        return player

    def automaticRandomizedMain(self):
        self.socket.connect("tcp://localhost:1111")
        thread = Thread(target=self.sendRandomPlayers, args=())
        thread.start()

    def sendRandomPlayers(self):
        while (1 == 1):
            randomPlayer = self.generateRandomPlayer()
            pickleObj = pickle.dumps(randomPlayer, protocol=-1)
            self.socket.send(zlib.compress(pickleObj))
            time.sleep(.1)
