# Password Authenticator

import random as rd
import string as st
import time as tm
import os


def generate_password():
    # Uppercase letters
    uppercase_letters = ''.join(rd.choice(st.ascii_uppercase) for _ in range(3))

    # Lowercase letters
    lowercase_letters = ''.join(rd.choice(st.ascii_lowercase) for _ in range(3))

    # Digits
    digits = ''.join(rd.choice(st.digits) for _ in range(3))

    # Symbols
    symbols = ''.join(rd.choice(st.punctuation) for _ in range(3))

    # Combine and shuffle
    gen_password = list(uppercase_letters + lowercase_letters + digits + symbols)
    rd.shuffle(gen_password)

    return ''.join(gen_password)


def input_password():
    i_password = input("Enter password: ")
    return i_password


def reg(lin):
    lin = lin.lower()
    lin = lin.strip()
    return lin


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def msg():
    print("Copy the password")


# Get Password
get_password = input("Do you want to generate password? \nYes/No:")
get_password = reg(get_password)

while True:
    if get_password == "yes":
        gen_password = generate_password()
        print(gen_password)
        tm.sleep(5)
        clear_console()
        msg()
        authenticator = input("Paste it here:")
        if authenticator == gen_password:
            print("Password authenticated 👍")
        else:
            print("Password mismatch 👎\nTry again")
        break
    elif get_password == "no":
        in_password = input_password()
        print(in_password)
        tm.sleep(2)
        clear_console()
        msg()
        authenticator = input("Paste it here:")
        if authenticator == in_password:
            print("Password authenticated 👍")
        else:
            print("Password mismatch 👎\nTry again")
        break
    else:
        print("Invalid prompt, please enter 'yes' or 'no'")
        get_password = input("Do you want to generate password? \nYes/No: ")
        get_password = reg(get_password)
