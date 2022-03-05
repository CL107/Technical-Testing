def linear(L, value):
    
    for i in range(len(L)):
        if L[i] == value:
            print (f"{value} has been found at index {i} in the list.")
            break


array = [72, 798, 34, 12, 56, 94, 10, 1, 999, 3, 7, 0]
value = 34

linear(array, value)