from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
        

    def roll_dice(self):
        for i in range(10):
            print(randint(1, self.sides))

dice1 = Dice()
dice1.roll_dice()
dice2 = Dice(10)
dice2.roll_dice()
dice3 = Dice(20)
dice3.roll_dice()

import random

list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

randomm = random.sample(list_number, 4)

print("Any ticket matching these four numbers or letters wins a prize:", randomm)

my_ticket = ["b", 6, "a", 3]
cnt = 0
while True:
    if randomm != my_ticket:
        cnt+=1
    else:
        break

print(cnt)