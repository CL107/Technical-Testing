import math as m
def binary_search(L, value, left, right):

    while left <= right:
        
        mid = (right - left) / 2 + left
        mid = m.floor(mid)
        
        if L[mid] == value:
            return mid
            
            right == mid + 1
        else:
            left == mid + 1

        print (left)
        print (right)
    return "Not found"



array = [0, 1, 3, 7, 10, 12, 34, 56, 72, 94, 798, 999]
value = 2
left = 0
right = len(array)

print (f"{value} has been found at index {binary_search(array, value, left, right)} in the list.")

