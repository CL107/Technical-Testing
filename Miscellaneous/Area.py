import math

class Area:

    def __init__(self, radius):

        self.radius = int(radius)
        self.area = self.area_circle()

    def area_circle(self):

        return math.floor(math.pi * (self.radius**2))

def main():

    user = input("What is the radius of your circle: ")
    circle = Area(user)
    print("The area is", circle.area, "cm²") 

main()
