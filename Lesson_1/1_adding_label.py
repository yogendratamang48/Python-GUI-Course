import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# win.resizable(0, 0)

ttk.Label(win, text="A quick brown fox jumps over the lazy dog").grid(column=0, row=0)
win.mainloop()