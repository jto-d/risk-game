from Dice import Dice
from Attack import Attack
from Country import Country
from Map import Map
from Player import Player

num_players = 4

# allow people to input names
p = [Player('Player ' + str(i), i) for i in range(0,num_players)]

m = Map(p)
m.init_map()

m.play_round()

