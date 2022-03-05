# Author: Cameron Liddell
# Date: 23/01/20
# Title: Q3

class Array:
    def __init__(self, *numbers):
        self.numbers = numbers

    def linear_search(self, item):
        for i, I in enumerate(self.numbers):
            if I == item:
                return i

n = Array(12, 45, 43, 67, 21, 81, 87, 93, 73)
print(n.linear_search(73))
            
            
    
