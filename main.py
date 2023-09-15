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
import tkinter as tk
import time, datetime


app_frame_comment = '''
    Module that provides information about the current state of the application
'''
class Application(tk.Frame):
    '''Application object that can be used to interact with the application'''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.create_buttons()

    def create_widgets(self):
        '''Creates the widgets for the application'''
        self.quit_button = tk.Button(self, text='Quit',
            command=self.quit)
        self.quit_button.grid(column=4, row=4)

    def create_buttons(self):
        '''Creates the buttons for the application'''
        self.start_button = tk.Button(self, text='Start',fg='black', 
bg='green', font=("Helvetica", 20))
        self.start_button.grid(column=0, row=4)
        self.pause_button = tk.Button(self, text='Pause/Resume',fg='black', 
bg='blue', font=("Helvetica", 20))
        self.pause_button.grid(column=2, row=4)
        self.stop_button = tk.Button(self, text='Stop',fg='black', bg='red', 
font=("Helvetica", 20))
        self.stop_button.grid(column=3, row=4)

app = Application()
app.master.title('Timer Application')
# app.master.geometry('800x800+10+20')
main_label = tk.Label(app, text='Timer', font=('Helvetica', 30))
main_label.place(x=400, y=20)
app.mainloop()
