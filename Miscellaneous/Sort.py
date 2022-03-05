# Author: Cameron Liddell
# Date: 13/9/19
# Title: Q4

from random import choice

class Array:
    def __init__(self, *numbers):
        self.numbers = list(numbers)
        self.bubble = self.bubble_sort()
        self.quick = self.quick_sort(self.numbers)
        
    def linear_search(self, item):
        for i,I in enumerate(self.numbers):
            if I == item:
                return i
                                                                                    
    def bubble_sort(self):
        Sorted = False
        b = self.numbers
        while not Sorted:
            Sorted = True

            for i in range(len(b)):
                I = b[i]
                try:
                    if I > b[i + 1]:
                        Sorted = False
                        b[i],  b[i + 1] = b[i + 1], b[i]

                except IndexError:
                    pass
        return b
    
    def quick_sort(b):


        if len(b) > 1:
            pivot = choice(b)

            l = []
            r = []

            for i in b:
                if i > pivot:
                    r.append(i)

                elif i < pivot:
                    l.append(i)

            return b.quick_sort(l) + [pivot] + b.quick_sort(r)

        else:
            return b
                
n = Array
x = [12, 45, 43, 67, 21, 81, 87, 93, 73]
print (n.bubble_sort(x))

            
            
    
