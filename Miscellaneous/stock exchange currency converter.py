class converter():

    def __init__(self, value):
    
        self.value = value

    def YEN(self, value):

        value = value * 143.08
        return value
    
    def XBT(self, value):

        value = value / 6588.97
        return value
    
    def YUAN(self, value):

        value = value / 0.11
        return value

    def WON(self, value):

        value = value / 0.00065
        return value

value = 0

a = converter(value)

def userChoice():

    value = float(input("What value of currency do you have: "))

    inp = input("What currency would you like to convert from: ").lower()
    out = input("What currency would you like to convert to: ").lower()
    
    

    if inp == "gbp":
        
        value = value
    
    elif inp == "yen":
        
        value = value / 143.08

    elif inp == "xbt":

        value = value * 6588.97

    elif inp == "yuan":

        value = value * 0.11

    elif inp == "won":

        value = value * 0.00065

    if out == "gbp":
    
        end = a.GBP(value)
        print(end)

    elif out == "yen":
        
        end = a.YEN(value)
        print(end)

    elif out == "xbt":

        end = a.XBT(value)
        print(end)
        
    elif out == "yuan":

        end = a.YUAN(value)
        print(end)

    elif out == "won":
        
        end = a.WON(value)
        print(end)

userChoice()
        