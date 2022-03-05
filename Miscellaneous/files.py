# Author: Cameron Liddell
# Date: 25/02/20
# Class: 12B/CS

filename = "Write_sample.txt"
mode = "w"

with open(filename, mode) as fh:
    fh.write("Cameron\n")
    fh.write("Matthias\n")

mode = "a"

with open(filename, mode) as fh:
    fh.write("Ethan\n") 
    fh.write("Girvan")

mode = "r"

with open(filename, mode) as fh:
    yeet = fh.read().split("\n")[0]
    print (yeet)
