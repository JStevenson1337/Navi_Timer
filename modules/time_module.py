#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module containing functions related to the timer
'''
import time
import datetime

class Current_dt():
    '''Stores the current time and current date'''
    def __init__(self):
        self.current = datetime.datetime.now()
        self.one_year = self.current + datetime.timedelta(days = 365)

t1 = Current_dt()

print("Current Time: " + t1.current)

# Create class that acts as a countdown
def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
 
# Inputs for hours, minutes, seconds on timer
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))