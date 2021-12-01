

#=======import and setup========
from time import strftime
from tkinter import Label, Tk
import sys
import os
if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

#======= Configuring window =========
window = Tk()
window.title("time")
window.geometry("800x480+0+0")
window.attributes("-fullscreen", False)
window.configure(bg="black")
window.resizable(True, True)
#=========text info===========
clock_label = Label(window,bg="black", fg="white", font = ("calibri", 100, 'bold'), relief='flat')
clock_label.place(x = 0, y = 0)
window.overrideredirect(True)

date1_label = Label(window,bg="black", fg="white", font = ("calibri", 40, 'bold'), relief='flat')
date1_label.place(x = 15, y = 150)
window.overrideredirect(True)

#=========displaying time & date========
def update_label():
    current_time = strftime('%H: %M')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

def date_label():
    from datetime import date
    today=date.today()
    date=today.strftime('%d / %m / %Y')
    date1_label.configure(text = date)
    date1_label.after(1000, date_label)

#============main==============

date_label()
update_label()
window.mainloop()
