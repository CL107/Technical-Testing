def decrypt(word_string):

    count = 0
    decrypted = ""

    while count < len(word_string):
        print(count)
        temp = ord(word_string[count])
        temp -= 1
        temp = chr(temp)
        decrypted = decrypted + temp
        
        
        count-=1

    print(decrypted)

def decrypt_enter():    
    
    user = input("What do you want to decrypt: ")  

    decrypt(user)
    
def enter():

#try:
    choice = input("Do you want to encrypt(e) or decrypt(d): ").lower()
    
    if choice == "e":
        encrypt_enter()
    
    elif choice == "d":
        decrypt_enter()
    
    else:
        print("\nInvalid Input\n")
        enter()

#except:
#    print("\nInvalid Input\nError Occurred\n")

enter()