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
        self.label = Label(text="", fg="Black", font=("Helvetica", 20), justify='left')
        self.label.pack(fill='none', expand=2)
        # self.label.grid(column=0, row=0)
        # self.grid()
        self.create_widgets()
        self.create_buttons()
        self.update_clock()

    def create_widgets(self):
        '''Creates the widgets for the application'''

        # creating a Fra, e which can expand according
        # to the size of the window
        pane = Frame(self.master)
        pane.pack(fill = 'none', expand = True)

        # button widgets which can also expand and fill
        # in the parent widget entirely

        # Start button
        start_button = Button(pane, text = "Start",
                    background = "green", fg = "white", font=("Helvetica", 20) )
        start_button.pack(side = LEFT, expand = True, fill = 'none')

        # Pause/Resume button
        pause_button = Button(pane, text = "pause/resume",
                    background = "blue", fg = "white", font=("Helvetica", 20))
        pause_button.pack(side = LEFT, expand = True, fill = 'none')

        # Stop button
        stop_button = Button(pane, text = "Stop",
                    background = "red", fg = "white", font=("Helvetica", 20))
        stop_button.pack(side = LEFT, expand = True, fill = 'none')

        # Exit button
        exit_button = Button(pane, text = "Exit",
                    background = "black", fg = "white", font=("Helvetica", 20), command=self.exit_program)
        exit_button.pack(side = LEFT, expand = True, fill = 'none')
        


    def create_buttons(self):
        '''Creates the buttons for the application'''
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
main_label = Label(app, text='Timer', font=('Helvetica', 30, 'bold', 'underline'), justify='center', fg='black', bg='white')
main_label.pack(fill='none', expand=2)
# main_label.grid(column=0, row=0)
root.geometry('500x500+10+20')
root.after(1000, app.update_clock)




















# Main loop for the application
app.mainloop()


# if __name__ == '__main__':
#     Application()
#     Timer()
#     Station()



