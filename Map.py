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

        self.turn_number = 1

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
        
        # add countries from the list of unowned_countries to respective players until no more unowned
        
        while unowned_countries != []:
            country = unowned_countries.pop(0)
            country.player = index

            self.countries.append(country)

            # initialize countries and armies dictionary
            self.players[index].init_countries(country)

            # store country objects to a player object
            self.players[index].countries.append(country)

            # if the index is the same as the length of players, reset the index
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
    def init_turn(self, player: Player) -> None:
        armies = self.calculate_armies(player)
        print(f'You have {armies} armies to place')

        while armies > 0:
            
            print('Available Countries: ' + str(player.country_armies))
            # print('Available Countries: ' + str([str(ctry) for ctry in player.countries]))
            index = int(input('What index country do you want to add armies to? '))
            add = 0

            # store the selected country in a string
            country_name = str(player.countries[index])
            while add == 0 or add > armies:
                add = int(input(f'How many armies would you like to add to {country_name}? '))
            armies -= add
            player.country_armies[country_name] += add

        print('Armies: ' + str(player.country_armies))



    # a round of turns for each player
    def turn(self, player: Player):
        # initialize armies for the player's turn
        self.init_turn(player)

        # let the player attack if they choose to

    # play a full round using all players
    def play_round(self, player_list = []):
        player_list = self.players
        for player in player_list:
            self.turn(player)


 
