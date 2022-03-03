from Dice import Dice
from Country import Country

class Attack:
    def __init__(self, atk_ctry, de_ctry):
        
        self.atk_ctry = atk_ctry
        self.de_ctry = de_ctry


    # assumes that it is a valid attack
    def calc_dice(self):
        self.atk_armies = self.atk_ctry.armies
        self.de_armies = self.de_ctry.armies


        if self.atk_armies > 3:
            self.atk_dice_num = 3
        else:
            self.atk_dice_num = self.atk_armies - 1

        if self.de_armies == 1:
            self.de_dice_num = 1
        else:
            self.de_dice_num = 2
    
    def roll_dice(self):

        self.calc_dice()

        self.atk_dice = Dice(self.atk_dice_num)
        self.de_dice = Dice(self.de_dice_num)

        self.atk_rolls = self.atk_dice.roll()
        self.de_rolls = self.de_dice.roll()

        print(self.atk_rolls, self.de_rolls)


    def compare_rolls(self):


        atk_subtract = 0
        de_subtract = 0

        for i in range(2):
            if self.atk_rolls[i] > self.de_rolls[i]:
                de_subtract += 1
            else:
                atk_subtract += 1
        
        self.atk_ctry.subtract_armies(atk_subtract)
        self.de_ctry.subtract_armies(de_subtract)

        if self.atk_ctry.armies == 1:
            print(f"You can no longer attack with {str(self.atk_ctry)}")
        elif self.de_armies <= 0:
            print(f"You have conquered {str(self.de_ctry)}")
        else:
            print(f'{str(self.atk_ctry)} now has {self.atk_ctry.armies} armies\n{str(self.de_ctry)} now has {self.de_armies} armies')

        

        

        