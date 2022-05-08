from random import randint

class Dice:
    """ Represents a dice with arbitrary number of sides. """
    def __init__(self, sides=None):
        if sides is None:
            sides = 6
        self.sides = sides
        
    def roll_dice(self):
        """ roll the dice"""
        return randint(1, self.sides)
    

# roll the 6 side dice 10 times
d6 = Dice()

results = []
for roll in range(10):
    results.append(d6.roll_dice())
    
print(results)

# how about a ten sided dice

d10 = Dice(10)

results_1 = []
for roll in range(20):
    results_1.append(d10.roll_dice())
    
print(results_1)