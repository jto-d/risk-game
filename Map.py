from Country import Country
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
        index = 1
        while unowned_countries != []:
            country = unowned_countries.pop(0)
            country.player = index
            if index == 4:
                index = 1
            else:
                index += 1
            self.countries.append(country)

