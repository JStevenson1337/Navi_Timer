#!/usr/bin/env python3
'''A Simple Timer implementation.'''
from tkinter import *
import time
import datetime


current = datetime.datetime.now()
print ("Current date:", str(current))
one_year = current + datetime.timedelta(days = 365)
print("The date in one year:", str(one_year))


root = Tk()

# 
# window.title('Timer')
# window.geometry('800x800+10+20')
# 
# main_label = Label(window, text='Timer', font=('Helvetica', 30))
# main_label.place(x=400, y=20)
# start_button = Button(window, text='Start', fg='black', bg='green', font=("Helvetica", 20))
# start_button.place(x=20, y=700)
# 
# pause_button = Button(window, text='Pause/Resume', fg='black', bg='blue', font=
# ("Helvetica", 20))
# pause_button.place(x=200, y=700)
# 
# stop_button = Button(window, text='Stop', fg='black', bg='red', font=("Helvetica", 20))
# stop_button.place(x=600, y=700)

class TimerApp(root.Frame):
    '''Superclass for the main timer application '''
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


nav_app = TimerApp()

nav_app.master.title("Timer Application")
nav_app.master.maxsize(1000, 1000)
main_label = nav_app.master.Label("Timer Application")


nav_app.mainloop()
