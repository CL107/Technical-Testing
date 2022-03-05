names = {"Cameron", "Matty", "Ethan"}

def func(names):

    new = {"Dan", "Jack"}
    names.update(new)
    print("Inside the function is", names)

func(names) 
print ("Outside the function is", names)