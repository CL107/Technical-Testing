import random

class person:

    _nextid = 1

    def __init__(self):

        self.id = person._nextid
        self.age = random.randrange(0, 10)
        person._nextid += 1

class generate:

    def __init__(self):

        self._listpersons = []

    def create_person(self):

        temp = person()
        self._listpersons.append(temp)

    def add_person(self):        

        for x in range(0, 10):
            self.create_person()

    def get_person(self):

        #print(self._listpersons[0].id)

        for p in self._listpersons:
            name = input("What is the name: ")
            print(name, ":" , 'The id is ', p.id, ' and the age is ', p.age)          


# main
people = generate()
people.add_person()
people.get_person()
