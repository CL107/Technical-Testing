# Setting up a class called "dog"
class dog():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def bark(self, woof):

        print(woof, self.name)

    def wag_tail(self, wag):

        print(wag, self.name)

    def 


# Instantiating a class to produce an object
ronny = dog("Ernie", 6)

ronny.bark("Woof, woof!")
ronny.wag_tail("Wagging the tail")

