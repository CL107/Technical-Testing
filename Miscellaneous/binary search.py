def binary(choice, L):

    temp = []
    loops = 1
    boo = True
    mid = int(len(L) / 2) 
    end = len(L)
    start = 0
    

    if choice == L[mid]:
            num = f"{choice} has been found and looped once"
            boo = False
            return num
    
    elif choice > L[mid]:
        temp = L[mid+1:end]

    elif choice < L[mid]:
        temp = L[start:mid+1] 

    loops+=1


    while boo == True:
        
        #print(temp)
        mid = int(len(temp) / 2)
        end = len(temp)
        #print(mid)
        
        if len(temp) == 2:
            if temp[0] == choice or temp [1] == choice:
                num = f"{choice} has been found and looped {loops} times" 
                break
            else:
                num = f"{choice} has not been found"
                break
        
        elif choice == temp[mid]:
            num = f"{choice} has been found and looped {loops} times"
            break
        
        elif choice > temp[mid]:
            temp = temp[mid+1:end]
        
        elif choice < temp[mid]:
            temp = temp[start:mid-1]
        
        elif choice != 0:
            num = f"{choice} has not been found"  
        
        loops+=1
    
    return num

def menu(L):      

    try:  
        print(f"The highest value is {L[-1]} and the lowest value is {L[0]}")
        choice = int(input("What number would you like to search for: "))
    except:
        print("\nInvalid Input\n")
        menu(L)
    

    result = binary(choice, L)
    print (result)


    while True:

        try:
            leave = input("Would you like to go again Y/N: ").lower()

            if leave == "y" or leave == "n":
                break
            
            else:
                print("\nInvalid Input\n")

        except:
            print("\nInvalid Input\n")


    if leave == "n":
        exit()

    elif leave == "y":
        menu(L)

    else:
        menu(L)


L = [12, 45, 67, 68, 70, 87, 99, 105, 123, 150, 167]
menu(L)