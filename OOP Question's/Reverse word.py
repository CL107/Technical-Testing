class reverse():

    def __init__(self, x):

        self.x = x
    
    def switch(self, x):

        i = len(x) - 1

        for y in len(x):

            temp = x[-i]
            new = new + temp
            i -= 1

        print(new)

word = "Hello World"

a = reverse(word)
a.switch(word)

