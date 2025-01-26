import random
import string

def password_generator(length=12):
    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password

try:
    length = int(input("Enter the desired password length (minimum 6): "))
    password = password_generator(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")