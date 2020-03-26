import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# win.resizable(0, 0)

lbl_click = ttk.Label(win, text="A label")
lbl_click.grid(column=0, row=0)

def click_me():
    action.configure(text="** I have been cliecked! **")
    lbl_click.configure(foreground='red')
    lbl_click.configure(text="A Red Label")


action = ttk.Button(win, text="Click me", command=click_me)
action.grid(column=1, row=0)
win.mainloop()