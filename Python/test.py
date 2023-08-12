import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_dataframe():
    # Load the dataframe (example data)
    data = {'Name': ['John', 'Emily', 'Ryan', 'Sarah'],
            'Age': [25, 30, 35, 28],
            'City': ['New York', 'London', 'Paris', 'Sydney']}
    df = pd.DataFrame(data)
    
    # Create the Tkinter window
    window = tk.Tk()
    window.title("Dataframe Display")
    
    # Create a treeview widget to display the dataframe
    treeview = ttk.Treeview(window)
    treeview["columns"] = list(df.columns)
    
    # Configure the treeview columns
    for column in df.columns:
        treeview.column(column, width=100, anchor=tk.CENTER)
        treeview.heading(column, text=column)
    
    # Insert the dataframe rows into the treeview
    for index, row in df.iterrows():
        treeview.insert("", tk.END, text=index, values=list(row))
    
    # Pack the treeview widget
    treeview.pack(padx=10, pady=10)
    
    # Start the Tkinter main loop
    window.mainloop()

# Call the function to display the dataframe
display_dataframe()
