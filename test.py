import random

from Dice import Dice

print(random.randint(1,6))

atk_dice = Dice(3)

print(atk_dice.roll_dice())