#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):
    '''Application object that can be used to interact with the application'''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''Creates the widgets for the application'''
        self.quit_button = tk.Button(self, text='Quit',
            command=self.quit)
        self.quit_button.grid()
        self.start_button = tk.Button(self, text='Start',fg='black', bg='green', font=("Helvetica", 20))
        self.start_button.grid()

app = Application()
app.master.title('Timer Application')
app.master.geometry('800x800+10+20')
main_label = tk.Label(app, text='Timer', font=('Helvetica', 30))
main_label.place(x=400, y=20)
app.mainloop()
