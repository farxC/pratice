from tkinter import *

root = Tk()

root.geometry('300x300')
def submit():
    a = nameEntry.get()
    print(a)
nameEntry = Entry(root, text='Insira o texto')
nameEntry.pack()

btn = Button(root, text='Insira',command= submit).pack()


root.mainloop()