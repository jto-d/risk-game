class Continent:
    # a continent contains countries, if a player possesses all of them, they get bonus armies
    def __init__(self, countries: list, bonus: int):
        self.countries = countries
        self.bonus = bonus
