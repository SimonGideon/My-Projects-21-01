"""create a pyhton program that creates a txt file and adds some text into it then with
the same program you print the documentation using the default printer"""



import os
with open("D:\DESKTOP\HandsOnPython\Projects/notes.txt", "w") as f:
    f.write("This is assignment #2")
os.startfile("D:\DESKTOP\HandsOnPython\Projects/notes.txt", 'print')
f.close()
