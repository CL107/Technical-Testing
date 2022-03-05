import getpass

with open("usernames.txt", "r") as f:
    usernames = f.read().split("\n")

with open("passwords.txt", "r") as j:
    passwords = j.read().split("\n")

class users():
    
    def __init__(self):
        
        self.username = usernames
        self.password = passwords  

obj = users()

success = False

def menu():

    choice = input("Login(1) or Register(2): ")

    if choice == "1":
        login_user(success)
    
    elif choice == "2":
        register()

    else:
        print ("Invalid Input")
        menu()

def login_user(success):

    print ("Enter X at any time to return to the menu")

    User = input("Username: ")

    if User == "X" or User == "x":
        menu()
    
    else:
        pass

    for x in range(0, len(obj.username)):
        if User != obj.username[x]:
            pass
            
        elif User == obj.username[x]:
            success = login_pass(x)
    
    if success == False:
        print ("Invalid username")
        success = login_user(success)


def login_pass(x):

    Pass = getpass.getpass()

    if Pass == "X" or Pass == "x":
        menu()

    else:
        pass    

    if Pass != obj.password[x]:
        print ("Invalid password")
        login_pass(x)
    
    elif Pass == obj.password[x]:
        print(f"Login Successful\nWelcome {obj.username[x]}")
        return True

def register():

    name = input("Pick a username: ")
    passw = input("Pick a password: ")
    usernames.append(name)
    passwords.append(passw)
    
    with open("usernames.txt", "w") as f, open("passwords.txt", "w") as g:
        f.write("\n".join(usernames))
        g.write("\n".join(passwords))

    login_user(success)

menu()
