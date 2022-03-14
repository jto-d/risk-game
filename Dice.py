import random

class Dice:
    def __init__(self, num):
        self.num = num

    def single_roll(self):
        return random.randint(1,6)

    def roll(self):
        
        # roll amount of dice
        roll = [self.single_roll() for i in range(self.num)]
        
        # return list of length self.num of rolls in descending order
        return sorted(roll, reverse = True)


