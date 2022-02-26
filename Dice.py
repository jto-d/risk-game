import random

class Dice:
    def __init__(self, num):
        self.num = num

    def roll(self):
        return random.randint(1,6)

    def roll_dice(self):
        
        # roll amount of dice
        roll = [self.roll() for i in range(self.num)]

        return sorted(roll, reverse = True)

        # # return list of length self.num of rolls in descending order
        # return roll.sort(reverse = True)
