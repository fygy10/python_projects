#Tkinter: graphic user interface, corss-platform interfaces; fairly fast and easy to learn

import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'User'}")

#create the main window
root = tk.Tk()
root.title('Title')

#creates a 'greet' button that prints 'hello world' when pressed following the greet() above
greet_button = ttk.Button(root, text = "Greet", command = greet)
greet_button.pack(side = 'left', fill = 'x', expand = True)

#creates a 'quit' button that quits the program when presses
quit_button = ttk.Button(root, text = "Quit", command = root.destroy)
quit_button.pack(side = 'left', fill = 'x', expand = True)

#user input below returned in greet() with f-string, print, and .get()
user_name = tk.StringVar()

#input fields for user
name_label = ttk.Label(root, text = 'Name: ')
name_label.pack(side = 'left', padx = (0, 10))
name_entry = ttk.Entry(root, width = 15, textvariable = user_name)
name_entry.pack(side = 'left')
name_entry.focus()


root.mainloop()

