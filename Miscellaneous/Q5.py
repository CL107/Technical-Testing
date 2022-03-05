# Author: Cameron Liddell
# Date: 16/9/19
# Title: Q5

class word:
    def __init__ (self):
        self.Input = input("Type a word: ")
        output = ""
        for i in range(1, len(self.Input) + 1):
            output += self.Input[len(self.Input) - i]
        print(output)

user = word()



