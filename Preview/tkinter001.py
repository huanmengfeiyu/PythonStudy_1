from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup',message='Button pressed!')

window=Tk()
button=Button(window,text='press',command=reply)
button.pack()
Label(window, text='Spam').pack()
window.mainloop()