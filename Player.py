class Player:
    def __init__(self,name: str, index: int):
        self.name = name
        self.index = index
        self.countries = []
        self.cards = []

    def __str__(self):
        return self.name
