import os
path = os.getcwd()
for i in range(1, 1000000000000):
    os.mkdir(path + f"\\{i}")