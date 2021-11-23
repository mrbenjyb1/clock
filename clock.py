#=======import and setup========
from time import strftime
from tkinter import Label, Tk
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt

#======= Configuring window =========
window = Tk()
window.title("time")
window.geometry("800x480+80+0")
window.attributes("-fullscreen", True)
window.resizable(False, False)
#=========text info===========
clock_label = Label(window,bg="black", fg="white", font = ("calibri", 148, 'bold'), relief='flat')
clock_label.place(x = 0, y = 0)
window.overrideredirect(True)

#=========displaying time========
def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)
#============main==============

update_label()
window.mainloop()


