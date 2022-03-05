class parrot:

    species = "bird"

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):
        return f"\nParrot:\n \t{self.name}, \t{self.age}"
    
    def __repr__(self):
        return f"\nParrot --> {self.name}"

    

green = parrot("Dave", 4)
yellow = parrot("June", 96)

x = []




for x in range(3):

    name = input("Enter a name: ")
    age = int(input("Enter a age: "))

    x.append(parrot(name, age))

print (x)

# print("Name is:", green.name)
# print("Age is:", green.age)

# print("")

# print("Name is:", yellow.name)
# print("Age is:", yellow.age)