import random

class Shuffle():

    def __init__(self, suit, num):

        self.suit = suit
        self.num = num


    def shuffle(self, suit, num):
    
        random.shuffle(suit)
        random.shuffle(num)

        print (num[0], "of", suit[0])

suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]

a = Shuffle(suit, num)
a.shuffle(suit, num)