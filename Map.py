from Country import Country
from Player import Player
import random

class Map:
    def __init__(self, players: list):
        self.countries = []
        self.num_players = len(players)
        
        # list of player objects in the game
        self.players = players
        self.card_turn_ins = 0

        self.turn = 1

    def init_map(self):
        
        # open txt file with countries and their adjacencies
        with open("countries.txt", "r") as f:
            countries = f.read()
        countries = countries.split('\n')
        unowned_countries = []
        for country in countries:
            # adjcent countries
            info = country.split(',')

            # add each country to the list of countries on the map
            unowned_countries.append(Country(info.pop(0),-1,info))
        
        # randomly shuffle countries
        random.shuffle(unowned_countries)

        # assign countries to players and overall list
        index = 0
        
        # add countries from the list of unowned_countries until empty
        while unowned_countries != []:
            country = unowned_countries.pop(0)
            country.player = index

            self.countries.append(country)
            self.players[index].countries.append(country)

            if index == 3:
                index = 0
            else:
                index += 1
    

    def calculate_armies(self, player: Player) -> int:
        num_ctrys = len(player.countries)
        if num_ctrys//3 > 3:
            return num_ctrys//3
        return 3

    # a single player's turn
    def indiv_turn(self, player: Player) -> None:
        armies = self.calculate_armies(player)
        print(f'You have {armies} armies to place')

        while armies > 0:
            print('Available Countries: ' + str([str(ctry) for ctry in player.countries]))
            index = int(input('What index country do you want to add armies to?'))
            add = 0
            while add == 0 or add > armies:
                add = int(input(f'How many armies would you like to add to {str(player.countries[index])}?'))
            armies -= add



    # # a round of turns for each player
    # def turn(self):
    #     for player in self.players:
    #         self.indiv_turn(player)

 
