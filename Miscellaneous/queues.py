q1 = [1, 2, 3, 4, 5]

def queue(q1):
    choice = int(input("Do you want to remove an item(1) or add an item(2): "))
    if choice == 1:
        underflow(q1)
        pop(q1)
    if choice == 2:
        overlow(q1)
        push()

def underflow(q1):
    if len(q1) == 0:
        print("There is underflow, an item cannot be removed")
        queue(q1)
    elif len(q1) != 0:
        pass

def overlow(q1):
    if len(q1) == 10:
        print("There is underflow, an item cannot be added")
        queue(q1)
    elif len(q1) != 10:
        pass

def pop(q1):
    print(q1)
    print(f"{q1.pop(0)} has been removed from the list")
    print(q1)

def push(q1):
    value = int(input("What do you want to push onto the list: "))
    q1.append(value)

queue(q1)