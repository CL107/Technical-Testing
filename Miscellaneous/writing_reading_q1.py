import re

def remove_vowel(string):
    return(re.sub("[aeiouAEIOUa ]", "", string))

with open("stringexample.txt", "w") as se:
    se.write("Never trust a computer you cannot throw out a window")

with open("stringexample.txt", "r") as se:
    string = se.read()

print (remove_vowel(string))