import random


class Dice():
    def __init__(self, num):
        self.num = num

    def roll(self):
        return random.randint(1, self.num)
