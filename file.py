import strings
import random

chars = strings.digits + strings.letters
password = "".join([random.choice(chars) for _ in range(10)])
print(f"This is your generated password {password}")
