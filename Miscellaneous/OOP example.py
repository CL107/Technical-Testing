class Addition: 
    first = 0
    second = 0
    answer = 0
      
    def __init__(self, f, s): 
        self.firstnum = f 
        self.secondnum = s 
    
    def __del__(self):
        print("Deleted")

    def display(self): 
        print("First number = " + str(self.first)) 
        print("Second number = " + str(self.second)) 
        print("Addition of two numbers = " + str(self.answer)) 
  
    def calculate(self): 
        self.answer = self.first + self.second 

class Subtraction(Addition):

    def __init__(self, f, s):
        super().__init__(f, s)
        
    def minus(self):
        print("First number = " - str(self.first)) 
        print("Second number = " - str(self.second)) 
        print("Subtraction of two numbers = " - str(self.answer))

obj = Addition(1000, 2000) 

obj.calculate() 

obj.display() 

obj = Subtraction(2000, 1000)

obj = minus()

del obj