import random

test = []
x = 0

while x < 20:

    y = random.randrange(1, 100)
    test.append(y)

    x+= 1

for x in range(len(test)):

    for y in range(len(test)):

        if test[x] == test[y]:
            
            test[y].replace(0)

print
    