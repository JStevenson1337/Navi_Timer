#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: main.py
Purpose: Main file for the application that will 
be used to run the application and its modules in the  main loop
Author: Jeremy Stevenson < Jeremy Stevenson at protonmail dot com>
License: MIT License
"""

import modules.app_frame as app_frame


try:
    app_frame.app.mainloop()
except ValueError:
    print("Failed to initialize")

if __name__ == "__main__":
    ''' Main loop'''
    app_frame.app.mainloop()
