import random


class deck():
    def __init__(self):
        num = []
        suits = ["hearts", "clubs", "spades", "daimonds"]
        for v in range(1, 14):
            for suit in suits:
                num.append(f"{v} of {suit}".replace("11", "Jack").replace("12", "Queen").replace("13", "King"))
        self.num = num

deck1 = deck()
deck1 = deck1.num
random.shuffle(deck1)
print(deck1[0])

        





