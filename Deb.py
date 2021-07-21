import os
import random
import string
path = os.getcwd()
for i in range(1, 10123):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all = lower + digits
    length = 16
    name = "".join(random.sample(all, length))
    os.mkdir(path + f"\\{name}")