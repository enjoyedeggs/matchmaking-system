import Player as Pl
import time
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

for x in range(10):
    Pl.username = adj[randint(0,len(adj)-1)] + noun[randint(0,len(noun)-1)]
    Pl.summonerID = randint(10000000, 99999999)
    Pl.division = randint(0,8)
    Pl.tier = randint(1,4)
    Pl.honor = randint(0,2)
    Pl.wins = randint(50, 500)
    Pl.losses = Pl.wins+randint(-100,100)
    Pl.MMR = randint(0,9000)
    print(Pl.username,"\nID:", Pl.summonerID,"\nDivision:", Pl.division,"\nTier:", Pl.tier,"\nHonor:", Pl.honor,"\nMMR:", Pl.MMR, "\nWins:", Pl.wins, "\nLosses", Pl.losses,"\n")