import string
import random
import sys

characters = string.ascii_letters + string.punctuation  + string.digits
password = ""
password_length = random.randint(8, 16)
for x in range(password_length):
    char = random.choice(characters)
    password = password + char

sys.stdout.write(password)