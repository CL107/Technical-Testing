class hashtable():
    def __init__(self, length=4):
        self.array = [None * length] 
        self.length = length

    def hash(self, item):
        length = len(self.array)
        return hash(item) % length

    def add(self, item):
        x = self.hash(item)

        while True:
            if self.array[x] == None:
                break
            else:
                x += 1
                x %= self.length

        self.array[x] = item



        
        
        



    
    
        
        
