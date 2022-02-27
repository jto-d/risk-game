class Country:
    def __init__(self, name: str, player: int, continent: str, adjacent: list):
        self.name = name
        self.player = player
        self.continent = continent

        self.armies = 1

    