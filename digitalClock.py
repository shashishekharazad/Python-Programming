from tkinter import *
from tkinter.ttk import *
from time import strftime

master = Tk()
master.title("Digital Clock")

def time():
    timefrmt = strftime('%H:%M:%S %p')
    label.config(text = timefrmt)
    label.after(1000,time)

label = Label(master, font = ("Times New Roman", 38, 'bold'),
    background = "brown", foreground = "white")
button = Button(master, text = "Close Clock", width = 50,
    command = master.destroy)
label.pack()
button.pack()
time()

mainloop()


                                                                                    
