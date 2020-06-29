class Fortune():
    kuji = ['大吉', '中吉', '小吉', '凶', '大凶']

    def draw(self):
        import random
        print(random.choice(kuji))
