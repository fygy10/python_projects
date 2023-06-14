#pack: place compenents in the container; other methods exist too

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#frame to control certain labels; usually one to be grouped together and not affect other components -> achieve layouts easier
main = ttk.Frame(root)
main.pack(side = 'left', fill = 'both', expand  = True)

#side: where component is 'glued' / 'anchored'
#fill: component fills a determined ampount of space (ex. x axis))
#expand
tk.Label(root, text = 'Label 1', bg = 'green').pack(side = 'left', fill = 'y')  #listed first so it takes priority
tk.Label(root, text = 'Label 2', bg = 'red').pack(side = 'top', fill = 'x')




root.mainloop()