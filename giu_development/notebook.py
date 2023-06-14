import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

#notebook with multiple tabs
#text area within each of the tabs


#check contents for unsaved changes
text_contents = dict()  #puts text into a dictionary

def check_changes():
    current  = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    #reflected in the notebook title once start type or nothing in the text field if changes have been made
    if hash(content) != text_contents[str(current)]:    #if the file is unsaved
        if name[-1] != "*": #if the name doesn't end in an '*'; common practice in tect editors if unsaved
            notebook.tab('current', text = name + '*') 
    elif name[-1] == "*":   
        notebook.tab('current', text = name[:-1])



#function for the current text_widget not saved and what current typing in
#extracted into own function from 'save_file()'
def get_text_widget():
    text_widget = notebook.nametowidget(notebook.select())
    # text_widget = current_tab.winfo_children()    #goes into 'Frame' below and get the children and first one which is 'text_area'
    return text_widget


def close_current_tab():
    current = get_text_widget()
    if current_tab_unsaved() and not confirm_close():
        return
        
    #creates a new tab when the previous open tab is closed
    if len(notebook.tabs()) == 1:
        create_file()

    notebook.forget(current)


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message = "You have unsaved changes. Are you sure you want to quit?",
        icon = "question",
        title = "Unsaved Changes")



def confirm_quit():
    unsaved = False     #begins by assuming everything is saved

    for tab in notebook.tabs():     #cycles through tabs
        text_widget = root.nametowidget(tab) 
        # text_widget = tab_widget.winfo_children()[0]    
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:    #if there is a file that has content that does not match what is saved
            unsaved = True
            break

    if unsaved and not confirm_close():     #asks if user wants to save
        return
            

    # if not confirm: #confirm if don't want to quit, then return nothing
    #         return
            
    root.destroy()  #confirm yes ends the program


#creats a new notebook area when opened and 'new' selected from the menu bar
def create_file(content = "", title = "Untitled"): #default parameters until specified from open saved files
    text_area = tk.Text(notebook)

    text_area.insert("end", content)
    text_area.pack(fill = 'both', expand = True)     #pused to left to make room for the cscroll bar

    notebook.add(text_area, text = title)
    notebook.select(text_area) 

    text_contents[str(text_area)] = hash(content)    #hash: turn data of arbitrary length into data of a specific length

    # #scroll bar movement makes text area move and vice versa
    # text_scroll = ttk.Scrollbar(container, orient = 'vertical', command = text_area.yview)
    # text_scroll.pack(side = 'right', fill = 'y')
    # text_area["yscrollcommand"] = text_scroll.set 


def open_file():
    file_path = filedialog.askopenfilename()
    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file:
            content = file.read()   #not ideal for very long files
    
    except (AttributeError, FileNotFoundError):
        print("Open file failed")
        return
    
    create_file(content, filename)


def save_file():
    file_path = filedialog.asksaveasfilename()  #asks where do you want to save
    try: 
        filename = os.path.basename(file_path)  #saves to file path user gives
        text_widget = get_text_widget()
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, 'w') as file:  #writes the contents of the file into it
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation failed; not a .txt file")
        return 
    
    notebook.tab('current', text = filename)    #updates the tab to show it as it was saved
    text_contents[str(text_widget)] = hash(content)



def show_about_info():
    messagebox.showinfo(
        title = "About",
        message = "Helpng with text editing"
    )


root = tk.Tk()
root.title("My Notebook")
root.option_add("*tearOff", False) #keeps menu options attached to the application window

#format for the notebook
main = ttk.Frame(root)
main.pack(fill = 'both', expand = True, padx = 1, pady = (4, 0))

#creates a menu bar
menu_bar = tk.Menu(root)
root.config(menu = menu_bar)

#adds options to the menu bar
file_menu = tk.Menu(menu_bar)
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(menu = file_menu, label = 'File')
menu_bar.add_cascade(menu = help_menu, label = 'Help')


file_menu.add_command(label = 'New', command = create_file, accelerator = 'Cmd + n')
file_menu.add_command(label = 'Save', command = save_file, accelerator = 'Cmd + s')
file_menu.add_command(label = 'Open...', command = open_file, accelerator = 'Cmd + o')
file_menu.add_command(label = 'Close Tab', command = close_current_tab, accelerator = 'Cmd + t')
file_menu.add_command(label = 'Quit', command = confirm_quit)

help_menu.add_command(label = 'About', command = show_about_info)



notebook = ttk.Notebook(main)
notebook.pack(fill = 'both', expand = True)
create_file()

#for Mac keyboard shortcuts
root.bind("<Command - n>", lambda event: create_file())
root.bind("<Command - s>", lambda event: save_file())
root.bind("<Command - o>", lambda event: open_file()) 
root.bind("<KeyPress>", lambda event: check_changes())
root.bind("<Command - q>", lambda event: close_current_tab())


root.mainloop()