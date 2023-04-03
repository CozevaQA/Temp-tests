from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style()
style.theme_use('alt')
style.configure('My.TCheckbutton', font=('Helvetica', 13, 'bold'), foreground='Black', background='#5a9c32', padding=15, highlightthickness=0, height=1, width=25)
style.map('My.TCheckbutton', background=[('active', '#72B132')])

# create a label
label = ttk.Label(root, text="Select your choices:")
label.pack()

# create 4 checkboxes
checkbox1 = ttk.Checkbutton(root, text="Option 1", style="My.TCheckbutton")
checkbox2 = ttk.Checkbutton(root, text="Option 2", style="My.TCheckbutton")
checkbox3 = ttk.Checkbutton(root, text="Option 3", style="My.TCheckbutton")
checkbox4 = ttk.Checkbutton(root, text="Option 4", style="My.TCheckbutton")

# pack the checkboxes
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()
checkbox4.pack()

root.mainloop()
