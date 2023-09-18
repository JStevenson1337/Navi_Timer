
"""
    Name: main.py
    Purpose: Main file for the application that will 
    be used to run the application and its modules in the  main loop
    Author: Jeremy Stevenson < Jeremy Stevenson at protonmail dot com>
    License: MIT License
"""
import sys
import tkinter as tk
import time
# import datetime


APP_COMMENT = '''
    Module that provides information about the current state of the application
'''
class Application(tk.Frame):
    '''Application object that can be used to interact with the application'''
    def __init__(self, master='None'):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()


        # Label widget
        self.label = tk.Label(text="", fg="Black", font=("Helvetica", 20))
        self.label.pack(side='top', fill='none')
        self.main_label = tk.Label(text='Line Timer', font=('Helvetica', 50, 'bold', 'underline'), justify='center', fg='black', activebackground='black', activeforeground='white', bg='white')
        self.main_label.pack(side='top', fill='none', expand='true')

        # Function instantiations
        self.create_pw()
        # self.start_timer()
        self.create_widgets()
        self.create_buttons()
        self.update_clock()

    # Create widgets function
    def create_widgets(self):
        '''Creates the widgets for the application'''

        # creating a Fra, e which can expand according
        # to the size of the window
        pane = tk.Frame(self.master)
        pane.pack(fill = 'none', expand = 'True')

        # button widgets which can also expand and fill
        # in the parent widget entirely

        # Start button
        start_button = tk.Button(pane, text = "Start",
                    background = "green", fg = "white", font=("Helvetica", 20) )
        start_button.pack(side = 'left', expand = 'true', fill = 'none', padx=10, pady=10)

        # Pause/Resume button
        pause_button = tk.Button(pane, text = "pause/resume",
                    background = "blue", fg = "white", font=("Helvetica", 20))
        pause_button.pack(side = 'left', expand = 'true', fill = 'none', padx=10, pady=10)

        # Stop button
        stop_button = tk.Button(pane, text = "Stop",
                    background = "red", fg = "white", font=("Helvetica", 20))
        stop_button.pack(side = 'left', expand = "true", fill = 'none', padx=10, pady=10)

        # Exit button
        exit_button = tk.Button(pane, text = "Exit",
                    background = "black", fg = "white", font=("Helvetica", 20), command=self.exit_program)
        exit_button.pack(side = 'left', expand = 'true', fill = 'none', padx=10, pady=10)

    # Create buttons function
    def create_buttons(self):
        '''Creates the buttons for the application'''
        # Menu bar
        menu = tk.Menu(self)
        self.master.config(menu=menu)

        # File menu
        file_menu = tk.Menu(menu)
        file_menu.add_command(label="Item")
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menu)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = tk.Menu(menu)
        help_menu.add_command(label="About")
        menu.add_cascade(label="Help", menu=help_menu)

    # Create PanedWindow
    def create_pw(self):
        '''Creates the PanedWindow for the application'''
        # panedwindow object
        pw = tk.PanedWindow(orient ='vertical')

        # Button widget
        top = tk.Button(pw, text ="Click Me !")
        top.pack(side = 'top')

        # This will add button widget to the panedwindow
        pw.add(top)

        # Checkbutton Widget
        bot = tk.Checkbutton(pw, text ="Choose Me !")
        bot.pack(side = 'top')

        # This will add Checkbutton to panedwindow
        pw.add(bot)

        # adding Label widget
        label = tk.Label(pw, text ="I'm a Label")
        label.pack(side = 'top')

        pw.add(label)

        # Tkinter string variable
        string = tk.StringVar()

        # Entry widget with some styling in fonts
        entry = tk.Entry(pw, textvariable = string, font =('arial', 15, 'bold'))
        entry.pack()

        # Focus force is used to focus on particular
        # widget that means widget is already selected for operations
        entry.focus_force()

        pw.add(entry)

        # expand is used so that widgets can expand
        # fill is used to let widgets adjust itself
        # according to the size of main window
        pw.pack(fill = 'both', expand = 'true')

        # This method is used to show sash
        pw.configure(sashrelief ='raised')



    # CLock update function
    def update_clock(self):
        '''Updates the clock on the application'''
        now = time.strftime("%H:%M:%S")
        self.label.configure(text="Current Time: " + now)
        self.after(1000, self.update_clock)

    # Exit program function
    def exit_program(self):
        '''Exits the program'''
        sys.exit()

   # def start_timer(self):
   #     '''Starts the timer'''
   #     while True:
   #         try:
   #             mins, secs = input("Enter the time in minutes and seconds: ").split(":")
   #             mins = int(mins)
   #             secs = int(secs)
   #             break
   #         except ValueError:
   #             print("Error: Please enter the correct format")
   #     timer = mins*60 + secs
   #     while timer > -1:
   #         mins, secs = divmod(timer, 60)
   #         hours, mins = divmod(mins, 60)
   #         timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
   #         print(timeformat, end='\r')
   #         time.sleep(1)
   #         timer -= 1
   #     print("Timer completed!")




class Timer():
    '''Timer object that can be used to interact with the timer'''
    def __init__(self):
        pass


class Station():
    '''IPV_Station object that can be used to interact with the IPV_Station'''
    def __init__(self):
        pass





root = tk.Tk()
app = Application(root)
root.title('Timer Application')
root.geometry('500x500+10+20')
root.after(1000, app.update_clock)
app.mainloop()


















# Main loop for the application



if  __name__ == '__main__':
    Application()
    Timer()
    Station()

















