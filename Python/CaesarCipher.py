import string

def encrypt(message, key):
    shift = key % 26
    #shifts the alphabet by 'shift' number of spaces.
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    #translates the message with the cipher
    encrypted = message.lower().translate(cipher)
    return encrypted

def decrypt(encrypted_message, key):
    #essentially doing the opposite of the encrypt function
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    #using this opposite key to decrypt the message
    decrypted = encrypted_message.translate(cipher)
    return decrypted

#selection menu to encrypt or decrypt a message
def main():
    print("Would you like to encrypt or decrypt a message?")
    select = input("Press 1 to encrypt or 2 to decrypt.")
    if select == "1":
        message = input("What is your message: \n")
        while True:
            key = int(input("Select a number from 1 to 26: "))
            if 1 <= key <= 26:
                break
            else:
                print("Please select a number between 1 and 26")
        encrypted_message = encrypt(message, key)
        print(encrypted_message)
    elif select == "2":
        message = input("What is the encrypted message: \n")
        while True:
            key = int(input("What is the key?\n"))
            if 1 <= key <= 26:
                break
            else:
                print("The Key should be between 1 and 26")
        decrypted_message = decrypt(message, key)
        print(decrypted_message)
    
if __name__ == "__main__":
    main()