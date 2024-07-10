import string
import random

chars = string.digits + string.ascii_letters + string.punctuation
password = "".join([random.choice(chars) for _ in range(10)])
print(f"This is your generated password {password}")
