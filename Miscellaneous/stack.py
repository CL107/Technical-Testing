# Author: Cameron Liddell
# Date: 16/03/20
# Group: 12B/CS
# Title: Stacks
def pop(stack):

    global pointer

    if pointer == 0:
        print("\nThe stack is empty, can't remove another")
        pass
    else:
        pointer -=1
        del stack[-1]
        

    print (f"\n{stack}\n")
    
def push(stack, limit, num):

    global pointer

    if pointer > limit:
        print("\nThe stack is full, can't add another\n")
        pass
    else:
        stack.append(num)
        pointer +=1

    print(f"\n{stack}\n")

stack = []
pointer = 0
limit = 9

while True:
    
    choice = input("Would you like to pop, push or quit: ").lower()

    if choice == "pop":
        pop(stack)
    
    elif choice == "push":
        while True:
            try:
                num = int(input("\nWhat do you want to append: "))
                push(stack, limit, num)
                break
            except:
                print("\nInvalid Input")
        
    
    elif choice == "quit":
        quit()
    
    else:
        print("\nInvalid input\n")
        
        pass
