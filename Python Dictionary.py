# Importing library
from tkinter import *
from PyDictionary import PyDictionary

# Creating an object.
dictionary = PyDictionary()
root = Tk()

# Setting geometry.
root.geometry("400x400")


def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


# Adding frames and labels.
Label(root, text="Dictionary", font="Helvetica 20 bold", fg="Green").pack(pady=10)

# Frame 2
frame = Frame(root)
Label(frame, text="Type word", font="Helvetica 15 bold").pack(side=LEFT)
word = Entry(frame, font="Helvetica 15 bold")
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font="Helvetica 10 bold").pack(side=LEFT)
meaning = Label(frame1, text="", font="Helvetica 10 bold")
meaning.pack()
frame1.pack(pady=10)

# Frame 3
frame2 = Frame(root)
Label(frame2, text="Synonym:- ", font="Helvetica 10 bold").pack(side=LEFT)
synonym = Label(frame2, text="", font="Helvetica 20 bold")
synonym.pack()
frame2.pack(pady=10)

# Frame 4
frame3 = Frame(root)
Label(frame3, text="Antonym:- ", font="Helvetica 10 bold").pack(side=LEFT)
antonym = Label(frame3, text="", font="Helvetica 20 bold")
antonym.pack()
frame3.pack(pady=10)

Button(root, text="Submit", font="Helvetica 15 bold", command=dict).pack()
root.mainloop()
