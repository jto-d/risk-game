from Country import Country

class Map:
    def __init__(self):
        self.countries = []
        self.card_turn_ins = 0

        self.turn = 1

    def init_map(self):
        with open("countries.txt", "r") as f:
            countries = f.read()
        countries = countries.split('\n')
        for country in countries:
            info = country.split(',')
            self.countries.append(Country(info.pop(0),-1,info))

        print(self.countries[0].adjacent)


    