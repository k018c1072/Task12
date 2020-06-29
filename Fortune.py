import random


class Fortune():
    kuji = ['大吉', '中吉', '小吉', '凶', '大凶']

    def draw(self):
        print(random.choice(self.kuji))
