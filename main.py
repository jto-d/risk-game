from Dice import Dice
from Attack import Attack
from Country import Country
from Map import Map
from Player import Player

num_players = 4
p = [Player('Player ' + str(i), i) for i in range(1,num_players+1)]

for player in p:
    print(str(player))

m = Map(p)
m.init_map()


