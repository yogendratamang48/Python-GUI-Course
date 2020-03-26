import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# win.resizable(0, 0)

lbl_click = ttk.Label(win, text="Enter text")
lbl_click.grid(column=0, row=0)

def click_me():
    action.configure(text="** Hello **" + name.get())

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click me", command=click_me)
action.grid(column=1, row=1)
action.configure(state="disabled")

name_entered.focus()
win.mainloop()