
#=======import and setup========
from time import strftime
from tkinter import Label, Tk
import sys
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#======= Configuring window =========
window = Tk()
window.title("time")
window.geometry("800x480+80+0")
window.attributes("-fullscreen", False)
window.resizable(True, True)
#=========text info===========
clock_label = Label(window,bg="black", fg="white", font = ("calibri", 148, 'bold'), relief='flat')
clock_label.place(x = 0, y = 0)
window.overrideredirect(True)

#=========displaying time========
def update_label():
    current_time = strftime('%H: %M')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)
#============main==============

update_label()
window.mainloop()

