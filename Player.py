from Country import Country

class Player:
    def __init__(self,name: str, index: int):
        self.name = name
        self.index = index
        self.countries = []
        self.country_armies = {}
        self.cards = []

    def init_countries(self, ctry: Country):
        self.country_armies[str(ctry)] = ctry.armies

    def __str__(self):
        return self.name
