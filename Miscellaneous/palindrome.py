def palindrome():
    
    try:
    
        str1 = input("What would you like to check for a palindrome: ")

        test = False
        x = 0
        y = len(str1) - 1
        mid = len(str1) / 2
        
        while test == False:
            
            if len(str1) == 1:
                print("That is not a valid input, make sure that it is longer than 1 character.")
                palindrome()

            elif str1[x] != str1[y]:
                test = True
                print("That is not a palindrome")
            
            elif mid == x or y:
                test = True
                print("That is a palindrome")

            elif str1[x] == str1[y]:
                print (True)
                x += 1
                
        choice = input("Do you want to do another, y/n: ")
        if choice == "n":
            quit()
    
        elif choice == "y":
            palindrome()

        else:
            print("That is not a valid answer")
            palindrome()
        
    except:
        palindrome()
    
palindrome()