#Password Generator

import random as rd
import string as st

while True:
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


    def reg(lin):
        lin = lin.lower()
        lin = lin.strip()
        return lin


    #Generate a password
    gen_password = generate_password()
    print("Password:", gen_password)

    on = input("Press 'G' to generate another password or press any other key to terminate.\n_")
    reg(on)
    if on == "g":
        continue
    else:
        break
