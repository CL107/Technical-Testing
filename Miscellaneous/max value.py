def Max(L):

    max_num = 0

    for x in range(0, len(L)):
        
        if L[x] > max_num:
            max_num = L[x]

    return max_num

print(Max([23, 45, 65, 67, 98, 21, 4, 6, 23, 65]))

