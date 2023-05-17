import random
import string

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)

print("Your random password is:", password)
