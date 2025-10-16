# random_password_generator.py
# Author: Mahvil
# Description: A simple Python script to generate random secure passwords.

import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Random Password Generator 🔐")
    try:
        length = int(input("Enter desired password length (default is 12): ") or 12)
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"\nYour random password is: {password}\n")
    except ValueError:
        print("Please enter a valid number.")
