import tkinter as tk  # this contains the basic contents (window- liable - text etc...
# from tkinter import ttk # here all the widgets - once we install ttkbootstrap we can comment it out
import ttkbootstrap as ttk

def convert():
    mile = entry_int.get()
    miles = mile * 1.61
    output_string.set(miles)


window = ttk.Window(themename = 'journal')

window.title(" Bond Python Desktop App ")

window.geometry("600x400")

# using ttk we produce title label and put it inside the window
title_label = ttk.Label(master = window, text = " Miles to Kilometers ", font =' Calibri 24 bold')
title_label.pack()

# using ttk we create an input field and button inside a frame
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)

entry.pack(side = 'left', padx = 10) # now we put the entry inside the frame
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
button.pack(side = 'left') # we put the button inside the frame

# now we need to put the frame altogether inside window object
input_frame.pack(pady = 5)

# we need output label to send the result to
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                         text = 'Output',
                         font = 'Calibri 24',
                         textvariable=output_string)
output_label.pack(pady = 5)

'''
Before we run any Tkinter application, we need to call the mainloop() method. 
If you know the C language, it is like calling the main() program in C. 
This main program executes everything that we’ve written above it. Let’s call the mainloop().
'''

window.mainloop()