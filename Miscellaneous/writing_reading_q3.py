import re

lojban = {

    "pa": 1,
    "re": 2,
    "ci": 3,
    "vo": 4,
    "mu": 5,
    "xa": 6,
    "ze": 7,
    "bi": 8,
    "so": 9,
    "no": 0

}

user = input("Enter a string in lojban: ")

split = re.findall('.{1,2}', user)

lojbannum = []
j = 0
y = 0

for x in split: 
    
    while y < len(split) - 1:
        
        temp = split[j]
        j += 1
        print(temp)


print (lojbannum)

