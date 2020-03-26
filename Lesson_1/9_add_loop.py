import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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


# Adding three check buttons
ch_var_1= tk.IntVar()
check_1 = tk.Checkbutton(win, text="Disabled", variable=ch_var_1, state="disabled")
check_1.select()
check_1.grid(column=0, row=4, sticky=tk.W)

ch_var_2= tk.IntVar()
check_2 = tk.Checkbutton(win, text="UnChecked", variable=ch_var_2)
check_2.deselect()
check_2.grid(column=1, row=4, sticky=tk.W)


ch_var_3= tk.IntVar()
check_3 = tk.Checkbutton(win, text="Enabled", variable=ch_var_3)
check_3.select()
check_3.grid(column=2, row=4, sticky=tk.W)

# Add radio button

colors = [
    "Blue", "Gold", "Red"
]

def radio_call():
    radio_sel = radio_val.get()
    win.configure(background=colors[radio_sel])

radio_val = tk.IntVar()
radio_val.set(99)
for col in range(3):
    rad1 = tk.Radiobutton(win, text=colors[col], variable=radio_val, value=col, command=radio_call)
    rad1.grid(column=col, row=5, sticky=tk.W, columnspan=3)


# Add Scroll
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

name_entered.focus()
win.mainloop()