import time
import datetime

# seconds = time.time()
# print("Time in seconds since the epoch:", seconds)
# local_time = time.ctime(seconds)
# print("Local time:", local_time)
# 
# print("This is the start of the program.")
# time.sleep(5)
# print("This prints five seconds later.")



 
current = datetime.datetime.now()
print ("Current date:", str(current))
one_year = current + datetime.timedelta(days = 365)
print("The date in one year:", str(one_year))


## Timer starts
# starttime = time.time()
# lasttime = starttime
# lapnum = 1
# value = ""
#   
# print("Press ENTER for each lap.\nType Q and press ENTER to stop.")
#   
# while value.lower() != "q":
#               
#     # Input for the ENTER key press
#     value = input()
#   
#     # The current lap-time
#     laptime = round((time.time() - lasttime), 2)
#   
#     # Total time elapsed since the timer started
#     totaltime = round((time.time() - starttime), 2)
#   
#     # Printing the lap number, lap-time, and total time
#     print("Lap No. "+str(lapnum))
#     print("Total Time: "+str(totaltime))
#     print("Lap Time: "+str(laptime))
#             
#     print("*"*20)
#   
#     # Updating the previous total time and lap number
#     lasttime = time.time()
#     lapnum += 1
#   
# print("Exercise complete!")
# 



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