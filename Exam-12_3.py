from Dice import Dice

dice_1 = Dice(6)
dice_2 = Dice(6)
dice_3 = Dice(6)

while True:
    a = dice_1.roll()
    b = dice_2.roll()
    c = dice_3.roll()
    print([a, b, c])
    if a == b == c:
        print('当たり！')
        break
