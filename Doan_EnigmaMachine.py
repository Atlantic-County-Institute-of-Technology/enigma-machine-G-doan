# Author: Gavin Doan
# Description: To encrypt using a rotational cipher
# Created: 11.19.25
# Last Updated: 11.24.25


# Used Imports
import os
import inquirer3


def set_key(msg):  # Function to se the key length equal to the msg length
    key = input("Please enter a Key: ")
    key_fixed = ""
    j = -1  # Separate counter for the message so it skips spaces correctly
    if len(msg) == len(key):  # Returns if the length is already the same
        return key
    else:  # If key length isn't same length
        for i in range(len(msg)):
            if msg[i].isalpha():  # Checks to see if character is alphabetical
                j += 1  # Adds one to move on to next character in msg(if it is alphabetical)
                key_fixed += (key[j % len(key)])
            else:
                key_fixed += (msg[i])  # adds on the letter to the end of the key
    return key_fixed


def encrypt_vigenere(msg):  # Function for the Encryption using vigenere cipher
    encrypted_text = ""
    key = set_key(msg)
    for i in range(len(msg)):  # for loop to repeat for each character in the string
        if msg[i].isalpha():  # Encrypt only alphabetic characters
            char = msg[i]
            if char.islower():  # If char is lowercase
                start = ord('a')
                shift = ord(key[i].lower())
            else:  # if char is uppercase
                start = ord('A')
                shift = ord(key[i].upper())
            shifted_char_code = (ord(char) + shift - 2 * start) % 26 + start
            encrypted_text += chr(shifted_char_code)  # To add the encrypted to encrypted_text
        else:  # To Keep non-alphabetic characters as they are
            encrypted_text += msg[i]  # To add the non-alphabetic characters back to the string
    return encrypted_text


def decrypt_vigenere(msg):  # Function for the Encryption using vigenere cipher
    decrypted_text = ""
    key = set_key(msg)
    for i in range(len(msg)):  # for loop to repeat for each character in the string
        if msg[i].isalpha():  # Decrypt only alphabetic characters
            char = msg[i]
            if char.islower():  # If char is lowercase
                start = ord('a')
                shift = ord(key[i].lower())
            else:  # if char is uppercase
                start = ord('A')
                shift = ord(key[i].upper())
            shifted_char_code = ((ord(char) - start) - (shift - start)) % 26 + start
            decrypted_text += chr(shifted_char_code)  # To add the decrypted to decrypted_text
        else:  # To Keep non-alphabetic characters as they are
            decrypted_text += msg[i]  # To add the non-alphabetic characters back to the string
    return decrypted_text


def write_file(message):
    # Inquirer Menu options for writing it to a file
    questions2 = [
        inquirer3.List('menu',
                       message="Do you want to Overwrite or make a New file?",

                       choices=['Overwrite File', 'New File', 'Do Not Save'])
    ]
    answers = inquirer3.prompt(questions2)
    select2 = "{}".format(answers['menu'])

    match select2:
        case "Overwrite File":
            filename = input("\nWhat file do you want to Overwrite:") + ".txt"
        case "New File":
            filename = input("\n Enter new filename:")
            filename = filename + ".txt"
        case "Do Not Save":
            return
    try:
        # Adds the message to the file
        with open(filename, 'w') as file:
            file.write(message)
        print(f"[✓] Message successfully written to '{filename}'.\n")

    except Exception as e:
        # if there is any issue, error out
        print(f"\n[!] Error writing to file: {e}\n")


# read the contents of a file (if it exists).
def read_file():
    # in this context we need to include the file extension (ex: 'hello.txt)
    filename = input("[-] Please enter the filename to read: ") + ".txt"

    try:
        # attempt to read the contents of the file
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"[-] Contents of '{filename}':")
            # contents is stored as a string, so we can just throw it to print
            print(f"Contents: {contents}\n")

    except FileNotFoundError:
        # we account for FNF since it's the most likely issue
        print(f"\n[!] Error: File '{filename}' not found.\n"
              f"\n[?] Did you make sure to enter the filename correctly?\n")
        # general error case in the event the file is corrupted or gets deleted mid-read
    except Exception as e:
        print(f"[!] Error reading file '{filename}': {e}\n")


def main():
    while True:

        # Inquirer Menu options
        questions = [
            inquirer3.List('menu',
                           message="What would you like to do?",

                           choices=['Encrypt Text', 'Decrypt Text', 'Encrypt File', 'Decrypt File', 'Read File', 'Exit'])
        ]
        answers = inquirer3.prompt(questions)
        select = "{}".format(answers['menu'])

        # Code for the choices of the menu
        match select:

            case "Encrypt Text":  # Option to Encrypt Text
                os.system('cls' if os.name == 'nt' else 'clear')  # To clear old text
                message = input("Enter Text: ")  # Input for to be encrypted msg
                encrypted_message = encrypt_vigenere(message)  # Function to encrypt the message
                print(f"Encrypted Text: {encrypted_message} \n")  # Prints the Encrypted Message
                write_file(encrypted_message)

            case "Decrypt Text":  # Option to Decrypt text
                os.system('cls' if os.name == 'nt' else 'clear')  # To clear old text
                message = input("Enter Text: ")  # Input for to be Decrypted msg
                decrypted_message = encrypt_vigenere(message)  # Function to Decrypt the message
                print(f"Encrypted Text: {decrypted_message} \n")  # Prints the Decrypted Message
                write_file(decrypted_message)

            case "Encrypt File":  # Option to Decrypt file
                os.system('cls' if os.name == 'nt' else 'clear')  # To clear old text
                fname = input("What File?: ") + ".txt"

                try:  # try block to make sure file exists
                    with open(fname, 'r') as f:
                        fmsg = f.read()
                        print(f"Text: {fmsg}")  # Prints the content before the Decrypt
                    encrypted_message = encrypt_vigenere(fmsg)
                    print(f"Encrypted File Text: {encrypted_message}")
                    write_file(encrypted_message)

                except FileNotFoundError:
                    print("Error! File Not Found.")

                except Exception as e:
                    print(f"Error: {e}")

            case "Decrypt File":  # Option to Decrypt file
                os.system('cls' if os.name == 'nt' else 'clear')  # To clear old text
                fname = input("What File?: ") + ".txt"

                try:  # try block to make sure file exists
                    with open(fname, 'r') as f:
                        print(f.read())
                        fmsg = f.read()
                        print(f"Text: {fmsg}")  # Prints the content before the Decrypt
                    decrypted_message = decrypt_vigenere(fmsg)
                    print(f"Decrypted File Text: {decrypted_message}")
                    write_file(decrypted_message)

                except FileNotFoundError:
                    print("Error! File Not Found.\n")

                except Exception as e:
                    print(f"Error: {e}")

            case "Read File":  # Option to read File
                os.system('cls' if os.name == 'nt' else 'clear')  # To clear old text
                read_file()

            case "Exit":
                exit()


if __name__ == "__main__":
    main()
