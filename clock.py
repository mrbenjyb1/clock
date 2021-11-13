#miror screen project

import matplotlib
matplotlib.use('Agg')

from time import strftime
from Tkinter import Label, Tk

#======= Configuring window =========
window = Tk()
window.title("time")
window.geometry("800x480+80+0")
window.attributes("-alpha", "0")
window.resizable(False, False)
#=========text info===========
clock_label = Label(window,bg="silver", fg="white", font = ("calibri", 148, 'bold'), relief='flat')
clock_label.place(x = 0, y = 0)
window.overrideredirect(True)


#=========displaying time========
def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()


