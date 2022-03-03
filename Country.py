class Country:
    def __init__(self, name: str, player: int, adjacent: list):
        self.name = name
        self.player = player
        self.adjacent = adjacent

        self.armies = 4

    def __str__(self):
        return self.name

    def add_armies(self, num):
        self.armies += num

    def subtract_armies(self, num):
        self.armies -= num

    