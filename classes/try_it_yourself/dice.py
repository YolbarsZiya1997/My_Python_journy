from random import randint

class Dice:
    """ Represents a Dice"""
    
    def __init__(self, sides=None,):
        """ Initialize the Dice"""
        if sides is None:
            sides = 6
        self.sides = sides
        
    
    def roll_die(self):
        """ Return a number between 1 and the number of sides"""
        return randint(1, self.sides)
        
        
# make a  6-sided die, and show the results for 10 rolls
d6 = Dice()

results = []
for rolls in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sided dice")    
print(results)

# make a 10-sided die, and show the results for 10 rolls
d10 = Dice(sides=10)

results = []
for rolls in range(10):
    result = d10.roll_die()
    results.append(result)
    
print('\n10 rolls of 10-sided dice')
print(results)

# make a 20-sided dice, and show the results for 10 rolls
d10 = Dice(sides=20)

results = []
for rolls in range(10):
    result = d10.roll_die()
    results.append(result)
    
print('\n10 rolls of 10-sided dice')
print(results)
    