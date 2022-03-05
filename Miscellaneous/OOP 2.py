# Setting up a class called "dog"
class dog():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def bark(self, woof):

        print(woof, self.name)

    def wag_tail(self, wag):

        print(wag, self.name)

class puppy(dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        print("'Whimper'")
        


# Instantiating a class to produce an object
ronny = dog("Ernie", 6)
bill = puppy("Bob", 2)
ronny.bark("Woof, woof!")
ronny.wag_tail("Wagging the tail")

