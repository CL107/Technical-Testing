# Author: Cameron Liddell
# Date: 20/11/19
# Group: 12B/CS
# Title: Caesar Shift
def encrypt(word_string, key):

    count = 0
    encrypted = ""

    while count < len(word_string):
        
        temp = ord(word_string[count])
        temp += key
        temp = chr(temp)
        encrypted = encrypted + temp
        count+=1

    print(f"\nThe encrypted string is: {encrypted}\n")

    end()

def decrypt(word_string, key):

    count = 0
    decrypted = ""

    while count < len(word_string):
        
        temp = ord(word_string[count])
        temp -= key
        temp = chr(temp)
        decrypted = decrypted + temp
        count+=1

    print(f"\nThe decrypted string is: {decrypted}\n")
    
    end()

def decrypt_enter():    
    
    user = input("\nWhat do you want to decrypt: ")  

    key = value_d()

    decrypt(user, key)

def encrypt_enter():    
    
    user = input("\nWhat do you want to encrypt: ")  

    key = value_e()

    encrypt(user, key)

def value_d():

    while True:
        
        try:
            key = int(input("\nWhat is your key: "))
            if key > 60000:
                print("\nKey is too large, must be less than 60,000")
                pass
            else:
                return key
                break
        except:
            print("\nInvalid Input")
            pass

def value_e():

    while True:

        try:
            key = int(input("\nWhat key would you like to use: "))
            if key > 60000:
                print("\nKey is too large, must be less than 60,000")
                pass
            else:
                return key
                break
        except:
            print("\nInvalid Input")
            pass

def end():

    choice = input("Do you want to quit Y/N: ").lower()
    print("")
    
    if choice == "y":
        quit()
    
    elif choice == "n":
        enter()
    
    else:
        end()

def enter():

    while True:
        
        choice = input("Do you want to encrypt(e) or decrypt(d): ").lower()
        
        if choice == "e":
            encrypt_enter()
        
        elif choice == "d":
            decrypt_enter()

        else:
            print("\nInvalid Input\n")
            enter()
        
        enter()

enter()