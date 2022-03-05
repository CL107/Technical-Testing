#Author: Cameron Liddell
#Date: 12/11/19
#Group: Yr12
#Title: Starter

#Negative Indexing
a = [1, 2, 3, 4, 5]

print("Negative Indexing,", a[-1])

#Unpacking
a, *b, c = [1, 2, 3, 4, 5]

print("Unpacking,", a, b, c)
print("Unpacking,", b[-1])

#Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Slicing,", a[::5])
