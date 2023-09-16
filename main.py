#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: main.py
Purpose: Main file for the application that will 
be used to run the application and its modules in the  main loop
Author: Jeremy Stevenson < Jeremy Stevenson at protonmail dot com>
License: MIT License
"""
import sys, os
from tkinter import *
import time, datetime


APP_COMMENT = '''
    Module that provides information about the current state of the application
'''
class Application(Frame):
    '''Application object that can be used to interact with the application'''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.grid(column=3, row=3, columnspan=3)
        self.grid()
        self.create_widgets()
        self.create_buttons()
        self.update_clock()

    def create_widgets(self):
        '''Creates the widgets for the application'''

    def create_buttons(self):
        '''Creates the buttons for the application'''
        # Start button
        self.start_button = Button(self, text='Start',fg='black',        bg='green', font=("Helvetica", 20))
        self.start_button.grid(column=0, row=4)
        # Pause/Resume button
        self.pause_button = Button(self, text='Pause/Resume',fg='black', bg='blue', font=("Helvetica", 20))
        self.pause_button.grid(column=2, row=4)
        # Stop button
        self.stop_button = Button(self, text='Stop',fg='black', bg='red', font=("Helvetica", 20))
        self.stop_button.grid(column=3, row=4)
        # Exit button
        self.quit_button = Button(self, text='Quit',
        command=self.quit)
        self.quit_button.grid(column=4, row=4)
        
        # Menu bar
        menu = Menu(self)
        self.master.config(menu=menu)
        
        file_menu = Menu(menu)
        file_menu.add_command(label="Item")
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=edit_menu)

        help_menu = Menu(menu)
        help_menu.add_command(label="About")
        menu.add_cascade(label="Help", menu=help_menu)

    # CLock update function
    def update_clock(self):
        '''Updates the clock on the application'''
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def exit_program(self):
        '''Exits the program'''
        sys.exit()





class Timer():
    '''Timer object that can be used to interact with the timer'''
    def __init__(self):
        pass

class Station():
    '''IPV_Station object that can be used to interact with the IPV_Station'''
    def __init__(self):
        pass




root = Tk()
app = Application(root)
root.title('Timer Application')
# app.master.geometry('800x800+10+20')
main_label = Label(app, text='Timer', font=('Helvetica', 30, 'bold', 'underline' ))
main_label.grid(column=3, row=1, columnspan=7)
root.maxsize(1000, 1000)
root.minsize(700, 700)
root.after(1000, app.update_clock)




















# Main loop for the application
app.mainloop()


