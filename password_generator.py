# Write a program to generate a random password with a specified length, 
# containing a mix of letters, numbers, and special characters.
import random
import string

def password_generator(count):
    password = ''
    for i in range(count):
        choice = random.randint(0,4) 
        if choice == 0 or choice == 3:
            password += random.choice(string.digits)
        elif choice == 1 or choice == 4:
            password += random.choice(string.ascii_letters)
        elif choice == 2:
            password += random.choice(string.punctuation)
    return password

print(password_generator(15))