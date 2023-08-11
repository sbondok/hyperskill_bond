import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Auto typing')
window.geometry('500x300')

entry_var = tk.StringVar(value="Default")

def btn_func():
   entry_var.set("")

entry = ttk.Entry(master=window, textvariable=entry_var)
entry.pack()

lable = ttk.Label(master=window, text="Some text", textvariable=entry_var)
lable.pack()

string_var = tk.StringVar(value="I will clear every thing")
button = ttk.Button(window, text='Button', command=btn_func, textvariable=string_var)
button.pack()

lable_2 = ttk.Label(window, text="==============================")
lable_2.pack()

check_var = tk.BooleanVar()
check_btn = ttk.Checkbutton(window,
                            text='Check Button1',
                            command=lambda :print(check_var.get()),
                            variable=check_var,
                            )
check_btn.pack()
window.mainloop()
