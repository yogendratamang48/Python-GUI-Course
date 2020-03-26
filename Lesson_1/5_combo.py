import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# win.resizable(0, 0)

lbl_click = ttk.Label(win, text="Enter text:")
lbl_click.grid(column=0, row=0)

def click_me():
    action.configure(text="** Hello **" + name.get() + " " + number.get())

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click me", command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
combo_number = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
combo_number['values'] = (1, 2, 4, 42, 100)
combo_number.grid(column=1, row=1)
combo_number.current(0) 
combo_number.focus()
win.mainloop()