#Author: Cameron Liddell
#Date: 12/11/19
#Group: Yr12
#Title: Functions

#Function to write to a file
import time
from sys import setrecursionlimit
setrecursionlimit(1500)

def write_file(var_text):
    file_object = open('testfile.txt', 'w')
    a = file_object.write(var_text)
    file_object.close()

    return a

def append(userinput):
    file_object = open('testfile.txt', 'a')
    try:
        file_object.write(userinput)

    except:
        pass
    file_object.close()

def read_file():
    fo = open('testfile.txt', 'r')
    a = fo.read(100)
    print ("Read string is: ", a)
    fo.close()


def Stop(count=0):
    if count < 10:
        program = ("You entered an invalid argument, would you like to quit, y/n ?\n").lower()
        if program == "y":
            quit()

        elif program == "n":
            menu()

        else: 
            count += 1
            Stop(count)

    else:
        quit()


def menu():

    choice = input("Would you like to write to the file (w), read it (r), append it (a) or quit (q):\n")
    
    try:
        if choice == "w" or choice == "W":
            
            var_text = input("What would you like to write to the file:\n")

            write_file(var_text)
            read_file()
            time.sleep(2)
            menu()

        elif choice == "r" or choice == "R":
            
            read_file()
            time.sleep(2)
            menu()

        elif choice == "a" or choice == "A":
            
            userinput = input("What would you like to append to the text: ")
            append(userinput)
            read_file()
            time.sleep(2)
            menu()
        
        elif choice == "q" or choice == "Q":
            quit()

        
        
        else:
            print("Invalid Input")
            menu()    

    except:
        Stop()

menu()