## generating random values

import random


for i in range(3):
    print(random.randint(10,20))


members = ['John','Mary','Bob','Mosh']
leader = random.choice(members)
print(leader)

#challenge


class Dice:
    def roll(self):
        return (random.randint(1,6),random.randint(1,6))
    

dice = Dice()
print(dice.roll())