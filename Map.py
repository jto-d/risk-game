class Map:
    def __init__(self, countries: list, c: int):
        self.countries = countries
        self.card_turn_ins = c

        self.turn = 1