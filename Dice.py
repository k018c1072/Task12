class Dice():
    def __init__(self, num):
        self.num = num

    def roll(self):
        import random
        return random.randint(1, self.num)
