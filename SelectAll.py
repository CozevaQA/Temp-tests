import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

def select_all():
    if select_var.get() == 1:
        #one.configure(state="enabled")
        one.invoke()
        #two.configure(state="enabled")
        two.invoke()
        #three.configure(state="enabled")
        three.invoke()
    elif select_var.get() == 0:
        #one.configure(state="disabled")
        one.invoke()
        #two.configure(state="disabled")
        two.invoke()
        #three.configure(state="disabled")
        three.invoke()


style = ttk.Style(root)
style.configure("TButton", foreground="red", background="blue")

#checkbox widgets
select_var = tk.IntVar()
select = ttk.Checkbutton(root, text="Select All", variable=select_var, command=select_all)
one_var = tk.IntVar()
one = ttk.Checkbutton(root, text="One", variable=one_var)
two_var = tk.IntVar()
two = ttk.Checkbutton(root, text="Two", variable=two_var)
three_var = tk.IntVar()
three = ttk.Checkbutton(root, text="Three", variable=three_var)
button1 = ttk.Button(root, text="Click me!")

style.configure('TButton', font=('Helvetica', 100))


#packing
select.pack()
one.pack()
two.pack()
three.pack()
# one.configure(state="disabled")
# two.configure(state="disabled")
# three.configure(state="disabled")
button1.pack()















root.title("Cozeva Production Verification")
#root.iconbitmap("assets/icon.ico")
#root.geometry("400x400")
root.mainloop()

