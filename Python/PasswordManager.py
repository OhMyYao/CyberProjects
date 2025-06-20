import hashlib
import getpass

password_manager = {}

def account():
    username = input("Enter your desired username: ")
    #hides the password being entered
    passwd = getpass.getpass("Enter your desired password: ")
    #Store the password as a hash. Make sure it's converted to bytes so hashlib can read it
    hashedpass = hashlib.sha256(passwd.encode()).hexdigest()
    #store the username and password as a pair
    password_manager[username] = hashedpass
    print("Account created Sucessfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashedpass = hashlib.sha256(password.encode()).hexdigest()
    #checks if the username and hash of the input password is in the dictionary and if the has matches
    if username in password_manager.keys() and hashedpass == password_manager[username]:
        print("Login successful!")
        return 0
    else:
        print("Invalid username or password")
        return 1
    
def main():
    print("Welcome to the password manager.\nHere are your options. Enter 1 to create account, Enter 2 to login, or Enter 0 to quit.")
    while True:        
        choice = input("Please enter your choice from the menu:")
        if choice == "1":
            account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()