import Player as Pl
import time
import random
from random import seed
from random import randint

seed(time.process_time_ns())
adj = ["Youthful", "Hurt", "Beautiful", "Plausible", "Simple", "Educated", "Gentle", "Jumpy", "Defeated", "Impolite",
    "Volatile", "Real", "Visible", "Graceful", "Ordinary", "Strong", "Accidental", "Chubby", "Melted", "Embarrassed", "Chunky",
    "Snotty", "Magenta", "Awesome", "Swanky", "Automatic", "Blushing", "Jittery", "Brash", "Kindhearted", "Tense", "Conscious", 
    "Alleged", "Large", "Bright", "Heavenly", "Symptomatic", "Windy", "Ignorant"]

noun = ["Bread", "Paper", "Diamond", "Queen", "Pizza", "Hat", "Law", "Chocolate", "King", "City", "Heart",
    "Worker", "Unit", "Player", "Entry", "Bath", "Power", "Meal", "Sir", "Farmer", "Photo", "Hair", "Apple",
    "Death", "Data", "Storage", "Lady", "Stranger", "Union", "Chest", "Orange", "Actor", "Week", "Knowledge", "Dirt", "Success"]

tier = [27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

weights = [0.012, 0.027, 0.04, 0.1, 0.18, 0.12, 0.35, 1.18, 1.3, 1.4, 1.6, 5.2, 4.5, 6.1, 4.8, 12, 9.5, 9.5, 5, 9.1, 
    9.4, 6.1, 2.9, 3.7, 2.5, 1.3, .52, 0.079]

userValue = 10000000

#change below to a while loop, for while the program is still running
for x in range(10):
    #Below line is for wait between new random player generation
    #time.sleep(randint(0, 180))
    Pl.username = adj[randint(0,len(adj)-1)] + noun[randint(0,len(noun)-1)]
    Pl.summonerID = userValue
    placement = random.choices(tier, weights,k=1)
    Pl.division = int(placement[0] / 4)
    Pl.tier = placement[0] % 4
    Pl.honor = randint(1,15)
    Pl.wins = randint(50, 500)
    Pl.losses = Pl.wins+randint(-50,100)
    Pl.MMR = 500+(placement[0]*250) + randint(-400, 600)
    userValue += 1
    print(Pl.username,"\nID:", Pl.summonerID,"\nGenerated Placement:", placement[0],"\nDivision:", Pl.division,"\nTier:", Pl.tier,"\nHonor:", Pl.honor,"\nMMR:", Pl.MMR, "\nWins:", Pl.wins, "\nLosses", Pl.losses,"\n")