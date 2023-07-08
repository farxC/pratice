import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# Create the application
myapp= App()

myapp.master.title("Teste")
myapp.master.maxsize(1000,400)

#start
myapp.mainloop()